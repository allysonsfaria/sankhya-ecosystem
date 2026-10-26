---
id: "360044609514"
titulo: "Cópia de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514-C%C3%B3pia-de-Estoque"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-10-01T12:31:31Z"
rotulos: ["Produtos", "Configuração", "Inventário", "WMS", "Estoque", "Cópia de Estoque manual", "Cópia de Estoque", "br.com.sankhya.mgeinvent.copia.estoque", "Definir empresa data local", "Agrupar por controle/local copiar consignação", "Copiar estoque para conferência", "INVEXCCONTCOPIA"]
---

# Cópia de Estoque

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312595264023) Módulo: Inventário > Arquivo
```

---

Esta tela é utilizada para que efetuar a cópia do estoque. Essa cópia é feita para que depois, seja usada na tela de [Contagem de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694) a fim de que seja feita a conferência do estoque. Além disso, a Cópia de Estoque é também utilizada na rotina [Registro de Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117653-Registro-de-Invent%C3%A1rio).

**Importante:** produtos com o USOPROD marcado como **"T"** (Terceiros) não podem ser duplicados na cópia de estoque.

![Imagem 2: Importante: produtos com o USOPROD marcado como "T" (Terceiros) não podem ser duplicados na cópia de estoque.](https://ajuda.sankhya.com.br/hc/article_attachments/360078183653)

Inicialmente, informe a **"Empresa"** da qual o Estoque será copiado.

**Nota:** ao preencher este campo, é sugerido automaticamente no campo **"Empresa destino"**, a mesma empresa.

Preencha no campo **"Empresa destino"** a Empresa que receberá a cópia do Estoque.

Marcando a opção **"Copiar estoque de hoje"**, a cópia será realizada na data do dia atual da execução, e o campo **"Data da cópia"** será desabilitado.

Você poderá informar o campo Data da cópia a data em que a cópia será executada.

Você pode determinar o **"Grupo de produtos"** que deseja buscar os itens a serem copiados.

De maneira similar ao campo anterior, no campo **"Local de estoque"** defina o local de estoque que você deseja buscar os produtos a serem copiados.

Efetuando a marcação **"Somente estoque maior que zero"**, os produtos que tiverem a quantidade igual ou menor a zero não serão copiados.

A marcação **"Filtro para produtos sem estoque"** estará disponibilizada para uso quando a marcação Somente estoque maior que zero estiver desabilitada; temos neste botão, a possibilidade de criar um filtro que considere os produtos que não possuem estoque, ou seja, com quantidade menor ou igual a zero. Ao executar a rotina sem nenhum filtro de produtos sem estoque selecionado, a cópia de estoque é executada normalmente; caso este filtro esteja ativo, além da cópia normal, serão copiados os produtos que não têm estoque e já tiveram movimentação, respeitando o critério estabelecido no filtro.

**Observação:** na utilização do Filtro para produtos sem estoque, o sistema realiza a cópia dos produtos, porém, a quantidade dependerá do estoque do item; sendo menor que zero, a quantidade será zero, caso contrário, será a quantidade de estoque do produto no período. Caso seja necessário que algum produto não seja copiado, utilize o botão Filtro localizado no topo da tela.

Ao efetuar a marcação **"Usar data Entrada/Saída para filtro"**, o sistema fará a cópia com base na data de **"Entrada/Saída"** do cabeçalho da nota, independentemente da configuração da TOP, portanto, esta informação deverá estar preenchida em todas as notas.

**Observação:** caso a marcação acima esteja desabilitada e a marcação **"Usar Dt.Negociação p/ TOPs de livro de saída"** esteja ligada, trará para a cópia do estoque todos os movimentos que possuam a TOP configurada para atualizar livro fiscal pela data da negociação maior ou igual à data definida no filtro e os movimentos em que a TOP esteja configurada para não atualizar livro fiscal pela data de entrada e saída maior ou igual à data definida no filtro.

Quando nenhuma das marcações estiverem ativas, o sistema dará preferencia aos movimentos pelo campo DTENTSAI porém quando este for nulo trará pelo DTNEG.

Efetuando a marcação **"Usar Dt. Negociação p/ TOPs de livro de saída"**, ao fazer a cópia de itens cuja TOP seja de livro de saída, será utilizada a Data de Negociação do cabeçalho da nota para o filtro dos itens.

**Nota:** esta marcação não pode ser utilizada em conjunto com a opção **"Usar data Entrada/Saída para filtro"**.

#### Seção Agrupar

Nesta seção, será determinado se serão e como serão realizados os agrupamentos dos produtos copiados.

A marcação **"por controle"** determina o agrupamento dos produtos de acordo com o controle dos mesmos; esta marcação é habilitada caso o parâmetro **"Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE"** esteja ativado.

Abaixo temos um exemplo:

|  | **Tamanho** | **Qtd.** |
| --- | --- | --- |
| **Camisa** | P | 5 |
|  | M | 10 |
|  | G | 7 |
| **Total:** |  | **22** |

|  | **Tamanho** | **Qtd.** |
| --- | --- | --- |
| **Calça** | 34 | 7 |
|  | 36 | 10 |
|  | 38 | 8 |
| **Total:** |  | **25** |

É diferente para a análise do estoque, separar as camisas de mesmo código com tamanhos diferentes; assim, o sistema irá totalizar por Código e não por Código/Controle.

Já a marcação **"por** local", define o agrupamento dos produtos de acordo com seu **"local"**; esta marcação é habilitada quando o parâmetro **"Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL"** estiver ligado.

Temos abaixo um exemplo:

Temos os seguintes locais:

Prateleira 1

Prateleira 2

E os seguintes produtos:

Arroz

Feijão

Sabão em Pó

Detergente

Suponhamos que o Arroz e o Feijão sejam dispostos na Prateleira 1 e o Sabão em Pó e Detergente na Prateleira 2. Assim, a cópia de contagem para estoque ficaria assim:

Prateleira 1

Arroz

Feijão

Prateleira 2

Sabão em Pó

Detergente

**Importante:** ao solicitar uma cópia agrupando o Controle/Local, o sistema emite a mensagem:

**"Para efeitos de ajuste de estoque não será possível utilizar esta cópia mediante as marcações de agrupamento de controle\local. Deseja continuar?".**

#### Seção Copiar consignação

Efetuando a marcação **"de venda"**, será feita a cópia dos itens consignados nas operações de venda. Esta marcação é habilitada quando o parâmetro **"TOPs p/ consignação de venda - TOPCONSIGV"** possuir algum valor.

A marcação **"de compra"** quando efetuada, fará a cópia dos itens consignados nas operações de compra. É uma marcação habilitada quando o parâmetro "TOP para consignação de Compra - TOPCONSIGC" possuir algum valor.

#### Botão Executar Cópia

Após a configuração desejada dos filtros, acione o botão **"Executar Cópia"** para efetuar a cópia. Caso seja executada uma Cópia de Estoque que já tenha sido realizada naquele dia, será apresentada a seguinte mensagem:

**"Já existe uma cópia feita na data "XX/YY/ZZZZ" para a empresa "W". O que deseja fazer?"**

A partir desta mensagem, poderá escolher uma das opções abaixo:

- Substituir pela nova cópia;
- Somar com a cópia anterior.

Para Substituir pela nova cópia é necessário que o parâmetro **"Exclui contagem ao exlcuir a cpia? - INVEXCCONTCOPIA"** esteja ligado, para que a [Contagem de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694) também seja substituída por uma nova cópia.

#### Parâmetros que influenciam nesta rotina

**Se o parâmetro "TOPs a serem somadas a cópia de estoque - TOPEXCCOPIA"** estiver preenchido, o sistema fará uma cópia dos itens cujas TOPs estejam na lista informada no referido parâmetro e que o **"Nro. Único"** da nota seja maior que o valor do parâmetro **"Num. Início(TGFNum) do controle de estoque - INICIOCONTEST"**, que a data utilizada através das marcações Usar data Entrada/Saída para filtro ou Usar Dt.Negociação para TOPs de livro de saída esteja dentro do número de dias informado no parâmetro **"Dias retroação das TOPs somadas a cópia de estoque - DIASRETEXCCOP"**.

#### Assistente de Filtros

Você poderá estabelecer um **"Filtro Personalizado"** a partir do assistente de filtros, disponibilizado no topo da tela, que permite inclusive, entre outros critérios, a cópia de estoque por **"Marca"** de Produto, para o ajuste de inventário.

**Observação:** o filtro por **"Marca"**, se localiza em **"Assistente para a criação de filtros > Ligações Produto (clicar em Produto) > Campo Produto (clicar em Marca)"**.

![Imagem 3: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16252749303319) Acesse também:

[Ajuste de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633)

[Contagem de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694)
