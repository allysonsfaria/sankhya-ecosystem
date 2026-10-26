---
id: "360045108833"
titulo: "Compensação de Devolução"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108833-Compensa%C3%A7%C3%A3o-de-Devolu%C3%A7%C3%A3o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:10Z"
rotulos: ["Configuração", "Compensação de Devolução", "Compensação de Devolução manual", "Contas", "Parceiro", "Movimentação Financeira", "Financeiro"]
---

# Compensação de Devolução

Compensar uma devolução é um aproveitamento do valor da devolução feita pelo Parceiro, de modo que este valor será debitado das compras anteriormente efetuadas por ele. Considere o seguinte exemplo:

O Parceiro efetuou três compras parceladas em datas distintas por meio das notas 10, 22 e 35; posteriormente, ele decide realizar uma devolução, porém a Empresa não realiza a devolução monetária ao cliente (não devolve o dinheiro); neste caso, é indicada a compensação da devolução, pois é pego o valor da devolução da venda, e efetua-se o abatimento deste valor nas parcelas que o Parceiro possui ainda em aberto junto a Empresa (notas 10, 22 e 35).

Para realizar a compensação, é fundamental que a nota de devolução esteja lançada e confirmada no sistema. Além disso, é necessário informar uma [Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) que esteja configurada com a marcação **"Emite"** ativada e o [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) com a opção **"Imprimir Pix/Boleto/Duplicata?"** (aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas)), diferente de **"Proibido"**. O sistema segue a sequência abaixo para localizar a Conta:

1. Será utilizada a Conta informada nas parcelas do Tipo de Negociação, se especificada.
2. Caso não haja conta definida nas parcelas, o sistema buscará o parâmetro **"Conta padrão para financeiro-CONTAPADRAOFIN"**.
3. Se esse parâmetro não estiver configurado, será verificado o parâmetro **"Número da conta padrão na baixa-CONTAPADRAO"** para localizar a conta.
4. Na sequência, o sistema verificará no cadastro de [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610034-Parceiro) o campo **"Conta bancária da empresa"** na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610034-Parceiro#abaidentificao). Se esse campo estiver preenchido, a conta será utilizada. Caso contrário, o sistema buscará no Tipo de Negociação a conta do Banco configurada como **"Conta padrão para emissão"** (aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas)). Se houver mais de uma conta, será selecionada a de menor código, com preferência para contas exclusivas da empresa, mas aceitando também contas não exclusivas.
5. Em seguida, o sistema verificará o parâmetro **"Substitui Conta do Financeiro com Conta Baixa - SUBSTCONTA"**.
6. Se nenhuma das opções anteriores apresentar informações de conta, o sistema verificará se a [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) possui uma Conta configurada com as marcações **"Conta padrão para emissão"**, **"Emite"** e **"Exclusiva da empresa"** marcadas. A conta de menor código será escolhida.

Caso nenhuma dessas opções seja atendida, o financeiro da nota ficará sem informação bancária.

Este procedimento é realizado na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), onde primeiramente você localiza a nota de devolução desejada e por meio do botão **"Outras Opções..."**, seleciona a opção **"Compensar devolução"**.

**Observação:** quando o parâmetro **"Realizar compensação de devolução usando acerto - COMPDEVACERTO"** for ligado, o campo **"Nro Compensação/Acerto"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#abageral) da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela) será preenchido quando houver uma compensação de devolução realizada nas [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas).

Em seguida, será aberto o pop-up **"Compensação de Devolução"**:

