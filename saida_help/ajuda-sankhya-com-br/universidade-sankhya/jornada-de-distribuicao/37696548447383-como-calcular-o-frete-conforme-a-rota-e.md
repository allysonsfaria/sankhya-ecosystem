---
id: "37696548447383"
titulo: "Como calcular o frete conforme a rota e realizar o rateio por valor dos pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37696548447383-Como-calcular-o-frete-conforme-a-rota-e-realizar-o-rateio-por-valor-dos-pedidos"
trilha: "Universidade Sankhya > Jornada de Distribuição"
atualizado_em: "2026-08-20T04:14:53Z"
rotulos: ["Configuração", "Rateio", "Transporte", "Financeiro", "Sankhya", "Logística"]
---

# Como calcular o frete conforme a rota e realizar o rateio por valor dos pedidos

| Categoria |
| --- |
| [Como funciona o cálculo de frete por rota e qual sua importância?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37696548447383-Como-calcular-o-frete-conforme-a-rota-e-realizar-o-rateio-por-valor-dos-pedidos#h_01KF0YRKW1PQDF6CZB8523E48P) |
| [Quais problemas são evitados com a utilização do cálculo de frete por rota e rateio por valor?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37696548447383-Como-calcular-o-frete-conforme-a-rota-e-realizar-o-rateio-por-valor-dos-pedidos#h_01KF0YQYCFF6904CJ0V1VG2RPJ) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37696548447383-Como-calcular-o-frete-conforme-a-rota-e-realizar-o-rateio-por-valor-dos-pedidos#h_01KFDSENHFQ910HJARTADDED8X) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37696548447383-Como-calcular-o-frete-conforme-a-rota-e-realizar-o-rateio-por-valor-dos-pedidos#h_01KF0YMWT2GX7SAJC4FAVJ864P) |
| [Mãos à obra! Use o passo a passo para explorar o potencial do ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37696548447383-Como-calcular-o-frete-conforme-a-rota-e-realizar-o-rateio-por-valor-dos-pedidos#h_01KF0YQ6XBEX53D5GEQV53C7ZE) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37696548447383-Como-calcular-o-frete-conforme-a-rota-e-realizar-o-rateio-por-valor-dos-pedidos#h_01KF0YN7AZ4XSS6FAYD7VVVETW) |

## Cálculo de frete por rota, rateio por valor dos pedidos

#### Como funciona o cálculo de frete por rota e qual sua importância?

O cálculo de frete por rota com rateio por valor no Sankhya permite distribuir os custos de transporte de forma proporcional ao valor das mercadorias destinadas a diferentes clientes ou filiais. Essa funcionalidade é configurada após a criação da Ordem de Carga e assegura uma divisão justa dos custos, evitando distorções financeiras. Além de proporcionar maior transparência, o recurso melhora o controle logístico e financeiro, facilita auditorias, reduz inconsistências na apuração dos custos e contribui para uma precificação mais precisa dos produtos.

#### Quais problemas são evitados com a utilização do cálculo de frete por rota e rateio por valor?

A ausência de um critério eficiente para ratear os custos de transporte pode gerar cobranças desproporcionais entre os clientes, comprometendo a justiça na divisão dos valores. Isso afeta diretamente a precificação dos produtos, podendo causar distorções financeiras e perdas de margem. Além disso, a falta de um método estruturado dificulta a alocação precisa das despesas logísticas, prejudicando o controle contábil e a transparência nas operações. A prática do cálculo por rota com rateio por valor corrige essas falhas ao garantir uma divisão mais justa, rastreável e alinhada ao valor transportado por cada destinatário.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1067866314)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa realiza entregas para diversos clientes em diferentes regiões do país. Para otimizar os custos logísticos e garantir que o frete seja cobrado de maneira justa, a empresa utiliza o cálculo de frete por rota e o rateio é por valor de acordo com os pedidos.
Atualmente, os custos de transporte estão sendo divididos igualmente entre os pedidos, independentemente do valor da mercadoria transportada. Isso tem gerado distorções financeiras, pois clientes que compram em maior volume acabam pagando o mesmo frete que aqueles com pedidos menores. Para corrigir essa situação, a empresa decidiu aplicar o rateio proporcional por valor de nota fiscal.

**Tarefa:** Seu desafio é distribuir proporcionalmente o valor das mercadorias em cada pedido. Isso garantirá que cada cliente pague um percentual justo do custo total do transporte, eliminando distorções e promovendo um controle logístico mais eficiente.

#### Mãos à obra! Use o passo a passo para explorar o potencial do ERP Sankhya

**Atente-se!** Antes de prosseguir com este procedimento, certifique-se de que todas as etapas anteriores foram devidamente realizadas. Para a correta execução, é necessário que os seguintes cadastros estejam disponíveis no sistema:

**Rotas**

- **Pedidos de Venda** registrados para clientes dentro da rota definida;
- **Formação de Carga** consolidada, garantindo que os pedidos estejam corretamente agrupados;
- **Sequência de Entrega** previamente estabelecida para a Ordem de Carga que será utilizada.

1. **Configuração da Ordem de Carga**

- Acesse a tela **Ordens de Carga**.
  Menu: Comercial » Rotinas » Ordem de Carga » Ordens de Carga

- Selecione uma OC criada anteriormente.

- Na aba **Frete**, informe no campo Tipo de Cálculo de Frete, "**Valor por Rota/Rateio por Valor**".
- Isso habilita o campo **Rota**, onde se deve informar a rota a ser considerada. Utilize, nesse exemplo, a rota cadastrada anteriormente “Uberlândia x Uberaba”.
- Clique em **Salvar**.

2. **Cálculo do frete**

**Atente-se!** Para cálculo do frete, é importante que as etapas dos exercícios anteriores sejam cumpridas. O cadastro da rota deve ter sido realizado, além da inserção do valor do frete para ela. O frete é calculado devidamente apenas caso a ordem de carga tenha uma sequência de entrega definida.

- Acesse a tela: **Cálculo de Frete**
  Menu:  Comercial » Rotinas »  Ordem de Carga » Cálculo de Frete
- Habilite o filtro personalizado da Ordem de Carga.
- No campo **Tipo de movimento** informe: **Pedido de venda**
- Clique em **Aplicar**
- Informe o número da **Ordem de Carga** configurada anteriormente e clique em **Aplicar**.
- Clique em **Calcular frete.**

3. **Validação do cálculo**

- Acesse a tela **Formação de Carga**
  Menu:  Comercial » Rotinas »  Ordem de Carga » Formação de Carga
- Utilize o campo **OC**, para localizar a ordem de carga no qual foi feito o cálculo do frete.
- Clique em **Aplicar**.
- No rodapé da tela localize o campo **Valor do Frete** e veja se foi devidamente calculado.

#### Correção e Repetição

- Antes de seguir com o procedimento, confirme se todos os cadastros e configurações anteriores foram realizados corretamente.
- Garanta que a Ordem de Carga está devidamente configurada e possui vínculo de Rota.
- Valide se o cálculo de frete foi devidamente realizado.
- Se necessário, ajuste as configurações e repita o processo para garantir precisão nos cálculos.
