---
id: "37230545518743"
titulo: "E0712 Rejeição: Para ME/EPP indTotTrib nunca poderá ser informado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37230545518743-E0712-Rejei%C3%A7%C3%A3o-Para-ME-EPP-indTotTrib-nunca-poder%C3%A1-ser-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:44Z"
rotulos: ["Configuração", "NF-e", "Simples Nacional", "XML", "SEFAZ", "ME/EPP", "Empresa de Pequeno Porte (EPP)", "ME/EPP indTotTrib", "Indicador de Totalização de Tributos", "indTotTrib"]
---

# E0712 Rejeição: Para ME/EPP indTotTrib nunca poderá ser informado.

**MENSAGEM**

E0712 Rejeição: Para ME/EPP indTotTrib nunca poderá ser informado.

**SITUAÇÃO**

Ao emitir uma **NF-e ou NFC-e**, a nota foi **rejeitada pela Sefaz** com a mensagem informando que o campo **"Indicador de Totalização de Tributos" (indTotTrib)** não pode ser preenchido quando a empresa emitente é optante pelo **Simples Nacional** e enquadrada como **Microempresa (ME)** ou **Empresa de Pequeno Porte (EPP)**.

**SOLUÇÃO**

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o **cadastro da empresa emitente** da nota fiscal rejeitada.

**(2)** Na aba **''Naturezas''**, verifique o campo **''Cód. Regime Tribut''** e confirme se a empresa está configurada como optante pelo **''Simples Nacional''**.

**(3)** Caso a empresa não seja optante pelo ''Simples Nacional'', ajuste o campo **"Cód. Regime Tributário"** para o regime correto (Lucro Real, Lucro Presumido ou outro aplicável).

**(4)** Se a empresa **realmente for optante pelo Simples Nacional**, verifique se existe alguma **configuração ou customização** que esteja forçando o preenchimento do campo **"Indicador de Totalização de Tributos" (indTotTrib)** no XML da nota fiscal.

**(5)** Remova qualquer **preenchimento manual ou automático** do campo **indTotTrib** nas configurações de emissão de documentos fiscais.

**(6)** Após realizar os ajustes necessários, **reemita a nota fiscal** e verifique se a rejeição foi solucionada.

**CAUSA**

A rejeição ocorre porque, de acordo com a **legislação tributária** e as **regras de validação da Sefaz**, empresas optantes pelo **Simples Nacional** enquadradas como **ME ou EPP** não devem informar o campo **"Indicador de Totalização de Tributos" (indTotTrib)** no XML da NF-e ou NFC-e.

Este campo é aplicável apenas para empresas que **não são optantes pelo Simples Nacional** e que estão sujeitas à **Reforma Tributária** com a obrigatoriedade de informar a totalização dos tributos IBS e CBS. Quando o sistema identifica que a empresa emitente é **ME/EPP optante pelo Simples Nacional** e o campo **indTotTrib** está preenchido, a nota é **rejeitada automaticamente** pela Sefaz.
