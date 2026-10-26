---
id: "360043772434"
titulo: "Tipo de Transportador deve ser diferente de TAC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043772434-Tipo-de-Transportador-deve-ser-diferente-de-TAC"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:59:11Z"
rotulos: ["ERROMDFE", "#PUBLIFER", "#revisadohugo", "MDF-e", "SEFAZ", "Transporte", "457", "Tipo de Transportador Inválido para TAC", "Erro", "RNTRC", "Documentos Eletrônicos"]
---

# Tipo de Transportador deve ser diferente de TAC

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16201309540119) MENSAGEM:**

457 - Rejeição: Tipo de Transportador deve ser diferente de TAC.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201309544215) SITUAÇÃO:**

Mensagem apresentada na geração do MDF-e.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201331640855) SOLUÇÃO:**

Quando a carga é própria e o dono do veículo terceiros:

- Informe CNPJ do proprietário do veículo [esse deve ser diferente do CNPJ do emitente do MDF-e];
- Preencha corretamente o RNTRC;
- A opção **"Veículo da EMPRESA"**, no cadastro do veículo, deve estar DESMARCADA.

Caso seja um veículo próprio:

- Opção Veículo da EMPRESA, no cadastro do veículo, deve estar MARCADA:

![Imagem 4: Opção Veículo da EMPRESA , no cadastro do veículo, deve estar MARCADA:](https://ajuda.sankhya.com.br/hc/article_attachments/14663943345815)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16201331642263) CAUSA:**

Se tipo emitente informado for igual a Prestador de Serviço de Transporte (tpEmit=1), modal = Rodoviário e CNPJ do proprietário do veículo não for informado ou for igual ao CNPJ do Emitente do MDF-e: A informação do tipo de transportador (tpTransp) deverá ser diferente de TAC (2).
