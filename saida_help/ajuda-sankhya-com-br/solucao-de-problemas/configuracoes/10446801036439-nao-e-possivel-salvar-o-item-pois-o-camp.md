---
id: "10446801036439"
titulo: "Não é possível salvar o item '', pois o campo 'Solicitação de Compra' está marcado mas a TOP '' não permite gerar solicitação de compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10446801036439-N%C3%A3o-%C3%A9-poss%C3%ADvel-salvar-o-item-pois-o-campo-Solicita%C3%A7%C3%A3o-de-Compra-est%C3%A1-marcado-mas-a-TOP-n%C3%A3o-permite-gerar-solicita%C3%A7%C3%A3o-de-compra"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:03:33Z"
rotulos: ["Produtos", "Configuração", "TOP", "Estoque", "Financeiro", "CORE_E03244", "Erro ao Salvar Item por Configuração Incorreta de Solicitação de Compra"]
---

# Não é possível salvar o item '', pois o campo 'Solicitação de Compra' está marcado mas a TOP '' não permite gerar solicitação de compra

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19297974918167) MENSAGEM:**

[CORE\_E03244] Não é possível salvar o item '', pois o campo 'Solicitação de Compra' está marcado mas a TOP '' não permite gerar solicitação de compra.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19298019482391) SITUAÇÃO:**

Ao tentar salvar o item no lançamento a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19298019488407) CAUSA:**

Quando as configurações na TOP não estão devidamente configuradas.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19298019493143) SOLUÇÃO:**

Verifique se no cadastro do **produto** (Caminho de acesso à tela: Configurações » Cadastros » Produtos) o campo "Solicita compra?" está selecionado.

![Imagem 5: Verifique se no cadastro do produto (Caminho de acesso à tela: Configurações » Cadastros » Produtos) o campo "Solicita…](https://ajuda.sankhya.com.br/hc/article_attachments/10446492564119)

Quando acionar a marcação **"Solicita Compra?"**, estará informando que o produto faz parte do processo de Solicitação de Compra. Abaixo, temos duas configurações ligadas a este processo:

No **[Cadastro de Tipos de Operações - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)** (Caminho de acesso à tela: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes), as marcações **"Faturar Produtos com Estoque na Confirmação?"** e **"Gera Solicitação de Compra na Confirmação?"** devem estar acionadas.

![Imagem 6: No Cadastro de Tipos de Operações - TOP (Caminho de acesso à tela: Financeiro » Arquivos » Cadastros » Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/19298019494295)
