---
id: "360044602934"
titulo: "Alíquotas de ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:24:27Z"
rotulos: ["AJUDA DO SKW", "manual", "Alíquotas", "Configuração", "Frete", "ICMS", "Alíquotas de ICMS manual", "Impostos", "Substituição Tributária", "Alíquotas de ICMS", "Combustível", "CTEPARCTOMDICMS", "Garantido Integral", "Percentual de Outorga", "PERCSTCAT137SP", "PODEDUPALIQICMS", "Redução da Base", "RIOLOG", "UF Destino", "UF Origem", "br.com.sankhya.com.cad.aliquotasicms", "HABFORMASREPRED", "IMPCOD1RALIQICM", "ENDICMS", "ORDENAALIQCAD", "ALQDECRETO54308", "Cadastro Alíquotas ICMS", "NAOCONSIDMVA", "MINTCALCSTSPEC8", "CONSALIQINT0RS.", "LAZYALIQICMS", "Comercial"]
---

# Alíquotas de ICMS

```
 Módulo: Comercial > Arquivo > Cadastros > Alíquotas
```

---

Nesta tela são configuradas as alíquotas de ICMS a serem utilizadas para cálculos deste imposto nas Operações de Entrada e Saída. O sistema está preparado para trabalhar com várias regras e exceções de alíquotas de Estado para Estado. Por meio dessas exceções são configuradas diversas possibilidades de tributações. A combinação das regras e exceções deve abranger a totalidade das operações da empresa.

É necessário que se tenha bastante cuidado ao realizar o cadastro das Alíquotas de ICMS, pois falhas podem ocasionar em prejuízos para a empresa junto aos órgãos de fiscalização.

Quando o parâmetro `LAZYALIQICMS` está **habilitado**, o sistema altera o método de carregamento das grades da tela de Alíquota de ICMS:

1. **Carregamento "Sob Demanda":** O Sankhya não carrega todas as linhas de dados e todas as grades disponíveis de uma única vez ao abrir a tela.
2. **Performance:** Os dados são carregados de forma progressiva, conforme a necessidade do usuário (ex: ao rolar a tela ou selecionar uma grade), garantindo uma **performance superior** e evitando lentidão ou travamento da tela em ambientes com grande volume de informações.

Para facilitar sua navegação nas funcionalidades dessa rotina, acesse os links abaixo:

| Funcionalidades da Tela | |
| --- | --- |
| [Cadastrando uma Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#cadastrandoumaalquotadeicms) | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral) |
| [Aba Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abafrete) | [Aba Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasubstituiotributria) |
| [Aba SIMPLES Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasimplesnacional) | [Validações que facilitam este cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#validaesquefacilitamestecadastro) |
| [Aba ICMS Antecipado Entradas...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abaicmsantecipadoentradasinterestaduais) | [Validações que facilitam este cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#validaesquefacilitamestecadastro) |
| [Cálculo do ICMS "Garantido Integral"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#clculodoicmsgarantidointegral) | [Cálculo de ICMS por distinção de alíquotas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#clculodeicmspordistinodealquotassimilares) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#botooutrasopes...) |  |

![Imagem 1: Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/21376275216023)

A árvore hierárquica localizada à esquerda da tela exibe a **"Sigla"** da Unidade Federativa e sua respectiva **"Descrição"**. Quando a UF for **"EX"** significa que se trata de um destino ou origem estrangeira e é exibido dessa forma tanto para importação quanto para exportação.

**Nota:** os registros que possuem exceção configurada, contém o código dessa exceção em sua descrição para facilitar sua identificação.

**Observação:** caso queira que sejam apresentadas todas as regras de alíquotas configuradas independente do **"Cód. Restrição"** na árvore de hierarquias, o parâmetro **"Imprime cód. 1a restrição na árvore de alíq. ICMS? - IMPCOD1RALIQICM"** deve estar desligado; assim, o sistema não irá imprimir o código da primeira restrição na pasta, criando apenas uma pasta por tipo de primeira restrição.

Para que os registros "filhos" fiquem em ordem alfabética ou numérica, deverá ser ativado o parâmetro **"Ordena cadastro de Alíquotas ICMS - ORDENAALIQCAD"**.

Através do parâmetro **"Endereço para ICMS - ENDICMS"**, configure qual dos endereços no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) (entrega, recebimento ou principal) o sistema irá utilizar para calcular ICMS. Esta opção é utilizada quando os endereços cadastrados para o parceiro são de cidades diferentes.

### Cadastrando uma Alíquota de ICMS

Primeiramente, determine por meio da árvore hierárquica quais serão os estados de **"Origem"** e **"Destino"** a receber a nova alíquota. Em seguida, acione o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15993376476311) **"Cadastrar Alíquotas de ICMS"** para que os campos sejam habilitados. Sendo eles:

O campo **"Código"** é preenchido automaticamente e se refere ao código da alíquota que está sendo cadastrada. Esse mesmo número também é apresentado na árvore de pesquisa entre parênteses logo à frente da descrição do nome da alíquota.

Selecione o estado de origem da operação no campo **"UF Origem"** sempre com relação à empresa do sistema, ou seja, para operações de saída, defina o estado da empresa; para operações de entrada, o estado do parceiro.

De forma inversa ao campo anterior, no campo **"UF Destino"** seleciona-se o estado para onde se encaminha o produto, ou seja, o estado do parceiro cliente quando se tratar de venda ou o estado da empresa quando se tratar de compra.

Exemplos:

- **Na Venda:** para uma empresa de Minas Gerais e o parceiro (cliente) de São Paulo, a UF Origem será MG e a UF Destino será SP.
- **Na Compra:** para um parceiro (fornecedor) de Goiás e a empresa de Minas Gerais, a UF Origem será GO e a UF Destino será MG.

#### Seção Exceções

Nesse espaço, determine o tipo de exceção. Esses campos serão utilizados quando for necessário informar uma alíquota exclusiva para um tipo de cliente, produto, grupo de produtos. A opção **"sem exceção"** representa a regra geral. 

Existem situações em que a empresa precisa configurar suas regras de cálculo de impostos nas notas fiscais de acordo com o NCM dos produtos pois, dessa forma, as definições das regras ficam mais fáceis. O sistema permite definir regras de cálculo do imposto das notas fiscais de acordo com o NCM dos produtos negociados. Sendo assim, o sistema buscará as devidas alíquotas para cada produto lançado na central.

Para isso, tem-se na tela Cadastro de Alíquotas de ICMS (Tipo 1 e Tipo 2) várias opções de exceções, dentre elas:

- **Por capítulo do NCM:** ao selecionar essa opção, será apresentado um campo para informar no máximo 2 dígitos numéricos. O valor digitado é salvo no campo Código de Restrição e servirá como base de regra para enxergar as duas primeiras casas do código NCM do produto.
- **Por posição do NCM:** escolhendo essa opção, o sistema apresentará um campo para que seja digitado no máximo 4 números. Essa opção servirá como base de regra para enxergar as 4 primeiras casa do código NCM do produto.
- **Por NCM:** com essa opção selecionada, o sistema apresentará um campo para que sejam digitados no máximo 8 números. Essa opção também servirá como base de regra para enxergar o código NCM do produto. No lançamento da nota, o sistema irá verificar a regra configurada na alíquota e validará com os produtos presentes na nota. Se a regra definida na alíquota for por capítulo, posição ou o próprio NCM será validado com o NCM do produto lançado na nota de acordo com suas posições conforme foi citado acima.
- **Por perfil principal:** pode-se configurar as exceções de diversas formas, uma delas é em relação ao Perfil Principal. Essa exceção leva em consideração a informação contida no campo **"Perfil Principal"** localizado no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao). Sendo assim, não serão considerados os dados contidos na aba [Perfil do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaperfildoparceiro).
- **Por tipo de transporte de importação:** Essa opção somente funcionará em notas de importação (o módulo Importação ainda não existe no **Sankhya Om**), sendo possível utilizar esta funcionalidade somente em integração com o MGE Importação. A informação do tipo de transporte será apresentada na aba Transporte da nota de importação desse último. O campo para definição do tipo de transporte de importação contém as seguintes opções para escolha:

- - - 01 – MARITIMA;
    - 02 – FLUVIAL;
    - 03 – LACUSTRE;
    - 04 – AEREA;
    - 05 – POSTAL;
    - 06 – FERROVIARIA;
    - 07 – RODOVIARIA;
    - 08 – TUBO-CONDUTO;
    - 09 – MEIOS PROPRIOS;
    - 10 – ENTRADA FICTA;
    - 11 – OUTROS MEIOS.
- **Regra Consumidor Final:** utilizará a alíquota interestadual priorizando a exceção para Consumidor independente da hierarquia, sendo que, pode-se aplicar outra alíquota que mais se aproxime da operação caso não exista uma específica para essa classificação fiscal.

**Nota:** caso o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado na operação não esteja com a opção **"Calcular DIFAL Partilhado"** localizada na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) selecionada ou uma das configurações para cálculo do DIFAL não esteja realizada ([Partilhas DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111373-Partilhas-DIFAL), % de alíquota interna de destino) o sistema irá considerar a alíquota de ICMS de dentro do estado.

- **Regra Consumidor Contribuinte:** primeiro verifica se tem exceção de ICMS para eles fora do estado, se não tiver, será analisado se tem exceção para eles dentro do estado. A regra para fora do estado será aplicada se na exceção **"Tipo 1"** a opção Consumidor Contribuinte for selecionada, sendo que esta opção será utilizada nessas operações mesmo que ela seja menos prioritária que as demais. Caso contrário, o sistema buscará a regra dentro do estado.
- **Regra Produtor Rural:** verifica-se a exceção de produtor rural de acordo com as UF's envolvidas, senão encontrar exceção de produtor rural então considera a exceção mais próxima do processo que esta sendo negociado dentro ou fora do estado. Como por exemplo: Exceção por produto, grupo de produto, ICMS do parceiro.
- **Regra Consumidor Final e Consumidor Contribuinte:** caso não se encontre nada de acordo com o descrito anteriormente será feito da seguinte forma: Considera a exceção de dentro do estado mais próximo do processo que está sendo negociado. Assim, tem-se por exemplo: Exceção por produto, grupo de produto, ICMS do parceiro.
- **Por grupo de ICMS do parceiro:** ao utilizar a exceção **"por grupo de ICMS do parceiro"** (configuração realizada no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Grupo ICMS/ISS por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abagrupoicmsissporempresa)), caso o parâmetro **"Busca alíq. ICMS referenciando parc. tomador CT-e? - CTEPARCTOMDICMS"** esteja ligado, tendo na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) o lançamento de um CT-e e o Parceiro Tomador desse CT-e sendo informado, este parceiro será utilizado para referenciar o Grupo de ICMS do Parceiro na Alíquota de ICMS; no momento da inclusão do CT-e, especificamente quando ocorrer o cálculo do ICMS, o sistema busca a alíquota de ICMS tendo como base o parceiro tomador de serviço do CT-e.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Aba Geral

## Imagem 3: Aba Geral

