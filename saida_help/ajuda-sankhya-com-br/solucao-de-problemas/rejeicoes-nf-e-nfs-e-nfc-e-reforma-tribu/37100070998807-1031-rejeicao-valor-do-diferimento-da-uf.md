---
id: "37100070998807"
titulo: "1031 Rejeição: Valor do Diferimento da UF difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37100070998807-1031-Rejei%C3%A7%C3%A3o-Valor-do-Diferimento-da-UF-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:44Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Reforma Tributária", "IBS-UF", "Assistente de Configuração da Tributação integral IBS e CBS", "CST do IBS/CBS", "NT 2020.005", "Alíquotas IBS e CBS", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# 1031 Rejeição: Valor do Diferimento da UF difere do calculado [nItem: 999]

**MENSAGEM**

1031 Rejeição: Valor do Diferimento da UF difere do calculado [nItem: 999]

**SITUAÇÃO:**

A rejeição ocorre quando o valor do diferimento estadual (IBS-UF) informado na nota fiscal eletrônica não corresponde ao valor calculado pela SEFAZ. O sistema compara o valor informado com o valor calculado automaticamente para validar a nota.

**SOLUÇÃO:**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Aliquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Verifique se o CST selecionado possui o indicador que exige o uso de diferimento (ind\_gDif = 1).

**(3)** Confira se o grupo de diferimento (gIBSUF/gDif) está corretamente informado na nota fiscal.

- Este grupo é **obrigatório** quando o CST utilizado exige o uso de diferimento.

**(4)** Certifique-se se os valores utilizados para o cálculo do diferimento estão corretos:

- Base de cálculo (vBC)
- Percentual do IBS da UF (pIBSUF)
- Percentual do diferimento (pDif)

**(5)** Acesse a tela [**''Assistente de Configuração Integral da Reforma Tributária''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria) (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(6)** Verifique e ajuste as configurações de diferimento do IBS Estadual.

**(7)** Após realizar as alterações, redigite o item na nota fiscal para que o sistema recalcule o valor do diferimento conforme a fórmula:

```
vDif = vBC x (pIBSUF / 100) x (pDif / 100).
```

**CAUSA:**

A rejeição 1031 ocorre quando o valor do diferimento da UF (vDif) informado no documento fiscal **não corresponde ao valor calculado pela Sefaz**.

Conforme a regra de validação **UB23-10 estabelecida na Lei Complementar 214/2025**, **o valor do diferimento deve ser resultante da multiplicação da Base de Cálculo pelo Percentual do IBS da UF e pelo Percentual do Diferimento**, seguindo a fórmula: vDif = vBC x (pIBSUF / 100) x (pDif / 100).

Esta validação é aplicada quando o **CST do IBS/CBS** informado possui indicador que exige o uso de diferimento (ind\_gDif = 1) e o grupo de diferimento (gIBSUF/gDif) está informado na nota fiscal.

Qualquer divergência entre o valor informado e o calculado resultará na rejeição do documento fiscal.
