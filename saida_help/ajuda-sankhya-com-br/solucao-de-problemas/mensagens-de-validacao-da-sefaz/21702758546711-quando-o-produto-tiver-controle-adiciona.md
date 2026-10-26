---
id: "21702758546711"
titulo: "Quando o produto tiver controle adicional por numero do lote e opção tem rasto do lote marcado, o campo unidade do lote e obrigatório"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21702758546711-Quando-o-produto-tiver-controle-adicional-por-numero-do-lote-e-op%C3%A7%C3%A3o-tem-rasto-do-lote-marcado-o-campo-unidade-do-lote-e-obrigat%C3%B3rio"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:49:53Z"
rotulos: ["Produtos", "Configuração", "Estoque", "CORE_E07619", "Erro", "Parametrização"]
---

# Quando o produto tiver controle adicional por numero do lote e opção tem rasto do lote marcado, o campo unidade do lote e obrigatório

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/21702743633815) **MENSAGEM:**

[CORE\_E07619] Quando o produto tiver controle adicional por numero do lote e opção tem rasto do lote marcado, o campo unidade do lote e obrigatório.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/21702743637143)CAUSA:**

Acontece quando o parâmetro **"Usar unidade do lote para conversão do qLote - USARUNIDLOTE"** está ligado.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21702758544279)SOLUÇÃO:**

Existe um parâmetro que habilita esse campo o nome dele é **"Usar unidade do lote para conversão do qLote - USARUNIDLOTE"**, foi feito a correção do fato desse parâmetro estar sendo aplicado de forma indevida na tela em FLEX, ele atua somente em HTML5. Desligando, será possível continuar com o processo.
