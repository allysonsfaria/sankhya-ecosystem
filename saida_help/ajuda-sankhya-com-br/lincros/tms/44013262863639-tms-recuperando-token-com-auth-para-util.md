---
id: "44013262863639"
titulo: "[TMS] - Recuperando token com /auth para utilizar em requisições WS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013262863639--TMS-Recuperando-token-com-auth-para-utilizar-em-requisi%C3%A7%C3%B5es-WS"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T19:52:33Z"
rotulos: ["sync_hc", "lincros", "lincros_13432774", "sync_hash_7774c5c0f22a"]
---

# [TMS] - Recuperando token com /auth para utilizar em requisições WS

**Menu**: Não se aplica

**Objetivo**: Obter um Token temporário para utilizar nas requisições utilizando o serviço /auth.

**Considerações**:

- O tempo de expiração do token recuperado é de 30 minutos, após este tempo o token será considerado inválido;
- A utilização do serviço /auth para recuperar um token temporário é indicada pois aumenta a segurança nas requisições, gerando um novo token a cada 30 minutos;
- O token que será retornado deverá ser armazenado e utilizado nas próximas requisições que serão disparadas;
- Como o token será válido por apenas 30 minutos, deverá ser parametrizado que após o primeiro retorno HTTP 401 - Unauthorized seja disparado uma nova requisição /auth gerando assim um novo token;
- Desta forma estarão sempre renovando este token, aumentando a segurança de informação nas requisições;
- A requisição poderá ser feita de dois métodos, utilizando GET e passando as informações de login e senha via URL, ou utilizando POST e passando estas informações no corpo da requisiçã;

 Abaixo segue os procedimentos:

## Relação de métodos

| URL | Tipo requisição | Descrição |
| --- | --- | --- |
| /auth/login/{login}/{senha} | GET | Responsável pelo fornecimento dos tokens de identificação, a partir das credenciais informadas na URL, para utilização dos demais serviços e métodos. |
| /auth/login | POST | Responsável pelo fornecimento dos tokens de identificação, a partir das credenciais informadas em um JSON, para utilização dos demais serviços e métodos. |

## Método /auth/login

| Parâmetro | Tipo | Aplicação | Default | Descrição |
| --- | --- | --- | --- | --- |
| login | String | Obrigatório |  | Login do usuário no transpoFrete |
| senha | String | Obrigatório |  | Senha do usuário no transpoFrete |

## Exemplo de requisição

| 1  2  3  4 | `{`  `"login":"meulogin",`  `"senha":"minhasenha"`  `}` |
| --- | --- |

## Exemplo de retorno

**Sucesso**

| 1 | `29491395A890FF87E9709570559A5633` |
| --- | --- |

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