**Observação:** quando a regra de alíquotas for criada ao processar os impostos, os campos dessa aba serão preenchidos conforme os valores da sub-aba **"Detalhes Integração Tributo ICMS"** da aba [ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573#abaicms) da tela [Integração Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573).

A tributação selecionada no campo **"Tributação"** será usada na composição do **"CST – Código da Situação Tributária"**, utilizado na geração das Notas e Livros Fiscais, conforme descrito abaixo: 

- 00 - Tributada integralmente;
- 02 - Tributação monofásica própria sobre combustíveis;
- 10 - Tributada e com cobrança do ICMS por ST;
- 15 - Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis;
- 20 - Com redução de base de cálculo;
- 30 - Isenta ou não tributada e com cobrança do ICMS por ST;
- 40 - Isenta;
- 41 - Não tributada;
- 50 - Com suspensão;
- 51 - Com diferimento;
- 53 - Tributação monofásica sobre combustíveis com recolhimento diferido;
- 60 - ICMS cobrado anteriormente por substituição;
- 61 - Tributação monofásica sobre combustíveis cobrada anteriormente;
- 70 - Com redução de base de cálculo e cobrança do ICMS por ST;
- 90 - Outras.

Os CST's compatíveis com os parceiros classificados como **"Consumidor Final Não Contribuinte"** (tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), campo **"Classificação ICMS"**), são:

- 00 - Tributada integralmente;
- 20 - Com redução da Base de Cálculo;
- 40 - Isenta;
- 41 - Não tributada;
- 60 - ICMS cobrado anteriormente por Substituição Tributária.

**Nota:** podem acontecer situações em que na emissão do [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834-Conhecimento-de-Transporte-Eletr%C3%B4nico-CT-e), o tomador do serviço precise recolher o ICMS antecipadamente através de guia, com base em um regime e conforme seu Estado. Nesse caso, a transportadora precisa emitir o CT-e com a tributação do imposto igual à **"60 - ICMS cobrado anteriormente por substituição"**. Além disso, a tag **<ICMS60>** é gerada no XML do CT-e emitido quando ocorrer esse cenário.

Ao emitir uma nota fiscal com itens configurados com CST 60 e o Tipo de Cálculo de ST Específico igual a **"14 - Cálculo ICMS e ICMS ST - Decreto 38.296/PE"**, o valor do ICMS ST calculado sobre os itens e sobre as despesas acessórias proporcionais a eles, não serão somados ao total da nota fiscal.

Com a opção de tributação igual a 14 - Cálculo ICMS e ICMS/ST - Decreto 38.286/PE selecionada e o parâmetro **"Buscar %Coefic Custo Aquisição Última Compra - COCUSTULTCOMP"** ligado, o sistema irá localizar o Percentual/ Coeficiente sobre Custo Aquisição-PE e/ou Percentual/Coeficiente sobre Custo Aquisição - PE - Origem Estrangeira da última compra de mercadoria para calcular o ICMS e o ICMS ST. Sendo:

```
 BC ST = Custo Médio (campo ?Tipo de custo Decreto 38.296/PE? da aba Geral)*(1 +
(MVA/100))
ICMS ST = BC ST * (Aliq ST / 100) - ICMS Próprio
```

Além disso, o sistema irá localizar a última nota de compra para encontrar a origem da mercadoria. Sendo assim, o MVA configurado na alíquota de compra será utilizado no cálculo no momento da saída.

---

**Cálculo de ICMS-ST: Tratamento Específico para o Rio Grande do Sul (RS)**

Para empresas localizadas no Rio Grande do Sul, o sistema Sankhya utiliza uma lógica de validação adicional para o cálculo da Substituição Tributária (ST), que é controlada pelo parâmetro **CONSALIQINT0RS**.

O parâmetro CONSALIQINT0RS**está configurado como LIGADO (S)** por padrão. Essa configuração aplica a particularidade de verificar o parâmetro **ALQDECRETO54308** (que armazena a Alíquota interna p/ decreto 54308/2018 de RS).

#### Comportamento da Regra

O resultado da busca pela alíquota depende da combinação desses dois parâmetros:

- **Regra Geral (Comportamento de Outros Estados):**
  - Se **CONSALIQINT0RS = N (Desligado)** e **ALQDECRETO54308 = 0**, o sistema busca a regra geral de ST, conforme o rastreamento padrão de outras Unidades da Federação.
- **Prevalência do Valor Informado:**
  - Se ALQDECRETO54308 **tiver um valor maior que zero (> 0)**, **esse valor será utilizado** no cálculo, **independentemente** do status do CONSALIQINT0RS (seja S ou N).

**Busca em Operação de Revenda RS para RS (CST 60):**

- Se CONSALIQINT0RS = S**(Ligado)** e ALQDECRETO54308 = 0, a busca da alíquota para preencher a tag <pST> em uma nota fiscal de venda (RS para RS) com CST 60 segue uma prioridade específica:

**a.** **Valor Fixo no Parâmetro:** O sistema primeiramente verifica se o campo "Número Decimal" do parâmetro ALQDECRETO54308 está preenchido. Se sim, essa alíquota é informada na tag <pST>.

**b.** **Prioridades de Restrições:** Caso o "Número Decimal" não tenha sido informado (ou seja, o valor é zero), o sistema buscará a alíquota nas "Prioridades de Restrições" (acessível pelo botão Outras Opções), seguindo rigorosamente a ordem abaixo. Ao encontrar uma exceção válida para a nota, o sistema utiliza o campo Alíquota da TGFICM para alimentar a tag <pST>:

- por NCM;
- por grupo de ICMS do produto;
- por TOP;
- por produto.

**c.** **Valor-Padrão:** Se nenhuma exceção for encontrada, será informado o valor presente no campo Alíquota da aba principal (Alíquotas de ICMS).

#### Instrução de Uso

- Se a empresa do RS deve seguir a regra fiscal especial, mantenha CONSALIQINT0RS = S.
- Se a empresa do RS não deve seguir a regra especial, **desative (N)** o parâmetro CONSALIQINT0RS.

**Observação:** Lembre-se que um valor diferente de zero em ALQDECRETO54308 sempre prevalecerá no cálculo.

---

**Emissão de notas com diferimento zerado**

Ative esta opção para emitir NF-e para o estado de Santa Catarina (SC) utilizando CST 51. Assim, o Sankhya OM gera as tags de diferimento (<pDif> e <vICMSDif>) no XML da nota **quando o percentual de diferimento é zero, evitando a Rejeição 351.**

Como configurar:

1. Acesse a aba **Geral**.

2. Navegue até **Configuração**.

3. Marque a opção **Gerar tags de diferimento zerado**.

![Imagem 4: 3. Marque a opção Gerar tags de diferimento zerado .](https://ajuda.sankhya.com.br/hc/article_attachments/35440441368599)

![Imagem 5: Para todas as outras operações que não se enquadram nesta regra específica, mantenha este parâmetro desmarcado para…](https://ajuda.sankhya.com.br/hc/article_attachments/23765533194135)Para todas as outras operações que não se enquadram nesta regra específica, mantenha este parâmetro desmarcado para evitar outras rejeições.

**Nota:** quando a opção 61 - Tributação monofásica sobre combustíveis cobrada anteriormente for selecionada, a tag **<IEST>** do XML da Nota de Venda será preenchida com a informação do campo **"Inscrição Estadual"** da aba [Insc. Estadual Contribuinte ST no Estado Dest.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abainsc.estadualcontribuintestnoestadodest.) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

No campo **"Alíquota"** é definida a alíquota de ICMS do Estado de origem para o Estado de destino selecionado. 

O campo **"Redução da base"** definirá o percentual de redução sobre a base de cálculo do ICMS, se houver.

Para que o campo **"% ICMS FCP Interno"** seja considerado quando for informado algum valor, será necessário habilitar a marcação **"Calcular FCP (ICMS/ST) Interno?"** na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), bem como a Empresa estar configurada para [NF-e 4.00](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00) e o campo Tributação (dessa tela e aba em referência) possuir uma das opções abaixo selecionada:

- 00 - Tributada integralmente;
- 10 - Tributada e com cobrança do ICMS por ST;
- 20 - Com redução de base de cálculo;
- 51 - Com diferimento;
- 70 - Com redução de base de cálculo e cobrança do ICMS por ST;
- 90 - Outras.

O campo **"Alíquota ad rem ICMS"** refere-se ao ICMS dos combustíveis que será o mesmo em todo país e terá a alíquota ad rem, isso é, por um valor fixo por unidade de medida, sendo estes o diesel gasolina e etanol anidro, e o quilograma para o GLP. 

O campo acima será habilitado somente quando o campo Tributação for preenchido com as seguintes opções:

- 02 - Tributação monofásica própria sobre combustíveis;
- 15 - Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis;
- 53 - Tributação monofásica sobre combustíveis com recolhimento diferido;
- 61 - Tributação monofásica sobre combustíveis cobrada anteriormente.

![Imagem 6: Para mais informações sobre o ICMS monofásico dos combustíveis, consulte as Notas ICMS Monofásico - CST's 02, 15, 53 e…](https://ajuda.sankhya.com.br/hc/article_attachments/16025028111127) Para mais informações sobre o ICMS monofásico dos combustíveis, consulte as [Notas ICMS Monofásico - CST's 02, 15, 53 e 61](https://ajuda.sankhya.com.br/hc/pt-br/articles/17111591056151).

**Observação:** quando o campo acima for configurado, o campo **"Vlr. Substituição"** dos [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) da nota será preenchido conforme regra abaixo:

```
 Base Substituição * Alíq. ICMS
```

Desse modo, observe o exemplo abaixo:

**Base ICMS:** 100.0000

**Alíquota ad rem ICMS:** 0,9456

**Vlr. ICMS:** 100.0000 \* 0,9456 = 94,56

O campo **"Base para cálculo do FCP interno"** permite configurar a forma que será calculado o FCP em operações internas, de acordo com as seguintes opções:

- **Valor da Operação:** se escolher essa opção, o sistema calculará a base do FCP interno de acordo com os valores dos produtos;
- **Base do ICMS:** através dessa opção, o sistema irá calcular a base do FCP interno utilizando a base do ICMS.

Caso o campo Tributação presente na aba Geral esteja definido com a opção **"Diferimento"**, o campo Alíquota também da aba Geral preenchido com valor maior que "0" (zero) e o campo **"% de Outorga/Diferimento"** preenchido com um valor diferente de "0" (zero) será considerado com uma divergência parcial, onde o valor do campo Tributação será alterado para **"Outras"** e o cálculo será realizado da seguinte maneira:

1. Se a Alíquota for maior que % de Outorga/Diferimento, o valor do ICMS será calculado através do resultado da subtração entre Alíquota e % de Outorga/Diferimento;
2. Se a Alíquota for menor que % de Outorga/Diferimento, o valor do ICMS será "0" (zero).

Em situações em que há notas de Devolução com Diferimento é possível encontrar o seguinte cenário:

Suponha que em 2023 uma nota de Venda ou Compra tenha sido lançada com um Diferimento de 30%. No entanto, em 2024, o cálculo do Diferimento tenha sido ajustado para 40%. Nesse contexto, ao registrar uma nota de Devolução, o sistema considera o novo Diferimento de 40%, ignorando o Diferimento utilizado no lançamento da nota original.

Isso ocorre porque, ao emitir a nota de Devolução, o sistema se baseia no Diferimento indicado na Alíquota de ICMS no momento da emissão da Devolução, em vez de considerar o Diferimento utilizado na emissão da nota original.

Para lidar com esses casos, utilize os parâmetros abaixo para contornar a situação:

- **Convert % diferimento em devol. (idAliqICMS:0.0;) - CONVPERDIFDEV:** este é responsável por informar o código da Alíquota de ICMS e o percentual que será utilizado durante a geração, exemplo:

Código da Alíquota de ICMS = 214 e 215

No parâmetro deve ser configurado: 214:33;215:35.55

- **Data lim. p/ obter % de diferimento via parâmetro - DTALIOBTPDIFDEV:** neste se determina a data limite que irá monitorar a conversão de percentual de Diferimento, por exemplo:

Houve a alteração no dia 13/03/2023, então deve ser informada a data 12/03/2023, se necessário o mesmo pode informar outra; a rotina irá comparar se a data de negociação da nota é inferior ou igual a data informada no parâmetro DTALIOBTPDIFDEV, se for irá obter o valor do diferimento informado no parâmetro CONVPERDIFDEV. Caso contrario, irá seguir o caminho padrão buscando da Alíquota de ICMS.

A marcação **"Cálculo Diferimento Por Dentro"** possibilita calcular o valor correto da **"CST 51-Diferimento"** selecionada no campo Tributação dessa aba.

**Importante:** referente à desoneração de ICMS do Estado do Rio de Janeiro, tem-se a seguinte fórmula vinculada à esse campo:

```
  ICMS diferido = Preço na Nota Fiscal / (1 - Alíquota) * Alíquota
```

**Nota:** com a marcação Cálculo Diferimento por Dentro habilitada, o sistema irá emitir uma nota fiscal com ICMS Diferido desde que:

**(1)** A opção **"NT 2020.005"** do campo **"Versão NT"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) esteja selecionada;
**(1)** Possua o campo **"Tipo de Cálculo DIFAL e do FCP"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral) dessa tela configurado com a opção **"0 - Sem considerar redução da Base"**;
**(1)** Além de selecionada a opção **"51-Diferimento"** do campo Tributação também dessa tela.

Desse modo, os valores de FCP Diferido serão gerados na tag <**pFCPDif**> na geração do XML, além de que, a base do cálculo do ICMS e do FCP irão realizar o cálculo por dentro da seguinte maneira:

```
 Valor da operação / (1 - (Alíq ICMS + Aliq FCP ))
```

O campo **"Tabela c/base p/ICMS"** está vinculado a marcação **"Usar a maior base para ICMS"**; esses dois campos influenciarão o cálculo do ICMS da seguinte forma:

1. Se houver tabela informada no campo Tabela c/base p/ICMS e a marcação Usar a maior base para ICMS não estiver efetuada, o cálculo do ICMS será com base na tabela.
2. Se houver tabela informada no campo Tabela c/base p/ICMS e a marcação Usar a maior base para ICMS estiver realizada, o cálculo de ICMS será com base no maior valor.
3. Se não houver tabela informada no campo Tabela c/base p/ICMS, o cálculo de ICMS será com base na alíquota do produto.

O objetivo do campo **"Modalidade BC ICMS"** é de codificar as movimentações, facilitando a identificação delas por parte do fisco. Através da **"Nota Fiscal Eletrônica - NF-e"** e/ou **"Escrituração Fiscal Digital - EFD"**, esse campo fornecerá informações referentes à modalidade para Base de Cálculo de ICMS, para o Sistema Público de Escrituração Digital (SPED).

**Nota:** outros arquivos magnéticos, exigidos pelo Governo também poderão utilizar tais informações.

**Observação:** caso seja necessário, é possível definir uma observação padrão por alíquota que será impressa na nota fiscal pelas Variáveis de TXT. A observação informada nesse campo deverá ser previamente cadastrada na tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474-Observa%C3%A7%C3%B5es-para-Notas).

**Importante:** ao vincular uma Observação no Cadastro de Alíquotas de ICMS e essa mesma observação no Item da Nota, campo **"Obs Padrão"**, após a escrituração e geração do [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI), ao consultar o arquivo, o Registro C190 vinculado à essa Nota apresentará a Observação descrita no campo 12, bem como também será apresentada no Registro 0460.

**Nota:** caso seja apresentada apenas uma observação, o campo será preenchido com ela; por outro lado, apresentando mais de uma, o campo será ocupado com a primeira observação localizada.

O campo **"Código Motivo de Desoneração do ICMS"** foi criado para atender a NT2011.004 e conta com as opções listadas abaixo:

- 1 - Táxi;
- 2 - Deficiente Físico (Desativado);
- 3 - Produtor Agropecuário;
- 4 - Frotista/Locadora;
- 5 - Diplomático/Consular;
- 6 - Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio;
- 7 - SUFRAMA;
- 8 - Venda a Órgãos Públicos;
- 9 - Outros;
- 10 - Deficiente Condutor (Convênio ICMS 38/12);
- 11 - Deficiente Não Condutor (Convênio ICMS 38/12);
- 12 - Órgão de Fomento e Desenv. Agropecuário;
- 16 - Olimpíadas Rio 2016;
- 90 - Solicitado pelo Fisco.

Por padrão, o campo acima é vazio. Para obter mais informações, acesse a documentação sobre [Desoneração do ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597834-Desonera%C3%A7%C3%A3o-do-ICMS).

**Observação:** no XML das notas será criado o grupo de tag **<detPag>** no grupo pag quando a soma de todos os títulos da nota forem diferentes do total da nota (tag 'vNF'), ou seja, será criado um novo grupo **<detPag>** com **<indPag>** igual a 0 = À vista, **<tPag>** igual a 90 (Sem pagamento) e **<vPag>** que será a diferença entre o valor total da nota e a soma dos títulos.

**Observação:** para que o sistema considere a base sem redução para o cálculo do percentual de repasse SUFRAMA, habilite o parâmetro **"Repasse SUFRAMA p/ base ST com reduo base ICMS? - SUFRAMABASERED"**.

O preenchimento do campo **"Alíquota p/ Origem Estrangeira"** está relacionado ao cálculo [ICMS para produtos de Origem Estrangeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111873-ICMS-para-produtos-de-Origem-Estrangeira).

Informe no campo **"Redução da Base para Origem Estrangeira"** o valor de redução da base estrangeira que será aplicada no cálculo de ICMS e ICMS ST.

**Nota:** para realizar o Cálculo do ICMS diferenciado para a revenda de veículos, as configurações abaixo deverão ser realizadas:

- Primeiramente, na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional), campo **"Controlar por"** selecione qualquer opção que seja diferente de **"Sem controle adicional"**.
- Depois, na tela Cadastro de Alíquotas de ICMS, desde que a UF Origem e Destino sejam iguais, nessa aba, a marcação **"Utilizar diferença positiva"** deverá estar habilitada e o campo **"Multiplicador para cálculo"** preenchido com valor diferente de 0 (zero).

Sendo assim, ao gerar uma Nota de Venda do veículo e as telas estando configuradas de forma correta, o sistema realizará a busca da última Nota de Compra que possua a mesma combinação de Produto/Controle. Assim, o valor unitário do item desta nota será utilizado para o cálculo da base ICMS.

Esse cálculo será feito da seguinte forma:

```
  1) Base ICMS = (Valor da venda-valor da compra)*Multiplicador para cálculo/alíquota ICMS
           2) Valor ICMS = Base ICMS * alíquota ICMS.
```

Desse modo, caso a base seja de valor menor ou igual a zero, o item na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) será gerado com **"Base ICMS"** e **"Vlr. ICMS"** iguais a zero e **"Tributação"** = **" 41-Não tributada"**.

O campo **"Percentual/Coeficiente sobre Custo Aquisição - PE"** apenas estará disponível para preenchimento se a opção **"14 - Cálculo ICMS e ICMS/ST - Decreto 38.286/PE"** do campo **"Tipo de Cálculo de ST Específico"** da aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/abasubstituiotributria) estiver selecionada ou caso o estado de destino seja igual a Pernambuco. Nesse campo, informa-se o percentual referente ao indicador sobre o custo de aquisição correspondente à entrada mais recente de mercadoria, conforme os decretos nº 38.213 de 28/05/12 e nº 38.296 de 12/06/12 - PE.

O funcionamento do campo **"Percentual/Coeficiente sobre Custo Aquisição - PE - Origem Estrangeira"** ocorrerá da mesma forma que o campo Percentual/Coeficiente sobre Custo Aquisição - PE, porém ele será utilizado para mercadorias procedentes do exterior.

**Observação:** com a opção de Tributação 14 - Cálculo ICMS e ICMS/ST - Decreto 38.286/PE selecionada e o parâmetro **"Buscar %Coefic Custo Aquisição Última Compra - COCUSTULTCOMP"** ligado, o sistema irá localizar o Percentual/ Coeficiente sobre Custo Aquisição-PE e/ou Percentual/Coeficiente sobre Custo Aquisição - PE - Origem Estrangeira da última compra de mercadoria para calcular o ICMS e o ICMS ST. Além disso, o sistema irá localizar a última nota de compra para encontrar a origem da mercadoria. Sendo assim, o MVA configurado na alíquota de compra será utilizado no cálculo no momento da saída.

Ao habilitar a marcação **"Calcular % de Redução BC ICMS Lei 9.025/2020"**, o valor calculado será exibido nos campos Redução de Base e % da Base ICMS e estes campos, por sua vez, ficarão desabilitados.

Se o campo **"Alíquota da Carga Tributária Reduzida"** não for preenchido e for realizado a seleção da marcação Calcular % de Redução BC ICMS Lei 9.025/2020, o cálculo da referida redução não será realizado e o sistema apresentará a mensagem:

**"O campo "Alíquota da Carga Tributária Reduzida" deve estar preenchido para utilizar a opção "Calcular % de Redução BC ICMS Lei 9.025/2020"."**

**Exemplo de cálculo de ICMS Próprio, Desonerado e Redução de BC ST**

**(1)** Cálculo ICMS Próprio = BC ICMS \* (1 - % da Redução de BC)

- BC ICMS Reduzido = 117,20 \* (1 - 0,40) = 70,32
- Valor do ICMS Próprio = 70,32 \* (18% + 2%) = 14,06

**(1)** ICMS Desonerado = Preço na Nota Fiscal \* (1 - (Alíquota padrão \* (1 - Percentual de redução da BC))) / (1 - Alíquota padrão) - Preço na Nota Fiscal

- Preço na Nota Fiscal = 117,2
- Alíquota Padrão = 18% + 2% FCP
- Percentual de redução da BC = 1 - (12% / (18% + 2%)) = 1 - 60% = 40%
- ICMS Desonerado = 117,20 \* (1 - (0,20\*(1-0,40))) / (1-0,20)-117,20 = 11,72

 **Nota:** neste cálculo não será considerada a alíquora de FPC da desoneração do ICMS ST.

O campo **"% Redução Alíquota ad rem ICMS"** deve ser completado apenas caso o campo Tributação for definido com a opção 15 - Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis. Desse modo, quando completo, ao gerar o valor do campo **"Valor ICMS Monifásico"** (tag <**vICMSMono**>), o seguinte cálculo será realizado:

```
  <qBCMono> x ( <adRemICMS> - <pRedAdRem> ) = <vICMSMono>
```

Então, o resultado do cálculo do campo % Redução Alíquota ad rem ICMS irá preencher a tag <**pRedAdRem**>.

Quando o campo Tributação for configurado com a opção 15 - Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis, o campo **"Cód. Mot. Desoneração ICMS"** deve ser definido com a opção **"1 - Transporte coletivo de passageiros"** ou **"9 - Outros"**; assim, a tag <**motRedAdRem**>. Caso contrário, o sistema irá exibir a mensagem:

**"Quando o campo “% Redução Alíquota ad rem ICMS” for preenchido, é necessário informar o campo “Motivo Redução do ad rem”."**

Se a CST for diferente de 51, a descrição do campo **"Cód. do Benefício"** será **"Cód. do Benefício Credito Presumido"**, no entanto, caso a CST seja igual a 51 o campo aparecerá como **“Cód. Beneficio Diferimento"**. 

Além disso, o campo **"Percentual do Crédito Presumido"** será desabilitado e estará inativo caso selecione a CST igual a 51. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

---

#### Seção DIFAL/FCP (Não contribuinte)

Determine no campo **"Tipo de Cálculo do DIFAL e do FCP"** qual o tipo de cálculo DIFAL ou FCP correspondente à alíquota, de acordo com as seguintes opções e respectivas fórmulas de cálculo:

