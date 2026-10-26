---
id: "32484233898519"
titulo: "Faturamento de Pedidos de Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32484233898519-Faturamento-de-Pedidos-de-Venda"
trilha: "Assistente de Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:31:04Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "TOP", "Vendas"]
---

# Faturamento de Pedidos de Venda

### Descrição

A funcionalidade **Faturamento de Pedidos de Venda** permite configurar as regras e liberar os acessos necessários para o processo de faturamento, garantindo a execução eficiente das operações de venda e controle de notas fiscais.

Ela oferece os seguintes recursos:

- **Portal de Vendas – Opção Pedidos:** Permite consultar, incluir, alterar, alterar a ligação entre documentos, realizar rateios, e imprimir ou reimprimir pedidos de venda.
- **Portal de Vendas – Opção Notas:** Permite consultar, incluir, alterar, alterar a ligação entre documentos, realizar rateios, e imprimir ou reimprimir notas fiscais.
- **Configuração de Tipos de Operação e Controle de Numeração:** Permite configurar e ajustar os tipos de operação para faturamento de pedidos de venda, bem como controlar a numeração de documentos.
- **Parâmetros de Faturamento:** Permite habilitar um tipo de operação específico para faturamento, configurar o controle de numeração de notas fiscais, e garantir que os usuários selecionados tenham os acessos necessários.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os grupos e/ou usuários responsáveis pelo faturamento de pedidos de venda.
3. Clique em **"Avançar"**.
4. Revise o resumo com os grupos e usuários selecionados.
5. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos liberados**

- **Portal de Vendas**
  Permissões: Consultar, Incluir, Alterar.
- **Portal de Vendas – Pedidos**
  Permissões: Consultar, Incluir, Alterar, Altera ligação entre documentos, Rateio, Imprimir/Reimprimir.
- **Portal de Vendas – Notas**
  Permissões: Consultar, Incluir, Alterar, Altera ligação entre documentos, Rateio, Imprimir/Reimprimir.

**Tabelas atualizadas**

- **TGFTOP – Tipos de Operação**
  - Inclusão/Ativação da TOP **"1101 – Venda NF-e"**.
  - Atualização da TOP **"1001 (Pedido de Venda)"** com destino padrão para a TOP 1101.
- **TGFNUM – Numeração**
  - Criação da base de numeração **"VENDA"** com série 1 para todas as empresas ativas.
  - Definição da numeração como automática para o modelo de documento fiscal 55.
