---
id: "13309976352535"
titulo: "ORA-00604: ocorreu um erro no nível 1 SQL recursivo ORA-01000: máximo de cursores abertos excedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13309976352535-ORA-00604-ocorreu-um-erro-no-n%C3%ADvel-1-SQL-recursivo-ORA-01000-m%C3%A1ximo-de-cursores-abertos-excedido"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T15:00:14Z"
rotulos: ["Configuração", "Oracle", "ORA-01000", "Ajuste de parâmetros", "ORA-00604", "Parâmetro", "ORA-00604 ORA-01000 open_cursors", "Erro", "open_cursors"]
---

# ORA-00604: ocorreu um erro no nível 1 SQL recursivo ORA-01000: máximo de cursores abertos excedido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17147593216791) MENSAGEM:**

[ORA-00604]: ocorreu um erro no nível 1 SQL recursivo
[ORA-01000]: máximo de cursores abertos excedido

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17147563313559) SOLUÇÃO:**

Com o usuário sys (conta criada quando o banco foi instalado), conecte-se no servidor Oracle, via putty ou diretamente no servidor, e execute o procedimento descrito abaixo para verificar o parâmetro: **open\_cursors**.

[oracle@oracletestes ~]$ sqlplus "/as sysdba"

Conferir valor do parâmetro open\_cursors

SQL> show parameter open\_cursors
NAME TYPE VALUE
----------------------------------- ----------- ------------------------------
open\_cursors integer 300

Ajustar parâmetros do Oracle:
SQL> alter system set open\_cursors=2000;
System altered.
SQL> exit

**![Imagem 3: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/17147593227159) OBSERVAÇÕES:**

![Imagem 4: Caso o retorno do parâmetro apresente valor <2000, efetue o procedimento de "Ajustar parâmetros do Oracle" para…](https://ajuda.sankhya.com.br/hc/article_attachments/17147593230231) Caso o retorno do parâmetro apresente **valor <2000,** efetue o procedimento de **"Ajustar parâmetros do Oracle"** para correção.

![Imagem 5: Esse comando deve ser realizado pela equipe de T.I. da empresa, ou por quem hospeda o banco de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/17147563323671) Esse comando deve ser realizado pela **equipe de T.I.** da empresa, ou por quem **hospeda o banco de dados.**

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17147563325719) CAUSA:**

O erro é apresentado quando a quantidade máxima de cursores está baixa, sendo necessário alterá-la, conforme [Manual de Instalação Sankhya OM em Ambiente Linux](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-OM-em-Ambiente-Linux), para no mínimo 2000 cursores.
