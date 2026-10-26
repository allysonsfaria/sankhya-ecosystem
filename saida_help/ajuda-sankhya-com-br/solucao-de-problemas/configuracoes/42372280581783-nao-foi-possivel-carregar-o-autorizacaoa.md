---
id: "42372280581783"
titulo: "Não foi possível carregar o AutorizacaoApi"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42372280581783-N%C3%A3o-foi-poss%C3%ADvel-carregar-o-AutorizacaoApi"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-15T20:08:58Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Plataforma - KCS", "Documentos Eletrônicos", "AutorizacaoApi"]
---

# Não foi possível carregar o AutorizacaoApi

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/42372280572055) **MENSAGEM:**

Não foi possível carregar o AutorizacaoApi

![Imagem 2: Não foi possível carregar o AutorizacaoApi](https://ajuda.sankhya.com.br/hc/article_attachments/43514933816983)

**CAUSA:**

A tela **Autorização de Api** (`Configurações > Avançado > Autorização de Api`) é servida pelo módulo **Configurações BFF (**`mge-bff`**)** e só é liberada quando a camada de autorização está habilitada no ambiente, pelo argumento de inicialização:

```
-Dsnk.authorization.api.enable=true
```

A mensagem ocorre em duas situações distintas:

1. **Argumento habilitado, módulo desatualizado:** o argumento

   `-Dsnk.authorization.api.enable=true` está configurado, mas o módulo Configurações BFF está em versão anterior à **1.5.2**, que é a versão em que o recurso `AutorizacaoApi` passou a ser entregue. O sistema tenta carregar o recurso e não o encontra.
2. **Argumento ainda não incluído no ambiente:** o módulo está atualizado, mas o argumento

   `-Dsnk.authorization.api.enable=true` ainda não foi adicionado à inicialização do servidor de aplicação. Sem ele, a camada de autorização não é inicializada e o recurso não é carregado.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/42372266387095)SOLUÇÃO:**

**(1)** Verificar a versão do módulo

Acesse o menu **Sobre** (canto superior direito do workspace) e localize o módulo **Configurações BFF /** `mge-bff` na lista de versões dos módulos.

- Se estiver **abaixo de 1.5.2** → atualize o módulo para a versão **1.5.2 ou superior**.
- Se já estiver em **1.5.2 ou superior** → siga para o Passo 2.

(2)** Verificar o argumento de inicialização**

Confirme junto ao responsável pelo ambiente se o argumento abaixo consta nos parâmetros de inicialização da JVM:

```
-Dsnk.authorization.api.enable=true
```

Após a inclusão, é necessário **reiniciar o serviço** para que o argumento tenha efeito.

Para mais detalhes da tela e do argumento acesse o Help: [Como controlar o acesso de usuários às APIs utilizando a tela Autorização de API](https://ajuda.sankhya.com.br/hc/pt-br/articles/34162979696663-Como-controlar-o-acesso-de-usu%C3%A1rios-%C3%A0s-APIs-utilizando-a-tela-Autoriza%C3%A7%C3%A3o-de-API)

Duvidas sobre como inserir o argumento acesse: [Configuração de argumentos para Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly)

**Ambientes hospedados em nosso SAAS CLOUD**

Nesses ambientes o cliente não tem acesso à atualização de módulos nem aos argumentos de inicialização. É necessário **abrir um ticket** solicitando:

- a **atualização do módulo Configurações BFF (**`mge-bff`**)** para a versão 1.5.2 ou superior e/ou
- a **inclusão do argumento** `-Dsnk.authorization.api.enable=true`,

Informando expressamente **em qual base a alteração deve ser aplicada "Produção ou Teste"** já que a solicitação é aplicada por base.
