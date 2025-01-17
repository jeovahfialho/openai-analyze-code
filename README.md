# Python Code Advisor

Um agente inteligente que analisa código Python e fornece sugestões de melhorias baseadas em boas práticas.

## Funcionalidades

- Análise de código Python
- Sugestões de melhorias de estilo
- Verificação de complexidade
- Recomendações de boas práticas
- Histórico de análises

## Requisitos

- Python 3.8+
- PostgreSQL
- Redis
- Docker e Docker Compose (opcional)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/python-code-advisor.git
cd python-code-advisor
```

2. Configure as variáveis de ambiente (copie o `.env.example` para `.env`):
```bash
cp .env.example .env
```

3. Execute com Docker:
```bash
docker-compose up --build
```

## Uso

A API estará disponível em `http://localhost:8000`

### Swagger UI (Documentação Interativa)
Para testar a API de forma interativa, acesse:
```
http://localhost:8000/docs
```

A interface Swagger UI permite que você:
- Visualize todos os endpoints disponíveis
- Teste as requisições diretamente no navegador
- Veja os modelos de dados esperados
- Entenda as respostas possíveis

### Endpoints:
- `POST /analyze-code`: Analisa um trecho de código Python
- `GET /health`: Verifica o status do serviço

### Exemplos de Uso

1. **Função com problemas de estilo e documentação**
```bash
curl -X POST http://localhost:8000/analyze-code \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def Calculate_sum(numberOne, numberTwo):\n    Result = numberOne + numberTwo\n    return Result"
  }'
```

2. **Função com muitos parâmetros**
```bash
curl -X POST http://localhost:8000/analyze-code \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def process_data(name, age, city, country, phone, email, occupation):\n    print(f\"{name} from {city}\")"
  }'
```

3. **Código com problemas de complexidade**
```bash
curl -X POST http://localhost:8000/analyze-code \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def complex_function(a, b):\n    if a > 0:\n        if b > 0:\n            if a > b:\n                if a % b == 0:\n                    return True\n    return False"
  }'
```

4. **Classe sem documentação**
```bash
curl -X POST http://localhost:8000/analyze-code \
  -H "Content-Type: application/json" \
  -d '{
    "code": "class UserManager:\n    def __init__(self, username):\n        self.username = username\n    \n    def get_user(self):\n        return self.username"
  }'
```

5. **Função com erro de sintaxe**
```bash
curl -X POST http://localhost:8000/analyze-code \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def broken_function(:\n    print(\"This has syntax error\")"
  }'
```

6. **Múltiplas funções para testar complexidade**
```bash
curl -X POST http://localhost:8000/analyze-code \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def func1():\n    pass\n\ndef func2():\n    pass\n\ndef func3():\n    pass\n\ndef func4():\n    pass\n\ndef func5():\n    pass\n\ndef func6():\n    pass"
  }'
```

### Exemplos de Respostas

1. **Resposta para problemas de estilo**:
```json
{
  "suggestions": [
    {
      "type": "style",
      "message": "Line 1: Consider using snake_case for variable names"
    },
    {
      "type": "documentation",
      "message": "Function 'Calculate_sum' lacks a docstring"
    }
  ],
  "analysis_id": 1,
  "created_at": "2024-01-17T12:00:00"
}
```

2. **Resposta para complexidade**:
```json
{
  "suggestions": [
    {
      "type": "complexity",
      "message": "Function 'process_data' has too many parameters"
    },
    {
      "type": "documentation",
      "message": "Function 'process_data' lacks a docstring"
    }
  ],
  "analysis_id": 2,
  "created_at": "2024-01-17T12:01:00"
}
```

## Interface Web

Você também pode testar a API usando a interface Swagger UI disponível em:
```
http://localhost:8000/docs
```

---

## Estrutura do Projeto

```
python-code-advisor/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── scripts/
│   └── init.sql
└── src/
    ├── main.py
    ├── config.py
    └── services/
        └── code_analyzer.py
```

## Contribuindo

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request