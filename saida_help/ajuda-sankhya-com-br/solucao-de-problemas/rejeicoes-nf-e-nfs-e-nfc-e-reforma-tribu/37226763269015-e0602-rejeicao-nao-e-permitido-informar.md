---
id: "37226763269015"
titulo: "E0602 Rejeição: Não é permitido informar alíquota quando o campo referente à tributação do ISSQN indicar imunidade, exportação ou não incidência."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226763269015-E0602-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-quando-o-campo-referente-%C3%A0-tributa%C3%A7%C3%A3o-do-ISSQN-indicar-imunidade-exporta%C3%A7%C3%A3o-ou-n%C3%A3o-incid%C3%AAncia"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:41Z"
rotulos: ["ISS", "Configuração", "Impostos", "Financeiro", "Prefeituras", "NFS-e", "Exportação", "Alíquota de ISSQN", "Campo referente à tributação do ISSQN", "Imunidade", "Não incidência", "imunidade exportação ou não incidência"]
---

# E0602 Rejeição: Não é permitido informar alíquota quando o campo referente à tributação do ISSQN indicar imunidade, exportação ou não incidência.

**MENSAGEM**

E0602 Rejeição: Não é permitido informar alíquota quando o campo referente à tributação do ISSQN indicar imunidade, exportação ou não incidência.

**SITUAÇÃO**

Ao emitir uma NFS-e, a nota é rejeitada com a mensagem E0602, indicando que **foi informada uma alíquota de ISSQN** em uma operação que possui código de tributação configurado como **imunidade, exportação ou não incidência**, situações nas quais não deve haver cobrança do imposto.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse o cadastro de **"Serviços"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Localize o serviço utilizado na nota fiscal rejeitada.

**(3)** Na aba **"Impostos"**, verifique o campo **"Cód. Trib. Município NFS-e"** e identifique qual código de tributação está configurado.

**(4)** Caso o **código de tributação** informado seja referente a **imunidade** (códigos **4, 5, 9, 29 ou C**), **exportação** (código **4**) ou **não incidência** (códigos **2, 7 ou E**), certifique-se de que **não exista alíquota de ISSQN informada**, tanto no **cadastro do serviço** quanto na **operação** utilizada.

**(4)** Acesse a tela [**"Tipo de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) utilizado na emissão da nota fiscal.

**(5)** Na aba **"NFS-e"**, verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"** e confirme se está configurado corretamente conforme a natureza da operação:

- **''2 - Não incidência''**
- **''3 - Isenção''**
- **''4 - Exportação''**
- **''5 - Imunidade''**

**(6)** Remova qualquer **alíquota de ISSQN** que esteja preenchida no cadastro do serviço ou na configuração da operação quando a tributação indicar imunidade, exportação ou não incidência.

**(7)** Salve as alterações realizadas e **emita novamente a NFS-e**.

**CAUSA**

A rejeição ocorre porque **foi informada uma alíquota de ISSQN** em uma operação cujo código de tributação indica **imunidade, exportação ou não incidência**. Nessas situações, **não deve haver cobrança do imposto**, portanto, a presença de uma alíquota configurada gera inconsistência e a Prefeitura rejeita a nota fiscal eletrônica.
