---
id: "37225096547863"
titulo: "E0423 Rejeição: O valor recebido deve ser informado na DPS quando o intermediário do serviço for o emitente da DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225096547863-E0423-Rejei%C3%A7%C3%A3o-O-valor-recebido-deve-ser-informado-na-DPS-quando-o-intermedi%C3%A1rio-do-servi%C3%A7o-for-o-emitente-da-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:12Z"
rotulos: ["Central de Vendas", "Portal de Vendas", "SEFAZ", "Impostos", "Reforma Tributária", "Intermediário do serviço", "DPS (Documento de Prestação de Serviços)", "Intermediador da Transação", "Valor recebido pela intermediação"]
---

# E0423 Rejeição: O valor recebido deve ser informado na DPS quando o intermediário do serviço for o emitente da DPS.

**MENSAGEM**

E0423 Rejeição: O valor recebido deve ser informado na DPS quando o intermediário do serviço for o emitente da DPS.

**SITUAÇÃO**

Mensagem apresentada durante a **emissão da DPS** (Documento de Prestação de Serviços) quando o emitente atua como **intermediário do serviço** e não informou o valor recebido pela intermediação.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize o documento que apresentou a rejeição.

- Ao selecionar e abrir o documento, o sistema direciona automaticamente para a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Na grade **''Cabeçalho''**, verifique se o campo **''Intermediador da Transação''** está configurado como **intermediário do serviço**.

**(3)** Na grade **''Rodapé''**, localize o campo **''Vlr do Desdobramento''** e informe o valor efetivamente recebido pela intermediação do serviço.

**(4)** Certifique-se de que o valor informado está **correto e corresponde ao valor da intermediação** realizada.

**(5)** Salve as alterações e **retransmita a DPS** para o portal da SEFAZ.

**CAUSA**

Esta rejeição ocorre quando a **DPS é emitida por um intermediário do serviço** e o campo referente ao **valor recebido pela intermediação não foi preenchido**. Conforme as regras estabelecidas pela **Lei Complementar nº 214/2025** (Reforma Tributária), quando o emitente da DPS atua como intermediário, é **obrigatório informar o valor recebido** pela prestação do serviço de intermediação, para fins de **apuração correta do IBS e da CBS**.
