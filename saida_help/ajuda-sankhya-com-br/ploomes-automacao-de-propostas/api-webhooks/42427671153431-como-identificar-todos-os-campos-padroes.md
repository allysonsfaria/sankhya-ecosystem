---
id: "42427671153431"
titulo: "Como identificar todos os campos (padrões e customizados) e suas chaves no Ploomes para desenvolvimento através da API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427671153431-Como-identificar-todos-os-campos-padr%C3%B5es-e-customizados-e-suas-chaves-no-Ploomes-para-desenvolvimento-atrav%C3%A9s-da-API"
trilha: "PLOOMES: Automação de propostas  > API & Webhooks"
atualizado_em: "2026-08-11T16:14:09Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452436", "sync_hash_10c34a9cde3a"]
---

# Como identificar todos os campos (padrões e customizados) e suas chaves no Ploomes para desenvolvimento através da API

Ao desenvolver integrações ou automações utilizando a API da Ploomes, é essencial saber quais campos estão disponíveis em cada entidade - como Clientes, Negócios, Tarefas, etc. Isso inclui tanto os **campos nativos** quanto os **campos personalizados** (**dinâmicos**).

Este artigo explica como identificar esses campos, consultar suas chaves (FieldKeys) e utilizá-las corretamente em suas requisições.

