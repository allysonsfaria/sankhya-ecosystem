---
id: "37226477339159"
titulo: "E0583 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que seja MEI na data de competência informada na DPS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226477339159-E0583-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-para-o-prestador-do-servi%C3%A7o-que-seja-MEI-na-data-de-compet%C3%AAncia-informada-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:54Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Não é permitido retenção do ISSQN", "retenção de ISSQN", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Regime MEI (Microempreendedor Individual)", "Microempreendedor Individual (MEI)", "MEI"]
---

# E0583 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que seja MEI na data de competência informada na DPS

**MENSAGEM**

E0583 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que seja MEI na data de competência informada na DPS.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** com retenção de ISSQN, a nota é rejeitada pela prefeitura apresentando a mensagem de erro E0583, informando que **não é permitida a retenção do imposto** quando o prestador do serviço é **Microempreendedor Individual (MEI)**.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

**(2)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''Geral''**, verifique se o campo **"Cód. Reg. trib. ISS (NFS-e)"** está configurado com a opção **"8 - Tributável MEI"**.

**(3)** Acesse a tela **"Parceiro"** (Configurações » Cadastros » Parceiros).

**(4)** Na aba **''Fiscal''**, marque o campo **''Retém ISS''** garatindo que não haverá retenção do imposto nas operações com este parceiro.

**(5)** Caso a retenção esteja sendo configurada na TOP, acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(6)** Na aba **"NFS-e"**, verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"** e certifique-se de que a **natureza da operação não está configurada para reter ISSQN**.

**(7)** Após realizar os ajustes necessários, **gere novamente a NFS-e** e verifique se a rejeição foi solucionada.

**CAUSA**

A rejeição ocorre porque a **legislação tributária não permite que empresas optantes pelo regime MEI** (Microempreendedor Individual) tenham **retenção de ISSQN** em suas operações. Quando o sistema identifica que o prestador é MEI e a nota está configurada com retenção do imposto, a prefeitura rejeita automaticamente o documento fiscal, gerando a mensagem de erro E0583.
