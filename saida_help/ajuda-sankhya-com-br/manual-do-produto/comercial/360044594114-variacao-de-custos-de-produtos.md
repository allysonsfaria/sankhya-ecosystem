---
id: "360044594114"
titulo: "Variação de Custos de Produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:19:11Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Custos", "Variação de Custos de Produtos", "br.com.sankhya.com.cons.variacaocustosprodutos", "Variação de Custos de Produtos manual", "Configuração", "Relatórios", "Pesquisa Detalhada", "Variação de Custos", "Exportação de Dados", "Comercial"]
---

# Variação de Custos de Produtos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311685306903) Módulo: Comercial > Consulta
```

---

Esta tela apresenta informações a respeito da variação de custos de cada produto, com seus respectivos valores, possibilitando assim, uma análise mais detalhada em diversos períodos.

![Imagem 2: Esta tela apresenta informações a respeito da variação de custos de cada produto, com seus respectivos valores,…](https://ajuda.sankhya.com.br/hc/article_attachments/8261122962967)

No campo **"Intervalo de Atualização"**, informe o período inicial e final que se deseja buscar as atualizações.

Podemos efetuar a pesquisa de variação de custos aplicando um **"Produto"** em específico, uma **"Empresa"** ou um **"Grupo de Produtos"**.

O botão ![Imagem 3: O botão " Exportar grade para PDF " apresenta opções de exportação e visualização das informações da tela. Assim,…](https://ajuda.sankhya.com.br/hc/article_attachments/16745363096855) **"Exportar grade para PDF"** apresenta opções de exportação e visualização das informações da tela. Assim, poderemos **"Exportar para PDF"**, **"Exportar para planilha"** ou **"Exportar para cubo"**.

## Parâmetros que influenciam nesta rotina

**Custo Médio ICM da MP no PA para Custo Produção? - USACUSMEDICMPRO:** quando este parâmetro estiver desligado, o cálculo de custo de ICMS será efetuado sem média. Do contrário, o sistema irá utilizar o custo médio de ICMS para o produto.

**Usa custo anterior no cálc. de custo? (performance) - CUSTANT**: quando habilitado, faz com que o sistema busque o último valor de custo para o produto. Assim, ao lançar uma nota com uma TOP marcada para atualizar custos e com o referido parâmetro ligado, os valores apresentados nesta rotina serão os de custo anterior.

**Observação:** Na tela [Fórmulas de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o), teremos variáveis que podem ser incluídas nas fórmulas e que são afetadas pelo parâmetro mencionado acima, são elas:

- ANTCUSCOMICM (Custo Médio Com ICMS);
- ANTCUSGER (Custo Gerencial);
- ANTCUSMED (Custo Médio Gerencial);
- ANTCUSREP (Custo de Reposição);
- ANTCUSSEMICM (Custo Médio Sem ICMS);
- ANTCUSVAR (Custo Variável).

Ao utilizar uma destas variáveis em uma fórmula, se o parâmetro mencionado anteriormente estiver habilitado, o sistema atualizará esta variável com o valor do último custo calculado para este produto. Com o parâmetro desligado, estas variáveis não serão calculadas, ficando com valor igual a 0 (zero).

Contudo, ainda que o parâmetro esteja ligado, se nenhuma das variáveis de custo descritas acima estiverem informadas na fórmula, o sistema também não as calculará. Assim, ao consultar o produto na grade, as colunas de custos apresentarão o valor segundo essa configuração.

**Atualiza custo de reposição? - ATUALCUSREP:** quando o parâmetro estava habilitado, ele atualizava o Custo de Reposição ao dar entrada em uma nota de compra que atualiza custo.

**Importante:** O parâmetro acima foi descontinuado do Sankhya Om.

**Obtém saldo de estoque pela contagem? - SALDOESTCTAGEM:** quando ligado faz com que a aplicação use a procedure STP\_CALCCUSMEDIOCONTAGEM para calcular os custos médios. Essa procedure tem algumas regras específicas para obtenção do saldo de estoque e deve ser usada com cautela. Quando desligado, o sistema utilizará a procedure STP\_CALCULARCUSTOMEDIODIA que busca os saldos de movimentação dos produtos da TGFESE.

**Cálculo de custo executado por Job? - CALCCUSTOPORJOB:**quando este parâmetro está ativado, o cálculo do custo não acontece de forma imediata (síncrona). O cálculo será realizado por um JOB, que executa o processo quando chega a vez da nota lançada, considerando que podem existir outras notas aguardando na fila. Ao confirmar uma nota, um registro é gerado na tabela TGFCCA e, durante a execução do JOB, essa tabela será consultada. Se houver registros, o sistema realiza a atualização do custo e insere os dados na tabela TGFCUS. É importante destacar que, com o parâmetro ativado, o cálculo de custo assíncrono é desativado.

Em relação à execução do JOB, ele verifica a cada minuto se há registros na tabela TGFCCA. Caso existam, ele processa as notas considerando o limite informado no parâmetro **"Qtd. de registros da TGFCCA executados por Job - QTDREGCCAPORJOB"**, que define a quantidade de registros por JOB. O limite máximo de notas processadas simultaneamente é 10. Se o valor informado for maior que 10, o JOB processará notas adicionais à medida que o cálculo de uma nota for concluído, até atingir o limite informado no parâmetro. Quando atinge a quantidade definida, o JOB finaliza a execução e reinicia o processamento no minuto seguinte.

Se o parâmetro CALCCUSTOPORJOB estiver desativado, o cálculo de custo assíncrono volta a ser executado. No entanto, caso existam notas pendentes na tabela TGFCCA, elas só serão processadas quando uma nova nota for incluída nesta tabela pelo sistema. Por exemplo, se houver 10 notas na tabela e o parâmetro QTDREGCCAPORJOB estiver configurado como "3", o cálculo assíncrono processará 3 notas e aguardará a inclusão de uma nova nota na tabela para continuar o processamento.

Independente de o cálculo ser assíncrono ou por JOB, as notas serão processadas sempre começando pelas de data mais antiga.
