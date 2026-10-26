---
id: "42430352793239"
titulo: "Componente Sankhya - Dados do Cliente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:13:30Z"
rotulos: ["sync_hc", "neppo", "neppo_857998528", "sync_hash_fc385507b394"]
---

# Componente Sankhya - Dados do Cliente

O componente **Dados do Cliente** permite consultar, dentro do fluxo do bot, os dados cadastrais de um parceiro (cliente ou fornecedor) registrados no ERP Sankhya utilizando **CPF ou CNPJ** como identificador principal.

bot-server: **versão 1.4.0**

bot-component-service: **versão 1.0.0**

Doc Sankhya: <https://developer.sankhya.com.br/docs/operacoes-comerciais#tgfpar>

![Imagem 1: Doc Sankhya: https://developer.sankhya.com.br/docs/operacoes-comerciais#tgfpar](https://ajuda.sankhya.com.br/hc/article_attachments/42639630554263)

Esse componente possibilita:

- Personalização do atendimento
- Validações cadastrais
- Regras comerciais baseadas em crédito
- Automação de fluxos de venda, cobrança e suporte
- Enriquecimento de dados para integrações posteriores

Os dados retornados são armazenados em uma variável do fluxo e podem ser reutilizados em qualquer etapa subsequente do bot.

Índice:

- [Objetivo do componente](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Objetivo-do-componente)
- [Integração técnica](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Integracao-tecnica)
- [Configuração no construtor de bot](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Configuracao-no-construtor-de-bot)
- [Estrutura do retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Estrutura-do-retorno)
- [Descrição dos campos retornados](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Descricao-dos-campos-retornados)
- [Mapeamento técnico Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Mapeamento-tecnico-Sankhya)
- [Boas práticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Boas-praticas)
- [Segurança e performance](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Seguranca-e-performance)
- [Dependências técnicas](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Dependencias-tecnicas)
- [Exemplo de fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Exemplo-de-fluxo)
- [Retorno de erro](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430352793239-Componente-Sankhya-Dados-do-Cliente#Retorno-de-erro)

- [Dados do Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42430352793239)
- [Obter pedidos](https://sankhya.zendesk.com/hc/pt-br/articles/42430345961879)
- [Itens do Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430353726743)
- [Criar Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430354191767)
- [Preço do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430386027287)
- [Estoque do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430402782487)
- [Locais de Estoque](https://sankhya.zendesk.com/hc/pt-br/articles/42430348719383)
- [Volumes Alternativos](https://sankhya.zendesk.com/hc/pt-br/articles/42430361336343)
- [Obter Preferência](https://sankhya.zendesk.com/hc/pt-br/articles/42430349855127)
- [Tabela de Preço](https://sankhya.zendesk.com/hc/pt-br/articles/42430362758935)
- [Tipo de Operação](https://sankhya.zendesk.com/hc/pt-br/articles/42430406143383)
- [Tipos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/42430364291351)
- [Detalhe do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430364864407)
- [Busca de Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430376763159)
- [Adicionar ao Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377203479)
- [Alterar Quantidade no Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377845911)
- [Obter Itens do Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430378480151)

---

## Objetivo do componente

Centralizar e disponibilizar, dentro do Construtor de Bot Neppo, informações oficiais do cadastro do cliente no Sankhya para suportar automações conversacionais inteligentes.

---

## Integração técnica

A consulta é realizada via integração com serviços internos Neppo responsáveis pela comunicação com o Sankhya.

Os dados são obtidos principalmente da tabela:

- TGFPAR – Cadastro de Parceiros

E também de tabelas relacionadas:

- TSIEND – Endereços
- TSICID – Cidade
- TSIBAI – Bairro

---

## Configuração no construtor de bot

### Parâmetros de entrada

#### CPF/CNPJ (Obrigatório)

Documento do cliente utilizado como chave de busca no Sankhya.

Exemplo:

```
{{cpfCliente}}
{{cnpjCliente}}
```

---

### Armazenamento

#### Variável de armazenamento

Define onde o retorno da consulta será salvo.

Exemplo:

```
dadoCliente
```

---

#### Variável de Escopo global

Quando habilitada:

- Torna os dados acessíveis em todo o fluxo
- Permite reutilização em múltiplos componentes
- Evita novas consultas desnecessárias

---

## Estrutura do retorno

### Exemplo completo

```
{
  "found": true,
  "data": {
    "code": "654",
    "document": "10.884.449/0001-XX",
    "type": "J",
    "name": "EMPRESA EXEMPLO LTDA",
    "tradeName": "EMPRESA EXEMPLO S/A",
    "gender": null,
    "birthDate": "DD/MM/AAAA",
    "authGroup": "V",
    "active": true,
    "hasSupplier": true,
    "creditLine": 50000,
    "stateRegistration": "ISENTO",
    "contact": {
      "phoneNumber": null,
      "cellphoneOrFaxNumber": "(34) 9XXXX-XXXX",
      "email": "financeiro@empresaexemplo.com.br",
      "nfseEmail": "nfse@empresaexemplo.com.br",
      "cteEmail": "cte@empresaexemplo.com.br",
      "deliveryNotificationEmail": "notificacoes@empresaexemplo.com.br"
    },
    "address": {
      "streetName": "Rua Exemplo",
      "streetType": "Av",
      "number": "XXX",
      "complement": "Sala X",
      "neighborhood": "Bairro Exemplo",
      "city": "Cidade Exemplo",
      "state": "UF",
      "postalCode": "00000-000",
      "latitude": null,
      "longitude": null
    }
  },
  "error": null
}
```

---

## Descrição dos campos retornados

### Informações básicas

| Campo | Descrição |
| --- | --- |
| found | Indica se o cliente foi encontrado |
| code | Código do parceiro |
| document | CPF ou CNPJ |
| type | F (Pessoa Física) / J (Pessoa Jurídica) |
| name | Nome do parceiro |
| tradeName | Razão social |
| gender | Sexo |
| birthDate | Data nascimento ou fundação |
| active | Cliente ativo |
| hasSupplier | Indica se também é fornecedor |
| stateRegistration | Inscrição estadual |

---

### Informações de crédito

| Campo | Descrição |
| --- | --- |
| creditLine | Limite de crédito cadastrado |
| authGroup | Grupo de autorização |

---

### Informações de contato

| Campo | Descrição |
| --- | --- |
| phoneNumber | Telefone fixo |
| cellphoneOrFaxNumber | Celular ou Fax |
| email | Email principal |
| nfseEmail | Email NFS-e |
| cteEmail | Email CT-e |
| deliveryNotificationEmail | Email notificações de entrega |

---

### Endereço

| Campo | Descrição |
| --- | --- |
| streetType | Tipo do logradouro |
| streetName | Nome do logradouro |
| number | Número |
| complement | Complemento |
| neighborhood | Bairro |
| city | Cidade |
| state | UF |
| postalCode | CEP |
| latitude | Latitude |
| longitude | Longitude |

---

## Mapeamento técnico Sankhya

| Campo JSON | Campo Sankhya | Tabela | Comentário |
| --- | --- | --- | --- |
| `data.code` | Cód. Parceiro | TGFPAR.CODPARC | Identificador único |
| `data.document` | CPF/CNPJ | TGFPAR.CGC\_CPF | Documento do cliente |
| `data.type` | Tipo de Pessoa | TGFPAR.TIPPESSOA | F: Física, J: Jurídica |
| `data.name` | Nome Parceiro | TGFPAR.NOMEPARC | Nome completo |
| `data.tradeName` | Razão Social | TGFPAR.RAZAOSOCIAL | Nome fantasia |
| `data.gender` | Sexo | TGFPAR.SEXO | M, F, ou null |
| `data.birthDate` | Data Nascimento | TGFPAR.DTNASC | Pessoa física ou fundação |
| `data.authGroup` | Grupo Autorização | TGFPAR.GRUPOAUTOR | Controle de acesso |
| `data.active` | Cliente Ativo | TGFPAR.CLIENTE | true/false |
| `data.hasSupplier` | Fornecedor | TGFPAR.FORNECEDOR | true/false |
| `data.creditLine` | Limite de Crédito | TGFPAR.LIMCRED | Valor R$ |
| `data.stateRegistration` | Insc. Estadual | TGFPAR.IDENTINSCESTAD | ou “ISENTO” |
| `data.contact.phoneNumber` | Telefone | TGFPAR.TELEFONE | Fixo |
| `data.contact.cellphoneOrFaxNumber` | Celular/Fax | TGFPAR.FAX | Celular principal |
| `data.contact.email` | Email | TGFPAR.EMAIL | Contato |
| `data.contact.nfseEmail` | Email NFSe | TGFPAR.EMAILNFSE | Específico para nota |
| `data.contact.cteEmail` | Email CTe | TGFPAR.EMAILCTE | Específico para transporte |
| `data.contact.deliveryNotificationEmail` | Email Entrega | TGFPAR.EMAILNOTIFENTREGA | Confirmações |
| `data.address.streetName` | Endereço | TSIEND.NOMEEND | Nome da rua |
| `data.address.streetType` | Prefixo (Av/Rua) | TSIEND.TIPO | Ex: “Av” |
| `data.address.number` | Número | TGFPAR.NUMEND | n° |
| `data.address.complement` | Complemento | TGFPAR.COMPLEMENTO | Sala, bloco, etc. |
| `data.address.neighborhood` | Bairro | TSIBAI.NOMEBAI | Bairro do endereço |
| `data.address.city` | Cidade | TSICID.NOMECID | Nome da cidade |
| `data.address.state` | UF | TSICID.UF | Estado |
| `data.address.postalCode` | CEP | TGFPAR.CEP | Código postal |
| `data.address.latitude` | Latitude | TGFPAR.LATITUDE | Coordenada geográfica |
| `data.address.longitude` | Longitude | TGFPAR.LONGITUDE | Coordenada geográfica |

---

## Boas práticas

- Validar CPF/CNPJ antes da consulta
- Evitar múltiplas chamadas desnecessárias
- Utilizar escopo global quando aplicável
- Sempre prever fallback para cliente não encontrado

---

## Segurança e performance

- Dados respeitam permissões do ERP
- Consulta realizada via APIs autenticadas
- Cache recomendado para fluxos intensivos

---

## Dependências técnicas

- Integração Sankhya habilitada
- Credenciais configuradas
- Permissão de leitura do cadastro de parceiros

---

## Exemplo de fluxo

```
Usuário informa CPF/CNPJ
        ↓
Componente Dados do Cliente
        ↓
Consulta Sankhya
        ↓
Retorna dados
        ↓
Armazena em variável
        ↓
Fluxo continua com dados enriquecidos
```

---

## Retorno de erro

1. **Dados Cliente com CPF/CNPJ incorreto**
   Quando o CPF/CNPJ informado estiver em formato inválido (ex.: curto, com caracteres incorretos ou fora do padrão), a API retorna `found=false` e traz um objeto de erro indicando validação.

```
{
  "scenario": "Dados Cliente com CPF/CNPJ incorreto",
  "input": {
    "documentType": "CPF",
    "document": "123"
  },
  "response": {
    "found": false,
    "data": null,
    "error": {
      "code": "INVALID_DOCUMENT",
      "message": "Invalid document. Please provide a valid CPF or CNPJ"
    }
  }
}
```

2. **Dados Cliente com CPF não cadastrado na base**
   Quando o CPF/CNPJ estiver válido, mas não existir registro na base, a API retorna `found=false` sem erro (erro `null`), indicando ausência de cadastro.

```
{
  "scenario": "Dados Cliente com CPF não cadastrado na base",
  "input": {
    "documentType": "CPF",
    "document": "123.456.789-00"
  },
  "response": {
    "found": false,
    "data": null,
    "error": null
  }
}
```

- [Dados do Cliente](https://sankhya.zendesk.com/hc/pt-br/articles/42430352793239)
- [Obter pedidos](https://sankhya.zendesk.com/hc/pt-br/articles/42430345961879)
- [Itens do Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430353726743)
- [Criar Pedido](https://sankhya.zendesk.com/hc/pt-br/articles/42430354191767)
- [Preço do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430386027287)
- [Estoque do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430402782487)
- [Locais de Estoque](https://sankhya.zendesk.com/hc/pt-br/articles/42430348719383)
- [Volumes Alternativos](https://sankhya.zendesk.com/hc/pt-br/articles/42430361336343)
- [Obter Preferência](https://sankhya.zendesk.com/hc/pt-br/articles/42430349855127)
- [Tabela de Preço](https://sankhya.zendesk.com/hc/pt-br/articles/42430362758935)
- [Tipo de Operação](https://sankhya.zendesk.com/hc/pt-br/articles/42430406143383)
- [Tipos de Negociação](https://sankhya.zendesk.com/hc/pt-br/articles/42430364291351)
- [Detalhe do Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430364864407)
- [Busca de Produto](https://sankhya.zendesk.com/hc/pt-br/articles/42430376763159)
- [Adicionar ao Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377203479)
- [Alterar Quantidade no Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430377845911)
- [Obter Itens do Carrinho](https://sankhya.zendesk.com/hc/pt-br/articles/42430378480151)
