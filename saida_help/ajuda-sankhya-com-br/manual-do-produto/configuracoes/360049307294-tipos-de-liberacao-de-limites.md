---
id: "360049307294"
titulo: "Tipos de Liberação de Limites"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-24T18:50:26Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Liberação de Limites", "ENDACESSEXTWGE", "Vendas", "Financeiro", "br.com.sankhya.liberacao.limites", "USAMAIDESCPROMO", "FORCEVLRLIBBX", "BLOQVENDAVIST", "VALDESCMAX", "LISTOPDESCONEV9", "DIASSEMVENDA", "GERMEMCLAEVELIB"]
---

# Tipos de Liberação de Limites

Abaixo, trataremos sobre os tipos de liberação de limites que encontram-se disponíveis no Sankhya Om.

#### **(1)** Alteração de comportamento

A partir desta versão sankhya-om - 4.35b810 / 4.36, módulo erpcore 5.13.2, quando uma alteração no item fizer com que a liberação deixe de ser necessária, o sistema removerá automaticamente a solicitação de liberação pendente.

Nas versões anteriores, a solicitação permanecia registrada como pendente mesmo após a alteração do item, podendo manter o documento bloqueado indevidamente.

Esse comportamento passa a ocorrer independentemente da configuração do parâmetro **GERMEMCLAEVELIB**, que continua sendo utilizado exclusivamente para controlar a geração da memória de cálculo dos eventos de liberação.

