---
id: "37637953763351"
titulo: "Como atualizar o estoque mínimo com base no giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37637953763351-Como-atualizar-o-estoque-m%C3%ADnimo-com-base-no-giro"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-10-05T02:18:00Z"
rotulos: ["Produtos", "Configuração", "Análise de Giro", "Estoque", "Sankhya"]
---

# Como atualizar o estoque mínimo com base no giro

| Categoria |
| --- |
| [O que é a atualização do estoque mínimo e quais seus benefícios?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37637953763351-Como-atualizar-o-estoque-m%C3%ADnimo-com-base-no-giro#h_01KEVPTM9FFPW0QE3SNRYA5M3K) |
| [Quais os problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37637953763351-Como-atualizar-o-estoque-m%C3%ADnimo-com-base-no-giro#h_01KEVPF7540MFWRDSWPHSQYP34) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37637953763351-Como-atualizar-o-estoque-m%C3%ADnimo-com-base-no-giro#h_01KEVPFMSK4GQ5PGHE3PWGKS0N) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37637953763351-Como-atualizar-o-estoque-m%C3%ADnimo-com-base-no-giro#h_01KFBGSXFYWE47T4D8287GA1Z9) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37637953763351-Como-atualizar-o-estoque-m%C3%ADnimo-com-base-no-giro#h_01KFBGRECA1WXNYDZ1JWMRMS92) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37637953763351-Como-atualizar-o-estoque-m%C3%ADnimo-com-base-no-giro#h_01KEVPG713C0A3QN4FBWW6E6AN) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37637953763351-Como-atualizar-o-estoque-m%C3%ADnimo-com-base-no-giro#h_01KEVPJC9YERZ6A4EX43QWZTWK) |

## Reposição do estoque em função do mínimo e máximo

#### O que é a atualização do estoque mínimo e quais seus benefícios?

A atualização do estoque mínimo ajusta automaticamente a quantidade mínima de produtos que a empresa deve manter, baseando-se no giro real de vendas e consumo. Diferente de simplesmente definir um valor fixo, esse processo considera dados históricos para garantir uma reposição estratégica, alinhada à demanda real. Dessa forma, os principais benefícios estão na falta de produtos e o acúmulo desnecessário de mercadorias, equilibrando oferta e demanda de forma eficiente e sustentável.

#### Quais os problemas este recurso resolve?

- **Falta de produtos no estoque:** O recurso evita rupturas ao manter os itens essenciais sempre disponíveis para atender à demanda.
- **Excesso de mercadorias paradas:** controlando o volume armazenado e minimizando custos e riscos de obsolescência.
- **Compras mal dimensionadas:** ajustando compras conforme a necessidade real e reduzindo gastos com armazenagem e transporte.
- **Desperdício de recursos financeiros:** trazendo previsibilidade às compras e ao fluxo de caixa, garantindo um uso mais estratégico dos recursos.

#### Quais os riscos de não utilizar?

Se a atualização do estoque mínimo não for feita com base no giro de vendas, a empresa corre o risco de ficar sem produtos importantes, perdendo vendas e deixando clientes insatisfeitos. Também pode acabar com mercadorias sobrando no estoque, o que aumenta os custos com espaço e manutenção, além do risco de os produtos vencerem ou ficarem obsoletos. Outro problema é o desperdício de dinheiro, já que o capital fica preso em itens desnecessários, dificultando investimentos e o crescimento da empresa.

#### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052445350)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Na **Axis**, após a ruptura de estoque de produtos com alta rotatividade, o setor de vendas precisou recusar alguns pedidos, gerando insatisfação nos clientes e perda de vendas.

Durante a Análise de Giro realizada, a compradora, ao observar os dados detalhados na tela, percebeu que o estoque mínimo cadastrado estava abaixo do ideal, considerando a rotatividade do item. Mesmo que a sugestão de compra tenha suprido a necessidade naquele momento, esse parâmetro incorreto poderia comprometer futuras análises e decisões de reposição.

Com base nos resultados obtidos, o comprador decidiu ajustar o estoque mínimo no cadastro dos produtos com comportamento semelhante, garantindo que o sistema esteja alinhado à realidade da operação e ajudando a prevenir novas perdas por falta de estoque.

**Tarefa:** Com base na Análise de Giro realizada na etapa anterior, acesse a aba Detalhes da Sugestão de Compra e ajuste o estoque mínimo dos produtos da sua base de acordo com o valor exibido na coluna Estoque Mínimo Sugerido.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Confira o parâmetro de sugestão de compra**

- Acesse a tela **Preferências**
  Menu: Configurações » Avançado » Preferências
- Na barra de pesquisa informe a chave **SUGCOMPMIMAMTZ** (**Sug. de compra estoque mínimo ao o máximo?**).
- Clique no botão “**Pesquisar**”.
- Selecione **Desligado** no campo “**Ligado/Desligado:**”.

Isso garante que a sugestão de compra leve em conta o estoque mínimo, e não o estoque máximo.

2. **Processar ou analisar a matriz de giro:**

- Acesse a tela **Análise de Giro**
  Menu: Comercial » Rotinas » Análise de Giro
- Selecione a matriz de giro **configurada anteriormente**.
- Clique no botão **"Processar Matriz"** para atualizar as informações.

Caso uma matriz tenha sido processada recentemente, revise os dados já calculados.

3. **Verificar a sugestão de estoque mínimo:**

- Na tela Análise de Giro, localize na porção inferior direita a aba **“Detalhes da Sug. de Compra”** e verifique a coluna **"Est.Min.Sug"** na linha **“Sug. Compra Giro”.**

Se o valor calculado for maior que zero, prossiga para a atualização.

4. **Atualizar o estoque mínimo nos cadastros:**

- Clique no botão **"Outras Opções"** e selecione **"Alterar Estoque Mínimo nos Cadastros"**.
- No pop-up **"Deseja confirmar a atualização do Estoque Mínimo?"** clique em **“Sim”**.
- Clique no botão “**OK**”.

5. **Validar a atualização no cadastro de produtos:**

- Acesse a tela **Produtos**

Menu: Configurações » Cadastros » Produtos

- Localize os produtos que apresentam sugestão de ajuste no estoque mínimo.
- Se a matriz apresentar o resultado por **Empresa, Local ou Controle**, acesse a aba **“Estoque”**.
- Nos demais casos, a atualização deve ser feita na aba **“Medidas e Estoque”**, no campo **“Estoque Mínimo”**.

#### Correção e Repetição

- Revise as informações dos produtos para garantir que o estoque mínimo esteja configurado corretamente.
- Se algo não tiver saído como esperado, refaça o processo ajustando os dados necessários.
- Reprocesse os dados na Matriz de Giro para garantir que as informações estejam atualizadas.
- Para treinar novamente, monte um novo cenário com produtos e quantidades de estoque mínimo diferentes.
