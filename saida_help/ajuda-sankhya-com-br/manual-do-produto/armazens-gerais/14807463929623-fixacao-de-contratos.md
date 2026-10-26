---
id: "14807463929623"
titulo: "Fixação de Contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos"
trilha: "Manual do Produto > Suprimentos e Estoque > Armazéns Gerais"
atualizado_em: "2026-07-29T15:06:07Z"
rotulos: ["Configuração", "WMS", "Contrato", "Impostos", "TOP", "Financeiro", "ID: br.com.sankhya.armazem.fixacaoContrato.xml", "fixação contratos valores"]
---

# Fixação de Contratos

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42313169217047) Módulo: Armazéns Gerais > Rotinas          ![Versão](https://ajuda.sankhya.com.br/hc/article_attachments/42313169221527)Versão disponível: A partir da 4.21
```

---

![essencial](https://ajuda.sankhya.com.br/hc/article_attachments/16027937064855) Para utilização desta tela é necessário possuir à licença do opcional **"30935 - Comercialização de Grãos/W"**.

Esta tela é destinada à conferência e cálculo dos valores a fixar dos contratos para que se possa gerar as fixações, compensações e documentos complementares à operação.

| Funcionalidades da tela | |
| --- | --- |
| [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos#PaineldeFiltros) | [Notas a Fixar](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos#NotasaFixar) |
| [Receitas a Compensar](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos#ReceitasaCompensar) | [Totalizadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos#Totalizadores) |

### Painel de Filtros

Informe o **"Contrato"** de comercialização do tipo **"Compra a Fixar"** (configuração realizada na tela [Contratos de Armazéns de Grãos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os), aba [Comercialização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armazenagem#abaComercializacao), campo **"Tipo de Contrato"**) e clique no botão **"Aplicar"** para que os campos do painel **"Parâmetros da Fixação"** sejam habilitados.

Nesse momento, a **"Data"** da fixação será preenchida automaticamente.

O campo **"Qtde. a Fixar"** irá exibir a quantidade a fixar disponível para o respectivo contrato, conforme somatório da coluna Qtde. a Fixar das linhas exibidas na grade [Notas a Fixar](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623#NotasaFixar).

Preencha a **"Qtde. p/ Fixação"** e no campo **"Valor da Cotação"**, informe o Valor Unitário/Kg a ser considerado na fixação.

Preencha também no campo **"Valor do Abono"** o Valor Unitário/Kg do abono que será considerado na fixação.

Caso tenha alguma informação adicional, insira no campo **"Observação"**.

Ao acionar o botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/16028324229783) **"Preferências"** será aberto o pop-up de mesmo nome com as seguintes abas:

![Imagem 5: Ao acionar o botão "Preferências" será aberto o pop-up de mesmo nome com as seguintes abas:](https://ajuda.sankhya.com.br/hc/article_attachments/14809208322327)

#### Aba TOPs

Informe nesta aba as TOPs desejadas para a fixação, sendo elas:

- Top p/ Fixação;
- Top p/ Complemento de Valor;
- TOP p/ Devolução de Valor;
- TOP p/ Baixa de Receita;
- TOP p/ Baixa de Despesa.

#### Aba Filtros p/ Receitas

Nesta aba, devem ser indicados a **"Natureza"**, o **"Tipo de Título"** e o **"Centro de Resultado"**.

O botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/16028349658007) **"Simular Funrural"** irá simular o cálculo do Funrural a ser considerado na fixação, caso seja devido. Para que este cálculo seja efetuado corretamente, é necessário que no mínimo, a Qtde. p/ Fixação e Valor da Cotação sejam informados. Uma vez calculado, o valor será exibido no campo **"Vlr. Funrural"** do [Totalizador](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623#Totalizadores) da tela. Porém, se qualquer alteração for realizada nos campos Qtde. p/ Fixação, Valor da Cotação e/ou Valor do Abono, o totalizador Vlr. Funrural será zerado, sendo necessário realizar o seu cálculo novamente.

**Observação:** o valor do referido imposto será calculado quando as seguintes marcações estiverem habilitadas:

- **"Calcula FUNRURAL/INSS"** da aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal) do cadastro de Parceiros;
- **"Tem INSS"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos) do cadastro de Produtos;
- **"Tem FUNRURAL/INSS"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) do cadastro da TOP;
- **"Calcula FUNRURAL/INSS?"** da aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) nas Preferências da Empresa.

**Nota:** caso não haja qualquer TOP informada no campo TOP p/ Fixação do pop-up Preferências, o sistema exibirá a seguinte mensagem:

**"Informe a TOP p/ Fixação para simular o cálculo do Funrural."**

Atendendo a essas regras, o cálculo será feito considerando os valores informados nos campos **"% INSS"** da aba Impostos do cadastro de Produtos e **"% a ser subtraído da Alíquota do FUNRURAL/INSS"** da aba Fiscal do cadastro de Parceiros.

Já o botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/16028364810519) **"Gerar Fixação"** irá gerar a nota de fixação no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953) utilizando a Qtde p/ Fixação e o **"Valor Unitário"**, sendo este o resultado da soma dos campos Valor da Cotação + Valor do Abono.

Além da nota de fixação, o sistema poderá realizar a geração de complemento ou de devolução de valor na operação na mesma transação em que a fixação será gerada vinculando essa nota a nota de origem fixada. Para isso, será verificada a relação Valor Total da Fixação gerada x Valor Total das notas fixadas a fim de determinar qual ação tomar, da seguinte forma:

- **Gerar Complemento**: se o Valor Total da Fixação for maior que o Valor total das notas fixadas, considerando as fixações parciais;
- **Gerar Devolução**: caso o Valor Total da Fixação seja menor do que o Valor total das notas fixadas, considerando as fixações parciais;
- **Não gerar outro documento**: se o Valor Total da Fixação for igual ao Valor total das notas fixadas, considerando as fixações parciais.

Após a conclusão, será apresentado o pop-up **"Documentos da Fixação"** com a informação dos documentos gerados e um ![Lançador](https://ajuda.sankhya.com.br/hc/article_attachments/16028470258711) lançador que, ao ser acionado, o redicionará aos respectivos lançamentos na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793).

![Imagem 9: Após a conclusão, será apresentado o pop-up "Documentos da Fixação" com a informação dos documentos gerados e um…](https://ajuda.sankhya.com.br/hc/article_attachments/14814643636759)

Ao clicar no botão **"Visualizar Fixação"** será aberto o recibo da fixação.

Além disso, será possível que após a conclusão do procedimento, o usuário reimprima e/ou consulte uma fixação realizada anteriormente. Para isso, clique na lupa de pesquisa do campo **"Consultar Fixações"**, informe o **"N° da Fixação"** do contrato e acione o botão Visualizar Fixação para que o sistema abra o recibo desejado.

No entanto, caso seja incerto o número da fixação, poderá localizá-la utilizando os filtros disponíveis (**"Empresa"**, **"Parceiro"**, **"Contrato"** e **"Período"**), ao aplicar o filtro informado, serão apresentados os registros. Selecionando uma das linhas do resultado da busca, clique em Visualizar Fixação, assim, o relatório será aberto conforme o modelo padrão desenvolvido.

Ainda é possível consultá-la pela opção [Documentos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598054-Portal-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#documentosrelacionados) do botão Outras Opções... da Central ou Portal. Lembrando que, a nota de fixação estará vinculada às notas de origem listadas na grade Notas a Fixar (conforme o FIFO e à quantidade fixada) e ao consultar estas notas de origem poderá observar que a quantidade fixada não irá consumir a quantidade entregue da nota.

**Observação:** caso realize o cancelamento/exclusão de uma nota de compra ou de devolução no Portal/Central de Compras, que façam parte de um processo de Fixação, o sistema sinalizará que a nota de fixação vinculada a ele será excluída. Consequentemente, ao excluir a nota de fixação, serão excluídas as notas de complemento e de devolução que estiverem a ela vinculadas usando o mesmo motivo de cancelamento da nota de complemento/devolução de valor. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos#top) 

### Notas a Fixar

Nesta grade serão apresentadas as notas pendentes de fixação. 

![Imagem 10: Nesta grade serão apresentadas as notas pendentes de fixação.](https://ajuda.sankhya.com.br/hc/article_attachments/20351493276439)

**[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos#top)**

### Receitas a Compensar

Esta grade exibirá os títulos financeiros de receita do tipo Real e em aberto do Parceiro vinculado ao Contrato.

![receitas](https://ajuda.sankhya.com.br/hc/article_attachments/15966062495255)

A apresentação dos resultados nessa grade levam em consideração os filtros inseridos na aba Filtros p/Receitas do pop-up Preferências.

Quando os campos TOP p/ Baixa de Despesa e TOP p/ Baixa de Receita do pop-up de Preferências forem preenchidas; o sistema irá gerar além da fixação, as notas de complemento e/ou devolução dos títulos exibidos. Assim, o financeiro da nota de fixação, que será do tipo Despesa será compensado com os títulos de receita da grade, usando como valor do acerto, o menor entre eles. Lembrando que, se a fixação for desfeita, ao selecionar o acerto que faça parte desta fixação na tela [Compensação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073), o número desse acerto será apagado da fixação.

**Importante:** caso a TOP p/Fixação informada no pop-up Preferências esteja configurada para **"Nunca Incluir Confirmada"**, o sistema não permitirá a continuidade da operação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos#top) 

### Totalizadores

![Imagem 12: Totalizadores](https://ajuda.sankhya.com.br/hc/article_attachments/20351478657303)

O **"Abono Calculado"** será o resultado do cálculo:

```
![Imagem 13: O "Abono Calculado" será o resultado do cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/42313169224087) Valor do abono * Qtde p/ Fixação
```

O **"Total Bruto c/ Abono"** irá refletir o resultado do cálculo:

```
![Imagem 14: O "Total Bruto c/ Abono" irá refletir o resultado do cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/42313169224087) (Valor da cotação * Qtde p/ Fixação) + (Valor do abono * Qtde p/ Fixação) 
```

O **"Vlr. Funrural"** resultará da seguinte fórmula:

```
![Imagem 15: O "Vlr. Funrural" resultará da seguinte fórmula:](https://ajuda.sankhya.com.br/hc/article_attachments/42313169224087) (Qtde p/ Fixação * (Valor do Abono + Valor da Cotação)) *
(% INSS/Funrural - % a ser subtraído da Alíquota do FUNRURAL/INSS)
```

O **"Total Fixação"** será o resultado do cálculo:

```
![Imagem 16: O "Total Fixação" será o resultado do cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/42313169224087) Total Bruto c/ Abono - Vlr. Funrural
```

O **"Vlr. Receitas a Compensar"** refletirá a soma do valor líquido dos títulos exibidos na grade Receitas a Compensar.

Já o **"Total Líquido"** irá apresentar o resultado do cálculo:

```
![Imagem 17: Já o "Total Líquido" irá apresentar o resultado do cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/42313169224087) Total Fixação - Vlr. Receitas a Compensar
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14807463929623-Fixa%C3%A7%C3%A3o-de-Contratos#top)
