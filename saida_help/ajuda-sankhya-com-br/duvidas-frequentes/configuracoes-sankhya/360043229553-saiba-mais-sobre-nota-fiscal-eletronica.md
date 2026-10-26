---
id: "360043229553"
titulo: "Saiba mais sobre nota fiscal eletrônica denegada "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043229553-Saiba-mais-sobre-nota-fiscal-eletr%C3%B4nica-denegada"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T16:06:15Z"
rotulos: ["ERRONF", "DUVIDANF", "#PUBLIFER", "Fiscal", "NF-e", "SEFAZ", "Entendendo Nota Fiscal Eletrônica Denegada", "Erro", "Documentos Eletrônicos", "DENEGADA"]
---

# Saiba mais sobre nota fiscal eletrônica denegada 

Esse documento tem por objetivo detalhar a causa/tratativa de Nota Fiscal Eletrônica com o Status NF-e=DENEGADA (STATUSNFE = D).

- Ocorre quando o emissor, e em alguns casos o destinatário também, apresentam pendências fiscais. Neste caso o faturamento estará impedido até que a regularização dessa situação fiscal ocorra.

![Imagem 1: Ao receber o resultado do processamento de uma NF-e, a nota pode ter sido DENEGADA. Neste caso, o status NF-e da nota é…](https://ajuda.sankhya.com.br/hc/article_attachments/16089577192855) Ao receber o resultado do processamento de uma NF-e, a nota pode ter sido DENEGADA. Neste caso, o status NF-e da nota é atualizado para DENEGADA.

- A NF-e já encontra-se com o **Status NF-e DENEGADA**?

No cenário acima **não existem ajustes** a serem realizados com essa NF-e no sistema, entenda os detalhes:

- NF-e com status 'DENEGADA' não pode ser excluída e/ou cancelada, seu registro deve ser mantido dessa forma em seu sistema.
- Caso a regularização fiscal aconteça, uma nova NF-e deve ser emitida.
- Os itens da nota passam a não atualizar estoque e os financeiros relacionados à nota são removidos.

![Imagem 2: Para situações onde a respectiva nota fiscal eletrônica encontra-se 'Denegada' na SEFAZ e esse status NÃO foi…](https://ajuda.sankhya.com.br/hc/article_attachments/16089577198615) Para situações onde a respectiva nota fiscal eletrônica encontra-se 'Denegada' na SEFAZ e esse **status NÃO foi atualizado no sistema:**

- Caso a respectiva NF-e esteja DENEGADA nos ambientes Nacional/Estadual da Sefaz, selecione a nota no respectivo portal, no botão NF-e selecione a opção **"Consulta situação atual da nota"**;
- Será exibida uma caixa de diálogo, informando que a situação da nota no sistema está diferente da situação atual da SEFAZ, clique em sim e confira a mudança do Status NF-e atual para DENEGADA.

![Imagem 3: Será exibida uma caixa de diálogo, informando que a situação da nota no sistema está diferente da situação atual da…](https://ajuda.sankhya.com.br/hc/article_attachments/14494933600919)

Caso sejam retornados erros nessa atualização de status, busque pela mensagem em nossa Central de Ajuda e não localizando acione nosso Service Desk Especializado.

(1)** PARÂMETROS:**

- Através do parâmetro **"DENEGDEIXAPEND - Nota Denegada deixa pedido pendente?"** poderá definir se o pedido que originou a NF-e DENEGADA ficará ou não pendente para um novo faturamento.
