---
id: "42427413878295"
titulo: "Como configurar a chave de acesso da integração com Power BI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427413878295-Como-configurar-a-chave-de-acesso-da-integra%C3%A7%C3%A3o-com-Power-BI"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-11T16:14:58Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11138008", "sync_hash_759b74c41f1e"]
---

# Como configurar a chave de acesso da integração com Power BI

A autenticação por chave no Power BI permite adicionar uma camada extra de segurança às URLs de exportação de dados do Ploomes, garantindo que **apenas usuários autorizados tenham acesso** às informações.

Com ela ativada, somente requisições autenticadas conseguem acessar os dados exportados, garantindo mais controle sobre informações sensíveis utilizadas em relatórios e dashboards, podendo ativar ou desativar a exigência de chave conforme necessário.

## Pré-requisitos

Antes de realizar a configuração, valide os seguintes pontos:

- A integração com o Power BI deve estar habilitada;
- O usuário precisa possuir permissão de administrador;
- É necessário ter acesso ao ambiente de configuração do Power BI para inserir os dados de autenticação.

Siga primeiro o artigo: [Integração com Power BI](https://sankhya.zendesk.com/hc/pt-br/articles/42427413992983).

## Como ativar a autenticação por chave

## 1. Ativar autenticação nas URLs

Para ativar a autenticação nas URLs de exportação:

1. Acesse **Integrações Plug and Play**;
2. Localize a integração do Power BI;
3. Ative a opção **Configuração de acesso aos dados da URL**;
4. Clique em **Atualizar integração**.

Uma mensagem de confirmação será exibida, informando que **todas as** URL's **antigas passarão a exigir chave.**

[GIF animado: Imagem 1: Uma mensagem de confirmação será exibida, informando que todas as URL's antigas passarão a exigir chave.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427573311/717156c9f37ba40d60343a5a872d/Design%2Bsem%2Bnome%2B-281-29.gif?expires=1786536000&signature=19bfde0b419007c37f2bf84213186f825dabfa948c0f5c55f4ccbbb7be5bb8d5&req=diQlEcx5noJeWPMW3nq%2BgSJyAv3kM8bcGcaNHtIW54KToWmF7DrnVk9a9b2F%0Adyv7SIu7z2oREXhA6emd4kl6NHI%3D%0A)

⚠️ **Atenção**: ao ativar a autenticação por chave, todas as URLs de exportação existentes passarão a exigir autenticação.

Caso a configuração não seja atualizada no Power BI, os relatórios deixarão de carregar os dados corretamente.

## 2. Gerar ou atualizar a chave de acesso

Após ativar a autenticação:

1. Realize uma nova exportação para o Power BI ou acesse a tela **Suas Exportações**;
2. Localize os dados de:

   - URL;
   - Valor;
   - Chave de acesso.

**Caso ainda não exista uma chave gerada**, clique na opção para gerar uma nova chave de acesso.

**Caso já exista uma URL configurada no Power BI**, você poderá reutilizar a mesma URL e atualizar apenas os campos de Valor e Chave de acesso no Power BI.

**Caso já exista uma chave de acesso**, a chave pode ser atualizada a qualquer momento. Após gerar uma nova chave, será necessário atualizar também a configuração correspondente no Power BI.

![Imagem 2: Caso já exista uma chave de acesso , a chave pode ser atualizada a qualquer momento. Após gerar uma nova chave, será…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427573903/944f06182c2ec76628fc4b96d06c/image.png?expires=1786536000&signature=4bc26b165593f4098d55e4edc5291f0ea8b925c0d974432c6f2905f937500f99&req=diQlEcx5nohfWvMW3nq%2BgTvLMmHo%2BXX%2FukxNpUqrg%2Fz8yx6053ncLTUB3EWL%0A9Plw4d8bJVSxa721r8%2FSiqt3wdY%3D%0A)

## 3. Configurar a chave no Power BI

Após identificar os dados de autenticação no Ploomes:

1. Acesse o Power BI;
2. Localize a configuração da conexão utilizada;
3. No campo **Parâmetros do cabeçalho de solicitação HTTP**, preencha:

   - No campo da esquerda: o **Valor** informado no Ploomes;
   - No campo da direita: a **Chave de acesso** correspondente.

![Imagem 3: No campo da direita: a Chave de acesso correspondente.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427574498/dff3a5b25b6be93759281f3d57ff/image.png?expires=1786536000&signature=cb2e16aa6253aabcd8302d55a1a6f2426e8f3178c70f6db82eb7592d4f59dfd3&req=diQlEcx5mYVWUfMW3nq%2BgaMHs9RWaMGBIAb2AWBwHzxKoDBQI6lGZ9zwlgjJ%0A0rqripiQ0s6HpZcEk4hC9ARBucU%3D%0A)

## Pronto!

Com isso, as requisições passarão a ser autenticadas corretamente.

## Como funciona a autenticação nas exportações

## URLs sem autenticação

Quando a autenticação estiver desativada:

- Qualquer pessoa com acesso à URL poderá consumir os dados;
- Os campos de Valor e Chave de acesso não serão exibidos.

## URLs com autenticação

Ao ativar a autenticação:

- Cada URL de exportação terá sua própria chave de acesso;
- Será necessário configurar corretamente o Valor e a Chave de acesso no Power BI;
- Requisições sem autenticação válida terão o acesso bloqueado.

## Impacto nas URLs antigas

Todas as URLs de exportação geradas anteriormente passarão a exigir autenticação após a ativação da funcionalidade.

Por isso, será necessário atualizar as configurações existentes no Power BI.

## O que acontece ao desativar a autenticação

Caso a autenticação seja desativada:

- As URLs voltarão a funcionar sem autenticação;
- As chaves geradas anteriormente serão desconsideradas.

## Avisos de segurança e comportamento do sistema

- Um alerta será exibido ao ativar a autenticação, reforçando que as URLs antigas passarão a exigir chave.
- A chave deve ser inserida corretamente no Power BI para não interromper o consumo de dados.
- A qualquer momento você poderá gerar uma nova URL ou uma nova chave. Lembre-se de sempre manter esses campos atualizados no Power BI.

## Limitações da funcionalidade

- Cada URL exportada possui sua própria chave de acesso;
- Chaves não podem ser reutilizadas entre exportações diferentes;
- Caso o usuário responsável pela exportação seja desativado ou perca a permissão de exportação, a URL correspondente deixará de funcionar;
- A atualização da chave exige reconfiguração no Power BI.

## Perguntas frequentes

**1. O que acontece com as** URLs **antigas quando ativo a chave?**

As URLs antigas passam a exigir a chave de autenticação.

Caso a configuração não seja atualizada no Power BI, o acesso aos dados será bloqueado.

**2. Posso desativar a exigência de chave a qualquer momento?**

Sim. Ao desativar, as URLs voltam a funcionar normalmente, sem necessidade de autenticação.

**3. Como validar se minha chave está funcionando?**

Após configurar corretamente os parâmetros no Power BI, os dados serão carregados normalmente.

Caso exista algum erro na autenticação, o Power BI exibirá uma mensagem de falha de acesso.

**4. A minha chave pode ser utilizada em** URLs **geradas por terceiros, mesmo que para a exportação de uma mesma aba?**

Não. Cada exportação possui sua própria URL e sua própria chave de acesso, mesmo quando dois usuários exportam a mesma aba.

**5. A chave de acesso influencia nos prazos de expiração?**

Não. A chave de acesso e o prazo de expiração são configurações independentes.

**6. Ativei a integração. Ainda posso acessar meu relatório/dashboard externamente pela URL do Power BI na web ou em outros sistemas?**

Não. Após ativar a autenticação por chave, qualquer integração ou consulta externa que utilize apenas a URL de exportação deixará de funcionar sem autenticação válida. Os dados passam a ser acessíveis apenas dentro da plataforma, garantindo mais segurança e controle dos dados.

## Glossário

- **Chave de acesso/autenticação:** código gerado que permite validar o acesso a uma URL de dados exportados.
- **Power BI:** ferramenta da Microsoft utilizada para análise e visualização de dados.
- **URL de exportação:** URL que permite consumir dados do Ploomes diretamente no Power BI.
- **Parâmetros do cabeçalho de solicitação HTTP:** são informações extras, ou "cabeçalhos de solicitação" específicos, que você envia para realizar uma consulta de informações na WEB. No nosso caso, preenchemos e enviamos as informações de autenticação para que o servidor possa reconhecer quem deseja fazer a solicitação e, caso as credenciais correspondam ao esperado, os dados extraídos do Ploomes para o Power BI serão apresentados.

## Artigos relacionados

[Nova Integração Power BI](https://sankhya.zendesk.com/hc/pt-br/articles/42427413992983)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
