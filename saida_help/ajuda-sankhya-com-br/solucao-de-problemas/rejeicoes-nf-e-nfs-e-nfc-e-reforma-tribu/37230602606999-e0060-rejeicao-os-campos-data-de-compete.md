---
id: "37230602606999"
titulo: "E0060 Rejeição: Os campos data de competência, subitem da lista nacional de serviços, código complementar municipal e local da prestação não podem ser alterados quando a opção do simples nacional for Não Optante (opSimpNac = 1)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37230602606999-E0060-Rejei%C3%A7%C3%A3o-Os-campos-data-de-compet%C3%AAncia-subitem-da-lista-nacional-de-servi%C3%A7os-c%C3%B3digo-complementar-municipal-e-local-da-presta%C3%A7%C3%A3o-n%C3%A3o-podem-ser-alterados-quando-a-op%C3%A7%C3%A3o-do-simples-nacional-for-N%C3%A3o-Optante-opSimpNac-1"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:43Z"
rotulos: ["Configuração", "Simples Nacional", "SEFAZ", "Impostos", "TOP", "Financeiro", "NFS-e", "Data de competência", "Subitem da Lista Nacional de Serviços", "Código complementar municipal e local", "Não Optante pelo Simples Nacional (Regime Normal)", "Local da Prestação"]
---

# E0060 Rejeição: Os campos data de competência, subitem da lista nacional de serviços, código complementar municipal e local da prestação não podem ser alterados quando a opção do simples nacional for Não Optante (opSimpNac = 1).

**MENSAGEM**

E0060 Rejeição: Os campos data de competência, subitem da lista nacional de serviços, código complementar municipal e local da prestação não podem ser alterados quando a opção do simples nacional for Não Optante (opSimpNac = 1).

**SITUAÇÃO**

A NFS-e foi emitida por empresa configurada como não optante pelo Simples Nacional, com o preenchimento ou alteração de campos relacionados à competência, classificação do serviço ou local da prestação no documento fiscal, resultando na rejeição da nota.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

**(2)** Verifique a aba **"Naturezas"**, no campo **"Cód. Regime Tribut."**, se a empresa está corretamente configurada como **''Não Optante pelo Simples Nacional (Regime Normal)''**.

**(3)** Caso a empresa seja realmente ''Não Optante pelo Simples Nacional'', acesse a tela **"Tipos de Operação - TOP"** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) e verifique a aba **"NFS-e"**:

- Certifique-se de que o campo **"Cód. Natureza Oper. ISS (NFS-e)"** esteja preenchido corretamente com uma das opções permitidas.
- Verifique se os campos relacionados à **Data de Competência**, **Subitem da Lista Nacional de Serviços**, **Código Complementar Municipal** e **Local da Prestação** não estão sendo preenchidos ou alterados indevidamente.

**(3)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço) e verifique a aba **"Impostos"**:

Certifique-se de que o campo **"Código de Serviço Municipal"** esteja preenchido no formato correto esperado pela prefeitura (exemplo: 01.02.01.001).

Verifique se o campo **"Tipo de Serviço"** está corretamente vinculado à Lista de Serviços cadastrada.

**(4)** Caso a empresa seja **Optante pelo Simples Nacional**, ajuste o campo **"Cód. Regime Tribut."** na tela **"Empresas"** para **"Simples Nacional"** ou **"Simples Nacional - Sublimite"**.

**(5)** Após realizar os ajustes necessários, exclua a NFS-e rejeitada, volte a numeração e emita a nota novamente.

**(6)** Valide no XML da NFS-e se as correções foram aplicadas corretamente, verificando as tags relacionadas aos campos mencionados.

**CAUSA**

Esta rejeição ocorre quando a empresa emissora da NFS-e está configurada como **Não Optante pelo Simples Nacional** (opSimpNac = 1) e os campos **"Data de Competência"**, **"Subitem da Lista Nacional de Serviços"**, **"Código Complementar Municipal"** ou **"Local da Prestação"** foram preenchidos ou alterados. A Sefaz valida que, para empresas não optantes pelo Simples Nacional, esses campos específicos não podem ser modificados, pois seguem regras tributárias distintas. A divergência entre a configuração do regime tributário da empresa e o preenchimento desses campos gera a rejeição E0060.
