---
id: "21517573466903"
titulo: "Consolidação do GOL não é executada ou leva valores de faturamento divergente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21517573466903-Consolida%C3%A7%C3%A3o-do-GOL-n%C3%A3o-%C3%A9-executada-ou-leva-valores-de-faturamento-divergente"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T14:50:07Z"
rotulos: ["Configuração", "Relatórios", "Faturamento", "TOP", "Financeiro", "GOL"]
---

# Consolidação do GOL não é executada ou leva valores de faturamento divergente

**(1)** As informações da consolidação do GOL (Gerente Online) podem ser utilizadas tanto para os relatórios com o filtro ‘Consolidação de Movimentos’ quanto para os cards de Faturamento e Lucratividade.

**(1)** Seguindo a configuração estabelecida na consolidação (GOL » Preferências » Consolidação de Movimentos), o sistema executa um Job no horário definido para popular a tabela TGFMGC, que é responsável por armazenar as informações de compra/venda dos produtos analisados.

**(1)**Quando existem valores incorretos ou zerados no faturamento, as configurações abaixo podem auxiliar na correção do problema:

![Imagem 1: Na Administração do Servidor ( Configurações » Avançado ) verifique se existe o ‘Argumento da VM’ com o nome…](https://ajuda.sankhya.com.br/hc/article_attachments/21863058982679) Na Administração do Servidor (Configurações » Avançado) verifique se existe o ‘Argumento da VM’ com o nome ‘-Dsankhyaw.schedule.=true’, caso esteja como 'true' o job de consolidação não executara.

![Imagem 2: É necessário existir uma referência de Custo Variável para cada empresa analisada.](https://ajuda.sankhya.com.br/hc/article_attachments/21863075428887) É necessário existir uma referência de Custo Variável para cada empresa analisada.

Acesse a tela Gerente On-Line - GOL (Comercial » Gerente), abra as configurações e acesse a aba Margem de contribuição.

**![Imagem 3: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21863059002647)OBSERVAÇÃO:**

O ano de referência deve ser anterior as notas de venda realizada.

![Imagem 4: O ano de referência deve ser anterior as notas de venda realizada.](https://ajuda.sankhya.com.br/hc/article_attachments/21863075447575)

![Imagem 5: O produto vendido deve obrigatoriamente possuir um CUSTO com data igual ou anterior à emissão da nota de venda…](https://ajuda.sankhya.com.br/hc/article_attachments/21863059023511) O produto vendido deve obrigatoriamente possuir um CUSTO com data igual ou anterior à emissão da nota de venda realizada.

![Imagem 6: As TOP's de compra/venda devem possuir as configurações dos campos de 'Apoio a Decisão'.](https://ajuda.sankhya.com.br/hc/article_attachments/21863059034903) As TOP's de compra/venda devem possuir as configurações dos campos de 'Apoio a Decisão'.

Acesse a tela Tipos de Operação - Top (Comercial » Arquivo » Cadastros); identifique a TOP correspondente; acesse a aba Geral e localize a opção 'Apoio a Decisão'.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21863059002647)OBSERVAÇÃO:**

Caso seja uma **TOP de devolução**, o 'Identificador de Devolução' precisa estar preenchido com a opção 'Sim'.

![Imagem 8: Caso seja uma TOP de devolução , o 'Identificador de Devolução' precisa estar preenchido com a opção 'Sim'.](https://ajuda.sankhya.com.br/hc/article_attachments/21863059050775)

![Imagem 9: Caso o tipo de operação esteja definido como 'Bonificação' os valores dessa operação não serão considerados na analise.](https://ajuda.sankhya.com.br/hc/article_attachments/21863059058967)  Caso o tipo de operação esteja definido como 'Bonificação' os valores dessa operação não serão considerados na analise.

![Imagem 10: O tipo e o tamanho dos campos entre as tabelas TGFPRO, TGFMGC e TGFMGC_TMP devem ser idênticos ao banco de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/21863075514647) O **tipo** e o **tamanho** dos campos entre as tabelas TGFPRO, TGFMGC e TGFMGC\_TMP devem ser idênticos ao banco de dados.

![Imagem 11: Verifique se a configuração da Consolidação está correta e se possui algum filtro que impeça a venda de ser buscada;](https://ajuda.sankhya.com.br/hc/article_attachments/24818370089239) Verifique se a configuração da Consolidação está correta e se possui algum filtro que impeça a venda de ser buscada;

Acesse a tela Gerente On-Line - GOL (Comercial » Gerente); abra as configurações; acesse a aba Consolidação de Movimentos - Consolidação e em seguida a aba filtros.

![Imagem 12: OBSERVAÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/21863059002647)**OBSERVAÇÃO:**

Caso a aba não seja apresentada, é necessário ativar o parâmetro 'GOL-CONSMOV - Usar Consolidação de Dados', através da tela Preferências (Configurações » Avançado).

![Imagem 13: Caso a aba não seja apresentada, é necessário ativar o parâmetro 'GOL-CONSMOV - Usar Consolidação de Dados', através da…](https://ajuda.sankhya.com.br/hc/article_attachments/21517573461015)

**![Imagem 14: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/21517573462167)CAUSA:**

Quando alguma configuração não está adequada, isso pode impedir a execução do Job consolidador ou resultar em informações de faturamento incompletas, podendo impactar a tomada de decisão.
