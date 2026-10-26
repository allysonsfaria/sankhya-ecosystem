---
id: "360044597054"
titulo: "Cotação - Parâmetros utilizados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597054-Cota%C3%A7%C3%A3o-Par%C3%A2metros-utilizados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:45:47Z"
rotulos: ["Configuração", "Cotação", "br.com.sankhya.swb.cotacao.rotinas.cotacao", "ENDACESSEXTWGE", "RESPCOTCOMPR", "AGRUPPRODREPCOT", "ALERTRESPMINCOT", "CODPRODGENCOT", "DTPADRAOMOECOT", "EXIBELOCALCOT", "EXIGCRCFR", "EXIGNATCFR", "TRABMOECOT", "USANROOSCOT", "Cotação - Parâmetros utilizados manual", "Parâmetros", "Estoque", "Preferências", "Parâmetros Cruciais para Cotações Eficientes"]
---

# Cotação - Parâmetros utilizados

Envolvidos na rotina de [Cotação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113993), estão diversos parâmetros que são empregados para algumas funcionalidades. Vale ressaltar que os parâmetros aqui mencionados, são os configurados na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias). Vejamos quais são estes parâmetros e o comportamento de cada um deles:

O parâmetro **"Exibe local na cotação? - EXIBELOCALCOT"** servirá para apresentar ou não o local de estoque do produto requisitado, no [Portal de Cotação Online](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114073), ou seja, por este parâmetro o comprador poderá controlar se seus fornecedores poderão ou não visualizar o local de estoque do produto.

Quando o parâmetro acima estiver ligado, o sistema irá exibir o campo de local do produto no Portal de Cotação Online para o fornecedor. Caso contrário, o campo não será exibido.

**Observação:** quando o parâmetro estiver desligado, e o comprador requisitar produtos que possuem locais diferentes, mas o restante das informações em comum, como empresa ou controle, o sistema irá agrupar suas quantidades em exibição no Portal de Cotação Online para o fornecedor.

O parâmetro **"Usa o número da OS na cotação - USANROOSCOT"** será utilizado para preencher alguns campos na tela de rotina de [Cotação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113993) de acordo com a requisição. Quando ele estiver ligado, e o comprador gerar uma solicitação de compra a partir de uma requisição, e essa requisição possuir os seguintes campos preenchidos nos itens:

- **Dt. Prev. Entrega:** Data de previsão de entrega do produto;
- **Observação:** Observação do item;
- **Número OS:** Número da ordem de serviço do item.

Na solicitação de compra (cotação) gerada, o sistema deverá preencher os campos abaixo respectivamente, de acordo com os campos citados acima da requisição:

- **Dt. Limite:** Data de limite para que o produto seja entregue até o comprador;
- **Observação:** Observação do produto na cotação gerada;
- **Número OS Gub.:** Número da ordem e serviço do produto na cotação gerada.

Caso o parâmetro esteja desligado, o campo **"Número OS Gub."** não ficará habilitado, e quando o comprador gerar a cotação a partir de uma requisição, o sistema não irá preencher os campos conforme citado acima.

Através do parâmetro **"Mínimo de respostas p/sugestão result. cotação - ALERTRESPMINCOT"**, o comprador define qual o mínimo de respostas de preço dos fornecedores para que seja calculado e sugerido qual o melhor fornecedor.

O produto somente é considerado como precificado na rotina de Cotação, caso tenha a quantidade de fornecedores que responderam à cotação igual ao informado no parâmetro.

**Observação:** se o parâmetro for igual a "2" e o comprador inserir somente um fornecedor para cotação e preencher o preço deste, o produto ainda não será considerado como precificado.

O parâmetro **"Agrupar produtos repetidos ao gerar a cotação - AGRUPPRODREPCOT"** servirá para que, quando o comprador gerar uma cotação a partir de uma requisição, e essa requisição possuir o mesmo produto em mais de uma linha de item considerando controle e local, na geração da cotação, estes serão agrupados somando suas quantidades, inclusive se possuírem a mesma data de previsão de entrega, observação e número de OS (parâmetro **"Usa o número da OS na cotação-USANROOSCOT"**).

Por meio do parâmetro **"Trabalhar com Moedas na Cotação? - TRABMOECOT"** o comprador poderá definir se trabalha ou não com moedas no processo de cotação. Quando o parâmetro estiver ligado, a rotina de Cotação possuirá os seguintes campos habilitados:

- **Data da moeda:** Data da cotação da moeda selecionada;
- **Código da moeda:** Moeda previamente cadastrada no sistema;
- **Valor da moeda:** Valor da moeda calculada a partir da data de cotação da mesma, informada no campo Data da moeda.

O botão **"Calcular moeda"** também será habilitado com a ativação do parâmetro acima; caso esteja desativado, o botão bem como os campos acima mencionados não serão habilitados.

