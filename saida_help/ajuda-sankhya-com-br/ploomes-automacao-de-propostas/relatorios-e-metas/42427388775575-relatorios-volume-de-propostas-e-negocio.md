---
id: "42427388775575"
titulo: "Relatórios: Volume de propostas e negócios por mês"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427388775575-Relat%C3%B3rios-Volume-de-propostas-e-neg%C3%B3cios-por-m%C3%AAs"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-11T16:15:00Z"
rotulos: ["sync_hc", "ploomes_5452215", "ploomes", "sync_hash_5cbe100b7c74"]
---

# Relatórios: Volume de propostas e negócios por mês

Nesse artigo, você aprende a montar um relatório que compara, mês a mês, a quantidade de Negócios criados com a quantidade de Propostas criadas — útil para acompanhar o volume de geração de propostas em relação ao volume de negócios abertos.

⚠️ **Atenção:** para montar este relatório, sua conta precisa ter o módulo **Analytics** contratado.

## Como acessar e configurar

Acesse o módulo de **Relatórios** (pelo menu lateral esquerdo).

![Imagem 1: Acesse o módulo de Relatórios (pelo menu lateral esquerdo).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577541620/9596f02e93c254526e0a6603096c/image.png?expires=1786536000&signature=419d169ad266884dae75540289762716dcbc2ccacfc1789a2735686ce8ba557e&req=diUgEcx6nIddWfMW3nq%2BgV7XWMFc07vLF0s9uMfjnCmqoyEfVmM75PsvmAFG%0AWS1UtiI1JhC3UyyAsAPWhIx9SH8%3D%0A)

Escolha o painel onde o gráfico deve ficar e clique em **Novo Gráfico**. Escolha um tipo de gráfico que permita comparar duas métricas ao longo do tempo, como **Barras** ou **Linhas**.

![Imagem 2: Escolha o painel onde o gráfico deve ficar e clique em Novo Gráfico . Escolha um tipo de gráfico que permita comparar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577543239/f1a19f13099ba67a00d20a7644fa/image.png?expires=1786536000&signature=1c68cb47c224cd12e13663cc096b5b5821cd221fd8482d777e02ec0e5748d235&req=diUgEcx6noNcUPMW3nq%2BgZrPuhgUAQJE0aXgHyKsNq7M0HWVszSeO5Hn1Ku1%0AAQnJPq%2BJ5CMuEMWJsyiygVMYAtI%3D%0A)

