---
id: "42427633040151"
titulo: "Como utilizar os Webhooks do Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427633040151-Como-utilizar-os-Webhooks-do-Ploomes"
trilha: "PLOOMES: Automação de propostas  > API & Webhooks"
atualizado_em: "2026-08-11T16:14:08Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452439", "sync_hash_705621d62a77"]
---

# Como utilizar os Webhooks do Ploomes

Ploomes conta com a funcionalidade de Webhooks. Para contextualizar, um Webhook é um meio pelo qual um sistema fornecer informações em tempo real para outras aplicações ou serviços. Por exemplo: sempre que uma venda for cadastrada no Ploomes, enviar os dados para um ERP.

## Como habilitar

Para habilitar os Webhooks na sua conta, é necessário fazer uso da API do Ploomes. O primeiro passo é registrar um **endpoint** para receber dados quando uma determinada **ação** no Ploomes acontecer. Um **endpoint** é simplesmente um endereço acessível por HTTP, pode ser um Webservice ou uma API própria ou de terceiros. Uma **ação** pode ser, por exemplo:

- Cadastrar um cliente
- Atualizar uma proposta
- Finalizar uma tarefa
- Excluir um Lead

Para realizar o registro, basta fazer um POST no seguinte endereço:
https://api2.ploomes.com/Webhooks

É necessário utilizar sua chave de integração no Header da requisição, na forma de um parâmetro 'User-Key' e o corpo da requisição deve contar os seguintes atributos:
{
 "EntityId": 1,
 "ActionId": 2,
 "CallbackUrl": "sua\_url\_de\_recebimento",
 "ValidationKey": "1234"
}

O exemplo acima vai fazer com que dados sejam disparados para um determinado endereço sempre que um Cliente for atualizado.

## Parâmetros

Abaixo a explicação para cada atributo:

- **EntityId:** a entidade que você deseja utilizar. Uma entidade pode ser um Cliente, um Negócio, uma Proposta, Lead, Tarefa, entre outros. O link abaixo leva para um artigo com informações sobre todas as entidades disponíveis:
  [Como identificar todos os campos (padrões e customizados) e suas chaves no Ploomes para desenvolvimento através da API](https://sankhya.zendesk.com/hc/pt-br/articles/42427671153431)

- **ActionId:** o ID da ação. Uma ação pode ser, por exemplo, criação, deleção, atualização ou ações específicas para algumas entidades, como no caso de Negócios que podem ser Ganhos, Perdidos e Reabertos e Tarefas que podem ser finalizadas. Para saber quais as ações disponíveis, basta dar um GET no seguinte endereço (sempre se lembre da chave do usuário no Header):
  https://public-api2.ploomes.com/Webhooks@Actions

- **CallbackUrl:** a URL (endereço WEB) que receberá os dados enviados pelos Webhooks do Ploomes

- **ValidationKey:** uma chave que pode ser criada (inventada) e usada no endereço que vai receber os dados do Ploomes. Com ela, é possível validar se as requisições estão sendo enviadas pelo Ploomes mesmo e rejeitar as demais, no caso de alguém descobrir seu serviço e tentar algum ataque, por exemplo.

Na mensagem enviada, a chave de validação (ValidationKey) estará no Header com o nome **X-Ploomes-Validation-Key**

## Corpo do Payload (exemplo)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Body:
{
 "Action": "**Update**",
 "Entity": "**Contacts**",
 "AccountId": **57**,
 "ActionUserId": **116**,

"**Old**":
 {
 "OtherProperties": {
 "contact\_check": **false** //CAMPOS CUSTOMIZÁVEIS DA CONTA
 },
 "Phones": [
 {
 "PhoneNumber": "**(11) 3842-6673**",
 "TypeId": 1,
 "CountryId": 76
 }
 ],
 "Tags": [
 {
 "TagId": **290**
 }
 ],
 "Id": 2630362,
 "LegalName": "**Ploomes**",
 },

"**New**":
 {
 "OtherProperties": {
 "contact\_check": **true**
 },
 "Phones": [
 {
 "PhoneNumber": "**(11) 4380-7749**",
 "TypeId": 1,
 "CountryId": 76
 }
 ],
 "Tags": [
 {
 "TagId": **287**
 }
 ],
 "Id": 2630362,
 "LegalName": "**Ploomes Sistemas Empresariais"**,
 }
}
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Análise do payload

"Action": "**Update**", --> **Atualização**
"Entity": "**Contacts**", --> **de Contato**
"AccountId": **57**, --> **ID da conta Ploomes**
"ActionUserId": **116**, --> **ID do usuário que gerou a ação (atualizou o contato)**

**Old** --> Detalhes de como eram os campos **ANTES** da atualização - somente os campos alterados são retornados. Pode ser NULL caso seja uma **Criação**.
**New** --> Detalhes dos valores dos campos **DEPOIS** da atualização.

Com o atributo **ActionUserId** e os objetos **OLD** e **NEW** é possível identificar os valores antes e depois de cada alteração e com isso fazer tratativas específicas para cada caso.

Exemplo de caso de uso: Se um usuário (**ActionUserId**) da equipe financeira editar o campo 'Análise de crédito concluída' de **Falso** para **Verdadeiro**, enviar um e-mail para o responsável pelo Negócio informando que a análise foi concluída e agora o processo comercial pode prosseguir.

Para acessar obter acesso à API do Ploomes, acesse o link abaixo:
[Como obter acesso à API do Ploomes](https://sankhya.zendesk.com/hc/pt-br/articles/42427485260695)

## Requisitos e recomendações

Para utilizar a API do Ploomes de forma segura e eficiente, é importante atender a alguns requisitos básicos:

- **Perfil técnico necessário:** o uso da API é recomendado exclusivamente para profissionais com conhecimento em desenvolvimento de software. A pessoa que realizará a integração deve ter familiaridade com conceitos como requisições HTTP (GET, POST, PUT, DELETE), autenticação por API Key, consumo de dados em JSON e estrutura de APIs REST/OData.
- **Estudo da documentação:** antes de iniciar qualquer integração, é fundamental estudar atentamente a [documentação da API do Ploomes](https://developers.ploomes.com/). Isso garante uma melhor compreensão dos endpoints disponíveis, parâmetros, estrutura de dados e boas práticas de uso.
- **Conhecimento da plataforma de destino:** se a API do Ploomes for utilizada em uma integração com outro sistema, também é necessário que a pessoa desenvolvedora compreenda a **API da outra plataforma** envolvida - para garantir que ambas as pontas da integração sejam tratadas corretamente.
- **Boas práticas de desenvolvimento:** recomenda-se implementar tratamento de erros, controle de fluxo (rate limiting) e lógica de retentativa em caso de falhas temporárias.

⚠️ Importante: não é recomendado que usuários sem experiência técnica ou sem acompanhamento de uma pessoa desenvolvedora tentem realizar integrações diretamente pela API.

Caso tenha dúvidas sobre a utilização dos Webhooks ou precisar de informações adicionais, nossa equipe de suporte estará sempre à disposição para ajudar.
