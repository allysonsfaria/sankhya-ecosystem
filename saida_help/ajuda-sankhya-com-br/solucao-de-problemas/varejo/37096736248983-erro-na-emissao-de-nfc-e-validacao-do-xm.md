---
id: "37096736248983"
titulo: "Erro na emissão de NFC-e – Validação do XML (xNome)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096736248983-Erro-na-emiss%C3%A3o-de-NFC-e-Valida%C3%A7%C3%A3o-do-XML-xNome"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T14:21:11Z"
rotulos: ["Configuração", "Parceiro", "XML", "SEFAZ", "NFC-e", "Erro", "Emissão da NFC-e", "Validação do XML", "xNome", "Parceiro Consumidor Final Não Contribuinte não identificado", "Parceiro padrão da NFC-e", "PDV-Web"]
---

# Erro na emissão de NFC-e – Validação do XML (xNome)

**MENSAGEM:**

**Erro durante validação do XML do lote:**
Erro durante validação do XML do lote: cvc-complex-type.2.4.a: Invalid content was found starting with element '{"http://www.portalfiscal.inf.br/nfe":xNome}'. One of '{"http://www.portalfiscal.inf.br/nfe":CNPJ, "http://www.portalfiscal.inf.br/nfe":CPF, "http://www.portalfiscal.inf.br/nfe":idEstrangeiro}' is expected.

**SITUAÇÃO:**

Ao realizar uma venda no **PDV Web** para um **Parceiro Consumidor Final Não Contribuinte não identificado**, diferente do parceiro informado na tela [**“Empresa”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (caminho: **Comercial » Preferências » Empresa**), aba **“NF-e/NFC-e”**, sub-aba **“NFC-e”**, no campo **“Parceiro padrão da NFC-e”**, o sistema apresenta o erro mencionado acima durante a validação do XML do lote.

**SOLUÇÃO:**

Para resolver o problema, existem duas alternativas:

**(1)** Acesse a tela ''Empresa'' (Comercial » Preferências » Empresa), aba “NF-e/NFC-e”, sub-aba “NFC-e”, no campo “Parceiro padrão da NFC-e”, para manter o parceiro configurado corretamente.

**(2)** No **PDV Web**, utilize o botão **“Identificar”** e informe o **CPF ou CNPJ do adquirente** no campo correspondente.

**OBSERVAÇÃO:** Essas informações são utilizadas exclusivamente para a emissão da NFC-e, **sem alterar o Parceiro padrão** configurado no sistema.

**CAUSA:**

Esse erro ocorre porque, para a **NFC-e**, a **SEFAZ** exige coerência entre a identificação do parceiro e os dados informados no XML.

Durante a venda, é utilizaddo um parceiro que não corresponde ao **Parceiro padrão da NFC-e** e que está configurado como não identificado, o sistema não consegue montar corretamente os campos obrigatórios do XML (CPF, CNPJ ou identificação estrangeira). Como consequência, o XML é rejeitado durante a validação.
