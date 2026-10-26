---
id: "360044616653"
titulo: "./sannfe-service: bin/unpack200: /lib/ld-linux.so.2: bad ELF interpreter: Arquivo ou diretório não encontrado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616653--sannfe-service-bin-unpack200-lib-ld-linux-so-2-bad-ELF-interpreter-Arquivo-ou-diret%C3%B3rio-n%C3%A3o-encontrado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:44Z"
rotulos: ["Configuração", "NF-e", "Linux", "Erro", "Java"]
---

# ./sannfe-service: bin/unpack200: /lib/ld-linux.so.2: bad ELF interpreter: Arquivo ou diretório não encontrado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16813942404119) MENSAGEM:**

./sannfe-service: bin/unpack200: /lib/ld-linux.so.2: bad ELF interpreter: Arquivo ou diretório não encontrado

Error unpacking jar files. Abortin.

you might need administrative priviledges for this operation

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16813934258327) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o putty com usuário ROOT](https://ajuda.sankhya.com.br/hc/article_attachments/16813942412183)  Acesse o putty com usuário **ROOT**

![Imagem 4: Execute o comando: (root@linux ~) yum install ld-linux.so.2](https://ajuda.sankhya.com.br/hc/article_attachments/16813942415255)  Execute o comando: [root@linux ~] **yum install ld-linux.so.2**

![Imagem 5: Selecione Y(Yes) quando solicitado e instale o pack unpack200](https://ajuda.sankhya.com.br/hc/article_attachments/16813934266647)  Selecione Y[Yes] quando solicitado e instale o pack **unpack200**

![Imagem 6: Volte com o usuário mgeweb, acesse o SANNFE e inicie o novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16813934268823)  Volte com o usuário mgeweb, acesse o SANNFE e inicie o novamente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16813934271127) CAUSA:**

Ocorre quando algumas distribuição do Linux estão recém instalada e/ou falta a biblioteca de JRE(Java).
