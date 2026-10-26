---
id: "360044604794"
titulo: "Dashboard de Resultados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604794-Dashboard-de-Resultados"
trilha: "Manual do Produto > Comercial e Vendas > Vendas > Venda Consultiva"
atualizado_em: "2026-07-29T14:12:05Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Negociações", "Venda Consultiva", "Resultados", "UTIUSUPREVENDA", "br.com.sankhya.os.cad.gerenciaprevenda", "Dashboard de Resultados manual", "Dashboard", "METARESEXEC", "Análise de Negociações", "Hierarquia de Vendedores", "Painéis e Filtros", "Funil de Vendas"]
---

# Dashboard de Resultados

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311485352215) Módulo: Venda Consultiva > Negociações
```

---

Esta tela está destinada à análise das negociações, segundo a expectativa classificada pelo vendedor.

![Imagem 2: Esta tela está destinada à análise das negociações, segundo a expectativa classificada pelo vendedor.](https://ajuda.sankhya.com.br/hc/article_attachments/360083354433)

Esta tela é composta pelos seguintes painéis:

- Critérios Gerais;
- Resumo de Execução;
- Expectativa de Fechamento;
- Negociações em Andamento;
- Funil de Vendas.

Estes painéis têm a função de permitir que você informe a expectativa em cada fase da Venda Consultiva; expectativa esta, que poderá ser modificada de acordo com a evolução da negociação. A fase inicial de uma negociação, pode estar com uma expectativa baixa e, após um certo período, evoluir para uma expectativa média, e assim sucessivamente.

Nesta tela, poderão ser visualizadas apenas as informações relacionadas as negociações de um determinado nível de alçada relativo à hierarquia, por exemplo, o gerente poderá visualizar as negociações de sua equipe.

**Importante:** independente da configuração do parâmetro **"Utiliza relacionamento de usuário Ger. Pré-Venda? - UTIUSUPREVENDA"**, o usuário vendedor não poderá verificar suas próprias vendas, isso ocorrerá apenas em casos em que ele esteja associado como próprio gerente.

Na aba Critérios Gerais, é possível utilizar o **"Filtro de Vendedores"**. Ao digitar o texto e clicar no botão **"Buscar"**, o sistema irá procurar na lista de vendedores se existe um vendedor com o texto informado. Caso exista, o vendedor ficará marcado na lista. Ao clicar em buscar novamente é exibido o segundo resultado e assim sucessivamente.

Ainda na aba Critérios Gerais, os filtros que são utilizados para construção do Funil de Vendas são:

- Negociação;
- Produto;
- Origem;
- Vendedores.

Para montagem do Funil de Vendas, quando uma OS está em uma etapa X, automaticamente ela é considerada em todas etapas anteriores da metodologia utilizada para se ter o efeito de funil. Por exemplo, em uma metodologia que possui etapas de 1 a 6, se uma OS está na etapa 4, então ela será considerada também na etapa 3, 2, e 1; da mesma forma, estando na etapa 5, ela será respeitada também nas etapas 4,3,2 e 1.

Para que a Meta seja apresentada no painel **"Resumo de Execução"**, primeiramente, configure a meta do tipo **"Comercial"** na tela [Estrutura de Metas e Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794). Lembrando que, esta pode ser do tipo Valor ou Quantidade, e definida por Produto/Serviço e Vendedor. Depois, informe o código dessa meta no parâmetro **"Meta para gráfico Resumo de Execução - METARESEXEC"**.

No painel **"Negociações em Andamento"** não se leva em consideração o filtro de data, fazendo com que sejam exibidos todos os lançamentos que não estejam fechados. Assim, se a negociação está em andamento, ela estará na data corrente.

**Nota:** a última etapa da negociação indica a conclusão do processo, embora a execução ainda não tenha sido registrada. Por isso, essa fase final não deve ser exibida no gráfico Negociações em Andamento, uma vez que seu propósito é sinalizar que a negociação foi finalizada e não está mais em andamento.

**Observação:** se estas negociações antigas não forem ser concretizadas, o ideal é que elas sejam fechadas.

#### Parâmetro que influencia esta rotina

**Utiliza relacionamento de usuário Ger.Pré-Venda? - UTIUSUPREVENDA:** possui o valor padrão igual a **"N"**, ou seja, irá listar a hierarquia dos vendedores (tabela TGFVEN - Tabela de Vendedores) na árvore de vendedores da gerência de pré-venda e Dashboard de Resultados. É de extrema importância que o código do parceiro vinculado ao usuário, seja igual ao código do parceiro do vendedor. Se o valor do parâmetro for alterado para **"S"**, irá listar a hierarquia dos vendedores à partir da tabela TCSRUS (Tabela de relacionamento entre vendedores e gerentes) onde o tipo de relação entre os usuários é igual a **"G"**.
