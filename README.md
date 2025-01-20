# Python Code Advisor

Um analisador de código Python que fornece sugestões de melhorias baseadas em boas práticas. Este projeto é compatível com a API OpenAI, permitindo integração com ferramentas como Crew AI.

## Funcionalidades

- Análise de código Python
- Sugestões de melhorias de estilo
- Verificação de complexidade
- Recomendações de boas práticas
- Interface compatível com OpenAI
- Integração com Crew AI

## Requisitos

- Python 3.8+
- FastAPI
- Docker (opcional)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/jeovahfialho/python-code-advisor.git
cd python-code-advisor
```

2. Configure o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Execute o serviço:
```bash
# Com Python diretamente
uvicorn src.main:app --reload

# Ou com Docker (Mais Aconselhável)
docker build -t python-code-advisor .
docker run -p 8000:8000 python-code-advisor
```

## Uso

### API Direta

O serviço expõe endpoints compatíveis com a API OpenAI:

```bash
# Listar modelos disponíveis
curl http://localhost:8000/models

# Analisar código
curl -X POST http://localhost:8000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "python-code-advisor-v1",
    "messages": [
      {
        "role": "user",
        "content": "def MinhaFuncao(Param1, Param2):\n    Resultado = Param1 + Param2\n    return Resultado"
      }
    ]
  }'
```

### Integração com Crew AI

1. Instale as dependências do Crew AI:
```bash
pip install crewai openai
```

2. Configure o ambiente:
```python
# config.py
import os

os.environ["OPENAI_API_BASE"] = "http://localhost:8000"
os.environ["OPENAI_API_KEY"] = "qualquer-string"
```

3. Crie seu script de análise:
```python
# analyzer_crew.py
from crewai import Agent, Task, Crew, Process

code_analyzer = Agent(
    role='Python Code Analyzer',
    goal='Analyze Python code and suggest improvements',
    backstory="Expert in Python code analysis and best practices",
    model="python-code-advisor-v1",
    verbose=True
)

analysis_task = Task(
    description="Analyze this Python code...",
    agent=code_analyzer
)

crew = Crew(
    agents=[code_analyzer],
    tasks=[analysis_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
print(result)
```

## Exemplos de Uso

### 1. Análise de Estilo
```python
# Exemplo de código para análise
def CalculateSum(NumberOne, NumberTwo):
    Result = NumberOne + NumberTwo
    return Result
```

Resposta:
```
Análise do Código Python:

⚠️ Linha 1: Considere usar snake_case para nomes
⚠️ A função 'CalculateSum' não possui docstring
```

### 2. Análise de Complexidade
```python
def process_data(name, age, city, country, phone, email, occupation):
    print(f"{name} from {city}")
```

Resposta:
```
Análise do Código Python:

⚠️ A função 'process_data' tem muitos parâmetros
⚠️ A função 'process_data' não possui docstring
```

## Estrutura do Projeto

```
python-code-advisor/
├── src/
│   ├── __init__.py
│   ├── main.py                # API principal
│   └── services/
│       ├── __init__.py
│       └── code_analyzer.py   # Lógica de análise
├── tests/
├── crew_examples/            # Exemplos de uso com Crew AI
├── requirements.txt
├── Dockerfile
└── README.md
```

## Contribuindo

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Add nova feature'`)
4. Push para a Branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## Notas Adicionais

- O serviço é compatível com a API OpenAI, permitindo seu uso como um modelo personalizado
- Pode ser integrado com Crew AI ou qualquer outra ferramenta que suporte a API OpenAI
- Os endpoints principais são `/models` e `/chat/completions`
- Suporta tanto endpoints com prefixo `/v1` quanto sem prefixo
