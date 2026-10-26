---
id: "44013404999831"
titulo: "[TMS] - Prazo de entrega da Empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013404999831--TMS-Prazo-de-entrega-da-Empresa"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:57:00Z"
rotulos: ["sync_hc", "lincros", "lincros_13432541", "sync_hash_1f6e5cc5c1bf"]
---

# [TMS] - Prazo de entrega da Empresa

**Menu**: Cadastros gerais > Modelo de distribuição > Critérios de seleção > Prazos de entrega > Empresa

**Objetivo**: O prazo de entrega da empresa constitui-se de um cadastro onde constam as cidades e os dias para entrega da mercadoria. Possibilita o controle do andamento do transporte de suas cargas sem depender do prazo de transportadora.

Abaixo segue o passo a passo para cadastrar os prazos:

Este cadastro deve ser realizado manualmente via botão novo encontrado na tela de listagem de prazos de entrega.

1. - Tela de listagem

     ![Imagem 1: Tela de listagem](https://ajuda.sankhya.com.br/hc/article_attachments/44013440833559)

- Tela de edição de prazo de entrega:

![Imagem 2: Tela de edição de prazo de entrega:](https://ajuda.sankhya.com.br/hc/article_attachments/44013417021591)

- Descrição: Este campo determina o título definido para o prazo de entrega;
- Início de vigência: Este campo delimita que só serão calculados prazos de entrega que tiveram a data de emissão igual ou maior à esta data;
- Fim de vigência: Este campo delimita que só serão calculados prazos de entrega que tiveram a data de emissão igual ou menor à esta data;
- Situação de aprovação: O prazo de entrega só passará a ser contado como ativo quando estiver com situação igual a DEFERIDO;
- Rota: Este campo é de suma importância por definir quais rotas serão atendidas por este prazo de entrega;
- Modal: Este campo define para qual modal será realizado o cálculo;
- Tipo de operação: Este campo define para qual tipo de operação será realizado o cálculo;
- Somente dias úteis: Esta configuração determina que a entrega só poderá ser efetuada em dias úteis, ou seja, finais de semana e feriados são ignorados no cálculo do agendamento de entrega;
- Inicia a contagem: Este campo define qual a data será usada como base para o cálculo da previsão do cliente: Data de emissão da nota fiscal, Data de emissão da pré-nota fiscal ou Ocorrência;
- Ocorrência: Este campo será habilitado caso o campo anterior possua o valor Ocorrência. Ao lançar esta ocorrência para uma nota que atenda ao cadastro, o cálculo será realizado a partir da data da ocorrência;
- Prazo: Consiste na quantidade de dias necessário para a transportadora realizar a entrega;
- Dias da semana: Determina os dias da semana em que são realizadas entregas pela transportadora;
- Localizações: Este campo permite customizar os campos de Prazo e Dias da semana, onde é possível selecionar para cada cidade ou estado (pertencentes à rota informada) a quantidade de dias necessárias para entrega e os dias em que são feitas as entregas. Caso esteja preenchido com algum valor, este será considerado o prazo. Caso zerado, será considerado o prazo geral.

Aba Histórico

Nesta aba estão registrados os históricos de alterações realizados pelos usuários no item selecionado.

**Calculo da previsão de entrega para o cliente:**Caso o parâmetro de empresa "calcularPrazoPrevisaoCliente" estiver ativo, ao lançar uma pré-nota, uma nota ou uma ocorrência que contemple os dados do cadastro, será calculada a data de previsão de entrega do cliente com base nos dados informados no cadastro, considerando os dias de entrega, se serão computados somente os dias úteis e o prazo de entrega para a nota.

Durante o cálculo, serão considerados também os feriados (do ano corrente ou do ano da data base).

Para ser ativado este parâmetro, favor solicitar ao time de suporte da Lincros por um dos canais de atendimento!

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