![Imagem 1: Em seguida, será aberto o pop-up "Compensação de Devolução" :](https://ajuda.sankhya.com.br/hc/article_attachments/7442963840023)

A partir disso, têm-se as seguintes etapas:

Primeiramente, serão apresentados os títulos referentes às notas de devolução que poderão ser utilizados para compensação. O sistema permite a seleção de um único título a ser compensado. Para prosseguir, selecione o título e clique no botão **"Próximo"**, ou realize um duplo clique na linha selecionada;

Em seguida, escolha as pendências que serão compensadas pelo título de devolução inicialmente definido:

![Imagem 2: Em seguida, escolha as pendências que serão compensadas pelo título de devolução inicialmente definido:](https://ajuda.sankhya.com.br/hc/article_attachments/7443014599575)

Ainda nesta etapa, você poderá fazer o uso de filtros personalizados para localização dos títulos que irão compor a compensação. Pode-se também selecionar quais notas pendentes serão apresentadas para escolha. Assim, temos as seguintes opções:

- **Notas de Origem:** Caso a nota de devolução seja uma nota renegociada, serão exibidos os títulos correspondentes às suas notas de origem.
- **Todas as Notas:** Serão exibidos todos os títulos que o parceiro possui em aberto junto à empresa.
- **Matriz e Filial:** Por esta opção, serão apresentados os títulos do parceiro lançados junto à empresa e sua correspondente matriz.

**Observação:** caso o parâmetro **"Compensar Dev.somente na mesma Empresa? - COMPDEVEMP"** seja habilitado, serão apresentadas na tela apenas as pendências da mesma empresa quando definido os filtros Todas as Notas e Matriz e Filial.

Além disso, é necessário definir como será realizado o cálculo de compensação, ou seja, **"Proporcional"** ou **"Manual"**. Sendo de maneira Proporcional, o título da devolução será compensado proporcionalmente entre as pendências selecionadas. Já de forma Manual, cada título pendente é compensado pelo seu valor total, até que todo o valor da devolução seja compensado. Você pode definir a ordem dos títulos que serão compensados.

**Observação:** se durante a busca de títulos o sistema localizar um único título, o assistente de Compensação de Devolução avançará automaticamente para o segundo passo acima descrito.

**Nota:** caso haja títulos já compensados, estes poderão ser estornados, caso assim queira. Para essa ação, basta clicar no botão ![Imagem 3: Nota: caso haja títulos já compensados, estes poderão ser estornados, caso assim queira. Para essa ação, basta clicar…](https://ajuda.sankhya.com.br/hc/article_attachments/20612618710551) **"Estornar"** na grade que esses títulos serão exibidos.

Por fim, acione o botão **"Compensar"**, com isso, a compensação será processada e serão exibidas outras três opções:

![Imagem 4: Por fim, acione o botão "Compensar" , com isso, a compensação será processada e serão exibidas outras três opções:](https://ajuda.sankhya.com.br/hc/article_attachments/7443004830871)

- **Compensar próximo título:** Esta opção será apresentada caso existam outros títulos a serem compensados. Assim, o sistema retorna a primeira etapa citada.
- **Ver títulos baixados:** Por meio dessa opção, serão exibidos os **"Títulos baixados"** e os **"Títulos em aberto"**.
- **Encerrar a compensação:** Esta opção irá finalizar a Compensação da Devolução.

Ao efetuar a compensação, alguns títulos poderão ser baixados parcialmente. Nesse caso, o título original será baixado e a pendência será lançada em um novo título, que será a cópia do título original.

**Importante:** as notas de devolução ligadas às suas respectivas notas de origem, que por sua vez fizeram parte do processo de compensação de devolução, tem seu valor abatido do valor desta nota de origem ao final do processo, ou seja, o documento de origem é modificado, o que nos remete aos boletos correspondentes à estes títulos que também sofrem modificação. Diante desse cenário, depois da compensação realizada, tem-se a necessidade de efetuar a reimpressão do boleto e/ou seu envio por e-mail ao cliente, para que o mesmo efetue seu pagamento.

![Imagem 5: A Compensação de Devolução da Central não efetua a compensação em moeda, para esse processo deve-se utilizar a rotina…](https://ajuda.sankhya.com.br/hc/article_attachments/19965600691735) A Compensação de Devolução da Central não efetua a compensação em moeda, para esse processo deve-se utilizar a rotina [Compensação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115073).

Caso os títulos envolvidos na compensação tenham gerado boletos, ao final do procedimento de compensação, os boletos modificados serão exibidos na grade com esta mesma nomenclatura.

A partir disso, pode-se realizar a **"Reimpressão"** ou **"Reenvio"** dos documentos em questão. Ao clicar em Reimprimir boletos, o sistema apresenta a seguinte mensagem a respeito da reimpressão a ser executada:

**"Reimprimir todos os boletos ou somente os selecionados?"**

Se você selecionar o botão **"Todos"**, serão impressos os boletos referentes aos títulos da grade; caso você indique a opção **"Selecionados"** será impresso o boleto correspondente ao título selecionado na grade; e se você optar por **"Cancelar"** não será impresso nenhum boleto e o pop-up será fechado.

Definindo por Reenviar os boletos, será aberto o pop-up **"Destinatários (opcional)"** para que você informe a lista de e-mails dos destinatários.

O reenvio de boletos segue as seguintes regras:

- Ao informar o endereço de e-mail, será utilizado o primeiro endereço como destinatário da mensagem enviada e os demais endereços como cópia; assim, é possível especificar dois ou mais endereços de e-mail separados por ponto e vírgula (**;**);
- Quando não for informado nenhum endereço de e-mail, será utilizado como destinatário da mensagem enviada o e-mail do parceiro da nota a qual o boleto pertence. Os endereços de e-mail dos contatos do parceiro da nota a qual o boleto pertence, receberão a mensagem como cópia.
- Quando não for informado nenhum endereço de e-mail e o parceiro da nota a qual o boleto pertence não apresenta e-mail especificado, a mensagem será enviada para o e-mail de todos os contatos que possuírem e-mail definido utilizando o primeiro deles como destinatário e os demais como cópia.
- Não sendo informado nenhum endereço de e-mail, e o parceiro e seus contatos não possuírem endereço de e-mail especificado, nenhuma mensagem de e-mail será gerada.

**Nota:** caso você decida Reenviar ou Reimprimir o boleto em um outro momento, acesse a tela [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793), opções **"Reimpressão"**, **"Reenvio"** ou a tela [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094).

Nos parâmetros **"TOP baixa da despesa na compensação de devolução - TOPBAIDESPDEV"** e **"TOP baixa da receita na compensação de devolução - TOPBAIRECDEV"** deverão ser inseridos os códigos dos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizados nas baixas da compensação, quando se tratar de um título de receita e quando este for de despesa, respectivamente.
