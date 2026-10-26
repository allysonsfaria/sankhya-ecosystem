---
id: "37617585764887"
titulo: "Como identificar a necessidade de compras pelo estoque mínimo e máximo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37617585764887-Como-identificar-a-necessidade-de-compras-pelo-estoque-m%C3%ADnimo-e-m%C3%A1ximo"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-07-22T14:12:33Z"
rotulos: ["Produtos", "Configuração", "Análise de Giro", "Estoque", "Sankhya", "Compras"]
---

# Como identificar a necessidade de compras pelo estoque mínimo e máximo

| Categoria |
| --- |
| [Qual a importância da reposição do estoque em função do mínimo e máximo?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37617585764887-Como-identificar-a-necessidade-de-compras-pelo-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KESKMER55N0T5WSE2696FJAW) |
| [Quais problemas este recurso do sistema resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37617585764887-Como-identificar-a-necessidade-de-compras-pelo-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KESKSDGYP9QQ9J0Z2VWQR6H7) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37617585764887-Como-identificar-a-necessidade-de-compras-pelo-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KFBBPA4P9NKQ9KY46XWMM93W) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37617585764887-Como-identificar-a-necessidade-de-compras-pelo-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KESKN5016F9Y4W86TTMRHBV9) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37617585764887-Como-identificar-a-necessidade-de-compras-pelo-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KESKVKP9F8WX8QFZXHVD4H5M) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37617585764887-Como-identificar-a-necessidade-de-compras-pelo-estoque-m%C3%ADnimo-e-m%C3%A1ximo#h_01KESKX7Y30EB2NAQJZJCT4EM4) |

## Necessidade de Compras por Estoque Mínimo e Máximo

#### Qual a importância da reposição do estoque em função do mínimo e máximo?

A reposição de estoque baseada em níveis mínimos e máximos é essencial para evitar rupturas de estoque e excesso de produtos, garantindo disponibilidade sem imobilizar capital desnecessariamente. Ao definir um nível mínimo, evita-se a falta de produtos, enquanto o nível máximo previne compras excessivas, reduzindo custos de armazenamento e desperdício. Esse método otimiza o capital de giro, facilita o planejamento de compras, melhora a previsibilidade e permite a automação do processo, proporcionando eficiência operacional e melhor atendimento ao cliente.

#### Quais problemas este recurso do sistema resolve?

- **Falta de produtos em estoque (rupturas):** Leva à perda de vendas e insatisfação dos clientes devido à indisponibilidade de produtos.
- **Excesso de estoque:** Gera custos elevados de armazenamento e risco de perdas por obsolescência ou deterioração.
- **Planejamento de compras ineficiente:** Resulta em compras desorganizadas, falta de previsibilidade e dificuldades nas negociações com fornecedores.
- **Imobilização de capital desnecessária:** Compromete o capital de giro da empresa, limitando recursos para outras operações importantes.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052296315)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Na **Axis**, parte do portfólio é composto por produtos de alto giro. A falta recorrente de alguns itens tem afetado a produtividade da equipe e gerado atrasos nas operações, evidenciando a necessidade de um controle mais eficiente. 
Para apoiar esse processo, o sistema ERP Sankhya disponibiliza à compradora uma ferramenta que permite acompanhar o consumo, definir os níveis de estoque mínimo e máximo e evitar rupturas no estoque.

**Tarefa:** Identifique a necessidade de compra de produtos com base nos dados gerados pelo processamento da matriz na Análise de Giro.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Validar o cadastro de produtos**

Menu: Configurações » Cadastros » Produtos

- Selecione o produto que irá identificar.
- Acesse a aba **“Medidas e Estoque”**.
- Preencha os campos '**Estoque Mínimo**' e '**Estoque Máximo**' com os respectivos valores.
- Salve o registro.
- Acesse a aba “**Estoque**”
- Clique em “+” (Cadastrar Estoque) e preencha:

  - Empresa
  - Local

**Sub aba Geral**

- Estoque mínimo
- Estoque máximo
- Acione o botão “**Salvar**”.

2. **Análise de Giro**

Comercial » Rotinas » Análise de Giro

- Localize a matriz de giro configurada, como **Análise Mensal com giro e sem giro.**

3. **Configure a Matriz de Giro**

- Clique no botão “**Alterar matriz selecionada**” ao lado da matriz para abrir o pop-up de configurações.

Verifique e ajuste os seguintes pontos:

**Aba “Períodos”:**

