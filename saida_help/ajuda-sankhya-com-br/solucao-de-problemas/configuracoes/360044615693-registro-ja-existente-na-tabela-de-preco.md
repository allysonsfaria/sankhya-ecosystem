---
id: "360044615693"
titulo: "Registro já existente na Tabela de Preços para esta Data de Vigor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615693-Registro-j%C3%A1-existente-na-Tabela-de-Pre%C3%A7os-para-esta-Data-de-Vigor"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:52Z"
rotulos: ["CORE_E01698", "Atualização", "Financeiro", "Registro Duplicado na Tabela de Preços", "Erro", "Tabela de Preços"]
---

# Registro já existente na Tabela de Preços para esta Data de Vigor

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16618221347863) MENSAGEM:**

[CORE\_E01698]:  Registro já existente na Tabela de Preços para esta Data de Vigor.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16618182800023) SOLUÇÃO:**

Valide se já existe **preço** para a Dt.Vigor/Tabela do item que a atualização está sendo realizada;

(1)** CASO DE USO:**

![Imagem 3: Acesse a tela "Atualização de preço de venda" para atualização de preço do produto 16.](https://ajuda.sankhya.com.br/hc/article_attachments/16618221354391) Acesse a tela **"Atualização de preço de venda"** para atualização de preço do produto 16.

- Criado filtro Excecao.CODPROD = 16;
- Defina Data de Vigor (08/01/2019) e Data de atualização (08/01/2019);
- Ao aplicar, clique em **novo** e insira um novo preço para esse produto;
- Apresentada mensagem de erro: Registro já existente na Tabela de Preços para esta Data de Vigor;

(2)** MOTIVO:**

![Imagem 4: Ao filtrar o produto 16, definir a data de vigor e aplicar, já existe um registro de preço para esse produto na Data de…](https://ajuda.sankhya.com.br/hc/article_attachments/16618221367959) Ao filtrar o produto 16, definir a data de vigor e aplicar, já existe um registro de preço para esse produto na Data de Vigor 08/01/2019, dessa forma uma nova inserção não é aceita:

![Imagem 5: Ao filtrar o produto 16, definir a data de vigor e aplicar, já existe um registro de preço para esse produto na Data de…](https://ajuda.sankhya.com.br/hc/article_attachments/14874209616791)

![Imagem 6: Se o novo preço for vigorar em data posterior, ajuste a Data de Vigor do filtro apresentado na tela e, após isso,…](https://ajuda.sankhya.com.br/hc/article_attachments/16618182810903) Se o novo preço for vigorar em data posterior, ajuste a Data de Vigor do filtro apresentado na tela e, após isso, realize a atualização.

![Imagem 7: Caso de fato necessite de ajustar o preço já existente para essa data de vigor, aconselha-se atenção no processo, visto…](https://ajuda.sankhya.com.br/hc/article_attachments/16618182813847) Caso de fato necessite de ajustar o preço já existente para essa data de vigor, aconselha-se atenção no processo, visto que preços ajustados mais que uma vez na mesma data não trata-se de melhor prática, pois o registro de preços será "perdido".

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16618182816151)CAUSA:**

Ao tentar inserir um preço de venda para itens que já possuem registro na respectiva data de vigor/tabela, será apresentada a mensagem.
