---
id: "37226863513239"
titulo: "E0631 Rejeição: Não é permitido informar alíquota quando o município de incidência do ISSQN não está Ativo no Sistema Nacional NFS-e, para o prestador de serviço ME/EPP (opSimpNac = 3) na data de competência informada na DPS, com apuração do ISSQN pelo si"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226863513239-E0631-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-quando-o-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-n%C3%A3o-est%C3%A1-Ativo-no-Sistema-Nacional-NFS-e-para-o-prestador-de-servi%C3%A7o-ME-EPP-opSimpNac-3-na-data-de-compet%C3%AAncia-informada-na-DPS-com-apura%C3%A7%C3%A3o-do-ISSQN-pelo-si"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:36Z"
rotulos: ["Configuração", "Empresa", "Alíquota de ISS", "XML", "Prefeituras", "NFS-e", "ISSQN", "Sistema Nacional NFS-e", "Retenção do ISSQN", "Município de incidência do ISSQN não está Ativo", "Apuração do ISSQN pelo Simples Nacional", "Simples Nacional (ME/EPP)"]
---

# E0631 Rejeição: Não é permitido informar alíquota quando o município de incidência do ISSQN não está Ativo no Sistema Nacional NFS-e, para o prestador de serviço ME/EPP (opSimpNac = 3) na data de competência informada na DPS, com apuração do ISSQN pelo si

**MENSAGEM**

E0631 Rejeição: Não é permitido informar alíquota quando o município de incidência do ISSQN não está Ativo no Sistema Nacional NFS-e, para o prestador de serviço ME/EPP (opSimpNac = 3) na data de competência informada na DPS, com apuração do ISSQN pelo simples nacional (regApTribISSQN = 1) sem retenção do ISSQN (tpRetISSQN = 1).

**SITUAÇÃO**

Ao tentar emitir uma NFS-e para um município que **não está ativo no Sistema Nacional NFS-e**, sendo a empresa prestadora optante pelo **Simples Nacional (ME/EPP)**, com **apuração do ISSQN pelo Simples Nacional** e **sem retenção do ISSQN**, o sistema apresenta a mensagem de rejeição acima.

**SOLUÇÃO**

**(1)** Verifique se o **município de incidência do ISSQN** informado na nota fiscal está **ativo no Sistema Nacional NFS-e**.

- Caso o município não esteja ativo, a **alíquota do ISSQN não deve ser informada** no XML da NFS-e.

**(2)** Acesse a tela [**"Empresa"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa), na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"** sub-aba **"Geral"**.

**(3)** Marque o campo **"Envia o Valor do ISS e alíquota no XML, apenas quando o ISS for devido a outro município?"**.

- Esta configuração garante que o sistema **envie as tags Valor do ISS e Alíquota no XML somente quando o município de incidência for diferente do município da empresa**.

**(4)** Acesse a tela **''Parceiros''** (Comercial » Preferências » Empresa), na aba **''Fiscal'',** verifique se o campo **"Retém ISSS"** está configurado corretamente:

- Se o tomador do serviço **não retém ISS**, não habilite a marcação.
- Se o tomador **retém ISS**, habilite a marcação.
- Verifique na aba **''Identificação''** no campo **''Cad.Mun.Contribuintes''** se o **CNPJ e/ou Inscrição Municipal** estão corretos e se o tomador está cadastrado na base de dados do município.

**(5)** Confirme se o campo **"Cidade"** no rodapé da nota fiscal está preenchido corretamente com a **cidade onde ocorreu a prestação do serviço**.

**(6)** Após realizar os ajustes, **gere novamente o lote da nota** e verifique se o XML não contém mais a tag **<ValorIss>** e a **tag de alíquota** quando o município de incidência não estiver ativo no Sistema Nacional NFS-e.

**(7)** Exporte o arquivo XML no **"Portal de Vendas"** (NFS-e > Gerar XML do RPS para NFS-e) e valide se a tag **<ISSRetido>** está preenchida corretamente conforme a situação da operação.

**CAUSA**

A rejeição ocorre porque o sistema está **enviando a alíquota do ISSQN no XML** para um município que **não está ativo no Sistema Nacional NFS-e**. Quando a empresa é **optante pelo Simples Nacional (ME/EPP)**, com **apuração do ISSQN pelo Simples Nacional** e **sem retenção do ISSQN**, a Prefeitura é responsável por calcular e determinar a alíquota aplicável. Portanto, **não é permitido informar a alíquota** nessas condições específicas quando o município não está ativo no sistema nacional.
