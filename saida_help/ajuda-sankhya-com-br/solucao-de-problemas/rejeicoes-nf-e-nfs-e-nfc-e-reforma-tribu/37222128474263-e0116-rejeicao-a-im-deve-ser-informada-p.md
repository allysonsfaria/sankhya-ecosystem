---
id: "37222128474263"
titulo: "E0116 Rejeição: A IM deve ser informada para o emitente prestador do serviço na DPS, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222128474263-E0116-Rejei%C3%A7%C3%A3o-A-IM-deve-ser-informada-para-o-emitente-prestador-do-servi%C3%A7o-na-DPS-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:05Z"
rotulos: ["Configuração", "SEFAZ", "Prefeituras", "NFS-e", "Erro", "NFS-e Padrão Nacional", "DPS (Declaração de Prestação de Serviços)", "Cadastro Nacional de Contribuintes (CNC)", "Inscrição Municipal (IM)", "Emitente prestador do serviço", "NFS-e do município emissor"]
---

# E0116 Rejeição: A IM deve ser informada para o emitente prestador do serviço na DPS, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**MENSAGEM**

E0116 Rejeição: A IM deve ser informada para o emitente prestador do serviço na DPS, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**SITUAÇÃO**

Ao emitir uma **NFS-e Padrão Nacional**, o sistema apresenta a rejeição informando que a **Inscrição Municipal (IM)** do emitente prestador do serviço deve ser informada na DPS (Declaração de Prestação de Serviços), conforme as informações complementares registradas no **Cadastro Nacional de Contribuintes (CNC)** da NFS-e do município emissor.

**SOLUÇÃO**

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

**(2)** Localize e selecione a **empresa emitente** da NFS-e que está apresentando a rejeição.

**(3)** Na aba **''Geral''**, no campo **''Inscrição Municipal''**, preencha com o número da **Inscrição Municipal (IM)** da empresa no município emissor.

**(4)** Salve as alterações realizadas no cadastro.

**(5)** Retorne à tela de emissão da **NFS-e** e realize novamente a transmissão do documento fiscal.

**OBSERVAÇÃO**: Verifique se a **Inscrição Municipal (IM)** está informada corretamente no **cadastro da empresa utilizada na emissão da NFS-e pela API**, pois divergências nesse campo podem ocasionar rejeições no envio do documento fiscal.

**CAUSA**

A rejeição ocorre quando a **NFS-e Padrão Nacional** é emitida sem que a **Inscrição Municipal (IM)** do emitente prestador do serviço esteja informada no cadastro da empresa. De acordo com as **regras de validação da Sefaz**, quando o município emissor exige a informação da IM nas informações complementares registradas no **CNC NFS-e**, este campo torna-se **obrigatório** para a transmissão do documento fiscal. A ausência desta informação impede a autorização da nota fiscal de serviço eletrônica.
