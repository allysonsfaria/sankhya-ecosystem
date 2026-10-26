---
id: "30589692603927"
titulo: "Modelo Estorno WMS - Dev. Compra não existe ou não pode ser usado aqui"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30589692603927-Modelo-Estorno-WMS-Dev-Compra-n%C3%A3o-existe-ou-n%C3%A3o-pode-ser-usado-aqui"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:35:29Z"
rotulos: ["Configuração", "WMS", "Estoque", "Preferências", "CORE_E01315", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Modelo Estorno WMS - Dev. Compra não existe ou não pode ser usado aqui", "Erro"]
---

# Modelo Estorno WMS - Dev. Compra não existe ou não pode ser usado aqui

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30589692595991) **MENSAGEM:**

[CORE\_E01315] Modelo Estorno WMS - Dev Compra não existe ou não pode ser usado aqui

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30589703697943)SOLUÇÃO:**

Acesse a tela **"Modelo de notas e pedidos"** (Comercial » Consulta » Modelo de Notas e Pedidos) e verifique se a empresa cadastrada no modelo é a mesma empresa que está sendo vinculada na tela Preferências da Empresa.
Caso não seja, inclua um novo modelo com a empresa correta e vincule este modelo dentro da tela Preferências da empresa.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30589703698583)CAUSA:**

Ocorre quando tentamos incluir um modelo de notas e pedidos com empresas diferentes.
