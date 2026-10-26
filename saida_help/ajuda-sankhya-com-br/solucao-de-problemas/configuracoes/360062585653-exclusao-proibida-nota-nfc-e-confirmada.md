---
id: "360062585653"
titulo: "Exclusão proibida. Nota NFC-e confirmada e marcada como Conting.Off-Line NFC-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360062585653-Exclus%C3%A3o-proibida-Nota-NFC-e-confirmada-e-marcada-como-Conting-Off-Line-NFC-e"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:42Z"
rotulos: ["Fiscal", "NF-e", "SEFAZ", "NFC-e", "não apagar", "CORE_E02690", "#validadoSheyla", "Restrição de Exclusão de NFC-e", "Erro", "Documentos Eletrônicos"]
---

# Exclusão proibida. Nota NFC-e confirmada e marcada como Conting.Off-Line NFC-e

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16302472858647) MENSAGEM**:

[CORE\_E02690] Exclusão proibida. Nota NFC-e confirmada e marcada como Conting.Off-Line NFC-e.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16302479804183) SOLUÇÃO:**

![Imagem 3: Verifique a chave gerada na aba NF-e no rodapé da nota e consulte verificando se de fato a nota não existe na SEFAZ.](https://ajuda.sankhya.com.br/hc/article_attachments/16302479805591) Verifique a chave gerada na aba NF-e no rodapé da nota e consulte verificando se de fato a nota não existe na SEFAZ.

Chave: 31191207602070000169650010000000049006671801 Não consta na SEFAZ.

![Imagem 4: Via DBEXplore realize a consulta: SELECT TPEMISNFE FROM TGFCAB WHERE NUNOTA = XXXX TPEMISNFE - 9 Notas com TPEMISNFE -…](https://ajuda.sankhya.com.br/hc/article_attachments/16302479806871) Via DBEXplore realize a consulta: **SELECT TPEMISNFE FROM TGFCAB WHERE NUNOTA = XXXX TPEMISNFE - 9 Notas com TPEMISNFE - 9** não podem ser excluídas. Então faça o ajuste do campo via banco de dados: altere o campo **TPEMISNFE** para **NULL** ou 0 (zero)

Após procedimento realize a exclusão da nota.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16302479808535) CAUSA:**

Mensagem ocorre porque o campo TPEMISNFE foi atualizado com 9 e apenas notas com o campo TPEMISNFE igual a NULL ou zero (0) podem ser excluídas.
