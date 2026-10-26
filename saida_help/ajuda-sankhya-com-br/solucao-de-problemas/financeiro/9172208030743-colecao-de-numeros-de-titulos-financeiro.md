---
id: "9172208030743"
titulo: "Coleção de números de títulos financeiros não pode ser vazia"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9172208030743-Cole%C3%A7%C3%A3o-de-n%C3%BAmeros-de-t%C3%ADtulos-financeiros-n%C3%A3o-pode-ser-vazia"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:09:54Z"
rotulos: ["Configuração", "Impressão", "Relatórios", "Financeiro", "Cheque", "FIN_E00386", "[FIN_E00386] Coleção de números de títulos financeiros não pode ser vazia!", "Ajustar na tela de Impressão de Cheques", "Selecionar Agrupar nominal ao fornecedor\" para receitas", "Erro"]
---

# Coleção de números de títulos financeiros não pode ser vazia

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16421754397847) MENSAGEM:**

[FIN\_E00386] Coleção de números de títulos financeiros não pode ser vazia!

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16421730431895) SITUAÇÃO:**

Ao tentar imprimir um cheque a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16421730433303) SOLUÇÃO:**

O erro ocorre devido a coluna Tipo Marcação Cheque, na tela "**[Impressão de cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313)"** (Caminho de acesso: Financeiro » Relatórios » Impressão de Cheques), não estar devidamente preenchida. EX: Normal ao fornecedor.

![mceclip0](https://ajuda.sankhya.com.br/hc/article_attachments/15479643372439)

**![Imagem 5: IMPORTANTE: O ato de trazer títulos de receita na impressão de cheques é devido à necessidade de compensar o financeiro…](https://ajuda.sankhya.com.br/hc/article_attachments/16421730435095) IMPORTANTE:** O ato de trazer títulos de receita na impressão de cheques é devido à necessidade de compensar o financeiro de forma que o cheque fique com o valor real a pagar ao fornecedor. Para isto, ao selecionar receitas, o sistema automaticamente trará para o campo **"Marcação do Cheque"** a opção de **"Agrupar nominal ao fornecedor"** e a emissão do cheque é feita somente para títulos de despesas.

**![Imagem 6: OBSERVAÇÃO: Caso seja selecionado somente um título de receita e solicite-se a emissão do cheque, o sistema avisa a não…](https://ajuda.sankhya.com.br/hc/article_attachments/16421754409495) OBSERVAÇÃO:** Caso seja selecionado somente um título de receita e solicite-se a emissão do cheque, o sistema avisa a não possibilidade da emissão.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16421730437911) CAUSA:**

Tentar imprimir cheque sem que os títulos sejam apresentados na grade.
