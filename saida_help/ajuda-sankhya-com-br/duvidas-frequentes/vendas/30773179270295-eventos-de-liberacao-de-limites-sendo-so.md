---
id: "30773179270295"
titulo: "Eventos de liberação de limites sendo solicitadas no PEDIDO e na NOTA, como evitar?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30773179270295-Eventos-de-libera%C3%A7%C3%A3o-de-limites-sendo-solicitadas-no-PEDIDO-e-na-NOTA-como-evitar"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:34:44Z"
rotulos: ["Produtos", "Configuração", "Eventos", "Liberação de Limites", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Eventos de liberação de limites", "sendo solicitadas no PEDIDO e na NOTA"]
---

# Eventos de liberação de limites sendo solicitadas no PEDIDO e na NOTA, como evitar?

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30787905276055) **SITUAÇÃO:**

Ao lançar um pedido de venda pode ser necessário realizar a liberação de eventos relacionados aos itens, para permitir sua confirmação. Esses eventos incluem, por exemplo:

- Evento 25 – Liberação de desconto
- Evento 10 – Verificação de estoque
- Entre outros

Após a confirmação do pedido, ele pode ser faturado sem que seja necessário refazer essas mesmas liberações na nota gerada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30773179237527)SOLUÇÃO:**

Para que o sistema copie as liberações do pedido para a  Nota, é preciso atender a dois requisitos:

![Imagem 3: Na aba "Geral", a opção "Copiar liberações quando faturando individualmente" deve estar marcada na TOP do lançamento;](https://ajuda.sankhya.com.br/hc/article_attachments/30787905277207) Na aba **"Geral",** a opção **"Copiar liberações quando faturando individualmente"** deve estar marcada na **TOP** do lançamento;

![Imagem 4: O parâmetro "Agrupar produtos repetidos em qualquer faturamento?" (AGRUPFATSEMP) deve estar desmarcado. Caso contrário,…](https://ajuda.sankhya.com.br/hc/article_attachments/30787932807959) O parâmetro **"Agrupar produtos repetidos em qualquer faturamento?" (AGRUPFATSEMP)** deve estar desmarcado. Caso contrário, a cópia não será realizada, pois a tabela de itens (TGFITE) poderá sofrer modificações.
