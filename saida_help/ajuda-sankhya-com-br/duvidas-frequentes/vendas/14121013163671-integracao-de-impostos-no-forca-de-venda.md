---
id: "14121013163671"
titulo: "Integração de impostos no Força de Vendas da Máxima "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14121013163671-Integra%C3%A7%C3%A3o-de-impostos-no-For%C3%A7a-de-Vendas-da-M%C3%A1xima"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:59:33Z"
rotulos: ["Alíquotas", "Configuração", "ICMS", "Impostos", "Integração", "Pedidos de vendas não integram ICMS e ST", "Configure alíquotas ICMS: Tipo 1 (produto/grupo) e Tipo 2 (sem exceção)", "Pedidos integram confirmados; exceções não suportadas causam problema", "Força de Vendas"]
---

# Integração de impostos no Força de Vendas da Máxima 

**![Imagem 1: SITUAÇÃO: Os pedidos de vendas feitos no Força de Vendas da Máxima não estão Integrando os impostos de ICMS e ST.](https://ajuda.sankhya.com.br/hc/article_attachments/16920530688535) SITUAÇÃO:**
Os pedidos de vendas feitos no Força de Vendas da Máxima não estão Integrando os impostos de ICMS e ST.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16920530694807) SOLUÇÃO:**

Não são todas as exceções que são suportadas/integradas com a Máxima.
Para que as informações sejam levadas para Máxima, é preciso ter o seguinte cenário na configuração das alíquotas de ICMS >> Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS, aba **"Geral"**:

**Exceções:**

**Tipo 1:** por produto
**Tipo 2:** sem exceção

**ou**

**Tipo 1:** por grupo de ICMS do produto
**Tipo 2:** sem exceção

Caso tenha algum cenário diferente, por exemplo: sem exceção + sem exceção **ou** por grupo de ICMS do parceiro, não será integrado com a Máxima.

(1)** Dúvida:**

É possível que um pedido de venda seja integrado como 'Não Confirmado?'

R: Não é possível. Os pedidos são integrados já confirmados para existir consistência entre os dois sistemas.

**![Imagem 3: CAUSA: Problema ocorre quando a alíquota de ICMS está configurada com tipos de exceções que não são suportados pela…](https://ajuda.sankhya.com.br/hc/article_attachments/16920530718999) CAUSA:**
Problema ocorre quando a alíquota de ICMS está configurada com tipos de exceções que não são suportados pela Máxima.