- Selecione "**Períodos dinâmicos - As datas serão definidas automaticamente no cálculo do Giro**"
- Defina o período como **3 meses anteriores.**

**Aba “Estoque Mínimo e Sugestão de Compras”:**

- Selecione o campo "**Período sem vendas influencia a média para estoque mínimo**".
- Selecione o campo "**Não Atualizar Estoque Mínimo quando a sugestão for zero?**"

**Aba “Outras configurações”**

- Selecione os campos "**Incluir produtos sem giro**" e "**Incluir produtos sem estoque**".
- Selecione **Reposição** no campo "**Considerar custo:**".
- Selecione **Produto** no campo "**Detalhar de acordo com:**".
- Selecione o campo "**Listar pedidos na aba Compras/Vendas Pendentes**".
- Selecione os campos "**Empresa**", "**Local**" e "**Controle**".

**FILTRO**

**Produtos com Giro:** 

**Iniciar a criação de um novo Filtro:**

- Clique no ícone de **filtro**.
- Selecione **+ Cadastrar Filtro**.
- No campo **Nome do Filtro**, digite: **Revenda**.
- Clique em **+ Cadastrar Condição**.
- No campo **Selecione o campo**, clique para abrir o pop-up com os campos disponíveis.
- Acesse a sub-aba **Ligações em Consolidação do Giro** e selecione **PRODUTO**.
- No campo **Informe sua busca**, digite **Usado como** e pressione **Enter**.
- Na sub-aba **Campos de Produto**, selecione o campo **Usado como**.
- No próximo campo, escolha a condição **= Igual (=)**.
- No campo seguinte, selecione o valor **Revenda**.
- Clique em **Salvar** para gravar o filtro.
- Clique em **< Filtro** para retornar e cadastrar os próximos filtros.

**Produtos sem Giro:**

**Iniciar a criação de um novo Filtro:**

- Clique no ícone de **filtro**.
- Selecione **+ Cadastrar Filtro**.
- No campo **Nome do Filtro**, digite: **Revenda**.
- Clique em **+ Cadastrar Condição**.
- No campo **Selecione o campo**, clique para abrir o pop-up com os campos disponíveis.
- No campo **Informe sua busca**, digite **Usado como** e pressione **Enter**.
- Na sub-aba **Campos de Produto**, selecione o campo **Usado como**.
- No próximo campo, escolha a condição **= Igual (=)**.
- No campo seguinte, selecione o valor **Revenda**.
- Clique em **Salvar** para gravar o filtro.
- Clique em **< Filtro** para retornar e cadastrar os próximos filtros.

**Produtos sem Giro e sem Estoque:**

**Iniciar a criação de um novo Filtro:**

- Clique no ícone de **filtro**.
- Selecione **+ Cadastrar Filtro**.
- No campo **Nome do Filtro**, digite: **Revenda**.
- Clique em **+ Cadastrar Condição**.
- No campo **Selecione o campo**, clique para abrir o pop-up com os campos disponíveis.
- No campo **Informe sua busca**, digite **Usado como** e pressione **Enter**.
- Na sub-aba **Campos de Produto**, selecione o campo **Usado como**.
- No próximo campo, escolha a condição **= Igual (=)**.
- No campo seguinte, selecione o valor **Revenda**.
- Clique em **Salvar** para gravar o filtro.
- Clique em **< Filtro** para retornar

4. **Processar a Matriz de Giro**

- Clique no botão “**Processar Matriz**”.
- Aguarde o sistema calcular as sugestões de compra.

5. **Analise os Resultados**

- Na **coluna Sugestão de Compras**, identifique os produtos sugeridos e suas quantidades.
- Consulte a **Sub Aba Detalhes da Sug. de Compras** para entender o cálculo e os critérios utilizados.

#### Correção e Repetição

- Confirme que todos os campos obrigatórios foram preenchidos de maneira correta e completa.
- Certifique-se de que os valores inseridos estão conforme as políticas e diretrizes da empresa, garantindo conformidade e precisão no pedido.
- Se os valores sugeridos não forem os esperados, revise o processo e corrija as informações necessárias antes de tentar novamente.
- Assegure-se de seguir todos os passos repassados no vídeo demonstrativo para evitar erros recorrentes.
- Para reforçar sua habilidade no sistema, pratique criando um novo cenário, como um fornecedor, cliente ou produto diferente.
- Essa prática ajuda a consolidar o aprendizado e a adaptar-se a diversas situações do dia a dia.
