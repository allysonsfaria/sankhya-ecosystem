---
id: "9320905546007"
titulo: "Você está tentando transformar um Lote Real em Lote Curinga mas o Nro. Lote XXX não está definido como Lote Curinga no Processo Produtivo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9320905546007-Voc%C3%AA-est%C3%A1-tentando-transformar-um-Lote-Real-em-Lote-Curinga-mas-o-Nro-Lote-XXX-n%C3%A3o-est%C3%A1-definido-como-Lote-Curinga-no-Processo-Produtivo"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T15:08:42Z"
rotulos: ["Produtos", "Configuração", "Lote", "Estoque", "PROD_E00186", "Lote real não pode virar curinga", "Erro ao alterar lote real para curinga", "Configure \"Número do Lote\" em \"Controle adicional\"", "Erro"]
---

# Você está tentando transformar um Lote Real em Lote Curinga mas o Nro. Lote XXX não está definido como Lote Curinga no Processo Produtivo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16700203389335) MENSAGEM:**

[PROD\_E00186]: Você está tentando transformar um Lote Real em Lote Curinga mas o Nro. Lote XXX não está definido como Lote Curinga no Processo Produtivo.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16700156005911) SITUAÇÃO:**

Ao tentar alterar o lote curinga para o lote real a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16700156009495) SOLUÇÃO:**

Acesse a tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), na aba **"Medidas e estoque"**, sub-aba **"Controle adicional",** informe o tipo de controle como: Número do Lote.

![Imagem 4: Acesse a tela "Produtos" (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) , na aba "Medidas e…](https://ajuda.sankhya.com.br/hc/article_attachments/16700203406743)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16700156019479) CAUSA:**

Ocorre quando o PA está configurado para não trabalhar com "**Controle de lote**" e na produção tenta realizar a alteração de lote real para lote curinga.
