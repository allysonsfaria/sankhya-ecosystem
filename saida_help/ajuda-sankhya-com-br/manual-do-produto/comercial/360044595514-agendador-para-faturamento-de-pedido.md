---
id: "360044595514"
titulo: "Agendador para Faturamento de Pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595514-Agendador-para-Faturamento-de-Pedido"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:20:19Z"
rotulos: ["manual", "Configuração", "Faturamento", "Portal de Vendas", "Agendamento", "br.com.sankhya.com.rotinas.agendfaturamentopedido", "Agendador para Faturamento de Pedido manual", "TOP", "NFS-e", "Agendador Faturamento Pedido"]
---

# Agendador para Faturamento de Pedido

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311710561815) Módulo: Comercial > Avançado > Agendadores
```

---

Esta rotina permite que você determine o agendamento necessário para realização do faturamento de pedidos de notas de forma automática. Assim, são geradas notas fiscais de serviço já confirmadas, que serão enviadas para a prefeitura. É necessário ressaltar que, somente serão faturados os pedidos que estiverem confirmados e pendentes.

Este agendador ignora qualquer tipo de erro durante o faturamento, confirmação da nova nota de venda e envio da NFS-e para a prefeitura, ou seja, caso seja apresentado algum erro ao criar e confirmar a nota, o sistema passa para o próximo pedido. As notas que foram faturadas e confirmadas com sucesso e são uma NFS-e, serão separadas em lote e enviadas para o servidor da prefeitura, entretanto, o sistema não irá buscar autorização neste momento.

As NFS-e enviadas, serão inseridas na rotina de [Notas Pendentes de Autorização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612174-Notas-Pendentes-de-Autoriza%C3%A7%C3%A3o). Nesta rotina, ocorre a consulta da situação do lote até o servidor da prefeitura retornar que o lote foi processado, caso a NFS-e seja aprovada ou o lote seja rejeitado, o sistema retira a nota dessa rotina e qualquer tratativa deve ser tomadas a partir do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#impressonoportaldevendas).

**Nota:** Esta tela não permite a impressão de NFS-e aprovadas; caso seja necessário, realize através do Portal de Vendas.

Inicialmente, efetue as seguintes configurações:

O "**Nro. agendamento"** corresponderá à identificação do agendamento.

Informe em **"Descrição agendamento"** o nome do agendamento a ser executado.

A marcação **"Ativo"** determina se o agendamento está ativo ou não, ou seja, se poderá ou não ser utilizado.

O campo **"Gerar Lote para"** determina qual o lote fiscal que será emitido no agendamento. Sendo assim, para agendamento de serviços, utilize a opção **"NFSe"** e, para agendamento de produtos, use **"NFe"**.

![Imagem 2: Certifique-se de observar o uso do produto para definir corretamente a opção, pois ao utilizar a opção inadequada, os…](https://ajuda.sankhya.com.br/hc/article_attachments/25996274440215) Certifique-se de observar o uso do produto para definir corretamente a opção, pois ao utilizar a opção inadequada, os pedidos gerados podem não ser faturados automaticamente.

**Observação:** após definir a opção no campo acima, será criada uma seção de igual nome na aba [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595514-Agendador-para-Faturamento-de-Pedido#abaconfiguraes).

A emissão do faturamento das NFS-e será realizada em lotes, sendo que para cada pedido será gerado uma respectiva nota, ou seja, não haverá agrupamento.

**Nota:** quando tiver um pedido que contenha produto e serviço, a rotina não irá faturar e gerar lotes de NFe ou NFSe; para isso, o operador deve fazer o faturamento manual pelo Portal de Vendas.

Em **"Status Última Execução"**, você poderá visualizar o status da última execução realizada.

[Aba Horários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595514-Agendador-para-Faturamento-de-Pedido#abahorrios)                                          [Aba Frequência Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595514-Agendador-para-Faturamento-de-Pedido#abafrequnciaagendamento)

[Aba Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595514-Agendador-para-Faturamento-de-Pedido#abaconfiguraes)

## Aba Horários

Nesta aba, configure o período em que será realizada a próxima execução do faturamento, como também a data final desta execução.

![Imagem 3: Nesta aba, configure o período em que será realizada a próxima execução do faturamento, como também a data final desta…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019852741)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595514-Agendador-para-Faturamento-de-Pedido#top)

## Aba Frequência Agendamento

Nesta aba, temos as configurações pertinentes à frequência do agendamento, abaixo trataremos sobre cada uma delas:

- Você pode intercalar o agendamento dentre uma ou várias execuções, em um horário específico;
- Indique em qual mês ocorrerá o agendamento; podendo ser em um determinado mês, acima de um ou todos os meses;
- De acordo com a configuração executada no item acima, será configurada a frequência do agendamento, de acordo com as seguintes formas:

1. **Diário:** Ao optar por esta opção, a frequência será efetuada todos os dias da semana;
2. **Semanal:** Nesta opção de frequência, determine um dia da semana acima de um ou todos os dias da semana;
3. **Mensal:** Configure por meio desta opção, um dia específico do mês para realizar o agendamento, acima de um ou todos os dias do mês.

![Imagem 4: Mensal: Configure por meio desta opção, um dia específico do mês para realizar o agendamento, acima de um ou todos os…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019852801)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595514-Agendador-para-Faturamento-de-Pedido#top)

## Aba Configurações

![Imagem 5: Aba Configurações](https://ajuda.sankhya.com.br/hc/article_attachments/1500019853241)

Referente ao campo **"E-mail Notificações"**, destacamos que a configuração deste será opcional e, caso este seja configurado, será enviado por e-mail um informativo com a quantidade de pedidos encontrados para faturamento, a quantidade de notas geradas e a quantidade de notas que ficaram pendentes de autorização.

O **"Filtro"** possibilita realizar a busca dos pedidos a serem faturados.

Por meio do campo **"Ordenação"**, será definida a ordem dos pedidos para confirmação dentre as seguintes opções:

- Do mais novo para mais velho;
- Do mais velho para o mais novo.

A **"Série da nota"** será utilizado para definir a série da nota que será criada.

Informe em **"Tipo de Operação"** a TOP que será utilizada na nota de venda, caso a TOP do pedido não tenha uma **"TOP p/ Faturamento"** configurada. A preferência será da TOP de faturamento do pedido.

A **"Quantidade de pedidos por lote"** indicará qual será a quantidade de pedidos do lote que será processada. Sendo que, quando não preenchido, o padrão será a quantidade de 50 pedidos.

Conforme a opção selecionada no campo **"Gerar Lote para"** do Painel Principal, será exibida uma nova seção na aba Configurações. Se escolhida a opção **"NFS-e"**, apresenta-se a seção de igual nome. Caso seja escolhida a opção **"NF-e"**, será exibida essa seção na aba.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595514-Agendador-para-Faturamento-de-Pedido#top)
