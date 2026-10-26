---
id: "360043196533"
titulo: "Dígito Verificador da Chave de Acesso da NF-e Referenciada inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043196533-D%C3%ADgito-Verificador-da-Chave-de-Acesso-da-NF-e-Referenciada-inv%C3%A1lido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:47Z"
rotulos: ["ERRONF", "#criadoRoger", "#RevisadoBraga", "NF-e", "SEFAZ", "547", "Rejeição: dígito inválido", "Correção chave NF-e", "Verifique e ajuste", "Erro", "Documentos Eletrônicos", "Rejeição SEFAZ"]
---

# Dígito Verificador da Chave de Acesso da NF-e Referenciada inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16512793321751) MENSAGEM:**

[547 - Rejeição]: Dígito Verificador da Chave de Acesso da NF-e Referenciada inválido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16512800614551) SOLUÇÃO:**

Para correção, siga os passos abaixo:

Para conseguir aprovar a NF-e de Devolução, informe a chave correta na nota de origem ou no campo: **"Chave NF-e Referenciada"**.

![Imagem 3: Selecione a NF-e de Venda(Origem) e confira a chave - Caso a chave esta correta.](https://ajuda.sankhya.com.br/hc/article_attachments/16512793328663) Selecione a NF-e de Venda(Origem) e confira a chave - Caso a chave esta correta.

![Imagem 4: Acesse a NF-e de Devolução e busque pelo campo "Chave NF-e Referenciada" - Identifique se a chave esta correta.](https://ajuda.sankhya.com.br/hc/article_attachments/16512800624535) Acesse a NF-e de Devolução e busque pelo campo **"Chave NF-e Referenciada"** - Identifique se a chave esta correta.

- Se a nota de devolução está sendo feita de forma Manual, informe a chave da nota referenciada corretamente.
- Se a nota de devolução foi feita a partir da Nota de Origem(Venda), a chave referenciada será populada automaticamente e deverá estar correta também.

![Imagem 5: Após os ajustes, gere o lote da NF-e de devolução novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16512800626839) Após os ajustes, gere o lote da NF-e de devolução novamente.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16512793336215) CAUSA:**

Ocorre quando foi emitido uma Nota Fiscal Eletrônica onde referenciou um ou mais documento(s) de origem, seja manualmente ou de forma automática. Onde o documento referenciado possui a chave de acesso com o dígito verificador inválido.
