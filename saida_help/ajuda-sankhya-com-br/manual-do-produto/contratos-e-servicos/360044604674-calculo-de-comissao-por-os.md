---
id: "360044604674"
titulo: "Cálculo de Comissão por OS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604674-C%C3%A1lculo-de-Comiss%C3%A3o-por-OS"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:04:13Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Faturamento", "Cálculo de Comissão por OS", "br.com.sankhya.os.rotinas.calculo.comissao", "Cálculo de Comissão por OS manual", "Vendedor", "Ordem de Serviço", "Comissão", "Financeiro", "OS", "Cálculo de Comissão por OS: Automatização Eficiente"]
---

# Cálculo de Comissão por OS

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311241407511) Módulo: Contratos e Serviços > Rotinas
```

---

Essa tela tem por objetivo automatizar o cálculo de produtividade dos colaboradores da empresa, aumentando assim, a segurança e a eficiência deste processo.

[Configurações necessárias para o Cálculo de Produtividade por OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604674-C%C3%A1lculo-de-Comiss%C3%A3o-por-OS#configuraesnecessriasparaoclculodeprodutividadeporos)

[Rotina para cálculo de Comissão por OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604674-C%C3%A1lculo-de-Comiss%C3%A3o-por-OS#rotinaparaclculodecomissoporos)

![Imagem 2: Rotina para cálculo de Comissão por OS](https://ajuda.sankhya.com.br/hc/article_attachments/5146234704407)

## Configurações necessárias para o Cálculo de Produtividade por OS

No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), o Parceiro deverá ser do **"Tipo"** igual a **"Cliente"**, **"Fornecedor"**, **"Usuário"** e **"Vendedor"**.

Na tela [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133), aba **"Geral"**, define-se em **"Pagamento de Comissão por data de"** se a produtividade será paga em regime de caixa (**"Negociação"**) ou competência (**"Baixa"**).

Ainda na tela acima, o campo **"Usar valor p/ comissão de OS"** definirá se o valor base da hora que entrará na regra de produtividade irá variar por **"Vendedor"** (Valor hora p/ comissão de OS) ou por **"Negociação"** (Valor Unitário do Serviço no Pedido).

Os campos **"Parceiro"** e **"Funcionário"** da tela acima deverão ser informados para geração da produtividade para a Folha de pagamento ou Financeiro. O campo Parceiro liga o Usuário com o Vendedor e Funcionário.

**Nota:**a marcação **"Recebe Hora Dobrada"**, localizada também na aba Geral do Cadastro de Vendedores/Compradores, define se o Vendedor receberá comissão sobre a hora extra com valor dobrado, porém, existem casos em que a comissão sobre hora extra é paga como horas normais; para isto, é necessário desabilitar a marcação e, uma vez desmarcado, quando o sistema for realizar o cálculo do valor da hora, o **"Vlr. Hora Extra Comissão"** será igual ao **"Vlr.Hora Comissão"**.

**Observação:**ao desmarcar a opção acima não influencia nos valores das horas para o faturamento.

No [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abavenda), deve-se realizar as seguintes configurações:

- Deve-se efetuar a marcação **"Calcular comissão"** para definir quais os serviços que calcularão a Produtividade de OS.
- Ao efetuar a marcação **"Hora dobrada"** tem-se que esta será utilizada tanto para o faturamento quanto para o cálculo de produtividade pois, poderão existir serviços desenvolvidos internamente na Empresa, por exemplo, uma customização, que são realizados fora do horário e não são faturados para o cliente como adicional de hora extra; sendo assim, a produtividade adicional também não é paga.

No [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba **"O.S"** define-se se a TOP calculará ou não a produtividade e a comissão sobre execução de OS efetuando-se a marcação **"Calcular comissão para OS."**.

Ainda referente à tela acima, no campo **"Faturamento relacionado a Ordem de Serviço"** defina a forma de calcular a comissão; tem-se as seguintes opções:

- **Pelo Mód. Serviço para O.S. Fechadas:** Ao selecionar esta opção, a produtividade será calculada em regime de caixa, ou seja, quando o valor for recebido (baixado), o sistema pagará todas as OS's ligadas ao pedido.
- **Pelo Mód. Serviço por Horas de O.S. Executadas:** Por meio desta, a produtividade também será paga pela baixa; no faturamento, as OS's são ligadas à Nota Fiscal, desta forma, sempre que um título for baixado, as OS's serão pagas.
- **Pelo Mód. Serviço pelas Parcelas do Financeiro:** Com esta opção, a produtividade será paga em regime de competência, pois um pedido poderá dar origem à várias notas e este Tipo de Negociação é do tipo pacote fechado.
- **Pelo Mód. Serviço todas as Parcelas do Financeiro:** Caso escolha esta, a produtividade será paga pela Baixa ou pela Competência, caso o Financeiro esteja baixado no sistema.
- **Pela Central de Atendimento ao Cliente:** Escolhendo-se esta opção, o faturamento não ocorrerá pelo Módulo de Serviços e sim, pela Central de Atendimento ao Cliente.
- **Pelo Mód. Serviço ou pela Central (todas Parcelas) e Pelo Mód. Serviço todas as Parcelas do Financeiro:** Estas opções permitem o faturamento tanto pelo Módulo Comercial quanto pelo Módulo de Serviços.
- **Não faturar:** Através desta opção, o sistema não fatura mas poderá calcular produtividade para tratamento de OS's bonificadas para os clientes e para as quais o colaborador terá direito à produtividade.

Na rotina [Índice de Produtividade por Executante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604934) serão registrados os índices para o cálculo do percentual (%) de Produtividade. Este percentual poderá ser composto por até 3 índices, que são definidos de acordo com as Regras de Negócios de cada Empresa, através de uma **"Trigger"** específica.

A fórmula utilizada para o Cálculo de Comissão por O.S. é: Horas Produzidas (OS) \* Valor da Hora \* IE. Onde: IE=Indice1 \* Indice2 \* Indice3.

- **Índice 1(\*):** Refere-se ao **"IF (Índice Fixo)"**. Este é o único índice de preenchimento obrigatório. O Percentual de Produtividade poderá ser calculado apenas por este índice, se assim ficar definido na Regra de Negócios da Empresa.
- **Índice 2:** Este índice refere-se ao **"INT (Índice de Nível Técnico)"** e varia de acordo com a posição do colaborador na Grelha.
- **Índice 3:** Refere-se ao **"IE (Índice de Efetividade)"** sendo que este índice é variável e podem existir regras para aplicá-lo, como: atingir meta, pontualidade etc.

Vejamos um exemplo:

Supondo que será calculado o Percentual de Produtividade para Monitor Pleno:

**Índice 1(\*):** Refere-se ao IF (Índice Fixo). Para este exemplo definimos aqui o valor 3.

**Índice 2:** Este índice refere-se ao INT (Índice de Nível Técnico). Neste exemplo vale 1,7.

**Índice 3:** Refere-se ao IE (Índice de Efetividade). No nosso exemplo este terá valor 2.

Logo, no nosso exemplo, o cálculo de Percentual de Produtividade para o Monitor Pleno será: 3\*1,7\*2= 10,2%.

**Nota:**estes índices são históricos, ou seja, deverão ser inseridos todos os meses para realização do cálculo.

Após o lançamento dos índices, deve-se utilizar esta rotina de Cálculo de Comissão por OS e calcular a produtividade das OS's no período desejado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604674-C%C3%A1lculo-de-Comiss%C3%A3o-por-OS#top)

## Rotina para cálculo de Comissão por OS

Essa tela é utilizada para o Cálculo de Comissões relacionadas à execução de itens de Ordens de Serviço para um determinado Vendedor.

O Vendedor está relacionado ao executante da OS, pois cada Executante está ligado a um Parceiro que, por sua vez, está ligado a um Vendedor.

No painel lateral da tela estão presentes os filtros e, também, um painel de apresentação do **"Resumo"**.

Pode-se utilizar um filtro personalizado configurado através do **"Assistente de filtro"** ou utilizar os campos de filtros estáticos presentes na tela.

**Observação:** o campo **"Centro de Resultado"**, refere-se ao Centro de Resultado ligado à nota da OS. O campo **"Centro de Resultado do Executante"** filtra por Centro de Resultado do Executante, ou seja, do usuário que executou. A **"Empresa do Executante"** filtra de acordo com a empresa do executante.

O painel Resumo exibirá a soma do **"Vlr. Total Comissão"** dos itens da grade, assim como a somatória das Horas Trabalhadas.

A grade desta tela poderá ter a exibição das colunas configurada e também, será possível imprimir seus dados. Sobre a grade estão presentes os botões **"Remover Selecionados"** e **"Remover NÃO Selecionados"**, para facilitar a manipulação dos dados.

Quando aplicamos o filtro, será exibido o resultado na grade com o Cálculo da Comissão efetuado.

Para confirmar os valores do Cálculo da Comissão, deve-se utilizar o botão **"Gravar Comissão"**. Este botão salvará os dados da grade na tabela de comissões de acordo com o **"Núm. OS"**, **"Sub-OS"** e **"Cód. Vendedor"**.

O botão **"Recalcular Vlr. Hora"** poderá ser visualizado pelo usuário SUP ou usuários que possuam o acesso especial **"Recalcular Valor-Hora"** concedido através da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos). A ação deste botão dependerá da base de dados do cliente.

**Importante:**para utilizar o recurso acima deve-se entrar em contato com a Sankhya, pois, esta rotina possui uma Trigger específica que deverá passar pela análise dos nossos DBAs para cada Regra de Negócio.

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16024485408663) Acesse também:

[Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604674-C%C3%A1lculo-de-Comiss%C3%A3o-por-OS#top)
