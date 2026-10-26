---
id: "360043138654"
titulo: "A TOP não atualiza saldo FLEX e o acréscimo/decréscimo está calculado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043138654-A-TOP-n%C3%A3o-atualiza-saldo-FLEX-e-o-acr%C3%A9scimo-decr%C3%A9scimo-est%C3%A1-calculado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:32Z"
rotulos: ["Configuração", "NF-e", "TOP", "Estoque", "ORA-06512", "Saldo FLEX Devolução"]
---

# A TOP não atualiza saldo FLEX e o acréscimo/decréscimo está calculado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16309937824151) MENSAGEM:**

A TOP não atualiza saldo FLEX e o acréscimo/decréscimo está calculado. Nota de Nro Único: XXXXX.

[ORA-06512]: em "SANKHYA.TRG\_INC\_TGFITE\_FLEX", line 147

[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_TGFITE\_FLEX'

![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309980295831) **SITUAÇÃO:**

Ao lançar uma NF-e de Devolução, ocorre a mensagem.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16309937838487) **CAUSA:**

Ao clicar para devolver, tentar faturar ou duplicar um lançamento, o sistema carrega as informações quanto ao Flex do pedido/nota e tenta incluir nesta nova nota. Com isso, caso a TOP de devolução não esteja configurada para trabalhar com flex, ocorre a mensagem.

![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309937829399) **SOLUÇÃO:**

Para correção siga os passos abaixo.

![Imagem 5: Acesse o caminho Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16309980300567) Acesse o caminho Comercial » Arquivo » Cadastros » [**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)

![Imagem 6: Selecione a TOP Destino que está sendo utilizada no procedimento que retornou a mensagem de validação.](https://ajuda.sankhya.com.br/hc/article_attachments/16309937835031) Selecione a TOP Destino que está sendo utilizada no procedimento que retornou a mensagem de validação.

**(2)** Aba "**Geral",** Campo "**Atualizar Acréscimos/Decréscimos",** marque a opção que seja **diferente** de "**Não Atualizar".**
