---
id: "37228132506647"
titulo: "E0698 Rejeição: Se CST informado for diferente de 0, 8 ou 9, o tipo de retenção para Pis/Cofins deve ser informado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228132506647-E0698-Rejei%C3%A7%C3%A3o-Se-CST-informado-for-diferente-de-0-8-ou-9-o-tipo-de-reten%C3%A7%C3%A3o-para-Pis-Cofins-deve-ser-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:22Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Alíquota de PIS", "Código de Situação Tributária (CST)", "Tipo de Retenção", "tipo de retenção de PIS e COFINS", "PIS/COFINS"]
---

# E0698 Rejeição: Se CST informado for diferente de 0, 8 ou 9, o tipo de retenção para Pis/Cofins deve ser informado.

**MENSAGEM**

E0698 Rejeição: Se CST informado for diferente de 0, 8 ou 9, o tipo de retenção para Pis/Cofins deve ser informado.

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida com um Código de Situação Tributária de PIS/COFINS informado, sem o preenchimento da informação de retenção correspondente a esses tributos no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Alíquota de PIS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS) e localize a alíquota utilizada no lançamento da nota fiscal que está sendo rejeitada.

**(2)** Verifique o campo **''Cód. sit. tributária''** configurado com o código na alíquota. Se o CST for **diferente de 0, 8 ou 9**, será necessário informar o tipo de retenção.

**(3)** Consulte seu **contador ou setor fiscal** para identificar qual é o tipo de retenção correto a ser aplicado para PIS e COFINS, considerando a operação fiscal e a legislação vigente.

**(4)** Na tela **"Alíquota de PIS"**, localize e preencha o campo **"Tipo de Retenção"** com a informação correta fornecida pelo setor fiscal.

**(5)** Repita o mesmo procedimento na tela **"Alíquota de COFINS"** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS), verificando o CST e preenchendo o campo **"Tipo de Retenção"** quando necessário.

**(6)** Salve as alterações realizadas nas alíquotas de PIS e COFINS.

**(7)** Retorne à nota fiscal rejeitada e realize novamente a **emissão do documento eletrônico**.

**CAUSA**

A rejeição ocorre porque a **Sefaz exige que seja informado o tipo de retenção** de PIS e COFINS quando o Código de Situação Tributária (CST) configurado na alíquota for diferente de 0 (Operação Tributável com Alíquota Básica), 8 (Operação sem Incidência da Contribuição) ou 9 (Operação com Suspensão da Contribuição).

Quando o campo **"Tipo de Retenção"** não é preenchido no cadastro das alíquotas de PIS e COFINS, o sistema não consegue enviar as informações fiscais completas para a Sefaz, resultando na rejeição do documento eletrônico.
