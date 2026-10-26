---
id: "360044225733"
titulo: "Valor unitário não pode ser menor que zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044225733-Valor-unit%C3%A1rio-n%C3%A3o-pode-ser-menor-que-zero"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T16:00:09Z"
rotulos: ["#PUBLIFER", "#revisadohugo", "Produtos", "Custos", "Configuração", "Produção", "CORE_E03241", "Valor unitário não pode ser menor que zero", "Custos negativos encontrados", "Ajuste os custos na \"Variação de Custos de Produtos\"", "Custos negativos identificados", "Erro"]
---

# Valor unitário não pode ser menor que zero

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17293097965463) MENSAGEM:**

[CORE\_E03241] Valor unitário não pode ser menor que zero.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17293126981655) SITUAÇÃO:**

Mensagem apresentada ao realizar o apontamento durante processo de produção.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17293097984663) SOLUÇÃO:**

![Imagem 4: Através da rotina "Variação de Custos de Produtos" (Caminho de acesso: Comercial » Consulta) verifique se existem…](https://ajuda.sankhya.com.br/hc/article_attachments/17293097993111) Através da rotina **"Variação de Custos de Produtos"** (Caminho de acesso: Comercial » Consulta) verifique se existem custos negativos relacionados a determinada MP.

![Imagem 5: Localizando o respectivo custo negativo, analise como os custos são calculados:](https://ajuda.sankhya.com.br/hc/article_attachments/17293098000663) Localizando o respectivo custo negativo, analise como os custos são calculados:

- por nota de entrada
- por tarifa CIP

![Imagem 6: Realize os devidos ajustes desse custo, assim será permitido o apontamento.](https://ajuda.sankhya.com.br/hc/article_attachments/17293127020695) Realize os devidos ajustes desse custo, assim será permitido o apontamento.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17293098023575) CAUSA:**

Mensagem apresentada quando identificado valores de custos negativos.
