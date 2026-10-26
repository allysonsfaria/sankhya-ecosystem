---
id: "42427485260695"
titulo: "Como obter acesso à API do Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427485260695-Como-obter-acesso-%C3%A0-API-do-Ploomes"
trilha: "PLOOMES: Automação de propostas  > API & Webhooks"
atualizado_em: "2026-08-11T16:14:45Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452438", "sync_hash_2eefb6a34771"]
---

# Como obter acesso à API do Ploomes

A **API do Ploomes** permite integrar o CRM com outros sistemas, automatizar processos e manipular dados da conta por meio de requisições externas.

Para começar a utilizar a API, é necessário realizar duas etapas:

1. Criar um **usuário de integração**, responsável por gerar a chave de acesso utilizada nas requisições.
2. Utilizar a **coleção de exemplos da API**, disponível para testes e desenvolvimento.

Você pode consultar a documentação completa da API neste link: <https://developers.ploomes.com/>

## Criar um usuário de integração

Para acessar a API do Ploomes, é necessário que exista **pelo menos um usuário de integração** na conta.

Esse tipo de usuário:

- **não possui custo adicional**
- **não pode acessar o sistema**
- é utilizado **exclusivamente para integrações e automatizações**

## Como criar

1. Acesse **Administração** no menu do sistema.
2. Clique em **Usuários de integração**.

   ![Imagem 1: Clique em Usuários de integração .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2155799354/7d319a027fe2990f778a6fb10798/image.png?expires=1786536000&signature=6439cf98b67ee4356b210d9cfc663ef421dca0256327b530c9cf611cc4ae0a76&req=diEiE853lIJaXfMW3nq%2BgZKqWc18vqA%2F%2Bg9KBefBnDvlCLbY%2FXoTGRUDIjvM%0AIIRYEO1YqENE5VHzB2hWHY0S8xo%3D%0A)
3. Clique em **Novo usuário** no canto superior direito.
4. Preencha o nome, e-mail¹, perfil² e outras informações obrigatórias do formulário
5. Clique em **Criar usuário.**

Após a criação, o usuário aparecerá na lista³. Ao clicar sobre ele, será exibida a **chave de integração (User-Key)**, que deverá ser utilizada nas requisições da API.

![Imagem 2: Após a criação, o usuário aparecerá na lista³. Ao clicar sobre ele, será exibida a chave de integração (User-Key) , que…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2155807305/314157006c94fe80263d60e03b7a/image.png?expires=1786536000&signature=a21d393eb61689f4b4544398063a723d525498a3364b163ebe643cf85c673d5c&req=diEiE8F%2BmoJfXPMW3nq%2BgZs4nviNQk6Sb4pbLzkaOsEW%2BfkYs6iLKfLNfyhy%0Ay%2F10XVNjK108Vo8mD02VGUxz2R4%3D%0A)

**Observações:**

1. O e-mail informado precisa seguir um formato válido (por exemplo: `automacao@suaempresa.com`). Esse endereço **não precisa existir de fato**, pois o usuário de integração não permite login no sistema.
   O e-mail é um dado único, então não pode ser igual ao de um usuário existente na conta ou no Ploomes em geral.
2. O perfil funciona da mesma forma que para usuários comuns, definindo **quais dados a integração poderá acessar ou modificar**.

   Na maioria dos casos, recomenda-se utilizar o **perfil de Administrador**, pois ele possui acesso completo aos dados da conta. No entanto, o perfil pode ser ajustado conforme a necessidade da integração.
3. Usuários de integração **não aparecem na mesma lista que os usuários comuns**. Eles ficam disponíveis apenas na área de **Usuários de integração** em Administração.

## Utilizar a coleção de testes da API

A Ploomes disponibiliza uma **coleção de exemplos de chamadas da API**, que pode ser utilizada para realizar testes e facilitar o desenvolvimento de integrações.

Essa coleção pode ser utilizada no **Postman**, uma ferramenta bastante comum para testes de APIs.

Acesse o arquivo da coleção por [este link](https://github.com/Ploomes-Suporte/Client-friendly-API-v2-Collection).

No arquivo da coleção, todas as chamadas utilizam duas variáveis:

- `#{{server}}`
- `#{{uk}}`

Elas devem ser substituídas da seguinte forma:

**##{{server}}:** https://public-api2.ploomes.com/

**##{{uk}}:** chave de usuário gerada na criação do **usuário de integração**.

Essa chave deve ser enviada no **Header da requisição** com o parâmetro: `User-Key`

## Estrutura da API

A API do Ploomes é baseada no protocolo **OData v4**, que define padrões para consulta e manipulação de dados via HTTP.

Esse protocolo permite realizar operações como:

- filtros
- ordenação
- paginação
- seleção de campos

Para entender melhor a sintaxe das requisições, consulte a documentação oficial do OData: <https://www.odata.org/documentation/>

Também recomendamos a leitura das convenções de URL do protocolo: <http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part2-url-conventions.html>

Leia também:

[Como identificar todos os campos (padrões e customizados) e suas chaves no Ploomes](https://sankhya.zendesk.com/hc/pt-br/articles/42427671153431)

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 3: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1385472031/7f22a7993e319bb81eb290c9cfec/Introdu-C3-A7-C3-A3o%2B-C3-A0%2BAPI%2Bdo%2BPloomes.png?expires=1786536000&signature=651cae4bbbe0a7785d157ca0780cad49451df64811c51fa1bb0640c3257ae1f6&req=dSMvE815n4FcWPMW3nq%2BgcHA5yHH5Gv1SNccxEL5xS3fiavMfn1sJCDAXYOo%0An06GKafUmajYwhn4H2chJRNSGD8%3D%0A)](https://universidade.ploomes.com/courses/introducao-a-api-do-ploomes)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