| [1 - Desconto Tipo Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#1-descontotiponegociao) | [2 - Desconto Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#2-descontoproduto) |
| --- | --- |
| [3 - Limite de Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#3-limitedecrdito) | [4 - Prazo Mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#4-prazomnimo) |
| [5 - Prazo Médio Máximo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#5-prazomdiomximo) | [6 - Prazo Máximo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#6-prazomximo) |
| [7 - Prazo Cad. Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#7-prazocad.parceiro) | [8 - Atraso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#8-atraso) |
| [9 - Tempo inativo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#9-tempoinativo) | [10 - Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#10-estoque) |
| [12 - Frete CIF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#12-fretecif) | [13 - Valor mínimo Tipo Negoc.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#13-valormnimotiponegoc.) |
| [14 - Valor máximo Tipo Negoc.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#14-valormximotiponegoc.) | [15 - Limite Créd. Mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#15-limitecrd.mensal) |
| [16 – Metas de Despesa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#16metasdedespesa) | [18 - Confirmação de Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#18-confirmaodenota) |
| [19 - Lucro mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#19-lucromnimo) | [20 - Lançamento de Compras p/...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#20-lanamentodecompraspcontrato) |
| [21 - Fórmula Desc. Máx...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#21-frmuladesc.mx.tiponegociao) | [22 - Quant. Máx. de títulos vencidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#22-quantidademximadettulosvencidos) |
| [23 - Bonificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#23-bonificao) | [24 – Autorização de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#24autorizaodepagamento) |
| [25 - Desconto por item da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#25-descontoporitemdanota) | [26 - Limite de crédito pela Média...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#26-limitedecrditopelamdianegociao) |
| [27 – Fórmula Desc. Máx. Tipo Negoc...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#27frmuladesc.mx.tiponegoc.poritem) | [28 – Limite de Bonificação por Projeto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#28limitedebonificaoporprojeto) |
| [29 - Desconto no Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#29-descontonofinanceiro) | [30 - Perdão de Multa no Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#30-perdodemultanofinanceiro) |
| [31 - Perdão de Juros no Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#31-perdodejurosnofinanceiro) | [32 - Descontos Financeiros por Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#32-DescontosFinanceirosporParceiros) |
| [33 - Antecipação de Orçamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#33-antecipaodeoramento) | [34 - Suplementação de Orçamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#34-suplementaodeoramento) |
| [35 - Transferência de Orçamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#35-transfernciadeoramento) | [36 - EPI antes do Vencimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#36-epiantesdovencimento) |
| [37 -EPI sem devolução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#37-episemdevoluo) | [38 - Caract. de Análises de Laudo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#38-caractersticasdeanlisesdelaudo) |
| [39 - Quantidade de Parcelas na Reneg.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#39-quantidadedeparcelasnarenegociao) | [40 - Solicitação de Compra p/...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#40-solicitaodecomprapprodutoemestoque) |
| [41 - Confirmação de Nota com análise...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#41-confirmaodenotacomanlisedositens) | [42 - Limite de Crédito por Grupo...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#42-limitedecrditoporgrupodetip.ttulo) |
| [44 - Liberação exigida pela TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#44-liberaoexigidapelatop) | [45 - Liberação para Laudo...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#45-liberaoparalaudodematriaprima) |
| [48 - Margem de Contribuição Mínima](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#48-margemdecontribuiomnima) | [55 - Liberação de grupo de autorização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#55-liberaodegrupodeautorizao) |
| [56 - Variação percentual no custo pedido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#56-Varia%C3%A7%C3%A3opercentualnocustopedido) | [58 - Variação na quantidade Pedido/Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#58-Varia%C3%A7%C3%A3onaquantidadePedido/Nota) |
| [61 - Liberação de data de validade...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#61-Libera%C3%A7%C3%A3odedatadevalidademenorqueoprevistro) | [63 - Liberação Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#63-Libera%C3%A7%C3%A3oFinanceiro) |
| [64 - Corte/divergência de pedido...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#64-cortedivergnciadepedidoconferncia) | [66 - Desconto do item abaixo do calculado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#66-Descontodoitemabaixodocalculado) |
| [67 - Excede Estoque Máximo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#67-ecedeestoquemaimo) | [68 - Variação do vlr. unit. orig./dest.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#68-variaodovlr.unit.orig.dest.) |
| [70- Acréscimo do valor unitário ref. ao último custo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#h_01KFXC3QWNRG18M4PDNP7Q1QM9) | [74 - Venda mínima por Parc./Cid...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#74-vendamnimaporparceirocidaderegio) |
| [75 - Diferença entre NCM, CEST ou Origem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#75-diferenaentrencmcestouorigem) | [76 - Diferença de impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#76-diferenadeimpostos) |
| [77 - Análise de crédito expirada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#77-anlisedecrditoexpirada) | [78 - Liberação de agrupamento mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#78-liberaodeagrupamentomnimo) |
| [79 - Fechamento Fiscal Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#79-FechamentoFiscalCont%C3%A1bil) | [81 - Desvio na quantidade apontada de PA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#81-desvionaquantidadeapontadadepa) |
| [82 - Pendências Financeiras maiores...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#Pend%C3%AAnciasFinanceirasMaioresQueOEstoqueDispon%C3%ADvel) | [83 - Liberação de Laudo de Classificação...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#Libera%C3%A7%C3%A3odeLaudodeClassifica%C3%A7%C3%A3op/Armazenagem) |
| [84 - Liberação para Destinação de Verba](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#84-libera%C3%A7%C3%A3oparadestina%C3%A7%C3%A3odeverba) | [Informações adicionais acerca dos eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#01JQPPR1J7RWW2VTE1R058JHJ6) |

### 1 - Desconto Tipo Negociação

O evento 1 - Desconto Tipo Negociação verifica o valor total do desconto no documento para acionar a liberação de limites. Isso significa que, mesmo que o percentual de desconto mude ao faturar apenas alguns itens de um orçamento de venda, o sistema considera o valor total do desconto como base para validar o evento.

O evento é acionado quando o valor total do desconto é maior do que o configurado no Tipo de Negociação utilizado na venda. Essa validação ocorre na confirmação do pedido de venda.

**Como configurar o evento:**

Para o funcionamento deste evento, é necessário realizar a seguinte configuração:

- No cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), na aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), configurar no campo **"% Desconto Máximo"** o valor máximo de desconto que a empresa permite ao utilizar aquele Tipo de Negociação.

**Exemplo:** Na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), ao proceder com um pedido de venda ou uma venda e informar um desconto no rodapé da nota que seja superior ao limite determinado no Tipo de Negociação, ou se os descontos inseridos nos itens da nota ultrapassarem o estipulado, o sistema abrirá o pop-up de solicitação de Liberação de Limites.

Isso ocorre mesmo que o percentual de desconto mude ao faturar apenas alguns itens, pois o sistema considera o valor total do desconto.

**Observação:** o parâmetro **"Valida desconto máx do tipo de negoc.? - DESCMAXTPN"** se ligado, faz com que o sistema solicite a liberação do evento 1 – Desconto tipo negociação caso o valor de desconto do produto seja maior que o configurado no Tipo de Negociação utilizado na venda. Se desligado não será solicitada a liberação desse evento.

**Nota:** o evento 1 - Desconto por Tipo de Negociação é validado quando o desconto é dado no rodapé da nota. Sendo que, para atender normas fiscais da Receita, o desconto no rodapé da nota será rateado nos itens. Portanto, mesmo sem configurar o evento 2 - Desconto Produto, ao confirmar a nota será solicitada a liberação do mesmo, pois neste momento o sistema tentará ratear o desconto nos produtos.

Para que isto não ocorra, configure no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba **"Venda"**, o campo **"% Desconto máximo"** com o valor 100% para que, ao confirmar a nota o sistema apresente somente o evento 1 - Desconto por Tipo de Negociação.

Outra opção para atender esta exigência fiscal, será configurar o evento 2 - Desconto Produto igual ao evento 1 - Desconto por Tipo de Negociação para que, ao confirmar a nota, o sistema faça a liberação dos dois eventos. Para isto, os parâmetros a seguir devem estar configurados da seguinte forma:

**"Valida desconto máximo - VALDESCMAX"** = VALIDA E NÃO ACEITA;

**"Trabalha com Perc.Desconto no pé da nota - PERCDESCPE"** = SIM;

**"Calcular 'Desconto no total' pelos itens? - DESCTOT"** = SIM;

**"Aceita desconto por Produto/Serviço? - DESCPRO"** = SIM.

**Observação:** em casos que os eventos 1 e 25 ocorrerem de maneira simultânea, o sistema utilizará a seguinte fórmula:

```
 Vlr item bruto sem desconto - Vlr item bruto sem desconto
```

Portanto, temos as fórmulas para circunstâncias em que a nota possui o desconto no produto e desconto no pé da nota:

**DIFERENÇA DE DESCONTO NOS PRODUTOS**

```
 descTot = (Vlr item bruto sem desconto - Vlr item bruto sem desconto)
```

**VALOR DO DESCONTO MAXIMO EM CIMA DOS PRODUTOS**

```
 descMax = Vlr item com desconto * (%De desconto do tipo de negociação/100)
```

**DESCONTO MÁXIMO PERMITIDO**

Para chamar o evento 1:

```
 ValMaxDescEvento = descMax + (-descTot) 
```

![Imagem 1: Com o parâmetro "Não consid. benef. fiscal como desc. no evento 1 - BENFISDESCEV1" ligado, o desconto de imposto…](https://ajuda.sankhya.com.br/hc/article_attachments/22512556654487) Com o parâmetro **"Não consid. benef. fiscal como desc. no evento 1 - BENFISDESCEV1"** ligado, o desconto de imposto associado à liberação de valores não será considerado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 2 - Desconto Produto

O funcionamento deste evento se deve à realização das seguintes configurações:

- No cadastro de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), no campo **"% Desconto Máximo"** presente na aba Venda, configure o percentual de desconto máximo que pode ser oferecido para aquele produto em uma venda.

**Exemplo:** Ao lançar um Pedido ou Nota e incluir um Produto aplicando desconto superior ao informado no Cadastro de Produtos, será aberto o pop-up de solicitação de liberação.

- É necessário atentar-se também para a configuração do parâmetro **"Valida desconto máximo - VALDESCMAX"**, pois ele modifica o comportamento desta validação na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

**Importante:** antes de realizar uma liberação configurando no pop-up **"Limites para Liberações"** (botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es) da tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)) o Evento com **"Tipo Limite"** igual a **"Mensal"**, o sistema verifica todas as liberações efetuadas durante o mês corrente e libera o desconto somente se ainda houver limite a ser utilizado.

É importante destacar que, quando dois produtos possuem diferentes valores no campo % Desconto Máximo, ao lançá-los juntos na Central de Vendas, o sistema considera esses dois valores máximos de desconto para calcular o total. Observe o exemplo:

O produto 3 que custa R$ 100,00, possui na aba Venda no cadastro de Produtos, um % Desconto Máximo de 5%. Já o produto 1 que custa R$ 153,12, possui no mesmo campo um desconto máximo de 100%. Assim, dado que o usuário informe que o produto 3 tem 50% de desconto, mas o produto 1 não possui desconto, o sistema não chamará o evento de liberação de desconto, pois a soma dos dois descontos não ultrapassa o valor total de desconto dos dois produtos juntos.

Para entender melhor, observe o cálculo:

**Produto 3:** 5% de desconto máximo.

**Produto 1:** 100% de desconto máximo.

**Valor total do desconto para os dois produtos:** 105%

**Descontos informados:**

50% de desconto para o Produto 3

0% de desconto para o Produto 1

**Total de desconto aplicado:** 50%

Como o valor total do desconto aplicado (50%) é menor que o desconto máximo permitido (105%), o pop-up de solicitação de liberação não será exibido neste caso.

#### **(1)** Memória de cálculo

Quando habilitado, o parâmetro **GERMEMCLAEVELIB** faz com que o sistema registre a memória de cálculo dos eventos de liberação 2, 3, 25 e 66, detalhando os critérios que originaram a solicitação de liberação, como percentual de desconto aplicado, valor total do item e limite permitido.

Essas informações ficam disponíveis ao liberador durante a análise da solicitação, permitindo identificar o motivo da liberação sem a necessidade de consultar o pedido manualmente.

### [GIF animado: Imagem 2: Essas informações ficam disponíveis ao liberador durante a análise da solicitação, permitindo identificar o motivo da…](https://ajuda.sankhya.com.br/hc/article_attachments/42311037827607)

A memória de cálculo detalha as seguintes informações:

- **soma do preço de tabela**: preço original do produto definido no cadastro;
- **soma do valor do desconto**: diferença entre o preço de tabela e o preço de venda;
- **soma do desconto máximo permitido**: valor máximo de desconto configurado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 3 - Limite de Crédito

Para este evento, temos as seguintes configurações:

- O parâmetro **"Valida limite de crédito? - VALLIMCRED"** deve estar configurado para validar;
- No cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), no campo **"Limite de crédito"** presente na aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacrdito), defina um valor.

**Exemplo:** ao lançar uma Nota (mais precisamente no ato da confirmação do Pedido/Nota), se a soma dos débitos do Parceiro forem superiores ao Limite de Crédito definido para o Cliente, será aberto o pop-up de solicitação de liberação. Mas lembre-se que, uma vez que a liberação já foi realizada e o pedido confirmado, a liberação de limites não será solicitada novamente mesmo que haja alteração nos produtos do pedido.

#### **(1)** Opções de validação do limite de crédito

**Valida limite de crédito? - VALLIMCRED:** Determine neste parâmetro, se serão ou não validados os limites de crédito dos parceiros; optando-se por validar, defina também como será essa validação; o parâmetro tem as seguintes opções:

- **Não valida:** não validará o limite de crédito;
- **Valida todo a receber:** validará o limite de crédito. Na solicitação de liberação do evento para o valor solicitado será considerado financeiros **"Reais"** existentes e o financeiro do lançamento em curso (**"Real"** ou **"Provisão"**), sendo que essa validação ignora provisões existentes;
- **Valida a receb. e prov. no mês:** irá validar o limite de crédito. Na solicitação de liberação do evento para o valor solicitado será considerado financeiros Reais e Provisão com data de negociação (TGFFIN.DTNEG) dentro do mês corrente + o valor do lançamento em curso (Real ou Provisão);
- **Valida TUDO p/TOP c/Financeiro:** validará o limite de crédito. Na solicitação de liberação do evento para o valor solicitado serão considerados financeiros Reais existentes mais o financeiro do lançamento em curso (somente em lançamento que atualiza financeiro Real). Para o lançamento que provisiona financeiro, o sistema permite confirmar quando o parceiro não tem financeiros Reais existentes que ultrapassem o limite de crédito;

Ao fazer lançamento que provisiona financeiro será solicitada a liberação somente se os financeiros Reais existentes ultrapassarem o limite de crédito, para o valor solicitado será considerado apenas os financeiros Reais existentes.

Com a opção Valida TUDO p/TOP c/Financeiro selecionada no parâmetro e a TOP da nota atualizar o financeiro, o sistema exigirá a liberação de limites. Caso a TOP da nota não atualize financeiro, não será exigida a liberação de limites.

- **Valida TUDO p/TOP c/Financeiro com provisão:** irá validar o limite de crédito. Na solicitação de liberação do evento para o valor solicitado serão considerados todos os financeiros pendentes, Reais e Provisões, inclusive o financeiro do lançamento em curso (Real ou Provisão).

#### **(1)** Pontos importantes

- Na configuração desse evento, caso o parâmetro **"Valida Limite de crédito pela matriz? - LIMCREDMATRIZ"** esteja habilitado e o parceiro matriz configurado não possuir limite de crédito, a liberação do evento não será solicitada.
- Os parâmetros **"Não consumir limite de crédito por Tipo de Negociação - VALLIMCRETPV"** e **"Não consumir limite de crédito por Tipo Título? - VALLIMCRETIT"** também influenciam na rotina para usar o evento 03, sendo assim, se atente nas configurações dos mesmos quando se tratar de vendas com cartão de crédito e debito; se eles estiverem com a opção **"Nenhum"** selecionada, mesmo que seja uma venda de cartão de débito (à vista), o sistema solicitará a liberação do evento 03;
- Já o parâmetro **"Validar limite de crédito com valor zero? - VALLIMCREDZERO"**, quando ligado, permite que o sistema valide limites de crédito para parceiros com limite  configurado como zero.

**Observação:** quando houver uma confirmação de pedido de venda em que os eventos 3 - Tipo de Limite e/ou [8 - Atraso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#8-atraso) tenham sido liberados, porém, o Parceiro for alterado, o sistema irá solicitar novamente a liberação desses eventos.

#### **(1)** Memória de cálculo

Quando habilitado, o parâmetro **GERMEMCLAEVELIB** faz com que o sistema registre a memória de cálculo dos eventos de liberação 2, 3, 25 e 66, detalhando os critérios que originaram a solicitação de liberação, como percentual de desconto aplicado, valor total do item e limite permitido.

Essas informações ficam disponíveis ao liberador durante a análise da solicitação, permitindo identificar o motivo da liberação sem a necessidade de consultar o pedido manualmente.

[GIF animado: Imagem 3: Essas informações ficam disponíveis ao liberador durante a análise da solicitação, permitindo identificar o motivo da…](https://ajuda.sankhya.com.br/hc/article_attachments/31002893907991)

A memória de cálculo detalha o **"Valor Solicitado"**, que representa o valor total do pedido. Além disso, apresenta possíveis quebras do valor solicitado, auxiliando na análise do limite de crédito e na tomada de decisões sobre a liberação do pedido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 4 - Prazo Mínimo

O cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) em si, não faz a validação se o prazo de vencimento da(s) parcela(s) é inferior ao prazo mínimo estipulado no campo **"Prazo mínimo"** (aba Características). Essa validação ocorre no lançamento das notas ou pedidos de Vendas.

Deste modo, na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), quando é feito o lançamento de uma nota/pedido que utilize um Tipo de Negociação com a configuração descrita, o sistema exige a liberação para o evento 4 correspondente ao prazo. Assim, basta especificar um usuário com alçada para liberação de limites de tal evento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 5 - Prazo Médio Máximo

Este evento é utilizado no caso de uma pessoa alterar manualmente as parcelas de uma venda.

**Exemplo:** Temos um Tipo de Negociação cujo prazo é 0/30/60 dias, portanto, seu prazo médio é de 30 dias. Informando 30 no campo **"Prazo médio máximo"** presente na aba Características do cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), quando for feita a tentativa de alteração da Data de Vencimento de parcelas fazendo com que o prazo médio aumente, o sistema irá impedir tal modificação. Com isso, será aberto o pop-up de Solicitação de Liberação de Limites para o evento 5 - Prazo Médio Máximo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 6 - Prazo Máximo

Para validação deste evento, temos as seguintes configurações:

No cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), no campo **"Prazo máximo"** presente na aba Características, informe em quantidade de dias, até quando poderão se estender os parcelamentos para aquele Tipo de Negociação. Esta informação também é utilizada no caso de alguma alteração manual nas parcelas de uma Venda.

**Exemplo:** Ao lançar uma Nota, se for modificada uma alteração nas parcelas de modo que seja ultrapassado o **"Prazo Máximo"**, será aberto o pop-up de Solicitação de Liberação de Limites para o evento 6 - Prazo Máximo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 7 - Prazo Cad. Parceiro

Para este evento, realize as seguintes configurações:

- No cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), na aba Geral, no campo **"Prazo médio pagamento"** configure a carência para pagamento que o cliente terá, a partir do faturamento.
- No cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), no campo **"Base do prazo"** presente na aba Características, selecione a opção **"A partir do dia"** e realize a marcação **"Valida prazo de cliente"**.

**Exemplo:** Esta informação também é utilizada caso alguma alteração manual seja feita nas parcelas de uma venda. Ao lançar uma Nota, as parcelas forem alteradas de modo que o prazo configurado no cadastro do Parceiro seja ultrapassado, será aberto o pop-up de solicitação de Liberação de Limites.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 8 - Atraso

O funcionamento deste evento se deve à realização das seguintes configurações:

- No cadastro de Parceiros, no campo **"Tolerância p/ inadimplência"** presente na aba Crédito, configure o prazo que o cliente terá de carência para pagamento depois que o título estiver vencido.
- Configure no parâmetro **"Dias de carência para atraso e limite de crédito - DIASCAR"** a quantidade de dias, após o título estar vencido, para considerar um cliente em atraso.
- Configure no cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) o campo **"Atraso"** presente na aba Validações, com a opção **"Validar e Bloquear"**.

**Exemplo:** ao realizar uma Venda, se o cliente estiver com pagamentos em atraso a um prazo superior ao configurado acima, será aberto o pop-up de solicitação de Liberação de Limites.

---

#### Regra de Atraso e Recriação de Pedido de Liberação

Caso o pedido de venda não esteja confirmado, o sistema irá apagar automaticamente a liberação de limite de crédito associada. Dessa forma, quando a confirmação do pedido for solicitada novamente, o sistema recriará a liberação de limite de crédito, exigindo uma nova aprovação.

---

**Observação:** quando houver uma confirmação de pedido de venda com os eventos 3 - Tipo de Limite e/ou 8 - Atraso já liberados, porém, o Parceiro for alterado após essa confirmação, o sistema irá solicitar novamente a liberação desses eventos.

O parâmetro **"Considera todas as empresas do parceiro no atraso? - ATRASMATRIZ"**, será validado em conjunto com este evento quando na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), o campo **"Matriz"** se encontrar preenchido. Se o referido parâmetro estiver habilitado, o sistema validará o atraso do parceiro pela sua matriz, ou seja, se uma filial estiver em atraso fará com que seja bloqueada a venda para todas as outras filiais. Quando desligado, a validação de atraso será efetuada para cada filial, independente da matriz.

**Observação:** o Parceiro Matriz deve definir como Matriz o seu próprio código.

O Evento 8 - Atraso, também é influenciado pelo parâmetro **"Considerar baixa futuras p/atraso? - BXAFUTLCATRA"**, que possui o seguinte comportamento: se ligado, faz com que as baixas futuras sejam consideradas na validação de atraso, ou seja, um título baixado com baixa futura será tratado como **"em atraso"** na hora de validar os limites na Central; caso esteja desligado, o sistema passará a não considerar as baixas futuras na validação de atraso, portanto, não validará o atraso para esses títulos.

---

![Imagem 4: Informações adicionais sobre os parâmetros que influenciam no evento 8:](https://ajuda.sankhya.com.br/hc/article_attachments/17084212891799) **Informações adicionais sobre os parâmetros que influenciam no evento 8:**

- Caso o parâmetro DIASCAR esteja habilitado, a tolerância será determinada por este, ou seja, qualquer parceiro possuirá a mesma tolerância. Por outro lado, caso o parâmetro **"Usar Tolerância Inadimplência p/calc.atraso? - USATOLERINADIMP"** esteja ligado, a tolerância será estabelecida de acordo com o Cadastro de Parceiros, ou seja, cada Parceiro terá sua tolerância.
- Se ambos os parâmetros acima estiverem ligados, o sistema considerará apenas a chave USATOLERINADIMP e, neste caso, se o Parceiro não possuir configuração, será considerado como zero.
- A configuração do campo **"Subtipo"** da aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) da tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), com a opção **"Cartão de Crédito"** definida, irá abranger um cliente em atraso, mas não impedirá a confirmação da nota, pois será considerada como uma venda garantida. O sistema terá o mesmo comportamento com o Subtipo **"Á vista"**, contudo, para este, pode-se do utilizar o parâmetro **"Bloquear vendas a vista p/clientes em atraso? - BLOQVENDAVIST"** para impedir a confirmação da Nota para clientes que estejam em atraso.
- As vendas realizadas com o Tipo de Negociação Á vista ou **"Parcelado"** com o Subtipo **"Cartão de Débito"** ou **"Cartão de Crédito"** serão validadas, mas não bloqueadas.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 9 - Tempo inativo

Para funcionamento deste evento, temos as seguintes configurações:

- Configure no parâmetro **"Nro de dias p/avisar que o cliente está sem venda - DIASSEMVENDA"** o tempo em dias, a partir do qual o sistema avisa que o cliente está sem negociar com a empresa.
- No cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), no campo **"Prazo p/ contato"** presente na aba Crédito, configure o tempo, em dias, para contato com o cliente.

**Exemplo:** Ao lançar uma Venda, sendo ultrapassado o tempo configurado acima, o sistema apresenta a mensagem **"Cliente inativo desde..."**, bloqueia a Venda e abre o pop-up de solicitação de Liberação de Limites.

**Nota:** o prazo de inatividade será verificado levando-se em consideração a data do último orçamento ou pedido de venda que o parceiro efetuou. Ou seja, o tempo em dias configurado no parâmetro de chave DIASSEMVENDA passará a contar a partir desta data.

**Observação:** a funcionalidade do parâmetro DIASSEMVENDA, tanto para avisar, quanto para bloquear a venda para parceiros que não compram a X dias, não é aplicada em Tipos de Negociação à vista.

Caso queira que determinadas TOPs não realizem a validação desse evento, basta informar os respectivos códigos separados por vírgula (,), ponto e vírgula(;) ou quebra de linhas, no parâmetro **"TOP's de Orçamento para desconsiderar o Evento 09 - LISTOPDESCONEV9"**. Desta forma, ao realizar um lançamento de venda que esteja com dias sem negociação configurado no parâmetro DIASSEMVENDA, o sistema permitirá o envio, mas manterá o Parceiro como **"Inativo"**.

**Importante:** essa validação também não acontecerá se você informar TOPs de Pedido de Venda ou Venda.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 10 - Estoque

O funcionamento deste evento se deve à realização das seguintes configurações:

- Ative o parâmetro **"Libera estoque por empresa pelo F10? - ACEITACSENHA"**.
- No cadastro de [Grupo de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os), efetue a marcação **"Pedir confirmação de liberação"** localizada na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os#abaestoque).
- No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (TOP de Venda), esta deve ser configurada para atualizar estoque.

**Exemplo:** Ao lançar uma Venda, se o Produto estiver sem estoque, é aberto o pop-up de solicitação de Liberação de Limites.

O parâmetro **"Solicitante/Itens na tela de liberação de limites? - MOSSOLITELIBEM"** quando ativado, acrescenta no pop-up de Liberação de Limites, os dados do solicitante (Código e Nome).

Se necessário realizar o lançamento de um pedido para uma empresa que não possua estoque disponível, ligue o parâmetro **"Liberação de estoque para reserva de estoque? - LIBESTRESERVA"**, assim, ao salvar os produtos na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), uma mensagem será apresentada informando que a reserva foi feita, direcionando a solicitação de Liberação de Limites ao evento 10 - Estoque:

**"Avisos**
**Liberação de estoque pendente."**

**Importante:** o parâmetro **"Usar liberação de limites por alçada? - USALIBLIM"** deve estar ligado para que a o parâmetro LIBESTRESERVA funcione efetivamente.

**Observação:** a marcação **"Copiar liberações quando faturando individualmente"** localizada na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) do Tipos de Operação - TOP não afeta na validação do evento, que ocorre exclusivamente durante a inclusão ou atualização de itens na nota fiscal. Portanto, se um pedido for criado, o evento 10 for liberado e a TOP de faturamento estiver com essa opção desabilitada, a validação só será  realizada quando houver alterações nos itens da nota fiscal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 12 - Frete CIF

Para este evento, realize as seguintes configurações:

- No cadastro de [Regiões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074-Regi%C3%B5es), no campo **"Frete mínimo"**, defina um valor mínimo que a nota deverá ter quando o frete for **"CIF"**, ou seja, quando o frete for pago por quem envia a mercadoria, o Remetente.
- No cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), na aba Endereço, informe a Região.

**Exemplo:** Se o valor de uma nota com Frete CIF for menor que o informado no cadastro de Regiões, será solicitada a liberação de limites para este evento; em seguida, será emitida a mensagem:

**"Valor mínimo p/ frete CIF não atingido (Cadastro de Região)."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 13 - Valor mínimo Tipo Negoc.

O funcionamento deste evento se deve à realização da seguinte configuração:

- No cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), na aba Características, registre o valor mínimo que o Tipo de Negociação em questão permite, no campo **"Valor mínimo p/ Venda"**.

Exemplo:  Utilizando este Tipo de Negociação em uma Venda, se o valor da nota for abaixo do estipulado, será solicitada a liberação de limites para este evento.

O conceito de liberação para os eventos 13 - Valor Mínimo Tipo Negociação, 19 - Lucro Mínimo e 48 - Margem de Contribuição Mínima difere do conceito de liberação dos demais eventos, pois envolve valores mínimos.

Nos outros eventos, o percentual cadastrado para o liberador deve ser maior do que o solicitado, já que o gatilho de solicitação do evento é o teto. Em contraste, para os eventos mencionados, o percentual cadastrado deve ser menor do que o solicitado, pois o gatilho é o piso.

Exemplo:

Evento 25 - Desconto por Item da Nota:
O máximo de desconto permitido em um produto é 20%; caso contrário, é necessária a solicitação de liberação. O liberador deve ter cadastrado o maior percentual que pode liberar, por exemplo, 30%. Qualquer desconto superior a 30% não será autorizado.

Evento 19 - Lucro Mínimo:
O mínimo de lucro em uma venda deve ser de 10%; caso contrário, é necessária a solicitação de liberação. O liberador deve ter cadastrado o menor percentual que pode liberar, por exemplo, 5%. Qualquer lucro inferior a 5% não será autorizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 14 - Valor máximo Tipo Negoc.

Para este evento, temos a seguinte configuração:

- No cadastro de Tipos de Negociação, na aba Características, registre o valor máximo que o Tipo de Negociação em questão permite na venda e na compra, nos campos **"Valor máximo p/ Venda" e "Valor máximo p/ Compra"**, respectivamente.

**Exemplo:** Utilizando este Tipo de Negociação em uma Compra, se o valor da nota ultrapassar o que foi determinado no Tipo de Negociação, será solicitada a liberação de limites para este evento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 15 - Limite Créd. Mensal

Para este evento, realize a seguinte configuração:

- No cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), configure o campo **"Limite crédito mensal"** presente na aba Crédito.

**Exemplo:** No momento da Venda, se o valor de uma parcela exceder o limite mensal do Parceiro, é aberto o pop-up de solicitação de Liberação de Limites.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 16 – Metas de Despesa

Quando uma nota de compra extrapolar o valor do previsto na Meta/Orçamento, no momento da confirmação do pedido, o sistema apresentará o pop-up de solicitação de liberação para este evento. Se a nota estiver dividida em parcelas, será solicitada a liberação de todas as parcelas.

Para que ocorra o controle deste evento, são necessárias as seguintes configurações:

- No módulo Controle Orçamentário e Metas, deve-se criar um orçamento de despesa;
- Configure, neste orçamento, as TOP's que serão utilizadas nos Lançamentos de Despesas e para lançamentos de Notas de Compra na Central de Atendimento ao Fornecedor;
- Planejar qual será o valor do orçamento;
- Configurar o evento Metas de Despesa para os usuários que poderão liberar;
- No momento da confirmação de uma Nota de Compra ou no Lançamento de uma Despesa, se o valor do lançamento ultrapassar o valor orçado, o sistema solicitará a liberação com a seguinte mensagem:

**Previsão de despesa excedida!!! <Nome da Meta e Data do planejamento>**

**Nota:** se a liberação referente ao evento 16 - Metas de Despesa for negada, sendo feita a alteração do valor, o sistema irá realizar uma nova solicitação de liberação.

**Importante:** em relação a este evento, será gravado no campo **"VLRTOTAL"** da tabela **"TSILIB"** o montante para o qual se deseja liberação (no caso o valor do financeiro). Esse valor então será utilizado para comparar com o montante liberado, caso o valor liberado seja maior ou igual a esse total, não será solicitada uma nova liberação. O sistema trabalha de modo que a liberação de Metas de Despesa não será solicitada uma segunda vez, caso o seu valor já tenha sido liberado. Independente de existir novos lançamentos, o sistema irá verificar se o valor liberado atende aquela solicitação.

Quando pelo menos um dos parâmetros **"NIVAPROVANTECIP"**, **"NIVAPROVSUPL"** ou **"NIVAPROVTRANSF"** estiver ligado, a meta cadastrada no módulo Metas e Controle Orçamentário em Delphi, deverá ter o **"Centro de Resultado"** como campo escolhido. Dessa forma, o liberador do evento será responsável pelo Centro de Resultado e que está informado na tela de cadastro de Centro de Resultado.

**Aba Propriedades**

![clip6154](https://ajuda.sankhya.com.br/hc/article_attachments/15297211251479)

Marque no quadro **"Quando exceder a Despesa Prevista**" a opção em conformidade ao que o sistema deverá levar em consideração. Se a opção de solicitação de liberação for marcada, ao efetuar os lançamentos que condizem com a Meta, será solicitada a liberação de limites, evento 16 – Metas para Despesas.

**Aba TOP**

É preciso também configurar as TOP's que serão consideradas nos lançamentos feitos para estas para a Atualização do Realizado e Previsão do Planejamento de Metas/Orçamentos, como pode-se visualizar na figura acima.

No Sankhya OM, no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras), ao efetuar um lançamento com as TOP's configuradas na Configuração da Meta e este exceder a Despesa Prevista, será solicitada a liberação de limites. Feita a liberação do evento 16, será possível confirmar a nota.

Após a confirmação da nota, é possível efetuar a atualização do realizado por meio da tela [Atualização do Realizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609774-Atualiza%C3%A7%C3%A3o-do-Realizado).

**Observação:** no lançamento de uma despesa financeira sem Orçamento Previsto, o sistema solicita a liberação deste evento e **"zera"** o valor do desdobramento. Quando for feita a Liberação de Limites, o sistema automaticamente atualizará o valor do desdobramento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 18 - Confirmação de Nota

O funcionamento deste evento se deve à realização das seguintes configurações:

- No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) , na aba Validações, efetue a marcação **"Exigir Liberação antes da Confirmação"**.

**Exemplo:** Ao confirmar um Pedido ou Nota, cuja TOP utilizada no lançamento esteja com a referida marcação realizada, será aberto o pop-up de solicitação de Liberação de Limites para este evento.

Este evento não trabalha com a aba **"Liberação em Cascata"** também presente no cadastro dos Tipos de Operação. Caso existam usuários em cascata configurados para este evento, o sistema somente irá disponibilizar o primeiro da lista.

**Observação:** as notas de complemento não geram a liberação de nenhum evento.

![Imagem 6: Este evento somente será disparado uma única vez ao confirmar o documento.](https://ajuda.sankhya.com.br/hc/article_attachments/26489853980951) Este evento somente será disparado uma única vez ao confirmar o documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 19 - Lucro mínimo

O conceito de liberação para os eventos 13 - Valor Mínimo Tipo Negociação, 19 - Lucro Mínimo e 48 - Margem de Contribuição Mínima difere do conceito de liberação dos demais eventos, pois envolve valores mínimos.

Nos outros eventos, o percentual cadastrado para o liberador deve ser maior do que o solicitado, já que o gatilho de solicitação do evento é o teto. Em contraste, para os eventos mencionados, o percentual cadastrado deve ser menor do que o solicitado, pois o gatilho é o piso.

Exemplo:

Evento 25 - Desconto por Item da Nota:
O máximo de desconto permitido em um produto é 20%; caso contrário, é necessária a solicitação de liberação. O liberador deve ter cadastrado o maior percentual que pode liberar, por exemplo, 30%. Qualquer desconto superior a 30% não será autorizado.

Evento 19 - Lucro Mínimo:
O mínimo de lucro em uma venda deve ser de 10%; caso contrário, é necessária a solicitação de liberação. O liberador deve ter cadastrado o menor percentual que pode liberar, por exemplo, 5%. Qualquer lucro inferior a 5% não será autorizado.

Para validação deste evento, tem-se a seguinte configuração:

- No cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), na aba Características informe no campo **"% Lucro mínimo"** o percentual mínimo de lucro que a empresa pode obter quando utilizar o tipo de negociação em questão.

Exemplo: no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (pedido e notas), o sistema verifica o lucro mínimo da nota e, sendo este inferior ao percentual cadastrado, será aberto o pop-up de solicitação de liberação de limites.

Neste caso de validação de valores mínimos, os parâmetros para validação são inversos; se é definido que o valor minimo é X, e uma movimentação exige um valor de -2X, o usuário responsável pela liberação deve ter um limite cadastrado que seja, no mínimo, igual ou inferior a -2X para o evento em questão.

Exemplo:

Tipo de Negociação: venda
Lucro Mínimo: 5%

Ao confirmar a nota, é solicitado o valor de liberação de 3,61% para o evento Lucro Mínimo. Considerando os seguintes limites de liberação para os usuários:

Usuário 1 - 2%
Usuário 2 - 3,62%
Usuário 3 - 3,6%

Neste caso, os usuários que podem liberar a nota são:

Usuário 1 - 2% (pois 2% é menor ou igual a 3,61%).
Usuário 3 - 3,6% (pois 3,6% é menor ou igual a 3,61%).

![Imagem 7: O usuário 2 só poderia liberar solicitações de lucro mínimo no valor percentual maior ou igual a 3,62%. Além disso,…](https://ajuda.sankhya.com.br/hc/article_attachments/22512556654487) O usuário 2 só poderia liberar solicitações de lucro mínimo no valor percentual maior ou igual a 3,62%. Além disso, utilizando este Tipo de Negociação em uma Venda, se o valor da nota for abaixo do estipulado, será solicitada a liberação de limites para este evento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 20 - Lançamento de Compras p/ Contrato

O funcionamento deste evento se deve à realização da seguinte configuração:

- O parâmetro **"Exige liberação p/lançar compras? - EXIGLIBCTCPA"** deve estar ativado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 21 - Fórmula Desc. Máx. Tipo Negociação

Para validação deste evento, é necessário realizar as seguintes configurações:

- Na tela [Fórmulas para desconto máximo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo) cadastre uma Fórmula de Desconto.
- No cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), no campo **"Fórmula desc. máximo"** presente na aba Características, informe a Fórmula de Desconto cadastrada no item anterior.

**Exemplo:** Ao lançar uma Nota, se os descontos excederem o que foi definido na Fórmula para desconto máximo, é aberto o pop-up de solicitação de Liberação de Limites.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 22 - Quantidade Máxima de títulos vencidos

Para esta validação, realize as seguintes configurações:

- No cadastro de [Tipos de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), efetue a marcação **"Validar Qtd. Máx. Títulos Vencidos"** localizado na aba Geral.
- O parâmetro **"Usar liberação de limites por alçada? - USALIBLIM"** necessita estar habilitado.
- O evento 22 - Quantidade Máxima de títulos vencidos deverá possuir um usuário liberador.
- No cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), configure no campo **"Qtd. máx. de títulos vencidos"** presente na aba Crédito, a quantidade máxima de títulos vencidos aceitos para cada Parceiro; o sistema irá se basear nesta informação para fazer a validação.

**Importante:** se o número de títulos vencidos for maior que o informado no campo Qtd. máx. de títulos vencidos da tela e aba acima informadas, será apresentada a seguinte mensagem:

**Parceiro com XX título(s) vencido(s) no Financeiro. Seu limite é de YY. Maior atraso é ZZ. A tolerância é XX.**

**Nota:** não será realizada a validação do evento 22 - Quantidade Máxima de títulos vencidos caso no parâmetro **"TOP p/impressão de NF p/acompanhar Cupom Fiscal - TOPIMPFISCAL"** esteja inserida a mesma TOP da nota que está sendo confirmada. Para que ocorra a validação deste evento, no campo **"Inteiro"** do parâmetro insira uma TOP que seja apenas relacionada à Cupom Fiscal ou não informe nenhum valor.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 23 - Bonificação

O funcionamento deste evento, se deve à realização das seguintes configurações:

- O parâmetro "Usa Desc. Bonificação? - DESCBONIF" deve estar ativado;
- A tela [Limites de Bonificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599894-Limites-de-Bonifica%C3%A7%C3%A3o) deve estar configurada;
- No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), na aba Geral, efetue a marcação **"Bonificação"**.

**Exemplo:** Se a marcação Bonificação presente na TOP estiver realizada, ao proceder com uma Venda a utilizando, é aberto o pop-up de solicitação de Liberação de Limites para o evento 23 - Bonificação, no valor total da nota. Com a marcação Bonificação não realizada, será solicitada a liberação para o evento 23 - Bonificação com base na somatória dos valores informados no campo **"Bonificação"** dos itens.

Na tela de solicitação de liberação de limites para bonificação, será sugerido pelo sistema o Gerente do Vendedor para liberação.

- Para isso, deve-se fazer a ligação pelos campos Funcionário e Empresa presentes no Cadastro de [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) (aba Identificação) e no Cadastro de [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores) (aba Geral). Faz-se a associação informando os mesmos códigos nos campos Funcionário e Empresa em ambos os cadastros.
- Na tela de liberação, quando o evento for de Bonificação e o Usuário Liberador possuir mais de um período, é aberta uma tela para que você escolha qual dos períodos será utilizado. Para validar o limite do Liberador no Período, será utilizado o somatório das notas liberadas pelo mesmo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 24 – Autorização de Pagamento

---

![Imagem 8: Este evento passou a utilizar exclusivamente a tela Autorização de Pagamentos , não sendo mais necessário o uso da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/26489853980951) Este evento passou a utilizar exclusivamente a tela [Autorização de Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606274), não sendo mais necessário o uso da tela Liberação de Limites.

---

Para que ocorra o controle deste evento, são necessárias as seguintes configurações:

- No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), para **"TOP de Pagamento"**, na aba Validações, no campo **"Valor mínimo p/ Autorização de Pagamento"**, informe o valor mínimo do título, acima do qual, o sistema bloqueará a baixa e solicitará a liberação.
- Configure o evento **"Autorização de Pagamento"** para as pessoas que poderão liberá-lo.

**Exemplo:** Quando for feita a tentativa de Baixa de um Título de despesa, cujo valor seja superior ao informado na TOP, é aberto o pop-up de solicitação de Liberação de Limites.

Para autorizar os pagamentos preventivamente, utilize a tela [Autorização de Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606274-Autoriza%C3%A7%C3%A3o-de-Pagamentos). A Autorização de Pagamentos é utilizada em todos os pontos de baixa no sistema, Baixa Normal, Automática, Automática por Vendedor, Baixa por Cheques, Baixa de Duplicatas e Baixa por Processamento de Arquivo Retorno.

No parâmetro **"Endereço para acesso externo ao WGE - ENDACESSEXTWGE"**, deve-se informar o endereço onde o sistema está hospedado e que pode ser acessado externamente. Caso haja alguma alteração na localização da base, é necessário atualizar esse parâmetro com o IP correto.

É fundamental que o endereço informado nesse campo seja exatamente o mesmo utilizado para acessar o sistema, a fim de evitar erros no processo de redefinição de senha.

Além disso, o endereço de acesso ao sistema pode variar conforme o local de acesso. Por exemplo, em uma rede interna, o endereço pode ser <http://127.0.0.1:8080/mge>, enquanto, para acesso interno e externo, pode ser <http://www.empresa.com.br/mge>.

**Importante:** para o evento 24 – Autorização de Pagamento, recomenda-se não utilizar a liberação em cascata, configurada na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba [Liberação em Cascata](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaliberaoemcascata).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 25 - Desconto por item da nota

O funcionamento deste evento se deve à realização das seguintes configurações:

- A validação será feita pelo Percentual de desconto máximo de cada item, informado no Cadastro de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), campo **"% Desconto Máximo"** presente na aba Venda.
- Sendo necessário utilizar a validação pelo total da Nota, utilize no parâmetro **"Valida desconto máximo - VALDESCMAX"** a opção **"Valida e Não aceita (somente na confirmação)"**.

Se o parâmetro de chave VALDESCMAX estiver definido como **"VALIDA E NÃO ACEITA"** e o produto estiver cadastrado com o campo % Desconto Máximo igual a "0" ou "vazio", o comportamento será:

- Caso exista desconto promocional cadastrado e o valor de venda seja o valor da promoção, não será solicitada liberação de limites para o evento 25 - Desconto por item da nota;
- Se houver desconto promocional cadastrado e o valor de venda for menor que o valor da promoção, será solicitada liberação de limites para o evento 25 - Desconto por item da nota;
- Caso não exista desconto promocional cadastrado e o valor de venda seja menor que o preço de tabela, será solicitada liberação de limites para o evento 25 - Desconto por item da nota.

Portanto, caso você queira que o evento 25 não seja solicitado para o produto, será necessário informar **"100%"** no campo % Desconto Máximo e no Cadastro de Produtos, aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abavenda), a marcação **"Promoção"** não deverá ser acionada para o produto.

É importante ressaltar que o sistema trabalha com uma precisão fixa de duas casas decimais para cálculos relacionados a descontos. Abaixo, considere um exemplo que ilustra como é determinado o valor máximo de desconto permitido para um item:

**Dados iniciais:**

- Valor de venda: 0,08
- Valor de desconto: 0,01
- Percentual máximo de desconto: 0,1
- Valor unitário: 0,08 − 0,01 = 0,07

**Cálculo do Desconto Máximo:**

0,08 × 0,1 = 0,008 (aplicando arredondamento para duas casas decimais: **0,01**)

**Cálculo do Desconto:**

0,08 − 0,07 = 0,01

Se o desconto calculado for maior que o desconto máximo permitido, o sistema gera uma solicitação de liberação para o evento 25.

#### **(1)** Memória de cálculo

Quando habilitado, o parâmetro **GERMEMCLAEVELIB** faz com que o sistema registre a memória de cálculo dos eventos de liberação 2, 3, 25 e 66, detalhando os critérios que originaram a solicitação de liberação, como percentual de desconto aplicado, valor total do item e limite permitido.

Essas informações ficam disponíveis ao liberador durante a análise da solicitação, permitindo identificar o motivo da liberação sem a necessidade de consultar o pedido manualmente.

[GIF animado: Imagem 9: Essas informações ficam disponíveis ao liberador durante a análise da solicitação, permitindo identificar o motivo da…](https://ajuda.sankhya.com.br/hc/article_attachments/31003308370711)

A memória de cálculo detalha as seguintes informações:

- **preço de tabela**: preço original do produto definido no cadastro;
- **valor do desconto**: diferença entre o preço de tabela e o preço de venda;
- **desconto máximo permitido**: valor máximo de desconto configurado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos).

---

#### **(1)** Validação do desconto ao incluir ou alterar um item na grade

Ao incluir ou alterar um item na grade [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), o sistema realiza a validação dos parâmetros **"Valida desconto máximo - VALDESCMAX"** e **"Usa liberação de limites por alçada? - USALIBLIM"**.

Se o VALDESCMAX estiver configurado como **"Valida e Aceita"**, qualquer desconto será aceito, mas uma mensagem de aviso será exibida.

Além disso, ao alterar o Tipo de Movimento da nota, o sistema pode recalcular o preço de custo do item, controlado pelo parâmetro **"Recalcula preços quando altera Tipo de Negociação: - RECPRECOTPV"**. Durante esse recálculo, ocorre a seguinte validação:

- A nota não pode ser de compra;
- O produto deve estar marcado como **"Promoção"** (configuração realizada na aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abavenda));
- O desconto aplicado deve ser maior que o desconto máximo permitido;
- O [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) não pode ter [Taxa Especial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abataxasespeciais).

Se todas essas condições forem atendidas, o desconto aplicado será substituído pelo desconto máximo permitido para o produto.

Desse modo, para garantir que os descontos sejam validados corretamente, considere as seguintes opções:

- Ajustar a configuração do VALDESCMAX conforme a política de descontos da empresa.
- Definir um desconto máximo adequado para os produtos, dentro da faixa normalmente aplicada.
- Utilizar o parâmetro RECDESCTPV.

---

#### **(1)** Informações Adicionais sobre o Evento 25 - Desconto por Item da Nota

**(2)** No faturamento de um pedido de venda ([Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)), sendo feita alguma modificação nas informações pertinentes ao Local, Código do Produto ou Controle na nota que é gerada, tem-se uma nova solicitação de liberação para o evento 25 - Desconto por item da nota, mesmo que a liberação para tal evento já tenha sido realizada para o pedido faturado e o percentual de desconto não tenha sido alterado.

**(2)** Ao configurar a liberação para o evento 25 - Desconto por item da nota, para que a ordem da digitação entre a quantidade e valor unitário não interfiram na apresentação da tela de liberação, o parâmetro **"Bloquear valor menor que o preço de tabela? - BLOQVLRMENORTAB"** deve estar desativado.

**(2)** Quando ocorrer a solicitação de liberação do evento 25 - Desconto por Item da Nota, serão disponibilizados para escolha os Usuários Liberadores, tomando-se por base o valor extrapolado. Por exemplo, suponhamos que um usuário solicite a liberação de um desconto de 10,75%, porém seu liberador imediato está apto a liberar apenas 10%; serão apresentados para escolha, neste caso, outros usuários liberadores que atendam não só os 10%, mas também o percentual excedido, ou seja, 0,75%; na janela de solicitação de liberação será exibido o percentual ultrapassado.

#### **(1)** Comportamento do Evento 25 no faturamento com distribuição de desconto de rodapé (DISTDESCNFE)

Quando o parâmetro **DISTDESCNFE** está habilitado, o sistema redistribui automaticamente o desconto informado no rodapé da nota entre os itens no momento do faturamento da NF-e. Essa redistribuição é uma exigência da SEFAZ para que o desconto esteja corretamente representado em cada item da nota fiscal.

Nesse cenário, o evento 25 - Desconto por item da nota não é solicitado na nota de faturamento, mesmo que, após a redistribuição, o percentual de desconto de algum item ultrapasse o limite configurado no Cadastro de Produtos.

Isso ocorre porque o desconto redistribuído nos itens tem origem no desconto de rodapé, que já passou pelo processo de aprovação via evento 2 - Desconto Produto. O sistema reconhece que não se trata de um novo desconto concedido, mas sim da alocação fiscal de um valor que já foi devidamente autorizado.

Em notas geradas a partir dessa nota de faturamento — como uma nota de devolução/estorno ou de remessa emitida a partir do mesmo número de nota já faturado — o evento 25 volta a ser solicitado normalmente, caso o desconto por item ultrapasse o limite permitido. Essas notas herdam os itens já com o desconto redistribuído, mas não possuem vínculo com a aprovação realizada na nota de origem, portanto o sistema avalia o desconto de cada item de forma independente.

Esse comportamento só fica evidente quando o pedido chega a gerar mais de uma nota fiscal. Em vendas faturadas em uma única NF-e, a checagem do evento 25 sobre os valores redistribuídos do rodapé não chega a ser realizada.

Em resumo, para operações com o parâmetro DISTDESCNFE habilitado:

- Nota de faturamento (NF-e): o evento 25 não é solicitado para descontos originados da redistribuição do rodapé, pois esses valores já foram aprovados pelo evento 2.
- Notas geradas a partir da nota de faturamento (remessa, devolução/estorno): o evento 25 é solicitado normalmente quando o desconto por item ultrapassar o limite configurado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

---

####

### 26 - Limite de crédito pela Média Negociação

Para este evento é necessário a configuração dos seguintes parâmetros:

- Qtd de meses p/ validação da média de negociação - QTDMESMEDNEGOC.
- Percentual de aumento p/ média de negociação - PERAUMMEDNEGOC.

**Exemplo:** Este evento bloqueia a venda quando o valor de Compras do Parceiro em questão superou a média que o cliente compra em um determinado período de tempo, período este, informado no parâmetro **"QTDMESMEDNEGOC"** somado com o percentual preenchido no parâmetro **"PERAUMMEDNEGOC"**.

A validação da Média somente será feita pelos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) que tiverem a marcação **"Validar Média de Negociações Mensais"** presente na aba Validações, assinalada.

O objetivo desta validação é evitar que um cliente aumente as suas compras de uma maneira repentina, uma vez que isso pode comprometer a sua capacidade de pagamento.

A validação do Limite de Crédito pela média será acionada somente na confirmação de uma Nota/Pedido.

Os valores apurados pela Média, são de Pedidos Confirmados e Pendentes, Notas de Venda Confirmada e Notas de Devolução Confirmada.

**Observação:** a validação da Média consiste em considerar o valor total do mês corrente e verificar se este é maior que o valor total dos meses anteriores, que foi informado no parâmetro **"Qtd de meses p/ validação da média de negociação - QTDMESMEDNEGOC"**, dividido pela quantidade de meses com valores maiores que zero e acrescido do percentual de aumento informando no parâmetro **"Percentual de aumento p/ média de negociação - PERAUMMEDNEGOC"**.

Na [Ficha de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601934-Ficha-de-Parceiros), no painel **"Indicadores"**, as opções **"Limite de crédito total" e "Limite de crédito mensal"**, agrupam informações referentes aos parâmetros QTDMESMEDNEGOC e PERAUMMEDNEGOC, total do mês, total dos meses anteriores e quantidade de meses utilizados na média.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 27 – Fórmula Desc. Máx. Tipo Negoc. por item

A liberação deste evento será acionada no sistema da seguinte maneira:

Na inclusão de um item na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), caso o [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) utilizado na nota, tenha em seu cadastro o campo **"Fórmula desc. máximo itens"** preenchido, e o valor do desconto no item for superior ao desconto máximo obtido pela fórmula, é aberto o pop-up de solicitação de Liberação de Limites.

Depois de lançados itens que geraram o evento 27 – Fórmula Desc. Máx. Tipo Negoc. por item, se houver uma troca de TOP ou de Tipo de Negociação e a fórmula utilizada no novo Tipo de Negociação for diferente da anterior, a liberação será solicitada novamente.

**Importante:** para que o Evento 27 – Fórmula Desc. Máx. Tipo Negoc. por item seja chamado, é necessário que você configure o parâmetro **"Valida desconto máximo - VALDESCMAX"** com uma das seguintes opções: **"VALIDA E NÃO ACEITA"**, **"VALIDA E NÃO ACEITA (EXCETO PROD. PROMOÇÃO)"** ou **"VALIDA E NÃO ACEITA (SOMENTE NA CONFIRMAÇÃO)"**, bem como, o [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) esteja com o Desconto Máximo = 100%.

**Nota:** o sistema não possui uma configuração que faça com que o Evento - 27 – Fórmula Desc. Máx. Tipo Negoc. por item seja solicitado apenas na confirmação do documento quando o desconto for informado diretamente no item.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 28 – Limite de Bonificação por Projeto

A liberação deste evento será acionada no sistema da seguinte maneira:

Ao realizar vendas para Projeto com TOP de Bonificação, se o parâmetro **"Validar Limite de Bonificação pelo Projeto? - VALLIMPROJ"** estiver Ligado, o sistema acumulará os valores até atingir o limite definido no Projeto e, a partir disso, passará a solicitar a liberação para este evento. O sistema levará em conta os rateios nas notas para fazer a somatória dos valores a serem liberados.

A validação ocorrerá no momento da confirmação das notas. Qualquer modificação depois da nota confirmada não será validada, portanto, deve-se proibir alterações depois da nota confirmada pela TOP (campo Permitir Alteração após confirmar na aba Geral).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 29 - Desconto no Financeiro

Caso o usuário logado não tenha alçada para liberar o valor do desconto fornecido na tela de Baixa no Financeiro, é aberto o pop-up de solicitação de Liberação de Limites.

---

![Imagem 10: Observações sobre o uso do evento 29 - Desconto no financeiro :](https://ajuda.sankhya.com.br/hc/article_attachments/17084212891799) **Observações sobre o uso do evento 29 - Desconto no financeiro:**

- Este evento trabalha apenas com **"Tipo limite"** por **"Evento"** uma vez que não considera montante mensal.
- Ao habilitar o parâmetro **"Usa Vlr. liberado na baixa quando Vlr. desc. zero? - FORCEVLRLIBBX"** os descontos digitados na baixa do financeiro serão mantidos quando o usuário realizar a solicitação de liberação de limites de um evento 29 - Desconto no financeiro.
- Caso a exibição da Liberação de Limites tenha sido dispensada na tela [Cadastro de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913), é recomendado que seja inserido um valor substancial no campo **"Usuário Liberador"** do [Cadastro Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), como, por exemplo, **"9999999"**.
- Para a Liberação de Limites de descontos no Financeiro, o campo **"Observação"** presente no pop-up **"Ver mensagem em HTML"** da tela [Fila para envio de e-mail de Liberação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593554), será preenchido automaticamente com as informações descritas no campo **"Histórico"** da [Baixa de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos#top) na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).
- Lembre-se que a Liberação de Limites para o evento 29 - Desconto no Financeiro é aplicável somente para títulos classificados como Receita.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 30 - Perdão de Multa no Financeiro

Para este evento realize a seguinte configuração:

- Ligue o parâmetro **"Usa liberação na baixa c/valores pagos digitados - USALIBBXPAGDIG"**.

Esta liberação só é aplicável sobre títulos de Receita.

**Exemplo:** Este evento controla a concessão de abatimentos nos encargos que incidem sobre os títulos financeiros, de modo que, somente o Liberador possa liberar os parceiros do pagamento de multas no momento da baixa do título.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 31 - Perdão de Juros no Financeiro

Para este evento temos a seguinte configuração:

- O parâmetro **"Usa liberação na baixa c/valores pagos digitados - USALIBBXPAGDIG"** deve estar Ligado.

Esta liberação só é aplicável sobre títulos de Receita.

**Exemplo:** Este evento controla a concessão de abatimentos nos encargos que incidem sobre os títulos financeiros, de modo que somente o Liberador possa liberar os parceiros do pagamento de juros no momento da baixa do título.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 32 - Descontos Financeiros por Parceiro

O evento 32 será disparado nas baixas da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) caso uma personalização seja realizada na tabela TGFDFP da tela [Descontos Financeiros por Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606354-Descontos-Financeiros-por-Parceiro), e esta esteja preenchida.

Lembre-se que, o parâmetro **"USADESCFIN - Usar Desconto Financeiro por Parceiro?"** precisa estar habilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 33 - Antecipação de Orçamento | 34 - Suplementação de Orçamento | 35 - Transferência de Orçamento

Estes três eventos determinam o quanto cada Liberador poderá liberar em cada operação da rotina de Orçamento.

**Observação:** no Cadastro de [Centro de Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado) define-se o seu usuário responsável no campo **"Usuário Responsável"** e de acordo com o nível do CR e com os parâmetros configurados ele poderá Antecipar, Suplementar ou Transferir Recursos de Orçamento. Além disso, o Usuário Responsável que o sistema utilizará para as liberações, será aquele informado no nível analítico do Centro de Resultado para a definição do Liberador dos Eventos.

![Imagem 11: Os parâmetros "Nível p/Aprov.Antecipação de Orçamento - NIVAPROVANTECIP" , "Nível p/Aprov.Suplementação de Orçamento -…](https://ajuda.sankhya.com.br/hc/article_attachments/22512556654487) Os parâmetros **"Nível p/Aprov.Antecipação de Orçamento - NIVAPROVANTECIP"**, **"Nível p/Aprov.Suplementação de Orçamento - NIVAPROVSUPL"** e **"Nível p/Aprov.Transferência de Orçamento - NIVAPROVTRANSF"** devem estar configurados com um valor diferente de zero no campo **"Inteiro"**, para que as operações relacionadas a eles sejam efetivadas.

**Nota:** na liberação destes eventos, na confirmação da solicitação, o sistema envia um e-mail ao liberador informando sobre tal solicitação. Trabalhando no pop-up de **"Solicitação de liberação de Orçamento"** (lançamento de Pedido ou Nota de Compra), este e-mail também será enviado caso o campo **"Tipo"** seja definido como **"Indefinido"**; será enviado o e-mail se o Usuário Liberador possuir alçada para realizar a liberação do orçamento com qualquer um dos eventos.

![Imagem 12: Os eventos mencionados não incluem o envio de e-mail ao solicitante da liberação orçamentária.](https://ajuda.sankhya.com.br/hc/article_attachments/22512556654487) Os eventos mencionados não incluem o envio de e-mail ao solicitante da liberação orçamentária.

**Importante:** esses eventos serão acionados quando o valor da nota exceder o montante disponível nas metas que abrangem essa nota. O valor pode ser verificado utilizando a seguinte consulta:

```
select X.ORCADO,X.REALIZADO,(X.ORCADO - X.REALIZADO) saldo
from (
SELECT (COALESCE(M.PREVDESP, 0) + COALESCE(M.SUPLEMENTODESP, 0) + COALESCE(M.ANTECIPDESP, 0) + COALESCE(M.TRANSFDESP, 0) + COALESCE(M.TRANSFSALDODESP, 0) - COALESCE(M.REDUCAODESP, 0)) AS ORCADO,
(COALESCE(M.REALDESP, 0) + COALESCE(M.COMPROMISSODESP, 0)) AS REALIZADO
FROM TGMMET MET
WHERE MET.CODMETA = 32
AND MET.DTREF = '01/01/2022'
AND MET.CODEMP = 0
AND MET.CODGER = 0
AND MET.CODVEND = 0
AND MET.CODCENCUS = 0
AND MET.CODNAT = 0
AND MET.CODREG = 0
AND MET.CODPROJ in (20000605) --10001602,
AND MET.CODPARC = 0
AND MET.CODCID = 0
AND MET.CODUF = 0
AND MET.CODPAIS = 0
AND MET.CODTIPPARC = 0) X
```

Lembrando que, para uma melhor visualização é essencial manter o Realizado da meta atualizado. Desse modo, verifique as configurações necessárias através do artigo [Configuração da Estrutura de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos).

![Imagem 13: Os valores liberados nos eventos 33, 34 e 35 são destinados à Meta. Portanto, ao liberar um valor adicional, é crucial…](https://ajuda.sankhya.com.br/hc/article_attachments/22512556654487) Os valores liberados nos eventos 33, 34 e 35 são destinados à Meta. Portanto, ao liberar um valor adicional, é crucial observar que a nota precisa ser confirmada em seguida. Após a liberação, é possível que uma nova nota utilize esse valor, o que exigirá uma nova liberação ao confirmar a nota original, gerando um novo evento de liberação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 36 - EPI antes do Vencimento | 37 -EPI sem devolução

A liberação destes eventos será acionada no sistema da seguinte maneira:

Ao lançar uma requisição de EPI (Equipamento de Proteção Individual) que exija devolução, sem o lançamento desta devolução, ou tente-se lançar um EPI, sem que o outro esteja vencido, é aberto o pop-up de solicitação de Liberação de Limites.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 38 - Características de Análises de Laudo

Evento não implementado no Sankhya Om.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 39 - Quantidade de Parcelas na Renegociação

A liberação deste evento será acionada no sistema da seguinte maneira:

Tendo no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), na aba Parc. Máx. em Renegociação uma quantidade informada no campo "Quantidade de Parcelas", no momento da realização da Renegociação, se este valor for excedido, é aberto o pop-up de solicitação de Liberação de Limites.

**Observação:** a configuração deste evento não é obrigatória. Se for cadastrada a Quantidade Parcelas igual a "0" (zero), o sistema também fará a validação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 40 - Solicitação de Compra p/produto em Estoque

Para este evento, realize as seguintes configurações:

- Cadastre um [Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) liberador do Evento 40.
- No cadastro de [Grupo de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os), efetue a marcação **"Participa da opção "Gerar solicitação de compra na confirmação?" do cadastro da TOP?"** localizada na aba Estoque.
- No cadastro de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), a marcação **"Solicita compra"** localizada na aba Geral deve estar realizada.

No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), a marcação **"Gera Solicitação de Compra na Confirmação"** presente na aba Validações deve estar efetuada.

**Exemplo:** Na confirmação da Nota, quando a TOP estiver além da marcação mencionada acima, com a opção **"Faturar Produtos com Estoque na Confirmação"** desmarcada (aba Validações), para cada produto com estoque maior que a quantidade Negociada (caso em que não seria gerada solicitação de compra), o sistema solicitará liberação, colocando na tela de **"Solicitação de Liberação de Limites"** a quantidade negociada no valor solicitado e o limite igual à zero.

**Nota:** toda vez que o estoque for maior que zero, o sistema deverá solicitar a liberação, e quando for menor que zero, ele não solicitará a liberação, e já irá gerar a solicitação de compra.

**Observação:** quando o parâmetro **"Ignorar validação do evento 40 - IGNORAEVENTO40"**estiver habilitado, a solicitação de liberação do evento 40 não ocorrerá.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 41 - Confirmação de Nota com análise dos itens

Este evento impede que as pessoas que utilizem o sistema confirmem Requisições ou Transferências ([Central de Movimentações Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas)) sem que o gerente avalie os produtos solicitados. O Liberador terá a opção de alterar estes produtos, ajustando suas quantidades ou até mudar o produto.

**Observação:** a confirmação de nota com análise dos itens está ligada diretamente à marcação **"Exigir liberação com análise dos itens antes da confirmação"** das TOP's de Pedido de Compra, Pedido de Requisição, Requisição, Devolução de Requisição e Transferência, que não Atualiza Financeiro, Calcula Impostos, Atualiza Custos, Estoque e Bens. Nesse sentido, a nota já liberada para esse evento não poderá ser alterada, mesmo que o acesso **"Altera registros confirmados"** no [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) esteja liberado. Caso tente alterar ou excluir, o sistema emitirá a mensagem:

**"Pedido/Nota com Liberação por Análise dos Itens não pode ser Alterada ou Excluída".**

**Importante:** ainda sobre o evento 41 - Confirmação de Nota com análise dos itens, caso seja necessário realizar a análise de documentos de Tipos de Movimento diferentes dos informados acima, pedidos de compra por exemplo, mesmo tendo um Usuário Liberador para este evento, não é possível alterar tal documento depois da liberação. Nestas situações, sendo necessário, proceda com a alteração dos itens e quantidades nas Centrais antes da liberação de limites.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 42 - Limite de Crédito por Grupo de Tip. Título

A liberação deste evento será acionada no sistema da seguinte maneira:

Quando é feito o lançamento de um Pedido ou Nota que ultrapasse o valor limite informado na aba Limite de Crédito p/ Grupo Tip.Titulo no campo **"Limite de Crédito"** do cadastro de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042432254-Parceiros), é aberto o pop-up de solicitação de Liberação de Limites.

Ao lançar um título pela tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) que tenha um [Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), marcado como Terceiros, se esse ultrapassar o limite de crédito o sistema não permitirá salvá-lo e emitirá a mensagem:

**"Grupo: Terceiros Lim.: xxx Total: xxx"**

**Nota:** para títulos já lançados, a revalidação deste limite de crédito irá ocorrer somente se os campos que influenciam no Tipo de Título e/ou no Valor do Desdobramento destes estiverem sendo editados, sendo que esta edição poderá ser feita na Movimentação Financeira ou por meio da opção [Parcelar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#parcelar).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 44 - Liberação exigida pela TOP

A configuração deste evento é realizada em concordância com a marcação **"Sempre exigir Liberação"** disponível no cadastro [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba Validações; uma vez esta marcação efetuada, no lançamento de uma movimentação utilizando esta TOP, será necessário que o Usuário Liberador para este evento, o faça.

Sendo solicitada a liberação do evento 44 - Liberação Exigida pela TOP e procedendo com essa liberação, temos prontamente a confirmação do pedido. Mesmo que sejam feitas alterações neste pedido já confirmado, uma vez sua liberação já efetuada, esta não será solicitada e/ou realizada novamente.

![Imagem 14: Este evento somente será disparado uma única vez ao confirmar o documento.](https://ajuda.sankhya.com.br/hc/article_attachments/26489853980951) Este evento somente será disparado uma única vez ao confirmar o documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 45 - Liberação para Laudo de matéria prima

A liberação deste evento é solicitada ao confirmar um documento de saída (P - Pedido de Venda ou V - Venda) cujo Tipo de Operação - TOP esteja com a marcação **"Exigir Laudo de Análise"** presente na aba Validações realizada e o último laudo não esteja aprovado (aprovado ou aprovado com ressalva) para um dos itens. Por meio desse evento, pode-se liberar a confirmação do documento sem a existência do laudo.

**Nota:** o Evento de Liberação 45, nos processos de Compras, necessita que o parâmetro **"Permite que notas de compra exijam lauto? - PERCOMPRAEXILAU"** encontre-se habilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 48 - Margem de Contribuição Mínima

A liberação deste evento será acionada no sistema da seguinte maneira:

O campo **"% MC Mínima"** presente na aba Características do cadastro de [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), indica o percentual mínimo permitido de margem de contribuição que a negociação deve contemplar.

Este evento é solicitado na confirmação de um pedido ou nota quando a negociação não atender ao percentual mínimo configurado no Tipo de Negociação utilizado.

Na confirmação da nota/pedido, para que ocorra o cálculo da comissão é necessário configurar no [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), o campo **"Comissão"** com a opção **"Calc. Vend. da Nota na Confirmação"**.

**Observação:** a liberação de limites 48 - Margem de Contribuição Mínima funciona de maneira inversa, ou seja, uma vez que o valor X é liberado, qualquer valor igual ou superior não acionará um novo pedido de solicitação. Para solicitar a liberação de limites novamente, é necessário reduzir o valor unitário do item em relação ao valor liberado anteriormente.

**Importante:** para que seja realizado o cálculo de comissão antes da execução da solicitação de liberação referente ao evento 48 - Margem de Contribuição Mínima, temos as seguintes configurações:

- O parâmetro **"Antecipa calc.comissão na margem mínima? - CALCCOMMARGMIN"** deve estar ativado;
- O parâmetro **"Atualizar comissão por item? - ATUALCOMITE"** deve estar desligado.

A premissa para que o cálculo de comissão seja antecipado, é a utilização do cálculo de comissão pelo cabeçalho da nota; se for utilizada a comissão no item, a antecipação não será realizada mesmo com o parâmetro CALCCOMMARGMIN ligado.

Exemplo:  Utilizando este Tipo de Negociação em uma Venda, se o valor da nota for abaixo do estipulado, será solicitada a liberação de limites para este evento.

O conceito de liberação para os eventos 13 - Valor Mínimo Tipo Negociação, 19 - Lucro Mínimo e 48 - Margem de Contribuição Mínima difere do conceito de liberação dos demais eventos, pois envolve valores mínimos.

Nos outros eventos, o percentual cadastrado para o liberador deve ser maior do que o solicitado, já que o gatilho de solicitação do evento é o teto. Em contraste, para os eventos mencionados, o percentual cadastrado deve ser menor do que o solicitado, pois o gatilho é o piso.

Exemplo:

- **Evento 25 - Desconto por Item da Nota:**
  O máximo de desconto permitido em um produto é 20%; caso contrário, é necessária a solicitação de liberação. O liberador deve ter cadastrado o maior percentual que pode liberar, por exemplo, 30%. Qualquer desconto superior a 30% não será autorizado.
- **Evento 19 - Lucro Mínimo:**
  O mínimo de lucro em uma venda deve ser de 10%; caso contrário, é necessária a solicitação de liberação. O liberador deve ter cadastrado o menor percentual que pode liberar, por exemplo, 5%. Qualquer lucro inferior a 5% não será autorizado.

**Observação:** este evento será solicitado apenas após a liberação de todos os demais eventos que compõem a nota, pois os impostos só podem ser calculados quando não houver mais liberações pendentes. Além disso, o cálculo dos impostos afeta diretamente o cálculo da margem de contribuição.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 55 - Liberação de grupo de autorização

Este evento é de uso exclusivo de um Parceiro Sankhya e esta disponível apenas para a linha gráfica do MGE. Deste modo, se encontra indisponível no Sankhya OM.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 56 - Variação percentual no custo pedido/nota

Este evento é exclusivo do MGE e não é utilizado no Sankhya Om. Caso necessite de validação de variação percentual no custo pedido/nota poderá criar uma [regra de negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 58 - Variação na quantidade Pedido/Nota

Este evento é exclusivo do MGE e não é utilizado no Sankhya Om. Caso necessite de validação de variação na quantidade do pedido/nota poderá criar uma [regra de negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 61 - Liberação de data de validade menor que o previsto

Ao realizar o lançamento de uma ou mais notas que possuírem produtos controlados por Data de Validade e esta for menor que a data atual somada à quantidade dos dias definidos no parâmetro **"Mínimo de dias p/validade dos produtos na entrada - MINDIASVALENT"**, o sistema irá solicitar a liberação do [evento 61](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#61-Libera%C3%A7%C3%A3odedatadevalidademenorqueoprevistro) na confirmação da nota, além de exibir a seguinte mensagem:

**"Data de validade [xx/xx/xxxx] não atende a validade mínima [xx/xx/xxxx] estabelecida no parâmetro MINDIASVALENT. Será colicitado liberação na confirmação da nota."**

É importante também que o parâmetro **"Usar data de validade junto com Lote? - LOTEDTVAL"** esteja ligado, pois assim, o sistema realizará a validação da Data de Validade dos produtos da nota.

**Observação:** o evento 61 será funcional quando utilizado em HTML5.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 63 - Liberação Financeiro

O evento Liberação Financeiro será utilizado para a aplicação de normas na tela [Regras de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio), quando os lançamentos forem inseridos corretamente e atenderem aos requisitos de uma Regra de Negócio.

Porém, o evento em questão só poderá ser utilizado em operações na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas). Assim, essa regra, a utilizar uma expressão Stored Procedure, poderá ser aplicada durante:

- Uma Confirmação de Venda;
- Inclusão / Alteração de Itens;
- Inclusão / Alteração de Cabeçalho.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 64 - Corte/divergência de pedido (Conferência)

A liberação deste evento será acionada no sistema da seguinte maneira:

O Usuário Liberador que possuir este evento para ele configurado, estará apto a realizar a liberação dos pedidos vindos da [Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#conferncia), onde foram efetuados cortes com divergências.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 66 - Desconto do item abaixo do calculado

Este evento ocorre quando as seguintes configurações são realizadas:

1. Defina o parâmetro **"Valida desconto máximo - VALDESCMAX"** com a opção **"VALIDA e NAO ACEITA"** ou **"VALIDA E NAO ACEITA (EXCETO PROD. PROMOCAO)"**
2. Ligue o parâmetro **"Usar o maior desconto promocional? - USAMAIDESCPROMO"**;
3. Associe um [Desconto Promocional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034) ativo ao produto.

Dessa forma, ao lançar o item na nota e alterar o campo **"% de desconto"** para um valor menor, por exemplo, se o desconto promocional for de R$ 8,00 e for aplicado um desconto menor, como R$ 7,00, diretamente no item, ao salvar o registro, o sistema solicitará a liberação do evento **"66 - Desconto do item abaixo do calculado"**.

#### **(1)** Memória de cálculo

Quando habilitado, o parâmetro **GERMEMCLAEVELIB** faz com que o sistema registre a memória de cálculo dos eventos de liberação 2, 3, 25 e 66, detalhando os critérios que originaram a solicitação de liberação, como percentual de desconto aplicado, valor total do item e limite permitido.

Essas informações ficam disponíveis ao liberador durante a análise da solicitação, permitindo identificar o motivo da liberação sem a necessidade de consultar o pedido manualmente.

[GIF animado: Imagem 15: Essas informações ficam disponíveis ao liberador durante a análise da solicitação, permitindo identificar o motivo da…](https://ajuda.sankhya.com.br/hc/article_attachments/31003495426583)

A memória de cálculo detalha as seguintes informações:

- **preço de tabela**: preço original do produto definido no cadastro;
- **valor do desconto**: diferença entre o preço de tabela e o preço de venda;
- **desconto máximo permitido**: valor máximo de desconto configurado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 67 - Excede Estoque Máximo

Este evento será utilizado para operações de Compra, e conterá as opções por **"Valor"** ou **"Percentual"**. Se a [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizada no pedido/nota de compra possuir em sua aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque) a opção **"Valida Estoque Máximo"** acionada, caso a quantidade a ser comprada faça com que o estoque ultrapasse o estoque máximo configurado, o sistema bloqueará a confirmação. Será considerado o seguinte cálculo para bloquear a confirmação do pedido/nota:

**Estoque Atual - Estoque Reservado + Pedido ou Compra Pendente + Pedido ou Compra Atual.**

Se essa soma for maior que o Estoque Máximo, ocorrerá o pedido de liberação do deste evento, caso contrário, o sistema confirmará a nota.

Para validação do estoque máximo, o sistema deverá buscar pelo estoque máximo da tabela de estoque (TGFEST), conforme Empresa Local e Controle do item, caso não exista estoque máximo na TGFEST, o sistema buscará o estoque máximo da tabela de produtos (TGFPRO).

**Nota:** Para o cálculo do evento 67, o sistema leva em consideração sempre os seguintes parâmetros: **Empresa, Local e Controle**. Portanto, este evento não deve ser utilizado quando se trabalha com **explosão de lote**, pois, com essa configuração, ocorrerá o lançamento sem o controle (antes da explosão), o que resultará em uma **validação incorreta do evento**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 68 - Variação do vlr. unit. orig./dest.

Esta validação será solicitada ao Liberador, quando na confirmação de um item em uma nota de venda, existir diferença entre seu valor unitário, e o valor unitário de seu pedido de origem; o mesmo vale na confirmação de um item em uma nota de devolução de venda, em relação a sua nota de venda de origem. Esta mesma validação também é realizada nas operações envolvendo pedidos, notas e devoluções de compra.

O parâmetro **"Campo p/ validação valor unit. evento 68? - CAMVLRUNITEVT68"** é o responsável pela validação do evento em questão, ou seja, informe no referido parâmetro o campocorrespondente ao valor unitário que será considerado.

Sendo que, na confirmação de um item em uma nota de devolução de venda, em relação a sua nota de venda de origem, este parâmetro permite que a validação seja realizada entre o valor unitário de seu pedido de origem com o valor unitário líquido de seu documento de destino. Para tanto, é necessário configurar o parâmetro informando no mesmo os campos calculados na tabela **"TGFITE"** pertinentes aos referidos valores, como por exemplo os campos **"VLRUNIT"** e **"VLRUNITLIQ"** sempre separados por ";".

**Observação:** será possível gerar uma nota de remessa ao faturar um Pedido de Venda quando o evento 68 - Variação do vlr. unit. orig./dest. for disparado e a liberação for realizada pela rotina de Liberação de Limites, tendo o mesmo comportamento da Central de Vendas.

Ainda, além do preenchimento do parâmetro CAMVLRUNITEVT68, é necessário habilitar a marcação **"Validar variações do vlr. unit. orig./dest."** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), seção [Conf. do evento 68 (Variação do valor unitário entre origem e destino)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) do [cadastro da TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de destino.

Lembre-se que, caso o usuário logado seja um usuário Liberador do evento 68 e seu limite de liberação seja maior que zero e maior que o valor a ser liberado na nota, então não será solicitada a liberação do limite.

### 70 - Acréscimo do valor unitário ref. ao último custo

A funcionalidade deste evento não está disponível para o Sankhya Om. Este evento está disponível apenas nas linhas MGE/Mitra.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 74 - Venda mínima por Parceiro/Cidade/Região

A solicitação de liberação para este evento está condicionada à configuração de Venda Mínima presente nos cadastros de [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), [Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) e [Região](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074-Regi%C3%B5es). O sistema obedece a seguinte ordem de precedência:

- Se no cadastro de Parceiros possuir informação no campo Venda Mínima ([aba Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abainformaes)), será feita validação pelo parceiro;
- Em seguida, o sistema verifica se a cidade possui o campo Venda Mínima informado ([aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abageral)), caso afirmativo, este valor será utilizado;
- Por fim, será verificado se a Região possui Venda Mínima ([Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074-Regi%C3%B5es#painelprincipal)) e, caso possua, este valor será considerado.

Com base nestas configurações, será feita a comparação do valor total da nota - bonificação, com o valor de Venda Mínima configurado nos cadastros mencionados acima, de modo que, se estes forem ultrapassados, será solicitada a liberação para o evento 74. Além disso, por meio dos parâmetros **"Validar venda mínima pela cidade de entrega? - VENDAMINCIDENT"** e **"Validar venda mínima pela região do parceiro? - VENDAMINREGPAR"**, determine qual a cidade e região serão consideradas para validação, respectivamente.

Trabalhando com este evento, será possível decidir pela viabilidade da venda de acordo com os valores da nota, comparando-os com os valores cobrados para frete de entrega, para aquela determinada região.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 75 - Diferença entre NCM, CEST ou Origem

Este evento está relacionado à rotina [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), onde o Liberador deste evento estará apto à conceder as permissões de continuidade na importação quando o **"NCM"**, **"CEST"** ou **"Origem"** dos produtos divergirem.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 76 - Diferença de impostos

Assim como o evento 75 - Diferença entre NCM, CEST ou Origem, o evendo 76 - Diferença de impostos também é ligado à rotina [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML); sua diferença é que, por este evento são tratadas pelo Liberador, as divergências de impostos nos produtos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 77 - Análise de crédito expirada

Este evento poderá ser utilizado caso a empresa possua o opcional **30720 - CONSULTA SERASA /W**. É um evento participante da [Integração Consulta Serasa Experian](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110113-Integra%C3%A7%C3%A3o-Consulta-SERASA-EXPERIAN), e a solicitação de liberação para ele irá ocorrer nas seguintes situações:

- **1º caso:** Ao proceder com uma venda, pode ser que a Data da consulta realizada em outro momento para o parceiro junto ao Serasa, tenha expirado (Data de Expiração menor que a Data de Negociação), sendo necessário que um Usuário Liberador autorize a continuidade da nova negociação, por meio da liberação de limites. Esta solicitação de liberação irá acontecer na tentativa de Confirmação da nota de venda;
- **2º caso:** Na realização de uma venda, pode ser que para o Parceiro em questão, não tenha-se efetuado nenhuma consulta junto ao Serasa; para seguimento na venda para um Parceiro nesta situação, também será necessário que um Usuário Liberador permita a operação através da liberação do evento 77 - Análise de crédito expirada. Assim como a situação anterior, a solicitação de liberação irá ocorrer quando na Confirmação da nota de venda.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 78 - Liberação de agrupamento mínimo

Para este evento, realize as seguintes configurações:

- No cadastro de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba Medidas e estoque, o campo **"Agrupamento mínimo"** deve estar configurado.
- No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba Validações, o campo **"Valida agrupamento mínimo"** deve estar configurado com a opção **"Valida e exige liberação"**.

**Exemplo:** Na confirmação da Nota, caso haja algum item negociado com a quantidade que não respeite o agrupamento mínimo, o sistema solicitará liberação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 79 - Fechamento Fiscal Contábil

O evento 79 - Fechamento Fiscal Contábil, será solicitado quando houverem alterações em períodos contábeis fechados.

Então, o usuário liberador poderá consultar os detalhes dessa e outras solicitações e decidir se irá ou não liberar na tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites). Além disso, o status dessa liberação poderá ser consultado na tela [Configuração de Bloqueio Contábil/Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595654-Configura%C3%A7%C3%A3o-Fechamento-Cont%C3%A1bil-Fiscal).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 81 - Desvio na quantidade apontada de PA

Este evento será solicitado quando a quantidade de produto apontada (Qtd apontada + Qtd perda) na atividade que esta sendo finalizada é diferente da quantidade de produtos que entrou no repositório de operação da mesma.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 82 - Pendências Financeiras Maiores que o Estoque Disponível

O referido evento será solicitado quando, na tela [Contratos de Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armazenagem), a marcação **"Valida pendência financeira x estoque disponível"** da aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armazenagem#abapropriedades) for habilitada e assim, o sistema realizará uma validação quando uma Nota de Saída for gerada para verificar se o valor do estoque disponível residual do produtor será suficiente para cobrir uma eventual inadimplência; para isso, o sistema irá considerar as apurações faturadas e pendentes na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/search?utf8=%E2%9C%93&query=Movimenta%C3%A7%C3%A3o+Financeira) e as apurações a faturar, sendo elas em aberto e parciais.

Dessa forma, quando for identificado que o saldo disponível não será suficiente para cobrir as pendências financeiras do contrato, o evento será gerado para que um usuário com alçada proporcional ao valor avalie se é viável ou não a liberação da saída.

Logo, para a realização do evento, considere os seguintes pontos:

- Quando o parâmetro **"Incluir serviços apurados na validação de pendências financeiras x estoque disponível - VALSAPFINESTDIP"** for desabilitado, o evento será lançado quando o Valor da Movimentação Financeira em aberto for menor que o Valor do Saldo Disponível;
- Porém, quando o parâmetro for ligado e o Valor da Movimentação Financeira somado ao Valor dos serviços apurados for menor que o Valor do saldo disponível, teremos:

```
    Vlr. Salo Disponível = (Saldo do contrato / Unidade Conversão por SC) * (Últ. Vlr. de
     Cotação da Moeda)
```

```
    Vlr. Movimentação em aberto = Valor em aberto (Vencidos e a Vencer) vinculado ao
     contrato na Mov. Financeira
```

```
    Vlr. Serviços apurados = Valores Líquidos de Expeedição/Recepção + Armazenagem
     apurados com status em aberto ou parcial
```

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 83 - Liberação de Laudo de Classificação p/ Armazenagem

O referido evento, será utilizado para aprovação do laudo por usuários específicos conforme os critérios definidos no [Cadastro das Características Analisáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600194-Caracter%C3%ADsticas-Analis%C3%A1veis) em que, as faixas de classificação serão selecionadas na tela [Padrões de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o) para a solicitação das liberações.

Dessa forma, é necessário habilitar a marcação **"Exibe Liberação"** da sub-aba **"Intervalo"** da tela Padrões de Classificação, assim, o Padrão de Classificação cadastrado será associado aos Laudos de Classificação.

O Laudo de Classificação é realizado para definir o tipo de padrão de classificação, e este, por sua vez, é vinculado ao contrato para determinar o tipo de produto a ser recebido no armazém, o que será utilizado como indicativo nos descontos e validações. Você pode realizar essa classificação na tela Laudo de Classificação ou na tela [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054-Pesagem), por meio do botão **"Laudo"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### 84 - Liberação para Destinação de Verba

```
 Esse evento está disponível apenas para a versão 4.18 e superiores.
```

O evento 84 será solicitado caso o valor a destinar de uma verba supere o valor limite definido no parâmetro **"Valor Limite Exigir Liberação Destinação Verba - VLEXIGLIBDESVBA"**. Ou seja, se o valor do parâmetro for zero ou vazio, não será solicitada a liberação de limites, porém caso esteja com um valor definido maior do que zero, será exigida uma liberação se o valor for ultrapassado antes de destinar uma verba, sendo que essa liberação deverá ser feita por um usuário que tenha alçada para esse evento.

**Observação:** o valor a ser considerado na validação é referente ao valor total da destinação e não de apenas uma única verba.

Sendo assim, após ser feita a solicitação de liberação, ao acessar a tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites) e clicar no botão ![Imagem 16: Sendo assim, após ser feita a solicitação de liberação, ao acessar a tela Liberação de Limites e clicar no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16808338715415) **"Detalhes"**, será aberta a tela [Destinação de Verbas](https://ajuda.sankhya.com.br/hc/pt-br/articles/10436515554839-Destina%C3%A7%C3%A3o-de-Verbas) já posicionada na respectiva destinação. Após isso, acessando o evento 84, serão apresentados os dados de valores, solicitante, código de destinação e o tipo de destinação informado no campo de observação.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)

### Informações adicionais acerca dos eventos

Caso realize qualquer alteração de cabeçalho ou dos itens, o sistema emitirá um alerta com a seguinte mensagem:

**“Este documento já foi confirmado, portanto, as liberações de limites pendentes só serão impeditivas em caso de faturamento."**

Esta mensagem somente será disparada quando o evento possuir o Valor atual maior que o Valor Liberado, com exceção dos eventos 18 e 44.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#top)
