---
id: "37224172221079"
titulo: "E0288 Rejeição: O IM informado está inativo no CNC NFS-e do município emissor para a data de competência informada na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224172221079-E0288-Rejei%C3%A7%C3%A3o-O-IM-informado-est%C3%A1-inativo-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-para-a-data-de-compet%C3%AAncia-informada-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:52Z"
rotulos: ["Configuração", "Central de Vendas", "Prefeituras", "NFS-e", "Erro", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Cadastro Nacional de Contribuintes (CNC)", "IM informado está inativo no CNC NFS-e do município emissor", "Inscrição Municipal (IM)", "Nota é rejeitada pela prefeitura", "Cadastro Nacional de Contribuintes (CNC) da NFS-e do município"]
---

# E0288 Rejeição: O IM informado está inativo no CNC NFS-e do município emissor para a data de competência informada na DPS.

**MENSAGEM**

E0288 Rejeição: O IM informado está inativo no CNC NFS-e do município emissor para a data de competência informada na DPS.

**SITUAÇÃO**

Ao emitir uma **NFS-e** (Nota Fiscal de Serviços Eletrônica) pela **Central de Vendas**, a nota é **rejeitada pela prefeitura** e a mensagem de erro E0288 é apresentada, informando que a **Inscrição Municipal (IM)** da empresa emissora está **inativa no Cadastro Nacional de Contribuintes (CNC)** da NFS-e do município para a data de competência informada no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)** Verifique junto à **Prefeitura do município emissor** se a **Inscrição Municipal (IM)** da empresa está **ativa e regularizada** no Cadastro Nacional de Contribuintes da NFS-e.

**(2)** Caso a Inscrição Municipal esteja **inativa, suspensa ou cancelada**, regularize a situação cadastral junto ao **órgão municipal competente** (Secretaria da Fazenda Municipal ou equivalente).

**(3)** Após a regularização da Inscrição Municipal junto à prefeitura, aguarde a **atualização do cadastro no sistema da prefeitura**, que pode levar algumas horas ou dias, dependendo do município.

**(4)** Acessa a tela [**''Empresa''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Configurações » Cadastros » Empresas).

**(5)** Verifique se o campo **''Inscrição Municipal''** está cadastrado corretamente e atualizado.

**(6)** Caso necessário, **atualize a Inscrição Municipal** no cadastro da empresa no sistema Sankhya com os dados corretos fornecidos pela prefeitura.

**(7)** Após a regularização cadastral, tente **emitir novamente a NFS-e** na tela [**"Central de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

**CAUSA**

A rejeição ocorre porque a **Inscrição Municipal (IM)** informada no cadastro da empresa emissora está **inativa, suspensa ou cancelada** no Cadastro Nacional de Contribuintes (CNC) da NFS-e do município para a **data de competência** informada no documento fiscal. Isso pode acontecer por **irregularidades fiscais**, **falta de atualização cadastral**, **débitos municipais pendentes** ou **cancelamento da inscrição** junto à prefeitura. A prefeitura valida a situação cadastral da Inscrição Municipal no momento da emissão da nota e, caso esteja inativa, **rejeita o documento** automaticamente.
