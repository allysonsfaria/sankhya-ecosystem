---
id: "360044225413"
titulo: "Nenhum processo de produção encontrado para o produto Cód.Produto = \"XX\" na planta Cód.Planta = \"Y\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044225413-Nenhum-processo-de-produ%C3%A7%C3%A3o-encontrado-para-o-produto-C%C3%B3d-Produto-XX-na-planta-C%C3%B3d-Planta-Y"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T16:00:12Z"
rotulos: ["#PUBLIFER", "PROD_E00322", "Produtos", "Configuração", "Ordem de Serviço", "Produção", "Nenhum processo de produção encontrado para o produto", "Verifique planta e configuração de \"Planejamento por Controle\"", "Falta de processo correspondente aos dados de O.P", "Erro"]
---

# Nenhum processo de produção encontrado para o produto Cód.Produto = "XX" na planta Cód.Planta = "Y"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17292401371031) MENSAGEM:**

[PROD\_E00322]: Nenhum processo de produção encontrado para o produto Cód.Produto = "XX" na planta Cód.Planta = "Y".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17292429322391) SOLUÇÃO:**

![Imagem 3: Certifique-se que a planta de manufatura configurada para o respectivo processo produtivo é a mesma inserida no…](https://ajuda.sankhya.com.br/hc/article_attachments/17292429331735) Certifique-se que a planta de manufatura configurada para o respectivo processo produtivo é a mesma inserida no lançamento da O.P.

![Imagem 4: Caso sejam MP'S com controle por lista verifique se a opção "Planejamento por Controle" foi marcada para o respectivo…](https://ajuda.sankhya.com.br/hc/article_attachments/17292401401239) Caso sejam MP'S com controle por lista verifique se a opção **"Planejamento por Controle"** foi marcada para o respectivo produto:

Produção » Rotinas » Planejamento de Produção (MRP I) >> Conf. >> Aba Produtos >> 'Planejamento por Controle':

- **Planejamento por Controle:** quando marcado, significa que o cálculo de demanda do MPS irá considerar o controle do produto (controle adicional do tipo lista). Dessa forma, será gerado um registro de necessidade de produção para cada produto/controle. Essa configuração faz sentido apenas para produtos com controle adicional do tipo Lista.

![Imagem 5: Ainda referindo-se a situação de controle por lista, valide se não existem espaços em branco indevidos inseridos no…](https://ajuda.sankhya.com.br/hc/article_attachments/17292401410711) Ainda referindo-se a situação de controle por lista, valide se não existem espaços em branco indevidos inseridos no campo **"Controle"** das respectivas MP'S no processo produtivo.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17292429358103) CAUSA:**

Mensagem apresentada quando não localiza-se um processo de produção correspondente aos dados do lançamento de O.P realizado, tal como: Planta, Controle.
