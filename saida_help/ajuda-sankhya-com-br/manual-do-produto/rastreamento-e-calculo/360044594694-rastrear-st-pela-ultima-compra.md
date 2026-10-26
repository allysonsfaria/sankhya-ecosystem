---
id: "360044594694"
titulo: "Rastrear ST pela Última Compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594694-Rastrear-ST-pela-%C3%9Altima-Compra"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Rastreamento e cálculo"
atualizado_em: "2026-09-15T17:25:36Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "br.com.sankhya.mgeliv.rastrearestoqueultcompra", "Rastrear ST pela Última Compra manual", "Configuração", "Fiscal", "Impostos", "Estoque", "Processa ICMS ST pela última compra", "Dados atualizados na aba Impostos", "Filtragem dinâmica e grade de produtos"]
---

# Rastrear ST pela Última Compra

| ``` ![Imagem 1: Módulo: Livros Fiscais > Avançado > Rastreamento de Estoque/ST](https://ajuda.sankhya.com.br/hc/article_attachments/42312890504087) Módulo: Livros Fiscais > Avançado > Rastreamento de Estoque/ST ``` |
| --- |

---

Esta tela apenas será exibida quando o parâmetro **"Rastreia ST pela última entrada - RASTSTULTENTRA"** encontrar-se habilitado, assim como a rotina [Entradas que Amparam ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594994).

![Imagem 2: Esta tela apenas será exibida quando o parâmetro "Rastreia ST pela última entrada - RASTSTULTENTRA" encontrar-se…](https://ajuda.sankhya.com.br/hc/article_attachments/8769561618711)

**Importante:** esta tela é a responsável por implantar o processo de Rastreamento de ST pela Última Compra do produto; caso não tenha sido implantada em primeiro momento, as informações de ICMS ST não serão devidamente populadas ou utilizadas.

**Observação:** ao realizar o rastreamento por meio dessa tela, o sistema informará na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Rastreamento Por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abarastreamentoporempresa), o **"Tipo de Rastreamento"** com a opção **"Última Compra"**.

**Nota:** o saldo utilizado nesta rotina será informado na tela Entradas que Amparam ST, onde constam os valores unitários de ICMS ST capturados na Últ. Entrada.

| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594694-Rastrear-ST-pela-%C3%9Altima-Compra#filtros) |  | [Grade de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594694-Rastrear-ST-pela-%C3%9Altima-Compra#gradeprodutos) |
| --- | --- | --- |
| [Rastreamento de ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594694-Rastrear-ST-pela-%C3%9Altima-Compra#rastreamentodest) |  |  |

## Filtros

![Imagem 3: Filtros](https://ajuda.sankhya.com.br/hc/article_attachments/8769566212759)

No local em destaque, teremos o **"Filtro personalizado"** e os **"Filtros rápidos"**, sendo que, através de um Filtro personalizado será possível filtrar os produtos para o Rastreamento de ST de uma maneira dinâmica, em que você poderá utilizar variáveis ou querys; já em relação aos Filtros rápidos, estes estão divididos em **"Empresa"** (que se trata de um campo de preenchimento obrigatório), **"Produto"**, **"Grupo de Produto"** e **"Grupo de ICMS do Produto"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594694-Rastrear-ST-pela-%C3%9Altima-Compra#top)

## Grade Produtos

![Imagem 4: Grade Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/8769603035799)

Esta grade exibirá todos os produtos que foram filtrados através do Filtro personalizado ou dos Filtros rápidos e que poderão ser processados.

**Observação:** os produtos que não se enquadram nos filtros ou que já estão sendo rastreados não serão exibidos nesta grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594694-Rastrear-ST-pela-%C3%9Altima-Compra#top)

## Rastreamento de ST

Após filtrados os produtos, para processar o Rastreamento de ST pela Última Compra, acione o botão ![Imagem 5: Após filtrados os produtos, para processar o Rastreamento de ST pela Última Compra , acione o botão "Rastrear" .](https://ajuda.sankhya.com.br/hc/article_attachments/8769621296407) **"Rastrear"**.

Assim, o sistema implantará o Rastreamento pela Última Compra para cada um dos produtos selecionados e, caso não ocorra nenhum erro, será exibida uma mensagem informando que o Rastreamento de ST pela Última Compra foi concluído com sucesso. Por outro lado, caso seja concluído o rastreamento mas ocorra erro em algum dos produtos apresentados na lista, será apresentada a seguinte mensagem:

**"Erro ao tentar buscar o rastreamento:**

**[Não foram encontrados valores de ICMS ST para rastreamento Código da Empresa: X Código do Produto: X Nota de Nro Único: X, Sequência: X]."**

Ainda neste sentido, caso o processamento do rastreamento tenha encontrado mais de um produto com erro, será exibida a mensagem a seguir:

**"Erro ao tentar buscar o rastreamento para X produtos".**

Após processado o rastreamento, o sistema incluirá e atualizará as informações do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostosinformaesporempresa), marcando a opção **"Usa Rastro/ST pela Últ. Entrada"**.

**Nota:** caso já exista uma linha correspondente na aba acima mencionada, apenas será atualizado o campo; caso não exista, o sistema realizará a cópia dos dados do produto e irá inserir uma nova linha na aba Impostos / Informações por empresa, para que corresponda ao mesmo.

**Observação:** além de serem inseridos os dados na aba Impostos / Informações por empresa do Cadastro de Produtos, também serão inseridos na tela [Entradas que Amparam ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594994).

Desta forma, após obter-se os dados dos impostos unitários pela rotina de Entradas que Amparam ST e o produto encontrar-se marcado como Usa Rastro/ST pela Ult. Entrada, ao realizar a venda do mesmo, no momento da confirmação da NF de Venda, o sistema imputará os valores multiplicados pela quantidade negociada do mesmo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594694-Rastrear-ST-pela-%C3%9Altima-Compra#top)
