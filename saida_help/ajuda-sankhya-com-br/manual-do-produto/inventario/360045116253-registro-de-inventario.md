---
id: "360045116253"
titulo: "Registro de Inventário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-07-29T14:49:37Z"
rotulos: ["AJUDA DO SKW", "manual", "Custos", "Configuração", "Relatórios", "Fiscal", "Estoque", "Registro de Inventário", "Registro de Inventário manual", "br.com.sankhya.inventario.relatorios.Registro", "Imprimir códigos matérias-primas razão social", "Levanta situação do estoque gera relatório", "Filtros custo quebra formatação discriminação"]
---

# Registro de Inventário

**Importante:** nesta tela você irá visualizar a descrição das funcionalidades da tela Registro de Inventário que está localizada nos menus **"Livros Fiscais > Relatórios > Registro de Inventário"** e **"Inventário > Relatórios > Registro de Inventário"**.

O relatório gerado nesta tela fará um levantamento sobre a situação atual do estoque para fins de contabilidade após sua contagem.

O processo se inicia com a formação de estoque, geralmente feito pelo lançamento de notas de compra. O Tipo de operação - TOP da Nota de Compra deve estar configurado para atualizar o estoque adequadamente, assim como as tabelas de custo.

Após a formação do estoque, uma Cópia do Estoque deverá ser gerada. É importante ressaltar que o relatório de inventário é gerado sobre a cópia do estoque, e não sobre o estoque em si. Assim com a cópia de estoque gerada, a empresa pode lançar ajustes de estoque, para corrigir erros encontrados durante a contagem do estoque (processo manual).

