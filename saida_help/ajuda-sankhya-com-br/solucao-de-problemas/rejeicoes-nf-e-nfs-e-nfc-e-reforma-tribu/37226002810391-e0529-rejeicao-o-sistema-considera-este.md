---
id: "37226002810391"
titulo: "E0529 Rejeição: O sistema considera este cenário para a prestação de serviço informada na DPS uma operação tributável. Não é permitido ao emitente da DPS informar que a prestação de serviço se trata de uma exportação de serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226002810391-E0529-Rejei%C3%A7%C3%A3o-O-sistema-considera-este-cen%C3%A1rio-para-a-presta%C3%A7%C3%A3o-de-servi%C3%A7o-informada-na-DPS-uma-opera%C3%A7%C3%A3o-tribut%C3%A1vel-N%C3%A3o-%C3%A9-permitido-ao-emitente-da-DPS-informar-que-a-presta%C3%A7%C3%A3o-de-servi%C3%A7o-se-trata-de-uma-exporta%C3%A7%C3%A3o-de-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:25Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Financeiro", "Código de Situação Tributária", "Exportação de serviço", "Prestação de serviço informada na DPS", "Operação tributável", "Prestação de serviço configurada é uma operação tributável"]
---

# E0529 Rejeição: O sistema considera este cenário para a prestação de serviço informada na DPS uma operação tributável. Não é permitido ao emitente da DPS informar que a prestação de serviço se trata de uma exportação de serviço.

**MENSAGEM**

E0529 Rejeição: O sistema considera este cenário para a prestação de serviço informada na DPS uma operação tributável. Não é permitido ao emitente da DPS informar que a prestação de serviço se trata de uma exportação de serviço.

**SITUAÇÃO**

Ao emitir uma **DPS (Declaração de Prestação de Serviços)** no sistema, o usuário informou que a operação se trata de uma **exportação de serviço**, porém o sistema identificou que a prestação de serviço configurada é uma **operação tributável**. Esta inconsistência entre a natureza da operação e a indicação de exportação resultou na rejeição do documento pela Sefaz com a mensagem E0529.

**SOLUÇÃO**

**(1)** Acesse a tela [**"Tipo de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Localize o TOP utilizado na emissão da DPS rejeitada.

**(3)** Verifique se o TOP está configurado corretamente para a natureza da operação:

- Se a operação **não é uma exportação de serviço**, certifique-se de que o campo relacionado à exportação não esteja marcado ou habilitado no TOP.
- Se a operação **é realmente uma exportação**, verifique se o **"Código de Situação Tributária - CST"** configurado nas alíquotas de IBS e CBS está adequado para operações de exportação.

**(4)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(5)** Verifique o **''Código de Situação Tributária'' (CST)** vinculado ao TOP utilizado.

**(6)** Ajuste o CST conforme a natureza da operação:

- Para **operações tributáveis**, utilize um CST que indique tributação normal.
- Para **operações de exportação**, utilize um CST específico para exportação, que indique isenção ou não incidência dos tributos.

**(7)** Após realizar os ajustes necessários, emita novamente a DPS com as configurações corretas.

**CAUSA**

A rejeição ocorre quando há uma **incompatibilidade entre a natureza da operação** configurada no sistema e a **indicação de exportação de serviço** na DPS. O sistema identifica que a prestação de serviço é uma operação tributável (sujeita ao recolhimento de IBS e CBS), mas o documento foi emitido indicando tratar-se de uma exportação, que possui tratamento tributário diferenciado. Esta inconsistência nas configurações do **Tipo de Operação** e do **Código de Situação Tributária** nas alíquotas de IBS e CBS resulta na rejeição pela Sefaz, pois não é permitido classificar uma operação tributável como exportação de serviço.
