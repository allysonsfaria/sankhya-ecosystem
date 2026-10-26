---
id: "37097298536343"
titulo: "1160 Rejeição: Ano e mês referência do período de apuração superior ao ano e mês atual [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097298536343-1160-Rejei%C3%A7%C3%A3o-Ano-e-m%C3%AAs-refer%C3%AAncia-do-per%C3%ADodo-de-apura%C3%A7%C3%A3o-superior-ao-ano-e-m%C3%AAs-atual-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-24T12:43:33Z"
rotulos: ["NF-e", "SEFAZ", "Crédito", "Passos para resolver", "Regra de validação", "Erro", "Como Resolver", "IBS", "Reforma Tributária", "Período de apuração", "Crédito presumido do IBS", "Período de apuração superior ao ano e mês atual", "Ano/Mês referência do período de apuração", "IBS na Zona Franca de Manaus (ZFM)", "Documentos Eletrônicos"]
---

# 1160 Rejeição: Ano e mês referência do período de apuração superior ao ano e mês atual [nItem: 999]

**MENSAGEM**

1160 Rejeição: Ano e mês referência do período de apuração superior ao ano e mês atual [nItem: 999]

**SITUAÇÃO**

Ao emitir uma nota fiscal com informações sobre crédito presumido do IBS na Zona Franca de Manaus (ZFM), o sistema está rejeitando a nota porque o ano e mês de referência do período de apuração informado no campo **"Ano/Mês referência do período de apuração"** (competApur) é superior ao ano e mês atual.

**SOLUÇÃO**

**(1)** Acesse a nota fiscal que está sendo rejeitada e verifique os dados do grupo de **Crédito Presumido do IBS na ZFM** (gCredPresIBSZFM).

**(2)** Localize o campo **"Ano/Mês referência do período de apuração"** (competApur) e corrija o valor informado para que seja igual ou inferior ao mês e ano atual.

**(3)** Certifique-se de que o formato da data esteja correto, seguindo o padrão **AAAAMM** (ano com 4 dígitos seguido do mês com 2 dígitos).

**(4)** Após a correção, tente emitir a nota fiscal novamente. 

**CAUSA**

Esta rejeição ocorre quando, ao informar o grupo de crédito presumido do IBS na Zona Franca de Manaus (gCredPresIBSZFM), o campo **"Ano/Mês referência do período de apuração"** (competApur) contém uma data futura, ou seja, superior ao mês e ano atual. A validação da Sefaz verifica se o ano e mês informados no campo competApur são iguais ou anteriores ao ano e mês atual da emissão do documento fiscal.

Quando o sistema identifica uma data futura neste campo, a nota é rejeitada com o código 1160. Esta validação está relacionada às regras de apuração de créditos presumidos do IBS na Zona Franca de Manaus, conforme estabelecido na Lei Complementar 214/2025, que implementa a Reforma Tributária.
