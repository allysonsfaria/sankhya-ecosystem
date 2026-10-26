---
id: "37226316573719"
titulo: "E0550 Rejeição: O código de identificação de Benefício Municipal, informada na DPS, não permite benefício para o código de tributação e/ou prestador (CPF ou CNPJ) informado na DPS, conforme parametrização do município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226316573719-E0550-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-de-Benef%C3%ADcio-Municipal-informada-na-DPS-n%C3%A3o-permite-benef%C3%ADcio-para-o-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-e-ou-prestador-CPF-ou-CNPJ-informado-na-DPS-conforme-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:04Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Código de tributação do ISS", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Incompatibilidade entre o código de benefício municipal", "CPF/CNPJ do prestador", "Código de benefício municipal"]
---

# E0550 Rejeição: O código de identificação de Benefício Municipal, informada na DPS, não permite benefício para o código de tributação e/ou prestador (CPF ou CNPJ) informado na DPS, conforme parametrização do município de incidência do ISSQN.

**MENSAGEM**

E0550 Rejeição: O código de identificação de Benefício Municipal, informada na DPS, não permite benefício para o código de tributação e/ou prestador (CPF ou CNPJ) informado na DPS, conforme parametrização do município de incidência do ISSQN.

**SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviços Eletrônica), o sistema apresenta a mensagem de rejeição informando que o **código de benefício municipal** utilizado não é compatível com o **código de tributação do ISS** ou com o **CPF/CNPJ do prestador** de serviços, conforme as regras estabelecidas pela prefeitura do município de incidência do ISSQN.

**SOLUÇÃO**

Para corrigir esta rejeição, siga o passo a passo abaixo:

**(1)** Verifique se o **código de benefício municipal** informado está correto e vigente junto à prefeitura do município onde o serviço foi prestado. Consulte o **manual da prefeitura** ou entre em contato com a **Secretaria Municipal de Fazenda** para confirmar os códigos válidos.

**(2)** Acesse a tela [**"Empresa"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

**(3)** Na aba **"NFS-e"**, verifique se o campo **"Regime esp. tributação ISS (NFS-e)"** está configurado corretamente conforme o benefício fiscal aplicável à empresa.

**(4)** Acesse a tela [**''Tipo de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(5)** Na aba **''NFS-e''**, verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"**, e valide se o campo está compatível com o código de benefício municipal informado.

**(6)** Confirme se o **CPF ou CNPJ do prestador de serviços** está **habilitado pela prefeitura** para utilizar o **código de benefício municipal** informado, considerando que alguns municípios **restringem a aplicação de benefícios fiscais a contribuintes específicos**.

**(7)** Caso necessário, altere o **código de benefício municipal** ou o **código de tributação do ISS**, conforme **orientação do contador responsável** e de acordo com a **parametrização aceita pela prefeitura**.

**(8)** Após realizar os ajustes necessários, **exclua a NFS-e rejeitada** e **emita novamente o documento fiscal**.

**CAUSA**

A rejeição ocorre quando há **incompatibilidade entre o código de benefício municipal** informado na DPS (Declaração de Prestação de Serviços) e o **código de tributação do ISS** ou o **CPF/CNPJ do prestador**, conforme as regras de validação estabelecidas pela prefeitura do município de incidência do ISSQN. Isso pode acontecer quando:

- O código de benefício não está cadastrado ou vigente na base da prefeitura;
- O código de tributação utilizado não permite a aplicação do benefício fiscal informado;
- O prestador de serviços não está autorizado pela prefeitura a utilizar aquele benefício específico;
- Há divergência entre as configurações do sistema e os parâmetros aceitos pelo município.
