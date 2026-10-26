---
id: "360052576234"
titulo: "O valor do desdobramento não pode ser negativo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052576234-O-valor-do-desdobramento-n%C3%A3o-pode-ser-negativo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:29:08Z"
rotulos: ["Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "#AGUARDANDOVALIDAÇÃO", "#formatadoroger", "CORE_E02415", "CORE_E02395", "Valor do desdobramento não pode ser negativo", "Verifique fórmula do tipo de negociação", "Ajuste fórmula ou contate o suporte", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# O valor do desdobramento não pode ser negativo

[CORE\_E02415] Erro interno: O valor do desdobramento não pode ser negativo.

[CORE\_E02395] Erro interno: O valor do desdobramento não pode ser negativo.

### CAUSA

O erro ocorre por diferentes motivos, dependendo do contexto:

**Tipos de Negociação:** Ocorre quando o resultado final do valor do título financeiro é negativo, geralmente ocasionado por uma fórmula do tipo de negociação com uma condição incorreta.

**Baixa de títulos com valor zero:** O parâmetro **"VLRBAIXAZERO"** está desabilitado, impedindo que o sistema aceite baixas com valor igual a zero.

**Descontos:** Utilizar o campo de desconto com valor superior ao valor do desdobramento, de forma que o desdobramento resulte em um valor negativo.

### SOLUÇÃO

A solução varia conforme o contexto em que o erro ocorre. Siga as orientações abaixo:

### Para Erros em Tipos de Negociação

**(1)** Identifique qual o tipo de negociação utilizado no lançamento.

**(2)** Acesse a tela **"Tipos de Negociação"** (Comercial >> Arquivo >> Cadastros >> Tipos de Negociação) e pesquise pelo tipo de negociação utilizado.

- Acesse a aba: Parcelas
- Identifique para cada linha de parcelas, o campo **"FÓRMULA"**:

![Imagem 1: Identifique para cada linha de parcelas, o campo "FÓRMULA" :](https://ajuda.sankhya.com.br/hc/article_attachments/18605387615895)

Solicite que o responsável analise a fórmula, pois ela pode conter uma condição que esteja negativando o financeiro. Ajuste a fórmula ou utilize um tipo de negociação sem fórmula que resulte em valores positivos.

### Para Baixa de Títulos com Valor Zero

**(1)** Acesse a tela **"Preferências"** (Configurações >> Avançado >> Preferências).

**(2)** Localize o parâmetro **"VLRBAIXAZERO - Aceita valor de baixa igual a zero"**, habilite-o, salve a alteração e realize novamente a baixa.

![Imagem 2: (2) Localize o parâmetro "VLRBAIXAZERO - Aceita valor de baixa igual a zero" , habilite-o, salve a alteração e realize…](https://ajuda.sankhya.com.br/hc/article_attachments/41743994771607)

Caso o erro persista após estas verificações, entre em contato com o Service Desk para análise técnica.
