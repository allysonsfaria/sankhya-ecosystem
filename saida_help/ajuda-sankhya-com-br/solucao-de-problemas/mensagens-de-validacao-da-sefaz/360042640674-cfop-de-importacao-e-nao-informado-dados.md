---
id: "360042640674"
titulo: "CFOP de Importação e não informado dados da DI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042640674-CFOP-de-Importa%C3%A7%C3%A3o-e-n%C3%A3o-informado-dados-da-DI"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:39Z"
rotulos: ["ERRONF", "NF-e", "Importação", "SEFAZ", "CFOP", "525", "CFOP importação sem DI", "NF-e exterior sem dados DI", "Marcar importação e preencher DI", "Erro", "DI"]
---

# CFOP de Importação e não informado dados da DI

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16505113249815) MENSAGEM:**

[525 - Rejeição]: CFOP de Importação e não informado dados da DI.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16505142746007) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16505113254295) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Aba: **"Geral"**
- Campo **"Digitar informações sobre Importação":** marque

![Imagem 4: Acesse: Portal Compras » Central de Notas.](https://ajuda.sankhya.com.br/hc/article_attachments/16505113255191) Acesse: Portal Compras » Central de Notas.

Para cada item da nota, preencha os dados da **"DI-Declaração de Importação".**

Selecione o item e depois o  botão: **"Outras Opções"**(...)>>**"Declaração de Importação e Adições":**

![Imagem 5: Selecione o item e depois o botão: "Outras Opções" (...)>> "Declaração de Importação e Adições":](https://ajuda.sankhya.com.br/hc/article_attachments/12118200066583)

![Imagem 6: Após os ajustes, gere o lote da nota novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16505142755479) Após os ajustes, gere o lote da nota novamente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16505113259927) CAUSA:**

Quando for emitida uma NF-e com CFOP iniciado por 3, indicando uma Operação com o Exterior, de Entrada, e não for informado o Grupo de Declaração de Importação (DI), será retornada a rejeição "525 - CFOP de Importação e não informado dados da DI".

Exceções a regra:

A regra 525 não se aplica para os seguintes CFOP: 3.201, 3.202, 3.211, 3.503 e 3.553.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16505113262871) OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte:](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)