- **0 - Sem considerar redução da Base:** Vlr. Operação x (Alíq. Interna Destino - Alíq. Interestadual)
- **1 - Com redução da base aplicada na base:** ((Vlr. Operação x (1 - Perc. Redução Base Destino)) x Alíq. Interna Destino) - ICMS Próprio
- **2 - Com redução da base aplicada na alíquota:** ((Vlr. Operação x Alíq. Interna Destino x (1 - Perc. Redução Base Destino))) - ICMS Próprio
- **3 - ICMS Interestadual calculado sob a BC do DIFAL:** (Vlr. Operação x (1 - Perc. Redução Base Destino)) x Alíq. Interna Destino) - Alíquota Interestadual)
- **4 - Cálculo do DIFAL com ICMS Destino por dentro:** (((Vlr. Operação / (1 - Alíq. Interna Destino + Perc. ICMS FCP))) x (1 - Perc. Redução Base Destino)) x Alíq. Interna Destino) - ((Vlr. Operação / (1 - Alíq. Interna Destino + Perc. ICMS FCP))) x Alíq. Interestadual)
- **5 - Cálculo do DIFAL Convênio 142/2018:** Vlr. Operação / (1 - Alíq. Interna Destino - Alíq. Interestadual)
- **6 - Cálculo do DIFAL com a redução do ICMS Próprio:** ((Vlr.Operação-ICMS próprio)/(1 - Alíq. Interna Destino - Alíquota FCP))
- **7 - ICMS difal base dupla UF Sergipe:** (Vlr. Operação x (1 - Perc. Redução Base Destino)) / (1 - Alíq. Interna Destino - Alíq. Interestadual)
- **8 - Base de cálculo do DIFAL e do FCP por fórmula:** A Base de cálculo do DIFAL e do FCP será calculada pela fórmula informada.
- **9 - Cálculo do DIFAL com ICMS Destino por dentro - Base Dupla:** (((Vlr. Operação / (1 - (Alíq. ICMS Interna Destino + Perc. ICMS FCP))) x (1 - Perc. Redução Base Destino)) x Alíq. Interna Destino) - (Vlr. Operação x Alíq. Interestadual).
- **10 - Calculo da base, valor do DIFAL e do FCP por fórmula:** A base de cálculo, o valor do DIFAL e o FCP serão calculados pelas fórmulas informadas.

**Importante:** a opção 8 - Base de Cálculo do DIFAL por fórmula está disponível para seleção a partir da versão 4.4 e apenas para layout [HTML5](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110733-HTML5).

Quando essa opção estiver selecionada, o sistema seguirá a regra de cálculo considerando o Convênio 142/2018. Sendo assim, juntamente com essa opção inserida, os campos **"Alíquota"** e **"Alíq. Interna Destino"** localizados nessa aba deverão ser preenchidos.

Ainda em relação ao campo Alíquota, quando o código da **"Origem do Produto"** (tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral)) for 1, 2, 3 ou 8 informe neste campo a alíquota de 4,00%. Já quando o código for 0, 4, 5, 6 ou 7, informe a alíquota de 7.00% ou 12.00%, conforme a UF de destino.

**Observação:** ao realizar essas configurações e clicar na opção **"Consultar/Alterar Dados do Imposto do Item"** (tela Central de Notas, grade **"Itens"**, botão **"Outras Opções"**) tem-se os cálculos realizados corretamente nos campos **"Valor DIFAL UF Destino"**, **"Base Difal"** e **"Tipo de Cálculo do DIFAL"** no pop-up que será exibido.

**Nota:** para obter a base de cálculo do DIFAL e FCP utilize a fórmula:

```
 ((Vlr.Operação- ICMS Próprio)/(1 - Alíq. Interna Destino - Alíquota FCP))
```

Para encontrar os valores de DIFAL e FCP, utilize as fórmulas abaixo:

```
  Vlr. Difal = (BC Difal x Alíq. Interna Destino) - ICMS Próprio
          Vlr. FCP = BC Difal x Perc. ICMS Fundo Comb. Pobreza
```

Os campos **"Alíq. Interna Destino"** e **"% ICMS FCP"** são participantes nas configurações relacionadas à [Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado).

O Fundo de Combate à Pobreza (FCP) somente será calculado para operações com destino ao Paraná (PR) se houver incidência do Diferencial de Alíquotas (DIFAL) na operação.

**Observação:** para a geração do Registro 0200, e assim, a geração do campo **"12 - ALIQ\_ICMS"** no SPED,  o sistema segue uma hierarquia. Observe:

1. Primeiramente, o Sankhya Om irá procurar o preenchimento do campo Alíquota Interna de ICMS na aba [0200 do EFD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#0200doEFD) do Cadastro de Produtos;
2. Caso essa informação esteja ausente, será verificada no campo Alíquota Interna de ICMS da aba [Impostos / informações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abaimpostosinformaesporempresa);
3. Em seguida, se o campo da aba acima também estiver vazio, o sistema irá verificar no campo Alíquota Interna de ICMS da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abaimpostos) do Cadastro de Produtos;
4. Por fim, se nenhum dos campos acima estiverem completos, a informação do ICMS será buscada no campo Alíq. Interna Destino dessa tela.

Informe no campo **"% Redução Base Destino"** o percentual de redução de base correspondente a localização destino do cálculo.

Ao habilitar a marcação **"Zerar Valor do ICMS DIFAL do Remetente"** na emissão de NF-e's contendo produtos com cálculo do DIFAL e que, logicamente se encaixem na alíquota em questão, o valor do ICMS DIFAL Remetente será zerado.

Para o preenchimento do campo **"Fórmula para Base de Cálculo do DIFAL e do FCP"** é necessário que o campo Tipo de Cálculo do DIFAL e do FCP esteja configurado com a opção 8 - Base de cálculo do DIFAL e do FCP por fórmula ou 10 - Calculo da base, valor do DIFAL e do FCP por fórmula. Além disso, para informar o código da fórmula neste campo é necessário que na tela [Fórmula Diferencial Alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594934-F%C3%B3rmula-Diferencial-de-Al%C3%ADquota) já exista uma fórmula cadastrada que atenda os cálculos, conforme for exigido para cada UF.

**Observação:** o cálculo dessa fórmula será realizado para o produto e será replicado para despesas acessórias.

Para utilizar o campo **"Fórmula para o Cálculo do DIFAL"**, o campo Tipo de Cálculo do DIFAL e do FCP deve estar configurado com a opção 10 - Calculo da base, valor do DIFAL e do FCP por fórmula. Além disso, para inserir um código neste campo é necessário que na tela [Fórmula Diferencial Alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594934-F%C3%B3rmula-Diferencial-de-Al%C3%ADquota) já exista uma fórmula cadastrada que atenda os cálculos, conforme for exigido para cada UF.

O campo **"Fórmula para o Cálculo do FCP do DIFAL"** será habilitado para configuração, se o Tipo de Cálculo do DIFAL e do FCP estiver com a opção 10 - Calculo da base, valor do DIFAL e do FCP por fórmula selecionada. Para informar o código da fórmula neste campo, é necessário que na tela [Fórmula Diferencial Alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594934-F%C3%B3rmula-Diferencial-de-Al%C3%ADquota) já exista uma fórmula cadastrada que atenda os cálculos, conforme for exigido para cada UF.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

---

#### Seção Configuração

Em conjunto com o campo Tabela c/base p/ICMS, a marcação **"Usar a Maior Base para ICMS"** influenciará no cálculo do ICMS da seguinte forma:

1. Se houver tabela informada no campo Tabela c/base p/ICMS e a marcação Usar a maior base para ICMS não estiver realizada, o cálculo do ICMS será com base na tabela.
2. Se houver tabela informada no campo Tabela c/base p/ICMS e a marcação Usar a maior base para ICMS estiver efetuada, o cálculo de ICMS será com base no maior valor.
3. Se não houver tabela informada no campo Tabela c/base p/ICMS, o cálculo de ICMS será com base na alíquota do produto.

Quando for configurada uma alíquota com a marcação **"Usar Vlr. ICMS na ST, anotar Base e Valor na Obs. do item e zerar Base e Valor do ICMS?"** habilitada no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), ao gerar uma Nota Fiscal de Venda não serão apresentados os valores e alíquota(s) de ICMS próprio. Contudo, os valores do ICMS continuarão sendo utilizados para cálculo da Substituição Tributária. Esses valores (ref. ICMS normal) também não serão gravados para os Livros Fiscais.

**Nota:** quando um [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de movimento Compra é configurada na aba Impostos, campo Cálculo de ICMS, IPI e ISS, com a opção **"Calcula e Digita"** e no cadastro da alíquota de ICMS, a marcação Usar Vlr.ICMS na ST, anotar Base e Valor na Obs. do Item e zerar Base e Valor do ICMS? estiver feita, o sistema só irá efetuar o recálculo do imposto se o campo Base ICMS estiver em branco. Isso se deve ao fato de que, como a configuração permite a digitação do valor do imposto o sistema, nesse caso, deve manter o que foi digitado. Se configurado na aba Impostos, o campo Cálculo de ICMS, IPI e ISS com a opção **"Calcula e NÃO Digita"** e no cadastro da alíquota de ICMS a marcação Usar Vlr.ICMS na ST, anotar Base e Valor na Obs. do Item e zerar Base e Valor do ICMS? estiver feita, o sistema efetua o recálculo do imposto normalmente na confirmação das alterações do item da nota.

A marcação **"Optante pelo Regime Especial do Pró-Emprego (Resolução n° 257/2008 - SEF)"** trata-se de um incentivo fiscal para a importação com redução na alíquota do ICMS. Quando habilitada, determinará que a alíquota se enquadre nos cálculos de Regime Especial do Pró-Emprego.

A marcação **"ICMS devido à UF de origem da prestação, quando diferente da UF do emitente"** é utilizada em casos em que a transportadora não possui inscrição no estado em que a mercadoria será coletada para emissão do CT-e. Nessa situação é preciso emitir o CT-e com a tributação igual a 90 - Outras. Portanto, essa marcação é corretamente utilizada quando o campo Tributação estiver definido com a opção **"90 - Outras"**.

Nos processos de saída interestaduais de produtos que possuem origem estrangeira, tem-se uma regra para aplicação da alíquota de ICMS de 4%. Quando o produto se enquadra nessa regra de aplicação, em consequência da sua origem estrangeira é necessário configurar o campo **"Para redução da base de cálculo p/ produtos de origem estrangeira"** de acordo com as seguintes opções:

- **Desconsiderar redução:** a redução não será aplicada;
- **Redução de Base:** teremos a aplicação da alíquota estrangeira e a redução normal;
- **Redução de Base Estrangeira:** aplica-se a alíquota e a redução estrangeira.

Sendo que, para que a alíquota e a redução estrangeira sejam aplicadas é necessário que o campo **"Redução da Base para Origem Estrangeira"** esteja preenchido com o valor da redução que será aplicada.

Quando for identificado no lançamento de uma nota, que um produto é de origem estrangeira, a Alíquota Estrangeira informada no campo **"Alíquota p/ Origem Estrangeira"** também presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral) será utilizada como Alíquota de ICMS. Acesse mais informações através do link [Cálculo de ICMS p/ produtos de Origem Estrangeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111873-ICMS-para-produtos-de-Origem-Estrangeira). Além disso, o sistema irá verificar se a marcação Desconsiderar redução de base de cálculo p/ produtos de origem estrangeira está realizada, assim, teremos às seguintes situações:

- Quando marcado e a Tributação do produto for 20 – Com redução de base de cálculo, o sistema irá alterar a tributação para 00 – Tributada Integralmente e o percentual de redução de base não será aplicado;
- Se estiver marcado e a Tributação do produto for 70 – Com redução de base e c/ cobrança por subst. , a tributação será modificada para 10 – Tributada e c/ cobrança por substituição e o percentual de redução de base não será aplicado;
- Se a referida marcação não estiver realizada, não haverá alteração no comportamento do sistema.

No campo **"Fórmula para cálculo da base de ICMS"** deve ser inserida a fórmula para cálculo da base de ICMS. Lembrando que, essa fórmula deve ser previamente cadastrada na tela [Fórmulas para ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601534-F%C3%B3rmulas-para-ICMS). Além disso, o parâmetro **"Proporcionalizar base ICMS calculada por fórmula? - PROPFORBASEICMS"** deve estar ligado para que a base de ICMS seja proporcionalizada na fórmula dos itens que possuam ICMS.

Dessa forma, tem-se o seguinte exemplo:

Existe um processo em que o estado de Rondônia determina que a base de ICMS deve ser composta a partir de uma fórmula, na prestação de serviço de transporte e emissão do CT-e. Nessa especificidade a base de ICMS precisa ser igual a:

Base de ICMS = peso da mercadoria transportadora x índice conforme tabela publicada pelo governo estadual x valor unitário do litro do diesel.

**Importante:** essa fórmula é empregada exclusivamente para determinação da base de ICMS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

---

#### Seção Repassar para o Cliente

Caso seja efetuada a marcação **"Redução do Imposto"** será calculado o valor da diferença entre o imposto normal e o imposto calculado sobre a base reduzida; esse valor será armazenado no campo Desconto de Redução de Base. Exemplo: 

```
 VLRREPRED = (BaseSemRed * ALIQICMS / 100) - VLRICMS
```

Ao efetuar a marcação **"ICMS"** será repassado o valor integral do ICMS calculado no item para o campo Desconto de Redução de Base. Exemplo:

```
  VLRREPRED = VLRICMS
```

Realizando a marcação **"Redução da Base"** será calculado o valor da diferença entre a base de cálculo para o ICMS normal e a base de cálculo reduzida e esse valor será armazenado no campo Desconto de Redução de Base. Exemplo: 

```
 VLRREPRED = BaseSemRed - BASEICMS
```

Quando o campo **"% da Base ICMS"** estiver configurado com um percentual, no lançamento de uma Nota que calcule ICMS, o sistema irá gerar um Valor de Repasse de ICMS ao Cliente, resultante da operação:

```
 Base ICMS * % Base ICMS / 100
```

Com a marcação **"ICMS DIFAL (Não Contribuinte)"** realizada, tem-se na emissão da NF-e, a desoneração dos valores do ICMS Próprio e DIFAL nas operações com benefício fiscal da Isenção na UF do Remetente e na UF de Destino. Ao configurar uma Alíquota de ICMS com Repasse para o Cliente, e emitir a NF-e na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), o sistema irá calcular o ICMS e o ICMS DIFAL (DIFAL Rem, DIFAL Dest e FCP) e somará todos esses valores, considerando os mesmos como desoneração.

Sendo assim, o valor total da NF-e será o valor total subtraindo-se os valores de ICMS Próprio, DIFAL Rem, DIFAL Dest, e FCP. No XML correspondente à essa NF-e, não será gerada a tag **<ICMSUFDest>** e a soma dos valores ICMS e ICMS DIFAL são apresentados na tag **<vICMSDeson>**.

Além disso, na geração do Livro Fiscal ([EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI)), o valor da desoneração será composto pelos valores de ICMS Próprio, DIFAL Rem, DIFAL Dest, e FCP; este valor será enviado para o registro C100 | campo 15 | VL\_ABAT\_NT.

**Observação:** para que a marcação ICMS DIFAL (Não Contribuinte) possa ser realizada é necessário que a marcação ICMS também presente na seção Repassar para o Cliente, esteja efetuada.

O campo **"Forma de Repasse Desoneração"** e a marcação **"Cálculo Desoneração ICMS por dentro"** possibilitam que o sistema calcule o valor do repasse bem como deduza ou não este valor do total da nota.

**Nota:** referente ao Cálculo de Desoneração de ICMS por dentro e às **"CSTs 30 e 40 - Isenção"** e **"CSTs 20 ou 70 - Redução de Base de Cálculo"**, o campo Forma de Repasse Desoneração e a marcação Cálculo Desoneração ICMS por dentro deverão estar devidamente configurados para que seja realizado o cálculo corretamente. O sistema utilizará as seguintes fórmulas para os cálculos das CSTs acima:

**(1)** **CST 30 ou 40:**

```
 Valor do ICMS Desonerado = Preço na Nota Fiscal / (1 - Alíquota) * Alíquota
```

(1)** CST 20 ou 70 - Com Redução de Base:**

```
 ICMS Desonerado = Preço na Nota Fiscal * (1 - (Alíquota * (1 - Percentual de redução
         da BC)))/ (1 - Alíquota) - Preço na Nota Fiscal
```

**Importante:** o campo Forma de Repasse Desoneração apenas será exibido e considerado no sistema caso o parâmetro **"Habilitar formas alternativas de repasse de ICMS?? - HABFORMASREPRED"** esteja habilitado.

**Observação:** quando esses campos estiverem configurados, poderão ser visualizados os cálculos destes na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) da grade **"Itens"**, opção **"Consultar/Alterar Dados Dados do Imposto do Item..."**. O campo **"Vlr.Repasse de Redução"**, localizado no pop-up que se abre ao clicar na opção acima, será preenchido caso o campo Forma de Repasse Desoneração, tela Alíquotas de ICMS, aba Geral, seção Repassar para o Cliente estiver com a opção **"Destacar valores e deduzir do total da nota"** selecionada. Caso contrário, será preenchido no pop up Consultar/Alterar Dados do Imposto do Item... o campo **"Vlr. redução sem desconto"**, considerando as mesmas fórmulas citadas acima.

**Nota:** para que o cálculo por dentro seja realizado é necessário que se habilite as marcações ICMS e **"Cálculo desoneração de ICMS"**, além de selecionar a opção Destacar valores e deduzir do total da nota do campo Forma de Repasse Desoneração e no campo % da Base ICMS informe o percentual da redução ou que for aplicado ao repasse.

