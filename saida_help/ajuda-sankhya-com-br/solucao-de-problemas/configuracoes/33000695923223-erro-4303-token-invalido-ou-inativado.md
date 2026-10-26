---
id: "33000695923223"
titulo: "Erro 4303 - Token Invalido ou Inativado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33000695923223-Erro-4303-Token-Invalido-ou-Inativado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-07T12:09:21Z"
rotulos: ["Configuração", "Autenticação", "API", "Passos para resolver", "Razão do erro", "Detalhe do erro", "4303 - token", "token invalido", "token inativado", "4303", "inativado ou invalido", "token", "API 4303", "Erro", "Artigo atualizado KCS", "Plataforma - KCS", "Sankhya Developer"]
---

# Erro 4303 - Token Invalido ou Inativado

**MENSAGEM**

[4405] Token e Appkey não associados

[4303] Token inválido ou inativado

**SITUAÇÃO**

Ao realizar uma integração via API do Sankhya, seja para autenticação ou consumo de endpoints, o sistema retorna uma das mensagens de erro acima. Essa situação ocorre frequentemente quando há **divergência entre o ambiente do token e o ambiente do endpoint** utilizado na requisição, ou quando **token e Appkey pertencem a aplicações diferentes**.

**SOLUÇÃO**

Este erro indica que houve uma incompatibilidade entre a URL, o Token e a Appkey informadas na tentativa de autenticação na API da Sankhya. Para que a autenticação funcione, utilize as credenciais correspondentes ao ambiente desejado:

**(1)** Identifique o ambiente de integração (produção ou sandbox/testes).

**(2)** Verifique se a URL da requisição corresponde ao ambiente correto:

- **Produção:** utilize a URL **https://api.sankhya.com.br** com Appkey de produção.
- **Sandbox/Testes:** utilize a URL **https://api.sandbox.sankhya.com.br** com Appkey de sandbox.

**(3)** Acesse a tela **"Configurações Gateway"** (Configurações >> Avançado >> Configurações Gateway) no ambiente correspondente.
**(4)** Verifique qual aplicação está vinculada ao token gerado na tela **"Configurações Gateway"**.
**(5)** Acesse a **Área do Desenvolvedor** e navegue até **"Gerenciar Soluções"**.
**(6)** Confirme que a **Appkey** utilizada na requisição pertence à mesma aplicação vinculada ao token gerado no passo 4.
**(7)** Certifique-se de que o **X-Token** foi gerado no mesmo ambiente do endpoint. Tokens de produção devem ser usados apenas em endpoints de produção, e tokens de sandbox apenas em endpoints de sandbox.
**(8)** Se necessário, gere um novo token no ambiente correto através da tela **"Configurações Gateway"**.
**(9)** Atualize a requisição com as credenciais corretas e valide a documentação em: [Obter Appkey - Sankhya Developer](https://developer.sankhya.com.br/reference/obter-appkey).

**CAUSA**

Esses erros ocorrem por motivos principais:

- **Divergência de ambientes:** Utilização de URL de produção com Appkey/Token de testes, ou vice-versa.
- **Incompatibilidade entre token e Appkey:** Token e Appkey devem sempre pertencer à mesma aplicação e ao mesmo ambiente.

**Importante:** o login pela API com usuário, senha, appkey e token (serviço **/login**) é um fluxo **legado e descontinuado**. Ele continua disponível só para manter as integrações que já existem e não recebe mais atualizações. Para novas integrações, use o fluxo [**OAuth 2.0 (serviço /authenticate)**](https://developer.sankhya.com.br/reference/post_authenticate) e planeje a migração das integrações atuais.

**Observação:**

- AppKeys de produção não funcionam no ambiente Sandbox e vice-versa.
- Tokens são **exclusivos** do ambiente em que foram gerados.
