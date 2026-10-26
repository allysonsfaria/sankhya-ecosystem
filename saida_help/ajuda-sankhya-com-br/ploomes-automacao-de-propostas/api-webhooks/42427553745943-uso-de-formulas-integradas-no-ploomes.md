---
id: "42427553745943"
titulo: "Uso de Fórmulas Integradas no Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427553745943-Uso-de-F%C3%B3rmulas-Integradas-no-Ploomes"
trilha: "PLOOMES: Automação de propostas  > API & Webhooks"
atualizado_em: "2026-08-11T16:14:30Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12894829", "sync_hash_87cf409c6e3b"]
---

# Uso de Fórmulas Integradas no Ploomes

As fórmulas integradas são utilizadas para automatizar o preenchimento de campos no Ploomes a partir de informações internas (via nossa API) ou externas (via API do cliente). Essa funcionalidade é essencial para buscar dados fora do escopo padrão entre entidades ou quando é necessário integrar sistemas diferentes.

Essa aba de configuração foi feita justamente para isso: permitir que você monte requisições usando URLs (de qualquer API, não só da Ploomes), escolha o método adequado (como GET ou POST), defina autenticação, envie dados e receba respostas que vão preencher os campos automaticamente.

---

## Estrutura da Fórmula Integrada

## 1. URL

É o endereço da requisição que será feita.

**Importante:** só podemos fazer requisições em URLs que utilizam o protocolo **HTTPS**

**Exemplo:**

```
https://api2.ploomes.com/Contacts?$filter=Id+eq+412923217
```

## 2. Método

Define a ação que será executada na URL. Pode ser `GET`, `POST`, `PATCH`, entre outros.

**Exemplo:**

```
Método: GET
```

Busca as informações do contato com ID 412923217.

## 3. Headers

Onde se define a autenticação. Para a API Ploomes, é usada a [User-Key](https://sankhya.zendesk.com/hc/pt-br/articles/42427485260695):

**Exemplo:**

```
{"user-key":"inserir user-key"}
```

##

## 4. JSONPath

Responsável por definir qual valor será retornado da requisição para preencher o campo.

**Exemplo:**

```
$.value[0].Name
```

Explicação:

- `$.` Início do path
- `value` é o array de retorno padrão da nossa API
- `[0]` seleciona o primeiro item do array
- `.Name` define qual campo daquele objeto deve ser retornado

**Obs:** O path pode variar de acordo com a estrutura da API usada. Recomendamos o uso do [JSON Path Evaluator](https://jsonpath.com/) para facilitar a localização do FieldPath

![Imagem 1: Obs: O path pode variar de acordo com a estrutura da API usada. Recomendamos o uso do JSON Path Evaluator para…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1841453614/e3e90d44d51e210c5acecd6996a7/image.png?expires=1786536000&signature=fe4efc60e0b2bbb82125c1bfdef7b8aa05d08a2ee9480b7045337c1a7878bb53&req=dSgjF817nodeXfMW3nq%2BgSEFf93mIlQWHuq%2FUHQfyKxsYW8oBlejjerl2uRp%0A5e54OpPTKXm%2BILKiact0Wg5U3%2Fc%3D%0A)

## 5. Body da Requisição

Necessário apenas para métodos como `POST` e `PATCH`. Aqui será definido o que será enviado para a URL.

Pode ser preenchido com um JSON fixo ou com campos dinâmicos do Ploomes.

![Imagem 2: Pode ser preenchido com um JSON fixo ou com campos dinâmicos do Ploomes.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1841440458/f61bd3015dc8ba2738a233e94a7f/image.png?expires=1786536000&signature=6e8fe458c7153b23b0d4749c6180fc6cf56aecb5c7d9722b498a47103b80c378&req=dSgjF816nYVaUfMW3nq%2BgRDCBXMdYazgo8xBDtXXUDBUe%2B%2FFnGPddkC7%2BGp1%0AocmlMFST7wl38iEe3fKdFsBGEB8%3D%0A)

Conforme o print acima você pôde identificar aonde estaria localizado cada um, fora isso temos também o **Mapeamento de Campos** que define os campos que vão receber o resultado da fórmula (pode ser o próprio campo)

---

## Exemplos de Uso

- Buscar dados do produto do cliente vinculado à proposta
- Filtrar opções de campos com base em atributos do cliente
- Puxar informações de sistemas externos usando dados preenchidos no Ploomes
- Retornar apenas contatos de determinada empresa em campos do tipo cliente

---

## Erros comuns e como corrigi-los

Consulte a referência completa de códigos HTTP [aqui](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status).

## 403 Forbidden

- A URL está incorreta ou possui parâmetros com erro.
- Revisar a URL usada e, se necessário, pedir apoio técnico.

## 401 Unauthorized

- User-Key incorreta ou mal configurada nos headers.
- Em APIs externas, validar com o cliente a forma correta de autenticação.

## 408/504 Timeout

- A requisição demorou mais de 20 segundos.
- Otimize filtros, use `TOP`/`SKIP`, e evite muitos `expands`.

## 405 Method Not Allowed

- O método usado não é aceito pela API de destino.
- Verifique a documentação da API utilizada.

Qualquer dúvida pontual sobre esse tipo de fórmula pode ser direcionada à nossa equipe de suporte que estará à disposição para te apoiar.