![Imagem 7: Caso o % da Base ICMS não seja informado ou seja igual a zero, o cálculo do ICMS Desonerado não será executado.](https://ajuda.sankhya.com.br/hc/article_attachments/23765533194135) Caso o % da Base ICMS não seja informado ou seja igual a zero, o cálculo do ICMS Desonerado não será executado.

A marcação **"Desoneração ICMS do Simples Nacional"** ficará disponível quando o campo **"Tipo de Cálculo de ST Específico"** da aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934#abasubstituiotributria) estiver definido com a opção **"19 - Cálculo ST SUFRAMA com Desoneração Simples Nacional"**. Sendo que, ao acionar esta marcação será efetuada a emissão de NF-e do Simples Nacional contendo a desoneração e o repasse. 

[[voltar ao topo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

#### Seção Informações de ICMS Efetivo:

No campo **"Alíquota Interna (CST 60)"** insira o valor referente à alíquota da Situação Tributária **"60 - ICMS  cobrado anteriormente por substituição tributária"**.

**Observação:** caso no campo **"Tributação"** dessa aba, a opção 60 - ICMS cobrado anteriormente por substituição esteja selecionada e o campo acima não tenha nenhum valor informado, o sistema emitirá a seguinte mensagem:

**"Para tributação 60-ICMS cobrado anteriormente por substituição o campo Alíquota Interna (CST 60) do grupo de Informações de ICMS Efetivo deve ser informado. Ajuste sua alíquota".**

**Nota:** apesar de exibida a mensagem acima, ainda será possível salvar o registro. Essa mensagem servirá apenas de lembrete para que a alíquota seja ajustada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Aba Frete

![Imagem 8: Aba Frete](https://ajuda.sankhya.com.br/hc/article_attachments/360102523354)

O campo **"Alíquota Frete"** define o percentual ICMS a ser calculado sobre o frete da nota fiscal, caso exista.

O campo **"Redução da Base Frete"** define percentual de redução sobre o valor do frete.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Aba Substituição Tributária

![Imagem 9: Aba Substituição Tributária](https://ajuda.sankhya.com.br/hc/article_attachments/1500003690421)

**Observação:** quando a regra de alíquotas for criada ao processar os impostos, os campos dessa aba serão preenchidos conforme os valores da sub-aba **"Detalhes Integração Tributo ICMS"** da aba [ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573#abaicms) da tela [Integração Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573).

A **"Margem Lucro (MVA)"** é usada para o cálculo de substituição tributária. Essa margem de lucro é definida por leis específicas.

O campo **"Alíq. Subst. Tributária"** define o percentual do ICMS a ser aplicado para o cálculo de ICMS por substituição tributária.

A princípio, o campo **"Redução Base ST"** será preenchido com o mesmo percentual de redução da base do ICMS (esse campo dará mais flexibilidade ao sistema). Esse campo é necessário para o correto cálculo do **"Garantido Integral"** (tópico [Cálculo do ICMS "Garantido Integral"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#clculodoicmsgarantidointegral)). A configuração desse campo vale tanto para venda quanto para compra. No caso da venda, se a Redução de Base ST estiver informada o sistema a usa, caso contrário, será considerado o percentual informado no campo **"Redução do ICMS"**.

O valor do coeficiente para ser informado no campo **"% ST FCP Interno/Coeficiente FECOP"** deve ser multiplicado por 100, conforme o exemplo: coeficiente 0,122 x 100 = 12,2.

**Observação:** assim como ocorre para o CST 10, o cálculo de FCP de ST para notas de entrada também permite a configuração de ICMS para CST 60. Sendo assim, pode-se configurar a % FCP de ST na tela de Alíquotas e na Central de Compras, após configurar uma nota com o uso do Produto, Empresa e TOP que permitam cálculo envolvendo FCP interno, conseguimos verificar que a porcentagem foi inserida corretamente nesse cálculo.

O campo **"Tipo de Cálculo de FCP Específico"** possui as opções abaixo para escolha:

- 0 - Não específico (Regra Geral);
- 1 - FECOP ST Majorado (CE).

```
  Regra para o cálculo para FCP e ICMS/ST:

- Vlr. Produto x Alq. ICMS = Vlr. ICMS
- Vlr. Produto x MVA = BC ICMS/ST
- BC ICMS/ST x Aliq. ICMS/ST = Vlr. ICMS/ST
- Vlr. ICMS/ST - Vlr. ICMS = Vlr. Dif. ICMS
- Vlr. Dif. ICMS x Coeficiente FECP legislação do Ceará (campo % ST FCP Interno/Coeficiente
 FECOP) = Vlr. FCP
- Vlr. Dif. ICMS - Vlr. FCP = Vlr. ICMS/ST
```

O campo **"Tabela c/ Base para ST"** está vinculado com a marcação Usar a maior base para ICMS ST e influenciará o cálculo do ICMS da seguinte forma:

1. Se houver tabela informada no campo Tabela c/base p/ICMS ST e a marcação Usar maior base para ICMS ST não estiver realizada, o cálculo do ICMS ST será com base na tabela.
2. Se houver tabela informada no campo Tabela c/base p/ICMS ST e a marcação Usar maior base para ICMS ST estiver efetuada, o cálculo de ICMS ST será com base no maior valor.
3. Se não houver tabela informada no campo Tabela c/base p/ICMS ST, o cálculo de ICMS será com base na alíquota do produto.

---

**Exemplo de cálculo de Base de ST e Vlr de ST**

**(1)** A Base de ST é obtida da seguinte forma:

```
 (QtdNeg * Último custo de Entrada com ICMS)*((100 - Redução de Base ST)
/ 100) * MVA
```

**(1)** O Vlr de ST é encontrado pelo seguinte cálculo:

```
 (Base de ST * Aliq.ST) – Vlr ICMS
```

Dados:

- Produto configurado para calcular ST na compra e na venda
- Último custo de Entrada com ICMS: 131,127
- Quantidade Negociada: 1
- Base de ICMS: 180,00
- Vlr de ICMS: 18,00

| - Base de ST:   1 \* 131,127 \* 1 \* 50% = 65,5635  = 131,27 + 65,5635  =196,69 | - Vlr ST:   (196,69 \* 18%)  = 35,40 - 18,00  = 17,40 |
| --- | --- |

---

Para as empresas que se enquadram em regime especial disponibilizado pelo decreto 44498 de 29 de novembro de 2013 para as empresas que se adequam no RIOLOG, deve-se realizar o preenchimento do campo **"Percentual Mínimo ST (RIOLOG)"**, onde informa-se o percentual mínimo de ST de acordo com a RIOLOG.

Caso a informação nesse campo seja um percentual maior que zero, o seguinte cálculo será realizado:

```
 (Base de Subst. * Perc. Min RIOLOG) / 100
```

O resultado desse cálculo será o valor da substituição com base no percentual da RIOLOG. Se o valor da Substituição calculado anteriormente for menor que o calculado pelo **"Perc. Mínimo RIOLOG"**, ele será substituído.

Algumas configurações são necessárias para que o cálculo aconteça, são elas:

- A alíquota de ICMS deverá estar cadastrada;
- Na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba Impostos, a marcação Calcular ICMS deve estar efetuada, e o campo Tipo de Substituição deve estar selecionado com uma opção diferente de **"Não tem"**;
- Na configuração do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) que está sendo utilizado na venda do produto, aba Impostos, o campo Cálculo de ICMS, IPI e ISS deve estar selecionado com uma das opções onde ordena-se a realização do cálculo, ou seja **"Calcula e não digita"**, **"Calcula e digita"** ou **"Calcula na confirmação"**; nessa mesma aba, a marcação Tem ICMS deve estar realizada;
- Nos cadastros de [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) e de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), configure corretamente a cidade e a UF, de acordo com a alíquota a ser configurada.

O objetivo fiscal do campo **"Modalidade BC ICMS ST"** é de codificar as movimentações, facilitando a identificação delas por parte do fisco. Através da **"Nota Fiscal Eletrônica - NF-e"** e/ou **"Escrituração Fiscal Digital - EFD"**, esses dois campos gerarão as informações referentes às modalidades para Base de Cálculo de ICMS e ST, para o Sistema Público de Escrituração Digital (SPED). Nesse campo pode-se escolher uma das seguintes opções:

- Pauta (Valor);
- Margem Valor Agregado (%);
- Valor da Operação;
- Lista Neutra (Valor);
- Lista Positiva (Valor);
- Lista Negativa (Valor);
- Preço tabelado ou Máximo Sugerido.

**Nota:** ao selecionar a opção **"Valor da Operação"**, o sistema realizará o cálculo do ICMS ST (sem aplicar o MVA) sobre o Valor da Alíquota da Substituição Tributária que encontra-se cadastrada.

**Observação:** quando a opção **"Margem Valor Agregado (%)"** for selecionada e quando tratar-se da última nota técnica, sempre será gerada a tag **<pMVAST>** no XML, mesmo quando o valor for igual a zero.

**Importante:** selecionando qualquer uma das outras opções desse campo, a tag acima mencionada não será gerada.

**Nota:** outros arquivos magnéticos, exigidos pelo Governo, também poderão utilizar tais informações.

A marcação **"Usar a maior base para Subst.Tributária"** deve ser usada junto com Tabela c/base p/ST.

Ao habilitar a marcação **"Considera Pauta + MVA para a base de calc do ICMS ST"**, o sistema irá utilizar o cálculo específico na Base de ICMS ST para os produtos bovinos para o estado de Alagoas conforme o embasamento legal da Instrução Normativa nº 042. Lembre-se que, para que essa marcação seja apresentada, é necessário que o parâmetro **"Não considera MVA ao Comparar as Bases - NAOCONSIDMVA"** e a marcação Usar a maior base para Subst.Tributária estejam ligados.

A marcação **"Reduzir Valor do ICMS no Cálculo da ST?"** só poderá ser usada se Redução de Base ST for maior que zero.

Se marcada, o cálculo do valor de ST será alterado utilizando a seguinte fórmula:

```
 Valor ST = Base ST * Aliq ST - (Vlr ICMS * (1 - Redução ST / 100))
```

Se desmarcada, o cálculo será o seguinte:

```
 Valor ST = Base ST * Aliq ST - Vlr ICMS
```

No campo **"Base ST será o valor do produto COM a redução do ICMS?"** temos três opções: **"Desconsidera"**, **"Desconsiderar IPI p/ Redução"** e **"Considerar IPI p/ Redução"** em que, por meio dessa última, o sistema executará o cálculo reduzindo o valor do produto de acordo com percentual informado no campo Redução de base, aplicando a alíquota de MVA sobre o valor reduzido para determinar a BASE DE ST.

```
 Base ST = (VLRPROD - REDUÇÃO DE BASE) + MVA
```

**Exemplo de cálculo:**

- VLRPROD = 1.000,00
- REDUÇÃO DE BASE = 60%
- IVA = 50%

**(1)** Base ST = (1.000,00 - 60%) + 50%

 = 600,00

Se a marcação **"Zerar valor da substituição tributária quando negativo"** estiver realizada e o cálculo de ST resultar em menor que zero, o sistema deixará o cálculo zerado. Caso a marcação não esteja efetuada e o cálculo de ST venha a ser menor que zero, o sistema emitirá a mensagem:

**"Valor da substituição não pode ficar negativo. Produto: xxxx"**

Para que o valor da substituição tributária seja zerado quando negativo, o sistema deve obter uma das três opções:

- O campo **"Tabela c/ base p/ ST"** estar diferente de zero; ou
- Se a marcação **"Usar Vlr. ICMS na ST anotar Base e Valor na Obs.do item e zerar Base e Valor do ICMS?"** estiver efetuada e zerar o valor da substituição Tributária; ou
- Se a marcação **"Zera Valor da Substituição Tributária quando negativo"** estiver realizada.

Caso nenhuma das condições acima seja satisfeita, será apresentada a mensagem:

**"Valor da substituição não pode ficar negativo. Produto: xxxx"**

O campo **“Calcula ST extra nota com base em MVA na VENDA (Não utilizar em compras)”**, possui as seguintes opções:

- **Não se aplica:** se selecionado, não deverá ser realizado nenhum cálculo referente a ICMS ST Extra Nota;
- **Com base em MVA:** aplica-se a fórmula (Base de ICMS sem redução \* (1 + MVA / 100) \* (Redução Base ST/100) \* (Alíq.Subst. Tributária) – Vlr. ICMS do Item);
- **Com base na Pauta:**  aplica-se a fórmula considerando apenas o valor de pauta, (Pauta \* (Redução Base ST/100) \* (Alíq.Subst. Tributária) – Vlr. ICMS do Item);
- **Com base na Pauta acrescida de MVA:** aplica-se a fórmula considerando pauta multiplicada pelo percentual de MVS, (Pauta \* (1 + MVA / 100) \* (Redução Base ST/100) \* (Alíq.Subst. Tributária) – Vlr. ICMS do Item).

Se o campo estiver configurado com uma opção diferente de **“Não se Aplica”** e o campo **“Tributação”** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934/live_preview/01JHMPFFNRY1THRWNREJV06TAV#abageral)) estiver com preenchido com uma das CSTs: 10, 30, 60 ou 70, quando clicar em Salvar, a seguinte mensagem surgirá na tela:

**"O campo 'Calcula ICMS ST Extra Nota na Venda (Não utilizar em compras)' deve ser igual a 'Não se aplica' para as CSTs 10, 30, 60 e 70"**

---

![Imagem 10: Informações adicionais acerca do campo Calcula ST extra nota com base em MVA na VENDA (Não utilizar em compras) :](https://ajuda.sankhya.com.br/hc/article_attachments/24752008754455) **Informações adicionais acerca do campo Calcula ST extra nota com base em MVA na VENDA (Não utilizar em compras):**

- Informar nos parâmetros TIPTITGNREST e TIPTITGNRESTRB os [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) referentes a GNRE e ao Reembolso GNRE, respectivamente;
- Para o Reembolso GNRE, o título vinculado no parâmetro de chave TIPTITGNRESTRB deve ter a natureza de Receita no movimento financeiro e, no movimento financeiro, o parceiro do título deve ser o mesmo que o da nota fiscal;
- No [Cadastro de Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados) informe o campo **"Cód. Parceiro Secretaria da Receita Estadual"**;
- No [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) devemos adicionar 2 (duas) parcelas com percentual 100%, informando nessas parcelas os mesmos Tipos de Títulos informados nos parâmetros TIPTITGNREST e TIPTITGNRESTRB configurados anteriormente; essas parcelas serão o GNRE e o Reembolso. Sendo assim, no campo **"Fórmula"**, informe VLRSTEXTRANOTATOT. Na parcela do GNRE deverá ser informado o mesmo Parceiro inserido no Cadastro de Estados;
- Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) e no cadastro de [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), a marcação **"Gerar GNRE?"** presente nas abas Livros Fiscais e Validações, respectivamente, deverá estar realizada;
- Os [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) deverão estar configurados para calcular ST.

---

No Cabeçalho da Nota, o campo **"Valor Total ST Extra Nota"** terá a soma do campo Valor ST Extra Nota de cada item da Nota. O Valor do ST Extra Nota é calculado através da seguinte fórmula:

```
 VLRSTEXTRANOTA = (Base ICMS sem redução) * (1 + MVA / 100)
* (Redução Base ST/100) * (Alíq.Subst. Tributária) – Vlr. ICMS do Item
```

**Observação:** além do campo Valor ST Extra Nota, serão alimentados também os campos **"Base ST Extra Nota"** e **"Alíquota ST Extra Nota"**. Esses campos estão disponíveis para inclusão no layout das notas ao acessar a tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota). A geração dos dados nestes campos depende da realização da marcação **"Usar ST Extra Nota na Restituição de ST"** localizada na aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abalivrosfiscais) nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa).

O cálculo de **"ST Extra Nota"** é feito em estados que comercializam seus produtos pra fora de seu território, sendo a Nota Fiscal emitida com tributação normal dos produtos porém, a ST é recolhida extra nota. Esse recolhimento deverá ser feito pela empresa vendedora e comprovado na barreira estadual, sendo este valor restituído pelo comprador.

O cálculo é realizado apenas quando a configuração da alíquota não envolver ICMS-ST, dessa forma, a marcação **"Calcula ST extra nota com base em MVA"** só poderá ser efetuada se no campo **"Tributação"** for diferente das opções abaixo:

- Tributada e c/ cobrança por substituição;
- Isenta e não trib. e c/cobrança por subst.;
- ICMS cobrado anteriormente por substituição;
- Com redução de base e c/cobrança por subst..

Se a marcação **"Usar último custo de entrada com ICMS como base p/ ST"** estiver realizada, será utilizado o **"Último Custo de Entrada com ICMS"** multiplicado pela quantidade do produto para compor a base de ST, aplicando as outras marcações que envolvem ST (se estiverem realizadas).

A busca do custo segue o conceito já existente no sistema de custo por empresa, local e controle. Se a busca do custo for igual a zero, a base de ICMS ST será calculada como se a marcação **"Usar último custo de entrada com ICMS como base p/ST"** estivesse desabilitada.

O parâmetro **"Data para atualização de custo - DTPATUCUST"** combinado com o campo **"Hora da Movimentação"** do cabeçalho da nota, determinará qual o campo de data da nota que será utilizado como limite superior da busca do último custo. Se o campo desse parâmetro estiver vazio na nota, o campo Data de Negociação será utilizado.

Ao abrir a tela de [Recálculo de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594214-Rec%C3%A1lculo-de-Custos) e confirmar uma nota que gere cálculo de custo (apresentada no painel de avisos), são apresentadas as seguintes mensagens:

- Quando o parâmetro DTPATUCUST está configurado com a opção **"Negociação"**:

**"Devido a regras fiscais o sistema foi ajustado para trabalhar com data para custos "Dt. Entrada/Saída" e caso ela não esteja preenchida usaremos "Dt. Negociação". Foi identificado que você está usando configuração diferente do que é atualmente permitido, entre em contato com a Sankhya para se informar sobre as consequências de usar esta configuração."**

- Quando o parâmetro DTPATUCUST está configurado com as opções **"Movimentação"** ou **"Faturamento"**:

**"Devido a regras fiscais o sistema foi ajustado para trabalhar com data para custos "Dt. Entrada/Saída" e caso ela não esteja preenchida usaremos "Dt. Negociação". Foi identificado que você possui configuração diferente de "Dt. Entrada/Saída", para não ver esta mensagem novamente, basta ajustar o parâmetro "Data para atualização de custo" (DTPATUCUST) colocando a opção "Entrada/Saída", quando o parâmetro "DTPATUCUST" está igual a "Negociação"."**

Para as mensagens não serem apresentadas, basta que o parâmetro DTPATUCUST seja configurado com a opção **"Entrada/Saída"**.

O sistema apresenta a variação de preço de venda, ao confirmar uma nota de compra, desde que o Tipo de Operação - TOP esteja configurado para precificar (aba Geral, campo Precifica) e o parâmetro **"Apresentar variação de preço na NF de compra? - APRVARPOMPRA"** esteja habilitado; será apresentada a mensagem:

**"Houve variação no preço de venda. Deseja visualizar os produtos com variação?"**

Clicando em Sim, é apresentada a variação do preço; a variação do preço em relação à última data de vigor da tabela de preço ignorando o dia da confirmação da nota de compra.

Quando a marcação **"Calcular ST conforme portaria Sutri 430/2014 - MG"** estiver habilitada, caso a base do ST seja calculada por pauta mas o valor da pauta seja menor que o valor do produto, será utilizado o cálculo comum da base ST pelo MVA.

Se a marcação **"Calcular ICMS ST Zona Franca/Área de livre comércio"** for habilitada, será calculado o ICMS ST para a área de livre comércio destinatário no Amapá. Assim, para que seja realizado o cálculo, além de selecionar essa marcação, realize as configurações abaixo:

- Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral) dessa tela, o CST deverá estar definido como **"30-Isenta e não tribut. e c/ cobrança por substituição"**;
- Defina a Alíquota do ICMS Interestadual aplicada para o caso;
- Na aba Geral, o campo **"Cód.Mot.Desoneração ICMS"** tem que estar com a opção **"7-SUFRAMA"** selecionada;
- Na aba Geral, seção **"Repassar para o Cliente"**, a marcação **"Redução do Imposto"** deve estar realizada;
- Na aba Substituição Tributária, os campos **"Margem Lucro (MVA)"** e **"Alíq.Subst. Tributária"** deverão estar preenchidos;
- Ainda na aba Substituição Tributária, realize as marcações **"Reduzir Valor do ICMS no Cálculo da ST"** e **"Base ST será o valor do produto COM a redução do ICMS?"**;
- Na aba Substituição Tributária, o campo **"Modalidade BC ICMS"** deve ser igual à **"Margem Valor Agregado (%)"**;
- Por fim, na aba acima mencionada, selecione no campo **"Tipo de Cálculo de ST Específico"** a opção **"3 - Calcular ST com Incentivos SUFRAMA e Redução da BC"**.

As marcações **"Considerar IPI na comparação conforme portaria Sutri860"**, **"Calcular ST conforme portaria Sutri860"** e o campo **"Percentual PMPF"** quando preenchidos, realizarão o cálculo de ICMS-ST conforme a Portaria Sutri n° 860de 23 de julho de 2019.

**Nota:** a marcação Considerar IPI na comparação conforme portaria Sutri860 fará com que a nova regra de comparação, considere o valor do IPI; esta não afetará nenhum cálculo, servirá apenas para comparação.

**Observação:** o campo Percentual PMPF refere-se ao valor em % de PMPF a ser aplicado durante a comparação, sendo que ele apenas será habilitado quando a marcação Calcular ST conforme portaria Sutri860 estiver efetuada.

**Importante:** a funcionalidade descrita acima não englobará o valor das despesas acessórias durante a comparação.

Determine no campo **"Calcular MVA Ajustado?"** qual será o embasamento para cálculo do MVA de acordo com as seguintes opções:

- **Não Calcular:** ao selecionar essa opção, o MVA será o valor informado na alíquota sem ajustes;
- **Pelo MVA Padrão do Produto/Empresa:** por essa opção, o MVA informado na alíquota será calculado pelo MVA Padrão definido no produto/empresa;
- **Pela fórmula:** selecionando esta opção, habilitará o campo **"Fórmula para calcular MVA Ajustada"** para que indique a fórmula cadastrada previamente na tela [Fórmulas para DIFAL, ICMS AT E MVA Ajustada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594934). Dessa forma, o cálculo do MVA Ajustado (registrado no campo IVA da tabela de impostos da nota) será calculado com base na fórmula fornecida e aplicada para o cálculo do ICMS ST.
- **Pelo MVA da Alíquota:** quando selecionada essa alternativa, o sistema irá utilizar o MVA da própria alíquota como base de cálculo para o MVA ajustado para operações interestaduais, aplicando-se a seguinte fórmula:

```
 MVA ajustado: [(1 + MARGLUCRO/100) * (1 - ALIQUOTA/100) /
(1 - CARGATRIBUTARIA/ 100)] -1
```

Em que:

MARGLUCRO: Margem Lucro (MVA) da Alíquota;

ALÍQUOTA: Alíquota de ICMS;

CARGATRIBUTARIA: (ALIQSUBTRIB \* (100 – REDBASEST )) /100;

ALIQSUBTRIB: Alíquota de substituição tributária;

REDBASEST: Redução de base de substituição tributária.

(1)** Exemplos de cálculo MVA ajustado**

![Imagem 11: Dados:](https://ajuda.sankhya.com.br/hc/article_attachments/24752182106391) Dados:

- Alíquota Substituição Tributária = 25
- Redução de Base Substituição Tributária = 0
- Margem de Lucro = 40
- Alíquota = 7
- Se Red. Base Subst. Tributária = 0, então Carga Tributária = Alíquota Substituição Tributária

**(2)** MVA ajustado:

[(1 + 0,4) \* (1 - 0,07) / (1 - 0,25)] -1

[(1,4) \* (0,93) / (0,75)] -1

[1,302 / (0,75)] -1

1,736 -1 = 0,736

MVA ajustado = 73,60%

Considerando que o produto possua um valor total de R$ 100,00, a base de Subst. Trib. será igual a 173,60.

![Imagem 12: Dados:](https://ajuda.sankhya.com.br/hc/article_attachments/24752182108951) Dados:

- Alíquota Substituição Tributária = 25
- Redução de Base Substituição Tributária = 10
- Margem de Lucro = 40
- Alíquota = 7

**(2)** Carga Tributária = (ALIQSUBTRIB/100) \* (1 - REDBASEST/100)

(25/100) \* (1 - 10/100)

0,25 \* (1 - 0,1)

0,25 \* 0,9 = 0,225

Carga Tributária = 0,225

**(2)** MVA ajustado:

[(1 + 0,4) \* (1 - 0,07) / (1 - 0,225)] -1

[(1,4) \* (0,93) / (0,775)] -1

[1,302 / (0,775)] -1

1,68 - 1 = 0,68

MVA ajustado = 68,00%

---

![Imagem 13: Informações adicionais acerca do campo Calcular MVA Ajustado?](https://ajuda.sankhya.com.br/hc/article_attachments/24752008754455) **Informações adicionais acerca do campo Calcular MVA Ajustado?**

Quando a opção Pelo MVA da Alíquota for selecionada, a seguinte fórmula será aplicada para as operações internas:

```
 MVA ajustado: [(1 + MARGLUCRO/100) * (1 - ALIQUOTA/100) /
(1 - ALIQGERAL/ 100)] -1
```

Em que:

MARGLUCRO: Margem Lucro (MVA) da Alíquota;

ALIQSUBTRIB: Alíquota de substituição tributária;

ALIQGERAL: Alíquota Geral da aba Informações por Empresa do Cadastro do Produto

(1)** Exemplos de cálculo MVA ajustado**

![Imagem 14: Dados:](https://ajuda.sankhya.com.br/hc/article_attachments/24752182106391) Dados:

- Alíquota Substituição Tributária = 19
- Margem de Lucro = 42
- Alíquota Geral = 12

**(2)** MVA ajustado:

[(1 + 0,42) \* (1 - 0,19) / (1 - 0,12)] -1

[(1,42) \* (0,81) / (0,88)] -1

[1,1502 / (0,88)] -1

1,3070 -1 = 0,3070

MVA ajustado = 30,70%

Considerando que o produto possua um valor total de R$ 100,00, a base de Subst. Trib. será igual a 130,70.

---

**Nota:** devido a Margem de Valor Agregado (MVA) tratar-se de uma operação interestadual, para que haja o correto cálculo do FCP, este campo está ajustado de acordo com os campos **"Alíq.Subst. Tributária"** e **"% ST FCP Interno/Coeficiente FECOP"**.

**Observação:** caso o produto da regra de alíquotas criada possua o campo **"MVA/IVA Ajustada"** da aba **"Detalhe Integração Tributo ICMS"** da tela [Integração Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos) preenchido com um valor de IVA Ajustado, o campo Calcular MVA Ajustado? da tela Alíquotas de ICMS (aba Substituição Tributária) não será configurado automaticamente com a opção Pelo MVA da Alíquota ao processar os impostos. Porém, se o campo **"MVA/IVA do produto"** (aba Detalhe Integração Tributo ICMS, tela Integração Impostos) estiver preenchido com um valor de IVA, então o campo Calcular MVA Ajustado? será automaticamente configurado com a opção Pelo MVA da Alíquota. Assim, conclui-se que o sistema sempre dará prioridade ao campo MVA/IVA Ajustada na integração, caso não haja valor, será considerado o campo MVA/IVA do produto.

Informe no campo **"Fórmula para calcular MVA Ajustada"**, a fórmula de diferencial de alíquota/base de ICMS AT para realização do cálculo do MVA ajustado em operações internas.

A marcação **"Usar MVA original quando carga trib. inferior à alíq."** estará disponível para habilitação apenas quando o campo Calcular MVA Ajustado? estiver com as opções Pelo MVA da Alíquota ou Pelo MVA da Alíquota considerando % ST FCP Interno selecionadas.

O campo **"Cód. Antecipação ST"** foi criado para preencher o campo 15 (Cód. Antecipação) na geração do Síntegra através do módulo Livros Fiscais.

Nos Portais, quando o item da Nota estiver com o campo **"Cód. Antecipação ST"** vazio, ele será preenchido com o mesmo valor definido no na Alíquota de ICMS.

Na gravação do item, se houver incompatibilidade entre os campos Cód. Antecipação ST e **"Cód. Tributação (CST)"**, o sistema limpará a informação presente no campo Cód. Antecipação ST.

Determine no campo **"Tipo de Cálculo de ST Específico"** como deverá ser o cálculo de ST, caso ele tenha que seguir alguma regra em particular. pode-se defini-lo com uma das seguintes opções:

- 0 - Não específico (Regra Geral);
- 1 - Calcular ST p/ Medicamentos - CAT-SP;
- 2 - Calcular ST (Dif.Alíq. por dentro), BC ST SEM Red. ICMS;
- 3 - Calcular ST com Incentivos SUFRAMA e Redução da BC;
- 4 - Calcular ST (Dif.Alíq. por dentro), BC ST COM Red. ICMS;
- 5 - Calcular ST Simplificado (Carga Média);
- 6 - Calcular ST sem dedução do ICMS próprio;
- 7 - Calcular ST (Dif.Alíq. Convênio 142/2018 - CFC);
- 8 - Calcular ST (Dif. Alíq. Considerando FCP e Redução de Base de ST);
- 10 - Calcular ST Via Pauta sem dedução do ICMS próprio;
- 11 - Calcular ST (Alíq. Limite créd. ICMS p/ devolução no Valor ST);
- 12 - Calcular ST (Dif.Alíq. por dentro), BC ST COM Red.ICMS COM FCP);
- 13 - Realizar cálc de ICMS para reduc no ST com alíq espec e utilizando o mesmo % de redução do ST;
- 14 - Cálculo ICMS e ICMS/ST - Decreto 38.286/PE;
- 15 - Calcular ST P/ Medicamentos - CAT-40/SP;
- 16 - Cálculo ICMS/ST - DIFAL - Decreto 40.230/2020- PB;
- 17 - Calcular ST - Lei nº 15730/PE;
- 18 - Cálculo ICMS ST e FCP (ICMS de Destino por Dentro) - Protocolo ICMS 104/2008 - AL;
- 19 - Cálculo ST SUFRAMA com Desoneração Simples Nacional;
- 20 - Calcular ICMS-ST com BC Reduzida por PIS/COFINS Desonerados e ICMS Operação;
- 21 - Calcular ST conforme convênio 133/02.

A seguir confira as observações referentes as opções mencionadas:

**1 - Calcular ST p/ Medicamentos - CAT-SP**

No caso da opção 1 - Calcular ST p/ Medicamentos - CAT-SP, configure o parâmetro **"% Aplicado sobre a Pauta Portaria CAT-137/2011 SP - PERCSTCAT137SP"**, informando o percentual a ser aplicado na pauta (PMC). Nesse caso, a base de ICMS-ST será calculada da seguinte forma:

**1)** O sistema irá buscar a pauta para medicamentos (PMC-Preço Máximo ao Consumidor), inserida no campo Tabela c/Base para ST presente na aba Substituição Tributária;

**2)** Será feita a busca pelo % de desconto, para cálculo da pauta com desconto (PMC com Desconto), no campo Redução Base ST também presente na aba Substituição Tributária;

Tendo essas duas informações, será feito o seguinte cálculo do PMC com Desconto:

```
 Tabela c/Base para ST x Redução Base ST = PMC com Desconto
```

**3)** Uma vez obtido o resultado da fórmula citada acima, será realizada a seguinte comparação de valores para seguir com a tributação do ICMS-ST:

- Se o Valor da Operação for maior ou igual ao (PMC com desconto \* PERCSTCAT137SP / 100), será calculado o valor da Base ST, através do MVA. Porém, se esse valor calculado através do MVA for maior que a pauta sem desconto (PMC sem desconto), será utilizada a pauta sem desconto. Sendo menor, utiliza-se este cálculo do MVA.
- Se o Valor da Operação for menor, será utilizado o preço de pauta com desconto (PMC com desconto).

**4 - Calcular ST (Dif.Alíq. por dentro) BC ST COM Red. ICMS**

Ao definir o campo Tipo de Cálculo de ST Específico com a opção 4 - Calcular ST (Dif.Alíq. por dentro) BC ST COM Red. ICMS, o cálculo em questão será realizado com base na seguinte fórmula: 

```
 (((Vlr. Operação - Vlr. ICMS Destacado) / ((1- (Alíquota de ST/100))) - Redução_ST)
 x Alíquota de ST) – Vlr. ICMS Destacado
```

**5 - Calcular ST Simplificado (Carga Média)**

Optando por configurar o campo Tipo de Cálculo de ST Específico com a opção 5 - Calcular ST Simplificado (Carga Média), o campo Margem Lucro (MVA) terá seu valor zerado e o campo Percentual Carga Trib. Média será habilitado para uso. Sendo assim, se os campos Percentual Carga Trib. Média e Alíq. Subst. Tributária estiverem devidamente preenchidos, o MVA Simplificado será calculado com base na seguinte fórmula:

```
 ((((((1+Alíq.IPI)*Percentual Carga Trib. Média) + ((1-Redução da Base)
*Alíquota))/Alíq. Subst. Tributária) / (1+Alíq.IPI)) -1) *100
```

Caso o cálculo acima resulte em um valor maior que zero, o MVA resultante desse cálculo será aplicado ao cálculo do ICMS ST normal.

Todavia, se o cálculo retornar um valor menor ou igual a zero, as fórmulas abaixo serão utilizadas:

- Para a base - (((Vlr ICMS + (Vlr. Operação \* Percentual Carga Média))/Aliq. ICMS ST);
- Para o Valor de ICMS ST - Vlr. Operação \* Percentual Carga Média.

**6 - Calcular ST sem dedução do ICMS próprio**

Se o campo Tipo de Cálculo de ST Específico for definido com a opção 6 - Calcular ST sem dedução do ICMS próprio, o sistema irá utilizar a seguinte fórmula para obtenção do valor de ICMS ST:

```
 (Vlr. Operação x (1 + % MVA)) x Alíq. Subst. Tributária
```

**8 - Calcular ST (Dif. Alíq. Considerando FCP e Redução de Base de ST)**

Se o campo Tipo de Cálculo de ST Específico estiver selecionado com a opção 8 - Calcular ST (Dif. Alíq. Considerando FCP e Redução de Base de ST), o sistema utilizará a fórmula abaixo para obter o valor de ICMS ST:

```
 (((Valor da Operação -  Redução de Base ST)/ Índice do Percentual do
Diferencial)) * Percentual do Diferencial) - Adicional FCP = Valor do Diferencial
```

**Nota:** habilite o parâmetro **"Manter aliquota no calculo de st especifico tipo 8 - MINTCALCSTSPEC8"** para que a alíquota de ST do cálculo seja aplicada tanto na nota quanto na tabela de imposto (TGFDIN).

![Imagem 15: Especificamente em operações para Parceiros situados em Sergipe/AL, deve-se utilizar a opção 8 - Calcular ST (Dif.…](https://ajuda.sankhya.com.br/hc/article_attachments/23765533194135) Especificamente em operações para [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) situados em Sergipe/AL, deve-se utilizar a opção 8 - Calcular ST (Dif. Alíq. Considerando FCP e Redução de Base de ST) e habilitar o parâmetro **"Cálculo Difal ST Portaria 367/2016 Sergipe - DIFSTPORT367SE"** para que o cálculo do diferencial de alíquota ST devido a esse estado seja realizado por meio da fórmula:

```
 (((Valor da Operação - Redução de Base ST) / (1- Percentual do Diferencial))
* Percentual do Diferencial) - ((Valor da Operação - Redução de Base ST) /
(1- Percentual do Diferencial)) * (% FCP)
```

E o FCP calculado pela fórmula:

```
 (((Valor da Operação - Redução de Base ST) / (1- Percentual do Diferencial)) * (% FCP)
```

**10 - Cálculo de ST Via Pauta sem dedução do ICMS próprio**

Com a opção 10 - Cálculo de ST Via Pauta sem dedução do ICMS próprio selecionada, teremos o cálculo de ICMS ST utilizando a regra de pauta sem a dedução do ICMS da operação própria. Esse cálculo utilizará a seguinte fórmula:

```
 (Valor da pauta x quantidade) x Aliq. Subst. Tributária
```

**11 - Calcular ST (Alíq. Limite créd. ICMS p/ devolução no Valor ST)**

Quando a opção 11 - Calcular ST (Alíq. Limite créd. ICMS p/ devolução no Valor ST) estiver selecionada, será estabelecida no campo **"Alíq. Limite créd. ICMS p/ dedução no Valor ST"** (localizado também nessa aba) a alíquota limite de ICMS a ser reduzida no ST. Dessa forma, temos os seguintes requisitos:

**1)** O valor de ICMS a ser retirado do ST não é o mesmo calculado na nota. Trouxemos o exemplo abaixo:

**(1)** Dados:

- Valor do produto: 100,00
- Alíquota de ICMS: 12%
- Alíquota de ICMS ST: 18%
- Alíquota de ICMS limite para apropriação: 7%
- MVA: 30%

**(1)** Calculo de ICMS: 100,00 x 12% = 12,00

BC ICMS ST: 100,00 + 30%

BC ICMS ST : 130,00

Vlr ST = (130,00 \* 18%) - (100,00 \* 7%)

Vlr ST = 23,40 - 7

Vlr ST = 16,40

**2)** E, caso o valor de Alíquota de ICMS seja menor do que a Alíquota de ICMS limitante, a mesma não deverá ser utilizada:

Dados: 

- Valor do produto: 100,00
- Alíquota de ICMS: 4%
- Alíquota de ICMS ST: 18%
- Alíquota de ICMS limite para apropriação:7%
- MVA: 30%

**(1)** Calculo de ICMS: 100,00 x 4% = 4,00

BC ICMS ST: 100,00 + 30%

BC ICMS ST : 130,00

Vlr ST = (130,00 \* 18%) - 4,00

Vlr ST = 23,40 - 4

Vlr ST = 19,40

**13 - Realizar cálc de ICMS para reduc no ST com alíq espec e utilizando o mesmo % de redução do ST**

Essa opção atende somente notas de venda.

**14 - Cálculo ICMS e ICMS/ST - Decreto 38.286/PE**

Escolhendo a opção 14 - Cálculo ICMS e ICMS/ST - Decreto 38.286/PE no campo Tipo de Cálculo de ST Específico, o cálculo dos impostos ICMS e ICMS/ST serão efetuados das seguintes formas:

- Ao realizar a venda de um produto com CST 10, o sistema irá calcular a variação do valor de venda com o valor de aquisição, em seguida, o resultado será comparado com a alíquota informada no campo **"Percentual/Coeficiente sobre Custo Aquisição - PE"**, considerando as variações a seguir:

        Se a variação estiver acima do percentual informado, será usada a fórmula:

```
 BC ICMS = (CUSTO MÉDIO * (COEFICIENTE/100)) + CUSTO MÉDIO
```

        Se a variação estiver abaixo do percentual informado, será usada a fórmula:

```
 BC ICMS = VLRTOT
```

       Cálculo final: 

```
 ICMS = BC ICMS * Alíquota ICMS
```

      Exemplo:

           Tipo de custo Decreto 38.296/PE = Último Custo Médio sem ICMS > 67,133866667

           Alíquota ICMS = 18%

           Percentual/Coeficiente sobre Custo Aquisição - PE = 13,41%

           Tipo de Cálculo de ST Específico = 14 - Cálculo ICMS e ICMS ST Decreto 38.296/PE

           Compra do item no valor de 100,00 e venda no valor de 150,24 - Variação de 50,24%             (maior que o percentual)

           Então:

           BC ICMS = (67,133866667 \* (13,41/100)) + 67,133866667 = 76,14
           ICMS = 76,14 \* 18% = 13,70

- Quando CST for igual a 60, será utilizada a fórmula abaixo:

```
 BC ST = Custo Médio (campo “Tipo de custo Decreto 38.296/PE” da aba Geral)*(1 +
(MVA/100)) ICMS ST = BC ST * (Aliq ST / 100) - ICMS Próprio
```

        Exemplo:

          Tipo de custo Decreto 38.296/PE = 67,133866667

          MVA e MVA origem estrangeira = 101,11%

          Alíquota ST = 18%

          ICMS Próprio conforme exemplo anterior = 13,70

          Então:

          BC ST = 67,13386667 \* (1 + (101,11/100) ) = 135,01

          ICMS ST = 135,01 \* 0,18 - 13,70 = 10,60

Considerando que o cálculo do ICMS e ICMS ST foram realizados através do Decreto 38.296/PE, quando o CST for 60, é necessário que esses valores sejam destacados no XML:

```
<ICMS60>
<CST> 60, onde traremos o CST
<vBCSTRet> 135,01, a BC do ST
<pST> 18,00, a alíquota do ST
<vICMSSubstituto> 13,70, o valor do ICMS Normal
<vICMSSTRet> 10,60, o valor do ICMS ST
```

**16- Cálculo ICMS/ST - DIFAL - Decreto 40.230/2020- PB**

Para obtenção do cálculo ST conforme Decreto 40.230/2020 da Paraíba, será possível selecionar no campo Tipo de Cálculo de ST Específico a opção 16- Cálculo ICMS/ST - DIFAL - Decreto 40.230/2020- PB. Assim, o sistema realizará o cálculo ST de acordo com a fórmula abaixo:

```
 (((Vlr. Operação - Vlr. ICMS Destacado) / ((1- (Alíquota de ST/100))) - Redução_ST) 
        BC Cálculo ICMS * Diferença Alíquota (Aliq. Interna - Aliq. Origem)
```

**18 - Cálculo ICMS ST e FCP (ICMS de Destino por Dentro)-Protocolo ICMS 104/2008 - AL**

Ao informar o campo Tipo de Cálculo de ST Específico com a opção  18 - Cálculo ICMS ST e FCP (ICMS de Destino por Dentro) - Protocolo ICMS 104/2008 - AL, o sistema irá utilizar a seguinte fórmula para obtenção do valor de ICMS ST:

```
 (((Base de Calculo ICMS Operaçao / (1 - (Alíq. ICMS Interna Destino + Perc. ICMS FCP))) x
         ( 1 - Perc. Redução_ST)) x (Aliquota Interna Destino - Aliquota Interestadual) +
         (Base de Calculo ICMS Operação x Alíq. FCP)
```

**19 - Cálculo ST SUFRAMA com Desoneração Simples Nacional**

Ao definir o campo Tipo de Cálculo de ST Específico com a opção 19 - Cálculo ST SUFRAMA com Desoneração Simples Nacional, deverá ser acionada a marcação **"Desoneração ICMS do Simples Nacional"** localizado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934#abageral), desta tela.

Quando a marcação **"MVA Simplificado"** for realizada, determinará que o cálculo do MVA Simplificado será realizado de forma automática. Teremos aqui uma configuração que implicará na realização de outras definições, bem como o Percentual Carga Trib. Média (campo a seguir) e a Margem Lucro (MVA), também presente nessa aba.

O campo **"Percentual Carga Trib. Média"** será habilitado para uso caso a marcação MVA Simplificado esteja realizada. Informe aqui o percentual da carga tributária média definido em lei.

Esses dois últimos campos, juntamente com as Alíquotas de IPI e de Substituição Tributária, configuram o cálculo do MVA Simplificado de maneira automática no sistema. Em lançamentos de Nota Fiscal de Saída, em uma operação interestadual, destinada a um estado com cálculo de ST com MVA Simplificado, como ocorre no estado do Mato Grosso (MT), o sistema irá verificar se a Alíquota de ICMS que está sendo considerada para o item em questão, possui as configurações acima mencionadas; caso afirmativo, o MVA Simplificado será calculado com base na seguinte fórmula:

```
 ((((((1+Alíq.IPI)*Percentual Carga Trib. Média) + ((1-Redução da Base)
*Alíquota ICMS)) / Alíq. Subst. Tributária) / (1+Alíq.IPI)) -1) *100
```

**Observação:** a Redução de Base somente será considerada (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral)) se a marcação **"Base ST será o valor do produto COM a redução do ICMS?"** presente na aba Substituição Tributária não estiver efetuada, esta informação será zerada na fórmula.

Feito o cálculo do MVA, o cálculo do ICMS-ST irá prosseguir normalmente no sistema.

**Importante:** para a realização do cálculo do diferencial de alíquota por substituição tributária conforme prescreve o Convênio ICMS 142/2018, haverá duas situações distintas de cálculos que são adotadas por certas unidades da federação, assim teremos:

- Cálculo do ICMS diferencial de alíquota ST com a base simples;
- Cálculo do ICMS diferencial de alíquota ST com base dupla.

Referente à primeira regra, deverá ser selecionada a opção **"7 - Calcular ST (Dif.Alíq. Convênio 142/2018 - CFC)"** do campo **"Tipo de Cálculo de ST Específico:"**.

Para a segunda regra, há duas situações distintas, sendo uma sem FCP e outra com FCP.

**Nota:** FCP é a sigla adotada para o Fundo de Combate a Pobreza. Existem UF's que adotam um termo diferente mas com a mesma característica fiscal, podendo ser representado por FECP, FECOP, FECOEP, FEM, etc.

**Observação:** quando  selecionar a opção 17 - Calcular ST - Lei nº 15730/PE do campo Tipo de Cálculo de ST Específico o sistema realizará o seguinte:

```
  ((Vlr. Operação - Vlr. ICMS Destacado) / (1- (Alíquota de ST/100))) x ((Alíquota
de destino - Alíquota Interestadual)/100)
```

Assim, para as operações que adotem a base dupla que não tenham cálculo do FCP, deve-se escolher a opção **"4 - Calcular ST(Dif.Alíq. por dentro), BC ST COM Red. ICMS"** e para as operações que adotem a base dupla e tenham cálculo do FCP, deve-se selecionar a opção **"12 - Calcular ST(Dif.Alíq. por dentro), BC ST COM Red. ICMS COM FCP"**.

Para os casos aqui relacionados, será necessário informar no campo **"Margem Lucro (MVA)"** localizado na presente tela, na aba Substituição Tributária o valor correspondente a **"0,01"**. Sendo assim, informações desnecessárias não irão constar nas tag's de XML, porém, o sistema procederá adequadamente com os cálculos dos valores de impostos.

Em relação à opção **"7 - Calcular ST (Dif.Alíq. Convênio 142/2018 - CFC)"**, o sistema seguirá com o seguinte cálculo:

**(1)** Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral):

- Preencha o campo **"Tributação"** com a opção **"10 - Tributada e c/ Cobrança por Substituição"**;
- Adicione o percentual correspondente no campo **"Alíquotas"**;
- Na Seção DIFAL/FCP, no campo **"Tipo de Cálculo DIFAL e do FCP"** selecione a opção **"5 - Cálculo do DIFAL Convênio 142/2018: Vlr. Operação"**;
- Por fim no campo **"Alíq. Interna Destino"** adicione o percentual correspondente.

**(1)** Na aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasubstituiotributria):

