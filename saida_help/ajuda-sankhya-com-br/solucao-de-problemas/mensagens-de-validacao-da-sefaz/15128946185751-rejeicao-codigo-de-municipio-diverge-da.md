---
id: "15128946185751"
titulo: "Rejeição: Código de Município diverge da UF de descarga do MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15128946185751-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-Munic%C3%ADpio-diverge-da-UF-de-descarga-do-MDF-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-08-06T17:29:52Z"
rotulos: ["MDF-e", "Cidades", "SEFAZ", "Transporte", "Rejeição", "Rejeição: Código de Município Diverge da UF de Descarga do MDF-e", "Documentos Eletrônicos"]
---

# Rejeição: Código de Município diverge da UF de descarga do MDF-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16969208057111) MENSAGEM:**

Rejeição: Código de Município diverge da UF de descarga do MDF-e.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16969208060055) SOLUÇÃO:**

Verifique o valor do campo **"UFFim"** e os valores do campo **"cMunDescarga"** dentro do grupo infMunDescarga. Para o(s) campo(s) cMunDescarga veja se as 2 posições da esquerda do código do município de descarregamento que identifica o código da UF de descarga estão de acordo com o que foi informado no campo UFFim.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16969197137047) CAUSA:**

Ocorre ao gerar MDF-e com UF de descarga divergente da UF de carga.
