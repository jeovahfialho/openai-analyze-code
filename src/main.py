from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
import ast

app = FastAPI(title="Python Code Advisor - OpenAI Compatible")

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    temperature: Optional[float] = 1.0
    max_tokens: Optional[int] = None

class ChatChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: str

class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[ChatChoice]
    usage: Dict[str, int]

class CodeAnalyzer:
    def analyze(self, code: str) -> List[Dict[str, str]]:
        suggestions = []
        try:
            tree = ast.parse(code)
            
            # Analisa o código usando visitor pattern
            visitor = CodeVisitor()
            visitor.visit(tree)
            suggestions.extend(visitor.suggestions)
            
            # Análises adicionais
            suggestions.extend(self._check_naming_conventions(code))
            suggestions.extend(self._check_code_complexity(tree))
            
            return suggestions
        except SyntaxError as e:
            return [{"type": "error", "message": f"Erro de sintaxe: {str(e)}"}]
        except Exception as e:
            return [{"type": "error", "message": f"Erro na análise: {str(e)}"}]

    def _check_naming_conventions(self, code: str) -> List[Dict[str, str]]:
        suggestions = []
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Verifica nomes em camelCase ou PascalCase
            if any(char.isupper() for char in line if char.isalnum()):
                suggestions.append({
                    "type": "style",
                    "message": f"Linha {line_num}: Considere usar snake_case para nomes (palavras_separadas_por_underline)"
                })
                
        return suggestions

    def _check_code_complexity(self, tree: ast.AST) -> List[Dict[str, str]]:
        suggestions = []
        
        # Conta funções e classes
        functions = len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
        classes = len([node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)])
        
        if functions > 5:
            suggestions.append({
                "type": "complexity",
                "message": "O código tem muitas funções. Considere dividir em módulos menores."
            })
            
        return suggestions

class CodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.suggestions = []
    
    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Verifica docstring
        if not ast.get_docstring(node):
            self.suggestions.append({
                "type": "documentation",
                "message": f"A função '{node.name}' não possui docstring"
            })
        
        # Verifica número de parâmetros
        if len(node.args.args) > 5:
            self.suggestions.append({
                "type": "complexity",
                "message": f"A função '{node.name}' tem muitos parâmetros. Considere refatorar."
            })
        
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        # Verifica docstring da classe
        if not ast.get_docstring(node):
            self.suggestions.append({
                "type": "documentation",
                "message": f"A classe '{node.name}' não possui docstring"
            })
        
        self.generic_visit(node)

async def process_completion(request: ChatCompletionRequest):
    """Função auxiliar para processar as completions"""
    try:
        # Extrai o código da última mensagem
        last_message = request.messages[-1]
        code = last_message.content
        
        # Analisa o código
        analyzer = CodeAnalyzer()
        suggestions = analyzer.analyze(code)
        
        # Formata a resposta em texto
        response_text = "Análise do Código Python:\n\n"
        
        if not suggestions:
            response_text += "✅ O código parece estar seguindo as boas práticas Python!\n"
        else:
            for suggestion in suggestions:
                prefix = "❌" if suggestion["type"] == "error" else "⚠️"
                response_text += f"{prefix} {suggestion['message']}\n"
        
        response_text += "\nRecomendações Gerais:\n"
        response_text += "- Use nomes descritivos em snake_case\n"
        response_text += "- Adicione docstrings para documentar funções e classes\n"
        response_text += "- Mantenha funções pequenas e focadas\n"
        response_text += "- Siga o PEP 8 (Guia de Estilo Python)\n"
        
        # Cria resposta no formato OpenAI
        response = ChatCompletionResponse(
            id=f"pythoncodereview-{datetime.now().timestamp()}",
            created=int(datetime.now().timestamp()),
            model="python-code-advisor-v1",
            choices=[
                ChatChoice(
                    index=0,
                    message=ChatMessage(
                        role="assistant",
                        content=response_text
                    ),
                    finish_reason="stop"
                )
            ],
            usage={
                "prompt_tokens": len(code),
                "completion_tokens": len(response_text),
                "total_tokens": len(code) + len(response_text)
            }
        )
        
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoints com prefixo v1
@app.post("/v1/chat/completions", response_model=ChatCompletionResponse)
async def chat_completion_v1(request: ChatCompletionRequest):
    return await process_completion(request)

@app.get("/v1/models")
async def list_models_v1():
    return {
        "data": [
            {
                "id": "python-code-advisor-v1",
                "object": "model",
                "owned_by": "organization-owner",
                "permission": []
            }
        ]
    }

# Endpoints sem prefixo v1 (para compatibilidade)
@app.post("/chat/completions", response_model=ChatCompletionResponse)
async def chat_completion(request: ChatCompletionRequest):
    return await process_completion(request)

@app.get("/models")
async def list_models():
    return {
        "data": [
            {
                "id": "python-code-advisor-v1",
                "object": "model",
                "owned_by": "organization-owner",
                "permission": []
            }
        ]
    }

# Endpoint de saúde
@app.get("/health")
async def health_check():
    return {"status": "ok", "model": "python-code-advisor-v1"}