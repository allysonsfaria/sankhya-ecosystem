---
id: "360043362833"
titulo: "Total do financeiro diferente do total da nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043362833-Total-do-financeiro-diferente-do-total-da-nota"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:24Z"
rotulos: ["CORE_E02783", "CORE_E02782", "Configuração", "Movimentação Financeira", "Impostos", "TOP", "Financeiro", "#PrintCláudio", "CORE_E06032", "Total financeiro diferente da nota", "Verifique valores e ajustes de parcelas", "Configurações inadequadas ou impostos"]
---

# Total do financeiro diferente do total da nota

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16116031020439) MENSAGEM:**

[CORE\_E02783] Total do financeiro diferente do total da nota.

[CORE\_E02782] Total do financeiro diferente do total da nota.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16116016367639) SOLUÇÃO:**

![Imagem 3: Certifique-se que o valor gerado no financeiro da nota (soma das parcelas da aba "Financeiro" ) está igual ao Valor…](https://ajuda.sankhya.com.br/hc/article_attachments/16116016369687) Certifique-se que o valor gerado no **financeiro da nota** (soma das parcelas da aba **"Financeiro"**) está igual ao **Valor total da nota**.

![Imagem 4: Certifique-se que o valor gerado no financeiro da nota (soma das parcelas da aba "Financeiro" ) está igual ao Valor…](https://ajuda.sankhya.com.br/hc/article_attachments/14601414346391)

![Imagem 5: Acesse Comercial » Arquivo » Cadastros » " Tipos de Negociação " e verifique no tipo de negociação, aba "Parcelas" , se…](https://ajuda.sankhya.com.br/hc/article_attachments/16116016371991) Acesse Comercial » Arquivo » Cadastros » **"[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)"** e verifique no tipo de negociação, aba **"Parcelas"**, se os percentuais, caso haja parcelas, somados resultará em 100%.

![Imagem 6: Acesse Comercial » Arquivo » Cadastros » " Tipos de Negociação " e verifique no tipo de negociação, aba "Parcelas" , se…](https://ajuda.sankhya.com.br/hc/article_attachments/14601430094999)

![Imagem 7: Verifique se existem parcelas por Empresa, na aba "Parcelas" , caso exista mais de uma parcela e cada parcela tenha um…](https://ajuda.sankhya.com.br/hc/article_attachments/16116016373271) Verifique se existem parcelas por Empresa, na aba**"Parcelas"**, caso exista mais de uma parcela e cada parcela tenha um código de empresa, deverá criar uma parcela específica para empresa da nota.

![Imagem 8: Verifique se existem parcelas por Empresa, na aba "Parcelas" , caso exista mais de uma parcela e cada parcela tenha um…](https://ajuda.sankhya.com.br/hc/article_attachments/14601430243735)

![Imagem 9: Em caso positivo, Botão "Outras opções (...)" » "Refazer Financeiro" , certificando-se que o valor das parcelas condiz…](https://ajuda.sankhya.com.br/hc/article_attachments/16116016374551) Em caso positivo, Botão **"Outras opções (...)"** » **"Refazer Financeiro"**, certificando-se que o valor das parcelas condiz com o total da nota

![Imagem 10: Em caso positivo, Botão "Outras opções (...)" » "Refazer Financeiro" , certificando-se que o valor das parcelas condiz…](https://ajuda.sankhya.com.br/hc/article_attachments/14601430208791)

![Imagem 11: Caso a divergência não esteja relacionada com os tópicos anteriores (cálculo incorreto do financeiro, fórmulas do tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/16116031031447) Caso a divergência não esteja relacionada com os tópicos anteriores (cálculo incorreto do financeiro, fórmulas do tipo de negociação), avalie se essa divergência está relacionada a incoerência de impostos. Exemplo:

**(2)** A diferença entre o total da nota e o valor do financeiro está relacionado ao Vlr.do IPI : nesse caso o IPI deveria somar ao total da nota, sendo necessário marcar na TOP a opção **"Somar IPI ao total da nota"**;

**![Imagem 12: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16116031034519) OBSERVAÇÕES:**

**(1)** Se o processo da sua empresa permite essa situação de divergência de valores, valide com o implantador da empresa a necessidade de ajustar os parâmetros abaixo, que permitem esse cenário:

(2)** Validação por TOP:**

**(3)**Parâmetro "**HABOPCFINMENNOT":** ativado

**(3)**Realizada marcação **"Permite financeiro menor que o valor total da nota"** (Tela 'Tipos de Operação-TOP', aba 'Financeiro')

(2)** Validação Geral:**

**(3)**Parâmetro **"VALTOTFINNOT- Valida total dos financeiros da nota"**: desativado

**![Imagem 13: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17801989316503) IMPORTANTE:**

- Nesse caso, é importante avaliar também as configurações atuais do parâmetro **NFEFINDIFNOTA**, de forma que a diferença dos valores seja devidamente gerada.
- Os parâmetros acima afetam a divergência de valor: financeiro **menor** que o total da nota. Se financeiro **maior** que o total da nota, a validação continuará acontecendo, visto não tratar-se de um cenário válido.

**![Imagem 14: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16116016396567) CAUSA:**

Ocorre, quando o financeiro da nota está diferente do total da nota, devido configurações inadequadas no tipo de operação ou fórmulas personalizadas no tipo de negociação.
