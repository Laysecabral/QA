# Este é um projeto que implementa uma função de validação de senhas em Python. 
O foco principal é garantir que todas as regras de segurança sejam respeitadas, 
com uma suíte de **testes unitários usando Pytest**.  O projeto atinge 92% de 
cobertura de código, garantindo que a maior parte das regras de negócio seja 
testada automaticamente.


## 🛠️ Tecnologias Utilizadas

- Linguagem: Python 3.9  
- Testes Unitários: Pytest  
- Cobertura de Testes: pytest-cov  
- Estrutura de Projeto: `src/` e `tests/`  


## 📋 Regras de Negócio Testadas

O módulo `password_validator.py` implementa as seguintes regras de segurança:

| Regra | Descrição |
|-------|-----------|
| R1. Comprimento Mínimo | A senha deve ter no mínimo 8 caracteres. |
| R2. Caractere Maiúsculo | A senha deve conter pelo menos uma letra maiúscula. |
| R3. Caractere Minúsculo | A senha deve conter pelo menos uma letra minúscula. |
| R4. Dígito Numérico | A senha deve conter pelo menos um número. |
| R5. Caractere Especial | A senha deve conter ao menos um caractere especial (!@#$%^&* etc). |

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente e rodar os testes no Windows com Git Bash:

1. Clonar o Repositório
git clone https://github.com/Laysecabral/QA.git
cd QA

2. Configurar e Ativar o Ambiente Virtual (venv)

* Crie o ambiente virtual:

python -m venv venv


* Ative o ambiente virtual no Git Bash:

source venv/Scripts/activate


Após ativar, o prompt deve mostrar (venv) indicando que o ambiente virtual está ativo.

3. Instalar Dependências

Com o ambiente virtual ativo, instale o Pytest e o pytest-cov (caso não haja requirements.txt):

pip install pytest pytest-cov

4. Rodar os Testes e Gerar o Relatório de Cobertura

Execute o comando a seguir para rodar todos os testes, gerar a saída de cobertura no terminal e criar a pasta htmlcov/:

PYTHONPATH=. pytest --cov=src --cov-report term-missing --cov-report html -v


O relatório exibirá no terminal a cobertura por arquivo, por exemplo:

Coverage report: 92%

src/__init__.py                statements 0 missing 0 excluded 0 coverage 100%

src/password_validator.py      statements 13 missing 1 excluded 0 coverage 92%

TOTAL                          statements 13 missing 1 excluded 0 coverage 92%

5. Abrir o Relatório de Cobertura no Navegador

Para abrir o relatório HTML gerado:

start htmlcov/index.html   # Windows


## 📊 Relatório de Cobertura

Resultados atuais:

Abaixo está o relatório de cobertura de testes, provando que a maior parte das regras 
de negócio do módulo password_validator.py foi validada pelos testes, atingindo 92% de cobertura.

<img width="828" height="447" alt="relatório de teste unitário" src="https://github.com/user-attachments/assets/6bbe88eb-04cb-489f-9538-26a608dd9c6b" />





