---
id: "37673233640343"
titulo: "Como controlar o fluxo de aprovação e liberar limite de crédito mensal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37673233640343-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-limite-de-cr%C3%A9dito-mensal"
trilha: "Universidade Sankhya > Jornada de Vendas"
atualizado_em: "2026-07-22T14:10:53Z"
rotulos: ["Configuração", "Parceiro", "Central de Vendas", "Portal de Vendas", "Crédito", "Financeiro"]
---

# Como controlar o fluxo de aprovação e liberar limite de crédito mensal

| Categoria |
| --- |
| [O que é o evento 15 (Limite Créd. Mensal) e por que ele é importante?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673233640343-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-limite-de-cr%C3%A9dito-mensal#h_01KEYR7VBQZGYV6K3EX47QAMEJ) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673233640343-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-limite-de-cr%C3%A9dito-mensal#h_01KEYR7GG5G6PRZB06HESZB2GD) |
| [Quais os riscos de não usar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673233640343-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-limite-de-cr%C3%A9dito-mensal#h_01KEYR73EGQ375ZYFA3D2FR0P1) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673233640343-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-limite-de-cr%C3%A9dito-mensal#h_01KFBVM8ZSFEV8HEW8QVZRZFP3) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673233640343-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-limite-de-cr%C3%A9dito-mensal#h_01KEYR40BENH3T40THXQT9NRKV) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673233640343-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-limite-de-cr%C3%A9dito-mensal#h_01KEYR4ER5GQPJG73AWBGG32W6) |

## Liberação do Evento 15 (Limite Créd. Mensal)

#### O que é o evento 15 (Limite Créd. Mensal) e por que ele é importante?

É um recurso do **ERP Sankhya** que controla o volume de compras a prazo, restringindo transações que ultrapassam o limite de crédito mensal definido para o cliente. 

Esse procedimento é essencial para prevenir inadimplências, garantir o alinhamento com o planejamento financeiro e assegurar que os limites acordados sejam respeitados. Além disso, proporciona rastreabilidade, decisões embasadas e transparência ao registrar e centralizar o processo de liberação, protegendo a saúde financeira da empresa e melhorando o controle sobre as transações comerciais.

#### Quais problemas este recurso resolve?

- **Falta de controle sobre o volume de compras mensais:** gera risco de comprometimento financeiro.
- **Aumento da inadimplência:** devido à ausência de limites claros para compras a prazo.
- **Descumprimento das políticas de crédito:** clientes excedem os limites acordados sem controle.
- **Processos de aprovação descentralizados:** dificultam o monitoramento e geram inconsistências.
- **Dificuldade para rastrear transações e liberações de crédito:** compromete a gestão comercial.
- **Tomada de decisões sem dados confiáveis:** prejudica o planejamento financeiro e estratégico.

#### Quais os riscos de não usar?

A ausência deste recurso pode resultar em uma exposição financeira desproporcional, desorganização na gestão de crédito, prejuízos ao fluxo de caixa, falta de transparência nas transações e decisões não embasadas, comprometendo a saúde financeira e o planejamento estratégico da empresa.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052403405)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Você é o gestor financeiro de uma organização que utiliza o **ERP Sankhya** para monitorar e gerenciar vendas e crédito de clientes. Um cliente possui um limite mensal de crédito estipulado em **R$20.000,00** para compras a prazo. Durante o período vigente, ele realizou dois pedidos no valor de **R$10.000,00** cada, totalizando o limite estabelecido. Posteriormente, o cliente solicita a aprovação de um terceiro pedido no valor de **R$5.000,00**, que excede o limite previamente definido.

Diante desta situação, o sistema bloqueia automaticamente o pedido e aciona a **Liberação do Evento 15**, exigindo uma análise detalhada e a aprovação de um usuário autorizado para permitir o prosseguimento da transação.

**Tarefa:** Liberar o evento 15 **(Limite Créd. Mensal)** para que o pedido seja processado, mantendo o controle financeiro e organizacional.

**Vamos praticar? Siga o passo a passo para realizar a liberação do Evento 15 (Limite Créd. Mensal) no ERP Sankhya**

1. **Parceiros**

- Acesse a tela **“Parceiros”.**
  Menu: Configurações » Cadastros »  Parceiros
- Selecionar o parceiro que irá definir o limite de crédito mensal**.**
- Na aba **Crédito**, preencha o campo **“Limite de crédito mensal”** com o valor do limite estabelecido para o cliente.
- Clique em **Salvar** para registrar as informações.

**Nota:** Ao lançar uma Nota (no ato da confirmação do Pedido/Nota), se a soma dos débitos do Parceiro forem superiores ao **Limite de Crédito** definido para o Cliente, será aberto o pop-up de solicitação de liberação. Porém, uma vez que a liberação já tenha sido realizada e o pedido confirmado, a liberação de limites não será solicitada novamente mesmo que haja alteração nos produtos do pedido.

2. **Registrar um pedido de venda**, assegurando a precisão das informações da operação nos campos essenciais, como tipo de negociação, parceiro e valor (excedendo o limite configurado).

- Certifique-se de que o **Tipo de Negociação** utilizado no pedido está configurado para pagamento **‘a prazo’**.

3. **Geração do evento 15**

- Ao tentar confirmar o pedido, o sistema detecta que o limite de crédito mensal foi excedido e gera o Evento 15.

4. **Vincular o liberador**

- Um pop-up denominado **Liberações Solicitadas** será exibido.
- Informe o **usuário liberador** no campo designado.
- Marque a opção **Notificação** para informar o liberador sobre a necessidade de aprovação.
- Clicar no botão **Definir liberador**.
- A coluna **Nome (Liberador)** será automaticamente atualizada.
- Clique no botão “**Salvar** **Liberações”** para registrar a solicitação.

5. **Realizar a liberação**
   **A liberação pode ser feita de duas formas:**

- **Na Central de Vendas:** Clique no botão **"Liberações”.**
- **Na Tela Liberação de Limites:** Acesse diretamente esta tela, que possui o mesmo layout da Central de Vendas.
  Insira o **usuário e a senha** do liberador autorizado.
- No painel lateral, localize o pedido que apresenta o **Nro Único** e selecione-o.
- Clique em **Liberar**.
- Caso necessário, adicione uma observação justificando a liberação.

6. **Caso o usuário liberador esteja logado**

- Se o liberador já estiver logado no sistema, marque a opção **Sou Liberador** para agilizar o processo.

7. **Confirmar o pedido**

- Retorne à **Central de Vendas** e clique novamente em **Confirmar** para concluir o pedido.
- No **Portal de Vendas**, habilite o filtro **Liberação - Pendentes** para verificar que o pedido liberado já não aparece mais na lista.
- Limpe o filtro e realize uma nova busca pelo número do pedido para confirmar que ele foi processado corretamente.

#### Correção e Repetição

- **Verifique os dados:** Confirmar a configuração do campo **Limite crédito** **mensal** no cadastro do parceiro e a precisão das informações da operação (valor, tipo de negociação e parceiro).
- **Valide o bloqueio:** Certifique-se de que o valor excede o limite cadastrado.
- **Correção de  falhas:** Ajuste erros, como liberador incorreto, dados incompletos ou aplicação inadequada de limites.
- **Confirme a operação:** Verificar e corrigir as falhas, retorne na central de vendas e confirme a operação para que o pop-up **"Liberações Solicitadas"** apresente na tela, realize novamente a definição do liberador, garantindo que os campos estejam corretamente preenchidos e as permissões sejam respeitadas.
- **Pratique:** Simule liberações para reforçar o aprendizado da equipe.
