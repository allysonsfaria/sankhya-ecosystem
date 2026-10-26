---
id: "42427587989783"
titulo: "Atualizações de Agosto de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427587989783-Atualiza%C3%A7%C3%B5es-de-Agosto-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:08Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12044193", "sync_hash_7a8324046b84"]
---

# Atualizações de Agosto de 2025

## [01/08/2025] [Correção]

- Havia uma propriedade na consulta que o exportador estava fazendo para a API2 que não estava sendo encontrada, ocorrendo erro na exportação de abas para Excel. A consulta foi corrigida substituindo a propriedade 'Name' por 'Id'.

## [07/08/2025] [Correção]

- Na integração Sankhya, durante a edição de propostas, corrigimos as consultas individuais de impostos para considerarem as despesas acessórias preenchidas. Agora, ao agendar uma consulta individual, o sistema verifica se há despesas acessórias e, quando necessário, realiza automaticamente uma consulta em lote. Além disso, melhoramos a integração entre o CPQ e o Sankhya, garantindo uma transmissão mais confiável das informações dos campos, incluindo a implementação de uma rotina de reenvio automático para lidar com requisições que antes eram barradas por concorrência no Sankhya.
- Em fluxos de aprovação, ao buscar campos de "Último atualizador", a opção salva era de "Responsável". Isto ocorria devido ao FieldPath não estar sendo salvo corretamente pela API de cache, o que foi corrigido.

## [11/08/2025] [Correção]

- A tag format e formattable não estavam na whitelist de tags permitidas, o que impedia que fossem salvas no código-fonte de modelos de email utilizado em automações. Agora é possível utilizá-las.

## [13/08/2025] [Correção]

- Ao criar Contatos por meio de formulários externos ou importação de planilhas utilizando um campo chave, o sistema podia atualizar informações de empresas de forma incorreta em vez de criar um novo contato. Isso acontecia porque não era verificado se o cliente era Pessoa ou Empresa, só era verificado a duplicidade pelo campo chave. Agora essa verificação é feita corretamente, considerando o tipo de cliente e o campo chave configurado.
- As views DealSimpleView, OrderSimpleView, QuoteSimpleView possuem propriedades padrão que são diferente de Id ou Name, o que estava quebrando as queries do exportador. Isso foi corrigido para que o exportador utilize as propriedades corretas.

## [21/08/2025] [Correção]

- Mobile: Corrigido a obtenção do OwnerId no formulário de produto e também a chave do Sankhya sandbox para fazer integrações, habilitando integrações no App.