- Preencha o campo **"Margem Lucro (MVA)"** com a devida margem de valor agregado

**Observação:** caso a operação não tenha MVA, o valor informado deve ser **"0,01"**. Essa configuração garante que a informação será gerada corretamente nas TAGs do XML, permitindo o cálculo dos impostos de acordo com as necessidades do cliente.

- Adicione ao campo **"Alíq.Subst. Tributária"** o percentual correspondente;
- Bem como, defina o campo **"Tipo de Cálculo de ST Específico"** com a opção **"7 - Calcular ST (Dif.Alíq. Convênio 142/2018 - CFC)"**.

Assim, o cálculo será dessa forma:

```
 (Vlr da Operação / (1 - (Aliq. Interna - Aliq. Interestadual))) *
(Aliq. Interna - Aliq. Interestadual)
```

Quando a opção **"4 - Calcular ST(Dif.Alíq. por dentro), BC ST COM Red. ICMS"** for selecionada, o sistema seguirá com o seguinte cálculo:

```
 ICMS ST DIFAL = [(Vlr Oper - ICMS origem) / ((100 - ALQ interna)/100)] x ALQ interna -
        (V oper x ALQ interestadual)
```

Em que:

- Vlr. Operação: 1.000,00
- Aliq. ICMS: 12%
- Vlr ICMS: 120,00 (1.000,00 \* 12%)
- Aliq ICMS ST: 18%
- BC ICMS DIFAL ST: 1.073,17 ((1.000,00 - 120,00)/((100-18)/100))
- Vlr DIFAL ST: 73,17 ((1.073,17 \* 18%)-120,00)

