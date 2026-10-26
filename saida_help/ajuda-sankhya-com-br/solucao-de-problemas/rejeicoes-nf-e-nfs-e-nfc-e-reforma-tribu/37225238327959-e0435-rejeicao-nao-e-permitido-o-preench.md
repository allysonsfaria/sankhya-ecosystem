---
id: "37225238327959"
titulo: "E0435 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN quando ocorrer Imunidade, Exportação do serviço ou Não incidência."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225238327959-E0435-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-dos-campos-do-grupo-de-informa%C3%A7%C3%B5es-relativas-%C3%A0-Dedu%C3%A7%C3%A3o-Redu%C3%A7%C3%A3o-do-ISSQN-quando-ocorrer-Imunidade-Exporta%C3%A7%C3%A3o-do-servi%C3%A7o-ou-N%C3%A3o-incid%C3%AAncia"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:07Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Financeiro", "NFS-e", "ISSQN", "Grupo de Dedução/Redução do ISSQN", "Legislação tributária municipal", "Nota Fiscal de Serviços Eletrônica (NFS-e)", "Não pode haver dedução ou redução do imposto", "ISSQN não é exigível", "Preenchimento de informações no grupo de Dedução/Redução do ISSQN"]
---

# E0435 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN quando ocorrer Imunidade, Exportação do serviço ou Não incidência.

**MENSAGEM**

E0435 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN quando ocorrer Imunidade, Exportação do serviço ou Não incidência.

**SITUAÇÃO**

Durante a emissão de uma **Nota Fiscal de Serviços Eletrônica (NFS-e)**, o sistema rejeitou o documento ao identificar o **preenchimento de informações no grupo de Dedução/Redução do ISSQN**, impedindo a autorização da nota fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela [**''Tipos de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Localize a natureza de operação utilizada na emissão da NFS-e rejeitada.

**(3)** Na aba **''NFS-e''**, verifique o campo **''Cód. Natureza Oper. ISS (NFS-e)''**.

**(4)** Confirme se a natureza está configurada com uma das seguintes opções:

- **''Código 2 - Não incidência''**
- **''Código 3 - Isenção''**
- **''Código 4 - Exportação''**
- **''Código 5 - Imunidade''**

**(5)** Acesse a tela [**"Ajustes de Apuração do ISSQN"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595934-Ajustes-de-Apura%C3%A7%C3%A3o-do-ISSQN) (Livros Fiscais » Avançado » Super Sintegra » Ajustes de Apuração do ISSQN).

**(6)** Verifique se existem lançamentos de **dedução ou redução do ISSQN** para a empresa e período da nota rejeitada.

**(8)** Nas abas **“Dedução do ISSQN”** ou **“Compensação do ISSQN”**, confirme se **existem lançamentos registrados**.

- Caso existam lançamentos, remova-os ou ajuste-os para que não sejam aplicados em operações classificadas como **''Imunidade''**, **''Exportação''** ou **''Não Incidência''**.

**(9)** Certifique-se de que, no momento da emissão da **NFS-e**, **nenhum campo relacionado a deduções ou reduções do ISSQN esteja preenchido** quando a **exigibilidade do imposto** for classificada como **Imunidade, Exportação ou Não Incidência**.

**(10)** Após realizar os ajustes necessários, **reemita a NFS-e** e verifique se a rejeição foi solucionada.

**CAUSA**

A rejeição ocorre porque a **legislação tributária municipal** determina que, em situações onde o **ISSQN não é exigível** (casos de Imunidade, Exportação do serviço ou Não incidência), **não pode haver dedução ou redução** do imposto, uma vez que não há base de cálculo ou valor de imposto a ser deduzido. O sistema da Sefaz valida essa regra e rejeita automaticamente notas fiscais que apresentem informações no grupo de Dedução/Redução do ISSQN quando a exigibilidade do imposto se enquadra nessas situações específicas.
