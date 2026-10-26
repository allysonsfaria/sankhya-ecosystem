---
id: "44011496545815"
titulo: "Como obter as credenciais Meus Correios?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011496545815-Como-obter-as-credenciais-Meus-Correios"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:04:05Z"
rotulos: ["sync_hc", "magis5", "sync_hash_8c0f0d1af5ec", "magis5_204051670290"]
---

# Como obter as credenciais Meus Correios?

## Para realizar cotações de frete, rastreamento e fechamento de PLP é preciso configurar as credenciais do portal 'Meus Correios' no Magis5 Hub.

---

### Como cadastrar as credenciais no portal dos Correios

Acesse o [portal dos Correios](https://cws.correios.com.br/) e clique em **"Entrar"**.

![Imagem 1: Acesse o portal dos Correios e clique em "Entrar" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011481963543)

Nesse menu, preencha o **"Usuário"** e **"Senha"** de seu painel e clique em **'Entrar'**

**⚠️** Caso ainda não tenha acesso ao painel dos Correios, verifique com o gerente dos Correios.

![Imagem 2: ⚠️ Caso ainda não tenha acesso ao painel dos Correios, verifique com o gerente dos Correios.](https://ajuda.sankhya.com.br/hc/article_attachments/44011471740695)

Em seguida, à esquerda da tela, clique em **"Gestão de acesso a API's".**

![Imagem 3: Em seguida, à esquerda da tela, clique em "Gestão de acesso a API's".](https://ajuda.sankhya.com.br/hc/article_attachments/44011482169751)

Na tela que será aberta:
![Imagem 4: Na tela que será aberta:](https://ajuda.sankhya.com.br/hc/article_attachments/44011497181975)

- Copie a informação do campo **"Usuário do Portal Meus Correios"**
- No campo de **"Senha do Portal Meu Correios"** insira a mesma senha utilizada para acessar o site Correios Web Services e em seguida clique em **"Gerar código"**.

Será aberta uma janela contendo a senha alfanumérica que será utilizada para consumo da API. **Copie este código!**

![Imagem 5: Será aberta uma janela contendo a senha alfanumérica que será utilizada para consumo da API. Copie este código!](https://ajuda.sankhya.com.br/hc/article_attachments/44011487250071)

Após isso, vá para o Magis5 Hub.

**Dica:**

Aguarde em torno de 5 minutos antes de continuar esta configuração, pois é o tempo que o sistema dos Correios precisará para permitir a autenticação.

### Como inserir as credenciais no Magis5 Hub

No Magis5 Hub vá para **Configurações -> Integrações -> Logísticas.**

![Imagem 6: No Magis5 Hub vá para Configurações -> Integrações -> Logísticas.](https://ajuda.sankhya.com.br/hc/article_attachments/44011497426071)

Localize sua integração do Correios e clique em **"Editar".**

![Imagem 7: Localize sua integração do Correios e clique em "Editar".](https://ajuda.sankhya.com.br/hc/article_attachments/44011472318743)

Dentro da aba **"Geral"**, na seção **"MEUS CORREIOS - API"** será necessário informar os 2 campos abaixo:

- **Usuário:** insira o [mesmo usuário que copiou](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011496545815-Como-obter-as-credenciais-Meus-Correios#usuario) do campo **"Usuário do Portal Meu Correios"** do painel do Correios.
- **Senha:** insira a [senha alfanumérica](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011496545815-Como-obter-as-credenciais-Meus-Correios#usuario) que copiou no painel do **Correios Web Services.**

![Imagem 8: Senha: insira a senha alfanumérica que copiou no painel do Correios Web Services.](https://ajuda.sankhya.com.br/hc/article_attachments/44011472416919)

Após atualizar os campos, clique em **"Autenticar"**, selecione os serviços que irá utilizar com o seu contrato do Correios e finalize clicando em **"Salvar"** no topo da página.

![Imagem 9: Após atualizar os campos, clique em "Autenticar" , selecione os serviços que irá utilizar com o seu contrato do…](https://ajuda.sankhya.com.br/hc/article_attachments/44011455572631)

Ao fim, basta aguardar que seus pedidos em Ag. Logística vinculado ao contrato dos Correios irão seguir automaticamente para Ag. Separação.
[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44011487754391)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
