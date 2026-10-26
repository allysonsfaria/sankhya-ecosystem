---
id: "360044089153"
titulo: "Esta nota não é de CT-e e o campo \"Cód.Cid.Início CT-e\" na aba Impostos não deve ser informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044089153-Esta-nota-n%C3%A3o-%C3%A9-de-CT-e-e-o-campo-C%C3%B3d-Cid-In%C3%ADcio-CT-e-na-aba-Impostos-n%C3%A3o-deve-ser-informado"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:35Z"
rotulos: ["CT-e", "Configuração", "SEFAZ", "Impostos", "TOP", "Lançamento de CT-e", "Central de Atendimento ao Fornecedor", "Modelo de Documento", "Documentos Eletrônicos"]
---

# Esta nota não é de CT-e e o campo "Cód.Cid.Início CT-e" na aba Impostos não deve ser informado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16168772785303) MENSAGEM:**

Esta nota não é de CT-e e o campo "Cód.Cid.Início CT-e" na aba Impostos não deve ser informado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16168789262615) SITUAÇÃO:**

Ao efetuar o lançamento de uma CT-e na Central de Atendimento ao Fornecedor, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16168789265815) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Arquivos » Cadastros » Tipos de Operação](https://ajuda.sankhya.com.br/hc/article_attachments/16168789267863) Acesse: Arquivos » Cadastros » Tipos de Operação

- Aba: **NF-/NFC-e**
- Campo **"Modelo de Documento":** Selecionar uma das opções: 57, 63 ou 67

![Imagem 5: Campo "Modelo de Documento": Selecionar uma das opções: 57, 63 ou 67](https://ajuda.sankhya.com.br/hc/article_attachments/14706829712919)

![Imagem 6: Após os ajustes, lance novamente uma nota CT-e e preencha os campos "Cód.Cid.Início CT-e" e "Cód.Cid.Fim CT-e".](https://ajuda.sankhya.com.br/hc/article_attachments/16168772794775) Após os ajustes, lance novamente uma nota CT-e e preencha os campos  **"Cód.Cid.Início CT-e"** e **"Cód.Cid.Fim CT-e".**

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16168789273623) CAUSA:**

Ocorre quando em uma nota de lançamento de CT-e (Conhecimento de Transporte Eletrônico), no qual exige o preenchimento do respectivo campo, o modelo de documento da TOP usada no lançamento esta diferente de 57, 63 ou 67.
