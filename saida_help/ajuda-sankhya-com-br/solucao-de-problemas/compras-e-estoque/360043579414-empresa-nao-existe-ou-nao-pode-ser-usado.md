---
id: "360043579414"
titulo: "Empresa não existe ou não pode ser usado aqui: PK[X]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579414-Empresa-n%C3%A3o-existe-ou-n%C3%A3o-pode-ser-usado-aqui-PK-X"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:31Z"
rotulos: ["Configuração", "NF-e", "XML", "Preferências", "MD-e", "Consulta de Documentos", "Configuração da Empresa", "Erro", "Documentos Eletrônicos"]
---

# Empresa não existe ou não pode ser usado aqui: PK[X]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16106044751511) MENSAGEM:**

Empresa não existe ou não pode ser usado aqui: PK[X]

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16106014402839) SITUAÇÃO:**

Ao tentar consultar documentos pela rotina **"[Configuração MD-e/DF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599234-Configura%C3%A7%C3%A3o-MD-e-DF-e)"** apresenta o erro.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16106014404119) SOLUÇÃO:**

Para correção, siga os passos abaixo:

**(1)** Acesse Comercial » Preferências » Empresa:

**(2)** Selecione a empresa que está configurada para utilizar a Rotina de MD-e/DF-e.

**(2)** Aba: **"NF-e/NFC-e"**

**(2)** Campo **"Utiliza distribuição de DF-e?":** Deve estar diferente de Não Utiliza

**(2)** Campo **"Versão NF-e/NFC-e":** Deve estar com a versão 'Versão NF-e e NFC-e 4.00'

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16106044758551) CAUSA:**

Ocorre quando a empresa que está recebendo os lotes de XML´s dos fornecedores não está devidamente configurada para utilizar a rotina.
