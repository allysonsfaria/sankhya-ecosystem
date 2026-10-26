---
id: "37096365296151"
titulo: "1061 Rejeição: CST do IBS/CBS informado obriga informação de diferimento da CBS [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096365296151-1061-Rejei%C3%A7%C3%A3o-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-da-CBS-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-08-21T15:26:21Z"
rotulos: ["NF-e", "SEFAZ", "Impostos", "Tributação", "CST (Código de Situação Tributária)", "Artigo atualizado KCS", "CST do IBS/CBS", "Alíquotas de CBS", "Alíquotas de IBS", "Redução e Diferimentos", "Informação de diferimento da CBS", "Fiscal/Contábil - KCS"]
---

# 1061 Rejeição: CST do IBS/CBS informado obriga informação de diferimento da CBS [nItem: 999]

**MENSAGEM**

1061 Rejeição: CST do IBS/CBS informado obriga informação de diferimento da CBS [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e, o documento foi rejeitado pela SEFAZ porque o CST (Código de Situação Tributária) do IBS/CBS utilizado exige a informação do grupo de diferimento da CBS, porém este grupo não foi informado no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique o CST configurado para a operação que está gerando a rejeição.

**(2)** Na aba **''Identificação''**, verifique se o CST utilizado possui indicador que exige o uso diferimento (ind\_gDif = 1). Neste caso, é obrigatório informar o grupo de diferimento da CBS.

**(3)** Na aba **''Tributação''**, na seção ''**Redução e Diferimentos''**.

**(4)** Preencha os campos obrigatórios do grupo de diferimento:

- Percentual de diferimento (pDif)
- Valor do diferimento (vDif)

**(5)** Salve as alterações e tente emitir o documento fiscal novamente.

**CAUSA**

A rejeição ocorre porque, de acordo com a regra de validação UB59-10 da SEFAZ, quando o CST do IBS/CBS utilizado possui o indicador que exige o uso de diferimento (ind\_gDif = 1), é **obrigatório** informar o grupo de diferimento da CBS (grupo: gCBS/gDif) no documento fiscal.

O diferimento é um mecanismo de postergação do pagamento do tributo, transferindo a responsabilidade para uma etapa posterior da cadeia. Quando um CST específico exige o uso de diferimento, todos os campos relacionados a este mecanismo devem ser corretamente preenchidos para que o documento fiscal seja aceito pela SEFAZ.

Cada CST possui indicadores específicos que determinam quais grupos de informações são obrigatórios ou não permitidos.No caso desta rejeição, o CST utilizado possui o indicador ind\_gDif = 1, tornando obrigatória a informação do grupo de diferimento da CBS.
