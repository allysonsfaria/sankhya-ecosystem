---
id: "23337241151511"
titulo: "Produto contado não consta na nota/pedido. Verifique o lote/controle"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/23337241151511-Produto-contado-n%C3%A3o-consta-na-nota-pedido-Verifique-o-lote-controle"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:48:25Z"
rotulos: ["Produtos", "Configuração", "WMS", "Lote", "Nota Fiscal", "Estoque", "Produto não consta na nota/pedido", "Lote não cadastrado; duplicidade de código de barras", "Ativar 'Utiliza explosão de lote'; evitar códigos duplicados"]
---

# Produto contado não consta na nota/pedido. Verifique o lote/controle

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/23337241141015) **MENSAGEM:**

Produto contado não consta na nota/pedido. Verifique o lote/controle.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/23337241148311)CAUSA:**

**1. Causa:** Validar se o lote informado é o mesmo cadastrado na nota de entrada, caso o lote seja informado durante o processo de conferencia para que ocorra a explosão na nota, é necessario configurar todas as empresas controlada pelo WMS com a opção 'Utiliza explosão de lote no Recebimento'. O coletor ainda não valida apenas a empresa indicada na nota de compra, mas sim todas as empresas cadastradas que utilizam e controlam o WMS.

**2. Causa:** A duplicidade na utilização do mesmo código de barras em produtos diferentes, causa inconsistencia na busca da informação correta do produto informado na nota.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/23337241147287)SOLUÇÃO:**

Confira se todas as empresas que são controladas pelo WMS possuem a opção 'Utiliza explosão de lote no recebimento' selecionada na aba WMS da tela Preferências da **Empresa**.

Verifique se o código de barras utilizado para a conferência do produto não está sendo empregado em outro produto, evitando assim duplicidades de cadastro quando o parametro **VALCODBARREPET** -Validar códigos de barra repetido? esta desligado.
