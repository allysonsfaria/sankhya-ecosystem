---
id: "37225250047639"
titulo: "E0436 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN quando o prestador de serviço é MEI."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225250047639-E0436-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-dos-campos-do-grupo-de-informa%C3%A7%C3%B5es-relativas-%C3%A0-Dedu%C3%A7%C3%A3o-Redu%C3%A7%C3%A3o-do-ISSQN-quando-o-prestador-de-servi%C3%A7o-%C3%A9-MEI"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:06Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "NFS-e", "ISSQN", "Regime especial de tributação", "NFS-e (Nota Fiscal de Serviço Eletrônica)", "MEI (Microempreendedor Individual)", "Grupo de Dedução/Redução do ISSQN", "Dedução/Redução do ISSQN", "Regime tributário simplificado", "Empresas optantes pelo regime MEI", "MEI"]
---

# E0436 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN quando o prestador de serviço é MEI.

**MENSAGEM**

E0436 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN quando o prestador de serviço é MEI.

**SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviço Eletrônica)**, o usuário preencheu informações no **grupo de Dedução/Redução do ISSQN**, porém a empresa emissora está cadastrada como **MEI (Microempreendedor Individual)**. Como o MEI possui um **regime especial de tributação** que não permite deduções ou reduções do ISSQN, a Sefaz rejeitou a nota fiscal com a mensagem de erro E0436.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**''Empresa''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

**(2)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba ''Geral'', confirme se o campo **''Reg. esp. trib. ISS (NFS-e)''** está configurado como **"5 - Microempresário Individual (MEI)"**.

**(3)** Acesse a tela [**''Ajustes de Apuração do ISSQN''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595934-Ajustes-de-Apura%C3%A7%C3%A3o-do-ISSQN) (Livros Fiscais » Avançado » Super Sintegra » Ajustes de Apuração do ISSQN).

**(4)** Remova qualquer lançamento de dedução ou redução do ISSQN tenha sido informado para o período de apuração da nota fiscal.

**(5)** Certifique-se de que **nenhum campo relacionado a deduções ou reduções do ISSQN** esteja preenchido na emissão da NFS-e, incluindo:

- **"Indicador de Dedução"**
- **"Valor da Dedução"**
- **"Nº do Processo"**

**(4)** Reemita a **NFS-e** sem informar dados no grupo de Dedução/Redução do ISSQN.

**CAUSA**

A rejeição ocorre porque **empresas optantes pelo regime MEI** não podem utilizar o **grupo de informações de Dedução/Redução do ISSQN** na emissão de NFS-e. O MEI possui um **regime tributário simplificado** com valores fixos mensais, não sendo permitidas deduções ou reduções na base de cálculo do ISSQN. Ao preencher esses campos indevidamente, o sistema da Sefaz identifica a **incompatibilidade entre o regime tributário e as informações declaradas**, resultando na rejeição E0436.
