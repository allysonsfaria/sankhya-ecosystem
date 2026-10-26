---
id: "36076049422743"
titulo: "1001 Rejeição: NF-e com finalidade de débito ou crédito somente para IBS/CBS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36076049422743-1001-Rejei%C3%A7%C3%A3o-NF-e-com-finalidade-de-d%C3%A9bito-ou-cr%C3%A9dito-somente-para-IBS-CBS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-08T15:05:50Z"
rotulos: ["NF-e", "SEFAZ", "Crédito", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "1001 Rejeição", "Rejeição 1001", "NF-e com finalidade de débito ou crédito somente para IBS/CBS", "IBS", "CBS", "Artigo atualizado KCS", "IBS/CBS", "Finalidade da NF-e", "Docs Eletrônicos - KCS"]
---

# 1001 Rejeição: NF-e com finalidade de débito ou crédito somente para IBS/CBS

**MENSAGEM**

1001 Rejeição: NF-e com finalidade de débito ou crédito somente para IBS/CBS

**SITUAÇÃO**

A mensagem de erro é apresentada ao tentar transmitir uma NF-e cuja **"Finalidade da NF-e"** está definida como **"Débito"** ou **"Crédito"** (finNFe=5 ou 6), porém há impostos informados nos itens da nota. O erro pode ocorrer tanto na emissão manual quanto na importação do XML da NF-e.

**SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

**(1)** Acesse a tela **"Central de Compras"** (Comercial >> Rotinas >> Central de Compras) e/ou **"Central de Vendas"** (Comercial >> Rotinas >> Central de Vendas).

**(2)** Localize e selecione a nota fiscal que apresentou a rejeição.

**(3)** Na grade **"Cabeçalho"**, verifique o campo **"Tipo Operação"** e identifique a TOP usada na nota.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) e selecione a TOP identificada.

**(5)** Na aba **"NF-e/NFC-e/CF-e"**, verifique o campo **"NF-e"**.

- Se estiverem selecionadas as opções **"Crédito"** ou **"Débito"**, siga as ações abaixo:

**(6)** Retorne à nota que recebeu a rejeição, e confira se nos itens ou na aba **"Impostos"** está informado algum dos seguintes impostos:

- **ICMS**
- **IPI**
- **PIS**
- **COFINS**
- **ISSQN**
- **II**
- **ICMS UF Destino**
- **Imposto Devolvido**
- **PIS ST**
- **COFINS ST**

**(7)** Corrija a nota fiscal:

**Se a nota foi gerada manualmente:**

- Remova todos os impostos citados dos itens da nota;
- Mantenha apenas **IBS/CBS**, se aplicável;
- Salve e gere novamente o XML.

**Se a nota foi importada via XML:**

- Edite o XML antes de importar;
- Remova as tags de impostos: <ICMS>, <IPI>, <PIS>, <COFINS>, <ISSQN>, <II>, <ICMSUFDest>, <impostoDevol>, <PISST>, <COFINSST>;
- Mantenha apenas as tags de **IBS/CBS**, se existirem.

**(8)**  Após corrigir a nota, transmita novamente para a Sefaz.

**(9)** Verifique se a rejeição foi solucionada.

**IMPORTANTE**: Se não for uma operação de IBS/CBS, não utilize as finalidades **Débito** ou **Crédito**. Se for, garanta que apenas **IBS/CBS** está informado.

**CAUSA**

A rejeição ocorre porque, conforme a **"Nota Técnica 2025.002 – v1.10"**, as NF-e com finalidade de débito ou crédito (finNFe = 5 ou 6) devem conter exclusivamente informações dos tributos IBS e CBS, não sendo permitido informar os tributos do regime anterior (ICMS, IPI, PIS, COFINS, ISSQN, entre outros).
