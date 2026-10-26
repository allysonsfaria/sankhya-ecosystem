---
id: "360043723714"
titulo: "Transferência de etapas não permite passar para a próxima etapa durante a produção, saiba como proceder"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043723714-Transfer%C3%AAncia-de-etapas-n%C3%A3o-permite-passar-para-a-pr%C3%B3xima-etapa-durante-a-produ%C3%A7%C3%A3o-saiba-como-proceder"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T16:00:07Z"
rotulos: ["#PUBLIFER", "#revisadohugo", "Produtos", "Configuração", "Segurança", "Produção", "Preferências", "Defina etapas para movimentação e nota", "Habilite \"Permite transferir etapas de Produção\"", "Etapa \"0\" deve ser inicial"]
---

# Transferência de etapas não permite passar para a próxima etapa durante a produção, saiba como proceder

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16422010707735) MENSAGEM:**

Transferência de etapas não permite passar para a próxima etapa durante a produção

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16422010708631) SOLUÇÃO:**

![Imagem 3: Em Avançado » Preferências » Todas Preferências , parametrizar o parâmetro "PAETAPA" :](https://ajuda.sankhya.com.br/hc/article_attachments/16421969925655) Em Avançado » Preferências » Todas Preferências, parametrizar o parâmetro **"PAETAPA"**:

Nesse parâmetro defina a etapa, ou lista de etapas, nas quais será necessário movimentar o produto acabado. A nota gerada nesta etapa terá, além das MP'S, o produto acabado.

![Imagem 4: Nesse parâmetro defina a etapa, ou lista de etapas, nas quais será necessário movimentar o produto acabado. A nota…](https://ajuda.sankhya.com.br/hc/article_attachments/360058891974)

![Imagem 5: Na tela Arquivos » Controle de Acesso » Usuários , selecione o usuário responsável pela transferência de etapas e…](https://ajuda.sankhya.com.br/hc/article_attachments/16422010712087) Na tela Arquivos » Controle de Acesso » Usuários, selecione o usuário responsável pela transferência de etapas e certifique-se que na aba **Segurança** a opção **"Permite transferir etapas de Produção"** está marcada.

![Imagem 6: Nas configurações de etapas, a fórmula de composição do produto deverá ter, obrigatoriamente, a etapa "0" como inicial.](https://ajuda.sankhya.com.br/hc/article_attachments/16421969930007) Nas configurações de etapas, a fórmula de composição do produto deverá ter, obrigatoriamente, a etapa "0" como inicial.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16421969932183) CAUSA:**

Situação ocorrerá quando o usuário não possui permissão para transferir etapas e/ou não foi definido o parâmetro PAETAPA.
