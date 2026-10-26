---
id: "360042725894"
titulo: "Operação com Exterior e país de destino igual a Brasil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042725894-Opera%C3%A7%C3%A3o-com-Exterior-e-pa%C3%ADs-de-destino-igual-a-Brasil"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:40Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "CFOP", "926", "Operação com Exterior e Destino Brasil", "Erro", "País"]
---

# Operação com Exterior e país de destino igual a Brasil

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16448513359767) MENSAGEM:**

[926 - Rejeição]: Operação com Exterior e país de destino igual a Brasil.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16448518271255) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: " Preferências " (Caminho de acesso: Configurações » Avançado » Preferências )](https://ajuda.sankhya.com.br/hc/article_attachments/16448513366039) Acesse: "**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Caminho de acesso: Configurações » Avançado » Preferências)

- Parâmetro "**CODPAISBRASIL"** = 55

![Imagem 4: Acesse: " Parceiros " (Caminho de acesso: Configurações » Cadastros » Parceiros )](https://ajuda.sankhya.com.br/hc/article_attachments/16448518278167) Acesse: "**[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho de acesso: Configurações » Cadastros » Parceiros)

- Aba: "**Endereço"**
- Campo "**Cód. Cidade"**: Verifique se está condizente a operação

![Imagem 5: Acesse: " Cidades " (Caminho de acesso: Configurações » Cadastros » Endereços » Cidades )](https://ajuda.sankhya.com.br/hc/article_attachments/16448518280727) Acesse: "[**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)" (Caminho de acesso: Configurações » Cadastros » Endereços » Cidades)

Verifique no cabeçalho da Cidade o campo "**Cód. UF"**, se este convém a operação realizada.

![Imagem 6: Após os ajustes, gere o lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16448518288791) Após os ajustes, gere o lote novamente.

![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16448513379223) **CAUSA:**

Quando emitida uma nota para o exterior (CFOP com iniciais 3 ou 7) e UF, tag<dest>/<UF>, igual a 1058 (Brasil).

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16448513381271) OBSERVAÇÃO:**

([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota Técnica.
