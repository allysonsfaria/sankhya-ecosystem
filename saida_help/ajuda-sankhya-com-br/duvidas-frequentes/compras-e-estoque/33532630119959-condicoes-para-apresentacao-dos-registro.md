---
id: "33532630119959"
titulo: "Condições para apresentação dos registros referentes a ''Entradas Pendentes'' na ''Consulta de Produtos''."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33532630119959-Condi%C3%A7%C3%B5es-para-apresenta%C3%A7%C3%A3o-dos-registros-referentes-a-Entradas-Pendentes-na-Consulta-de-Produtos"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-08-04T13:31:09Z"
rotulos: ["Produtos", "Configuração", "Consulta de Produtos", "Nota Fiscal", "TOP", "Estoque", "Notas de Compra", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Condições para apresentação dos registros", "referentes a ''Entradas Pendentes'' na ''Consulta de Produtos''.", "Pedidos de Compra"]
---

# Condições para apresentação dos registros referentes a ''Entradas Pendentes'' na ''Consulta de Produtos''.

Por meio da **Consulta de Produtos** é possível identificar quais são os lançamentos de entrada (notas/pedidos) do produto que se encontram pendentes de finalização. Esta informação é importante para apresentar ao usuário uma previsão de chegada do produto e posicionamento junto ao seu cliente, caso seu estoque não atenda à quantidade solicitada.

**SOLUÇÃO:**

Para a apresentação dos lançamentos, o sistema deve seguir a seguinte análise:

**(1)** No que diz respeito aos **Pedidos de Compra**, as condições são as seguintes:

- Estar confirmado;
- Estar pendente (cabeçalho e item);
- Quantidade negociada **superior** à quantidade entregue.

**(1)** Em relação às **Notas de Compra**:

- Não confirmada;
- Com o campo ''ADIAR ESTOQUE NA CONFIRMAÇÃO  = 'S' '' na TOP utilizada para o lançamento.
