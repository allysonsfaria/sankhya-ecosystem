---
id: "42429588716951"
titulo: "Chat Embarcado com Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429588716951-Chat-Embarcado-com-Sankhya"
trilha: "NEPPO: Personalização de atendimento > Chat Embarcado"
atualizado_em: "2026-08-12T18:39:30Z"
rotulos: ["sync_hc", "neppo", "neppo_220660225", "sync_hash_c97eae5a315a"]
---

# Chat Embarcado com Sankhya

Esta documentação tem como objetivo orientar a instalação e configuração do **Chat Embarcado Neppo** no **ERP Sankhya**, permitindo que a comunicação com os clientes ocorra diretamente dentro do ambiente de gestão da empresa.

Com a integração ativa, é possível centralizar o atendimento, agilizar processos e oferecer uma experiência mais fluida e eficiente para os usuários do ERP.

[1 - Acessar o Sankhya Place](https://sankhya.zendesk.com/hc/pt-br/articles/42429588716951#1.-Acessar-o-Sankhya-Place)

[2 - Localizar e instalar o aplicativo Neppo (addon)](https://sankhya.zendesk.com/hc/pt-br/articles/42429588716951#2.-Localizar-e-instalar-o-aplicativo-Neppo-(addon))

[3 - Configuração de credenciais no ERP](https://sankhya.zendesk.com/hc/pt-br/articles/42429588716951#3.-Configura%C3%A7%C3%A3o-de-credenciais-no-ERP)

[4 - Configuração de usuário no ERP](https://sankhya.zendesk.com/hc/pt-br/articles/42429588716951#4.-Configura%C3%A7%C3%A3o-de-usu%C3%A1rio-no-ERP)

[5 - Resultado esperado](https://sankhya.zendesk.com/hc/pt-br/articles/42429588716951#5.-Resultado-esperado)

6 - Ambientes para testar (produtivo)

## 1. Acessar o Sankhya Minhas Soluções

- No ERP Sankhya, vá até o campo de busca e digite: `Minhas Soluções`.
- Clique para acessar a loja de aplicativos da plataforma.
- Insira seu **usuário** e **senha** para acessar o ambiente de download de aplicativos do ERP.

**Atenção:** seu usuário no Sankhya Place deve ter o nível de permissão para baixar apps. Caso não tenha, procure o administrador do ambiente Sankhya.

[GIF animado: Imagem 1: Atenção: seu usuário no Sankhya Place deve ter o nível de permissão para baixar apps. Caso não tenha, procure o…](https://ajuda.sankhya.com.br/hc/article_attachments/42639367612311)

## 2. Localizar e instalar o aplicativo Neppo (addon)

- No campo de busca do Minhas Soluções, digite: `Chat Embarcado Neppo`.
- Clique no botão **Iniciar Download**.
- Um feedback será informado em tela da conclusão.

[GIF animado: Imagem 2: Um feedback será informado em tela da conclusão.](https://ajuda.sankhya.com.br/hc/article_attachments/42639409785111)

## 3. Configuração de credenciais no ERP

Após a instalação:

### A. Gerar credenciais no Neppo

1. No ambiente Neppo, acesse o menu.
2. Vá até a seção **Integrações**.
3. Clique em **Criar Token** para gerar as credenciais necessárias.

![Imagem 3: Clique em Criar Token para gerar as credenciais necessárias.](https://ajuda.sankhya.com.br/hc/article_attachments/42639410018967)

### B. Preencher credenciais no ERP

No ERP Sankhya, acesse o local de configuração da integração e preencha os campos com as informações geradas no Neppo:

- **Chave do Consumidor**
- **Senha**
- **Senha do Consumidor**
- **URL do Ambiente**
- **Usuário**

![Imagem 4: Usuário](https://ajuda.sankhya.com.br/hc/article_attachments/42639414231959)

## 4. Configuração de usuário no ERP

- No ERP, acesse a tela de **Usuários**.
- Localize o campo **E-mail** e altere para o e-mail de um **usuário do tipo Agente** já cadastrado no **Neppo Omnichannel**.

**Atenção:** Esse usuário precisa ter o **Token do Chat Agent** previamente gerado no Neppo para que o Chat Embarcado funcione corretamente no ERP. Esta informação é encontrada dentro da tela de usuários no Neppo.

![Imagem 5: Atenção: Esse usuário precisa ter o Token do Chat Agent previamente gerado no Neppo para que o Chat Embarcado funcione…](https://ajuda.sankhya.com.br/hc/article_attachments/42639410295447)

![Imagem 6: Atenção: Esse usuário precisa ter o Token do Chat Agent previamente gerado no Neppo para que o Chat Embarcado funcione…](https://ajuda.sankhya.com.br/hc/article_attachments/42639368503447)

## 5. Resultado esperado

Após todas as etapas acima, o **Chat Embarcado Neppo** será renderizado dentro do ambiente do ERP Sankhya, pronto para uso.

[GIF animado: Imagem 7: Após todas as etapas acima, o Chat Embarcado Neppo será renderizado dentro do ambiente do ERP Sankhya, pronto para uso.](https://ajuda.sankhya.com.br/hc/article_attachments/42639414946327)
