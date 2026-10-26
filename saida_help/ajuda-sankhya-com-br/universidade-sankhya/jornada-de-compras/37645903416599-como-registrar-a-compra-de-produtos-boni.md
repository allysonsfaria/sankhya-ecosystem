---
id: "37645903416599"
titulo: "Como registrar a compra de produtos bonificados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37645903416599-Como-registrar-a-compra-de-produtos-bonificados"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-07-22T14:12:03Z"
rotulos: ["Produtos", "Configuração", "TOP", "Estoque", "Financeiro"]
---

# Como registrar a compra de produtos bonificados

| Categoria |
| --- |
| [O que é uma entrada de bonificação?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37645903416599-Como-registrar-a-compra-de-produtos-bonificados#h_01KEW5Q8BARMET2Z8YD6J7QPBF) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37645903416599-Como-registrar-a-compra-de-produtos-bonificados#h_01KEW5QTYQ8NW77ZR9AN1G3AX2) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37645903416599-Como-registrar-a-compra-de-produtos-bonificados#h_01KFBN3DB1VNA2WEBG0QQE53D3) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37645903416599-Como-registrar-a-compra-de-produtos-bonificados#h_01KEW5R5Q0BPF7Q0MT22XXHJJJ) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37645903416599-Como-registrar-a-compra-de-produtos-bonificados#h_01KEW5RK2WNJZPXZY7VVP4F6E0) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37645903416599-Como-registrar-a-compra-de-produtos-bonificados#h_01KEW5W8XJGGHY1QX3W9PW0RT8) |

## Entrada de bonificação

#### O que é uma entrada de bonificação?

A Entrada de Bonificação é o registro fiscal e contábil da recepção de mercadorias enviadas pelo fornecedor sem custo para a empresa, geralmente como parte de ações promocionais, incentivos comerciais ou compensações estratégicas. 

A "Nota Fiscal de Compra - Item Bonificado refere-se a situações em que o fornecedor concede produtos como bônus, sem cobrança adicional, sendo essencial que esses itens sejam registrados corretamente no sistema, tanto para controle de estoque quanto para a correta escrituração fiscal. 
No momento da entrada da nota fiscal, é necessário especificar que o item é bonificado, garantindo que o tratamento tributário e contábil seja adequado e esteja alinhado às exigências fiscais vigentes. Apesar de não haver um custo direto, as bonificações podem ter implicações tributárias, dependendo da legislação aplicável, com possíveis incidências de ICMS, PIS e COFINS. 

#### Quais os riscos de não utilizar?

Sem esse registro formal, os produtos recebidos como bonificação podem ser incorretamente tributados, resultando em autuações, multas e sanções fiscais, uma vez que a ausência de documentação adequada pode ser interpretada como sonegação ou erro de escrituração. Além disso, a falta desse controle pode gerar distorções no inventário, impactando a acuracidade do estoque e dificultando a reposição de produtos, o que pode levar a perdas financeiras e falhas no atendimento da demanda. No âmbito financeiro, a ausência dessa formalização compromete a análise de custos e rentabilidade, podendo inflacionar os custos de aquisição ou distorcer a margem de lucro dos produtos, levando a decisões estratégicas equivocadas.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1066968410)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis** mantém uma relação de longa data com a **Distribuidora Real Sul**. Em reconhecimento aos anos de negociações bem-sucedidas, o representante informou ao comprador que o Produto 2 seria enviado como bonificação na nota fiscal. Para que a entrada do produto ocorra de forma regular, respeitando as normas fiscais e as diretrizes internas da empresa, é necessário que a bonificação esteja devidamente destacada no documento.

**Tarefa:** Acesse o Script de Configuração, siga o passo a passo e registre o pedido de compra. No momento do faturamento da nota, não se esqueça de sinalizar a bonificação, conforme as orientações abaixo.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Portal de compras**

- Acesse a tela **Portal de Compras**
  Menu: Comercial » Consulta » Portal de Compras

- No campo **Tipo de Movimento** localizado na porção superior esquerda, selecione **Pedido de Compra**.
- Clique no símbolo **“...”** (**Filtrar TOP(s)**) ao lado e selecione a TOP **Pedido de Compra**
- Clique em “**Aplicar**” para confirmar a seleção.

Na aba **Resultado da Seleção**, verifique se o pedido de compra está registrado e se os campos **Pendente** e **Confirmada** estão marcados como **Sim**.

- Clique no botão “**Faturar**”.
- Clique no botão “**Próximo**” - não é necessário informar a data de faturamento -.
- Clique no botão “**Concluir**” após checar se a TOP **Pedido de Compra** foi carregada.

**IMPORTANTE!** Para o caso de entrada de bonificação, é imprescindível que o seu pedido de compra tenha mais de 1 item registrado.

2. **Central de Compras**

   Revise as informações do pedido:

**Cabeçalho:** Confirme os dados do fornecedor, se a negociação escolhida foi a opção validada na tela de cadastros e preencha as informações obrigatórias.

**Itens:** Verifique o(s) produto(s), quantidade e valores registrados. Selecione o produto bonificado e insira as informações nos campos:

- **Campo Bonificação:** Preencher com o valor total do item.
- **Campo %desc. bonif.:** Preencher com 100%.
- Clique em **Salvar.**

**Rodapé:** Acesse a aba Financeiro, confira as informações da negociação comercial e verifique se o valor da bonificação foi descontado do título gerado. O valor do título deve ser menor que o valor total da nota.

**IMPORTANTE!**  Caso o valor na aba financeiro não apresente a bonificação mesmo após atualizar, revise as configurações anteriores descritas neste tópico e siga as orientações na Demonstração Prática para **Refazer o financeiro** e ajustar as informações financeiras da nota. 

- Clique em **Confirmar**. 
  O sistema irá gerar um alerta de que o pedido Exige Conferência, se configurado previamente na TOP.

1. **Processo de Liberação para Conferência**

- No botão “**...**” (**Outras opções**) e selecione  **Liberar para conferência**.
- Será emitido alerta de **“Pedido/Nota liberado para conferência”**, clique em **OK.**
- Acesse a tela **Fila de Conferência -** Menu: Comercial » Rotinas » Fila de Conferência

- Filtre pelo **número da nota**.
- Clique no botão “**Aplicar**”.
- Selecione a conferência correspondente com um duplo clique.

Realize a conferência dos produtos:

- Informe o **código de barras**.
- Insira a **quantidade** correspondente.
- Preencha o campo de **controle** (quando necessário).

- Clique no botão “**Finalizar Conferência**”.

Valide na grade de **‘Itens Conferidos**’ se ocorreu a conversão da quantidade. 

2. **Finalizar o Pedido**

- Após finalizar a conferência, retorne à **Central de Compras**.
- Clique no botão “**Confirmar**”.

#### Correção e Repetição

- Confirme as configurações a **TOP de Compra.**
- Valide se após salvar o Rodapé foi atualizado com as informações corretas.
- Caso não tenha sido concluído conforme esperado, refaça o processo corrigindo as informações necessárias.
- Certifique-se de que realizou as configurações da TOP e o Layout da Nota estão corretos. Lembre-se que a TOP é histórica, caso realize alguma alteração, será necessário iniciar um novo pedido de compra.
- Para praticar, experimente criar novamente um novo pedido de compra, com outros produtos e fornecedores.
