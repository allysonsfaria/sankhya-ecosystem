---
id: "24602150207639"
titulo: "Falha no cálculo de preço dinâmico: Para o modelo de nota XX deve ser informado um parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24602150207639-Falha-no-c%C3%A1lculo-de-pre%C3%A7o-din%C3%A2mico-Para-o-modelo-de-nota-XX-deve-ser-informado-um-parceiro"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:46:35Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "Nota Fiscal", "Preferências", "CORE_E02293", "Falha cálculo preço dinâmico", "Definir modelo de nota/pedido", "Modelo sem código e parceiro"]
---

# Falha no cálculo de preço dinâmico: Para o modelo de nota XX deve ser informado um parceiro

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24602176683159) **MENSAGEM:**

[CORE\_E02293] Falha no cálculo de preço dinâmico: Para o modelo de nota XX deve ser informado um parceiro

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24602176688663) **SOLUÇÃO:**

Acesse a tela **"Preferências"** (Caminho: Configurações » Avançado » Preferências), busque pelo parâmetro **"Nota modelo para cálculo de preço dinâmico - MODCALCPRECDIN"** e nele informe o modelo de nota/pedido que será utilizado para gerar um Cabeçalho transient.

No caso, esse cabeçalho não será persistido, pois ele serve apenas para fins de cálculo de impostos. Em algumas situações, como por exemplo a Consulta de Produtos aberta diretamente, não se tem o cabeçalho para calcular impostos.

Também dentro da tela **"Consulta de produtos"** verifique se tem algum filtro ativo. Caso tenha e ele seja importante para a busca, forneça as informações definidas pelas condições dele (por exemplo, parceiro, natureza, marca, grupo de produto, etc).

Por outro lado, se este filtro não for decisivo para a busca, desative-o.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24602150198167)**CAUSA:**

Ocorre quando o modelo utilizado não consta um CODIGO E PARCEIRO.
