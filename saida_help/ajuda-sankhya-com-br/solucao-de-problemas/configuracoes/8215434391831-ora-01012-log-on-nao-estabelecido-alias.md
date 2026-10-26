---
id: "8215434391831"
titulo: "ORA-01012 log-on não estabelecido Alias: DBNSiade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8215434391831-ORA-01012-log-on-n%C3%A3o-estabelecido-Alias-DBNSiade"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:12:23Z"
rotulos: ["Configuração", "MGE", "Financeiro", "ORA-01012", "Erro de Log-on ORA-01012: Resolução Rápida", "Erro", "DBNSiade"]
---

# ORA-01012 log-on não estabelecido Alias: DBNSiade

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16585671171863) MENSAGEM**:

ORA-01012 log-on não estabelecido 
Alias: DBNSiade

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16585671176855) SITUAÇÃO**

Mensagem apresentada ao tentar logar no MGE/MITRA/G1 :

General SQL error.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16585636341655) SOLUÇÃO:**

Crie o arquivo com a senha do usuário de banco de dados criptografada LICENSE.DAT com o aplicativo: <https://ajuda.sankhya.com.br/hc/pt-br/article_attachments/360060111454/License.zip>

Tendo o arquivo gerado, coloque o no diretório raiz do MGE/MITRA/G1

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16585671184407) CAUSA:**

Erro apresentado pelo fato da senha do banco de dados não ter sido definida corretamente, via arquivo LICENSE.DAT, que deve ficar no diretório raiz dos executáveis
