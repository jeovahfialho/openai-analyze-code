# Python Code Advisor

Um analisador de código Python que fornece sugestões de melhorias baseadas em boas práticas.

## 🌟 Interface Interativa (Swagger UI)

Acesse a documentação interativa da API em:
```
http://localhost:8000/docs
```

Na interface Swagger, você pode:
- Visualizar todos os endpoints disponíveis
- Testar a API diretamente no navegador
- Ver exemplos de requisições e respostas
- Explorar os modelos de dados

## Funcionalidades

- Análise de código Python
- Sugestões de melhorias de estilo
- Verificação de complexidade
- Recomendações de boas práticas
- Interface compatível com OpenAI

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

# Ou com Docker
docker build -t python-code-advisor .
docker run -p 8000:8000 python-code-advisor
```

## Uso com Crew AI (Manual de Integração)

### Preparação do Ambiente

1. Acesse app.crewai.com e faça login
2. Vá para "Settings" ou "Configurations"
3. Configure o modelo personalizado:
   - Model Base URL: `http://localhost:8000`
   - Tipo: custom-openai-compatible
   - Model Name: `python-code-advisor-v1`

### Registrando seu Agente

1. No dashboard do Crew AI, vá para a seção de agentes ou integrações
2. Configure seu agente com:
   ```
   Nome: Python Code Analyzer
   Descrição: Expert in Python code analysis and best practices
   Base URL: http://localhost:8000
   Modelo: python-code-advisor-v1
   ```

### Capacidades do Agente

O agente pode:
- Analisar estilo de código Python
- Verificar conformidade com PEP 8
- Sugerir melhorias de código
- Identificar problemas de complexidade

## Exemplos de Uso

### Via Swagger UI
1. Acesse `http://localhost:8000/docs`
2. Localize o endpoint `/chat/completions`
3. Clique em "Try it out"
4. Use o exemplo:
```json
{
  "model": "python-code-advisor-v1",
  "messages": [
    {
      "role": "user",
      "content": "def MinhaFuncao():\n    pass"
    }
  ]
}
```

### Exemplos via Terminal (cURL)

1. **Verificar Status do Serviço**
```bash
curl http://localhost:8000/health
```

2. **Analisar Função com Problemas de Estilo**
```bash
curl -X POST http://localhost:8000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "python-code-advisor-v1",
    "messages": [
      {
        "role": "user",
        "content": "def CalcularSoma(PrimeiroNumero, SegundoNumero):\n    Resultado = PrimeiroNumero + SegundoNumero\n    return Resultado"
      }
    ]
  }'
```

3. **Analisar Classe sem Documentação**
```bash
curl -X POST http://localhost:8000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "python-code-advisor-v1",
    "messages": [
      {
        "role": "user",
        "content": "class UserManager:\n    def __init__(self, name):\n        self.name = name\n    def get_user(self):\n        return self.name"
      }
    ]
  }'
```

4. **Analisar Função com Alta Complexidade**
```bash
curl -X POST http://localhost:8000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "python-code-advisor-v1",
    "messages": [
      {
        "role": "user",
        "content": "def process_data(a, b, c, d, e, f):\n    if a > 0:\n        if b > 0:\n            if c > 0:\n                return True\n    return False"
      }
    ]
  }'
```

5. **Analisar Código com Múltiplas Funções**
```bash
curl -X POST http://localhost:8000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "python-code-advisor-v1",
    "messages": [
      {
        "role": "user",
        "content": "def func1():\n    pass\n\ndef func2():\n    pass\n\ndef func3():\n    pass\n\ndef func4():\n    pass\n\ndef func5():\n    pass\n\ndef func6():\n    pass"
      }
    ]
  }'
```

Cada exemplo retornará uma análise detalhada com sugestões de melhorias específicas para o código fornecido.

## Estrutura do Projeto

```
python-code-advisor/
├── src/
│   ├── __init__.py
│   ├── main.py           # API principal
│   └── services/
│       ├── __init__.py
│       ├── code_analyzer.py
│       └── crew_integration.py  # Preparado para futura integração
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