Confira a documentação completa da nossa API [neste link](https://developers.ploomes.com/).

Confira como obter uma chave de acesso [neste artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427485260695).

## Conceitos introdutórios

## Tipos de campos

- **Campos nativos:** são criados automaticamente pelo sistema e estão presentes em cada entidade (ex: Nome, E-mail, Data de criação).
- **Campos dinâmicos:** são personalizados por cada empresa e criados sob demanda diretamente na plataforma (ex: "E-mail de cobrança", "Status interno", "Fonte do lead").

## O que é a FieldKey?

A `FieldKey` é a chave única que identifica cada campo dentro da API. É por meio dela que os dados dos campos personalizados podem ser manipulados em requisições, como criação ou atualização de registros.

Ela segue o padrão:

```
entidade_GUID
```

Exemplo: `contact_A51DFABF-56CA-4F03-AABB-F89AF0E7D354` → campo da entidade **Clientes** (`/Contacts`)

## Lista das principais entidades disponíveis

| **Entidade** | **EntityId** |
| --- | --- |
| Cliente | 1 |
| Negócio | 2 |
| Venda | 4 |
| Bloco de Venda | 5 |
| Proposta | 7 |
| Bloco de Proposta | 8 |
| Produto | 10 |
| Tarefa | 12 |
| Produto da Proposta | 14 |
| Produto da Venda | 20 |
| Registro de Contato | 36 |

## Consultando campos via API

## Listar todos os campos da conta

Para simplificar esse processo, basta realizar uma chamada GET no endpoint de Fields, dessa forma: https://public-api2.ploomes.com/Fields.

Essa chamada retorna todos os campos disponíveis, incluindo os dinâmicos.

## Filtrar a busca

Você pode aplicar filtros usando o parâmetro $filter.

### Listar apenas campos de uma entidade específica

Para obter todos os campos de uma entidade, como Negócio, basta realizar uma requisição GET neste formato:

https://public-api2.ploomes.com/Fields?$filter=EntityId+eq+2

### Listar apenas os campos dinâmicos de Clientes

Para isso, faça uma chamada GET em Fields com o parâmetro de $filter, dessa forma: https://public-api2.ploomes.com/Fields?$filter=EntityId+eq+1+and+Dynamic+eq+true&$expand=Type($select=NativeType)&$select=Name,Key,Type

`EntityId = 1` → Clientes

`Dynamic = true` → Apenas campos personalizados/dinâmicos

`$select` → Seleciona apenas as propriedades relevantes

[![Imagem 1: $select → Seleciona apenas as propriedades relevantes](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330169/a085427766add8634f072408/image.png-expires%3D1619816400-signature%3D2e07185dc94aa720b97d58d18591af52ccc22fbb88761f0ad2a93133cd437db5?expires=1786536000&signature=e1cd27525d5d115e3842e626598f9d31e5137e90a99c1675f0990eca58b5e3e8&req=dyYuFcp%2BnIdWFb4V1XW4gStt51DsrKefF56rzEF00v9ci3RDLXo2zw0HpHIv%0AhZzV2U23aCsM8NTlIk3EZCllAw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/66477690/54517ff6048730e6bdcc6f6a/image.png?expires=1619816400&signature=2e07185dc94aa720b97d58d18591af52ccc22fbb88761f0ad2a93133cd437db5)

Na imagem acima vemos o resultado da pesquisa.

### Listar campos do tipo 7 (opções pré-cadastradas)

Para campos com opções pré-cadastradas (como "Origem", "Segmento" etc.), é necessário consultar a tabela de opções vinculada.

#### Passo 1: Identificar o `OptionsTableId` do campo

Para isso, consulte os campos usando o endpoint `/Fields` com um `$select` que inclua a propriedade `OptionsTableId`.

No exemplo anterior esta opção não foi mostrada porque omitimos ela ao selecionar apenas o Nome, Chave e Tipo do campo ($select=Name,Key,Type). Mas no exemplo abaixo, esta informação é exibida:

https://public-api2.ploomes.com/Fields@OptionsTables?$filter=Id+eq+1204&$expand=Options

[![Imagem 2: https://public-api2.ploomes.com/Fields@OptionsTables?$filter=Id+eq+1204&$expand=Options](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1659634403/57577241f395054edc5f73ffbc32/image.png-expires-3D1619816400-signature-3De20d92346f19b11337019be81fed985f0af7c9e289cc5315b5de94a34df1cc0c?expires=1786536000&signature=2997b542c715a18848ddcb4f873e532c3b20829b6d70bf2435c4fdfa9edf35e5&req=dSYiH899mYVfWvMW3nq%2BgZYeu6sKJd%2FiuuwopjjhV%2B2rn%2F%2BF4rsiY82Rb2yr%0AHOlQbknGuY8hsqwR4tZ9i7pj5UM%3D%0A)](https://downloads.intercomcdn.com/i/o/66481025/5c630be7ddc0935dc9ef5e40/image.png?expires=1619816400&signature=e20d92346f19b11337019be81fed985f0af7c9e289cc5315b5de94a34df1cc0c)

Na imagem acima vemos o resultado.

#### Passo 2: Consultar as opções disponíveis

Usando o código 1204 retornado, pode-se então realizar uma chamada em OptionsTable para descobrir todas as opções válidas, como mostrado abaixo:

https://public-api2.ploomes.com/Fields@OptionsTables?$filter=Id+eq+1204&$expand=Options

A resposta mostrará todas as opções válidas, com seus respectivos IDs.

[![Imagem 3: A resposta mostrará todas as opções válidas, com seus respectivos IDs.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1659634402/093135aec81f11e450bea009833d/image.png-expires-3D1619816400-signature-3Da1464cc8236233a74242beb0be84c10ace97c03ec5a2741dfd5d87d776620585?expires=1786536000&signature=ccf2aeab878485eb2ea6ca74df275090a7db6a9cccd63de3b61c7e9f38d0d2b6&req=dSYiH899mYVfW%2FMW3nq%2BgVp7g2F8obUnrK2zS3zfqiCU7GPcAax0DpG16Tfi%0AFEFOOh%2B%2Bx0XUZXNG4vpUVnRhJfM%3D%0A)](https://downloads.intercomcdn.com/i/o/66481467/76199c9b80c244bce6cd7174/image.png?expires=1619816400&signature=a1464cc8236233a74242beb0be84c10ace97c03ec5a2741dfd5d87d776620585)

Na imagem acima vemos o resultado.

Se a intenção for adicionar uma Empresa e informar que a "Faculdade" relacionada é "Universidade Federal do Rio Grande do Norte", basta dar um POST em "Contacts" e incluir um objeto no Array de OtherProperties.

**Exemplo**

```
"OtherProperties": [
  {
    "FieldKey": "contact_94F9848B-7F0A-4BC4-9BC6-E1E9D846563B",
    "IntegerValue": 18653
  }
]
```

### Listar campos específicos como "Telefones"

Para campos como "Telefones", que armazenam conjuntos de números, é necessário expandir o objeto "Phones" no Endpoint "Contacts" durante uma requisição GET.

**Exemplo**

[https://public-api2.ploomes.com/Contacts?$expand=Phones](https://public-api2.ploomes.com/Contacts?%24expand=Phones)

![Imagem 4: https://public-api2.ploomes.com/Contacts?$expand=Phones](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1659634406/a98cf2635448d70bd88a0c99b836/phonesPostman.png?expires=1786536000&signature=ada061f198d5f5cc026414318577cc235f36ace1e2344431ae454d98690be8dc&req=dSYiH899mYVfX%2FMW3nq%2BgUZR6BV1V7s7ghChMsfC7kIAcLJqm%2FXgeF%2B5thuS%0AZ2Jbe2g9QUfFxLIpmhnVPioQfEM%3D%0A)

Na imagem acima vemos o resultado.

## Utilizando campos personalizados (dinâmicos) em requisições

Uma vez com a `FieldKey` em mãos, você pode usá-la em requisições `POST` ou `PATCH` dentro do objeto `OtherProperties`.

Exemplo: criar um Cliente com o campo "E-mail de cobrança" preenchido

POST em /Contacts:

```
{
  "Name": "Cliente Exemplo",
  "OtherProperties": [
    {
      "FieldKey": "contact_A51DFABF-56CA-4F03-AABB-F89AF0E7D354",
      "StringValue": "cobranca@ploomes.com"
    }
  ]
}
```

O tipo do campo define o sufixo usado na propriedade de valor:

- String → `StringValue`
- Inteiro → `IntegerValue`
- Booleano → `BooleanValue`
- Decimal → `DecimalValue`
- Data → `DateTimeValue`

###

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 5: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1385479731/13eb2ab96091c61dc858afac0fb9/Introdu-C3-A7-C3-A3o%2B-C3-A0%2BAPI%2Bdo%2BPloomes.png?expires=1786536000&signature=0ae3e441fef6b9bea0a5a96cd9cbe13a28f719a02c0096d176760df1b3afa01e&req=dSMvE815lIZcWPMW3nq%2BgbeFtyepsm4OhM1qfseE9WxS2RZ0jV%2Fm8nLlNnj3%0Aq1okqsDWY5Q6WOYoOlsdikz%2FaCY%3D%0A)](https://universidade.ploomes.com/courses/introducao-a-api-do-ploomes)

---

Dúvidas, comentários ou sugestões? Entre em contato com nosso time de suporte! Nos vemos online.
