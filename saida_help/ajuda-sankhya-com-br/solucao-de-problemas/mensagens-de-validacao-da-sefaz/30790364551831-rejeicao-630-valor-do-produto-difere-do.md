---
id: "30790364551831"
titulo: "Rejeição 630: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30790364551831-Rejei%C3%A7%C3%A3o-630-Valor-do-Produto-difere-do-produto-Valor-Unit%C3%A1rio-de-Tributa%C3%A7%C3%A3o-e-Quantidade-Tribut%C3%A1vel"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:34:42Z"
rotulos: ["Produtos", "NF-e", "XML", "SEFAZ", "Impostos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Rejeição 630", "difere do", "produto Valor Unitário de", "Valor do Produto", "Tributação e Quantidade Tributável", "Regra de validação"]
---

# Rejeição 630: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30790364541207) **MENSAGEM:**

Rejeição 630: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30790364542231)SOLUÇÃO:**

Para resolver a Rejeição, siga os passos abaixo:

![Imagem 3: Verifique os valores apresentados nas seguintes tags do XML: valor do produto ( vProd ), valor da multiplicação do…](https://ajuda.sankhya.com.br/hc/article_attachments/31295560206871) Verifique os valores apresentados nas seguintes tags do XML: valor do produto (**vProd**), valor da multiplicação do Valor da Unidade Tributável (**vUnTrib**) e a quantidade tributável (**qTrib**).

Exemplo da estrutura em XML:

<vProd>

<vProd>40.00</vProd>
<cEANTrib>SEM GTIN</cEANTrib>
<uTrib>CX</uTrib>
<qTrib>0.0417</qTrib>
<vUnTrib>960</vUnTrib>

**(1)** Neste caso, **qualquer valor na tag vProd que seja diferente da multiplicação dos  valores das tags vUnTrib x qTrib,**resultará na rejeição.

No exemplo apresentado anteriormente, a multiplicação seria realizado da seguinte forma:

vUnTrib x qTrib 
960 \* 0,0417 = 40,032

Assim, na tag vProd deveria ter sido apresentado o valor 40,032

**Observação:** para saber como baixar o XML, acesse o artigo: [Como gerar XML em conferência?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044343213)

![Imagem 4: Encontrada a divergência na tag vProd, nas Centrais, faça os devidos ajustes nos campos que influenciam nessa…](https://ajuda.sankhya.com.br/hc/article_attachments/31295515200279) Encontrada a divergência na tag vProd, nas Centrais, faça os devidos ajustes nos campos que influenciam nessa multiplicação.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30790364544023)CAUSA:**

A regra de validação da Sefaz, diz o seguinte:

Se NF-e Normal (tag:finNFe=1)

 - vProd (id:I11) difere de vUnTrib (id:I14a)\* qTrib (id:I14) (NT 2001/005)

Esta regra de validação é facultativa, isto é, fica a critério da UF a aplicação da regra e é valida para NF-e (modelo 55) e NFC-e (modelo 65)

Referencia: <https://www.nfe.fazenda.gov.br/portal/principal.aspx>
