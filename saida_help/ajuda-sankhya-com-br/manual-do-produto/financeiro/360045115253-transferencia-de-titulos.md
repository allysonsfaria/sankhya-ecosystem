---
id: "360045115253"
titulo: "Transferência de Títulos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:44:15Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contas", "Movimentação Financeira", "Cheques", "Financeiro", "Contas Bancárias", "Transferência de Títulos", "br.com.sankhya.fin.rotinas.transferenciatitulos", "Transferência de Títulos manual", "Transferência entre empresas/contas.", "Filtros: títulos baixados ou pendentes.", "Ajustar dados para confirmar transferência."]
---

# Transferência de Títulos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312448744855) Módulo: Financeiro> Rotinas
```

---

Esta tela será utilizada para a transferência de numerários entre empresas e contas bancárias. Assim, têm-se as seguintes considerações:

- Nesta tela, pode-se filtrar os títulos como **"Baixados"** e **"Pendentes"** conforme a marcação das opções, **"Pode transferir título pendente?"** e **"Pode transferir depois de baixado?"** no cadastro do [Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top), aba [Transferência de Cheques/Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abatransfernciadechequesttulos).
- É importante ressaltar que as marcações Pode transferir título pendente? e Pode transferir depois de baixado? têm o objetivo de filtrar os dados apresentados nesta tela, e não de conceder permissão para executar a transferência. Dessa forma, é recomendável que após qualquer operação de baixa e/ou estorno, o usuário responsável pela transferência reaplique os filtros, garantindo que a regra seja aplicada.
- O parâmetro **"Qtd de dias após a baixa permitido p/transf.? - DIASTRANSBX"** indicará o número de dias após a data da baixa que um título poderá ser transferido de conta.

Dada as configurações, você pode consultar a seguir as funcionalidades dessa tela:

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos#paineldefiltros)                                      [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)

[Transferência de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos#transfer%C3%AAnciadet%C3%ADtulos)                           [Como corrigir uma transferência errada?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos#comocorrigirumatransfer%C3%AAnciaerrada?)

![Imagem 2: Transferência de Títulos Como corrigir uma transferência errada?](https://ajuda.sankhya.com.br/hc/article_attachments/360098715953)

## Painel de Filtros

**Filtrar os títulos:** Poderá ser escolhida a opção **"Baixados"** ou **"Pendentes"**.

- Se marcado a opção Baixados, as caixas de seleção abaixo deste campo serão desabilitadas, e estarão marcadas as opções Receitas e Baixados.
- Se marcado Pendentes as caixas de seleção Receitas, Despesas, Pendentes e Baixados ficam habilitadas e possíveis de marcação.

[GIF animado: Imagem 3: Se marcado Pendentes as caixas de seleção Receitas , Despesas , Pendentes e Baixados ficam habilitadas e possíveis de…](https://ajuda.sankhya.com.br/hc/article_attachments/360098739853)

Referente aos campos **"Nro. Cheque"** ou **"Nro. Nota"**, se em **"Filtrar os títulos"** estiver selecionado Baixados, ele trará como descrição Nro. Cheque, senão, trará Nro. Nota. Neste campo, você poderá informar um Nro. Cheque ou Nro. Nota como critério de filtro.

Em **"Conta bancária"**, teremos a conta bancária que será a origem do lançamento bancário de transferência.

Para incluir cheques utilizando o código **"CMC7"**, utiliza-se esse campo. Ao clicar no botão ![Imagem 4: Para incluir cheques utilizando o código "CMC7" , utiliza-se esse campo . Ao clicar no botão "Incluir título pelo CMC7…](https://ajuda.sankhya.com.br/hc/article_attachments/16584950110231) **"Incluir título pelo CMC7 na lista de selecionados"**, o sistema enviará o título diretamente para a grade inferior da tela.

Referente aos campos **"Período de lançamento"** ou **"Período de Vencimento"**, se em **"Filtrar os títulos"** estiver selecionado Baixados, informar a data de lançamento do movimento bancário. Se em **"Filtrar os títulos"** estiver selecionado **"Pendentes"**, informar a data de vencimento do título. 

Depois de feitos os filtros, clique em **"Aplicar"**.

Os títulos serão apresentados na grade **"Títulos Disponíveis"** para seleção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos#top)

## Botão Outras Opções...

O botão **"Outras opções..."** está localizado na barra de ferramentas da grade "Títulos Disponíveis" e possui as seguintes opções:

![Imagem 5: O botão "Outras opções..." está localizado na barra de ferramentas da grade " Títulos Disponíveis" e possui as…](https://ajuda.sankhya.com.br/hc/article_attachments/360082739114)

Quando marcada, a opção **"Usar o Valor Cheque"** totalizará pelo valor do cheque. Se desmarcada, será utilizado o valor do lançamento ao efetuar a transferência.

Na visualização do relatório, ao confirmar a transferência trará como valor o **"Valor do Cheque"**, caso não marcado, aparecerá o **"Valor de Desdobramento do Título"**.

Caso a opção **"Exigir troca do Tipo de Título na primeira transf.?"** esteja selecionada, na primeira transferência, o sistema só permitirá transferir um título para outra conta mudando o Tipo de Título.

Caso você tente realizar a transferência com o mesmo título, o sistema emitirá a mensagem:

**"O Financeiro já está com este Tipo de Título! Transferência cancelada.".**

Uma vez transferido o título, não será permitido fazer o Estorno. Caso você tente fazê-lo o sistema apresentará a seguinte mensagem:

**"O título número 0000 foi movimentado por uma Transferência de Cheque. Não pode ser estornado."**

O sistema ainda emitirá uma mensagem, se você tentar transferir um título para a mesma Conta.

Quando os títulos não estiverem baixados, será alterada a conta do Financeiro e não será feita transferência de numerário.

Se desmarcado, a opção **"Transferir Títulos Baixados Separadamente"** irá gerar um único lançamento na **"Movimentação Bancária"** para todos os títulos selecionados para transferência.

Então, o sistema apresentará em forma de relatório todos os títulos que foram transferidos. Assim, você poderá optar por imprimi-los ou não.

Caso esta opção esteja marcada, o sistema irá gerar um lançamento na **"Movimentação Bancária"** para cada título transferido. Haverá a apresentação de todas as transferências realizadas e você será questionado se quer visualizar o resumo da transferência ou não.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos#top)

## Transferência de Títulos

Após aplicar o **"Filtro"** o sistema exibirá os títulos na grade **"Títulos Disponíveis"**.

Os títulos que serão transferidos deverão estar na grade **"Títulos Selecionados"**.

Aqui, pode-se também remover itens selecionados da grade ou ainda remover os não selecionados:

[GIF animado: Imagem 6: Aqui, pode-se também remover itens selecionados da grade ou ainda remover os não selecionados:](https://ajuda.sankhya.com.br/hc/article_attachments/360082743114)

Além disso, para selecionar vários títulos juntos segure a tecla **"Ctrl"** do seu teclado e selecione os registros desejados com o mouse.

Após selecionar os títulos desejados, clique no botão **"Selecionar Títulos"**.

Ao clicar no botão **"Confirmar"** localizado no rodapé da grade **"Títulos Selecionados"** o sistema abrirá a janela com as opções para serem configuradas:

![Imagem 7: Ao clicar no botão " Confirmar" localizado no rodapé da grade " Títulos Selecionados" o sistema abrirá a janela com as…](https://ajuda.sankhya.com.br/hc/article_attachments/360082844574)

No pop up teremos:

A **"Data Transferência"** para a transferência dos valores, que será registrada no campo "Dt. Lançamento" da movimentação bancária.

Insira em **"Conta Destino"** a conta para onde o título será transferido. Este será gravado no campo Conta Destino da Movimentação Bancária.

O **"Tipo de Título"** para o qual será alterado.

Digite em **"TOP de Transf.:"** o código da TOP de transferência que será registrada na movimentação bancária gerada.

Em **"Lançamento Origem"** insira o código do histórico de lançamento bancário que será registrado no campo lançamento origem da movimentação bancária.

No campo **"Lançamento Destino"** insira o código do histórico de lançamento bancário que será registrado no campo Lançamento destino da movimentação bancária.

Referente ao campo **"Histórico"** tem-se que esta será gravada no campo Histórico da Movimentação Financeira.

Ao clicar em **"OK"**, o sistema gera um lançamento na movimentação bancária, com os dados informados na tela de **"Transferência de Títulos"**.

**Observações:**

- Quando você realizar a exclusão uma movimentação bancária oriunda de uma transferência de títulos, o sistema retornará ao título original o código da empresa de baixa e código do tipo de título de origem.
- Os títulos que foram movimentados por uma transferência de títulos não poderão ser estornados.
- As informações sobre as transferências de títulos são registradas na tabela TGFTRC.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos#top)

## Como corrigir uma transferência errada?

O sistema não permite fazer a Transferência de um cheque mais de uma vez.

Caso você faça uma Transferência errada, ele deverá ir à tela de [Movimentação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653 "Movimentação Bancária ") e excluir a Transferência, com isto o sistema permitirá que o título seja apresentado novamente nesta rotina e assim, que você possa transferi-lo novamente. Mas atenção, se não for transferência de títulos já baixados estes não serão apresentados na Movimentação Bancaria, pois para existir uma Movimentação Bancária de fato, precisa ter existido a baixa gerando a gravação do número 'NUBCO'.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115253-Transfer%C3%AAncia-de-T%C3%ADtulos#top)
