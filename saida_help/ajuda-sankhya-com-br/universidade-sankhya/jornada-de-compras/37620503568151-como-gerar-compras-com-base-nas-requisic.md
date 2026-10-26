---
id: "37620503568151"
titulo: "Como gerar compras com base nas requisições internas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-07-22T14:12:26Z"
rotulos: ["Produtos", "Configuração", "Requisições", "Análise de Giro", "Estoque"]
---

# Como gerar compras com base nas requisições internas

| Categoria |
| --- |
| [Qual o objetivo de realizar uma compra em função de solicitações ou requisições internas e quais os benefícios?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas#h_01KESS0D3QMK512R1CYRJ7D6W8) |
| [Quais problemas este recurso do sistema resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas#h_01KESS16YZES11XP1MBRVHEVE5) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas#h_01KESS1SRGG2TREAW3RQQMX5S3) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas#h_01KFBDJFVGEHG4MB4GXYVG4GVR) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas#h_01KFBDGPN9NRPBGT73DDN009VZ) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas#h_01KESS2A4AMP02X7MF2HJ1PHQT) |
| [Passo a Passo para Configurar os Filtros da tela Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas#h_01KESS4G4ARCPGXE8V34WDY982) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37620503568151-Como-gerar-compras-com-base-nas-requisi%C3%A7%C3%B5es-internas#h_01KESS6200CWSVVTTCDV0C2P3W) |

## Identificar a necessidade de compras em função de requisições internas

#### Qual o objetivo de realizar uma compra em função de solicitações ou requisições internas e quais os benefícios?

O objetivo de realizar uma compra com base em solicitações ou requisições internas é assegurar que os setores da empresa recebam os materiais ou serviços necessários no momento certo, de forma planejada e conforme suas reais necessidades. Essa prática evita compras desnecessárias, reduz desperdícios, garante a continuidade das operações e promove um alinhamento mais eficiente entre os processos de demanda interna e o setor de compras, resultando em maior controle, economia e agilidade na gestão de aquisições.

#### Quais problemas este recurso do sistema resolve?

- **Prevenção de excessos e rupturas de estoque -** Garante que as aquisições sejam realizadas com base nas necessidades reais, evitando custos desnecessários com armazenagem ou falta de produtos essenciais.
- **Centralização e organização das demandas -** Facilita o controle interno ao consolidar solicitações em um único processo, promovendo maior visibilidade e eficiência.
- **Otimização de negociações com fornecedores -** Consolida pedidos, resultando em melhores condições de compra, redução de custos e maior eficiência na gestão de compras.

#### Quais os riscos de não utilizar?

A ausência de compras baseadas em requisições internas pode causar um desalinhamento com as demandas reais, resultando em aquisições inadequadas ou insuficientes, interrupções no abastecimento e acúmulo de produtos sem giro ou obsoletos no estoque. 

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052445237)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Na última semana, o setor de manutenção da **Axis** enfrentou atrasos por falta de materiais básicos, mesmo com requisições internas já registradas.
Para evitar esse tipo de falha, o comprador passou a utilizar o relatório de Análise de Giro com a matriz de **Uso e Consumo**, garantindo que os itens mais requisitados sejam identificados e comprados no momento certo.

**Tarefa:** Assim como foi feito para os produtos de revenda, você irá configurar a matriz para realizar uma análise detalhada e identificar quais produtos devem ser comprados, com base nas requisições internas pendentes.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

Certifique-se de ter uma matriz de giro para uso e consumo criada e configurada conforme as orientações do vídeo demonstrativo e também se **certifique de ter um pedido de requisição registrado**.

1. **Acesse a Tela de Análise de Giro**
   Menu:Comercial » Rotinas » Análise de Giro

- Selecione a matriz de giro configurada para **Produtos de Uso e Consumo**.
- Clique no botão “**Alterar a matriz selecionada**”

2. **Configuração**

**Aba Períodos**

- Marque a opção “**Períodos dinâmicos”**
- Defina o período para **3 mês/meses anteriores**.

**Aba Estoque Mínimo e Sugestão de Compras**

- Inserir **10** no campo “**%Acréscimo na Sugestão de Compras:**”.
- Verifique se o filtro **“Pedido de venda pendente”** está configurado corretamente com a fórmula:

CabecalhoNota->CODTIPOPER = 1801  

AND CabecalhoNota->TIPMOV = 'J'  

**Aba Outras Configurações**

- Marque o campo “**Incluir produtos sem giro**”.
- Marque o campo **“Incluir produtos sem estoque**”.
- No campo “**Considerar Custo**” selecione **Reposição**.
- No campo “**Detalhar de acordo com**:**”** selecione **Empresa**.
- Marque o campo “**Listar pedidos na aba** **Compra/Vendas Pendentes**”.

#### Filtros

- Aplique os filtros de produtos para consumo, nos campos: "**Produtos com Giro**", "**Produtos sem Giro**" e "**Produtos sem Giro e sem Estoque**".
- Clique no botão “**Processar Matriz**”.

#### Passo a Passo para Configurar os Filtros da tela Análise de Giro

**1º Campo:**

- Clique no botão **“+ Filtro”** (**Cadastrar Filtro**).
- Defina o nome **Consumo** para o filtro
- Em seguida, clique no botão **“+ Condição”** (Cadastrar Condição).
- Clique em **Selecione o campo**.
- Selecione **Produto** no painel “**Ligações em Giro de Produtos**”.
- No campo de busca **“Informe sua busca”**, pesquise **“Usado como”** e selecione a opção correspondente.

**2º Campo**

- Selecione a condição “**Igual (=)**”.

**3º Campo**

- Selecione a opção **Consumo**
- Clique no botão “**Salvar**”.

3. **Processar Matriz**

- Clique no botão **“Processar Matriz**”.

4. **Criar Filtro de Pedido de Requisição Interna**

- Clique no botão **“+ Filtro”** (**Cadastrar Filtro**) .
- Defina o nome **Pedido de** **Requisição Interna** para o filtro.
- Clique no botão **“Modo Avançado”**.
- Na caixa de texto, cole a fórmula abaixo:

GiroProduto.CODPROD IN (SELECT DISTINCT ITE.CODPROD FROM TGFITE ITE, TGFCAB CAB WHERE ITE.NUNOTA=CAB.NUNOTA AND CAB.CODTIPOPER = 1801 AND CAB.PENDENTE='S' AND GiroProduto.CODREL = ?:{entidade=GiroProduto;campo=CODREL})

- Clique no botão “**Salvar**”.

Aplique o filtro **Pedido de Requisição Interna** e verifique se apenas os produtos solicitados no pedido de requisição interna são exibidos.

#### Correção e Repetição

- Certifique-se de que todos os campos obrigatórios foram preenchidos corretamente na Matriz de Giro de Uso e Consumo
- Atenção para os Filtros dentro da Matriz e da tela de Análise de Giro.
- Caso não tenha sido concluído conforme esperado, refaça o processo corrigindo as informações necessárias.
- Certifique que existe Pedido de Requisição Interna.
- Para praticar, experimente criar novamente com um cenário diferente, como outro pedido de Requisição Interna, com outros produtos.