Referente à opção **"12 - Calcular ST(Dif.Alíq. por dentro), BC ST COM Red. ICMS COM FCP"** o sistema seguirá com o cálculo abaixo:

```
 ICMS ST DIFAL = [(Vlr Oper - ICMS origem) / ((100 - ALQ interna)/100)] x ALQ interna -
        (V oper x ALQ interestadual)
```

Em que:

- Vlr. Operação: 1.000,00
- Aliq. ICMS: 12%
- Vlr ICMS: 120,00 (1.000,00 \* 12%)
- Aliq ICMS ST: 18%
- Aliq. FCP ST: 2%
- BC ICMS DIFAL ST: 1.100,00 ((1.000,00 - 120,00)/((100-(18+2))/100))
- Vlr DIFAL ST: 78,00 ((1.100,00 \* 18%)-120,00)
- Vlr FCP ST: 22,00 (1.100,00\*2%)

Com a opção **"13 - Realizar cálc de ICMS para reduc no ST com alíq espec e utilizando o mesmo % de redução do ST"** selecionada no campo **"Tipo de Cálculo de ST Específico"** será realizado o cálculo abaixo:

```
 ((((base de ICMS + IPI) + MVA) - Redução Base ST) x Alíquota ST))
- ((Valor do produto - Redução Base ST) x Alíquota de ICMS Específico para
 o cálculo de ST)
```

Quando a marcação **"Cálculo de Desoneração ICMS/ST por Dentro, conforme Resolução SEFAZ nº 13/2019"** for efetuada, o cálculo de Desoneração de ICMS referente ao CST 10, 70 e 90 também será calculado junto ao imposto ICMS/ST, uma vez que, esta respeitará a configuração da marcação **"Cálculo de desoneração ICMS por dentro"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral). Observe a seguir, a fórmula utilizada na desoneração:

```
 ICMS/ST Desonerado = BC ICMS/ST * (1- (Alíquota * (1 - Percentual de redução da BC ))) /
        (1 - Alíquota) - BC ICMS/ST
```

**Observação:** caso haja redução de base de cálculo na operação de Substituição Tributária, o valor desonerado dessa operação deve ser somado à desoneração da operação própria.

Quando a marcação **"Aplicar a aliquota de FCP no cálculo de Desoneração ICMS/ST por Dentro"** estiver habilitada, o sistema considera a alíquota informada no campo % ST FCP Interno/Coeficiente FECOP para obtenção do valor calculado referente a Desoneração ICMS/ST por Dentro, aplicando então a fórmula a seguir:

```
 ICMS/ST Desonerado = BC ICMS/ST * (1- ((Alíquota + Alíquota FCP)*
     (1 - Percentual de redução da BC ))) / (1 - (Alíquota + Alíquota FCP)) - BC ICMS/ST
```

![Imagem 16: A referida marcação só estará disponível caso habilite a marcação Cálculo de Desoneração ICMS/ST por Dentro, conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/23765533194135) A referida marcação só estará disponível caso habilite a marcação Cálculo de Desoneração ICMS/ST por Dentro, conforme Resolução SEFAZ nº 13/2019.

Logo abaixo, você encontrará a marcação **"Desconsiderar redução da base na desoneração ICMS/ST por dentro"**. Esta opção atende às exigências fiscais do Estado do Rio de Janeiro (**Resolução SEFAZ/RJ nº 720/2014**).

