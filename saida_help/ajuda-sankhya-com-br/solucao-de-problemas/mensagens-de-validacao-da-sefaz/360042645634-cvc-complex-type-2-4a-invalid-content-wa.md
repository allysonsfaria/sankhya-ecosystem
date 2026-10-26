---
id: "360042645634"
titulo: "cvc-complex-type.2.4a: Invalid content was found starting with element 'xCpl' of {\"http://www.portalfiscal,inf.br\": nro} is expected"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042645634-cvc-complex-type-2-4a-Invalid-content-was-found-starting-with-element-xCpl-of-http-www-portalfiscal-inf-br-nro-is-expected"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:16Z"
rotulos: ["ERRONF", "ERROMDFE", "#RevisadoBraga", "MDF-e", "Configuração", "Parceiro", "NF-e", "SEFAZ", "Ajuste o campo Complemento", "Verifique número e complemento", "Redigite e gere novo lote", "Erro"]
---

# cvc-complex-type.2.4a: Invalid content was found starting with element 'xCpl' of {"http://www.portalfiscal,inf.br": nro} is expected

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16486166792855) MENSAGEM:**

cvc-complex-type.2.4a: Invalid content was found starting with element **'xCpl'** of {"http://www.portalfiscal,inf.br": **nro**} is expected.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16486166795671) SOLUÇÃO:**

Para correção, siga os passos abaixo:

Temos o campo Complemento nos seguintes locais.

![Imagem 3: Acesse: Configurações » Cadastros » Empresas (Emitente da NF-e/NFC-e/MDF-e)](https://ajuda.sankhya.com.br/hc/article_attachments/16486128097303) Acesse: Configurações » Cadastros » Empresas [Emitente da NF-e/NFC-e/MDF-e]

- Aba: **"Endereço"** - Campo **"Complemento"**

![Imagem 4: Configurações » Cadastros » Parceiros (Destinatário da NF-e/NFC-e/MDF-e)](https://ajuda.sankhya.com.br/hc/article_attachments/16486166803863) Configurações » Cadastros » Parceiros [Destinatário da NF-e/NFC-e/MDF-e]

- Aba: **"Endereço"** - Campo "**Complemento"**  ou Aba: **"Endereço"** de Entrega - Campo: **"Complemento entrega"**

![Imagem 5: Efetue os ajustes no que se refere ao campo de 'Número' e 'Complemento', verifique os caracteres, espaço em branco ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16486128112535) Efetue os ajustes no que se refere ao campo de 'Número' e 'Complemento', verifique os caracteres, espaço em branco ou valor não declarado no campo número.

![Imagem 6: Após efetuar os ajustes, redigite o campo 'parceiro' do cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16486166808215) Após efetuar os ajustes, redigite o campo 'parceiro' do cabeçalho da nota e gere um novo lote.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16486128118807) CAUSA:**

Ocorre quando o campo 'Complemento' do cadastro de endereço do Emitente ou Destinatário, possui uma informação/carácter invalido ou informação que a sefaz não aceite que seja declarado neste campo.

Exemplos de valores no campo que a Sefaz rejeita:

**<xCpl>**ANTONIO (43) 99101-6112**</xCpl>** [Valor declarado como numero o telefônico]

**<xCpl>** **</xCpl>** [Espaço em branco, geralmente um 'tab' ao cadastrar o complemento.]

**<xCpl>**BOX 38/39 , Camelodromo**</xCpl>** [Virgula não aceita]

**<xCpl>**QD 35  LT 5**</xCpl>** [Declarar um valor na tag xCpl e não declarar na tag Numero <nro> a informação SN ou 0(zero)]