💡 **Dica:** se você ainda não conhece a tela de Relatórios (criação de painéis, permissões de Leitor/Editor/Administrador e os tipos de gráfico disponíveis), veja também: **[Como criar relatórios no Ploomes (nova tela)](https://sankhya.zendesk.com/hc/pt-br/articles/42427389079447)**.

Esse relatório específico precisa de **duas métricas**: uma para o volume de Negócios e outra para o volume de Propostas.

## Métrica de Negócios

1. Em **Objeto da Análise/Entidade**, selecione **Negócio > Contagem**.

   ![seleção de Negócio > Contagem no campo Objeto da Análise](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577474885/bfd5b67c01f1357debd9d87373e0/Captura%2Bde%2Btela%2B2026-04-07%2B153116.png?expires=1786536000&signature=bc8dfbf49156c6adc4ed00a311a33c864ad6a5137dc62c32cd681026f23177b5&req=diUgEc15mYlXXPMW3nq%2BgUEmYT7Cv89%2Fm%2BrDcOOjehN6H0LtQkWtVVuuySi4%0AyqJIVNHbO8ZMvHsxb%2FgVOQHPB3c%3D%0A)
2. (Opcional) Aplique filtros para refinar os dados, como **Unidade de Negócio** ou **Categorias** específicas de produtos.

   ![Imagem 4: (Opcional) Aplique filtros para refinar os dados, como Unidade de Negócio ou Categorias específicas de produtos.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577476872/25c5b37d839f7d55fcf679ac0557/Captura%2Bde%2Btela%2B2026-04-07%2B153349.png?expires=1786536000&signature=0746c95d09c58d1fa343dd98fc5627a737061cf93167b9aeca02d48639ec7c53&req=diUgEc15m4lYW%2FMW3nq%2BgV2LKhKluD%2FJleSRBjhC4aaFrglJc0zDsMYEP%2FrL%0A6MsuRLLeKyvP6Qh%2FPKPpQr35mwo%3D%0A)

   💡 **Dica:** aplicar filtros reduz o escopo do que está sendo medido — o gráfico passa a mostrar o volume apenas do recorte filtrado, não o volume total de Negócios da conta.
3. Em **Escolha como agrupar os dados**, selecione o campo **Data de Criação** (pode ser a do Negócio ou da Proposta, dependendo de qual marco temporal você deseja priorizar) e, em **Intervalo da Data**, selecione **Mês**.

   ![configuração de agrupamento por Data de Criação, intervalo Mês](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577477742/440622fbc6fb7056f18214acb815/Captura%2Bde%2Btela%2B2026-04-07%2B1533491.png?expires=1786536000&signature=773a07e6e3e6c2b3e2946d0f2f59acfb53f4210b6b5459896adc8a243cf739e7&req=diUgEc15moZbW%2FMW3nq%2BgeF2pDJ%2BP2oKLQZtR28LSTZgL3ufhpk55uSuUyKG%0A5hd5LHQR9tjUTRP5tmrDyqjE54o%3D%0A)
4. Clique em **Salvar**.

## Métrica de Propostas

Como este é um gráfico comparativo, é preciso incluir o segundo volume:

1. Clique em **Adicionar métrica**.
2. Em **Objeto da Análise/Entidade**, selecione **Proposta > Contagem**.
3. Repita os passos de filtro e agrupamento das seções anteriores.
   💡 **Dica:** recomenda-se incluir o filtro **"Última revisão = Sim"** ao contar Propostas. Sem esse filtro, todas as revisões de uma mesma proposta são somadas na contagem, o que infla o número de propostas únicas realmente criadas.
4. Clique em **Salvar** para adicionar a métrica.

![configuração da métrica de Proposta > Contagem](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577479287/0b4ba4365425d219b07e697b90c5/Captura%2Bde%2Btela%2B2026-04-07%2B153440.png?expires=1786536000&signature=60bfcfb901cad3dbfb3645950e0bb2e306c943a605a293dc26bbc2438d20f3b2&req=diUgEc15lINXXvMW3nq%2BgaNpRKRZw3DkUXXFWk4z8j64JgkYhIDHz9rZX%2BLp%0A0A5SKsyhfyCd61Kzivm93lBUXH8%3D%0A)

## Resultado

Depois de salvar as duas métricas, clique em **Salvar gráfico.**

![Imagem 7: Depois de salvar as duas métricas, clique em Salvar gráfico.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577501432/b0ba9c396cb4ad8712295a51cb43/image.png?expires=1786536000&signature=833dfdf00992a6f5221a5b05df46726f4ef34ab860cce66732165e52fbd86b0e&req=diUgEcx%2BnIVcW%2FMW3nq%2BgaLMiUKR4Wxu%2BKa3w0ljsZTqvKdLTv6AjCXFSavG%0A2otBb0b2yr8%2F5%2FzIDh4Xz%2F%2FEjJc%3D%0A)

O gráfico exibe a comparação mensal entre a quantidade de Negócios e a quantidade de Propostas criados, um abaixo do outro no mesmo eixo de tempo.

![gráfico finalizado com as duas métricas](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577484916/a8b57b72affcddcbf9bc92d7d192/Captura%2Bde%2Btela%2B2026-04-07%2B154922.png?expires=1786536000&signature=c02d3fa1f3d7eab5cc3e899e4c9d7ae102eadc5f6ec02824e5ab2ec3e0d9f93a&req=diUgEc12mYheX%2FMW3nq%2Bgb6rCGvuexmPZyYc3c5BgiEOP7%2FP%2B04INjoMihNV%0Ai6VndRcXt%2FOeGCGbAHzES7BCPsc%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
