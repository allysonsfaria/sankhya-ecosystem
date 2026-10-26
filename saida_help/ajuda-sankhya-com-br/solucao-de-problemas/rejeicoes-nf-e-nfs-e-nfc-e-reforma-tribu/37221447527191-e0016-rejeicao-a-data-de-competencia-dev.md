---
id: "37221447527191"
titulo: "E0016 Rejeição: A data de competência deve ser igual ou posterior à data de ativação do convênio do município emissor informado na DPS, exceto quando o emitente for MEI na data de competência informada."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221447527191-E0016-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-deve-ser-igual-ou-posterior-%C3%A0-data-de-ativa%C3%A7%C3%A3o-do-conv%C3%AAnio-do-munic%C3%ADpio-emissor-informado-na-DPS-exceto-quando-o-emitente-for-MEI-na-data-de-compet%C3%AAncia-informada"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:41Z"
rotulos: ["Configuração", "Cidades", "SEFAZ", "Prefeituras", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "Declaração de Prestação de Serviços (DPS)", "MEI (Microempreendedor Individual)", "Data de competência", "Data de ativação do convênio", "Município emissor", "Data de ativação do convênio do município emissor"]
---

# E0016 Rejeição: A data de competência deve ser igual ou posterior à data de ativação do convênio do município emissor informado na DPS, exceto quando o emitente for MEI na data de competência informada.

**MENSAGEM**

E0016 Rejeição: A data de competência deve ser igual ou posterior à data de ativação do convênio do município emissor informado na DPS, exceto quando o emitente for MEI na data de competência informada.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o usuário informou uma **data de competência anterior à data de ativação do convênio** do município emissor. Como resultado, o documento foi rejeitado pela Sefaz com a mensagem de erro acima.

**SOLUÇÃO**

**(1)** Verifique a **data de ativação do convênio** do município emissor junto à prefeitura ou no portal da Secretaria da Fazenda municipal.

**(2)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(3)** Na grade **''Cabeçalho''**, localize o campo **''Dt. Neg.''** e ajuste a data da competência para que seja **igual ou posterior á data de ativação do convênio** do município emissor.

**(4)** Caso o emitente seja **MEI (Microempreendedor Individual)** na data de competência informada, esta validação não se aplica e a DPS poderá ser emitida normalmente.

**(5)** Salve as alterações e tente emitir novamente a DPS

**CAUSA**

A rejeição E0016 ocorre quando a **data de competência informada na DPS é anterior à data de ativação do convênio** do município emissor. Esta validação garante que apenas documentos fiscais com competência válida sejam processados, respeitando o período em que o município está habilitado para receber declarações eletrônicas. A exceção aplica-se quando o emitente possui a **condição de MEI** na data de competência, situação na qual esta regra de validação não é aplicada.
