---
id: "37222814611223"
titulo: "REJEIÇÃO E0228: A IM deve ser informada para o emitente tomador do serviço na DPS, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222814611223-REJEI%C3%87%C3%83O-E0228-A-IM-deve-ser-informada-para-o-emitente-tomador-do-servi%C3%A7o-na-DPS-conforme-informa%C3%A7%C3%B5es-complementares-registradas-no-CNC-NFS-e-do-munic%C3%ADpio-emissor-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:24Z"
rotulos: ["Configuração", "SEFAZ", "Prefeituras", "NFS-e", "Passos para resolver", "Como Resolver", "Cadastro Nacional de Contribuintes (CNC)", "Inscrição Municipal (IM)", "CNC NFS-e (Cadastro Nacional Centralizado de Notas Fiscais de Serviços Eletrônicas)", "NFS-e do município emissor", "Município emissor informado na DPS"]
---

# REJEIÇÃO E0228: A IM deve ser informada para o emitente tomador do serviço na DPS, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS

**MENSAGEM**

E0228 Rejeição: A IM deve ser informada para o emitente tomador do serviço na DPS, conforme informações complementares registradas no CNC NFS-e do município emissor informado na DPS.

**SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços eletrônica)** em que o **emitente é também o tomador do serviço**, o sistema rejeitou o documento porque a **Inscrição Municipal (IM)** do emitente não foi informada corretamente na DPS (Declaração de Prestação de Serviços), conforme exigido pelo **Cadastro Nacional de Contribuintes (CNC)** da NFS-e do município.

**SOLUÇÃO**

**(1)** Acesse a tela **"Empresa"** (Configurações » Cadastros » Empresa) e localize o cadastro da empresa emitente da NFS-e.

**(2)** Verifique se o campo **"Inscrição Municipal (IM)"** está preenchido corretamente com o número de inscrição municipal da empresa no município emissor.

**(3)** Caso a **Inscrição Municipal** não esteja cadastrada ou esteja incorreta, atualize o campo com as informações corretas fornecidas pela prefeitura do município.

**(4)** Confirme que o campo **"Código do contribuinte da NFS-e"** também está preenchido, pois este código é necessário para a emissão de NFS-e e deve estar de acordo com o cadastro no CNC do município.

**(5)** Salve as alterações realizadas no cadastro da empresa.

**(6)** Retorne ao ''**Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e gere novamente a NFS-e, garantindo que todas as informações do emitente tomador estejam corretas.

**CAUSA**

A rejeição ocorre porque, quando o **emitente é também o tomador do serviço** na DPS, a legislação municipal exige que a **Inscrição Municipal (IM)** seja obrigatoriamente informada no documento fiscal. Esta informação deve estar **registrada no Cadastro Nacional de Contribuintes (CNC)** da NFS-e do município emissor. A ausência ou incorreção da IM no cadastro da empresa impede a validação do documento pela Sefaz municipal, resultando na rejeição E0228.
