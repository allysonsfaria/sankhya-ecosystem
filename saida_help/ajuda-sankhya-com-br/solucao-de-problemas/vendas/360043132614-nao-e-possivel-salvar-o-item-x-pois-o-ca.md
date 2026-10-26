---
id: "360043132614"
titulo: "Não é possível salvar o item 'X', pois o campo 'Solicitação de Compra' está marcado mas o produto 'X' não permite gerar solicitação de compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043132614-N%C3%A3o-%C3%A9-poss%C3%ADvel-salvar-o-item-X-pois-o-campo-Solicita%C3%A7%C3%A3o-de-Compra-est%C3%A1-marcado-mas-o-produto-X-n%C3%A3o-permite-gerar-solicita%C3%A7%C3%A3o-de-compra"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-02T16:43:38Z"
rotulos: ["#Revisado Silvio", "#PUBLIFER", "Produtos", "Configuração", "TOP", "Solicitação de Compra", "CORE_E03245", "Campo 'Solicitação de Compra' não compatível", "Produtos não configurados para gerar solicitação", "Ajuste configurações em Produtos e TOP", "Erro"]
---

# Não é possível salvar o item 'X', pois o campo 'Solicitação de Compra' está marcado mas o produto 'X' não permite gerar solicitação de compra

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16144984494999) MENSAGEM:**

[CORE\_E03245] "Não é possível salvar o item 'X', pois o campo 'Solicitação de Compra' está marcado mas o produto 'X' não permite gerar solicitação de compra."

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145017347479) SITUAÇÃO:**

Mensagem apresentada ao tentar confirmar movimentos (Pedidos de venda, Pedidos de requisição, Venda ou Requisição) parametrizadas com a marcação 'Gerar solicitação de compra na confirmação" sem  que produtos utilizados estejam devidamente parametrizados.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16144984499223) SOLUÇÃO:**

![Imagem 4: Acesse a tela " Produtos " (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) , na aba "Geral"…](https://ajuda.sankhya.com.br/hc/article_attachments/16145017354519) Acesse a tela **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), na aba **"Geral"** identifique o **"Grupo"** vinculado ao respectivo produto.

![Imagem 5: Acesse a tela " Grupos de Produtos/Serviços " (Caminho de acesso: Configurações » Cadastros » Produtos » Grupos de…](https://ajuda.sankhya.com.br/hc/article_attachments/16145017355415) Acesse a tela **"[Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294)"** (Caminho de acesso: Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços), localize o grupo vinculado ao produto e na aba **"Geral"** marque a opção abaixo:

- **Participa da opção "Gerar Solicitação de Compra na Confirmação?" do cadastro da TOP**?

![Imagem 6: Participa da opção "Gerar Solicitação de Compra na Confirmação?" do cadastro da TOP ?](https://ajuda.sankhya.com.br/hc/article_attachments/14690090152215)

![Imagem 7: No cadastro de “ Tipos de Operação” (TOP), marque o campo “Gera Solicitação de Compra na Confirmação” .](https://ajuda.sankhya.com.br/hc/article_attachments/16144984506007) No cadastro de **“[Tipos de Operação”](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)** (TOP), marque o campo **“Gera Solicitação de Compra na Confirmação”**.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16144984508823) CAUSA:**

Mensagem apresentada ao confirmar no sistema 'Pedidos de venda', 'pedidos de requisição', 'venda' ou 'requisição', com produtos parametrizados para 'Solicitação de Compra', sem que as configurações de TOP e Grupo de produtos tenham sido devidamente realizadas.