Através do parâmetro **"Data Padrão p/ Moeda na Cotação, Coleta ou do Dia - DTPADRAOMOECOT"** determine qual será a data padrão para cotação da moeda, de acordo com as seguintes opções:

- **Dia:** Ao calcular uma moeda na rotina de cotação, o sistema automaticamente irá considerar a data de cotação da moeda como a data atual do sistema;
- **Coleta:** Ao calcular uma moeda na rotina de cotação, o sistema automaticamente considera a data de cotação da moeda como a data da coleta do preço.

**Observação:** caso o parâmetro esteja definido com a opção Coleta e o produto selecionado ainda não possua data da coleta, a data atual será considerada. E caso a data atual ou data da coleta obtida não esteja cadastrada como cotação da moeda, o sistema deverá considerar a primeira data mais antiga.

Por meio do parâmetro **"O responsável pela cotação tem que ser comprador? - RESPCOTCOMPR"**, determina-se que os responsáveis pela cotação possam ser somente usuários que são compradores. Caso o parâmetro esteja ligado, ao lançar uma nova cotação, selecionando-se o usuário responsável, o sistema somente permitirá usuários que sejam compradores; caso o parâmetro esteja desligado, qualquer usuário poderá ser responsável pela cotação.

Para o sistema, um usuário é considerado comprador, caso possua um funcionário informado no cadastro [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao), campo **"Funcionário"** e este mesmo funcionário deverá ser informado no [Cadastro Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133#abageral), campo **"Funcionário"**. Além disso, deve ser selecionado no campo **"Tipo"** a opção **"Comprador"**, para o comprador cadastrado.

Através do parâmetro **"Código p/ produto genérico na cotação - CODPRODGENCOT"**, o comprador permite ou não o lançamento de produtos repetidos na cotação. O parâmetro pode ser configurado com três valores:

- **-1 (menos um):** Caso seja informado este valor, todo e qualquer produto poderá se repetir no lançamento da cotação;
- **0 (zero):** Informando este valor, nenhum produto poderá se repetir no lançamento da cotação;
- **Valor maior que 0:** Neste caso, deve-se informar o código do produto que poderá se repetir, sendo permitida repetição somente para este produto no lançamento da cotação.

Sendo que, caso o produto a ser inserido seja repetido na mesma cotação e o parâmetro esteja configurado para não permitir a inserção; tem-se a exibição da seguinte mensagem:

**"Os seguintes produtos já existem em alguma cotação para a empresa X com o situação igual a "Aberta", portanto não é possível incluí-los. Produtos:**

**Y - "NOMEDOPRODUTO"**

**Retire esse(s) produto(s) dentre os selecionados para gerar cotação."**

Se tratando do Portal de Cotação online, somente através da configuração do parâmetro **"Endereço para acesso externo ao WGE - ENDACESSEXTWGE"** será possível o fornecedor realizar o acesso. Nele informe o endereço de acesso externo ao sistema.

Caso o parâmetro **"Exigir CR na central/financeiro/rateio? - EXIGCRCFR"** esteja ativado, no momento da geração do pedido de compra, se o campo **"Centro de Resultado"** não estiver informado, o sistema irá apresentar a seguinte mensagem:

**"Erro na nota. O Centro de Resultado deve ser informado. O parâmetro 'EXIGCRCFR' está ligado."**

De forma semelhante ao anterior, caso o parâmetro **"Exigir natureza na central/financeiro/rateio? - EXIGNATCFR"** esteja ligado, no momento da geração do pedido de compra, se o campo **"Natureza"** não estiver informado, a seguinte mensagem será exibida:

**"Erro na nota. A natureza deve ser informada. O parâmetro 'EXIGNATCFR' está ligado."**

### Fechar cotação na geração de Pedidos? - FECHARCOTGERPED

Este parâmetro é responsável por fechar a cotação automaticamente no momento em que o pedido é gerado, desde que regras específicas nos itens sejam atendidas.

- **Comportamento inicial:** quando uma Cotação é criada, o campo **"Situação"** (aba Geral) é definido nativamente como **"Aberta"**.
- **Regra para fechamento:** a situação geral da cotação só terá seu valor alterado para **"Fechada"** se o parâmetro **FECHARCOTGERPED** estiver ligado e **todos** os itens da Cotação possuírem o campo **STATUSPRODCOT** (coluna **"Situação do produto"** da aba **Itens de Cotação**) igual a **"Fechado"** ou **"Cancelado"**.
- **Momento da execução:** o gatilho para essa validação e alteração de status ocorre especificamente ao **gerar o pedido**.

Veja os prints abaixo para apoiar no entendimento desse parâmetro: 
![Campo "Situação" na aba Geral da Cotação.](https://ajuda.sankhya.com.br/hc/article_attachments/37943316974487)

![Coluna "Situação do produto" na aba Itens de Cotação.](https://ajuda.sankhya.com.br/hc/article_attachments/37943308134679)
