---
id: "16869639272087"
titulo: "Rejeição 890: GTIN inexistente no Cadastro Centralizado de GTIN (CCG) [nItem:999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16869639272087-Rejei%C3%A7%C3%A3o-890-GTIN-inexistente-no-Cadastro-Centralizado-de-GTIN-CCG-nItem-999"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:54:14Z"
rotulos: ["Produtos", "NF-e", "SEFAZ", "Impostos", "CFOP", "Corrija o GTIN no cadastro do produto ou configure como \"não informar\"", "GTIN inexistente no Cadastro Centralizado (CCG)", "GTIN não registrado no CCG para NCM e CFOP específicos", "GTIN"]
---

# Rejeição 890: GTIN inexistente no Cadastro Centralizado de GTIN (CCG) [nItem:999]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16869639263383)  MENSAGEM:**

GTIN inexistente no Cadastro Centralizado de GTIN (CCG) [nItem:999]

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16869645486615) CAUSA:**

A nota técnica informa que, para vendas de produção em estabelecimento onde os produtos utilizem NCM que consta no **Anexo I** da NT 2021.003\_v1\_10 e CFOP utilizado na operação esteja citado no **Anexo II** da mesma NT o GTIN (tag:cEAN) deve ser um valor válido no portal**CCG-Cadastro Centralizado de GTIN**,  caso contrário, acontecerá a rejeição. 

**Anexo I** :

![Imagem 3: Anexo I :](https://atendimento.tecnospeed.com.br/hc/article_attachments/8087753576855/mceclip2.png)

**Anexo II** :

![Imagem 4: Anexo II :](https://atendimento.tecnospeed.com.br/hc/article_attachments/8087822608023/mceclip3.png)

**![Imagem 5: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16869615346711) SOLUÇÃO:**

Para verificar o código GTIN informado no cadastro do produto é necessário realizar o passo a passo abaixo:

Acessar: Cadastro do produto
Aba: Imposto 
Campo: EAN/GTIN Produto p/ NF-e

Nele consta as opções onde poderá estar registrado o GTIN:

![Imagem 6: Nele consta as opções onde poderá estar registrado o GTIN:](https://ajuda.sankhya.com.br/hc/article_attachments/16868797024151)

Após realizar a correção do código é necessário redigitar o item da nota e gerar o lote. 

Caso não seja necessário informar o GTIN é necessário colocar no campo EAN/GTIN Produto p/ NF-e a opção não informar.

![Imagem 7: Após realizar a correção do código é necessário redigitar o item da nota e gerar o lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16921078378135)

📌 Em caso de dúvidas sobre as regras a serem aplicadas para o seu processo, consulte o seu contador.

Segue os links para consultar o GTIN nacional e para consultar os códigos da Tabela Prefixo GS1

<https://dfe-portal.svrs.rs.gov.br/Nfe/Gtin>

<https://www.gs1.org/standards/id-keys/company-prefix>
