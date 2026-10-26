---
id: "32738618991767"
titulo: "'Não autorizado' ao realizar login via API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32738618991767--N%C3%A3o-autorizado-ao-realizar-login-via-API"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:30:29Z"
rotulos: ["Configuração", "Segurança", "Autenticação", "erro", "API", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Login API", "Não autorizado", "400", "message", "error"]
---

# 'Não autorizado' ao realizar login via API

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32738618978455) **MENSAGEM:**

Requisição de login via API retorna código 400 com a mensagem de erro:

{"statusCode":400,"error":{"code":"BAD\_REQUEST","message":"Ocorreu algum erro inesperado!","details":"Não autorizado."}}

**SITUAÇÃO:**

Durante a tentativa de integração via API, a autenticação falha com retorno **"Não autorizado"**, mesmo com o envio correto de credenciais (usuário, AppKey e Token).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32738618981015)SOLUÇÃO:**

Verifique se o usuário utilizado na integração pertence a um **grupo de usuários configurado para autenticação em dois fatores (2FA)**.

Os argumentos da VM que controlam essa configuração podem ser verificados diretamente no sistema, acessando o menu **Administração de Servidor > Aba 'Geral'**.

Essa configuração é definida por argumentos de VM utilizados na inicialização do servidor:

```
-Dsnk.use.action.auth=true
-Dsnk.2fa.level=glist
-Dsnk.2fa.glist=3,4,9,10,12,14,18,41,42,45,81,85,125,131,132,135,139,147,149,150,166
-Dsnk.2fa.timeout=24H
```

O argumento `-Dsnk.2fa.glist` determina que os grupos listados devem realizar autenticação em duas etapas. Se o usuário da integração pertencer a um desses grupos, o login via API será bloqueado silenciosamente, resultando no erro **"Não autorizado"**.

Para permitir o login via API com este usuário é necessário r**emover o grupo do 2FA**

- Acesse os argumentos da VM utilizados na inicialização do servidor.
- Localize o argumento `-Dsnk.2fa.glist` e **remova o grupo ao qual o usuário pertence**.
- Reinicie o servidor para aplicar as mudanças.

> Exemplo: Se o usuário vinculado a API está no grupo 4, remova o "4" da lista.

**Observação:**

- Mesmo que o ambiente **não utilize a camada de autorização para API** (ausência do argumento

  `-Dsnk.authorization.layer.enable=true`), a autenticação em dois fatores é aplicada de forma independente.
- Para mais detalhes sobre autenticação em APIs e camada de segurança, consulte o artigo oficial:
  [Camada de autorização para API - Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32738618983319)CAUSA:**

O erro ocorre quando o usuário utilizado na integração pertence a um grupo configurado para autenticação em dois fatores (2FA), o que bloqueia o login via API.
