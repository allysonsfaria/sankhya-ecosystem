---
id: "32476617768727"
titulo: "Controles Adicionais de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32476617768727-Controles-Adicionais-de-Estoque"
trilha: "Assistente de Melhores Práticas > Estocagem"
atualizado_em: "2026-07-22T14:31:07Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Lote", "Estoque", "Validade", "Número de Série"]
---

# Controles Adicionais de Estoque

### Descrição

A funcionalidade **Controles Adicionais de Estoque** permite configurar e gerenciar variações de produtos no estoque por critérios como cor, tamanho, número de lote, número de série, validade e data de fabricação. Essa flexibilidade garante maior precisão no controle e rastreabilidade dos itens.

Ela oferece os seguintes recursos:

- **Definição de controles adicionais por produto:** Permite configurar, individualmente ou em massa, qual tipo de controle adicional será aplicado a cada item do portfólio.
- **Controles disponíveis:** Controle por Lote (com opção de validade e fabricação), Número de Série, Lista, Livre, Parceiro e Validade.
- **Atualização em Massa:** Permite aplicar rapidamente definições de controle para múltiplos produtos ativos sem estoque.
- **Configuração de Parâmetros:** Os parâmetros do sistema são atualizados automaticamente conforme as preferências escolhidas, refletindo o uso de controle adicional.
- **Rastreabilidade e Gestão Eficiente:** Ideal para segmentos que exigem controle por validade, lote ou personalizações de produtos.

### Como instalar

1. Clique em **"Iniciar"**.
2. Na primeira etapa, indique se deseja utilizar o controle adicional de estoque.
3. Caso tenha escolhido **"Sim"**, defina o tipo de controle adicional para os produtos ativos sem estoque, usando os filtros e botões disponíveis na tela.
4. Clique em **"Avançar"** para revisar o resumo com as informações configuradas.
5. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Tabelas atualizadas**

**TSIPAR – Parâmetros do Sistema**
Atualização automática dos seguintes parâmetros, conforme as escolhas realizadas:

- **UTILIZACONTROLE:** Define se o controle adicional de estoque está ativado.
- **LOTEDTVAL:** Ativa uso de data de validade nos controles por lote.
- **LOTEDTFAB:** Ativa uso de data de fabricação nos controles por lote.
- **LOTEDTVALFABPRO:** Ativa uso misto de produtos com e sem validade/fabricação dentro dos controlados por lote.

**TGFPRO – Produtos**
Atualização de todos os campos necessários no cadastro de produtos:

- **TIPCONTEST:** Define o tipo de controle adicional por produto (Lote, Série, Lista, Livre, Parceiro, Validade).
- **TITCONTEST:** Título do controle (para tipos Livre ou Lista).
- **LISCONTEST:** Opções da lista (para tipo Lista, formatadas com quebra de linha).
- **USALOTEDTVAL:** Indica se o controle por lote utiliza data de validade.
- **USALOTEDTFAB:** Indica se o controle por lote utiliza data de fabricação.
