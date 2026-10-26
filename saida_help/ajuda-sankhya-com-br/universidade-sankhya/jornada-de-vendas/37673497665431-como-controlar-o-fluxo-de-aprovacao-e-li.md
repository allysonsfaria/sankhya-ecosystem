---
id: "37673497665431"
titulo: "Como controlar o fluxo de aprovação e liberar venda em caso de atraso de pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37673497665431-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-venda-em-caso-de-atraso-de-pagamento"
trilha: "Universidade Sankhya > Jornada de Vendas"
atualizado_em: "2026-09-01T18:36:33Z"
rotulos: ["Configuração", "Parceiro", "Portal de Vendas", "Crédito", "TOP", "Financeiro"]
---

# Como controlar o fluxo de aprovação e liberar venda em caso de atraso de pagamento

| Categoria |
| --- |
| [O que é o evento 8 (Atraso) e qual sua importância?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673497665431-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-venda-em-caso-de-atraso-de-pagamento#h_01KEYRQY4NQAP0YB2H27BS5YGX) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673497665431-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-venda-em-caso-de-atraso-de-pagamento#h_01KEYRQPBWDP8AB6J7EGZ62432) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673497665431-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-venda-em-caso-de-atraso-de-pagamento#h_01KFBVSP67QMJ4DMCCM7C2QPRD) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673497665431-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-venda-em-caso-de-atraso-de-pagamento#h_01KEYRQCNA6AT4KEADCN198HF0) |
| [Hora de colocar a mão na massa! Siga o passo a passo para Liberar o Evento 8 (Atraso) no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673497665431-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-venda-em-caso-de-atraso-de-pagamento#h_01KEYRPVT8P5Q5E0MCWQF7XC8W) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37673497665431-Como-controlar-o-fluxo-de-aprova%C3%A7%C3%A3o-e-liberar-venda-em-caso-de-atraso-de-pagamento#h_01KEYRNE203QJKWZ02MNVPNJXG) |

## Liberação do Evento 8 (Atraso)

#### O que é o evento 8 (Atraso) e qual sua importância?

É um procedimento adotado pelas empresas para gerenciar riscos financeiros, acionado quando há pagamentos pendentes além do prazo de tolerância ou carência. Esse evento exige uma análise detalhada da situação financeira antes de permitir novas transações a prazo, garantindo que apenas aqueles que cumprem os termos de pagamento estabelecidos possam continuar realizando compras a prazo. Esse tipo de liberação é essencial para prevenir inadimplência, controlar o fluxo de caixa e evitar o superendividamento, protegendo assim a saúde financeira da empresa.

#### Quais problemas este recurso resolve?

- **Risco de inadimplência:** aumenta as perdas financeiras por falta de controle prévio.
- **Falta de controle financeiro:** dificulta o monitoramento de limites de crédito e de pagamentos em atraso.
- **Superendividamento de clientes:** permite acúmulo de dívidas acima da capacidade de pagamento.
- **Aprovação de transações sem análise prévia:** gera novos créditos para clientes já inadimplentes.
- **Desequilíbrio no fluxo de caixa:** compromete o planejamento financeiro da empresa.
- **Expansão descontrolada de dívidas:** aumenta o risco de prejuízos operacionais.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052413776)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa possui um cliente, que realizou um pedido de venda no valor de **R$ 10.000,00**. Durante a confirmação do pedido, o sistema identificou que o cliente possui um atraso de 15 dias em um pagamento anterior, enquanto a tolerância configurada para inadimplência é de apenas 10 dias. O sistema bloqueia automaticamente o pedido e gera o **Evento 8**, solicitando a liberação por parte de um usuário autorizado.

**Tarefa:**  Analise o **Evento 8** gerado pelo sistema e libere o limite de crédito para que o pedido seja processado, mantendo o controle financeiro e organizacional.

#### Hora de colocar a mão na massa! Siga o passo a passo para Liberar o Evento 8 (Atraso) no ERP Sankhya

1. Acesse a tela **“Parceiros”.**
   Menu: Configurações » Cadastros » Parceiros

- Na aba Crédito, preencha o campo **“Tolerância p/ inadimplência”** com os dias de carência para pagamento após o vencimento.
- Clique em Salvar **[F7]** para registrar as informações.

2. Acesse a tela **“Tipos de Operação - TOP”**
   Menu: Comercial » Arquivo » Cadastro

- Selecione o tipo de operação que irá validar. (**Pedido de venda**)
- Na aba Financeiro, preencha o campo **“Atraso”** e configure a validação de atraso nas movimentações.
- **Não validar:** Não será validado o atraso do parceiro por esta TOP.
- Clique no botão **Salvar [F7]** para registrar as informações.

3. Registrar um **pedido de venda**, assegurando a precisão das informações da operação nos campos essenciais, como tipo de negociação e parceiro.

- Certifique-se de que o **Tipo de Negociação** utilizado no pedido está configurado para pagamento **‘a prazo’**.

4. **Geração do evento 8**

- Ao tentar confirmar o pedido, o sistema detecta o prazo de tolerância ou carência definido pela empresa dos títulos em atraso e gera o Evento 8.

5. **Vincular o liberador**

- Um pop-up denominado **Liberações Solicitadas** será exibido.
- Informe o **usuário liberador** no campo designado.
- Marque a opção **Notificação** para informar o liberador sobre a necessidade de aprovação.
- Clicar no botão **Definir liberador**.
- A coluna **Nome (Liberador)** será automaticamente atualizada.
- Clique no botão “**Salvar** **Liberações”** para registrar a solicitação.

6. **Realizar a liberação**
   **A liberação pode ser feita de duas formas:**

- **Na Central de Vendas:** Clique no botão **"Liberações”.**
- **Na Tela Liberação de Limites:** Acesse diretamente esta tela, que possui o mesmo layout da Central de Vendas.
  Insira o **usuário e a senha** do liberador autorizado.
- No painel lateral, localize o pedido que apresenta o **Nro Único** e selecione-o.
- Clique em **Liberar**.
- Caso necessário, adicione uma observação justificando a liberação.

7. **Caso o usuário liberador esteja logado**

- Se o liberador já estiver logado no sistema, marque a opção **Sou Liberador** para agilizar o processo.

8. **Confirmar o pedido**

- Retorne à **Central de Vendas** e clique novamente em **Confirmar** para concluir o pedido.
- No **Portal de Vendas**, habilite o filtro **Liberação - Pendentes** para verificar que o pedido liberado já não aparece mais na lista.
- Limpe o filtro e realize uma nova busca pelo número do pedido para confirmar que ele foi processado corretamente.

#### Correção e Repetição

- **Verifique os dados:** Confirmar a configuração no tipo de operação e preferências dos valores e campos informados.
- **Valide o bloqueio:** Certifique-se a existência de títulos em atraso no prazo informado no cadastro do parceiro ou preferências.
- **Correção de  falhas:** Ajuste erros, como liberador incorreto, dados incompletos ou aplicação inadequada.
- **Confirme a operação:** Verificar e corrigir as falhas, retorne na central de vendas e confirme a operação para que o pop-up **"Liberações Solicitadas"** apresente na tela, realize novamente a definição do liberador, garantindo que os campos estejam corretamente preenchidos e as permissões sejam respeitadas.
- **Pratique:** Simule liberações para reforçar o aprendizado.
