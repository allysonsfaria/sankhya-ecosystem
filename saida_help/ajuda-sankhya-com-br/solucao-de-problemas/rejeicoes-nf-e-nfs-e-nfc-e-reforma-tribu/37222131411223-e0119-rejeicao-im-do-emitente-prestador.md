---
id: "37222131411223"
titulo: "E0119 Rejeição: IM do emitente prestador não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222131411223-E0119-Rejei%C3%A7%C3%A3o-IM-do-emitente-prestador-n%C3%A3o-est%C3%A1-autorizado-a-emitir-NFS-e-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:04Z"
rotulos: ["Configuração", "Prefeituras", "NFS-e", "Erro", "Inscrição Municipal (IM)", "Emitente prestador não está autorizada a emitir notas fiscais de serviço eletrônicas", "Cadastro Nacional de Contribuintes (CNC) da NFS-e do município emissor"]
---

# E0119 Rejeição: IM do emitente prestador não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**MENSAGEM**

E0119 Rejeição: IM do emitente prestador não está autorizado a emitir NFS-e, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e, o usuário recebe a mensagem de rejeição informando que a **Inscrição Municipal (IM)** do emitente prestador **não está autorizada** a emitir notas fiscais de serviço eletrônicas. Isso ocorre porque as informações cadastradas no sistema **não correspondem aos dados registrados** no Cadastro Nacional de Contribuintes (CNC) da NFS-e do município emissor.

**SOLUÇÃO**

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize a empresa emitente da NFS-e.

**(2)** Na aba **"Geral"**, verifique se as informações cadastrais da empresa estão **corretas e completas**, especialmente:

- **''CNPJ''**
- **''Razão Social''**
- **''Inscrição Municipal (IM)''**
- Endereço completo

**(3)** Compare as informações cadastradas no sistema com os **dados oficiais registrados junto à Prefeitura** do município emissor. Consulte o documento de autorização ou certificado de inscrição municipal fornecido pela Prefeitura.

**(4)** Caso identifique **divergências**, corrija as informações no cadastro da empresa, especialmente o campo **"Inscrição Municipal"**. Certifique-se de que o número está **completo e sem erros** de digitação.

**(5)** Verifique junto à Prefeitura se a empresa está **devidamente autorizada** a emitir NFS-e. Caso não esteja, solicite a autorização necessária diretamente no portal da Prefeitura ou junto ao setor responsável pela tributação municipal.

**(6)** Após realizar as correções e confirmar a autorização junto à Prefeitura, **gere novamente o lote da NFS-e** no sistema.

**(7)** Estando todas as configurações corretas e a empresa devidamente autorizada, a nota será **aprovada com sucesso**. 

**CAUSA**

A rejeição ocorre quando a **Inscrição Municipal (IM)** cadastrada no sistema **não corresponde** aos dados registrados no Cadastro Nacional de Contribuintes (CNC) da NFS-e do município, ou quando a empresa emitente **não está devidamente autorizada** pela Prefeitura a emitir notas fiscais de serviço eletrônicas. Erros de digitação no número da inscrição municipal ou ausência de autorização junto ao órgão municipal também podem gerar esta rejeição.