Depois de realizar os ajuste e gerar uma cópia, você poderá gerar o Registro de Inventário. Para tal ação, preencha os campos obrigatórios clique no botão ![Imagem 1: Depois de realizar os ajuste e gerar uma cópia, você poderá gerar o Registro de Inventário . Para tal ação, preencha os…](https://ajuda.sankhya.com.br/hc/article_attachments/360081809034). Um documento em PDF com os dados solicitados serão emitidos. Acesse maiores informações na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

Nesta tela, teremos as seguintes seções:

| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#filtros) |  | [Custo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#custo) |
| --- | --- | --- |
| [Quebra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#quebra) |  | [Formatação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#formata%C3%A7%C3%A3o) |
| [Discriminação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#discrimina%C3%A7%C3%A3o) |  | [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#outrasop%C3%A7%C3%B5es) |
| [Cópia/Contagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#c%C3%B3pia/contagem) |  | [Parâmetros e suas aplicabilidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#par%C3%A2metrosesuasaplicabilidades) |

                                        

![Imagem 2: Parâmetros e suas aplicabilidades](https://ajuda.sankhya.com.br/hc/article_attachments/360083239094)

## Filtros

**Personalizado:** Temos aqui, a possibilidade de personalizar filtros de acordo com a necessidade.

**Dt. Fechamento:** Informe a data do Inventário.

**Empresa:** Preencha este campo com a empresa para o lançamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#top)

## Custo

**Tipo:** Este campo define qual campo da tabela de custos será usado para estimar o custo dos produtos do relatório. Os campos que podem ser usados são: Custo Médio Com ICMS, Custo Médio Sem ICMS, Custo Gerencial e Custo de Reposição. Caso o campo **"Dt. Limite"** seja informado, este será usado como a data limite do custo. Para o Custo Gerencial e o Custo de Reposição, podem ser usados o custo mais atual ou o custo histórico e, para os campos Custo c/ ICMS e Custo s/ ICMS, sempre é usado o custo histórico. Quando a opção de custo atual é utilizada, a data atual do sistema é usada como data limite. Quando o custo histórico é utilizado, então a data limite do custo é a data da contagem do estoque.

**Dt. Limite:** Se este campo não for informado, o custo apresentado será referente ao da data do campo Dt. Fechamento e o tipo do custo será referente ao selecionado no campo Tipo. Se informado, trará o custo referente à data informada e ao tipo selecionado no campo Tipo.

## Divergência de valores entre o Registro de Inventário e o Relatório Kardex

O **Registro de Inventário** é o relatório que possui finalidade contábil e fiscal, sendo gerado com critérios padronizados de apresentação e precisão, no qual o sistema foi definido para truncar os valores em até 6 casas decimais, desconsiderando valores a partir da 7ª casa decimal.

Ao comparar os valores de estoque com o **Kardex**, é esperado que possam ocorrer diferenças residuais de dízimas, originadas exclusivamente de critérios técnicos de cálculo, arredondamento ou truncamento, e não de divergências reais de estoque ou erro contábil. Ressalta-se que o **Inventário** é a base válida para fins contábeis e fiscais.
 

### 1. A Natureza dos Relatórios: Fiscal vs. Comercial

A estrutura de custos separa as visões de acordo com a finalidade:

- **Registro de Inventário (Oficial/Fiscal):** Documento de **entrega obrigatória**. Utiliza custos de natureza contábil (**Médio com ICMS** ou **Médio sem ICMS**) para valoração por absorção.
- **Kardex (Controle Interno/Comercial):** Ferramenta de apoio à gestão. Quando configurado como **Custo Médio Gerencial**, foca em **preços de venda** e flutuações de mercado, podendo incluir gastos variáveis e fixos.

### 2. Por que o "Custo Médio Gerencial" não consta no Inventário?

Apresentar a nomenclatura "Gerencial" em um documento oficial ao Fisco **não é recomendado**, pois pode gerar interpretações de **divergência na base de cálculo de impostos**.

Por conformidade, o sistema **blinda o Registro de Inventário** contra o uso do Custo Médio Gerencial. Como esse custo inclui componentes não aceitos para valoração fiscal, sua adoção representaria um **risco operacional e jurídico**.

### 3. Como alinhar os valores para Auditoria

Para garantir a **coerência numérica** total em processos de auditoria, a orientação é **unificar o critério** de consulta:

1. Identifique o **custo contábil** adotado pela sua contabilidade.
2. Gere o **Kardex** utilizando este mesmo parâmetro (**Médio com ou sem ICMS**).
3. Gere o **Registro de Inventário** sob o **mesmo critério**.

Assim, ambos os relatórios apresentarão **valores idênticos**.

> **Nota sobre Flexibilidade:** Embora o Registro de Inventário suporte o **Custo Gerencial Atual** e **Histórico**, o **Custo Médio Gerencial** permanece restrito ao Kardex por sua natureza comercial.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#top)

## Quebra

Através do filtro **"Quebra"**, defina o campo que será utilizado para agrupar as linhas do relatório. São disponibilizadas as seguintes opções:

- Não imprimir grupo, ordenado por nome;
- Não imprimir grupo, ordenado por código;
- Imprimir por Grupo, ordenado por nome;
- Imprimir por Grupo, ordenado por código;
- Imprimir por Prioridade/Posse, ordenado por nome;
- Imprimir por Prioridade/Posse, ordenado por código.

Exemplos de Quebras:

**Observação:** um caso especial é quando se utiliza o agrupamento pelo grupo de produto (nome ou código) e o custo com ICMS, pois são impressos no total o custo c/ ICMS, o custo sem ICMS e o imposto recuperável.

Tipo **"Imprimir por Grupo, ordenado por nome"**: Agrupa as linhas pelo grupo do produto ordenando pelo nome do grupo.

Tipo **"Imprimir por Grupo, ordenado por código"**: Agrupa as linhas pelo grupo do produto ordenando pelo código do grupo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#top)

## Formatação

**Página Inicial:** Indica a numeração correspondente à primeira página do relatório. Exemplo: Se a página inicial informada for 3, ao solicitar a geração do relatório a primeira página iniciará com 3.

**Margem Superior:** Possibilidade de você formatar a margem superior do relatório conforme sua necessidade e/ou preferência.

**Margem Esquerda:** Possibilidade de você formatar a margem esquerda do relatório conforme sua necessidade e/ou preferência.

**Formulário:** Possibilidade de você utilizar o formulário em formato **"A4"** ou em **"Carta"**.

**Destacar Linhas:** Se marcado, as linhas serão apresentadas destacadas no relatório.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#top)

## Discriminação

**Complemento:** Se marcado, será apresentado no relatório o complemento referente ao item.

**Localização:** É onde está localizado o produto no estoque. Por exemplo, Prateleira, Almoxarifado, Depósito, etc.

**Nota:** a localização que será impressa, será a informada no campo **"Localização"** ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral)).

**Controle:** Informa o tipo de controle ao qual determinado produto pertence. Exemplo: parceiro, lote, data de validade, lista, sem controle adicional etc.

**Local:** Se o produto for controlado por local, o mesmo será apresentado, ou seja, é o local da disponibilidade do produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#top)

## Outras opções

**Imprimir por** **"Código":** Se selecionado, terá os códigos dos produtos impressos no relatório.

**Imprimir por "Referência":** Se selecionado, os produtos que tiverem referências terão as mesmas impressas no relatório.

**Imprimir por "Nenhum":** Se selecionado, não serão impressos no relatório nem os códigos dos produtos e nem as referências.

**Imprimir Matérias Primas:** Quando a quebra **"Não imprimir grupo, ordenado por nome"** é utilizada, você pode utilizar a opção **"Imprimir matérias-primas"**. Quando essa opção é habilitada, são impressas as matérias-primas de produtos manufaturados, ao invés dos produtos em si. Neste caso, o sistema verifica se o produto pertence ao grupo configurado no parâmetro **"Grupo de Prod.Acabados p/ desmembrar MPs noSintegr - SINTGRUPMP"**. Caso faça parte, ao invés de imprimir o produto, o sistema busca as matérias-primas desse produto e calcula a proporção de cada matéria-prima presente, para obter a quantidade e o custo de cada matéria-prima.

**Imprimir Razão Social:** Através da marcação **"Imprime Razão** **Social"**, você terá a opção de imprimir no cabeçalho do relatório a **"Razão Social da Empresa"**. Quando esta opção estiver desmarcada, será impresso no cabeçalho do relatório o **"Nome de Fantasia"** da empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#top)

## Cópia/Contagem

Estas opções são utilizadas para gerar **"Registro de Inventário"** sem os itens duplicados no relatório quando o mesmo é gerado na mesma data da Cópia e da Contagem do Estoque.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#top)

## Parâmetros e suas aplicabilidades

Em relação aos parâmetros **"Custo por Empresa?** **-** **CUSTOPOREMP"**, **"Controla Custos por Controle?** **-** **CUSTOPORCONT"** e **"Controla Custos por Local?** **-** **CUSTOPORLOC"**, estes são utilizados para definir como os custos serão controlados. Por exemplo, ao configurar a chave de parâmetro CUSTOPOREMP como ligado, o mesmo produto terá uma linha de custo para cada empresa.

Ao utilizar o parâmetro **"Grupo de Prod.Acabados p/ desmembrar MPs noSintegr** **-** **SINTGRUPMP"** e acionar a marcação **"Imprimir Matérias Primas"** (botão Outras Opções...), fará com que os produtos que participam deste grupo sejam desmembrados no relatório de acordo com suas matérias-primas.

**Importante:** ao considerar esta tela, o valor unitário apresentado no registro de inventário considera a quantidade de casas decimais configuradas no parâmetro **"Máscara para valores - \_MVEN"**. Assim, é relevante mencionar que o custo informado neste relatório não está vinculado aos registros inseridos no parâmetro **"Decimais para custo - CUSTODEC"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116253-Registro-de-Invent%C3%A1rio#top)
