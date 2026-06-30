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

### 04 — Processador de Vendas
Sistema de análise de vendas com ranking de vendedores e filtros estatísticos.

**Praticado:**
- List comprehension em múltiplos contextos (extração de valores, filtros condicionais)
- `set()` para remoção de duplicatas
- `sorted()` + `lambda` + `reverse=True` para ranking decrescente
- `enumerate()` para numerar posições e resultados
- Separação entre lógica de processamento (funções que retornam dados) e apresentação (formatação no `main`)

### 05 — Sistema de RPG Expandido
Sistema de batalha em equipe com 3 tipos de personagens construído do zero, aplicando todos os pilares de OOP.

**Praticado:**
- `ABC` e `@abstractmethod` para impedir instanciação direta da classe base
- `@property` + `@hp.setter` com `max(0, valor)` para proteger o HP
- Herança com `super()` em três subclasses (`Mago`, `Guerreiro`, `Curandeiro`)
- `isinstance()` para diferenciar comportamento por tipo em tempo de execução
- List comprehension com múltiplas condições para filtrar alvos e aliados vivos
- `choice()` para seleção aleatória de alvos
- Refatoração DRY: extração de lógica repetida para método `config_luta()`
- Debugging de race condition (lista vazia no meio de um turno de batalha)

## Tecnologias

- Python 3.14
- Sem bibliotecas externas — Python puro

## Sobre

Atividades desenvolvidas como parte da trilha de aprendizado back-end, com foco em consolidar fundamentos antes de avançar para frameworks como FastAPI e Django.