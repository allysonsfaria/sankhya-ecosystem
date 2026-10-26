---
id: "44011609957911"
titulo: "[Routing] Cadastro de Marcador via Web Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011609957911--Routing-Cadastro-de-Marcador-via-Web-Service"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T19:07:42Z"
rotulos: ["sync_hc", "lincros", "lincros_13438066", "sync_hash_9f0c28447e63"]
---

# [Routing] Cadastro de Marcador via Web Service

**Objetivo:** Entender como cadastrar o marcador no sistema e vinculá-lo ao pedido, para posteriormente ter a possibilidade de filtrar o pedido pela tela de iniciar uma nova sessão ou na sessão.

**Considerações**:

- Os marcadores podem ser cadastrados automaticamente via requisição Web Service;
- Documentação API /importacaopedidos para auxílio→ [Aqui](https://drive.google.com/file/d/1tRwIrjiqj6IJ0oZ6M-nYzGC2WM7UXVl5/view?usp=sharing)

Abaixo segue os procedimentos para o cadastro via requisição Web Service pela API /importacaopedidos:
1- Enviar a requisição de pedido via API [/importacaopedidos;](https://routing.lincros.com/api/cadastros/pedido/importacaopedidos)2- Conter o token de integração do depósito desejado;
3- No corpo da requisição deverá conter o campo "marcadores" com sua descrição, conforme exemplo do JSON abaixo:

![Imagem 1: Abaixo segue os procedimentos para o cadastro via requisição Web Service pela API /importacaopedidos: 1- Enviar a…](https://ajuda.sankhya.com.br/hc/article_attachments/44011633009559)

4- Enviar requisição.

Pronto, ao enviar a requisição ao sistema Routing o marcador será cadastrado e vinculado ao pedido. Conforme exemplo da imagem abaixo:

Tela > Cadastros > Marcador:

![Imagem 2: 4- Enviar requisição. Pronto, ao enviar a requisição ao sistema Routing o marcador será cadastrado e vinculado ao…](https://ajuda.sankhya.com.br/hc/article_attachments/44011649440023)

Tela Roteirizador > Roteirizar > Iniciar uma nova sessão de roteirização:

![Imagem 3: Tela Roteirizador > Roteirizar > Iniciar uma nova sessão de roteirização:](https://ajuda.sankhya.com.br/hc/article_attachments/44011610428695)

Tela > Sessão > Filtros da sessão > Marcadores >:

![Imagem 4: Tela > Sessão > Filtros da sessão > Marcadores >:](https://ajuda.sankhya.com.br/hc/article_attachments/44011633578647)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
