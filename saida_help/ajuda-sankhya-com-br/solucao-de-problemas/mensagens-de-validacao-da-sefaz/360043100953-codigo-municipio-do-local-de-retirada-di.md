---
id: "360043100953"
titulo: "Código Município do Local de Retirada: difere da UF do Local de Retirada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043100953-C%C3%B3digo-Munic%C3%ADpio-do-Local-de-Retirada-difere-da-UF-do-Local-de-Retirada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:50Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "Cidades", "SEFAZ", "277", "Atualize cadastro", "Rejeição cód. município", "Verifique UF", "Erro"]
---

# Código Município do Local de Retirada: difere da UF do Local de Retirada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16444112798871) MENSAGEM:**

[277-Rejeição]: Código Município do Local de Retirada: difere da UF do Local de Retirada

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16444076626967) SOLUÇÃO:**

Informe um Município que corresponda ao Estado identificado pela UF informada.

![Imagem 3: Certifique-se que a 'UF' vinculada para as cidades envolvidas nesse lançamento encontra-se correta.](https://ajuda.sankhya.com.br/hc/article_attachments/16444076628119) Certifique-se que a 'UF' vinculada para as cidades envolvidas nesse lançamento encontra-se correta.

Acesse a tela "[Cidades"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913) (Caminho de acesso: Configurações » Cadastros » Endereços) e revise os campos abaixo:

(2)**"Cód. UF"**

(2)**"Mun. domicílio fiscal"**

![Imagem 4: Realizado algum ajuste, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16444112803095) Realizado algum ajuste, redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16444076633239) CAUSA:**

Quando emitido uma NF-e informando o local de retirada localizado no Brasil, e os dois primeiros dígitos do Código do Município (cMun) for diferente do Código da UF correspondente a sigla da UF informada, será retornada a rejeição.
