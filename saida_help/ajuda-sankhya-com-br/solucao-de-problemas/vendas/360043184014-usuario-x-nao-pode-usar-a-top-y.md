---
id: "360043184014"
titulo: "Usuário 'X' não pode usar a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043184014-Usu%C3%A1rio-X-n%C3%A3o-pode-usar-a-TOP-Y"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:25Z"
rotulos: ["#PUBLIFER", "CORE_E02413", "Configuração", "TOP", "Natureza", "Usuário não pode usar TOP", "Verifique e ajuste restrições/exceções no TOP", "Restrição ou validação no Código 'Natureza' e TOP", "Erro", "Restrições"]
---

# Usuário 'X' não pode usar a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16310069877911) MENSAGEM:**

[CORE\_E02413] Usuário 'X' não pode usar a TOP 'Y'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16310071889303) SOLUÇÃO:**

TOP com restrições/exceções:

![Imagem 3: Anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/16310069882519) Anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo.

![Imagem 4: Acesse a tela " Tipos de Operação - TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros ).](https://ajuda.sankhya.com.br/hc/article_attachments/16310071895191) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros).

![Imagem 5: Acione o botão " Outras Opções " » " Restrições/Exceções ".](https://ajuda.sankhya.com.br/hc/article_attachments/16310069888535) Acione o botão **"[Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114#botooutrasopes...)"** » **"[Restrições/Exceções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#restricoeseexcecoes)".**

![Imagem 6: Acione o botão " Outras Opções " » " Restrições/Exceções ".](https://ajuda.sankhya.com.br/hc/article_attachments/14393173445143)

![Imagem 7: Verifique se existem regras vinculadas para "Usuário/Grupo Usuário" :](https://ajuda.sankhya.com.br/hc/article_attachments/16310069891735) Verifique se existem regras vinculadas para **"Usuário/Grupo Usuário"**:

![Imagem 8: Verifique se existem regras vinculadas para "Usuário/Grupo Usuário" :](https://ajuda.sankhya.com.br/hc/article_attachments/14393173446679)

**(2)** No exemplo acima, a TOP não poderá ser usada com o usuário 18-GERENTE.

![Imagem 9: Para utilização dessa TOP com esse usuário, exclua essa linha de exceções. Para tal, realize alinhamento interno e…](https://ajuda.sankhya.com.br/hc/article_attachments/16310071904023) Para utilização dessa TOP com esse usuário, exclua essa linha de exceções. Para tal, realize alinhamento interno e compreenda se essa exclusão é válida para o cenário atual da empresa.

![Imagem 10: Caso a marcação fosse para ' Restrições ' (só pode ser usado com), o usuário desejado deverá constar nessa lista.](https://ajuda.sankhya.com.br/hc/article_attachments/16310071909527) Caso a marcação fosse para 'Restrições' (só pode ser usado com), o usuário desejado deverá constar nessa lista.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16310071910935) CAUSA:**

Ocorre quando está sendo utilizado um Código 'Natureza' que tenha restrições e/ou validações em relação a 'TOP' utilizada.
