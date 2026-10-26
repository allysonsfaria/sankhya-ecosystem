---
id: "37224109649815"
titulo: "E0289 Rejeição: IM do emitente intermediário não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224109649815-E0289-Rejei%C3%A7%C3%A3o-IM-do-emitente-intermedi%C3%A1rio-n%C3%A3o-est%C3%A1-autorizado-a-emitir-NFS-e-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:54Z"
rotulos: ["Configuração", "Prefeituras", "NFS-e", "Erro", "NFS-e (Nota Fiscal de Serviço Eletrônica)", "Inscrição Municipal (IM)", "Divergência ou ausência de autorização no cadastro do Cadastro Nacional de Contribuintes (CNC)", "(IM) do emitente intermediário não está cadastrada ou autorizada", "IM do emitente intermediário não está autorizado a emitir NFS-e"]
---

# E0289 Rejeição: IM do emitente intermediário não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**MENSAGEM**

E0289 Rejeição: IM do emitente intermediário não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e (Nota Fiscal de Serviço Eletrônica)** através do sistema, o usuário recebe a rejeição E0289 informando que a **Inscrição Municipal (IM)** do emitente intermediário não está autorizada a emitir notas fiscais de serviço para o município especificado. Esta situação ocorre quando há **divergência ou ausência de autorização** no cadastro do Cadastro Nacional de Contribuintes (CNC) da prefeitura.

**SOLUÇÃO**

**(1)**  Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

**(2)** Na aba **''Geral''**, verifique as informações cadastrais da empresa, especialmente:

- **"Inscrição Municipal"**
- **"Razão Social"**
- **"CNPJ"**
- **"Endereço"**

**(3)** Compare os dados cadastrados no sistema com as **informações oficiais** fornecidas pela prefeitura do município emissor. Certifique-se de que todos os dados estão **idênticos e corretos**.

**(4)** Caso identifique alguma **divergência**, corrija imediatamente o cadastro no sistema para que fique **exatamente igual** ao cadastro da prefeitura.

**(5)** Verifique junto à **prefeitura do município** se a empresa está devidamente **autorizada e habilitada** para emitir NFS-e. Caso não esteja, solicite a autorização necessária.

**(6)** Após realizar as correções cadastrais e confirmar a autorização junto à prefeitura, **gere novamente o lote** da NFS-e.

**(7)** Estando todas as **configurações corretas** e a empresa devidamente autorizada, a nota será **aprovada com sucesso**.

**CAUSA**

Esta rejeição ocorre quando a **Inscrição Municipal (IM)** do emitente intermediário **não está cadastrada ou autorizada** no sistema da prefeitura para emitir NFS-e no município especificado. As causas mais comuns incluem:

- **Divergência** nos dados cadastrais da empresa entre o sistema Sankhya e o cadastro da prefeitura (especialmente na Inscrição Municipal)
- **Ausência de autorização** da empresa junto à prefeitura para emissão de NFS-e
- **Cadastro incompleto ou desatualizado** no CNC (Cadastro Nacional de Contribuintes) do município
- **Inscrição Municipal incorreta, incompleta ou inativa** no sistema da prefeitura
