---
id: "360053043573"
titulo: "Integração Impostos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-09-15T14:11:12Z"
rotulos: ["Configuração", "Livros Fiscais", "IPI", "ICMS", "Impostos", "br.com.sankhya.mge.comercial.integracaoimpostos", "Painel Principal e Filtros", "Processamento e Busca de Tributos", "Disponível para Grupo IMendes", "PIS/COFINS"]
---

# Integração Impostos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313121054487) Módulo: Livros Fiscais> Avançado          ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42313121055639) Versão disponível: A partir da 4.5
```

---

**Importante:** este recurso só estará disponível para clientes assinantes do serviço com Grupo IMendes.

Para utilizar os recursos disponíveis nesta tela, habilite o parâmetro **"Utiliza integração tributária de Broker? - UTILINTTRIBBROK"**.

Clique nos links abaixo para conhecer as funcionalidades desta tela:

| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#painelprincipal) |  | [Aba Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abafiltros) |
| --- | --- | --- |
| [Aba PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abapis/cofins) |  | [Aba ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abaicms) |
| [Aba IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abaipi) |  | [Botão Processar Tributos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#bot%C3%A3oprocessartributos) |
| [Botão Buscar Tributos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#botaobuscartributos) |  | [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) |
| [Processamento PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#processamentopis/cofins) |  | [Processamento ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#processamentoicms) |
| [Processamento de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#processamentodeipi) |  |  |

                      

## Painel Principal

![Imagem 3: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/4424836527127)

Primeiramente, informe a **"Empresa"** a qual deseja realizar a integração.

**Nota:** você só poderá cadastrar uma integração de impostos por empresa.

Marque a opção **"Ativo"** caso queira que a Empresa em questão esteja habilitada para integrar impostos e buscar tributos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Aba Filtros

Aqui, serão filtrados dados básicos na busca de tributos no broker. Lembrando que, todos os filtros são de preenchimento obrigatório.

Portanto, nas seções **"Uso do Produto"** e **"Característica"** você poderá escolher dentre as opções disponíveis na tela para o filtro.

**Observação:** em versões anteriores a 4.14, quando mais de uma opção de filtro for selecionada em Uso do Produto, será exibida a seguinte mensagem:

**"Consulta impedida! Deverá selecionar somente uma opção de Uso do Produto por Consulta."**

Nas seções **"Filtro Produto"**, **"Filtro UF"** e **"Filtro CFOP"** pode-se selecionar qualquer dado desde que estes já estejam cadastrados no sistema.

**Nota:** na seção Filtro UF, se for utilizado mais de 5 UF’s pode causar aumento exponencial de tempo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Aba PIS/COFINS

Esta aba exibirá todos os resultados de ICMS que foram importados do Broker conforme os dados retornados da API. Você pode consultar a **"Data/Hora"** e o **"Usuário"** que solicitou a busca do tributo em ação.

![Imagem 4: Esta aba exibirá todos os resultados de ICMS que foram importados do Broker conforme os dados retornados da API. Você…](https://ajuda.sankhya.com.br/hc/article_attachments/6113989049367)

**Sub-aba Detalhe Integração Tributo Federal**

Esta sub-aba exibe as informações do detalhe dos tributos de PIS/COFINS obtido na consulta, nas quais você deverá validar e processar por meio do botão ![Imagem 5: Esta sub-aba exibe as informações do detalhe dos tributos de PIS/COFINS obtido na consulta, nas quais você deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/16314263016599) **"Processar Tributos"**, para que as informações contidas possam ser consideradas a partir deste momento.

No campo **"Status Importação"** pode-se consultar o status da importação do tributo, sendo que:

- Quando o status estiver como **"Pendente"**, significa que foi efetuada a busca, porém não foi aceita.
- O status será apresentado como **"Processado"**, quando a busca foi efetuada e aceita, ao acionar o botão Processar Tributos e o processo foi concluído.

Quando o botão **"Excluir"** (disponível na sub-aba Detalhe Integração Tributo Federal das abas PIS / COFINS, [ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abaicms) e [IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abaipi)) for acionado, fará com que os itens da grade e da tabela sejam removidos e assim, ao processar tributos, esses itens não serão atualizados no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Aba ICMS

Esta aba exibirá todos os resultados de ICMS que foram importados do Broker conforme os dados retornados da API. Você pode consultar a **"Data/Hora"** e o **"Usuário"** que solicitou a busca do tributo em ação.

![Imagem 6: Esta aba exibirá todos os resultados de ICMS que foram importados do Broker conforme os dados retornados da API. Você…](https://ajuda.sankhya.com.br/hc/article_attachments/6113974740631)

**Sub-aba Detalhe Integração Tributo ICMS**

Esta sub-aba exibe as informações do detalhe dos tributos de ICMS obtido na consulta, nas quais você deverá validar e processar por meio do botão Processar Tributos, para que as informações contidas possam ser consideradas a partir deste momento.

No campo **"Status Importação"** pode-se consultar o status da importação do tributo, sendo que:

- Quando o status estiver como **"Pendente"**, significa que foi efetuada a busca, porém não foi aceita.
- Se o status apresentar como **"Processado"**, temos que a busca foi efetuada e aceita, ao acionar o botão Processar Tributos.

Quando o campo **"MVA/IVA Ajustada"** for preenchido e posteriormente os impostos processados, o campo **"Calcular MVA Ajustado?"** da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasubstituiotributria) será automaticamente configurado com a opção **"Pelo MVA da Alíquota"** conforme a regra de alíquotas do produto.

Além disso, na sub-aba **"Geral"** serão apresentadas as informações detalhadas:

![Imagem 7: Além disso, na sub-aba "Geral" serão apresentadas as informações detalhadas:](https://ajuda.sankhya.com.br/hc/article_attachments/19975203612823)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Aba IPI

Esta aba exibirá todos os resultados de IPI que foram importados do Broker. Você pode consultar a **"Data/Hora"** e o **"Usuário"** que solicitou a busca do tributo em ação.

![Imagem 8: Esta aba exibirá todos os resultados de IPI que foram importados do Broker. Você pode consultar a "Data/Hora" e o…](https://ajuda.sankhya.com.br/hc/article_attachments/6113976156311)

**Sub-aba Detalhe Integração Tributo IPI**

Esta sub-aba exibe as informações do detalhe dos tributos de IPI obtido na consulta, nas quais você deverá validar e processar por meio do botão Processar Tributos, para que as informações contidas possam ser consideradas a partir deste momento.

No campo **"Status Importação"** pode-se consultar o status da importação do tributo, sendo que:

- Quando o status estiver como **"Pendente"**, significa que foi efetuada a busca, porém não foi aceita.
- O status será apresentado como **"Processado"**, quando a busca foi efetuada e aceita, ao acionar o botão Processar Tributos e o processo ser concluído.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Botão Processar Tributos

Este botão encontra-se nas abas [PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abapis/cofins), [ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abaicms) e [IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#abaipi) desta tela, e processará as linhas do tributo selecionado individualmente.

![Imagem 9: A chave para a busca e processamento dos tributos em questão é o NCM destes, portanto será necessário que todos os…](https://ajuda.sankhya.com.br/hc/article_attachments/6114028999575)
A chave para a busca e processamento dos tributos em questão é o NCM destes, portanto será necessário que todos os produtos inseridos no filtro tenham o NCM informado.

**Importante:** na consulta ao produto a IMendes retorna o NCM proposto, ao Processar Tributos o mesmo será atualizado automaticamente no Cadastro do Produto, passando a ser vigente para o referido produto.

Ao iniciar o processamento do tributo, o sistema exibirá uma mensagem que informa o status em que a importação se encontra.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Botão Buscar Tributos

```
     ![Imagem 10: Botão Buscar Tributos](https://ajuda.sankhya.com.br/hc/article_attachments/42313121056535) Este botão será exibido na régua principal a partir da versão 4.15 do sistema.
```

Realizadas as configurações básicas no Painel Principal e na aba Filtros, efetue a consulta por meio do botão**"Buscar Tributos"**.

![Imagem 11: Realizadas as configurações básicas no Painel Principal e na aba Filtros , efetue a consulta por meio do botão " Buscar…](https://ajuda.sankhya.com.br/hc/article_attachments/9324237260183)

Ao acioná-lo, a comunicação com a IMendes será realizada, retornando para as abas de impostos as principais informações tributárias para atualização/configuração dos respectivos impostos:

- PIS e COFINS
- ICMS
- IPI

Os retornos apresentados são de total responsabilidade da IMendes, sendo assim, qualquer divergência encontrada nas informações obtidas deverão ser enviadas a eles.

Além disso, a consulta será realizada conforme cadastro dos produtos na base do Parceiro IMendes, caso a consulta não retorne nenhum valor, significa que está sendo analisada conforme SLA (Acordo de Nível de Serviço) e será imputado os valores no prazo preestabelecido em seu contrato.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Botão Outras Opções...

Através do botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15526313931671) **"Outras opções..."** você pode realizar a consulta por lotes de marca e por grupos de produtos por meio da opção **"Lotes de Produtos"**

![Imagem 13: Através do botão "Outras opções..." você pode realizar a consulta por lotes de marca e por grupos de produtos por meio…](https://ajuda.sankhya.com.br/hc/article_attachments/9324010361495)

Após efetuar a consulta, o produto selecionado, será apresentado na aba Filtros, seção Filtro Produto, sendo necessário seguir o fluxo da opção Buscar Tributos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Processamento PIS/COFINS

Para o processamento deste, é necessário habilitar o parâmetro **"Grupo do imposto federal na Int. Tributária - INTTRIBGRUPIMPF"**. Assim, utilizaremos para gerar o nome de grupo dos impostos importados, e utilizaremos da variável "$NCM" que contém o NCM processado atualmente.

Este processamento efetua a inclusão das regras nas telas [Alíquota de Pis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434) e [Alíquota de Cofins](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813) considerando as informações obtidas na consulta para entrada e saída.

![Imagem 14: Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBF) para as tabelas do Sankhya Om :](https://ajuda.sankhya.com.br/hc/article_attachments/4410702263191)Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBF) para as tabelas do Sankhya Om:

![Imagem 15: Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBF) para as tabelas do Sankhya Om :](https://ajuda.sankhya.com.br/hc/article_attachments/360085872833)

![Imagem 16: Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBF) para as tabelas do Sankhya Om :](https://ajuda.sankhya.com.br/hc/article_attachments/360085876733)

![Imagem 17: Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBF) para as tabelas do Sankhya Om :](https://ajuda.sankhya.com.br/hc/article_attachments/360085876973)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Processamento ICMS

Este processamento efetua a inclusão das regras na tela [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934) considerando as informações obtidas na consulta por estado:

![Imagem 18: Este processamento efetua a inclusão das regras na tela Alíquota de ICMS considerando as informações obtidas na…](https://ajuda.sankhya.com.br/hc/article_attachments/4410710247447)

**Importante:** para que essa configuração seja priorizada você deve configurar por meio do botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#botooutrasopes...) a **"Prioridade das Restrições"** por NCM, que será o padrão de inclusão.

![Imagem 19: Importante: para que essa configuração seja priorizada você deve configurar por meio do botão Outras Opções... a…](https://ajuda.sankhya.com.br/hc/article_attachments/4410702972439)

Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBI) para as tabelas do Sankhya Om:

![Imagem 20: Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBI) para as tabelas do Sankhya Om :](https://ajuda.sankhya.com.br/hc/article_attachments/360084691194)

![Imagem 21: Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBI) para as tabelas do Sankhya Om :](https://ajuda.sankhya.com.br/hc/article_attachments/360084691814)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Processamento de IPI

Neste, utilize o parâmetro **"Descricao do imposto IPI na Int. Tributária - INTTRIBDESCRIPI"**, que por sua vez definirá a descrição da Alíquota de IPI cadastrada e todos os NCMs vinculados serão inseridos na nova rotina localizada no cadastro de [Alíquota de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013), aba [NCM](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abaNCM).

Este processamento efetua a inclusão das regras na tela Alíquota de IPI considerando as informações obtidas na consulta:

![Imagem 22: Este processamento efetua a inclusão das regras na tela Alíquota de IPI considerando as informações obtidas na consulta:](https://ajuda.sankhya.com.br/hc/article_attachments/4410710378135)

Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBF) para as tabelas do Sankhya Om:

![Imagem 23: Observe abaixo o de-para no processamento do tributo da tabela intermediária (TGFDITBF) para as tabelas do Sankhya Om :](https://ajuda.sankhya.com.br/hc/article_attachments/360085883693)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)

## Informações Adicionais

A consulta à IMendes poderá ser efetuada por código de barras ou código do produto, conforme definição determinada na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), campo **"Considerar na Integração Impostos"**:

![Imagem 24: A consulta à IMendes poderá ser efetuada por código de barras ou código do produto, conforme definição determinada n a…](https://ajuda.sankhya.com.br/hc/article_attachments/4410710620055)

Lembrando que, para os produtos definidos como Código de barras deve ser informado na aba [Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacdigodebarras) a **"Unidade de Volume"**.

![Imagem 25: Lembrando que, para os produtos definidos como Código de barras deve ser informado na aba Código de Barras a "Unidade…](https://ajuda.sankhya.com.br/hc/article_attachments/4410703452183)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos#top)
