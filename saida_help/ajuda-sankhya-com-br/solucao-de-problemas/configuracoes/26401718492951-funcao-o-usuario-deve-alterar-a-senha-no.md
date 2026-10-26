---
id: "26401718492951"
titulo: "Função 'O usuário deve alterar a senha no próximo logon' e parametro 'DIASEXPSENHA' não funcionam"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26401718492951-Fun%C3%A7%C3%A3o-O-usu%C3%A1rio-deve-alterar-a-senha-no-pr%C3%B3ximo-logon-e-parametro-DIASEXPSENHA-n%C3%A3o-funcionam"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:42:23Z"
rotulos: ["Configuração", "Segurança", "Usuário", "Autenticação", "Sankhya ID", "Passos para resolver", "Razão do erro", "Detalhe do erro", "O usuário deve alterar a senha no próximo logon", "parametro 'DIASEXPSENHA' não funcionam"]
---

# Função 'O usuário deve alterar a senha no próximo logon' e parametro 'DIASEXPSENHA' não funcionam

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26438784602135) **SITUAÇÃO:**

Configurado o usuario com a marcação "O usuário deve alterar a senha no próximo logon' e parametro "DIASEXPSENHA" mas continua sem forçar a alteração.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26401718476183)SOLUÇÃO:**

A partir do momento em que o **usuário do OM é vinculado ao usuário do Sankhya ID, o usuário do Sankhya ID se torna dominante**. Portanto, é recomendado que, ao possuir um vínculo com o Sankhya ID, o login seja feito apenas com o usuário e a senha do Sankhya ID. Trata-se, portanto, de um comportamento do sistema.

**Caso ainda assim queira forçar a alteração da senha do usuário Sankhya, desvincule o Sankhya ID do usuário, seguindo os passos:**

![Imagem 3: Logue com o usuário do Sankhya ID/ Sankhya OM;](https://ajuda.sankhya.com.br/hc/article_attachments/26438821317527) Logue com o usuário do Sankhya ID/ Sankhya OM;

![Imagem 4: No ícone de usuário, localizado no canto superior direito da tela, clique no botão "Desvincular";](https://ajuda.sankhya.com.br/hc/article_attachments/26438821318679) No ícone de usuário, localizado no canto superior direito da tela, clique no botão **"Desvincular";**

![Imagem 5: No popup apresentado, clique no botão Desvincular novamente;](https://ajuda.sankhya.com.br/hc/article_attachments/26438821320087) No popup apresentado, clique no botão Desvincular novamente;

![Imagem 6: Pronto o usuário do OM está desvinculado do usuário do ID;](https://ajuda.sankhya.com.br/hc/article_attachments/26438784612503) Pronto o usuário do OM está desvinculado do usuário do ID;

Após realizar os passos anteriores, será possível forçar a alteração de senha do usuário do Sankhya OM.

Depois de realizar a alteração da senha, pode-se vincular o e-mail do sankhya ID novamente.

**Observação:** uma alternativa adicional é **desligar** o parâmetro **"HABILITAACCOUNT - Habilita Sankhya ID"**, realizar o procedimento de configuração da marcação no usuário ou parâmetro de expiração de senha, aguardar que todos os usuários realizem o login e alterem a senha e **ligar** o parâmetro novamente. Porém, todos terão que refazer o vínculo manualmente. Essa configuração é recomendada em casos de **extrema necessidade**.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26401718480407)CAUSA:**

É um comportamento, o vinculo com Sankhya ID é dominante, fazendo com que essas configurações não sejam válidas para os usuários com conta do Sankhya ID vinculado.
