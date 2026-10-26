---
id: "360044232193"
titulo: "Indicativo de recolhimento FGTS na GRRF deve ser informado para código de movimentação I1, I2, I3, I4, I5 OU L. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044232193-Indicativo-de-recolhimento-FGTS-na-GRRF-deve-ser-informado-para-c%C3%B3digo-de-movimenta%C3%A7%C3%A3o-I1-I2-I3-I4-I5-OU-L-Como-resolver"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:21:38Z"
rotulos: ["#RevisadoLorrana", "Configuração", "Atualização", "Impostos", "SEFIP", "320625", "GRRF", "FGTS incorreto GRRF", "Atualize leiaute SEFIP", "Indicativo FGTS ausente", "FGTS"]
---

# Indicativo de recolhimento FGTS na GRRF deve ser informado para código de movimentação I1, I2, I3, I4, I5 OU L. Como resolver?

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17290488989463) MENSAGEM:**

320625 - Indicativo de recolhimento FGTS na GRRF deve ser informado para código de movimentação I1, I2, I3, I4, I5 OU L.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17290517099031) SITUAÇÃO:**

Mensagem apresentada na geração do arquivo SEFIP.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17290489012887) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Atualize o leiaute utilizado na transmissão do SEFIP, visto que esse contemplará na fórmula do registro 32 -…](https://ajuda.sankhya.com.br/hc/article_attachments/17290489016599) Atualize o leiaute utilizado na transmissão do SEFIP, visto que esse contemplará na fórmula do registro 32 - movimentação do trabalhador - Sequência 12, as devidas informações referentes ao novo código de afastamento I5 para rescisão de mutuo acordo.

![Imagem 5: Atualizado o leiaute, gere um novo arquivo SEFIP.](https://ajuda.sankhya.com.br/hc/article_attachments/17290489021591) Atualizado o leiaute, gere um novo arquivo SEFIP.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17290489029271) IMPORTANTE:**

É possível localizar o layout padrão no ['Sankhya Place'](http://portal.sankhya.com.br/#/downloads/listararquivos/id/267).

Dúvidas de como atualizar o Layout acesse esse artigo: [Como baixar e importar Layout's](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043729794)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17290489036439) CAUSA:**

Mensagem será apresentada ao transmitir o arquivo SEFIP quando não informado o indicativo de Recolhimento FGTS na GRFC para Código de Movimentação I1, I2, I3, I4 ou L.
Solução: Preencher o campo com 'S' ou 's' ou ?N? ou ?n? Regra: Obrigatório para códigos de movimentação I1, I2, I3, I4 ou L.
Registro 32 - Posição: 134
