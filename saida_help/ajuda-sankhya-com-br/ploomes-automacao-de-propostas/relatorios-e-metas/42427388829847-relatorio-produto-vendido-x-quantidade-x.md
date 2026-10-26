---
id: "42427388829847"
titulo: "Relatório: Produto Vendido x Quantidade x Valor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427388829847-Relat%C3%B3rio-Produto-Vendido-x-Quantidade-x-Valor"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-11T16:15:00Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452218", "sync_hash_2ba3abae95a6"]
---

# Relatório: Produto Vendido x Quantidade x Valor

Esse relatório reúne, em uma única tabela, o produto vendido, a quantidade total e o valor total das vendas, agrupados por produto. Ele ajuda a identificar quais itens têm mais saída e qual o peso de cada um no faturamento, apoiando decisões de estoque, precificação e priorização comercial. Use esse relatório sempre que precisar comparar o desempenho de vendas entre os produtos do seu catálogo.

⚠️ **Atenção:** para montar este relatório, sua conta precisa ter o módulo **Analytics** contratado.

## Antes de criar o relatório

Antes de montar o relatório, confirme que as informações que você quer analisar estão preenchidas nas vendas.

Acesse **Documentos > Vendas > Quebrar por produtos > Aba de Produtos da Venda**, entre na ferramenta de configuração de campos e garanta que os campos **Nome do Produto**, **Quantidade** e **Valor Unitário** estejam habilitados para exibição.

![(Imagem: tela de configuração de campos da aba Produtos da Venda)](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2576683487/7576864464fd646216cc877f7b9b/1.png?expires=1786536000&signature=1fcc7a1a45985f3ebec589fc821f7c00595a0e4155ecddcd803c166e7f9f679e&req=diUgEM92noVXXvMW3nq%2BgfO6hF00eXJgzr6I8Cfc8sKOHE6u5djxWNJ5psce%0AEn8XOhfPWJJjBriRlGRHqiUHzbo%3D%0A)

💡 **Dica:** você pode configurar outros campos além desses três mas, para a emissão desse relatório específico, essas três opções precisam estar aparentes.

## Como acessar e configurar

Acesse o módulo de **Relatórios** (pelo menu lateral esquerdo).

![Imagem 2: Acesse o módulo de Relatórios (pelo menu lateral esquerdo).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577538483/05bdb0526e765714d5b2f0499b4e/image.png?expires=1786536000&signature=962589d20012781a49e4d0c1afa4025742ee53e261a092e84d32c515359cdd0b&req=diUgEcx9lYVXWvMW3nq%2BgTuc7LL6m0v2lVg6zTBTQMa5v4SIXOacLA3kBvMv%0AEa0hs%2BFrdjmA%2BcmyAfZShQJADRA%3D%0A)

Escolha o painel onde o gráfico deve ficar, clique em **Novo Gráfico** e selecione o tipo **Tabela**.

![Imagem 3: Escolha o painel onde o gráfico deve ficar, clique em Novo Gráfico e selecione o tipo Tabela .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2576687846/53715a786337abd68805d67883dc/image.png?expires=1786536000&signature=a54eebb63ba6c16db975e8f83ba07f748284090d1ebbf2b3adfd968fc384bc35&req=diUgEM92molbX%2FMW3nq%2BgTKi5rxmd2OZSRg1%2B4R%2F8IybXz4ICXBbw77Tg80d%0AycX2y3SjwBgN2gg2koXdRJLD4iM%3D%0A)

💡 **Dica:** se você ainda não conhece a tela de Relatórios (criação de painéis, permissões de Leitor/Editor/Administrador e os tipos de gráfico disponíveis), veja também: **[Como criar relatórios no Ploomes (nova tela)](https://sankhya.zendesk.com/hc/pt-br/articles/42427389079447)**.

Esse relatório específico precisa de **duas métricas**: uma para o valor total e outra para a quantidade.

## Métrica de Valor

1. Em **Objeto da Análise/Entidade**, selecione **Produto da Venda > Soma > Total**.
2. Em **Escolha como agrupar os dados**, selecione o campo **Produto**.
3. Você pode escolher uma cor para a métrica, mas isso não é obrigatório em relatórios do tipo Tabela.
4. Clique em **Salvar**.

![Imagem: configuração da métrica de valor](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2576696563/1c4e9ac0729a31e03c9c6605c8f9/image.png?expires=1786536000&signature=187093f1d3d6da644f24c1d105a44b65902bc385063b80df8751799eab66bcb8&req=diUgEM93m4RZWvMW3nq%2BgR%2BLIuk4ujI4MPURzf%2F6qwuToH9CFnLHyyxtUqEP%0AFfbVto21mOiIk6MaQA%2BTRPwsjo0%3D%0A)

## Métrica de Quantidade

1. Clique em **Adicionar métrica**.

   ![Imagem: botão Adicionar métrica](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577401075/dc12e9a9e4cd342b8b26a8f85122/image.png?expires=1786536000&signature=68f73720f71b7e7ef22057d4525290fa985c1e1b3ead83651e967d30e4d7408e&req=diUgEc1%2BnIFYXPMW3nq%2BgaLnHNRK6Xh4RTsk5QNIPRSmiuMDTfIVd4wiWuD4%0AlPx7xPRc%2F9t0RJS%2FllhT2IpgPy0%3D%0A)
2. Em **Objeto da Análise/Entidade**, selecione **Produto da Venda > Soma > Quantidade**.
3. Em **Escolha como agrupar os dados**, selecione o campo **Produto**.
4. Clique em **Salvar**.

![Imagem: configuração da métrica de quantidade](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577403928/e17637ccbca543887364c227f106/image.png?expires=1786536000&signature=17ab495c6b9b822840099474892ef1e8025b75a3f69aa43b2a1905086b32bc5f&req=diUgEc1%2BnohdUfMW3nq%2Bget%2FBGPlAP0oGmJb5bnRZWkhnsdfX3SsrBKA1v7y%0A9O9gUkbWlMrTbcMk8So0hb43B0U%3D%0A)

## Resultado

Depois de salvar as duas métricas, clique em **Salvar gráfico.**

![Imagem 7: Depois de salvar as duas métricas, clique em Salvar gráfico.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577507911/781be651068c3dc352b508d29548/image.png?expires=1786536000&signature=c3703ed08783640cc667c81da62f48131dd44a677cf507bee4aa30f844e2567f&req=diUgEcx%2BmoheWPMW3nq%2BgXgWlkD2ne4u01DxA0%2FiF%2FF6jquR%2FDC9zL7U%2BsFm%0ALfTfh%2BcIybPZ3S548tsFf0NeVvw%3D%0A)

O relatório exibe uma tabela com o produto, a quantidade total vendida e o valor total, lado a lado.

![exemplo do relatório finalizado](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577440305/987200a2ff4eaa71969f2da0824f/image.png?expires=1786536000&signature=eb05e4ebd2c19644b8b1203892a64cfc5ea8c549cd961c6f4bde296c39056005&req=diUgEc16nYJfXPMW3nq%2BgQpBC%2BQbi80rTG087sFDhBiqA27MMCF09aKi1b9F%0Aep986YcmmpJ0nk8wNWt5vp86GjM%3D%0A)

---

Esse artigo te ajudou? Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

Ficou com alguma dúvida? Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
