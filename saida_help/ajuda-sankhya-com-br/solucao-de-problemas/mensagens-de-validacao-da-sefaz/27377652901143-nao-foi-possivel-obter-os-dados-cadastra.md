---
id: "27377652901143"
titulo: "Não foi possível obter os dados cadastrais. STATUS: 239 MOTIVO: Rejeicao: Versão do arquivo XML nao suportada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27377652901143-N%C3%A3o-foi-poss%C3%ADvel-obter-os-dados-cadastrais-STATUS-239-MOTIVO-Rejeicao-Vers%C3%A3o-do-arquivo-XML-nao-suportada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:39:44Z"
rotulos: ["DUVIDANF", "Configuração", "NF-e", "XML", "SEFAZ", "VERCONSCADUF", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Rejeicao: Versao do arquivo XML nao suportada", "STATUS: 239", "Não foi possível obter os dados cadastrais", "Erro"]
---

# Não foi possível obter os dados cadastrais. STATUS: 239 MOTIVO: Rejeicao: Versão do arquivo XML nao suportada

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/27377667755415) **MENSAGEM:**

Não foi possível obter os dados cadastrais. STATUS: 239 MOTIVO: Rejeicao: Versão do arquivo XML nao suportada

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27377652883863)SOLUÇÃO:**

Verifique as informações do parâmetro "**VERCONSCADUF - Versão da NF-e utilizada para consulta de cadastro",** que determina o estado e a versão a ser utilizada na consulta cadastral.

Se houver uma versão informada para o estado que está consultando, retire o estado e a versão do parâmetro e realize uma nova consulta.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27377652885783)CAUSA:**

Normalmente ocorre para o estado do **Mato Grosso do Sul,** que pode estar com a informação **"MS=3.10"** informada no parâmetro. A versão 3.10 informada já não é mais suportada pelo estado, sendo necessário retirar a informação do parâmetro e realizar uma nova consulta.
