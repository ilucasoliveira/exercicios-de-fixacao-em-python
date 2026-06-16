# Atividades de Fixação — Python

Repositório com atividades práticas desenvolvidas para fixar e aprofundar conceitos de Python, cobrindo desde estruturas de dados básicas até lógica de validação mais elaborada.

Cada atividade foi construída do zero, com funções organizadas por responsabilidade única, tratamento de erros com `try/except` e menus interativos em loop.

## Atividades

### 01 — Agenda de Contatos
CRUD completo de contatos usando dicionário aninhado.

**Praticado:**
- Dicionário de dicionários (`agenda[nome] = {"telefone": ..., "email": ...}`)
- Busca parcial por nome (case-insensitive) com `in` e `.lower()`
- Validação de entrada reutilizável (`input_strip`)
- Formatação de saída com f-strings multilinha

### 02 — Analisador de Notas
Sistema de gestão de notas de turma com relatório estatístico.

**Praticado:**
- Lista de dicionários ordenada com `sorted()` e `lambda`
- `max()` / `min()` com `key` para encontrar maior e menor nota
- Cálculo de média, contagem de aprovados/recuperação/reprovados
- `any()` com generator expression para verificação de existência

### 03 — Validador de Senhas
Validador de força de senha com score e feedback detalhado.

**Praticado:**
- `any()` combinado com `isupper()`, `islower()`, `isdigit()` e `in`
- Dicionário de retorno estruturado (`score` + `feedback`)
- Classificação por faixas de pontuação

## Tecnologias

- Python 3.14
- Sem bibliotecas externas — Python puro

## Sobre

Atividades desenvolvidas como parte da trilha de aprendizado back-end, com foco em consolidar fundamentos antes de avançar para frameworks como FastAPI e Django.
