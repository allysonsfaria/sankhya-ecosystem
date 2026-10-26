---
id: "32379955890711"
titulo: "Cálculo das Comissões"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32379955890711-C%C3%A1lculo-das-Comiss%C3%B5es"
trilha: "Assistente de Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:31:33Z"
rotulos: ["Configuração", "Vendedor", "TOP", "Financeiro", "Comissões"]
---

# Cálculo das Comissões

### Descrição

A funcionalidade **Cálculo das Comissões** permite configurar as regras de comissionamento e liberar os acessos necessários para que usuários específicos realizem o cálculo e o fechamento das comissões de forma automatizada.

Permite também:

- Definir os responsáveis pelo cálculo de comissões.
- Selecionar os Tipos de Operação elegíveis para comissionamento.
- Escolher o tipo de cálculo aplicável à empresa.
- Informar percentuais por vendedor/gerente.
- Informar percentuais por produto, se necessário.
- Aplicar fórmulas e atualizar os cadastros conforme os critérios definidos.

### Como instalar

1. Selecione os **usuários** ou grupos responsáveis pelo cálculo e fechamento de comissões.
2. Escolha os **Tipos de Operação (TOPs)** de Venda e Devolução de Venda que são elegíveis para o pagamento de comissões.
3. Selecione o **tipo de cálculo** de comissão:

      3.1 Calcular (Padrão): o cálculo será feito posteriormente via rotina de fórmula.

      3.2 Calcular Vendedor da Nota na Confirmação.

      3.3 Calcular Vendedor do Parceiro na Confirmação.

      4. Defina os percentuais de comissão por vendedor/gerente e o tipo de pagamento (data de negociação ou baixa).

      5. Informe percentuais específicos por produto, se necessário, sendo que os percentuais inseridos terão prioridade sobre os percentuais por vendedor.

      6. Revise as configurações realizadas e clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos liberados**

- **Rotinas de Comissões**

      - Caminho: Avançado » Cálculo de Comissão por Fórmula e Financeiro » Fechamento de Comissão.

      - Permissões: Consultar, Incluir, Alterar.

      - Acesso concedido a todos os usuários e grupos definidos na Etapa 1.

**Tabelas Atualizadas**

**TGFTOP – Tipos de Operação**

- Atualização do campo Comissão (ATUALCOM) para todas as TOPs selecionadas, conforme tipo de cálculo definido na Etapa 3.

**TGFFOC – Fórmulas de Comissão**

Criação ou reutilização de fórmulas padrão:

- Fórmula 1 – Vendedor: LIQ \\* (IF(queProd.COMVEND = 0, queVend.COMVENDA, queProd.COMVEND) / 100) \\* IF(queCab.TIPMOV = 'D', -1, 1).
- Fórmula 2 – Gerente: LIQ \\* (IF(queProd.COMGER = 0, queVend.COMGER, queProd.COMGER) / 100) \\* IF(queCab.TIPMOV = 'D', -1, 1).

**TGFVEN – Vendedores/Compradores**

- Atualização dos percentuais de comissão informados por tipo de colaborador e tipo de pagamento definido.
- Associação das fórmulas padrão criadas para cada tipo (Vendedor/Gerente).

**TGFPRO – Produtos**

- Atualização dos produtos com os percentuais de comissão inseridos na Etapa 5:

      - COMVENDA (Comissão do vendedor).

      - COMGER (Comissão do gerente).
