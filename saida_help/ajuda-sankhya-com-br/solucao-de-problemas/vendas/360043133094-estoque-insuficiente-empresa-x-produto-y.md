---
id: "360043133094"
titulo: "Estoque insuficiente. Empresa: X Produto: YYYY Local: ZZZZZ Controle: XPTO Validação do estoque: XPTO"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043133094-Estoque-insuficiente-Empresa-X-Produto-YYYY-Local-ZZZZZ-Controle-XPTO-Valida%C3%A7%C3%A3o-do-estoque-XPTO"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-13T18:57:30Z"
rotulos: ["#criadoRoger", "CORE_E04794", "CORE_E04796", "Produtos", "Configuração", "TOP", "Estoque", "CORE_E01128", "CORE_E04686", "CORE_E01167", "CORE_E04792", "CORE_E04176", "CORE_E04795", "Falta de estoque para o item especificado", "Falha ao inserir dados para buscar o item em estoque", "Verifique estoque do produto e ajuste se necessário", "Erro"]
---

# Estoque insuficiente. Empresa: X Produto: YYYY Local: ZZZZZ Controle: XPTO Validação do estoque: XPTO

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16147789340951) MENSAGEM:**

[CORE\_E04176] Estoque insuficiente. Empresa: X Produto: YYYY Local: ZZZZZ

[CORE\_E04794] Estoque insuficiente. Empresa: X Produto: YYYY Local: ZZZZZ Controle: XPTO Validação do estoque: XPTO.

**![Imagem 2: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16147789366807) CAUSA**:

 Ocorre quando no lançamento de um item não foi inserido os dados para buscar o item em estoque.

**![Imagem 3: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16147789344535) SOLUÇÃO**:

Para um melhor controle e gerenciamento do Estoque, identifique as validações de estoque dos produtos do lançamento, como:

![Imagem 4: Realize a validação de Estoque do Grupo de Produtos: Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/article_attachments/16147795305495) Realize a validação de Estoque do Grupo de Produtos: [Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602054)

![Imagem 5: Verifique se o produto possui estoque, considerando Empresa, Local e Controle (quando houver): Comercial » Gerente »…](https://ajuda.sankhya.com.br/hc/article_attachments/16147795312919) Verifique se o produto possui estoque, considerando Empresa, Local e Controle (quando houver): [Comercial » Gerente » Gerência de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111253) ou [Comercial » Consulta » Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)

![Imagem 6: Se houver estoque físico, considere verificar se há inconsistências entre estoque físico e do sistema em: Configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/16147789352855) Se houver estoque físico, considere verificar se há inconsistências entre estoque físico e do sistema em: [Configurações » Avançado » Verificação de Saldo de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612054)

![Imagem 7: Se o produto for lançado pela Consulta de Produtos, selecione o item de acordo com seu Local e Controle, para que o…](https://ajuda.sankhya.com.br/hc/article_attachments/16147795320599) Se o produto for lançado pela Consulta de Produtos, selecione o item de acordo com seu Local e Controle, para que o sistema carregue esses dados para a grade de itens.

![Imagem 8: Verifique se as Notas de Compras dos Produtos estão devidamente lançados e confirmados, caso identifique…](https://ajuda.sankhya.com.br/hc/article_attachments/16147789360151) Verifique se as Notas de Compras dos Produtos estão devidamente lançados e confirmados, caso identifique inconsistências, considere efetuar Ajuste de Estoque através da melhor prática via Inventário de Ajuste de estoque.

![Imagem 9: Importante:](https://ajuda.sankhya.com.br/hc/article_attachments/18133344111511) **Importante:**

Verifique o processo produtivo e caso necessário, realize a alteração do modelo de nota e pedido, para um que esteja configurado corretamente para a empresa desejada.

**![Imagem 10: Observação:](https://ajuda.sankhya.com.br/hc/article_attachments/16147795327383) Observação:**

Esta mensagem pode ocorrer nos casos em que o pedido de origem reservou o estoque, mas o campo da TOP de origem, aba **"Validações"**: **Validar Estoque p/ Reservar:** estava desmarcado. Nesse caso, ao tentar faturar esse pedido pela opção normal "Faturar" irá emitir a mensagem de estoque insuficiente.
