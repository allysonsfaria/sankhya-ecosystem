---
id: "7116849779351"
titulo: "O Grupo de usuário 'X' não pode usar a TOP 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7116849779351-O-Grupo-de-usu%C3%A1rio-X-n%C3%A3o-pode-usar-a-TOP-Y"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-02T12:27:42Z"
rotulos: ["Configuração", "Segurança", "TOP", "CORE_E02939", "Restrições de Uso da TOP para Grupos de Usuário", "Erro", "Grupo de Usuário"]
---

# O Grupo de usuário 'X' não pode usar a TOP 'Y'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16490877854871) MENSAGEM:**

[CORE\_E02939] O Grupo de usuário 'X' não pode usar a TOP 'Y'.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16490877857175) CAUSA:**

Ocorre quando está sendo utilizado um usuário, vinculado a um grupo de usuários, que tenha restrições e/ou validações em relação a 'TOP' utilizada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16490877863063) SOLUÇÃO:**

TOP com restrições/exceções:

Anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo.

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros).

**(1)** Acione o botão **"Outras Opções",** em seguida clique em: **"Restrições/Exceções".**

![Imagem 4: (1) Acione o botão "Outras Opções", em seguida clique em: "Restrições/Exceções".](https://ajuda.sankhya.com.br/hc/article_attachments/15938758696471)

**(1)** Verifique se existem regras vinculadas para **"Usuário/Grupo Usuário"**:

![Imagem 5: (1) Verifique se existem regras vinculadas para "Usuário/Grupo Usuário" :](https://ajuda.sankhya.com.br/hc/article_attachments/15938777940119)

- No exemplo acima, a TOP não poderá ser lançada por **usuários que estão vinculados ao grupo de usuário 34 - CAIXA PDV**;
- Para utilização dessa TOP com esse grupo de usuários, essa linha deverá ser excluída de exceções. Para tal, realize alinhamento interno e compreenda se essa exclusão é válida para o cenário atual da empresa.
- Caso a marcação fosse para 'Restrições' (só pode ser usado com), o grupo de usuário desejado deverá constar nessa lista.