Por padrão, ela vem desabilitada. Para conseguir marcá-la, é obrigatório que o checkbox superior **"Cálculo de Desoneração ICMS/ST por Dentro..."** esteja acionado e que o campo **"Motivo da Desoneração do ICMS ST"** esteja preenchido.

- **Regra de Cálculo (CST 70):** quando ativada em operações com CST 70, o sistema isola o ICMS-ST desonerado para que ele **não sofra** a redução da base de cálculo. O valor será calculado considerando a Base Cheia (Valor da Operação + MVA). A redução da base continuará sendo aplicada apenas para o ICMS próprio e para o ICMS-ST reduzido.
- **Comportamento Padrão:** se a marcação for mantida desativada, o sistema seguirá a regra padrão, aplicando a redução da base (CST 70) uniformemente para todos os impostos da operação, incluindo o ICMS-ST desonerado.
- **Geração do XML:** com a regra ativada, o XML da nota será gerado corretamente com o grupo estrutural `<ICMS70>`, apresentando a tag `<vICMSSTDeson>` calculada sobre a base cheia, além das tags `<motDesICMS>` e `<motDesICMSST>`.

O campo **"Motivo da Desoneração do ICMS ST"** possui as seguintes opções: **"Uso na agropecuária"**, **"Outros"** ou **"Órgão de fomento e desenvolvimento agropecuário"** e só poderá ser preenchido quando a marcação Cálculo de Desoneração ICMS/ST por Dentro, conforme Resolução SEFAZ nº 13/2019 estiver realizada.

Ao habilitar a marcação **"Calcular % de Redução BC ICMS Lei 9.025/2020"**, não será possível preencher o campo **"Redução de Base ST"**, pois o valor dele será calculado nos campos Alíq. Subst. Tributária e % ST FCP Interno/Coeficiente FECOP. Observe a seguir, um exemplo do cálculo a ser realizado:

- Alíquota da Carga Tributária = 12%
- Alíquota ICMS ST = 18%
- Alíquota ICMS ST FCP = 2%

**(1)** Então:

1 - (12% / (18% + 2%)) =

1 - 60% = 40%

Se o campo **"Alíquota da Carga Tributária Reduzida"** não for preenchido e for realizado a seleção da marcação Calcular % de Redução BC ICMS Lei 9.025/2020, o cálculo da referida redução não será realizado e o sistema apresentará a mensagem:

**"O campo "Alíquota da Carga Tributária Reduzida" deve estar preenchido para utilizar a opção "Calcular % de Redução BC ICMS Lei 9.025/2020"."**

Desta forma, o ICMS Próprio, Desonerado e a Redução de BC ST serão calculados. Observe a seguir, um exemplo desse cálculo:

Cálculo ICMS ST = Valor da Operação \* (1+MVA)

BC ICMS ST = 117,20 \* (1+0,41) = 165,25

Cálculo ICMS ST Reduzido = BC ICMS ST \* (1 - % da redução de BC ST)

- BC ICMS ST Reduzido = 165,25 \* (1 - 0,40) = 99,15
- Valor do ICMS ST = 99,15\* (18% + 2%) - 14,06 = 5,77

ICMS ST Desonerado = Base ICMS ST \* (1 - (Alíquota padrão \* (1 - Percentual de redução da BC ST))) / (1 - Alíquota padrão) - Preço na Nota Fiscal

Exemplo do Cálculo:

- Alíquota Padrão = 18% + 2% FCP
- Percentual de redução da BC = 1 - (12% / (18% + 2%)) = 1 - 60% = 40%
- Base de Calculo ICMS ST Desonerado = 165,25
- ICMS Desonerado = 165,25 \* (1 - (0,20\*(1-0,40))) / (1-0,20)-165,25 = 16,53

Total do ICMS Desonerado na Operação = 11,72 (ICMS Próprio + 16,53 (ICMS ST) = 28,25

O campo **"Tabela p/ Base ST - Farmácia Popular"** apenas ficará habilitado, se o campo **"Tabela p/ Base ST - PMPF"** estiver vazio.

Assim, ao informar a tabela no campo Tabela p/ Base ST - Farmácia Popular, o sistema irá considerar o **"Valor de Referência"** da tabela para o cálculo da Base de Cálculo do imposto. Feito isso, deve-se comparar o Valor de Referência com o PMC:

- Se o PMC for menor que o Valor de Referência, o PMC passa a ser o valor considerado.
- Se o PMC for maior/igual que o Valor de Referência, utiliza o Valor de Referência.

Considere o exemplo a seguir:

- Valor de Referencia > Captopril 25 mg, comprimido: 0,19 por comprimido = 5,70
- PMC: 43,35
- Comparação: 43,35 >= 5,70, sendo PMC >= Valor Referencia

**(1)** Neste caso, a partir da comparação, sendo PMC maior que o Valor da Referência, utilizaremos o Valor da Referência para composição da base de cálculo.

Quando o campo Tabela p/ Base ST - Farmácia Popular estiver vazio, o campo Tabela p/ Base ST- PMPF será habilitado.

Desse modo, se selecionado no campo Tipo de Cálculo de ST Específico a opção **"15 - Calcular ST P/ Medicamentos - CAT-40/SP"**, ao informar uma tabela no campo Tabela p/ Base ST- PMPF e o produto fizer parte da tabela PMPF, o sistema fará o seguinte cálculo:

```
 PMPF: (Vlr. PMPF * %Trava/100) > 22,14 * 95 / 100 = 21,03
```

O resultado da operação acima deve ser comparada com o **"Valor da Operação"**, afim de decidir qual Base de Cálculo será utilizada para o cálculo do ST, seguindo os critérios abaixo, desde que estes não ultrapasse o PMC:

- Se valor da operação < PMPF \* Trava / 100: Utiliza o PMPF
- Se valor da operação >= PMPF \* Trava / 100: Utiliza o IVA/MVA

Considere os seguintes exemplos:

**Exemplo 1:**

- Vlr Operação: 32,54
- PMPF: 22,14 (PMPF = (Vlr PMPF \* %Trava/100) > 22,14 \* 95 / 100 = 21,03)
- Comparação: 32,54 >= 21,03

**(1)** Neste caso, a partir da comparação, sendo Vlr. Operação maior que o PMPF, utilizaremos o MVA para composição da base de cálculo.

Feito isso é identificado qual o valor será utilizado e  deverá ser comparado o resultado com o PMC:

- Se o PMC for menor que o resultado do item anterior, o PMC passa a ser o valor considerado. Neste caso, não será aplicada a trava, isto é, (PMC x %Trava).
- Se o PMC for maior/igual que o resultado, utiliza o resultado do item anterior. Neste caso, não será aplicada a trava, ou seja, (PMPF x %Trava).

**Exemplo 2:**

- Vlr Operação: 32,54
- PMC: 43,35
- MVA: 33,11 > MVA = (Vlr Operação \* ( 1+ %MVA / 100) > 32,54 \* 1,3311 = 43,31)
- Comparação: 43,35 >= 43,31, sendo PMC >= MVA

**(1)** Neste caso, a partir da comparação, sendo PMC maior que o MVA, utilizaremos o MVA para composição da base de cálculo.

Quando o medicamento não estiver na lista PMPF, o sistema utilizará o IVA/MVA para cálculo da Base de Cálculo do imposto. Feito isso,  deve-se comparar o resultado com o PMC:

- Se o PMC for menor que a MVA, o PMC passa a ser o valor considerado.
- Se o PMC for maior/igual a MVA, utiliza MVA.

Para facilitar sua compreensão, considere o exemplo a seguir:

**Exemplo 3:**

- Vlr Operação: 32,54
- PMC: 43,35
- MVA: 33,11 (MVA = (Vlr Operação \* ( 1+ %MVA / 100)) > 32,54 \* 1,3311 = 43,31)
- Comparação: 43,35 >= 43,31, sendo PMC >= MVA

**(1)** Neste caso, a partir da comparação, sendo PMC maior que o MVA, utilizaremos o MVA para composição da base de cálculo.

Para efetuar o cálculo do ICMS ST com base no Decreto Nº 4.520/2020 utilizando o crédito presumido, acione a marcação **"Calcular ST conforme Decreto 4.520/2020 - PR"**, e, em seguida, preencha o percentual do crédito presumido no campo **"%Crédito Presumido Decreto 4.520/2020 - PR"**. Desse modo, o cálculo será efetuado conforme a fórmula abaixo: 

```
 VLR ICMS ST = (BC ICMS ST * Alíquota ST) - (BC ICMS ST * Crédito Presumido) -
ICMS Normal
```

Considere o exemplo a seguir:

- BC ICMS ST = 3,39
- Alíquota ST = 27%
- Alíquota Crédito Presumido = 13%
- ICMS Normal = 0,22

**(1)** Então:

VLR ICMS ST = (3,39 \* 27%) - (3,39 \* 13%) - 0,22

VLR ICMS ST = 0,91 - 0,44 - 0,22

VLR ICMS ST = 0,25

**Observações:**

- Este cálculo só será realizado se o campo **"Tipo de Cálculo de ST Específico"** estiver com a opção **"0 - Não específico (Regra Geral)"** selecionada.
- O campo %Crédito Presumido Decreto 4.520/2020 - PR poderá ser preenchido apenas se a marcação Calcular ST conforme Decreto 4.520/2020 - PR estiver acionada.

O valor preenchido no campo **"Percentual de Crédito Presumido de ICMS ST Convênio ICMS 106/1996"** será utilizado no cálculo do crédito presumido para preencher as tags <**vRec**> e <**vComp**>, caso a marcação **"Calcular % de Crédito Presumido de ICMS ST Convênio ICMS 106/1996"** esteja habilitada.

Informe o campo **"Alíquota suportada pelo Consumidor Final"** em casos de ICMS com cobrança anterior de Substituição Tributária. Assim, ao emitir uma NF-e de um produto sem rastreamento de estoque (sem entrada anterior), isto é, com o campo **"Alíquota da ST de oper. ant."** (localizado na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)) vazio, a tag **<pST>** será preenchida com o valor do campo Alíquota suportada pelo Consumidor Final. 

No entanto, se o campo Alíquota da ST de oper. ant. estiver informado, o sistema usará esse valor para preencher a tag **<pST>**.

**20 - Calcular ICMS-ST com BC Reduzida por PIS/COFINS Desonerados e ICMS Operação.**

Agora, você pode calcular o ICMS-ST com uma base de cálculo reduzida. Para isso, siga os passos abaixo:

Ao definir o campo **"Tipo de Cálculo de ST Específico"** com a opção **20 - Calcular ICMS-ST com BC Reduzida por PIS/COFINS Desonerados e ICMS Operação**.

O sistema fará o cálculo do ICMS-ST automaticamente, já aplicando a redução da base de cálculo. Isso significa que ele levará em conta os valores de **PIS/COFINS Desonerados e ICMS da operação** antes de calcular o imposto final.

- Base de Cálculo do ICMS-ST

A base de cálculo deve ser obtida subtraindo o valor de ICMS Operação e de PIS/COFINS Desonerados do valor da operação, conforme a fórmula: 

**Base de Cálculo do ICMS-ST = (Valor da Operação - Valor do ICMS Operação - Valor de PIS/COFINS Desonerados) × (1+MVA/100)**

- Cálculo do ICMS-ST

Após determinar a base de cálculo ajustada, o ICMS-ST será calculado pela fórmula: 

**ICMS-ST = (Base de Cálculo do ICMS-ST × Alíquota de Substituição Tributária) - Valor do ICMS Operação**

- Despesas Acessórias

A mesma fórmula deve ser aplicada para determinar o valor de ICMS ST proporcional às despesas acessórias da nota.

**21 - Calcular ST conforme convênio 133/02**

**Quando usar:** utilize em operações interestaduais (ex: venda de veículos) que exigem que o desconto na base do ICMS próprio influencie a base da ST.

**Ordem de Cálculo:** esta opção altera a ordem padrão em que o sistema aplica as reduções e os impostos agregados. Quando selecionada, o sistema executará o cálculo respeitando rigorosamente a seguinte sequência:

1. Aplica a redução da base do ICMS próprio sobre o valor da operação.
2. Soma o valor do IPI ao resultado.
3. Aplica a Margem de Valor Agregado (MVA).
4. Por último, aplica a redução da base do ICMS-ST.

A memória de cálculo gerada seguirá a fórmula:

```
Base ST = (((Valor da Operação * (1 - %Redução Base)) + IPI) * (1 + MVA))
* (1 - %Redução Base ST)
```

> **Atenção:** nos termos do Convênio 166/02, caso a sua operação possua um preço de venda ao consumidor sugerido pelo fabricante, a redução da base do ICMS próprio não deve diminuir a base de cálculo da ST. Certifique-se de preencher as abas de redução corretamente no cadastro da alíquota para garantir a legalidade da operação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Aba SIMPLES Nacional

![Imagem 17: Aba SIMPLES Nacional](https://ajuda.sankhya.com.br/hc/article_attachments/1500003642162)

Para empresas optantes pelo Simples Nacional, todas as regras de ICMS devem ter o campo **"Código de Situação da Operação no Simples Nacional - CSOSN"** configurado com uma das opções de Código CSOSN:

- 101 - Tributada pelo Simples Nacional com permissão de crédito;
- 102 - Tributada pelo Simples Nacional sem permissão de crédito;
- 103 - Isenção do ICMS no Simples Nacional para faixa de receita bruta;
- 201 - Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por ST;
- 202 - Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por ST;
- 203 – Isenção do ICMS no Simples Nac. para faixa de rec. bruta e com cobrança do ICMS por ST;
- 300 – Imune;
- 400 – Não tributada pelo Simples Nacional;
- 500 - ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação;
- 900 – Outros.

**Observação:** é necessário selecionar um código no campo CSOSN, se a empresa cadastrada nesta tela estiver configurada com as marcações **"Optante pelo Simples"** e **"Tem convênio Simples Nacional no Estado"** (tela [Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas), aba [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abanaturezas)) habilitadas e a UF registrada na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), campo **"Cód. UF"** esteja vinculada a essa empresa (tela Empresas, aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abaendereo), campo **"Cód. Cidade"**). Do contrário, caso não seja configurado o campo CSOSN o sistema emitirá o seguinte aviso:

**"Existe empresa do Simples Nacional cadastrada no sistema e o campo CSOSN não foi configurado."**

**Observação:** para os parceiros classificados como **"Consumidor Final Não Contribuinte"** (tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), campo **"Classificação ICMS"**) os CSOSN'S compatíveis são os de código 102, 103, 300, 400 e 500.

**Importante:** quando a empresa é Simples Nacional com rec. Bruta excedida e Regime Normal, não é informado o CSOSN e sim o CST, pois quando o Simples ultrapassa o valor que pode tributar, serão tributados os impostos normalmente.

**Observação:** para que seja realizado o cálculo do FCP Interno referente às empresas optantes pelo Simples Nacional, deve-se selecionar uma das seguintes opções:

- 201 - Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por ST;
- 202 - Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por ST;
- 203 – Isenção do ICMS no Simples Nac. para faixa de rec. bruta e com cobrança do ICMS por ST;
- 900 – Outros.

Para maiores informações acesse o link [Nota Fiscal Eletrônica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica "Nota Fiscal Eletrônica").

**Nota:** no caso onde o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) está configurado como **"Calcular e Digita"** (aba Impostos, campo Cálculo de ICMS, IPI e ISS), e não exista CSOSN configurado na alíquota de ICMS, o CSOSN utilizado poderá ser informado manualmente.

Em casos de Pedido e Nota de Compra, o sistema sempre utilizará o CSOSN que for informado no item. Em Devoluções de Compra, caso tenha algum CSOSN informado na alíquota de ICMS e não tenha informado o CSOSN no item da nota de compra, o sistema utilizará o da alíquota.

**Importante:** se o Tipo de Operação - TOP não for configurado no campo mencionado como **"Calcula e Digita"**, o sistema não necessita que o CSOSN seja informado na grade de itens.

Outros casos:

- Quando se tem uma empresa optante pelo Simples Nacional e um fornecedor que não é, os cálculos de ICMS para os itens da nota serão realizados de acordo com a alíquota configurada.
- Tendo uma nota de devolução para uma empresa que é optante pelo Simples Nacional e o fornecedor que não é, deve-se devolver a nota para o fornecedor do mesmo modelo que ela chegou para empresa, ou seja, considerando os cálculos de Simples Nacional.
- Ao confirmar as notas que foram utilizadas alíquotas que tenham CSOSN 101 ou 201 e tendo cálculo de simples, zeram-se os impostos pertinentes aos itens na confirmação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Aba Combustível

Essa aba será apresentada somente se parâmetro **"Distribuidor de combustível? - COMBUSTIVEL"** estiver habilitado.

