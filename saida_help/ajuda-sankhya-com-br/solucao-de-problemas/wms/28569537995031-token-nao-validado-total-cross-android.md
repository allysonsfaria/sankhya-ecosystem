---
id: "28569537995031"
titulo: "Token não validado! Total Cross (Android)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28569537995031-Token-n%C3%A3o-validado-Total-Cross-Android"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-08-14T22:45:00Z"
rotulos: ["Configuração", "Segurança", "Android", "Token", "Passos para resolver", "Razão do erro", "Detalhe do erro", "token não validado!", "Token não validado! Total Cross (Android)", "Total Cross (Android)", "Erro"]
---

# Token não validado! Total Cross (Android)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/28569537981335) **MENSAGEM:**

Token não validado!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28569537984919)SOLUÇÃO:**

![Imagem 3: Verifique se tem algum bloqueio no Firewell](https://ajuda.sankhya.com.br/hc/article_attachments/29524095554839) Verifique se tem algum bloqueio no Firewell  

 O servidor onde está instalado a aplicação, precisa ter as seguintes exceções: 

- Ter acesso a internet liberada;
- Regras de Permissões de Firewall/ Proxy liberada para o endereço: [**https://grupo.sankhya.com.br**](https://grupo.sankhya.com.br/)
- Porta 10050 liberada no Firewall/Proxy;

 

![Imagem 4: Verifique a conexão com a Internet.](https://ajuda.sankhya.com.br/hc/article_attachments/29524095556119) Verifique a conexão com a Internet.  

- Caso não tenha conexão com a internet, pode ser que perca a conexão e não fique com o fuso horário igual.

![Imagem 5: Identifique se o horário do coletor é o mesmo horário do servidor. Se ambos estiverem diferentes será gerada a mensagem…](https://ajuda.sankhya.com.br/hc/article_attachments/29524074735767) Identifique se o horário do coletor é o mesmo horário do servidor. Se ambos estiverem diferentes será gerada a mensagem de Token não validado. 

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/28569537987735)CAUSA:**

Ao abrir o coletor Total Cross (Android) a mensagem é apresentada.
