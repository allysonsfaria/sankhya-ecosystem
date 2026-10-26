---
id: "44012135227159"
titulo: "Diferença entre os relatórios fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012135227159-Diferen%C3%A7a-entre-os-relat%C3%B3rios-fiscais"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:20:31Z"
rotulos: ["sync_hc", "magis5", "magis5_211397687653", "sync_hash_2e917da6d97e"]
---

# Diferença entre os relatórios fiscais

## Entenda nesse artigo quais são as principais diferenças entre os relatórios fiscais do Magis5 ERP

---

O Magis5 ERP oferece **três telas** distintas para consultar **Notas Fiscais**. Embora tenham uma aparência semelhante, cada uma possui um objetivo específico e extrai dados de fontes diferentes no sistema.

### Tela de Notas Fiscais

Para acessar a tela de Notas fiscais, vá até a opção **"Vendas"** e depois **"Notas Fiscais".**

![Captura de tela 2026-04-21 084315](https://ajuda.sankhya.com.br/hc/article_attachments/44012114395031)

#### Captura de tela 2026-04-21 090058

Esta é a tela principal para a **gestão operacional** e fiscal de todas as notas geradas no sistema.

#### Finalidade

Seu objetivo é fornecer uma visão completa e centralizada das notas fiscais criadas na plataforma. Ela exibe:

- Todas as notas fiscais, tanto de **venda** quanto de **devolução**.
- Notas que possuem um **pedido de venda vinculado** e também as que **não possuem**.

**⚠️ Importante:** Apenas notas geradas **dentro do sistema** são consideradas, excluindo documentos fiscais que foram apenas importados ou recebidos de terceiros.

#### Fonte dos Dados

As informações são consultadas diretamente na tabela de Notas Fiscais do sistema, refletindo os dados exatos de cada documento.

#### Funcionamento dos Filtros

Todos os filtros atuam diretamente sobre as informações da nota fiscal:

- **Filtro de Data:** Considera sempre a **data de emissão** da nota.
- **Outros Filtros:** Status, número da NF-e e demais campos referem-se aos dados da própria nota.

#### Quando Utilizar esta Tela É a tela ideal para tarefas operacionais e fiscais. Use-a para:

- Consultar todas as notas fiscais emitidas em um determinado período.
- Verificar o status de uma NF-e (se foi autorizada, cancelada, etc.).
- Obter uma visão geral da movimentação fiscal gerada pelo sistema.

### BI (Business Intelligence) – Visão de Notas Fiscais

Para acessar a tela de BI, vá até a opção **"Gerenciamento"** e depois **"Business Intelligence".**

![Captura de tela 2026-04-21 085249](https://ajuda.sankhya.com.br/hc/article_attachments/44012089596055)

![Captura de tela 2026-04-21 090230](https://ajuda.sankhya.com.br/hc/article_attachments/44012123041303)

Este é um **relatório gerencial** desenhado para a **análise de vendas**, utilizando as notas fiscais como parte do contexto comercial.

#### Finalidade

O foco desta tela é puramente **analítico e comercial**. Ela exibe apenas as notas fiscais que estão diretamente vinculadas a um pedido de venda, permitindo cruzar dados fiscais com informações estratégicas do negócio.

#### Fonte dos Dados

Diferente da tela operacional, a fonte de dados primária aqui é a **tabela de Vendas**. As notas fiscais aparecem como uma consequência, ou seja, **são um atributo de uma venda já existente.**

#### ⚠️ Atenção: O Funcionamento do Filtro de Data

Este é o ponto mais importante de diferenciação entre as telas.

- Os filtros de data deste relatório **utilizam a data da VENDA**, e não a data de emissão da nota fiscal.

**O que isso significa na prática?**
Uma nota fiscal emitida em um mês, mas referente a uma venda do mês anterior, aparecerá em períodos diferentes em cada tela. **Isso não é um erro**, mas sim o reflexo de duas perspectivas diferentes: uma operacional **(quando a nota foi emitida)** e uma comercial **(quando a venda foi realizada).**

#### Quando Utilizar esta Tela

É a ferramenta ideal para uma visão **gerencial e estratégica**. Use-a quando o objetivo for:

- Analisar a performance de vendas em um período.
- Cruzar dados das notas com **vendedor, cliente, produtos e valores**.
- Entender o faturamento sob a ótica das vendas, e não apenas da emissão fiscal.

### Relatório de Tributos sobre Notas Fiscais

Para acessar a tela de Tributos sobre Notas Fiscais, vá até a opção **"Relatórios"** e depois **"Tributos sobre Notas Fiscais".**

![Captura de tela 2026-04-21 085835](https://ajuda.sankhya.com.br/hc/article_attachments/44012089756311)

![Captura de tela 2026-04-21 090314](https://ajuda.sankhya.com.br/hc/article_attachments/44012114916119)

Este é um relatório **exclusivamente fiscal**, projetado para a análise detalhada de i**mpostos e conferência tributária**, servindo de apoio direto à contabilidade.

#### Finalidade

Seu objetivo é analisar os valores tributários das operações. Diferente das telas operacional e analítica, o foco aqui está nos **impostos**, **tipos de operação fiscal** e **totais fiscais** de notas de entrada e saída.

#### Fonte dos Dados e Critérios de Inclusão

A base de dados são as Notas Fiscais, mas a exibição de uma nota no relatório depende de regras específicas para cada tipo de operação.

- **Notas de Entrada**

O relatório considera **apenas notas que tiveram uma entrada de estoque efetivada no sistema**.

**⚠️ Importante:** Notas que foram apenas recebidas ou importadas, mas que não movimentaram o estoque, **não serão exibidas**.

- **Notas de Saída**

Para uma nota de saída aparecer, ela deve atender a **TODOS** os seguintes critérios:

1. Estar **vinculada a uma venda**.
2. A venda correspondente precisa ter **pelo menos um item**.
3. A venda **não pode ter sido excluída**.
4. A nota fiscal precisa **possuir um número**.

Se os critérios acima forem atendidos, o relatório pode incluir diversas naturezas de operação de saída, como **venda, devolução, remessa, transferência, bonificação, complementar e ajuste.**

#### Funcionamento dos Filtros

Os filtros do relatório variam conforme o tipo de nota analisada.

- **Notas de Entrada**

O relatório utiliza as informações fiscais da própria nota e considera as notas que tiveram entrada efetiva no sistema.

- **Notas de Saída**

Não existe um campo específico para filtrar diretamente pelo tipo da nota. O mais próximo disso é utilizar filtros relacionados, como:

- **Natureza da operação**
- **Data da venda**
- **Status da nota**

Esses filtros são opcionais e ajudam a refinar a consulta, permitindo resultados mais precisos conforme os critérios selecionados.

#### Quais datas podem ser usadas

No relatório de tributos sobre **notas de saída**, existem **duas datas diferentes** que podem ser usadas como filtro:

- **Data de emissão**: filtra pela data de emissão da nota fiscal
- **Data da venda**: filtra pela data da venda vinculada à nota

Por isso, a mesma nota pode aparecer em resultados diferentes, dependendo do campo de data utilizado no filtro.

Para **notas de entrada**, a consulta considera a base fiscal da nota conforme a entrada efetivada no sistema.

#### Quais status são considerados

No caso das **notas de saída**, quando o filtro de status é preenchido, a busca considera os status da nota fiscal.

Os principais status disponíveis são:

- **Autorizado**
- **A enviar**
- **Cancelado**
- **Denegado**
- **Erro de autorização**
- **Erro de cancelamento**
- **Processando autorização**
- **Processando cancelamento**

Se o usuário não preencher o campo de status, o relatório poderá retornar todas as notas que atendam aos demais critérios definidos na consulta.

#### ⚠️ Atenção importante sobre os impostos

No caso das notas de saída, os impostos são calculados somente quando o status da SEFAZ for **“Autorizado”**.

Isso significa que:

- Notas com status **Autorizado** apresentam os valores tributários normalmente
- Notas com qualquer outro status podem até aparecer no relatório, mas os impostos ficam zerados.

#### O que o relatório apresenta

Esse relatório pode exibir informações como:

- **ICMS**
- **ICMS DIFAL**
- **PIS**
- **COFINS**
- **ICMS ST**
- **PIS ST**
- **COFINS ST**
- **IPI**
- **Totais fiscais da nota**

Esses dados permitem uma visão consolidada da carga tributária das notas, desde que estejam devidamente autorizadas.

#### Quando Utilizar este Relatório

É a ferramenta correta para a equipe **fiscal e contábil**. Use-o para:

- Conferir os impostos calculados em notas de saída autorizadas.
- Analisar a carga tributária de um período.
- Gerar dados de apoio para obrigações fiscais e contábeis.

#### Resumo rápido

| Tela | Base dos dados | Data usada nos filtros | Objetivo principal |
| --- | --- | --- | --- |
| **Notas Fiscais** | Notas fiscais criadas no sistema | Data de emissão | Operacional / Fiscal |
| **BI – Visão de Notas Fiscais** | Vendas | Data da venda | Análise / Gestão |
| **Tributos sobre Notas Fiscais** | Notas fiscais com entrada efetiva / notas fiscais vinculadas à venda | Data fiscal da nota | Fiscal / Impostos |
