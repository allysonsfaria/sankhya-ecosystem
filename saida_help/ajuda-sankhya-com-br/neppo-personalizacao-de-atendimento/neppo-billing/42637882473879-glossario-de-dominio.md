---
id: "42637882473879"
titulo: "Glossário de Domínio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42637882473879-Gloss%C3%A1rio-de-Dom%C3%ADnio"
trilha: "NEPPO: Personalização de atendimento > Neppo Billing"
atualizado_em: "2026-08-11T17:13:21Z"
rotulos: ["sync_hc", "neppo", "neppo_916389890", "sync_hash_846e71cfaa2b"]
---

# Glossário de Domínio

Termos usados no Neppo Billing — e apenas nesse sentido. Antes de usar um desses
nomes com outro significado (ou de propor um termo novo), confira aqui.

## Operation (Operação)

Um **cliente/implantação** — na prática, 1 Operation = 1 banco de dados de cliente. É
a unidade de coleta: o job de ingestão itera as Operations ativas e coleta o consumo
de cada uma, de forma independente.

## Instance (Instância)

Um **servidor de banco de réplica** (MySQL/MariaDB) de onde o sistema lê os dados dos
clientes. Um servidor (Instance) hospeda várias Operations, cada uma em seu próprio
banco/schema — a credencial de acesso é do servidor; o nome do banco específico fica
na Operation. Senha de acesso é criptografada em repouso (AES-256).

## License (Licença)

Um **template SQL nomeado** que mede uma métrica específica (ex.: "mensagens SMS
enviadas no dia"). É executado sobre os dados já coletados de cada Operation, um dia
de cada vez — o total do mês é a soma dos dias.

> Não confundir com "licença de software" no sentido comum: aqui é a definição de uma
> métrica de consumo, não um direito de uso.

## Package (Pacote / Plano)

Uma **entrada de catálogo** que agrupa uma License, representando um "plano" em termos
de negócio. **Não carrega nenhum valor monetário** — é só metadado de catálogo (nome,
código de integração) para o sistema de billing downstream resolver o produto/SKU na
hora da sincronização. Um Package **não decide** se uma License roda para uma
Operation — isso já roda para todas as Operations ativas, independente de Package.

## Consumption (Consumo)

O **registro central** do sistema: o resultado de rodar uma License sobre uma
Operation em um dia específico. Guarda a **quantidade** medida (nunca um valor em
dinheiro). É append-only — nunca sobrescrito; uma correção gera um novo registro
(revisão) e marca o antigo como substituído.

## Os três jobs

- **IngestionJob** — coleta os dados brutos do dia de cada Operation
- **ConsolidationJob** — roda as Licenses sobre os dados coletados e grava Consumption
- **ApiSyncJob** — envia os registros de Consumption pendentes para a API externa

**Ver também:** [Como Funciona](https://sankhya.zendesk.com/hc/pt-br/articles/42637911579543) · [Perguntas Frequentes](https://sankhya.zendesk.com/hc/pt-br/articles/42637911712407)
