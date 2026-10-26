---
id: "37221411208215"
titulo: "E0015 Rejeição: A data de competência informada na DPS não pode ser posterior à data de emissão (dhEmi) da DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221411208215-E0015-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-informada-na-DPS-n%C3%A3o-pode-ser-posterior-%C3%A0-data-de-emiss%C3%A3o-dhEmi-da-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:42Z"
rotulos: ["Central de Vendas", "XML", "SEFAZ", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "Data de competência informada na DPS", "DPS (Documento de Prestação de Serviços)", "Data de emissão (dhEmi) da DPS"]
---

# E0015 Rejeição: A data de competência informada na DPS não pode ser posterior à data de emissão (dhEmi) da DPS.

**MENSAGEM**

E0015 Rejeição: A data de competência informada na DPS não pode ser posterior à data de emissão (dhEmi) da DPS.

**SITUAÇÃO**

Durante a emissão de uma **DPS (Documento de Prestação de Serviços)**, o usuário informou uma **data de competência posterior à data de emissão** do documento. Ao tentar transmitir a DPS para a Sefaz, o documento foi rejeitado com a mensagem de erro acima, pois a validação da Sefaz não permite que a data de competência seja futura em relação à data de emissão.

**SOLUÇÃO**

Para resolver esta rejeição, ajuste a **data de competência** da DPS para que seja **igual ou anterior à data de emissão** do documento. Siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Na grade **''Cabeçalho''**, verifique o campo **"Dt. Neg."**.

**(3)** Verifique a **data de Emissão (dhEmi)** da DPS no XML de conferência ou na tela de emissão do documento.

**(4)** Ajuste a data da competência para que seja **igual ou anterior à data de emissão**.

**(5)** Salve as alterações.

**(6)** Gere um novo lote e reenvie a DPS para autorização na Sefaz.

**CAUSA**

A rejeição ocorre quando a **data de competência informada na DPS é posterior à data de emissão** do documento. A Sefaz valida que a competência do serviço prestado não pode ser futura em relação ao momento em que o documento está sendo emitido, garantindo a **consistência temporal das informações fiscais**.
