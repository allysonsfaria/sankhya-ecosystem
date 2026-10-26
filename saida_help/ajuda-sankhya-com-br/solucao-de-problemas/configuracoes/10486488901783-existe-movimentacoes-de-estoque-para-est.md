---
id: "10486488901783"
titulo: "Existe movimentações de estoque para este produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10486488901783-Existe-movimenta%C3%A7%C3%B5es-de-estoque-para-este-produto"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:03:24Z"
rotulos: ["Produtos", "Configuração", "Estoque", "CORE_E06628", "Rastreamento de Estoque", "Ativação de Rastreamento de Estoque", "Erro"]
---

# Existe movimentações de estoque para este produto

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19035502435735) MENSAGEM:**

[CORE\_E06628] Existe movimentações de estoque para este produto. A ativação do rastreamento deve ser feito pela tela de implantação.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19035540985879) SITUAÇÃO:**

Ao realizar alguma alteração no cadastro de Produtos > aba Medidas e Estoque > sub-aba Estoque,  a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19035502454039) CAUSA:**

Já existe uma linha de rastreamento de estoque para determinado produto.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19035540993815) SOLUÇÃO:**

Realize o reprocessamento pela tela Ativar/Reprocessar Rastreamento de Estoque/ST. Essa rotina visa ativar e reprocessar o Estoque/ST, assim, o sistema irá verificar se o produto já possui o Rastreamento de ST habilitado e, caso haja, a rotina deletará as linhas de rastreamento e irá processá-la novamente. Para mais informações sobre essa rotina, acesse o link abaixo:

[Ativar/Reprocessar Rastreamento de Estoque/ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854-Ativar-Reprocessar-Rastreamento-de-Estoque-ST)
