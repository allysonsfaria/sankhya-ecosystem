---
id: "4421372721175"
titulo: "Total do financeiro diferente do total da nota (Tipo Negoc.possui Nro de Parcelas)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4421372721175-Total-do-financeiro-diferente-do-total-da-nota-Tipo-Negoc-possui-Nro-de-Parcelas"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:19:27Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Financeiro", "#validadoClaudio", "#causaraiz", "CORE_E02784", "Total financeiro difere da nota", "Ajuste e refaça financeiro", "Tipo de negociação com parcelas inconsistentes", "Erro"]
---

# Total do financeiro diferente do total da nota (Tipo Negoc.possui Nro de Parcelas)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16287126709143) MENSAGEM:**

[CORE\_E02784] - Total do financeiro diferente do total da nota (Tipo Negoc.possui Nro de Parcelas).

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16287126713495) CAUSA:**

Essa mensagem será apresentada quando o tipo de negociação utilizado possui 'Nro de Parcelas' informado (aba **"Característica",** da tela **"Tipo de Negociação"**) e o total do financeiro gerado difere do total da nota.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16287158058903) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Certifique-se que o valor gerado no financeiro da nota (soma das parcelas da aba "Financeiro" ) está igual ao 'Valor…](https://ajuda.sankhya.com.br/hc/article_attachments/16287126718487) Certifique-se que o valor gerado no financeiro da nota (soma das parcelas da aba **"Financeiro"**) está igual ao 'Valor total da nota'.

![Imagem 5: Certifique-se que o valor gerado no financeiro da nota (soma das parcelas da aba "Financeiro" ) está igual ao 'Valor…](https://ajuda.sankhya.com.br/hc/article_attachments/15500597353367)

![Imagem 6: Selecione a opção "Refazer Financeiro" e valide se as parcelas geradas foram ajustadas, de forma que essa divergência…](https://ajuda.sankhya.com.br/hc/article_attachments/16287126719767) Selecione a opção **"Refazer Financeiro"** e valide se as parcelas geradas foram ajustadas, de forma que essa divergência sejam sanadas.

![Imagem 7: Selecione a opção "Refazer Financeiro" e valide se as parcelas geradas foram ajustadas, de forma que essa divergência…](https://ajuda.sankhya.com.br/hc/article_attachments/15500673593751)

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16287158062231) OBSERVAÇÃO:**

**(1)** Se o processo da sua empresa permite essa situação, valide com o implantador da empresa a necessidade de ajustar os parâmetros abaixo, que permitem esse cenário:

**Validação por TOP:**

- Parâmetro "**HABOPCFINMENNOT" :** ativado
- Realizada marcação **'Permite financeiro menor que o valor total da nota '** (Tela 'Tipos de Operação-TOP' >> aba 'X')

**Validação Geral:**

- Parâmetro **"VALTOTFINNOT- Valida total dos financeiros da nota":** desativado

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16287158066583) IMPORTANTE:**

**(1)** Nesse caso, é importante avaliar também as configurações atuais do parâmetro NFEFINDIFNOTA, de forma que a diferença dos valores seja devidamente gerada.

**(1)** Os parâmetros acima afetam a divergência de valor: financeiro **menor** que o total da nota. Se financeiro maior que o total da nota, a validação continuará acontecendo, visto não tratar-se de um cenário válido.
