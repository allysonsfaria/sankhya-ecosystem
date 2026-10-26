---
id: "360045107333"
titulo: "Pesagem Avulsa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107333-Pesagem-Avulsa"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:27:51Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "WMS", "Produto", "Parceiro", "Movimentação Financeira", "br.com.sankhya.armazem.cad.pesagem.avulsa", "Pesagem Avulsa manual", "Pesagem Avulsa Registro Painel de Filtros", "Pesagem Avulsa: Registro Flexível de Pesagens", "Pesagem"]
---

# Pesagem Avulsa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311935645719) Módulo: Comercial > Rotinas                   ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311935646615) Versão disponível: A partir da 4.3
```

---

Por meio desta tela, o sistema permitirá que o registro de pesagens não vinculadas ao contrato de armazéns seja realizado.

Há armazéns que prestam serviços de pesagem de veículos com cargas de diversas naturezas, e estas podem não estar relacionadas especificamente à sua atividade principal. Assim, teremos disponível:

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107333-Pesagem-Avulsa#paineldefiltros)                                                                                            [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107333-Pesagem-Avulsa#painelprincipal)

[Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107333-Pesagem-Avulsa#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)

![Imagem 3: Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/4412898148119)

## Painel de Filtros

Você terá disposto nesta tela o **"Painel de Filtros"**, em que teremos os **"Filtros Personalizados"** onde pode-se personalizar os filtros de acordo com a sua preferência, e os **"Filtros rápidos"** em que você poderá filtrar os registros por meio dos campos **"Data do Movimento"**, **"Veículo"**, **"Parceiro"**, **"Motorista"**, **"Produto"**, **"Empresa"**, além do campo **"Status da Pesagem"** que filtrará os registros que estiverem com os status a seguir:

- Aberto;
- Pesagem Concluída;
- Aguardando Pesagem Final;
- Pesagem Fechada;
- Pesagem Cancelada.

E o campo **"Tipo de Pesagem"** que, assim como aquele mencionado acima, filtrará os registros que estarão com o Tipo de Pesagem de acordo com as opções **"Pesagem Carga"**, **"Pesagem Descarga"** e **"Pesagem Única"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107333-Pesagem-Avulsa#top)

## Painel Principal

No Painel Principal da tela Pesagem Avulsa tem-se disposto os campos:

O **"Ticket"** será um campo com numeração automática e sequencial sendo este, atribuído à indicação do número de pesagem registrada.

Se a marcação **"Pesagem manual"** estiver habilitada, permitirá que você realize o registro manual das informações de **"Peso Bruto"** e **"Tara"**. Uma vez desabilitado, a captura do peso só ocorrerá de automaticamente por meio da integração com a Balança.

**Observação:** Este recurso será liberado por usuário, na opção **"Permite pesagem manual?"** no [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) desta tela.

No campo **"Tipo de Pesagem"** você poderá definir que tipo de operação está envolvido na pesagem, desta forma, teremos:

- **Pesagem Carga:** Nesta opção, inicialmente você deverá registrar a **"Tara"** (Veículo descarregado) e depois do carregamento do produto, é preciso registrar o **"Peso Bruto"** do veículo, chegando então ao resultado do **"Peso Líquido"**, que equivale ao peso da carga carregada no veículo;
- **Pesagem Descarga:** Por meio desta, deve-se primeiramente registrar o Peso Bruto (Veículo carregado) e depois que a descarga do produto for realizada, deve-se registrar a Tara, chegando assim ao resultado do Peso Líquido, que representa o peso da carga descarregada do veículo;
- **Pesagem Única:** Ao selecionar esta opção, será permitido apenas o registro do Peso Bruto apontado na balança em que não há o envolvimento de carga e descarga de produtos.

No campo **"Balança"**, você selecionará a balança que será utilizada para realizar a captura conforme aquelas que forem cadastradas no [Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection), aba [Integração Balança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#abaintegra%C3%A7%C3%A3obalan%C3%A7a), caso a marcação **"Múltiplas Balanças"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#abageral) esteja habilitada. Se esta estiver desmarcada, o campo Balança ficará desabilitado com a descrição **"Balança Padrão"**. 

**Nota:** se a marcação Pesagem manual estiver marcada, o campo ficará desabilitado.

O campo **"Status da Pesagem"** exibirá o status da pesagem à medida que houver movimentações no processo de pesagem. Assim, teremos as opções:

- **Aberto:** Esta informará que a pesagem foi aberta e não há nenhum registro de captura de peso no sistema;
- **Aguardando Pesagem Final:** Por meio deste, informa-se que a pesagem já possui uma captura de peso registrado no sistema, sendo esta o Peso Bruto ou Tara, de acordo com o Tipo de Pesagem selecionado, e aguarda o registro pesagem final no sistema.
- **Pesagem Concluída:** Refere-se que o processo de captura de peso já foi registrado no sistema, de acordo com do Tipo de Pesagem selecionado. Assim, ao clicar no botão ![Imagem 4: Pesagem Concluída: Refere-se que o processo de captura de peso já foi registrado no sistema, de acordo com do Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16364635810199) **"Finalizar Pesagem"** o processo será concluído.
- **Pesagem Fechada:** Informa que você já realizou a finalização do processo de pesagem.
- **Pesagem Cancelada:** este status informa que a pesagem foi cancelada.

Em seguida, informe a empresa no campo **"Cód. Empresa"** da operação.

**Nota:** É possível limitar o acesso dos usuários dessa tela para que estes possam visualizar apenas  o(s) registro(s) da(s) empresa(s) desejadas. Para tal ação, é necessário criar uma regra na tela [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es) e em seguida vincular esta no cadastro do(s) usuário(s) desejado(s) por meio da aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes).

Informe o veículo que será pesado por meio do campo **"Veículo"**. Caso não seja encontrado o cadastro do veículo, este poderá ser feito de forma simplificada através da opção **"Cad. Simplif. Veículos 'CTRL +1"** localizado no botão **"Outras Opções"**.

Em seguida, informe o **"Motorista"**. Destacamos ainda que assim como o registro do veículo, caso este não seja encontrado, o cadastro do motorista (parceiro) poderá ser feito de forma simplificada, por meio da opção **"Cad. Simplif. Parceiro 'F2'"**.

No campo **"Parceiro"** você irá inserir o parceiro envolvido na operação.

No campo **"Produto"** você indicará o produto da pesagem, porém para tal ação, não há necessidade de cadastro.

Nos campos **"Km Inicial"** e **"Km Final"** você irá inserir a quilometragem inicial e final do veículo, respectivamente.

No campo **"Km Percorrido"** teremos a quilometragem do veículo de pesagem. Este campo é o resultado do cálculo entre Km Inicial - Km Final.

Em **"Peso Declarado"** deve ser inserido o Peso informado na nota.

Você também poderá adicionar observações adicionais na pesagem em **"Observação"**.

O campo **"Peso Bruto"** carregará o Peso Bruto do veículo, a pesagem deste poderá ocorrer com ele carregado ou descarregado a depender do Tipo de Movimento da pesagem.

A **"Tara"** do veículo também poderá ser realizada com o ele carregado ou descarregado.

**Observação:** A captura automática do Peso Bruto e Tara de veículos, pode ser realizada automaticamente por meio do botão ![Imagem 5: Observação: A captura automática do Peso Bruto e Tara de veículos, pode ser realizada automaticamente por meio do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/15633999686423).

O **"Peso Líquido"** refere-se à subtração da Tara sobre o Peso Bruto (Peso Bruto - Tara = Peso Líquido).

Os campos **"Nome Usuário Peso Bruto"** e **"Nome Usuário Tara"** será gravado os nomes dos usuários que realizaram a captura do Peso Bruto e Tara, respectivamente.

Além disso, nos campos **"Balança Peso Bruto"** e **"Balança Tara"** serão exibidos os nomes das balanças utilizadas nas pesagens do Peso Bruto e Tara, respectivamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107333-Pesagem-Avulsa#top)

## Botão Outras Opções...

Para acessar o menu Outras Opções..., basta você clicar no botão ![Imagem 6: Para acessar o menu Outras Opções... , basta você clicar no botão no topo da tela. Assim, o sistema disponibilizará a…](https://ajuda.sankhya.com.br/hc/article_attachments/360074901334) no topo da tela. Assim, o sistema disponibilizará a você as opções:

(4)** Configurar balança:** Ao selecionar esta, será aberto o pop-up **"Configuração de Balança"** em que deverá ser informada a **"URL"** de comunicação com a balança vinculada ao Web Connection.

A URL a ser inserida no campo URL, deverá ter a estrutura ws://IP da Máquina:9098/balanca/pesagem, em que o **"IP da Máquina"** refere-se ao IP da máquina que a balança e o Web Connection estão instalados.

**Observação:** A configuração deste poderá ser realizada para qualquer balança do tipo serial. Além dos campos presentes na **"Integração balança"**, é preciso verificar no manual da balança as informações pertinentes aos campos **"Expressão para captura do peso"**, **"Início da string de leitura"**, **"Fim da string de leitura"** e **"Casa decimal"**.

(4)** Cad. Simplif. Veículos 'CTRL +1':** Ao selecionar esta, o sistema exibirá o pop-up **"Cadastro simplificado Veículo"** onde você poderá realizar o cadastro de Veículos de maneira mais eficiente.

(4)** Cad. Simplif. Parceiro 'F2':** Por meio desta, você poderá realizar o cadastro de Parceiros quando o pop-up **"Cadastro de Simplificado de Parceiros"** for exibido na tela.

As opções abaixo só poderão ser preenchidas caso a marcação **"Permite limpar informações de pesagem avulsa"** na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) for definida aos usuários selecionados:

(4)** Limpar Peso Bruto:** ao selecionar esta opção, as informações inseridas na pesagem avulsa referente ao Peso Bruto serão excluídas. Essa ação é possível apenas se a Pesagem Avulsa estiver com Status diferente de **"Pesagem Fechada"**.

(4)** Limpar Tara:** ao selecionar esta opção, as informações inseridas na pesagem avulsa referente à Tara serão excluídas. Essa ação é possível apenas se a Pesagem Avulsa estiver com Status diferente de Pesagem Fechada.

(4)** Cancelar Pesagem:** clicando nesta opção será possível cancelar pesagens que possuam o campo Status da Pesagem diferente de Pesagem Fechada. Após cancelar uma pesagem não será possível editá-la.

**Observação:** lembre-se que para selecionar esta opção é necessário liberar o acesso habilitando a marcação **"Permite cancelar pesagem avulsa"** da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) (Módulos>Comercial>Rotinas>Pesagem Avulsa).

**Nota:** ao cancelar uma pesagem, o botão ![Imagem 7: Nota: ao cancelar uma pesagem, o botão Finalizar Pesagem ficará desabilitado.](https://ajuda.sankhya.com.br/hc/article_attachments/16364635810199) Finalizar Pesagem ficará desabilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107333-Pesagem-Avulsa#top)
