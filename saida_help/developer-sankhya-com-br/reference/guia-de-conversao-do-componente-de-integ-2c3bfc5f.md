---
id: "https://developer.sankhya.com.br/reference/guia-de-conversao-do-componente-de-integracao-appkey-oauth2"
titulo: "Guia de Conversão do Componente de Integração (AppKey → OAuth2)"
url: "https://developer.sankhya.com.br/reference/guia-de-conversao-do-componente-de-integracao-appkey-oauth2"
atualizado_em: "2026-03-02T13:55:44.000Z"
---

# Guia de Conversão do Componente de Integração (AppKey → OAuth2)

Este guia explica **como converter um componente de integração existente**, que atualmente utiliza autenticação legada via **/login (AppKey + Token + SankhyaID)**, para o **novo modelo OAuth2**, utilizando o endpoint **/authenticate**, **sem a necessidade de criar um novo componente de integração**.

A conversão preserva:

* Os clientes já configurados
* Os tokens existentes
* O histórico da solução

***

## 1. Visão geral da conversão

A conversão permite que **o mesmo componente de integração** passe a operar temporariamente em **modo híbrido**, suportando simultaneamente:

* Autenticação legada (`/login`)
* Nova autenticação OAuth2 (`/authenticate`)

Isso garante uma migração **segura, gradual e sem impacto imediato** para as integrações em produção.

***

## 2. Pré-requisitos

Antes de iniciar a conversão, verifique se:

* Você possui permissão de **edição** da solução
* O componente de integração utiliza atualmente **AppKey**
* O componente está **ativo**

> ℹ️ Nenhuma ação precisa ser realizada nos ambientes dos clientes neste momento.

***

## 3. Acessando o componente de integração

1. Acesse a **Área do Desenvolvedor**
2. Navegue até **Soluções**
3. Selecione a solução desejada
4. Abra o **Componente de Integração** existente

<Callout icon="📸" theme="default">
  ### **Componente de Integração Legado**

  ![](https://files.readme.io/e4daf65b63a564ffcf166184cbdefbb42da5064cf9438ec84bf69e5f1f68aab3-image.png)

  Fluxo visual: Minhas Soluções → Lista de Soluções → Detalhe da Solução → Lista de Componentes → Componente de Integração. Detalhe do componente de integração **antes da conversão**, exibindo apenas AppKey (Sandbox e Produção). Caso o botão **Gerar novas chaves** não seja exibido, limpe o cache do navegador e tente novamente.
</Callout>

***

## 4. Iniciando a conversão para OAuth2

Na tela do componente de integração, será exibido o botão:

**“Gerar novas chaves”**

Este botão indica que o componente pode ser convertido para o novo modelo de autenticação.

### Passos:

1. Leia atentamente as instruções exibidas
2. Clique em **Gerar novas chaves** para criar as chaves para autenticação OAuth2\*\*
3. Visualize as novas credencias na tela após o processamento

<Callout icon="📸" theme="default">
  ### **Botão "Gerar novas chaves"**

  ![](https://files.readme.io/15892ced9da38979d2c7e581c021712a4724bc42cea2b860bffeea3677dc6d34-image.png)

  Botão de migração destacado, com texto explicativo informando que não será criado um novo componente.
</Callout>

***

## 5. Visualização das credenciais OAuth2

Após a realização do procedimento de **Gerar novas chaves**:

* O sistema apresentará:
  * `client_id`
  * `client_secret`
* As credenciais OAuth2 passam a coexistir com:
  * AppKey (Produção)
  * AppKey (Sandbox)

### Importante:

* Ambos os métodos de autenticação funcionam em paralelo
* Nenhuma integração existente é interrompida

<Callout icon="📸" theme="default">
  ### **Componente de Integração Após Gerar as Novas Credenciais**

  ![](https://files.readme.io/51ed0f41b32c4a1adac1efc9a12246f1ac6a92e6e222abf1242c6d2831ca1526-image.png)

  Tela exibindo **AppKey (fluxo legado) + client_id + client_secret** ativos simultaneamente. As chaves são geradas tanto para ambiente de Produção quanto ambiente de Sandbox.
</Callout>

***

## 6. Atualizando sua aplicação para OAuth2

Com as credenciais OAuth2 disponíveis:

1. Atualize sua aplicação para autenticar via endpoint **/authenticate**
   * Veja a documentação completa da autenticação OAuth2 [clicando aqui](https://developer.sankhya.com.br/reference/post_authenticate)
2. Utilize:
   * `client_id`
   * `client_secret`
   * O **Token** fornecido pelo cliente (mesmo `token` que já é utilizando no **/login**) é o que deverá ser utilizado como **X-Token** no novo método de autenticação **/authenticate**

> ✅ Recomendamos iniciar os testes em **Sandbox** antes de aplicar em Produção.

***

## 7. Boas práticas recomendadas

* Migre primeiro clientes de menor impacto
* Utilize Sandbox para validação completa
* Registre internamente a data da conversão para avaliar o comportamento após a migração

***

## 8. Checklist final de conversão

Antes de concluir, valide:

* [ ] `client_id` e `client_secret` gerados
* [ ] Aplicação autenticando via `/authenticate`
* [ ] Testes realizados em Sandbox
* [ ] Testes realizados em Produção
* [ ] Autenticação legada inativada (opcional, mas recomendada)

<br />

<br />
