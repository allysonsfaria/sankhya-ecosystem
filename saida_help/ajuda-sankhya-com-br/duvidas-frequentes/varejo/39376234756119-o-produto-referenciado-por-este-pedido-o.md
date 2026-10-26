---
id: "39376234756119"
titulo: "O produto referenciado por este pedido ou nota já está associado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39376234756119-O-produto-referenciado-por-este-pedido-ou-nota-j%C3%A1-est%C3%A1-associado"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-08-01T02:32:11Z"
rotulos: ["Produtos", "Fiscal", "NF-e", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# O produto referenciado por este pedido ou nota já está associado.

**MENSAGEM**

O produto referenciado por este pedido ou nota já está associado

**SITUAÇÃO**

Esta mensagem aparece ao tentar incluir um produto em uma nota fiscal de devolução após realizar o **"cancelamento extemporâneo"** de uma devolução anterior. Mesmo após a exclusão da primeira devolução do sistema, o produto permanece vinculado à nota original, impedindo sua inclusão em uma nova devolução.

**SOLUÇÃO**

Para resolver este problema, siga os passos abaixo:

**(1)** Acesse a tela de **"Portal de Vendas"** (Comercial Consulta) e localize a nota fiscal de devolução que está apresentando o erro.

**(2)** Exclua completamente a **"nota fiscal de devolução"** que foi criada anteriormente.

**(3)** Localize a **"nota fiscal de origem"** (a nota que originou a devolução, é possível identificar através da opção Documentos relacionados ou consultando na Tabela de ligação TGFVAR).

**(4)** Utilize o botão **"Dev/Est"** disponível na própria nota fiscal de origem para gerar uma nova devolução.

**(5)** Inclua os produtos desejados na nova nota de devolução gerada através do botão **"Dev/Est"**.

**CAUSA**

O erro ocorre porque, ao criar manualmente uma nova nota de devolução após o **"Cancelamento Extemporâneo"**, o sistema mantém o vínculo do produto com a nota fiscal original na tabela **"TGFITE"**. Esse vínculo impede que o mesmo produto seja associado novamente a outra devolução. Ao utilizar o botão **"Dev/Est"** diretamente da nota de origem, o sistema gerencia corretamente os vínculos entre os itens, eliminando o conflito de associação.
