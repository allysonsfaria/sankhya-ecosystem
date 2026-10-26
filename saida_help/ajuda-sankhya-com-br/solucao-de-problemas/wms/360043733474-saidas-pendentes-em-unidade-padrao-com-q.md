---
id: "360043733474"
titulo: "Saídas pendentes em unidade padrão com qtd. incorreta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733474-Sa%C3%ADdas-pendentes-em-unidade-padr%C3%A3o-com-qtd-incorreta"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:59:18Z"
rotulos: ["#criadoRoger", "#RevisadoWellington", "Produtos", "Configuração", "WMS", "Estoque", "Erro de Saídas Pendentes com Quantidade Incorreta", "Erro"]
---

# Saídas pendentes em unidade padrão com qtd. incorreta

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16198957187223) MENSAGEM:**

[Erro: SQL-50001] Saídas pendentes em unidade padrão com qtd. incorreta.
Produtos: xxx Endereço:xxx Unidades:xx Saidas pendentes:x.xxxx.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16198957190807) SITUAÇÃO:**

Ao enviar uma OC(Ordem de Carga), para expedição(WMS), pela Rotina Formação de Carga, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16198957193879) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Configurações » Cadastros » Produtos » Produtos , a ba Geral , preencha o Campo: "Unidade Padrão".](https://ajuda.sankhya.com.br/hc/article_attachments/16198957197207) Acesse: Configurações » Cadastros » Produtos » Produtos, aba **Geral**, preencha o Campo: **"Unidade Padrão".**

![Imagem 5: Acesse: Configurações » Cadastros » Produtos » Produtos , a ba Geral , preencha o Campo: "Unidade Padrão".](https://ajuda.sankhya.com.br/hc/article_attachments/14499206758935)

![Imagem 6: Acesse: Configurações » Cadastros » Produtos » Produtos , a ba WMS , e cadastre o Endereçamento (Ter um registro da…](https://ajuda.sankhya.com.br/hc/article_attachments/16198941903255) Acesse: Configurações » Cadastros » Produtos » Produtos, aba **WMS**, e cadastre o Endereçamento (Ter um registro da Unidade UN).

![Imagem 7: Acesse: Configurações » Cadastros » Produtos » Produtos , a ba WMS , e cadastre o Endereçamento (Ter um registro da…](https://ajuda.sankhya.com.br/hc/article_attachments/14499213563159)

![Imagem 8: Acesse: Configurações » Cadastros » Produtos » Produtos , a ba Unidades Alternativas e realize um registro da Unidade…](https://ajuda.sankhya.com.br/hc/article_attachments/16198941905687) Acesse: Configurações » Cadastros » Produtos » Produtos, aba **Unidades Alternativas** e realize um registro da Unidade maior que a Unidade Padrão.

![Imagem 9: Acesse: Configurações » Cadastros » Produtos » Produtos , a ba Unidades Alternativas e realize um registro da Unidade…](https://ajuda.sankhya.com.br/hc/article_attachments/14499264636183)

**![Imagem 10: C AUSA](https://ajuda.sankhya.com.br/hc/article_attachments/16198957204759) CAUSA**

Para evitar que este erro aconteça é necessário configurar a unidade do produto no picking com a menor unidade, a qual geralmente é a unidade padrão.

**Não** configurar Unidade Alternativa do produto no Picking.
