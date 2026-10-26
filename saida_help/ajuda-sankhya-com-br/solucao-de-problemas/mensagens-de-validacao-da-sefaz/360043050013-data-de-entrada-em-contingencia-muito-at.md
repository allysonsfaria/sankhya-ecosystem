---
id: "360043050013"
titulo: "Data de entrada em contingência muito atrasada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050013-Data-de-entrada-em-conting%C3%AAncia-muito-atrasada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:53Z"
rotulos: ["ERRONF", "#RevisadoBraga", "Configuração", "NF-e", "SEFAZ", "569", "Atualizar data e cadastrar contingência", "Contingência muito atrasada", "Atraso maior que 30 dias", "Erro", "Documentos Eletrônicos"]
---

# Data de entrada em contingência muito atrasada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16474027879831) MENSAGEM:**

[569-Rejeição]: Data de entrada em contingência muito atrasada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474024209943) SOLUÇÃO:**

Para correção, siga os passos abaixo:

Acesse a tela de "**Manutenção de contingência"** (Caminho de acesso: Comercial » Avançado » Manutenção de Contingência) e identifique a data de criação da contingência, que deve ser inferior a 30 dias, da data da NF-e.

Esta Rejeição ocorre também quando não há um registro de Manutenção de contingência cadastrada, então considere cadastrar.

Após o cadastro, gere o Lote da NF-e novamente.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16474024213399) CAUSA:**

Quando for emitida uma NF-e com Data/Hora de Entrada em Contingência com atraso maior que 30 dias da Data de Emissão será retornado a rejeição.
