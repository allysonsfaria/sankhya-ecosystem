---
id: "360043128893"
titulo: "Seguro da carga é obrigatório para modal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043128893-Seguro-da-carga-%C3%A9-obrigat%C3%B3rio-para-modal"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:06Z"
rotulos: ["ERROMDFE", "MDF-e", "SEFAZ", "Transporte", "698", "Seguro da Carga Obrigatório para Modal", "Documentos Eletrônicos", "Seguro"]
---

# Seguro da carga é obrigatório para modal

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16447819076887) MENSAGEM:**

698-Rejeição: Seguro da carga é obrigatório para modal

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16447847272087) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Acesse " Viagens de Transporte (MDF-e)" (Caminho de acesso: Comercial » Rotinas » Viagens de Transporte (MDF-e):](https://ajuda.sankhya.com.br/hc/article_attachments/16447819083287) Acesse "**[Viagens de Transporte (MDF-e)"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514)** (Caminho de acesso: Comercial » Rotinas » Viagens de Transporte (MDF-e):

Aba: "**MDF-e"**, Sub-Aba: "**Seguro"**

- **"Nro. Apólice":** preencha este campo com Número da Apólice do seguro;
- **"Seguradora":** preencha com nome da Seguradora.

Sub-aba: "**Averbações**":

- **"Nro. Averbação":** preencha com Número da Averbação sobre o seguro.

![Imagem 4: "Nro. Averbação": preencha com Número da Averbação sobre o seguro.](https://ajuda.sankhya.com.br/hc/article_attachments/14387635069335)

![Imagem 5: Após os ajustes, gere o lote novamente do MDF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16447819088791) Após os ajustes, gere o lote novamente do MDF-e.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16447819089303) CAUSA:**

Ocorre quando no MDF-e 3.00 o valor informado na tag tpEmit = Tipo do Emitente, for igual a 1–Prestador de serviço de transporte e não tenha as informações da seguradora no grupo modal rodoviário.
