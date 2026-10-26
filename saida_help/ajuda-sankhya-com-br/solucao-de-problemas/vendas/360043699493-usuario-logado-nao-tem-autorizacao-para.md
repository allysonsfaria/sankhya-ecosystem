---
id: "360043699493"
titulo: "Usuário logado não tem autorização para alterar SubOS desta fila"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043699493-Usu%C3%A1rio-logado-n%C3%A3o-tem-autoriza%C3%A7%C3%A3o-para-alterar-SubOS-desta-fila"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:26Z"
rotulos: ["Configuração", "Segurança", "Parceiro", "Ordem de Serviço", "Controle de Acesso", "Usuário não autorizado a alterar SubOS", "Ajuste controle de acesso e parâmetros", "Falta de autorização ou configuração de fila"]
---

# Usuário logado não tem autorização para alterar SubOS desta fila

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16163743468951)MENSAGEM:**

Usuário logado não tem autorização para alterar SubOS desta fila.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16163743473559) SITUAÇÃO:**

Ao tentar alterar uma Ordem de Serviço, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16163775648023) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Configurações » Controle de Acesso » Relacionamento entre Usuários](https://ajuda.sankhya.com.br/hc/article_attachments/16163743477911) Configurações » Controle de Acesso » Relacionamento entre Usuários

**(2)** Com o usuário que está tentando alterar a SubOS, caso seja diferente do usuário que lançou a OS-Ordem de Serviço.

**(2)** Insira o usuário na aba **"Gerente"**, de forma que o usuário que lançou a negociação seja Subordinado a ele e esteja devidamente cadastrado na aba **"Subordinado".**

**(2)** Nesta tela também é possível configurar usuário Membro de alguma Fila, inserindo o mesmo na aba: Membros da Fila.

**(3)**Para conseguir alterar a SubOS o parâmetro **"SERVGERALTSUB"** deve estar ligado.

![Imagem 5: (3) Para conseguir alterar a SubOS o parâmetro "SERVGERALTSUB" deve estar ligado.](https://ajuda.sankhya.com.br/hc/article_attachments/14713235309847)

![Imagem 6: Após os ajustes, execute novamente o processo.](https://ajuda.sankhya.com.br/hc/article_attachments/16163743483287) Após os ajustes, execute novamente o processo.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16163743484823) CAUSA:**

Ocorre quando a tentativa de alteração na Ordem de Serviço é realizada por outro usuário e/ou seu respectivo Gerente, que não efetuou o lançamento inicial e não é membro da fila.
