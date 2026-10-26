---
id: "37834359307159"
titulo: "Como elaborar DMPL e DLPA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37834359307159-Como-elaborar-DMPL-e-DLPA"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-07-24T12:43:46Z"
rotulos: ["Configuração", "Relatórios", "ECD", "Contabilidade", "Financeiro", "ERP Sankhya"]
---

# Como elaborar DMPL e DLPA

| Categoria |
| --- |
| [O que são a DMPL e a DLPA?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834359307159-Como-elaborar-DMPL-e-DLPA#h_01KFGS8RVBNTBJ804P004XP48T) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834359307159-Como-elaborar-DMPL-e-DLPA#h_01KFGS94A0R8CZD6QQ622A11EW) |
| [Demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834359307159-Como-elaborar-DMPL-e-DLPA#h_01KFGS9ASHS53W7GAT2SKTXKRP) |
| [Cenário de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834359307159-Como-elaborar-DMPL-e-DLPA#h_01KFGS9M223FR9CNEHNWFHRX1H) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37834359307159-Como-elaborar-DMPL-e-DLPA#h_01KFGS9VYSA4EYHE7V697G4FW1) |

## Demonstração das Mutações do Patrimônio Líquido (DMPL) e Demonstração de Lucros ou Prejuízos Acumulados (DLPA)

#### O que são a DMPL e a DLPA?

A **Demonstração das Mutações do Patrimônio Líquido (DMPL)** apresenta, de forma detalhada, todas as alterações ocorridas nas contas do patrimônio líquido da empresa ao longo de um período contábil. Esse demonstrativo evidencia variações em itens como capital social, reservas de capital e de lucros, lucros ou prejuízos acumulados e demais ajustes, resultantes das operações do exercício (como o lucro líquido) ou de eventos extraordinários (como distribuição de dividendos e aumento de capital).

A **Demonstração de Lucros ou Prejuízos Acumulados (DLPA)** integra a DMPL, funcionando como uma de suas colunas. Ela detalha especificamente as movimentações da conta de lucros acumulados, evidenciando saldo inicial, resultado do exercício, ajustes de períodos anteriores, reservas, dividendos e saldo final.

Em conjunto, DMPL e DLPA permitem visualizar com clareza a evolução do patrimônio líquido da empresa, assegurando transparência na destinação do resultado e fortalecendo a integridade das demonstrações contábeis.

#### Quais problemas este recurso resolve?

- Falta de transparência nas variações do patrimônio líquido e da destinação de lucros.
- Dificuldade em identificar a origem das alterações patrimoniais em empresas com operações complexas.
- Inconsistências na prestação de contas a sócios, acionistas e demais interessados.
- Risco de decisões estratégicas baseadas em informações incompletas sobre reservas e dividendos.
- Desalinhamento entre DRE, DMPL e Balanço Patrimonial.
- Ausência de rastreabilidade de ajustes retroativos ou de políticas contábeis.
- Conflitos societários por ausência de controle sobre a distribuição de dividendos.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1120904009)

#### Cenário de aplicação

A empresa Axis LTDA., do segmento atacadista, está em processo de fechamento contábil anual e precisa gerar a DMPL, contemplando também a DLPA. A diretoria solicitou um relatório que evidencie todas as variações ocorridas no patrimônio líquido ao longo do exercício, incluindo lucro líquido, distribuição de dividendos, aumento de capital e movimentações nas reservas. Para atender a essa demanda, o contador responsável deve configurar o ERP Sankhya para consolidar corretamente as contas patrimoniais e a movimentação de lucros acumulados.

**Tarefa:** assista ao vídeo de demonstração prática e siga o passo a passo abaixo para parametrizar a geração da DMPL e da DLPA. Certifique-se de que todos os eventos contábeis — resultado do exercício, ajustes de períodos anteriores, destinações de lucros e movimentações de reservas — estejam corretamente classificados, garantindo a emissão de relatórios confiáveis e em conformidade com as normas contábeis.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Demonstrativos ECD**
   **Menu:** Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD

Aba **Fatos DMPL/DLPA**

- Clique em “**+**” (**Cadastrar** **Fato Contábil**).
- Informe inicialmente o **Código Fato Contábil** e sua descrição no campo indicado como **Desc. Fato Contábil**.
- Defina, também, o campo **Situação** entre Automático e Subtotal ou Total.
- Através do campo **Tipo**, determine o tipo do saldo a ser apresentado no demonstrativo.
- Salve o registro.
- Selecione o fato contábil que deseja vincular ao histórico.
- No painel inferior, clique em “**+**” (**Cadastrar** **Histórico do Fato Contábil**).
- informe o **Cód. do Histórico Padrão.**
- Salve o registro.

Aba **DMPL/DLPA**

- Clique em “**+**” (**Cadastrar** **Hierarquia do Demonstrativo**).
- Informe o **Código** aglutinador da conta.
- Cadastre no campo **Descrição** o nome da conta.
- Marque a opção **Analítico** se o cadastro em questão for analítico.
- Marque a opção **Agrupamento p/ DLPA** para definir se a conta cadastrada irá representar a DLPA.
- Salve o registro.
- Selecione a demonstração que deseja vincular à conta..
- No painel inferior, clique em “**+**” (**Cadastrar** **Contas do Demonstrativo**).
- Preencha o campo**Código Reduzido** da conta, com base no plano de contas da empresa.

  **Observação**: Os lançamentos efetuados nestas contas, obrigatoriamente deverão possuir **Histórico Padrão** informado, para ser possível gerar as demonstrações. A falta desta informação em algum lançamento, provocará uma inconsistência nos saldos.

2. Acesse a tela **Demonstrativos Contábeis**
   **Menu:** Contabilidade »Consultas  »  ECD  » Demonstrativos Contábeis

- Na janela Procurando por Empresa, selecione sua empresa.
- Determine inicialmente o **Período** a ser considerado para geração do relatório.
- Selecione o **Tipo de Período** dentre as opções: Período Comparativo, Período.
  Para a geração de análise em período comparativo, é necessário informar período anterior.
- Informe a referência que os Demonstrativos Contábeis deverão abranger, no campo **Data período**.
- No campo **Apresentação da empresa** defina qual nomenclatura pertinente a empresa que está gerando o demonstrativo deverá ser exibida.
- Por meio do campo **Demonstração de valores** determine como serão exibidos os valores no demonstrativo.
- Por meio do campo **Símbolos para valores negativos** defina como os valores negativos serão apresentados.
- Determine no campo **Formato data p/ impressão** qual o formato a ser utilizado para impressão das datas no demonstrativo.
- Na seção Demonstrativos, selecione **Demonstrativos das mutações do patrimônio líquido - DMPL**.
- Para a geração do relatório **Demonstrativos de Lucros ou Prejuízos Acumulados – DLPA**, aplicam-se as configurações orientadas acima.
