---
id: "35379135676567"
titulo: "741 Rejeição: O contratante deve ser igual ao emitente do MDFe quando indicado proprietário do veículo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35379135676567-741-Rejei%C3%A7%C3%A3o-O-contratante-deve-ser-igual-ao-emitente-do-MDFe-quando-indicado-propriet%C3%A1rio-do-ve%C3%ADculo"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:25:16Z"
rotulos: ["ERROMDFE", "MDF-e", "Configuração", "Parceiro", "SEFAZ", "quando indicado proprietário do veículo", "Contratante", "741 Rejeição", "O contratante deve ser igual ao emitente do MDFe", "Documentos Eletrônicos"]
---

# 741 Rejeição: O contratante deve ser igual ao emitente do MDFe quando indicado proprietário do veículo

**MENSAGEM**

741 Rejeição: O contratante deve ser igual ao emitente do MDFe quando indicado proprietário do veículo

**SITUAÇÃO**

Ao emitir um MDF-e, ao informar o proprietário ou possuidor do veículo, mas não preencher o grupo **"Contratante"** ou, se preenchido, não corresponder ao mesmo CNPJ/CPF do emitente, ocorre a rejeição **"741"**.

**SOLUÇÃO**

**(1)**  Acesse a tela **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)), va até a aba **"MDF-e",** sub aba **"Contratantes".**

**(2)**  Verifique se o grupo **"Contratante"** está preenchido.

![Imagem 1: (2) Verifique se o grupo "Contratante" está preenchido.](https://ajuda.sankhya.com.br/hc/article_attachments/35379327315863)

**(3)**  Se o grupo **"Contratante"** estiver preenchido, confira se os dados informados correspondem ao mesmo CNPJ/CPF do emitente do MDF-e.

**(4)**  Se necessário, ajuste os dados do **"Contratante"** para que estejam corretos e correspondam ao emitente.

**(5)**  Salve as alterações e tente emitir novamente o MDF-e.

**CAUSA**

A rejeição **"741"** ocorre devido à validação implementada na NT 2021.002. Quando o proprietário do veículo for informado, se for Pessoa Jurídica, o campo **"Contratante"** deve ser preenchido com o mesmo parceiro. Se o proprietário for Pessoa Física, o **"Contratante"** deve ser preenchido como a empresa emitente.
