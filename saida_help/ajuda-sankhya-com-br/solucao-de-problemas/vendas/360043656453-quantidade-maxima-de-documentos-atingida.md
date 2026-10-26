---
id: "360043656453"
titulo: "Quantidade máxima de documentos atingida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043656453-Quantidade-m%C3%A1xima-de-documentos-atingida"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:34Z"
rotulos: ["Configuração", "Portal de Vendas", "Documentos", "Preferências", "Quantidade máxima de documentos atingida", "Fechar e reabrir documentos após ajuste", "Ajustar parâmetro \"MAXCENTRAIS\" para mais documentos", "Erro"]
---

# Quantidade máxima de documentos atingida

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16134672991895) MENSAGEM:**

Quantidade máxima de documentos atingida.

A quantidade máxima de 10 documento(s) aberto(s) simultaneamente foi atingida. Selecione um documento para ser substituído.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16134691174679) SITUAÇÃO:**

Ao selecionar 10 ou mais documentos na tela de Portal de Vendas para devolução, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16134691178647) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16134672994327) Acesse: Configurações » Avançado » Preferências

**(2)** Pesquise pelo parâmetro: **"MAXCENTRAIS** **- Qtd. máx. de Centrais abertas"**: Altere o valor do campo Inteiro, pode aumentar para um valor considerável de acordo com a quantidade de documentos que costuma abrir na central.

![Imagem 5: (2) Pesquise pelo parâmetro: "MAXCENTRAIS - Qtd. máx. de Centrais abertas" : Altere o valor do campo Inteiro, pode…](https://ajuda.sankhya.com.br/hc/article_attachments/14633058457623)

![Imagem 6: Após o ajuste, feche a tela de Portal de Vendas e abra os documentos novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16134691180055) Após o ajuste, feche a tela de Portal de Vendas e abra os documentos novamente.

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17803866701207) IMPORTANTE:**

Quando a quantidade definida for 1 (um) registro o sistema irá substituir automaticamente o registro atual pelo anterior. Sendo que, se o registro atual possuir alterações, a seguinte mensagem será apresentada: "O registro atual foi alterado, deseja salvar as alterações?". Após a seleção, o novo documento será carregado na Central.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16134672998807) CAUSA:**

Ocorre quando a quantidade de notas aberta atingiu o limite estipulado pelo parâmetro MAXCENTRAIS, fazendo com que seja solicitado a troca de uma nota já aberta por outra que deseja abrir, então se faz necessário aumentar o valor do parâmetro.
