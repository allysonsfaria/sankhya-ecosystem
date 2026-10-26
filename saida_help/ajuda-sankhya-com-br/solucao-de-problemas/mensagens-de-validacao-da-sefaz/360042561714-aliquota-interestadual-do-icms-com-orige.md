---
id: "360042561714"
titulo: "Alíquota interestadual do ICMS com origem diferente do previsto (NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042561714-Al%C3%ADquota-interestadual-do-ICMS-com-origem-diferente-do-previsto-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:50Z"
rotulos: ["ERRONF", "Alíquotas", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "697", "Alíquota ICMS incorreta", "Ajustar alíquotas conforme origem", "Verificar origem produto"]
---

# Alíquota interestadual do ICMS com origem diferente do previsto (NT2015/003)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16475086489623) MENSAGEM:**

[697 - Rejeição]: Alíquota interestadual do ICMS com origem diferente do previsto (NT2015/003).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16475040022039) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Identifique a origem dos produtos inseridos na respectiva NF-e:](https://ajuda.sankhya.com.br/hc/article_attachments/16475086497303) Identifique a origem dos produtos inseridos na respectiva NF-e:

- Tela "**[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)"** (Caminho de acesso: Configurações » Cadastros)
  Aba: "**Geral"** » Campo: "**Origem do Produto"**

![Imagem 4: Na Central de Vendas busque pela coluna 'Alíq.ICMS' e verifique se as regras abaixo estão sendo seguidas:](https://ajuda.sankhya.com.br/hc/article_attachments/16475086501911) Na Central de Vendas busque pela coluna 'Alíq.ICMS' e verifique se as regras abaixo estão sendo seguidas:

- Para Produto de Origem Nacional (**0,4,5,6,7**), o percentual de alíquota deverá ser  **7%** ou **12**%
- Para Produtos de Origem Estrangeira (**1,2,3,8**), o percentual de alíquota deverá ser **4**%

![Imagem 5: Ao identificar em seu lançamento itens que não obedeçam às tributações mencionadas acima, localize a regra de ICMS que…](https://ajuda.sankhya.com.br/hc/article_attachments/16475086507031) Ao identificar em seu lançamento itens que não obedeçam às tributações mencionadas acima, localize a regra de ICMS que gerou essa tributação, através da tela **"[Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS) nos campos "**Tributação"**; "**Alíquota"** e "**Alíquota p/ Origem Estrangeira"** e realize os devidos ajustes.

Lembre-se que esse é um ajuste fiscal/tributário e deverá ser realizado por um usuário com conhecimento sobre a rotina, com informações transmitidas pelo Contador, de forma que os ajustes sejam realizados sem causar impactos indevidos para os demais itens.

![Imagem 6: Após ajustes, inutilize a numeração da NF-e, realize um novo faturamento, confira as alíquotas buscadas e proceda com…](https://ajuda.sankhya.com.br/hc/article_attachments/16475040031127) Após ajustes, inutilize a numeração da NF-e, realize um novo faturamento, confira as alíquotas buscadas e proceda com confirmação da nota.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16475086513431) CAUSA:**

Há duas validações para a Rejeição.

(1)** Primeira situação:**

Quando for emitida uma NF-e com Alíquota Interestadual igual 4.00% (quatro por cento) e a Origem da Mercadoria for IGUAL a:

0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8;
4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes;
5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%;
6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural;
7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural.

(1)** Segunda situação:**

Quando for emitida uma NF-e com Alíquota Interestadual igual a 7.00% (sete por cento) ou 12.00% (doze por cento) e a Origem da Mercadoria for IGUAL a:

1 - Estrangeira - Importação direta, exceto a indicada no código 6; ou
2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; ou
3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; ou
8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%.

**![Imagem 8: OBSERVAÇÃO: ( NT2015/003 ) - Nota Técnica.](https://ajuda.sankhya.com.br/hc/article_attachments/16475086520471) OBSERVAÇÃO:**
([NT2015/003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zJGzcwysHPo=)) - Nota Técnica.
