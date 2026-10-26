---
id: "37222431333271"
titulo: "E0160 Rejeição: No mês de competência da NFS-e, a opção de situação perante o Simples Nacional, do prestador, informada na DPS não está de acordo com o cadastro Simples Nacional."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222431333271-E0160-Rejei%C3%A7%C3%A3o-No-m%C3%AAs-de-compet%C3%AAncia-da-NFS-e-a-op%C3%A7%C3%A3o-de-situa%C3%A7%C3%A3o-perante-o-Simples-Nacional-do-prestador-informada-na-DPS-n%C3%A3o-est%C3%A1-de-acordo-com-o-cadastro-Simples-Nacional"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:49Z"
rotulos: ["Configuração", "Receita Federal", "Simples Nacional", "SEFAZ", "Impostos", "NFS-e", "NFS-e Padrão Nacional", "Empresa foi enquadrada no Simples Nacional", "Regime tributário da empresa", "Empresa foi desenquadrada do Simples Nacional", "Portal do Simples Nacional", "Ativa como optante pelo Simples Nacional", "Situação da empresa perante o Simples Nacional"]
---

# E0160 Rejeição: No mês de competência da NFS-e, a opção de situação perante o Simples Nacional, do prestador, informada na DPS não está de acordo com o cadastro Simples Nacional.

**MENSAGEM**

E0160 Rejeição: No mês de competência da NFS-e, a opção de situação perante o Simples Nacional, do prestador, informada na DPS não está de acordo com o cadastro Simples Nacional.

**SITUAÇÃO**

Ao emitir uma **NFS-e Padrão Nacional**, o sistema apresenta a rejeição acima indicando que a **situação da empresa perante o Simples Nacional** informada no documento fiscal **não corresponde ao cadastro oficial** do Simples Nacional para o mês de competência da nota.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Verifique a situação atual da empresa no **Portal do Simples Nacional** da Receita Federal para confirmar se a empresa está **ativa como optante pelo Simples Nacional** no mês de competência da NFS-e que está sendo emitida.

**(2)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o cadastro da empresa emissora da NFS-e.

**(3)** Na aba **“Naturezas”**, revise as configurações tributárias da empresa:

- Verifique se a opção **“Optante pelo SIMPLES”** está **marcada**, caso a empresa seja optante pelo **Simples Nacional**;
- No campo **“Cód. Regime Tribut.”**, selecione **“Simples Nacional”** ou **“Simples Nacional – Sublimite”**, conforme o enquadramento vigente da empresa;
- No campo **“Tipo de Partilha / Anexo SN”**, escolha o **anexo correspondente à atividade exercida** pela empresa (por exemplo: Anexo I – Comércio).

**(4)** Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).

**(5)** Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"** sub-aba **"Geral"**.

**(6)** No campo **“Regime de Apuração dos Tributos do Simples Nacional”**, selecione a opção adequada, de acordo com a forma de apuração adotada pela empresa.

**(7)** Caso a empresa **não seja mais optante pelo Simples Nacional**:

- Desmarque a opção **“Optante pelo SIMPLES”** na aba **“Naturezas”** conforme o passo 1 e 2;
- Ajuste o campo **“Cód. Regime Tribut.”** para **“Regime Normal”**.

**(8)** Após realizar todos os ajustes, **gere novamente a NFS-e** e verifique se a rejeição foi solucionada.

**CAUSA**

A rejeição ocorre quando as **informações sobre o regime tributário da empresa** cadastradas no sistema Sankhya **não correspondem aos dados oficiais** registrados no Portal do Simples Nacional da Receita Federal para o mês de competência da NFS-e. Isso pode acontecer quando a empresa foi **desenquadrada do Simples Nacional** e o cadastro no sistema não foi atualizado, ou quando a empresa foi **enquadrada no Simples Nacional** e as configurações no sistema não refletem essa mudança.
