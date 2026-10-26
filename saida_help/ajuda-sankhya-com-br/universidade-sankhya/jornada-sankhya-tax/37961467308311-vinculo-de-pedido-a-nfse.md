---
id: "37961467308311"
titulo: "Vínculo de pedido à NFSe"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37961467308311-V%C3%ADnculo-de-pedido-%C3%A0-NFSe"
trilha: "Universidade Sankhya > Jornada Sankhya Tax"
atualizado_em: "2026-07-22T14:03:29Z"
rotulos: ["Configuração", "NFSe", "Contrato", "TOP", "Financeiro"]
---

# Vínculo de pedido à NFSe

## Vínculo de pedido às notas capturadas

#### Qual a importância dessa funcionalidade?

O vínculo do pedido à nota fiscal de serviço capturada é essencial para garantir controle e rastreabilidade nos processos financeiros e fiscais. Essa funcionalidade conecta o que foi contratado no pedido com o serviço efetivamente faturado, assegurando aderência aos valores, impostos e centros de custo definidos previamente. Com isso, a empresa ganha mais segurança na validação das notas, na liberação de pagamentos e no acompanhamento do status das contratações, mantendo a gestão organizada e confiável dentro do ERP Sankhya.

#### Quais problemas essa funcionalidade resolve?

- Evita pagamento de serviços sem pedido previamente aprovado.
- Reduz lançamentos de notas fora do escopo contratado.
- Impede divergências entre valores negociados e valores faturados.
- Simplifica a conferência fiscal e financeira no recebimento da nota.
- Garante rastreabilidade entre contratação, execução e pagamento.
- Diminui retrabalho na conciliação entre pedidos, notas e títulos financeiros.
- Facilita auditorias com histórico claro das operações.
- Fortalece o controle de orçamento e centro de custo.

#### Cenário de aplicação

A Axis LTDA., empresa do segmento atacado distribuidor, contratou um serviço mensal de manutenção preventiva de empilhadeiras utilizadas no centro de distribuição. O pedido de compra foi registrado no sistema com valor negociado de R$ 8.500, centro de resultado “Logística” e orçamento aprovado para o mês. Após a execução do serviço, o prestador emitiu a NFSe, que foi capturada automaticamente pelo ERP Sankhya. Durante a conferência, o analista identificou que a nota foi integrada sem vínculo com o pedido de compra, o que faria o serviço aparecer como despesa sem contrato, comprometendo o controle orçamentário e a análise de custos da operação logística.

**Tarefa:** Assista ao vídeo de demonstração prática para entender como realizar o vínculo do pedido à NFSe capturada. Em seguida, utilize as notas fiscais de serviço já capturadas em sua base, selecione uma NFSe sem vínculo e realize a associação ao pedido de compra correspondente.

#### É o momento de aplicar o conhecimento adquirido! Execute as movimentações no ERP Sankhya

1. Acesse a tela **Tipos de Operação - TOP**
   **Menu:** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Selecione no menu lateral esquerdo da tela, em **Tipos de Movimento**, a opção **Nota de Compra**.
- Selecione com um duplo clique na grade de resultado o tipo de operação utilizado para a nota de compra.

**Aba Geral**

- Selecione a opção Exigir algum item no campo “**Exigir Pedido**”.
- Salve a alteração.

2. Acesse a tela **Sankhya Tax - Captura e Importação de Nfse**
   **Menu:** Snk Tax - Importação NFS-e

- Selecione a nota ser processada com um duplo clique.
- Trate as divergências apontadas.
- Acesse a aba Pedidos. 
  Para que ela seja apresentada é necessário que a TOP configurada seja informada no campo indicado.
- Clique em “**Atualizar** **Pedidos**”.
- Selecione o pedido correspondente e na coluna Vinculados relacione a quantidade desejada no pedido.
- Selecione a flag da linha do pedido vinculado e no painel Itens da nota clique em “**Salvar ligação**”.
- Para que os dados do pedido sejam inseridos na nota capturada, acione o botão “**Copiar Cabeçalho**”.
- Após executar todos os ajustes e vincular o pedido, clique em “**Validar**” na porção superior direita da tela.
