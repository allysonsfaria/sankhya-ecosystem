---
id: "24999521658647"
titulo: "Operação 'X' não configurada para emissão de NFSe"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24999521658647-Opera%C3%A7%C3%A3o-X-n%C3%A3o-configurada-para-emiss%C3%A3o-de-NFSe"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:46:19Z"
rotulos: ["Configuração", "TOP", "NFS-e", "CORE_E00506", "Erro"]
---

# Operação 'X' não configurada para emissão de NFSe

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24999511262359) **MENSAGEM:**

[CORE\_E00506] Operação 'X' não configurada para emissão de NFSe

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24999521651735)**SOLUÇÃO:**

Verifique se a TOP utilizada na nota é uma TOP para emissão de NFSe, se de fato essa é a intenção do lançamento. Pois, caso o campo **"NFS-e"** da TOP esteja como **"normal",** as demais configurações para esse tipo de emissão são necessárias.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24999511270935) **CAUSA:**

O erro é apresentado quando é usada uma TOP de NFS-e ao tentar emitir a nota fiscal, mas as demais configurações não foram feitas, ou quando o campo citado foi acionado por acidente.

**Mais informações sobre configurações de NFS-e clique [aqui.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047599473-Configura%C3%A7%C3%B5es-gerais-para-NFS-e#cadastrodetiposdeoperao-top)**
