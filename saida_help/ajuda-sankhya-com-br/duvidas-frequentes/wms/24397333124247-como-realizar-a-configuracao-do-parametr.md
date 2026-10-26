---
id: "24397333124247"
titulo: "Como realizar a configuração do parâmetro  \"WMSINFOADTAREFA\"?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24397333124247-Como-realizar-a-configura%C3%A7%C3%A3o-do-par%C3%A2metro-WMSINFOADTAREFA"
trilha: "Dúvidas Frequentes > WMS"
atualizado_em: "2026-07-22T14:46:52Z"
rotulos: ["Produtos", "Configuração", "WMS", "Parâmetros", "Detalhes do Produto", "Parâmetro", "WMSINFOADTAREFA", "Parâmetro \"WMSINFOADTAREFA\"", "Exibir campos na tela de \"Detalhes do Produto\"", "\"NUMNOTA CAB#Parceiro.NOMEPARC ITE#Produto.DESCRPROD\""]
---

# Como realizar a configuração do parâmetro  "WMSINFOADTAREFA"?

No parâmetro **"WMSINFOADTAREFA"** podemos configurar uma expressão com os campos que serão apresentados na tela de **"Detalhes do Produto"**, durante a execução de Tarefas, ao clicar no botão **"Adicional"**.

**Na expressão podemos utilizar campos separados por vírgula da TGFCAB, TGFITE e campos de tabelas que ligam com estas.** A tabela padrão de busca é a TGFCAB. Para selecionarmos campos da TGFITE devemos utilizar o prefixo ITE#.

**Por exemplo:**
**"NUMNOTA,CAB#Parceiro.NOMEPARC,ITE#Produto.DESCRPROD"**

A expressão acima exibirá na tela de Informações adicionais dos detalhes do produto os seguintes campos:
Nro. Nota da TGFCAB, Nome do Parceiro da TGFPAR e Descrição da TGFPRO.

O prefixo CAB# é opcional para campos da TGFCAB, pois os mesmos são padrões. Mas, **para campos que partem da TGFITE, é obrigatório o uso do prefixo ITE#.**
