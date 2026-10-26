---
id: "360052313713"
titulo: "Driver de conexão com o banco de dados está desatualizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052313713-Driver-de-conex%C3%A3o-com-o-banco-de-dados-est%C3%A1-desatualizado"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T15:29:56Z"
rotulos: ["Configuração", "Atualização", "Financeiro", "atualização desempenho OJDBC", "Erro", "Banco de Dados"]
---

# Driver de conexão com o banco de dados está desatualizado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18588518897815) MENSAGEM:**

Driver de conexão com o banco de dados está desatualizado.

A versão do banco de dados XX.X é mais recente que a versão do driver de conexão XX.X

Isto pode afetar o desempenho do sistema com relação ao carregamento de telas e a gravação de informações.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588518906519) SOLUÇÃO:**

Orientações a serem seguidas com apoio do T.I e/ou DBA da empresa:

![Imagem 3: Efetuar o download do OJDBC no site da Oracle (De acordo com a versão do seu banco de dados);](https://ajuda.sankhya.com.br/hc/article_attachments/18588518909207) Efetuar o download do OJDBC no site da Oracle (De acordo com a versão do seu banco de dados);

![Imagem 4: Atualizar o driver de conexão com o banco de dados por este baixado da versão 12.2.X.X.X, conforme a versão do banco…](https://ajuda.sankhya.com.br/hc/article_attachments/18588518914967) Atualizar o driver de conexão com o banco de dados por este baixado da versão 12.2.X.X.X, conforme a versão do banco atualmente.

![Imagem 5: Vale ressaltar a importância de renomear o arquivo para "ojdbc.jar"](https://ajuda.sankhya.com.br/hc/article_attachments/12633902349847) Vale ressaltar a importância de renomear o arquivo para "ojdbc.jar"

Esta troca é feita no caminho:

/home/mgeweb/wildfly\_producao/modules/custom/ojdbc/main

- Parar o Wildfly;
- Substituir o arquivo neste caminho descrito acima com o usuário mgeweb.
- Iniciar novamente o Wildfly
