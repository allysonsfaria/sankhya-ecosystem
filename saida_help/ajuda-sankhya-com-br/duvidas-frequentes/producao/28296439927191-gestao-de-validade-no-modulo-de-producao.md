---
id: "28296439927191"
titulo: "Gestão de Validade no Módulo de Produção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28296439927191-Gest%C3%A3o-de-Validade-no-M%C3%B3dulo-de-Produ%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-07-22T14:37:59Z"
rotulos: ["Configuração", "Estoque", "Produção", "Gestão de Validade no Módulo de Produção", "Seleção de insumos por validade", "Prioridade no uso de produtos", "FEFO", "First Expired First Out", "Squad WMS", "Qualidade"]
---

# Gestão de Validade no Módulo de Produção

A gestão eficiente da validade dos insumos é essencial para garantir a qualidade e segurança dos produtos finais.

No módulo de Produção, esse controle foi aprimorado por meio da adoção do método **FEFO (First Expired, First Out — Primeiro a Vencer, Primeiro a Sair)**, garantindo que os materiais com menor prazo de validade disponível sejam consumidos antes dos demais.

#### Como funciona?

##### O processo FEFO prioriza a utilização de insumos com menor prazo de validade, garantindo um rodízio mais eficiente e reduzindo desperdícios. No módulo de produção, aplicam-se as seguintes regras:

**Seleção de insumos por validade**

- Somente produtos cuja validade ainda seja válida até um dia antes do vencimento serão considerados aptos para uso na produção.
- Caso um insumo atinja a data de vencimento no próprio dia previsto para o consumo, ele será automaticamente desconsiderado, pois o sistema o interpreta como vencido.
- Em caso de explosão de lotes onde com datas de validade é iguais, o sistema selecionará os lotes de forma aleatória.

**Prioridade no uso de produtos próximos ao vencimento:**

- Os insumos são organizados para que aqueles com menor prazo de validade sejam utilizados primeiro, respeitando o método FEFO e otimizando o aproveitamento dos estoque, considerando o local de baixa configurado no processo.

#### Benefícios do processo FEFO na produção

**Redução de desperdícios**

- O uso dos insumos antes do vencimento minimiza perdas e melhora o aproveitamento do estoque.

**Garantia de qualidade**

- Produtos vencidos são automaticamente desconsiderados no processo produtivo, assegurando padrões de qualidade e segurança.

**IMPORTANTE:** O módulo de produção **não trabalha com o FIFO** (“First In, First Out” - O primeiro a entrar é o primeiro a sair). O sistema atende nativamente apenas FEFO, priorizando sempre que os produtos com menor prazo de validade.
