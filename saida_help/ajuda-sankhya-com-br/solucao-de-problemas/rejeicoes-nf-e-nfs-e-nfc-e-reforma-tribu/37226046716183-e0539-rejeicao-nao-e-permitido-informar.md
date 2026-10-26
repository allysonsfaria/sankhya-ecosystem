---
id: "37226046716183"
titulo: "E0539 Rejeição: Não é permitido informar não incidência do ISSQN = 4 (Não Incidência) para qualquer subitem da lista nacional de serviço informado na DPS, se o subitem for incidente, conforme a parametrização do município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226046716183-E0539-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-n%C3%A3o-incid%C3%AAncia-do-ISSQN-4-N%C3%A3o-Incid%C3%AAncia-para-qualquer-subitem-da-lista-nacional-de-servi%C3%A7o-informado-na-DPS-se-o-subitem-for-incidente-conforme-a-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:21Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "NFS-e", "ISSQN", "Não incidência do ISSQN", "Incidência do ISSQN = 4 (Não Incidência)", "Parametrização do município de incidência", "4 - Não Incidência", "Manual da prefeitura do município", "Lista nacional de serviço informado na DPS"]
---

# E0539 Rejeição: Não é permitido informar não incidência do ISSQN = 4 (Não Incidência) para qualquer subitem da lista nacional de serviço informado na DPS, se o subitem for incidente, conforme a parametrização do município de incidência do ISSQN.

**MENSAGEM**

E0539 Rejeição: Não é permitido informar não incidência do ISSQN = 4 (Não Incidência) para qualquer subitem da lista nacional de serviço informado na DPS, se o subitem for incidente, conforme a parametrização do município de incidência do ISSQN.

**SITUAÇÃO**

Ao emitir uma NFS-e, a nota é rejeitada pela Sefaz com a mensagem de erro E0539, indicando que foi informada **não incidência do ISSQN** para um serviço que, segundo a parametrização do município de incidência, **deveria ser tributado**.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço)

**(2)** Localize o serviço utilizado na nota fiscal rejeitada.

**(3)** Na aba **“Alíquotas de ISS”**, valide a configuração para o **município de incidência do ISSQN**:

**(4)** No campo **“Cod. Trib. Município”**, confirme que está preenchido corretamente com o código do município onde o serviço é prestado.

**(5)** Acesse a tela [**“Tipo de Operação – TOP”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação – TOP), na aba **“NFS-e”**, revise o campo **“Cód. Natureza Oper. ISS (NFS-e)”**:

- **Serviço tributável:** utilize **“A - Sem dedução”** ou **“B - Com dedução/Materiais”**;
- **Serviço isento ou imune:** utilize **“C - Imune/Isenta ISSQN”**;
- Evite usar configurações que indiquem **não incidência** quando o serviço é tributável no município.

**(6)** Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa), na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e''** sub-aba **''Geral"**.

**(7)** No campo **“Regime esp. trib. ISS (NFS-e)”**, confirme a configuração correta:

- Para serviços tributáveis, utilize **“T - Tributável”**, **“H - Tributável S.N”** ou **“G - Tributável Fixo”**;
- Não utilize **“E - Não Incidência no Município”** ou **“N - Não Tributável”** para serviços incidentes no município.

**(8)** Consulte o **manual da prefeitura do município** de incidência para confirmar se o serviço prestado possui **incidência de ISSQN** ou se há alguma particularidade na legislação local.

**(9)** Após realizar todos os ajustes necessários, emita novamente a NFS-e.

**CAUSA**

A rejeição ocorre porque foi informado no documento fiscal que o serviço possui **não incidência do ISSQN** (código 4), porém, de acordo com a **parametrização do município de incidência** e a **lista nacional de serviços**, o subitem informado **é incidente de ISSQN**. Isso gera uma **inconsistência entre a configuração do sistema e as regras tributárias do município**, resultando na rejeição da nota pela Sefaz.
