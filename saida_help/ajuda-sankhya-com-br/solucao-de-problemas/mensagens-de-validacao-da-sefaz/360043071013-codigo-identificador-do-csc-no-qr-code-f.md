---
id: "360043071013"
titulo: "Código Identificador do CSC no QR-Code foi revogado pela empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043071013-C%C3%B3digo-Identificador-do-CSC-no-QR-Code-foi-revogado-pela-empresa"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:58Z"
rotulos: ["ERRONF", "Configuração", "SEFAZ", "463", "Configure o Token", "CSC revogado", "Emita NFC-e novamente", "Detalhe do erro", "Erro"]
---

# Código Identificador do CSC no QR-Code foi revogado pela empresa

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16459596233879) MENSAGEM:**

[463 - Rejeição]: Código Identificador do CSC no QR-Code foi revogado pela empresa.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16459596242199) SOLUÇÃO:**

Para correção, siga os passos abaixo.

![Imagem 3: Confira as configurações para geração do Token em ' Comercial » Preferências » Empresa '](https://ajuda.sankhya.com.br/hc/article_attachments/16459563929239) Confira as configurações para geração do Token em 'Comercial » Preferências » Empresa' 

Aba**: "NF-e/NFC-e"**, campos:

- **"Sequencial do TOKEN NFC-e"**
- **"Token NFC-e"**

![Imagem 4: "Token NFC-e"](https://ajuda.sankhya.com.br/hc/article_attachments/14473670599191)

Os dados dos dois campos acima são fornecidos pela equipe Fiscal/Contábil da empresa. Junto a SEFAZ do Estado se faz o cadastro e são fornecidos o TOKEN(CSC) e o sequencial do TOKEN(ID).

![Imagem 5: Após o preenchimento dos campos com os valores corretos, gere o lote novamente da NFC-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16459596247703) Após o preenchimento dos campos com os valores corretos, gere o lote novamente da NFC-e.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16459596254231) CAUSA:**

Quando for emitida uma NFC-e com CSC (Token) revogado (desativado) pela empresa emitente em data menor que a data de emissão da NFC-e, será retornado a rejeição.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16459596256919) OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=v9JbkEY7evI=)) - Nota técnica.
