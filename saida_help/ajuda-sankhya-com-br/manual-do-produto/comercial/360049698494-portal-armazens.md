---
id: "360049698494"
titulo: "Portal Armazéns"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-09-01T13:50:29Z"
rotulos: ["WMS", "Parceiro", "Faturamento", "Contrato", "Movimentação Financeira", "Estoque", "br.com.sankhya.mgeamz.portal.armazens", "Gerenciamento Eficiente no Portal Armazéns", "NF Depósito", "Movimentações de armazenagem", "Armazéns"]
---

# Portal Armazéns

```
 Módulo: Comercial > Consulta                   Versão disponível: A partir da 4.3
```

---

As movimentações de armazenagem dos Armazéns Gerais ficarão concentradas nesta tela.

![Imagem 1: As movimentações de armazenagem dos Armazéns Gerais ficarão concentradas nesta tela.](https://ajuda.sankhya.com.br/hc/article_attachments/9911841140119)

Estas movimentações estão vinculadas à diferentes Tipo de Movimentos. Sabendo disso, teremos:

- [Pedido de Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#pedidodearmazenagem);
- [Entradas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#entradas);
- [NF Depósito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#nfdep%C3%B3sito);
- [Pedido de Devolução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#pedidodedevolu%C3%A7%C3%A3o);
- [Saídas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#sa%C3%ADdas);
- [Faturamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#faturamento).

**Observação:** não é possível selecionar no Painel de Filtros, no campo **"Contrato de Armazenagem"** os contratos da modalidade **"Comercialização"**.

## Pedido de Armazenagem

Este movimento será necessário para gerar a sequências das movimentações, sendo assim, ele será lançado na Central de acordo com as informações cadastradas no contrato do parceiro e, a partir dele, serão faturados os lançamentos do Tipo de Movimento **"Entradas"**.

**Importante:** Este Tipo de Movimento ainda não pode ser utilizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#top)

## Entradas

Para este Tipo de Movimento temos duas operações, são elas:

**NF de Transporte:** Esta NF será gerada a partir do Pedido de Armazenagem com quantidade aproximada ao carregamento, para que o transportador possa transitar com a carga. Quando este chegar ao Armazém, será realizada a pesagem e classificação do produto sobre essa NF e, posteriormente, a geração do romaneio de entrada com a quantidade líquida (Peso Bruto - Tara - Descontos de Classificação).

**Importante:** Esta operação ainda não pode ser utilizada.

**Romaneio:** O romaneio será gerado a partir da tela [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054-Pesagem) e lançado automaticamente no Portal Armazéns.

Há a possibilidade de um romaneio ser desmembrado em mais de uma nota para diferentes parceiros de diferentes contratos. Assim, considere o exemplo:

Temos um Produtor que precisa enviar apenas uma pequena quantidade de grãos para completar seu contrato, porém, a quantidade não encherá o caminhão; assim, um outro produtor irá completar essa carga restante do veículo. Ao chegar no Armazém, um romaneio com a pesagem e a classificação da carga será realizado e, assim, poderá ser feito o seu desmembramento conforme as quantidades entregues por cada produtor.

Neste Tipo de Movimento estarão disponíveis no botão ![Imagem 2: Neste Tipo de Movimento estarão disponíveis no botão "Outras opções" , as opções "Pesagem" e "Laudo" que, ao serem…](https://ajuda.sankhya.com.br/hc/article_attachments/16336290012823) **"Outras opções"**, as opções **"Pesagem"** e **"Laudo"** que, ao serem acionadas, irá direcioná-lo para a tela de [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054) ou de [Laudo de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074) contextualizando respectivamente nos tickets ou laudos de classificação aos quais as notas estão vinculadas. Caso não encontre um ticket ou laudo para a referida nota, será exibida uma mensagem informando que não há Pesagem ou Laudo vinculado a ela. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#top)

## NF Depósito

Trata-se do efetivo documento fiscal de entrada dos produtos no armazém gerados a partir dos romaneios de entrada com o peso ajustado. Poderá existir a geração de uma NF Depósito para vários romaneios ou uma NF para cada um, conforme definição do Armazém.

Destas poderão ser gerados os movimentos **"Pedidos de Devolução"** e **"Saídas"**.

**Importante:** O Tipo de Movimento Pedidos de Devolução ainda não pode ser utilizado.

**Observação:** Com a NF Depósito selecionada, ao clicar no botão **"Faturar"** será exibido um pop-up de mesma nomenclatura. Nele, temos o campo **"Parceiro Destinatário**", que será exibido conforme as seguintes condições:

- Se a TOP informada for do tipo **"2 - Pedido de Devolução"** e estiver configurada com a opção **"Warrant"** ou **"Procuração"** no campo **"Tipo de Movimento de Armazenagem"** da aba [Armazéns](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaarmaz%C3%A9ns), a informação do campo Parceiro Destinatário será obrigatoriamente solicitada no próximo passo, sendo que, essa informação será exibida no cabeçalho do pedido gerado.
- Caso a TOP informada seja do tipo **"3 - Saídas"** ou **"2 - Pedido de Devolução"** e esteja com a opção **"PD Devolução"** selecionada no campo Tipo de Movimento de Armazenagem da aba Armazéns, o campo Parceiro Destinatário não será solicitado no próximo passo do pop-up e assim, você conseguirá confirmar no faturamento.

---

A NF Depósito pertencerá a uma Transferência de Propriedade quando estiver lançada na tabela TGAHTP, campo NUNOTAENT (Nº Único da NF de Depósito). Desse modo, para confirmá-la, serão feitas as seguintes validações:

1 - A NF de Saída desta transferência também deverá estar confirmada.

2 - Caso a NF de Saída referente à esta transferência não esteja confirmada, será exibido um alerta informando que a referida nota deve ser confirmada previamente.

Para excluir ou cancelar uma NF Depósito vinculada à uma Transferência de Propriedade, a NF de Saída pertencente à mesma transferência também será excluída conforme as validações:

1 - Ao cancelar a NF Depósito com a NF de Saída confirmada, será apresentada a mensagem abaixo:

**"A nota com Nº Único XX faz parte da Transferência de Propriedade Nº X. Portanto, a Nota de Saída com Nº Único XXX, que também faz parte da transferência, será cancelada. Deseja continuar?"**

- Se escolher **"Não"**, a operação será cancelada.
- Ao clicar em **"Sim"**, o sistema excluirá a nota de Entrada e em seguida, irá cancelar a de nota de Saída, passando por todas as validações já existentes na Central.
- Caso haja algum impedimento para excluir a nota de Entrada ou cancelar a nota de Saída, a operação não será finalizada.
- Não havendo impedimento, será exibido o pop-up para informar o motivo do cancelamento. Se **"Fechar"** este pop-up, desfaz toda a operação. Ao informar o motivo e clicar em **"OK"**, o cancelamento da nota será finalizado.

2 - Caso a NF de Saída não esteja confirmada, o sistema irá sinalizar que a exclusão/cancelamento será efetivada após a confirmação da seguinte mensagem:

**"A nota com Nº Único XX faz parte da Transferência de Propriedade Nº X. Portanto, a Nota de Saída com Nº Único XXXX, que também faz parte da transferência, será excluída. Deseja continuar?"**

- Ao clicar em **"Não"** a operação será cancelada.
- Se clicar em **"Sim"**, ambas as notas serão excluídas, passando por todas as validações já existentes para isso na Central.
- Caso haja algum impedimento para excluir alguma das notas, a operação não será finalizada.
- Se as notas forem excluídas, será apresentada a mensagem de sucesso na exclusão.

3 - Caso a NF Depósito não pertença à nenhuma Transferência de Propriedade, ela será excluída normalmente.

**Nota:** Esta implementação foi desenvolvida apenas para o layout HTML5.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#top)

## Pedido de Devolução

A geração desse pedido ocorrerá a partir da seleção das NF's de Depósito, quando o cliente manifestar interesse em retirar seu produto contendo a quantidade total para a retirada. A partir desse pedido, as notas fiscais de saída do armazém serão geradas conforme cada operação.

**Importante:** Este Tipo de Movimento ainda não pode ser utilizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#top)

## Saídas

Este Tipo de Movimento ocorrerá a partir do Pedido de Devolução ou da NF Depósito. Serão geradas as notas fiscais de devolução de armazenagem com a quantidade exata a ser devolvida para o cliente. Quando a quantidade total for devolvida, o processo de armazenagem será finalizado.

A nota de Saída será vinculada à uma Transferência de Propriedade quando estiver lançada na tabela TGAHTP, campo NUNOTASAI (Nº Único da nota de saída).

Se desejar excluir ou cancelar um lançamento que esteja vinculado a uma Transferência de Propriedade, será apresentada a seguinte mensagem:

**"A nota com Nº Único XX faz parte da Transferência de Propriedade Nº XXX .Neste caso, esta operação deve ser feita a partir da exclusão ou cancelamento da Nota de Entrada Nº Único XX."**

Ao clicar em **"OK"**, mesmo que mais de uma nota tenha sido selecionada, a operação não será realizada. Sendo necessário excluir primeiramente a nota de Entrada.

Caso a NF Saída não pertença à uma Transferência de Propriedade, ela será excluída normalmente.

**Nota:** Esta implementação foi desenvolvida apenas para o layout HTML5.

Neste Tipo de Movimento, se o cliente tiver a licença do Opcional **[30935 - Comercialização de Grãos/W]**estarão disponíveis no botão ![Imagem 3: Neste Tipo de Movimento , se o cliente tiver a licença do Opcional (30935 - Comercialização de Grãos/W) estarão…](https://ajuda.sankhya.com.br/hc/article_attachments/16336290012823) **"Outras opções"**, as opções **"Pesagem"** e **"Laudo"** que ao serem acionadas, irá redirecioná-lo para a tela de [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054) ou de [Laudo de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074) contextualizadas nos respectivos tickets aos quais as notas estão vinculadas. Caso não encontre um ticket para a referida nota será exibida uma mensagem informando que não há Pesagem ou Laudo vinculado a ela. Essa consulta também não é permitida para múltiplas notas. 

Quando a nota é **criada manualmente pela Central**, sem passar pela tela de Pesagem, a **validação de estoque não é realizada**, pois a Central/Portal não possui contexto suficiente para efetuar essa verificação. O fluxo correto para garantir a validação de estoque é a **emissão da nota pela tela de Pesagem**.

![Imagem 4: Nos casos em que o Pedido de Devolução realiza baixa de estoque, isso ocorre porque a TOP utilizada para a devolução…](https://ajuda.sankhya.com.br/hc/article_attachments/33846093751319) Nos casos em que o **Pedido de Devolução** realiza baixa de estoque, isso ocorre porque a TOP utilizada para a devolução está configurada com a opção **"Baixar"** no campo **"Atualização do Estoque"**. Dessa forma, ao gerar a nota de devolução, o sistema realiza a baixa no saldo disponível.
Se não for desejada a baixa de estoque, é necessário **ajustar a configuração da TOP**, alterando o campo **"Atualização do Estoque"** para a opção **"Nenhum"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#top)

## Faturamento

No faturamento, deverão ser configuradas as TOP's para faturamento das notas de serviços de expedição/recepção e armazenagem, relacionadas ao armazém. Este faturamento poderá ser realizado manualmente ou por meio da tela **"Apuração/ Faturamento de Contratos"**.

Com o parâmetro ARMATUALFINFAT ("Atualiza finalidade da operação no faturamento no módulo de armazéns") ativado, ao faturar uma nota originada no módulo de Armazéns (romaneio de entrada, depósito de pesagem e similares), o sistema copia o NUFOP (Número da Finalidade de Operação) configurado na TOP de faturamento para o cabeçalho da nota gerada, desde que o NUFOP esteja informado na TOP. Esse parâmetro atua de forma independente do parâmetro geral ATUALFINFAT ("Atualiza finalidade da operação no faturamento"), permitindo habilitar a atualização do NUFOP exclusivamente para operações de armazém, sem impactar os demais fluxos de faturamento do sistema.

**Observação:** O NUFOP só é atualizado se estiver configurado na TOP.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns#top)
