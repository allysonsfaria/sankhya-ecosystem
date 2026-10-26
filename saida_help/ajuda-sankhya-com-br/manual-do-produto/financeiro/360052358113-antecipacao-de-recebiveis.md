---
id: "360052358113"
titulo: "Antecipação de Recebíveis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:46:06Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Financeiro", "br.com.sankhya.antecipacaoderecebiveis", "Permitir antecipação recebíveis", "Configurar filtros e despesas", "Antecipar desfazer baixar títulos", "Recebíveis"]
---

# Antecipação de Recebíveis

```
 Módulo: Financeiro > Rotinas                       Versão disponível: A partir 4.3
```

---

Por meio dessa tela, você poderá permitir a antecipação de recebíveis, mantendo o título de seu cliente em aberto, ou seja, é um adiantamento de recursos realizado pelo banco, referente aos valores de títulos (duplicatas, cheques, notas promissórias, etc.), de forma a antecipar o fluxo de caixa.

Acesse os links abaixo para facilitar sua navegação nas funcionalidades desta tela:

[Contextualização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis#contextualiza%C3%A7%C3%A3o)                                                 [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis#filtros)

[Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis#bot%C3%B5esdotopodatela)                                       [Considerações importantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis#considera%C3%A7%C3%B5esimportantes)   

## Contextualização

No tipo de operação realizado nessa tela, destacamos que seu cliente receberá o dinheiro antecipado de suas vendas a prazo. Entretanto, ao apresentar um título para antecipação, ele não recebe seu valor total, pois diversos encargos sobre seu valor nominal serão descontados, como juros, IOF e taxas administrativas.

Essa operação dá ao banco o direito de regresso, ou seja, se no vencimento o título não for pago pelo sacado, o cedente assumirá a responsabilidade do pagamento, incluindo multa e/ou juros em decorrência do atraso.

Ao efetivar a antecipação, o valor do título é lançado como receita contra o banco envolvido na operação com as despesas. Quando forem lançados, ocorrerá a compensação entre eles, de modo que, o valor líquido será igual ao pago pelo banco na antecipação, para que ocorra a baixa com a movimentação bancária.

**Nota:** quando você efetuar a antecipação do título, o sistema não efetuará sua baixa, ele o marcará como antecipado na TGFFIN, campo NUANTBANC.

Quando essa operação for realizada, a empresa deverá pagar as despesas com o banco, de forma que, se o pagamento não for realizado, o banco realizará um débito automático do valor do título na conta-corrente, sendo que este possivelmente terá mais encargos para fins de quitação da pendência. Essa obrigação será lançada como um **"Contas a pagar"** ao banco, no mesmo valor e vencimento do título antecipado.

Aqui, você também poderá realizar a execução da operação para vários títulos simultaneamente, porém, com as baixas e lançamento separados, prevendo que pode haver a necessidade futura de regresso de algum título não pago.

![Imagem 1: Aqui, você também poderá realizar a execução da operação para vários títulos simultaneamente, porém, com as baixas e…](https://ajuda.sankhya.com.br/hc/article_attachments/1500018531842)

**Observação:** para atualizar, ou alterar uma informação manual nos lançamentos de origem da antecipação, ou lançamentos gerados a partir desta, deve-se desfazer a antecipação, corrigir a informação e em seguida, realizar outro lançamento. Desse modo, a integridade registrada no sistema é mantida.

**Nota:** não é possível realizar a recompra de título no sistema.

**Observação:** nesta tela, não serão apresentados os títulos cujo **"Valor Líquido"** seja igual ou inferior a zero.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis#top)

## Filtros

No painel de Filtros, você poderá filtrar por **"Tipo de Título"**, **"Vencimento"**, **"Empresa"**, **"Parceiro"**, **"N° Nota"**, e **"N° Único"** sendo que, ao filtrar por Tipo de Título, teremos as opções:

- **Não antecipados:** são títulos elegíveis para antecipação, não vencidos e que não foram antecipados e não pagos;
- **Antecipados:** títulos que já passaram pelo processo de antecipação, mas que ainda não foram quitados;
- **Antecipado e baixado:** aqui teremos os títulos antecipados e baixados.
- **Antecipado não pago:** são títulos que foram antecipados e não foram pagos pelo cliente.

Na aba **"Despesas operacionais"**, serão lançadas todas as despesas incidentes na operação, caso existam.

![Imagem 2: Na aba "Despesas operacionais" , serão lançadas todas as despesas incidentes na operação, caso existam.](https://ajuda.sankhya.com.br/hc/article_attachments/1500018531982)

Em **"Data da antecipação"**, informe a data em que a operação será realizada.

O valor informado no campo **"Vlr. de Antecipação por Título"**, será incluído como despesa em cada título. Já o valor inserido no campo **"Vlr. de Antecipação por Operação"**, será dividido entre os títulos selecionados e adicionado como despesa em cada título.

Em relação ao campo **"Vlr. de Antecipação por Operação"**, ao acionar o botão **"Antecipar"**, será apresentado um pop-up para confirmação da antecipação; nesse pop-up, temos o campo **"Distribuir Vlr. de Antecipação por Operação"** para você escolher como quer distribuir a despesa operacional entre os títulos, se **"Igualmente"** ou **"Proporcionalmente"**.

No campo **"Vlr. IOF"** você poderá lançar a taxa de IOF incidente sobre os títulos que estão sendo antecipados, para que assim, o sistema calcule o imposto separadamente, sendo possível então, realizar sua contabilização.

**Observação:** sendo assim, quando você informar no campo acima valores com até 2 casas decimais e clicar no botão Calcular Despesas, o sistema irá calcular a proporção do imposto para cada título antecipado. A fórmula para o cálculo do IOF é: (Vlr. do iof / Valor dos títulos)\*100.

**Nota:** no rodapé da tela, você poderá visualizar o valor total calculado referente ao IOF no totalizador **"Total Vlr. IOF"**.

Informe no campo **"Taxa de Juros diária"**, a taxa de juros que é paga pelo desconto de títulos por dia.

Você poderá definir através do campo **"Tipo de Juros"**, se os juros serão calculados de forma **"Simples"** ou **"Compostos"**.

No campo **"Outra taxa de Juros diária"** você informa uma taxa adicional paga pelo desconto de título por dia.

Também temos disponível o botão ![Imagem 3: Também temos disponível o botão " Calcular Despesas" , que é responsável por realizar uma prévia dos valores…](https://ajuda.sankhya.com.br/hc/article_attachments/16088442408471) **"Calcular Despesas"**, que é responsável por realizar uma prévia dos valores pagos/descontados. É necessário utilizar esse botão para dar continuidade à antecipação.

**Nota:** a cada alteração dos campos de despesa operacional, você deve pressionar o botão Calcular Despesas.

Quando o campo **"Tipo de Título"** estiver com a opção **"Não Antecipado"** selecionada, ao clicar no botão Calcular Despesas na aba Despesas Operacionais, o botão ![Imagem 4: Quando o campo "Tipo de Título" estiver com a opção "Não Antecipado" selecionada, ao clicar no botão Calcular Despesas…](https://ajuda.sankhya.com.br/hc/article_attachments/16088463927703) **"Ajustar Juros"** será habilitado. Assim, ao clicar nesse botão, será aberto um pop-up para você informar e aplicar o valor dos juros em moeda:

![Imagem 5: Quando o campo "Tipo de Título" estiver com a opção "Não Antecipado" selecionada, ao clicar no botão Calcular Despesas…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019262502)

**Observações:**

- Se o valor nesse pop-up estiver zerado, o botão **"Ajustar"** ficará inativo.
- Quando você clicar no botão Ajustar Juros, informar o valor e aplicar o ajuste para compor os Juros da Antecipação no rodapé e, em seguida alterar algum dos campos do painel Despesas Operacionais, fará com que o valor informado manualmente seja zerado no rodapé.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis#top)

## Botões do topo da tela

Na Antecipação de Recebíveis, temos alguns botões com funcionalidades específicas, são eles:

![Imagem 6: "Detalhes" : por meio deste, as informações referente aos títulos gerados no lançamento da antecipação serão exibidas:](https://ajuda.sankhya.com.br/hc/article_attachments/16088205756055) **"Detalhes"**: por meio deste, as informações referente aos títulos gerados no lançamento da antecipação serão exibidas:

![Imagem 7: "Detalhes" : por meio deste, as informações referente aos títulos gerados no lançamento da antecipação serão exibidas:](https://ajuda.sankhya.com.br/hc/article_attachments/360081673314)

![Imagem 8: "Antecipar" : ao clicar nesse botão, o pop up "Antecipação" será exibido e, conterá as informações das preferências da…](https://ajuda.sankhya.com.br/hc/article_attachments/16088339020311) **"Antecipar"**: ao clicar nesse botão, o pop up **"Antecipação"** será exibido e, conterá as informações das preferências da antecipação dos lançamentos de receitas e despesas.

![Imagem 9: "Antecipar" : ao clicar nesse botão, o pop up "Antecipação" será exibido e, conterá as informações das preferências da…](https://ajuda.sankhya.com.br/hc/article_attachments/1500018804401)

Quando você realizar uma antecipação e tiver valor informado de IOF, considerando que a **"Natureza"** e/ou **"Centro de Resultado"** do IOF foram configurados no pop-up acima, o sistema irá gerar uma linha de IOF para cada título que foi antecipado, para que seja possível a contabilização desse imposto de forma separada. Porém, se não houver Natureza e/ou Centro de Resultado informados, será somado o valor do IOF às demais despesas operacionais.

Ao realizar a antecipação de um título que contenha incidências de juros, o sistema se comportará da seguinte maneira:

- Quando o parâmetro **"Considerar natureza de juros na antecipação - NATJUROANTEC"** estiver ligado, e a **"Natureza"** do **"Lançamento juros"** for informada, o título de **“juros/encargos”** conterá apenas os juros (Juros + Outra Taxa Diária) com a natureza de despesa definida no campo **“Natureza”** do subgrupo **“Lançamento Juros”** e o título de contrapartida de Receita para juros/encargos, receberá os dados definidos no subgrupo **“Lançamento/Baixa das Receita"**;
- Sendo gerado um título chamado **“Demais despesas operacionais”** com o restante das despesas financeiras da operação, sendo elas: Vlr. de Antecipação por Título + Vlr. de Antecipação por Operação + IOF (caso este não tenha recebido uma Natureza e/ou Centro de Resultado própria no subgrupo **“Lançamento IOF”**).

**Nota:** quando o título possuir um desconto, ainda assim, os cálculos de encargos da antecipação são feitos sobre o valor total do título, sendo que o valor do título em si é considerado líquido. Desse modo, se os encargos forem maiores que o valor líquido não será possível realizar a antecipação.

![Imagem 10: "Desfazer" : se você clicar nesse botão, será desfeito o lançamento do título antecipado e, assim, exibirá o pop up…](https://ajuda.sankhya.com.br/hc/article_attachments/16088395900951) **"Desfazer"**: se você clicar nesse botão, será desfeito o lançamento do título antecipado e, assim, exibirá o pop up **"Desfazer Operação"**:

![Imagem 11: "Desfazer" : se você clicar nesse botão, será desfeito o lançamento do título antecipado e, assim, exibirá o pop up…](https://ajuda.sankhya.com.br/hc/article_attachments/360081674134)

Caso o seu cliente não pagar o título, o banco irá debitar da conta de sua empresa, o valor nominal adicionado da devida correção previamente acordada. O valor debitado deverá baixar a obrigação a pagar, lançada contra o banco no momento da operação.

Para isso, a Antecipação de Recebíveis deve retornar o título antecipado para a carteira e cobrança normal, ao baixar automaticamente o título de despesa pendente no código do banco contra o valor debitado em conta e ainda, possibilitando o lançamento dos juros e encargos incorridos sobre o não pagamento.

Ao utilizar o botão Desfazer, você poderá selecionar o motivo pelo qual a ação está sendo desfeita dentre as opções:

- **Operação não realizada:** selecione essa opção, quando a operação com o banco não se concretizar e todos os movimentos tiverem que ser desfeitos.
- **Pagamento não efetuado pelo cliente:** essa opção deve ser utilizada quando seu cliente não efetuar o pagamento do título antecipado. Será desfeito apenas o vínculo do título do cliente com o lançamento feito contra o Banco, e a alteração do campo Antecipado para Antecipado e Não Pago.

![Imagem 12: "Baixar" : o botão Baixar realizará a baixa do título antecipado, finalizando assim, o processo. Após a confirmação do…](https://ajuda.sankhya.com.br/hc/article_attachments/16088401802007) **"Baixar"**: o botão Baixar realizará a baixa do título antecipado, finalizando assim, o processo. Após a confirmação do pagamento pelo cliente, o título é baixado sem movimentação bancária, pois o saldo bancário já foi movimentado anteriormente, no momento em que o valor do título antecipado foi pago pelo banco.

Isso é feito com a compensação do título antecipado do cliente, com a obrigação a pagar lançada contra o banco no momento da efetivação da operação.

**Importante:** ao acionar o botão Baixar, se houverem registros sem carimbo no período selecionado será apresentado o aviso:

**"Você possui registros de notas ou financeiras que infringem as regras e condições de uso do Sankhya Om e podem comprometer a integridade e segurança do EIP.**

**Para que as movimentações sejam normalizadas exclua os documentos sem origem reconhecida ou comunique o administrador da aplicação para que o padrão de governança seja seguido"**

Para conferir sobre como corrigir os registros, acesse o artigo [Registros não identificados.](https://ajuda.sankhya.com.br/hc/pt-br/articles/15935553131671)

**Observação:**  os títulos antecipados gerados nessa rotina, só poderão ser baixados por meio dessa tela.

**Importante:** o parâmetro **"Permite parceiro vazio no filtro da compensação financeira - PERMFILPARCVAZ"** precisa estar ligado para que a compensação (Cliente x Banco) ocorra.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis#top)

## Considerações importantes

1. Nas [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#preferncias) da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), você poderá definir uma cor para apresentação dos títulos de antecipação, na grade de exibição, por meio do campo **"Cor para antecipados"**:

![Imagem 13: Nas Preferências da Movimentação Financeira , você poderá definir uma cor para apresentação dos títulos de antecipação,…](https://ajuda.sankhya.com.br/hc/article_attachments/360082828713)

Nos filtros da tela [Fluxo de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051904053-Fluxo-de-Caixa) e Preferências da [Agenda Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115533-Agenda-Financeira), temos a opção **"Desconsiderar Antecipação"**, para que o sistema desconsidere as antecipações nas buscas.

![Imagem 14: O parâmetro "Valida tipo de natureza (Receita / Despesa) na movimentação - VALIDATIPONAT" não realiza validação nesta…](https://ajuda.sankhya.com.br/hc/article_attachments/26897264284695) O parâmetro **"Valida tipo de natureza (Receita / Despesa) na movimentação - VALIDATIPONAT"** não realiza validação nesta rotina, pois essa verificação ocorre apenas na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

2. **Observação:**
Quando o título possuir **desconto** e estiver vinculado ao **evento de liberação “29 – Desconto no Financeiro”**, é necessário que o **usuário realize previamente a liberação do evento** antes de executar a **antecipação**.
Caso contrário, o sistema impedirá a baixa do título antecipado até que a liberação seja concluída.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052358113-Antecipa%C3%A7%C3%A3o-de-Receb%C3%ADveis#top)
