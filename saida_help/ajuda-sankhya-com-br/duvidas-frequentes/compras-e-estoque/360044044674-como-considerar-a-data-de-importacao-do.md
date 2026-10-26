---
id: "360044044674"
titulo: "Como considerar a data de importaçao do XML através da rotina Portal de Importação de XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044044674-Como-considerar-a-data-de-importa%C3%A7ao-do-XML-atrav%C3%A9s-da-rotina-Portal-de-Importa%C3%A7%C3%A3o-de-XML"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:55:24Z"
rotulos: ["#criadoRoger", "Configuração", "NF-e", "XML", "Importação", "Dados de importação do XML", "Parâmetro DHSAIENTIMPXML", "Documentos Eletrônicos"]
---

# Como considerar a data de importaçao do XML através da rotina Portal de Importação de XML

**(1)** Parâmetro : **"DHSAIENTIMPXML - Usa dhSaiEnt na import. do XML do portal de imp.?"**

![Imagem 1: (1) Parâmetro : "DHSAIENTIMPXML - Usa dhSaiEnt na import. do XML do portal de imp.?"](https://ajuda.sankhya.com.br/hc/article_attachments/13460616760727)

Este parâmetro por padrão é apresentado ativado. Quando desabilitado, serão desconsiderados os valores das tag's <dhSaiEnt>, e a data e hora atual serão preenchidos com os campos **"Dt. Entrada/Saída"** e **"Hr. Entrada/Saída"**, respectivamente. Assim como será desconsiderado o valor da tag <dhEmiss> e o campo **"Dt. Importação"** será preenchido com a data atual.

O parâmetro **DHSAIENTIMPXML**, no contexto da importação de XML, atualmente só é aplicável a NF-e.
