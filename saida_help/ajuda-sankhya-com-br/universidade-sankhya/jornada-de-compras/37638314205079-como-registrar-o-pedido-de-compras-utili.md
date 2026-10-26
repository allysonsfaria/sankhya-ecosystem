---
id: "37638314205079"
titulo: "Como registrar o pedido de compras utilizando a sugestão de compra giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37638314205079-Como-registrar-o-pedido-de-compras-utilizando-a-sugest%C3%A3o-de-compra-giro"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-07-22T14:12:15Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Análise de Giro", "TOP", "Estoque"]
---

# Como registrar o pedido de compras utilizando a sugestão de compra giro

| Categoria |
| --- |
| [Para que serve a sugestão de compra por giro na matriz de análise e quais seus benefícios?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638314205079-Como-registrar-o-pedido-de-compras-utilizando-a-sugest%C3%A3o-de-compra-giro#h_01KEVQBSJTM1SQQ7C1RD2JMFQK) |
| [Quais os problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638314205079-Como-registrar-o-pedido-de-compras-utilizando-a-sugest%C3%A3o-de-compra-giro#h_01KEVQC8RWYS404TS8NSJJ1BDG) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638314205079-Como-registrar-o-pedido-de-compras-utilizando-a-sugest%C3%A3o-de-compra-giro#h_01KFBGXVZQPN1MBWGTWNVXBTSH) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638314205079-Como-registrar-o-pedido-de-compras-utilizando-a-sugest%C3%A3o-de-compra-giro#h_01KEVQ0CRHCX7HR9796GQG0MVV) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638314205079-Como-registrar-o-pedido-de-compras-utilizando-a-sugest%C3%A3o-de-compra-giro#h_01KEVQDK1D9DBT978DHZ0DA8S2) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638314205079-Como-registrar-o-pedido-de-compras-utilizando-a-sugest%C3%A3o-de-compra-giro#h_01KEVQK88PRJ86MRJE5GF1443T) |

## Registro de pedidos de compra

#### Para que serve a sugestão de compra por giro na matriz de análise e quais seus benefícios?

A sugestão de compra por giro, gerada a partir da matriz de análise, é um recurso estratégico que utiliza o histórico de giro dos produtos para orientar decisões de aquisição. Com base em critérios como demanda, estoque disponível e lead time, o sistema automatiza a geração de pedidos de compra, promovendo maior precisão, agilidade e alinhamento entre oferta e demanda.

#### Quais os problemas este recurso resolve?

- **Falta de produtos em estoque:** evita rupturas ao indicar automaticamente os itens que precisam ser repostos com base no consumo real.
- **Excesso de mercadorias paradas:** reduz o acúmulo de produtos com baixo giro, otimizando o espaço e o capital investido.
- **Compras desalinhadas com a demanda:** melhora a assertividade nas aquisições, ajustando os pedidos à demanda real e ao histórico de vendas.
- **Dificuldade no planejamento de compras:** torna o processo mais ágil e estratégico, com base em critérios previamente definidos na matriz.
- **Erros manuais e retrabalho:** minimiza falhas humanas ao automatizar parte da análise e geração dos pedidos.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052445728)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Na **Axis**, um dos principais clientes antecipou a reposição do Produto 1, mas o pedido de compra ainda não havia sido registrado no sistema, mesmo após a Análise de Giro realizada.

Com o estoque zerado e risco de descumprir o prazo, o comprador agiu com urgência e registrou o pedido imediatamente, garantindo o abastecimento e evitando prejuízos à operação e ao relacionamento com o cliente.

A praticidade da tela Análise de Giro foi essencial para visualizar rapidamente os dados e tomar uma decisão assertiva a tempo.

**Tarefa:** Acesse a tela Análise de Giro e, com a matriz configurada e processada anteriormente, registre o pedido de compra com base nas informações apresentadas no diagnóstico da sugestão de compra.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Acesse a tela Análise de Giro**
   Menu: Comercial » Rotinas » Análise de Giro

- Localize a matriz de giro configurada e processada anteriormente.

2. **Analise os Resultados**

- Na grade de dados da análise, localize a coluna “**Sugestão de Compras**” para visualizar as quantidades indicadas para cada produto.
- Acesse a sub-aba “**Detalhes da Sug. de Compras**” para entender como foi calculada a sugestão de compra com base nos critérios do giro.

3. **Valide o Fornecedor Preferencial**

- Acesse a tela Produtos
  Menu: Configurações » Cadastros » Produtos
- Na aba “**Geral**”, preencha o campo “**Fornecedor Preferencial**” com o fornecedor cadastrado na sua base de testes.

4. **Gere o Pedido de Compra**

- Volte para a tela “**Análise de Giro**”.
  Menu: Comercial » Rotinas » Análise de Giro
- Clique no botão “**Pedidos**”, localizado no menu principal, no canto superior esquerdo da tela.
- Na grade “**Resumo por Fornecedor/Pedido**”, confirme que está configurado para usar “**Sug. Compra Giro**”**.**
- Clique no botão “**Preferências**”.

**Informe as preferências nos campos indicados:**

- **TOP (Tipo de Operação):** Selecione **PEDIDO DE COMPRA**.
- **Tipo de Negociação**: Escolha o tipo de negociação definida com o fornecedor.
- **Empresa de Negociação**: Informe a empresa responsável pela negociação da operação.
- **Centro de Resultado**: Escolha conforme o que está previsto no orçamento.
- **Natureza**: Defina a natureza do produto, levando em conta o objetivo da compra.
- **Usar Custo TOP**: Marque esta opção.

- Clique no botão “**OK**”.

**Geração do Pedido**

- Clique no botão “**Gerar Pedido**” para processar o pedido.

**Validação do Pedido Gerado**

- Clique no botão “**Visualizar Pedido**”, localizado ao lado de “Gerar Pedido”.

Será direcionado para a tela **Central de Compras**, confirme se todos os dados do orçamento estão corretos antes de finalizar.

É importante lembrar que, caso os produtos sejam fornecidos por diferentes parceiros, será necessário gerar um pedido separado para cada fornecedor.

5. **Revise o pedido na Central de Compras**

- Clique no botão “**Visualizar Pedido**”, localizado ao lado de “Gerar Pedido”.

Será direcionado para a tela **Central de Compras**, confirme se todos os dados do orçamento estão corretos antes de finalizar.

**Verifique as informações do pedido:**

- **Itens:** Quantidade, fornecedor, valores e condições.
- **Totais:** Valores totais.
- **Transporte:** Informações de frete.
- **Impostos:** Tributos aplicados.
- **Financeiro:** Condições de pagamento.
- Clique em “**Confirmar**”.
  Se o sistema estiver configurado para exigir liberação, um alerta será exibido informando a necessidade de aprovação, gerando automaticamente o **Evento 44**.

6. **Processo de Liberação**

- No pop-up exibido, preencha o campo “**Liberador**” com o usuário responsável, clique em “**Definir Liberador**” e, em seguida, em “**Salvar**”.
- Retorne à tela” Central **de Compras**” e clique no botão “**Liberações**”.
- Na tela de liberação, insira o usuário e a senha do responsável informado e clique em “**Aplicar**”.
- Selecione o pedido exibido e clique no botão “**Liberar**” ou dê um duplo clique no registro para realizar a aprovação.

#### Correção e Repetição

- Certifique-se de que todos os campos obrigatórios foram preenchidos corretamente na Matriz de Giro.
- Verifique se a TOP “Pedido de Compra” está configurada corretamente.
- Verifique-se de que o fornecedor foi cadastrado dentro da tela Produto.
- Se algo não tiver funcionado como esperado, refaça o processo corrigindo as informações necessárias.
- No painel inferior, acesse a aba “Sugestão de Compras” e confira se foi gerada a Sugestão de Compra Giro.
- Para praticar novamente, crie um novo cenário com produtos diferentes.
