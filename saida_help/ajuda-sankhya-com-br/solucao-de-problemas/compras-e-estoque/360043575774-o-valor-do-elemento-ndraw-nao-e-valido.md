---
id: "360043575774"
titulo: "O valor '  ' do elemento 'nDraw' não é válido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575774-O-valor-do-elemento-nDraw-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:19Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "Erro de Validação: Campo 'Nro.Ato Conc. regime DrawBack'", "Erro de Validação", "Confirmação de Notas", "Erro"]
---

# O valor '  ' do elemento 'nDraw' não é válido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16454505205399) MENSAGEM:**

cvc-pattern-valid: O valor ' ' nÃ£o tem um aspecto vÃ¡lido em relaÃ§Ã£o ao padrÃ£o '[0-9]{0,11}' do tipo '#AnonType\_nDrawadiDIproddetinfNFeTNFe'.
cvc-type.3.1.3: O valor '  ' do elemento 'nDraw' nÃ£o Ã© vÃ¡lido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454521646871) SITUAÇÃO:**

Mensagem retornada na confirmação de notas de importação/nacionalização.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454505212695) SOLUÇÃO:**

![Imagem 4: Acesse o respectivo lançamento na Central de Compras;](https://ajuda.sankhya.com.br/hc/article_attachments/16454521658007) Acesse o respectivo lançamento na Central de Compras;

![Imagem 5: Na grade de itens, para todos os produtos da nota, busque pela opção " Outras Opções" » 'Declaração de Importação e…](https://ajuda.sankhya.com.br/hc/article_attachments/16454505227415) Na grade de itens, para todos os produtos da nota, busque pela opção "**Outras Opções"** » **'Declaração de Importação e Adições'** e verifique as informações inseridas no campo **'Nro.Ato Conc. regime DrawBack':**

![Imagem 6: Na grade de itens, para todos os produtos da nota, busque pela opção " Outras Opções" » 'Declaração de Importação e…](https://ajuda.sankhya.com.br/hc/article_attachments/14400282953623)

![Imagem 7: Valide se a informação inserida é válida, caso negativo, realize o ajuste ou retire a informação conforme orientações…](https://ajuda.sankhya.com.br/hc/article_attachments/16454521667607) Valide se a informação inserida é válida, caso negativo, realize o ajuste ou retire a informação conforme orientações do contador.

![Imagem 8: Realizado os ajustes, teste uma nova emissão da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16454521671575) Realizado os ajustes, teste uma nova emissão da nota.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16454521673879) CAUSA:**

Mensagem apresentada quando enviada uma informação inconsistente para o campo 'Nro.Ato Conc. regime DrawBack'.
