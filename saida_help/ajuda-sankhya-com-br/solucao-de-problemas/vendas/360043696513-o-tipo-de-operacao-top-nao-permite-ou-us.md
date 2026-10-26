---
id: "360043696513"
titulo: "O Tipo de Operação (TOP) não permite ou usuário está com o campo \"Altera Nota Fiscal Confirmada\" desmarcado ou o parâmetro EXCLUIRNOTACONF está desligado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043696513-O-Tipo-de-Opera%C3%A7%C3%A3o-TOP-n%C3%A3o-permite-ou-usu%C3%A1rio-est%C3%A1-com-o-campo-Altera-Nota-Fiscal-Confirmada-desmarcado-ou-o-par%C3%A2metro-EXCLUIRNOTACONF-est%C3%A1-desligado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-02T12:34:33Z"
rotulos: ["#criadoRoger", "#RevisadoClaudio", "CORE_E00891", "Configuração", "Segurança", "NF-e", "TOP", "Preferências", "TOP ou usuário sem permissão", "Habilite EXCLUIRNOTACONF ou ajuste TOP", "Verifique permissões de usuário"]
---

# O Tipo de Operação (TOP) não permite ou usuário está com o campo "Altera Nota Fiscal Confirmada" desmarcado ou o parâmetro EXCLUIRNOTACONF está desligado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16163886573207) MENSAGEM:**

[CORE\_E00891] O Tipo de Operação (TOP) não permite ou usuário está com o campo "Altera Nota Fiscal Confirmada" desmarcado ou o parâmetro EXCLUIRNOTACONF (Permite exclusão de notas confirmadas?) está desligado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16163917203607) SITUAÇÃO:**

Ao tentar realizar exclusão/alterações de nota fiscal confirmada é apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16163917207575) SOLUÇÃO:**

Para liberação de exclusão de notas confirmadas em sua base, temos as restrições abaixo que precisam ser analisadas conforme sua necessidade:

![Imagem 4: Liberação de forma Geral:](https://ajuda.sankhya.com.br/hc/article_attachments/16163886580375) Liberação de forma Geral:

**(2)** Acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)"** (Configurações » Avançado) e ligue o parâmetro **"EXCLUIRNOTACONF"**.

![Imagem 5: (2) Acesse a tela " Preferências " (Configurações » Avançado) e ligue o parâmetro "EXCLUIRNOTACONF" .](https://ajuda.sankhya.com.br/hc/article_attachments/14711754751639)

![Imagem 6: Liberação por Tipo de Operação - TOP:](https://ajuda.sankhya.com.br/hc/article_attachments/16163917212951) Liberação por Tipo de Operação - TOP:

**(2)** Acesse a tela de cadastros da TOP (Caminho de acesso: Comercial » Arquivos » Cadastro » Tipos de Operação).

**(2)** Na aba **"Geral"**, a opção **"Permitir alteração após confirmar"** deve estar marcada.

![Imagem 7: (2) Na aba "Geral" , a opção "Permitir alteração após confirmar" deve estar marcada.](https://ajuda.sankhya.com.br/hc/article_attachments/14711785327511)

![Imagem 8: Liberação por Usuário:](https://ajuda.sankhya.com.br/hc/article_attachments/16163917213847) Liberação por Usuário:

**(2)** Acesse a tela de **"[Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)"** (Caminho de acesso: Configurações » Controle de Acesso), na aba Segurança, a opção **"Altera registros confirmados"** deve estar marcada.

**(2)**Se a marcação **"Altera registros confirmados"** estiver realizada, mesmo que a TOP não permita alterar nota depois de confirmada, será possível realizar a alteração. Se a TOP permitir alteração, o sistema não usa esta marcação do cadastro de usuários e permite que todos os usuários alterem notas confirmadas.

![Imagem 9: (2) Se a marcação "Altera registros confirmados" estiver realizada, mesmo que a TOP não permita alterar nota depois de…](https://ajuda.sankhya.com.br/hc/article_attachments/14711770744983)

**![Imagem 10: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16163917215511) CAUSA**:

Ocorre quando a TOP do lançamento  e/ou o Usuário não possui permissões para alterar nota/pedido já confirmado.
