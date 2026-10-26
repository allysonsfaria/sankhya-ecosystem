---
id: "37226188484375"
titulo: "E0533 Rejeição: Não é permitido informar Benefício Municipal (BM deve ser nulo) quando o serviço prestado diferente de Tributável (tribISSQN = 1), ou seja, tribISSQN = 2, 3 ou 4."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226188484375-E0533-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-Benef%C3%ADcio-Municipal-BM-deve-ser-nulo-quando-o-servi%C3%A7o-prestado-diferente-de-Tribut%C3%A1vel-tribISSQN-1-ou-seja-tribISSQN-2-3-ou-4"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:13Z"
rotulos: ["ISS", "Configuração", "SEFAZ", "Impostos", "TOP", "NFS-e", "Código de benefício municipal", "Serviço prestado diferente de Tributável", "Regime de tributação do ISS", "Não é permitido informar Benefício Municipal", "Tributável"]
---

# E0533 Rejeição: Não é permitido informar Benefício Municipal (BM deve ser nulo) quando o serviço prestado diferente de Tributável (tribISSQN = 1), ou seja, tribISSQN = 2, 3 ou 4.

**MENSAGEM**

E0533 Rejeição: Não é permitido informar Benefício Municipal (BM deve ser nulo) quando o serviço prestado diferente de Tributável (tribISSQN = 1), ou seja, tribISSQN = 2, 3 ou 4.

**SITUAÇÃO**

A **NFS-e** foi emitida com a informação de um **Benefício Municipal** associada a um serviço cujo r**egime de tributação do ISS** não está definido como tributável no documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa) e localize a empresa emissora da NFS-e.

**(2)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **"NFS-e"**, sub-aba **''Geral''**, verifique o campo **"Regime esp. tributação ISS (NFS-e)''** e identifique qual regime de tributação está configurado:

- Se o código for **2, 3 ou 4** (Exigibilidade Suspensa por Decisão Judicial, Exigibilidade Suspensa por Procedimento Administrativo ou Imune), **não é permitido informar benefício municipal**.
- Se o serviço realmente deve ser **tributável**, altere o código para **1 (Tributável)**.

**(3)** Caso o regime de tributação esteja correto como **2, 3 ou 4**, acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(4)** Localize o TOP utilizado na emissão da NFS-e e acesse a aba **"NFS-e"**.

**(5)** Verifique se há algum **código de benefício municipal** preenchido. Caso exista, **remova a informação** deste campo, deixando-o vazio.

**(6)** Salve as alterações realizadas.

**(7)** Emita novamente a NFS-e.

**OBSERVAÇÃO:** Consulte sempre o **contador responsável** ou a **legislação municipal** para confirmar qual é o regime de tributação correto para o serviço prestado e se há direito a benefício fiscal municipal.

**CAUSA**

A rejeição ocorre porque a **Sefaz valida** que o campo de **Benefício Municipal** só pode ser preenchido quando o serviço está configurado com o **regime de tributação "Tributável" (código 1)**. Quando o serviço possui outros regimes, como **Exigibilidade Suspensa por Decisão Judicial (código 2)**, **Exigibilidade Suspensa por Procedimento Administrativo (código 3)** ou **Imune (código 4)**, o sistema não permite que seja informado benefício municipal, pois **não há tributação efetiva do ISS** nessas situações. A informação indevida do benefício municipal gera inconsistência fiscal e, consequentemente, a rejeição da nota.
