---
id: "33132716523159"
titulo: "Ao faturar pedidos agrupados e imprimir/salvar como PDF não está respeitando a ordem do número único das notas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33132716523159-Ao-faturar-pedidos-agrupados-e-imprimir-salvar-como-PDF-n%C3%A3o-est%C3%A1-respeitando-a-ordem-do-n%C3%BAmero-%C3%BAnico-das-notas"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:29:30Z"
rotulos: ["Impressão", "NF-e", "Portal de Vendas", "XML", "SEFAZ", "DANFE", "Ao faturar pedidos agrupados e imprimir/salvar como PDF", "não está respeitando a ordem do número único das notas", "Faturar Direto", "DBEXPLORER"]
---

# Ao faturar pedidos agrupados e imprimir/salvar como PDF não está respeitando a ordem do número único das notas

Ao selecionar mais de um pedido no **''Portal de Vendas''** (Comercial» Consulta» Portal de Vendas) e selecionar **''Outras opções'' > ''Faturamento'' > ''Faturar Direto (com emissão da nota)''** as notas impressas não seguem a ordem de número único.

![Imagem 1: Ao selecionar mais de um pedido no ''Portal de Vendas'' (Comercial» Consulta» Portal de Vendas) e selecionar ''Outras…](https://ajuda.sankhya.com.br/hc/article_attachments/33259365807127)

A impressão do **DANFE** acontece quando a nota de venda é confirmada pelo Faturar Direto. O PDF gerado não tem uma função de ordenação definida, então o arquivo vai recebendo as impressões conforme as notas são geradas e aprovadas pela Sefaz.

É possível conferir a ordem de aprovação usando o **''DBEXPLORER''** (Configurações» Avançado» DBExplorer) com a consulta abaixo, verificando o campo **"XMLPROTAUTNOT"**:

SELECT NUNOTA, XMLPROTAUTNOT FROM TGFNFE ORDER BY NUNOTA DESC
