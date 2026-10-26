---
id: "31564859100567"
titulo: "ORA-20101: Grupo de usu?rio 0 n?o esta ativo. ORA-06512: em \"SANKHYA.TRG_INC_UPD_TSIUSU\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31564859100567-ORA-20101-Grupo-de-usu-rio-0-n-o-esta-ativo-ORA-06512-em-SANKHYA-TRG-INC-UPD-TSIUSU"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:33Z"
rotulos: ["Configuração", "Grupo de Usuários", "ORA-20101", "ORA-06512", "ORA-04088", "Controle de Acesso", "Grupo de usuário 0 não está ativo", "em \"SANKHYA.TRG_INC_UPD_TSIUSU\" linha 16", "erro durante a execução do gatilho 'SANKHYA.TRG_INC_UPD_TSIUSU'", "Erro"]
---

# ORA-20101: Grupo de usu?rio 0 n?o esta ativo. ORA-06512: em "SANKHYA.TRG_INC_UPD_TSIUSU"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31564859095319) **MENSAGEM:**

[ORA-20101]: Grupo de usuário 0 não está ativo.
[ORA-06512]: em "SANKHYA.TRG\_INC\_UPD\_TSIUSU", linha 16
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_UPD\_TSIUSU'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31564859097495)SOLUÇÃO:**

Para que o usuário possa ser criado no Sankhya Om, é necessário que o grupo de usuários ao qual ele será associado esteja ativo. Para ativá-lo, acesse a tela **Grupo de Usuário** (Configurações » Controle de Acesso » Grupo de Usuários), localize o grupo desejado para realizar a ativação e ative-o.

![Imagem 3: Para que o usuário possa ser criado no Sankhya Om, é necessário que o grupo de usuários ao qual ele será associado…](https://ajuda.sankhya.com.br/hc/article_attachments/31570959507223)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31564827905303)CAUSA:**

O grupo de usuários ao qual o funcionário está sendo vinculado está desativado.
