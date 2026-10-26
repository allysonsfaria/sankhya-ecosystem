---
id: "44011218140695"
titulo: "[TMS] - Importação de Ct-e  - Erro: A forma de negociação do pré-conhecimento não pode ser alterada de FOB para CIF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011218140695--TMS-Importa%C3%A7%C3%A3o-de-Ct-e-Erro-A-forma-de-negocia%C3%A7%C3%A3o-do-pr%C3%A9-conhecimento-n%C3%A3o-pode-ser-alterada-de-FOB-para-CIF"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T18:57:20Z"
rotulos: ["sync_hc", "lincros", "lincros_13439172", "sync_hash_4056be3350d8"]
---

# [TMS] - Importação de Ct-e  - Erro: A forma de negociação do pré-conhecimento não pode ser alterada de FOB para CIF

**Menu**: Documentos Eletrônicos > Ct-es

**Objetivo**: Como corrigir a mensagem de erro 'A forma de negociação do pré-conhecimento não pode ser alterada de FOB para CIF' ao fazer a importação do Ct-e.

## Considerações:

- Possuir nota fiscal com pré-conhecimento importados no sistema;

Ao fazer a importação do Ct-e é apresentando a seguinte mensagem: 'A forma de negociação do pré-conhecimento não pode ser alterada de FOB para CIF':

![Imagem 1: Ao fazer a importação do Ct-e é apresentando a seguinte mensagem: 'A forma de negociação do pré-conhecimento não pode…](https://ajuda.sankhya.com.br/hc/article_attachments/44011201634071)

Esta mensagem ocorre, pois a nota fiscal vinculada ao pré-conhecimento estão com a forma de negociação do frete diferente do que consta no Ct-e. Exemplo abaixo:

Pré-conhecimento vinculado a nota fiscal

![Imagem 2: Pré-conhecimento vinculado a nota fiscal](https://ajuda.sankhya.com.br/hc/article_attachments/44011201757207)

Ao baixar o XML da nota fiscal, verificar a tag 'Modfrete', conforme exemplo abaixo:

![Imagem 3: Ao baixar o XML da nota fiscal, verificar a tag 'Modfrete', conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44011155858455)

Neste caso, a modalidade do Frete está '1' = Contratação do Frete por conta do Destinatário (FOB).

Porém o Ct-e foi gerado com a negociação CIF e por este motivo ocorreu a divergência.

Verificar com o cliente qual vai ser a forma de negociação do Frete, já que na Nota fiscal consta como 'FOB' e no Ct-e 'CIF', caso considerar CIF, basta alterar a forma de negociação no pré-conhecimento.

Se for realmente FOB a transportadora deve gerar um novo XML.

  "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
