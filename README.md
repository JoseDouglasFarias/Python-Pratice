# Python-Pratice

Repositório de estudos criado para praticar a linguagem Python e fortalecer a
base necessária para programar. A ideia é aprender fazendo: começar com
problemas pequenos, exercitar a lógica e evoluir os exemplos conforme novos
conceitos forem estudados.

## O que há no projeto de prática

Até o momento, o exercício implementado neste repositório é o
`expenser-analyzer`, descrito na próxima seção. Ele serve como prática de:

- criação e chamada de funções;
- uso de listas e laços `for`;
- acumuladores e contadores;
- condições com `if`;
- retorno de vários resultados;
- tratamento de uma lista vazia;
- verificações simples com `assert`.

O repositório pode receber outros exercícios e projetos à medida que os estudos
avançarem.

## Projeto: `expenser-analyzer`

Um exercício introdutório de análise de despesas. A função
`analisar_despesas(valores)` recebe uma lista de valores e retorna uma tupla com:

1. a soma de todos os valores;
2. a quantidade de valores estritamente maiores que `30`;
3. o maior valor da lista.

Quando a lista está vazia, a função retorna `(0, 0, None)`, pois não existe um
maior valor a informar.

### Exemplo

Para a lista `[10, 20, 30, 40, 50]`, o resultado é:

```text
(150, 2, 50)
```

O arquivo principal executa esse exemplo ao ser iniciado e exibe o total de
despesas, a quantidade de valores acima de `30` e o maior valor.

### Estrutura atual

```text
.
├── README.md
└── expenser-analyzer/
    ├── automated_test.py
    └── expense_analyzer.py
```

- `expenser-analyzer/expense_analyzer.py`: define `analisar_despesas` e
  apresenta um exemplo de execução.
- `expenser-analyzer/automated_test.py`: verifica que
  `analisar_despesas([10, 20, 30])` retorna `(60, 0, 30)`.

### Como executar

É necessário ter Python instalado. Não há dependências externas: o exercício
usa apenas recursos da biblioteca padrão da linguagem.

No PowerShell, a partir da pasta do repositório:

```powershell
python .\expenser-analyzer\expense_analyzer.py
```

Para executar a verificação existente, entre na pasta do projeto e rode o
arquivo de teste:

```powershell
Set-Location .\expenser-analyzer
python .\automated_test.py
```

O teste usa uma instrução `assert`. Se a condição não for atendida, Python
interrompe a execução com um erro; se for atendida, o processo termina sem
mensagem de falha. Ao importar o módulo, o exemplo do arquivo principal também
exibe seus resultados.
