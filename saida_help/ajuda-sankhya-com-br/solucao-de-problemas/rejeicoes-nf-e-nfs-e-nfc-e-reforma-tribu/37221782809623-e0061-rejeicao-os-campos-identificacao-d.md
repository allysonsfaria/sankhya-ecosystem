---
id: "37221782809623"
titulo: "E0061 Rejeição: Os campos identificação do Tomador (se identificado na DPS), data de competência (dCompet), e valor do serviço (vServ), não podem ser alterados quando a opção do simples nacional for MEI (opSimpNac = 2) ou ME/EPP (opSimpNac = 3)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221782809623-E0061-Rejei%C3%A7%C3%A3o-Os-campos-identifica%C3%A7%C3%A3o-do-Tomador-se-identificado-na-DPS-data-de-compet%C3%AAncia-dCompet-e-valor-do-servi%C3%A7o-vServ-n%C3%A3o-podem-ser-alterados-quando-a-op%C3%A7%C3%A3o-do-simples-nacional-for-MEI-opSimpNac-2-ou-ME-EPP-opSimpNac-3"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:25Z"
rotulos: ["Configuração", "Simples Nacional", "SEFAZ", "Impostos", "NFS-e", "Erro", "Valor do serviço", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "MEI (Microempreendedor Individual)", "Data de competência", "Identificação do tomador", "ME EPP - Simples Nacional", "ME/EPP (Microempresa e Empresa de Pequeno Porte)", "MEI - Simples Nacional"]
---

# E0061 Rejeição: Os campos identificação do Tomador (se identificado na DPS), data de competência (dCompet), e valor do serviço (vServ), não podem ser alterados quando a opção do simples nacional for MEI (opSimpNac = 2) ou ME/EPP (opSimpNac = 3).

**MENSAGEM**

E0061 Rejeição: Os campos identificação do Tomador (se identificado na DPS), data de competência (dCompet), e valor do serviço (vServ), não podem ser alterados quando a opção do simples nacional for MEI (opSimpNac = 2) ou ME/EPP (opSimpNac = 3).

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** para uma empresa optante pelo **Simples Nacional** enquadrada como **MEI (Microempreendedor Individual)** ou **ME/EPP (Microempresa e Empresa de Pequeno Porte)**, o usuário tentou **alterar informações** que não podem ser modificadas após o envio inicial, como a **identificação do tomador**, a **data de competência** ou o **valor do serviço**. Essa tentativa de alteração resultou na rejeição da nota pela Sefaz com a mensagem E0061.

**SOLUÇÃO**

**(1)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

**(2)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''Geral''**.

**(3)** Verifique o campo **“Regime esp. Tributação ISS (NFS-e)”** e confirme se ele está configurado corretamente, de acordo com o **enquadramento tributário da empresa**:

- **Código 5** – **MEI (Microempreendedor Individual)** – Simples Nacional
- **Código 6** – **ME/EPP (Microempresa ou Empresa de Pequeno Porte)** – Simples Nacional

**(4)** Caso seja necessário corrigir informações da **NFS-e rejeitada**, realize o **cancelamento da nota fiscal original** pelo sistema, informando o **motivo do cancelamento** conforme as opções permitidas pelo município.

**(5)** Em seguida, **emita uma nova NFS-e** com as informações corretas desde o início, garantindo que:

- A **identificação do tomador** esteja correta na tela **''Parceiros''** (Configurações » Cadastros » Parceiros);
- A **data de competência** esteja compatível com a **prestação do serviço**;
- O **valor do serviço** esteja corretamente informado, de acordo com o serviço prestado.

**(5)** Por fim, **transmita a nova nota fiscal para autorização pela prefeitura**, evitando realizar alterações nos campos citados após a emissão inicial.

**CAUSA**

A rejeição ocorre porque a **Sefaz estabelece regras específicas** para empresas optantes pelo **Simples Nacional** enquadradas como **MEI** ou **ME/EPP**. Quando o campo **"Regime esp. Tributação ISS (NFS-e)"** está configurado com as opções **5 (MEI - Simples Nacional)** ou **6 (ME EPP - Simples Nacional)**, determinados campos da NFS-e **não podem ser alterados** após a emissão inicial do documento. Essa restrição visa **garantir a integridade fiscal** e evitar inconsistências nas informações prestadas à administração tributária. A tentativa de modificar a **identificação do tomador**, a **data de competência** ou o **valor do serviço** em uma nota já emitida viola essa regra de validação, resultando na rejeição E0061.