![Imagem 18: Essa aba será apresentada somente se parâmetro "Distribuidor de combustível? - COMBUSTIVEL" estiver habilitado.](https://ajuda.sankhya.com.br/hc/article_attachments/1500003690461)

As configurações dessa aba permitem:

- Parametrizar o sistema para NF-e (Nota Fiscal Eletrônica);
- Parametrizar o sistema para cálculo de ICMS ST em operações com combustíveis para SPED (NF-e e EFD);
- Calcular os valores dos campos Base ST UF Destino, Valor ICMS UF Destino e Base ST Operação Anterior, dos itens de uma nota, quando o produto for combustível.

O preenchimento do campo **"Tabela c/ base para ST em favor da UF de destino"** origina-se do cadastro de uma Tabela de Preços no sistema, que irá caracterizar a base de Substituição Tributária da UF de destino.

Informe no campo **"Margem Lucro (MVA) UF Destino"** a **"Margem de Valor Agregado"** ou **"Ajustado da UF de destino"**.

Preencha o campo **"Alíquota Estado Destino"** com a alíquota referente ao estado de destino.

Informe no campo **"Tabela c/base ST operação anterior"** uma tabela de preços válida para o tipo de pauta a ser utilizado.

```
 Base ST Operação Anterior= (QTDNEG * Valor do produto na tabela)
```

Esse valor será destacado no DANFE, no quadro Informações Complementares e será registrado no XML da NF-e como uma TAG de informações adicionais, não gerando cálculo de valor.

**Observação:** as tabelas acima utilizarão tabelas de preço do sistema para informar as diversas pautas existentes (Pauta por PMPF, por VLR Refinaria e por VLR Unitário Médio).

Deve-se configurar o campo Base ST UF Destino por:

- Se estiver marcado Pauta, a base será calculada usando a tabela informada no campo Tabela c/ Base ST em Favor da UF de Destino.
- Se marcar Valor do Produto, será usado o valor na nota.

O cálculo é feito da seguinte forma:

- Base ST em Favor da UF de Destino = (QTDNEG \* VLRPROD) + MVA (se for informado).
- ICMS Devido na UF de Destino = Base ST em Favor da UF de Destino \* Alíquota de ICMS p/ UF Destino.

**Nota:** os campos **"Base ST UF Destino"**, **"Valor ICMS UF Destino"** e **"Base ST Operação Anterior"**, presentes na grade de itens da nota também são habilitados pelo parâmetro Distribuidor de combustível? - COMBUSTIVEL; logo, quando esse parâmetro estiver desabilitado, esses campos não serão mais visíveis na grade de Itens.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Aba ICMS Antecipado Entradas Interestaduais

![Imagem 19: Aba ICMS Antecipado Entradas Interestaduais](https://ajuda.sankhya.com.br/hc/article_attachments/1500003642202)

Nessa aba, tem-se os seguintes campos:

No campo **"Regra p/ cálculo da base ICMS AT"** temos as opções abaixo:

- **Cálculo por dentro:** Considerando que essa será a opção padrão do sistema, o seguinte cálculo será executado: (Valor líquido do produto + IPI) - (ICMS normal do item) / ((100 - Alíquota de ICMS Interna) / 100); sendo que o **"Valor líquido do produto"** será o valor do produto mais despesas acessórias menos desconto, caso haja algum;
- **Cálculo (Valor líquido do produto + IPI):** Por meio dessa opção, o sistema fará o cálculo:  Base de Cálculo da operação própria + IPI.
- **Fórmula personalizada:** Quando selecionado essa opção, o sistema habilitará o campo **"Fórmula para Cálculo da Base do ICMS AT"** para que o código de fórmula criado na tela Fórmulas diferencial de Alíquota possa ser informada.

Por meio do campo **"Alíquota ICMS AT (%)"** deve ser informada a alíquota do ICMS que será aplicada sobre a base de ICMS AT.

No campo **"Alíquota ICMS AT produto importado (%)"** poderá informa-se a alíquota do ICMS determinada para aplicação nas operações com produtos importados.

Preencha o campo **"Alíquota de ICMS Interna (%)"** com a alíquota do ICMS interna, ou seja, a alíquota de ICMS da UF que dará a entrada da mercadoria em seu estabelecimento.

**Observação:** o campo acima será habilitado ao marcar a opção Cálculo por dentro.

Por fim, no campo **"Deduzir do ICMS AT"**, defina se haverá dedução do ICMS normal e ICMS ST nos cálculo do ICMS AT dentre as seguintes opções e as respectivas fórmulas que serão utilizadas por cada uma delas:

- **Sem dedução:** (Base de ICMS AT x Alíquota ICMS AT) - ICMS normal = ICMS AT;
- **Deduzir ICMS normal:** (Base de ICMS AT x Alíquota ICMS AT) - ICMS normal = ICMS AT;
  **Deduzir ICMS-ST:** (Base de ICMS AT x Alíquota ICMS AT) - ICMS ST = ICMS AT;
- **Deduzir ICMS normal e ICMS-ST:** (Base de ICMS AT x Alíquota ICMS AT) - (ICMS Normal + ICMS ST) = ICMS AT.

**Nota:** nas regras acima, deve ser considerada a alíquota ICMS AT conforme a origem do produto, sendo o campo Alíquota ICMS AT (%) para produtos nacionais e Alíquota ICMS AT produto importado (%) para produtos importados.

**Observação:** para que os valores referentes ao ICMS AT apenas são informados nos itens da nota após a confirmação da mesma.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Validações que facilitam este cadastro

De acordo com a definição realizada no campo **"Tributação"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), teremos habilitadas ou desabilitadas as Modalidades Modalidade BC ICMS e Modalidade BC ICMS ST, aba Geral e aba Substituição Tributária, respectivamente), dessa forma, trouxemos o exemplo abaixo:

Tributação preenchida como Tributada Integralmente não permite Modalidade BC ICMS ST, sendo assim, essa modalidade é desabilitada sempre que essa tributação for selecionada. O campo Tabela c/ Base p/ ST só pode ser preenchido se a tributação contemplar Substituição Tributária. Se o campo Modalidade BC ICMS estiver definido como Pauta (Valor), o campo Tabela c/ Base p/ ICMS deve ser preenchido, pois a Pauta exige tabela.

O sistema validará:

1. A combinação do campo Tributação com os campos Modalidade BC ICMS e Modalidade BC ICMS ST, ao habilitar ou desabilitar, conforme o caso (Tributação de ICMS, Tributação de ST);
2. O campo Usar a maior base para Subst.Tributária deve ser utilizado juntamente com a Tabela c/base p/ST;
3. O campo Usar a maior base para ICMS deve ser usado junto com a Tabela c/base p/ICMS.

- Para visualizar/editar os detalhes da alíquota, clique no último item da árvore ou dê um duplo clique na linha desejada da grade.
- Após a confirmação do registro, os campos UF Destino, UF Origem, e as Exceções não podem ser alteradas.
- Quando se cadastra uma alíquota, se a combinação de exceções ainda não existir, o sistema abre um pop-up para configuração das prioridades das restrições; também poderá fazê-lo por meio do botão **"Outras Opções..."**, opção **"Prioridades"**.
- Estando posicionado em um item da árvore que seja UF Destino e/ou UF Origem, ao clicar em incluir, o sistema sugere o preenchimento dos campos UF Origem e UF destino.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Cálculo do ICMS Garantido Integral

A tributação dos produtos que se enquadram nesse sistema é semelhante à substituição tributária, ao diferenciar pelos seguintes aspectos:

- O imposto é pago na barreira;
- Ocorre somente nas compras;
- O valor do imposto não é somado ao total da nota.

Devem ser configurados os parâmetros abaixo para os que trabalham com esse tipo de tributação:

- **Código da observação para o garantido integral - CODOBSGARANTIDO:** A observação informada nesse parâmetro será a mesma utilizada na configuração de Alíquotas de ICMS para os produtos do garantido.
- **Código do imposto para o garantido integral - CODIMPGARANTIDO:** Configura-se na tela [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos), o imposto cujo código será informado neste parâmetro.

Ao configurar os parâmetros acima, o sistema passa a calcular o valor do imposto Garantido Integral. Deve-se também configurar nas exceções de alíquota dos produtos que se enquadram no regime do Garantido Integral, o mesmo código de observação informado no parâmetro CODOBSGARANTIDO.

Ao calcular os totais da nota e os impostos, o sistema não soma o Garantido Integral ao total da nota e na base da ST; separa o total da base e valor da ST, dos itens cujo código de observação seja o mesmo do informado no parâmetro CODOBSGARANTIDO e grava este valor na tabela de outros impostos (TGFIMN), através do código informado no parâmetro CODIMPGARANTIDO.

Para gerar uma parcela de despesa no financeiro referente ao valor do imposto Garantido integral, basta configurar a função VALORIMPOSTO (código, tipo) no cadastro do [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), onde código é o mesmo do informado no parâmetro CODIMPGARANTIDO e tipo pode ser V (valor), B (base) ou A (alíquota).

No cadastro da alíquota de ICMS, temos o campo **"Redução base ST"**, presente na aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasubstituiotributria). Nas compras, se houver alíquota de redução de base informada nesse campo, o sistema utiliza e reduz a base de ST, caso contrário, não o faz.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Cálculo de ICMS por distinção de alíquotas similares

Existem casos no processo de cálculo de ICMS em que as exceções disponíveis no cadastro das respectivas alíquotas não são suficientes para retratar o cenário em que a movimentação ocorre. Além disso, em situações que a alíquota de ICMS para produtos estrangeira é aplicada, não só alíquota mas outras informações precisam ser substituídas como Tributação, Redução da Base, entre outras.

Esse tópico apresenta os dados que permitirão a definição de novas exceções de alíquotas, além das já existentes no cadastro de alíquotas de ICMS. Essa é uma configuração que deve ser utilizada apenas em caso específicos. Vejamos seus detalhes:

- Com o parâmetro **"Permite duplicar cad. de tributação alíquota ICMS? - PODEDUPALIQICMS"** ativo, quando for realizada a duplicação de uma alíquota, todos os dados pertinentes à ela serão reproduzidos também na nova alíquota gerada, tais como, Tributação, Alíquota, Redução da Base etc.
- O Cadastro de Alíquotas de ICMS está apto a receber Campos Adicionais; o cadastro de um campo adicional é realizado na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados) onde, nesse caso, deve-se fazê-lo na tabela TGFICM. Finalizado o cadastro do campo adicional e acessando novamente o Cadastro de Alíquotas de ICMS, será possível notar uma nova aba denominada "Campos adicionais", que será alimentada logicamente pelos campos adicionais anteriormente criados.
- Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), caso o parâmetro **"Permite duplicar cad. de tributação alíquota ICMS? - PODEDUPALIQICMS"** esteja habilitado, será apresentada a aba Filtro de Alíquota ICMS. Nessa aba será cadastrado um filtro que irá distinguir alíquotas que possuam os mesmos tipos de restrições; informe na aba uma cláusula AND de uma restrição SQL, de modo que esta será utilizada na obtenção das alíquotas de ICMS, quando este imposto for calculado na nota.

Ainda nas Preferências da Empresa, também na aba Filtro de Alíquota ICMS, temos o ícone  localizado à frente do campo Filtro p/ obtenção da alíquota de ICMS que, ao ser acionado, exibirá as configurações aceitas para o filtro, bem como, exemplos de sua utilização.

**Importante:** indica-se que essa configuração seja feita com o acompanhamento de um Consultor Sankhya.

- Também sob a influência da ativação do parâmetro **"Permite duplicar cad. de tributação alíquota ICMS? - PODEDUPALIQICMS"**, no próprio cadastro de alíquotas de ICMS, botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#botooutrasopes...), temos também a opção Filtro p/ obtenção da alíquota de ICMS, para que possa realizar o mesmo tipo de cadastro citado acima. Esse filtro será único para todas as alíquotas de ICMS cadastradas.
- No momento de calcular a alíquota de ICMS, caso sejam encontradas mais de uma alíquota com as mesmas regras, será considerado o filtro definido nas Preferências da Empresa pra distingui-las; caso nas Preferências da Empresa não exista um filtro informado, será considerado o filtro inserido no Cadastro de Alíquotas de ICMS para diferenciá-las. Se ainda assim, em nenhum desses locais existir um filtro para distinguir a alíquota, a primeira regra de alíquota encontrada será considerada e aplicada.

**Observação:** se durante o cálculo forem encontradas mais de uma alíquota que atendam o filtro, a primeira dessas alíquotas será considerada para o cálculo.

#### Particularidade no Cálculo para o Paraná (PR)

Ao realizar o cálculo da distinção de alíquotas (DIFAL) em operações interestaduais destinadas ao Estado do Paraná, o sistema adota a seguinte regra para o Fundo de Combate à Pobreza (FCP):

- **Regra de Dispensa:** Conforme a legislação paranaense (Art. 1º do Anexo XII do RICMS/PR), o FCP é parte integrante do DIFAL. Portanto, **se não houver valor de DIFAL a recolher** (devido à carga tributária efetiva ou equiparação de alíquotas), **o sistema não calculará o FCP**, zerando ambos os valores.

Essa validação segue o entendimento das Soluções de Consulta nº 132/2015 e nº 47/2021 da SEFAZ/PR.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

### Botão Outras Opções...

O botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15993376482455) **"Outras Opções..."**, localizado na parte superior esquerda da tela dispõe de quatro funcionalidades:

#### Prioridade das Restrições

Essa opção é utilizada para determinar a ordem de prioridade das exceções de alíquotas. Deve-se escolher sempre uma ordem decrescente de prioridades, de modo que as alíquotas sem exceção devem ficar por último na classificação. Assim, veja o exemplo:

Cadastre uma alíquota de ICMS dentro de um mesmo Estado, que tenha exceção, primeiro pelo produto X e depois pela cidade destino Y. Nesse caso, a configuração de prioridades deve ser:

- 1º por produto;
- 2º por cidade destino;
- 3º sem exceção.

![Imagem 21: 3º sem exceção.](https://ajuda.sankhya.com.br/hc/article_attachments/1500003642282)

#### Copiar...

Ao acionar essa opção, será aberto o pop-up **"Cópia de Alíquotas de ICMS"** que possibilita a realização de uma cópia de alíquota. Para isso, é necessário o preenchimento dos devidos filtros visando selecionar a alíquota desejada. Logo em seguida, informe a configuração da alíquota de Destino.

![Imagem 22: Ao acionar essa opção, será aberto o pop-up "Cópia de Alíquotas de ICMS" que possibilita a realização de uma cópia de…](https://ajuda.sankhya.com.br/hc/article_attachments/360102523594)

Uma vez informadas as UF's de Origem e Destino, as Exceções e os dados da alíquota de Destino, clique no botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15993332796823) **"Copiar"**para concretização do procedimento.

#### Conversão de CFOP's

Essa opção tem a função de quando for necessário e exigido, em determinada operação, substituir uma CFOP por outra; o **Sankhya Om** dispõe de mecanismo que efetua essa conversão/substituição.

Ao acionar essa opção, será aberto um pop-up também de nome **"Conversão de CFOP's"** onde informe a CFOP que será substituída, bem como, por qual CFOP ela será substituída.

![Imagem 24: Ao acionar essa opção, será aberto um pop-up também de nome "Conversão de CFOP's" onde informe a CFOP que será…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003690761)

Feito isso, no lançamento cujo processo esteja configurado para o cálculo da CFOP XXXX, ou seja, a CFOP a ser substituída, o sistema irá converter a mesma para a nova CFOP YYYY.

**Nota:** a configuração da conversão é por alíquota e não geral.

**Importante:** o número de caracteres dos campos que dizem respeito ao ICMS têm capacidade para até 10 dígitos desde que não excedam o número 2.147.483.647.

**Observação:** se tratando de emissão de CT-e, o sistema irá realizar as validações abaixo:

- Se o documento lançado for um CT-e;
- Se o campo Tipo de emissão CT-e  for igual a N - Normal ou C - Complementar ou S - Substituição;
- Se a UF da cidade Início do CT-e for diferente de EX;
- Se a UF da cidade Fim do CT-e for diferente de EX;
- Se a UF da cidade Início do CT-e for igual à da UF da cidade da Empresa do CT-e e se for Subcontratação, converter o CFOP para 5360 quando operação interna e 6360, quando operação interestadual;
- Caso todas essas validações sejam verdadeiras, o sistema irá acatar o CFOP definido 5360 ou 6360.

**Nota:** caso seja selecionada a opção Subcontratação e a UF da cidade Início do CT-e seja igual a UF da cidade da Empresa do CT-e, o sistema irá converter automaticamente para o CFOP 5360, se operação interna, e CFOP 6360 caso a operação seja externa.

#### Buscar exatamente pelo código da alíquota

Selecionando essa marcação, ao efetuar uma busca por uma Alíquota de ICMS (campo de Pesquisa) e informando o código do registro desejado, o sistema irá buscar pela alíquota na íntegra, ou seja, irá trazer precisamente a alíquota correspondente ao código digitado.

Caso a marcação esteja desabilitada (situação padrão), ao realizar a pesquisa por uma Alíquota de ICMS, o código informado servirá como base para busca dos registros, de modo que o sistema irá apresentar todas as alíquotas que possuem em sua composição o código informado; a cada vez que a tecla Enter é pressionada, o sistema exibe o código posterior. Considere o exemplo abaixo:

Buscar exatamente pelo código da alíquota Marcada:

- Ao pesquisar pela alíquota de código 15, o sistema irá filtrar e exibir apenas esta alíquota.

Buscar exatamente pelo código da alíquota Desmarcada:

- Ao pesquisar pela alíquota de código 15, o sistema irá apresentar as alíquotas de código 15, 515, 1522, 2215 e assim sucessivamente.

**Observação:** a definição realizada nessa marcação será válida para todos os usuários; não é uma definição individual.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top)

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16025028111127) Acesse também:

[Desoneração do ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597834-Desonera%C3%A7%C3%A3o-do-ICMS)

[Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado)

[ICMS para produtos de Origem Estrangeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111873-ICMS-para-produtos-de-Origem-Estrangeira)

[Finalidade da Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599434-Finalidade-da-Opera%C3%A7%C3%A3o)

[Finalidade da Operação - Onde informar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596074-Finalidade-da-Opera%C3%A7%C3%A3o-Onde-informar-)
