---
id: "360044597894"
titulo: "Cálculo de Custos sem Fórmula de Precificação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597894-C%C3%A1lculo-de-Custos-sem-F%C3%B3rmula-de-Precifica%C3%A7%C3%A3o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:53Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Custos", "Configuração", "Fórmulas", "Cálculo de Custos sem Fórmula de Precificação", "Cálculo de Custos sem Fórmula de Precificação manual", "Impostos", "Financeiro", "Cálculo de Custos Automático", "Precificação Automática"]
---

# Cálculo de Custos sem Fórmula de Precificação

Quando o produto não possui fórmulas de custo/preço, o sistema utiliza a fórmula interna para calcular os custos e preços do produto. Desta forma, temos as seguintes expressões:

**Custo sem ICMS:** Se refere ao valor unitário do produto considerando despesas de rodapé da nota fiscal, ou seja:

```
CusSemCal = Round2((VlrPro * IndTot) - (VlrICM * IndICMS)QtdCasasDecimaisCusto);
```

**Custo com ICMS:** Representa o valor unitário do produto considerando despesas de rodapé, isto é:

```
 CusComCal = Round2((VlrPro * IndTot), QtdCasasDecimaisCusto);
```

**Custo Variável:** São custos que dependem diretamente do volume de produtos produzidos. Quanto maior a quantidade fabricada, maior seu consumo não é calculado, ou seja:

```
CusVarCal=0;
```

**Custo de Reposição:** Se refere ao valor do item na nota:

```
 CusRepCal = VlrUnit;
```

**Custo Gerencial:** É calculado segundo a fórmula:

```
CusGerCal = Round2(CusSemCal - (VlrUnit * TaxaJuro * intPrazoMedio /3000)
QtdCasasDecimaisCusto),
```

Em que:

- **Taxa de Juro:** é um parâmetro que calcula a taxa de juro mensal;
- **IntPrazoMedio:** é calculado a partir das datas informadas no financeiro da nota.

**Observação:** divisão por 3000 significa: (/30 (dias do mês comercial) \* 100).

**Preço:** O preço de tabela será calculado da seguinte maneira:

Sendo realizado o cálculo do Preço de Venda através da rotina **"Recálculo do Preço de Tabela pela Fórmula de Precificação"**, o preço será o resultado da seguinte expressão:

```
Preço = round2(CusGerCal / (1- (MARGLUCRO / 100)), QtdCasasDecimaisVLR);
```

**Custo médio com ICMS:** Representa o valor calculado com base no custo com ICMS, utilizando o seguinte algoritmo:

```
((ACusComCal * EA) + (NCusComCal* QC)) / (EA + QC),
```

Sendo que:

- **AcusComCal:** é o Custo Médio com ICMS Anterior;
- **EA:** corresponde ao Estoque Anterior;
- **NCusComCal:** é o Novo Custo Médio com ICMS;
- **QC:** expressa a Quantidade Comprada (Entrada).

**Custo médio sem ICMS:** Consiste no valor calculado sem base no custo sem ICMS, utilizando o seguinte algoritmo:

```
 ((ACusSemCal * EA) + (NCusSemCal * QC)) / (EA + QC);
```

**Custo Médio Gerencial:** Se refere ao valor calculado com base no custo gerencial, utilizando o seguinte algoritmo:

```
((ACusGerCal * EA) + (NCusGerCal* QC)) / (EA + QC).
```

**Atualização de Custo:** Para que o custo seja atualizado no item da tabela TGFCUSITE, é necessário preencher o campo **"Custo de Reposição"** da tela [Atualização de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594174).

**Observação:** caso seja inserida alguma expressão na fórmula padrão, o sistema irá utilizá-la.

## Observações para configuração

Para que os custos sejam atualizados de forma correta, é necessário que você verifique os seguintes pontos:

- A configuração do campo **"Precifica"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), para os [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de Compra;

**Nota:** para efetuar o cálculo dos custos médios é necessário ter uma linha histórica da TOP (TGFTOP) que precificou, com data igual ou anterior a data de entrada e/ou saída da nota.

- Os parâmetros na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834);
- Se os campos **"Fórmula de Custo/Preço"** e **"% Margem de Lucro"**, aba [Formação de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaformaodecustopreo), da tela [Cadastro de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), estão devidamente preenchidos;
- Se a expressão matemática está correta no Cadastro de Fórmulas de Precificação.

**Nota:** caso uma fórmula sem custo seja utilizada em operações de Devolução de Venda e Requisição, será utilizado o custo que estava em vigor na data em que os lançamentos foram realizados.

Abaixo, temos algumas dicas:

**1.** Se na compra o produto for adquirido para produção (matéria-prima) utilizando a CFO do item = 111/211 (antigas) ou 1101/2101 = Compra para Industrialização dentro ou fora do estado, então VlrPro (Valor do Produto) = VlrUnit (Valor Unitário) senão VlrPro = VlrUnit + (VLRIPI / QtdNeg). O IPI é desprezado nas compras para industrialização, pois normalmente o mesmo também é abatido do custo sob a forma de crédito tributário;

**2.** Para o valor do produto determinado no item anterior, será somado o valor unitário de substituição e deduzido o valor unitário do desconto oferecido para o item, ou seja:

```
VlrPro = Round2(VlrPro + (VLRSUBST / QtdNeg) - (VLRDESC / QtdNeg) QtdCasasDecimaisCusto).
```

Onde:

**QtdCasasDecimaisCusto:** se refere a quantidade de casas decimais para o cálculo do custo. A quantidade de casas decimais para custo é configurado através do parâmetro **"Decimais para custo - CUSTODEC"**;

**3.** Se o produto for de Revenda com Substituição Tributária ele não terá ICMS. Se não, o Valor unitário do ICMS é o Valor total do ICMS do item dividido pela Quantidade Negociada, ou seja:

```
RevendaCSubst então VlrICM = 0; senão VlrICM = (VLRICMS / QtdNeg);
```

**4. "IndTot"** é um índice que determina a participação de despesas acessórias e despesas do rodapé da nota contra o total de mercadorias negociadas, ou seja:

```
(IndTot = curTotal / TotalItens);
```

onde TotalItens é o valor total dos produtos;

Você também pode utilizar as expressões IndTot conforme as seguintes condições:

```
curTotal := TGFCAB.VlrNota ;

Se TGFCAB.ISSRETIDO <> 'S' Então

curTotal := curTotal - TGFCAB.VLRISS ;

Se TGFCAB.TIPIPIEMB <> 'I' Então

curTotal := curTotal + TGFCAB.IPIEMB + TGFCAB.VLREMB ;

Se (TGFCAB.TIPFRETE <> 'S') Então

curTotal := curTotal + TGFCAB.VLRFRETE ;
```

Assim, realize a troca dos campos pelos valores correspondentes conforme a necessidade de suas operações.

**5. "curTotal"** é o valor total da nota, considerando o:

```
Valor Total dos produtos + Valor de Frete (se houver) + Valor de Embalagem e IPI da
Embalagem (se houver) - Valor do ISS (se ISS não for retido);
```

**6. "IndICMS"** é um índice que determina a participação do ICMS cobrado sobre as despesas acessórias e despesas do rodapé da nota contra o valor do ICMS de mercadorias negociadas, ou seja:

```
IndICMS = ICMSTotal / (Valor ICMS total da nota);
```

**7. "ICMSTotal"** se refere ao:

```
Valor ICMS total da nota + (ICMS sobre frete + ICMS sobre seguro + ICMS de embalagem)
(se houver).
```
