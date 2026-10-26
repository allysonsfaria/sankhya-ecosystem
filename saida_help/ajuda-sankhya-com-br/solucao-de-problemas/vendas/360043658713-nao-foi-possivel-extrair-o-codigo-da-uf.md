---
id: "360043658713"
titulo: "Não foi possível extrair o código da UF do XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043658713-N%C3%A3o-foi-poss%C3%ADvel-extrair-o-c%C3%B3digo-da-UF-do-XML"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:26Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "Corrija e retransmita a NF-e", "Erro ao extrair código da UF", "Verifique o Código IBGE em \"Endereços\"", "Erro"]
---

# Não foi possível extrair o código da UF do XML

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16453823320087) MENSAGEM:**

Erro no Serviço "Consulta do Status do Serviço".

Erros encontrados:

Não foi possível extrair o código da UF do xml.

erro.handshake=true

erro.interno.uf.invalida=true

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453823322903) SITUAÇÃO:**

No sistema MGE/Mitra, ao tentar transmitir uma NF-e, o sistema retorna a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453839969175) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 4: Acesse MGE/Mitra » Arquivos » Cadastros » Endereços »UF's](https://ajuda.sankhya.com.br/hc/article_attachments/16453839974167) Acesse MGE/Mitra » Arquivos » Cadastros » Endereços »UF's

- Campo '**Código IBGE':** informe um valor válido
- Para consultar, recomendamos o site do IBGE, ou solicitar informações com o contador da empresa.
  <https://www.ibge.gov.br/>

![Imagem 5: Após o ajuste, transmita novamente a NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16453839977751) Após o ajuste, transmita novamente a NF-e.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16453823337367) CAUSA:**

Ocorre quando no cadastro da UF não foi informado um valor válido para o campo Código IBGE.
