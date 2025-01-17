import ast
from typing import List, Dict

class CodeAnalyzer:
    def analyze(self, code: str) -> List[Dict[str, str]]:
        suggestions = []
        
        try:
            tree = ast.parse(code)
            
            # Analisa o código usando o visitor pattern
            analyzer = CodeVisitor()
            analyzer.visit(tree)
            suggestions.extend(analyzer.suggestions)
            
            # Análises adicionais
            suggestions.extend(self._check_naming_conventions(code))
            suggestions.extend(self._check_code_complexity(tree))
            
            return suggestions
        except SyntaxError as e:
            return [{"type": "error", "message": f"Syntax error: {str(e)}"}]
        except Exception as e:
            return [{"type": "error", "message": f"Analysis error: {str(e)}"}]
    
    def _check_naming_conventions(self, code: str) -> List[Dict[str, str]]:
        suggestions = []
        lines = code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            if any(char.isupper() for char in line if char.isalnum()):
                suggestions.append({
                    "type": "style",
                    "message": f"Line {line_num}: Consider using snake_case for variable names"
                })
        
        return suggestions
    
    def _check_code_complexity(self, tree: ast.AST) -> List[Dict[str, str]]:
        suggestions = []
        
        functions = len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
        classes = len([node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)])
        
        if functions > 5:
            suggestions.append({
                "type": "complexity",
                "message": "Consider breaking down the code into smaller modules"
            })
        
        return suggestions


class CodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.suggestions = []
    
    def visit_FunctionDef(self, node: ast.FunctionDef):
        if not ast.get_docstring(node):
            self.suggestions.append({
                "type": "documentation",
                "message": f"Function '{node.name}' lacks a docstring"
            })
        
        if len(node.args.args) > 5:
            self.suggestions.append({
                "type": "complexity",
                "message": f"Function '{node.name}' has too many parameters"
            })
        
        self.generic_visit(node)