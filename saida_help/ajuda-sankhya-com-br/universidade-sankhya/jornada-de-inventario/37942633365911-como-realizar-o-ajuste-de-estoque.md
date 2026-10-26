---
id: "37942633365911"
titulo: "Como realizar o ajuste de estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37942633365911-Como-realizar-o-ajuste-de-estoque"
trilha: "Universidade Sankhya > Jornada de Inventário"
atualizado_em: "2026-07-22T14:04:16Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "Estoque", "Sankhya"]
---

# Como realizar o ajuste de estoque

| Categoria |
| --- |
| [Qual é o objetivo de se realizar o ajuste de estoque?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37942633365911-Como-realizar-o-ajuste-de-estoque#h_01KFXNNTDP6HYRKT500RK3AQEJ) |
| [Quais problemas esse recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37942633365911-Como-realizar-o-ajuste-de-estoque#h_01KFXNP35HH4YZTBY5W1ECHANK) |
| [Quais os riscos de não realizar o ajuste de estoque?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37942633365911-Como-realizar-o-ajuste-de-estoque#h_01KFXNR3JG3AXTR74BQMWRKEBX) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37942633365911-Como-realizar-o-ajuste-de-estoque#h_01KFXNRA11FME0D20XZEKWV9PV) |
| [Cenário prático e passo a passo para realizar a atividade no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37942633365911-Como-realizar-o-ajuste-de-estoque#h_01KFXNRT3N24TZVP73JP3DXWCT) |
| [Vamos lá! Transforme a maneira como você gerencia seguindo o passo a passo do Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37942633365911-Como-realizar-o-ajuste-de-estoque#h_01KFXNS0D50Y6FAF2H80S7M072) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37942633365911-Como-realizar-o-ajuste-de-estoque#h_01KFXNSAGPZWQ58ZBNJKD978HK) |

## Ajuste de estoque

#### Qual é o objetivo de se realizar o ajuste de estoque?

O ajuste de estoque tem como objetivo alinhar os dados do sistema com a realidade física dos produtos armazenados, sempre que forem identificadas diferenças durante uma contagem ou análise. A correção garante que as quantidades registradas estejam atualizadas a partir daquele momento, refletindo com exatidão o inventário real. Isso fortalece o controle interno, sustenta decisões operacionais e contribui para um fluxo de trabalho mais seguro e eficiente.

#### Quais problemas esse recurso resolve?

- Dificuldade em manter registros consistentes após movimentações não lançadas.
- Falhas no controle de estoque por inversão de produtos ou erros de conferência.
- Perda de rastreabilidade sobre itens com variações não justificadas.
- Planejamento desalinhado com a disponibilidade real de produtos.
- Desconexão entre áreas operacionais e contábeis por ausência de correção das divergências.

#### Quais os riscos de não realizar o ajuste de estoque?

Negligenciar os ajustes de estoque compromete a confiabilidade dos dados e pode gerar uma cadeia de impactos operacionais e financeiros. Entre os riscos estão rupturas por falta de reposição adequada, compras desnecessárias devido a registros incorretos, aumento de perdas não detectadas e falhas na prestação de contas fiscais. Além disso, a empresa pode enfrentar penalidades em auditorias, atrasos na operação e insatisfação do cliente por falta de produtos disponíveis ou informações imprecisas.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052006686)

#### Cenário prático e passo a passo para realizar a atividade no sistema

**Contexto:** Após a realização de um inventário físico no setor de notebooks, a equipe de estoque da TechTools identificou divergências entre as quantidades registradas no ERP e o estoque real. Foram constatadas sobras e faltas em determinados itens, causadas por movimentações não registradas e possíveis erros operacionais. Diante disso, o gestor solicitou providências imediatas para corrigir a base de dados.

**Tarefa:** Realize os ajustes de estoque no ERP Sankhya, alinhando os saldos registrados com a contagem física apurada. Em seguida, analise e registre as possíveis causas das divergências encontradas, como movimentações manuais não lançadas ou falhas no processo de conferência.

#### Vamos lá! Transforme a maneira como você gerencia seguindo o passo a passo do Sankhya

1. **Gerar relatório de divergências da contagem**

- Acesse a tela **Entradas e saídas**
  Menu: Comercial » Relatórios » Entradas e saídas
- Clique na seta para abrir a pasta Indicadores.
- Repita o processo para abrir as subpastas **Estocagem** e **Gerência de estoque**.
- Selecione o relatório **407 - Relatório de Divergência de Contagem** .
- Informe a **Data da cópia** e **Data da contagem** nos campos indicados.
- Informe o código da empresa no campo **Cód. Empresa**.
- Clique no botão “**OK**”.

**Atenção!**
Caso algum dos produtos cadastrados em sua base de testes estiver em poder de terceiros, o ajuste de estoque será impedido. Ao executar a rotina, o sistema verifica todos os produtos estocados na empresa informada. 

Para identificar o **Parceiro** responsável pelo armazenamento, acesse o cadastro do produto na tela:

**Produtos** (Configurações » Cadastros » Produtos » Produtos), aba **Estoque**.   

**Importante:**

Se a base de testes possuir produtos em poder de terceiros, **crie um filtro específico** na tela **Ajuste de Estoque** (Inventário » Arquivo » Ajuste de Estoque) para excluí-los da seleção antes de realizar o ajuste.

**Filtro de Parceiro**

- Clique no botão ”**Filtros**”.
- Clique no botão “**+ Filtro**” (**Cadastrar Filtro**).
- Informe o nome **Parceiro** no campo “**Nome do Filtro**”.

**1º campo**

- Selecione a opção **Cód. Parceiro**.

**2º campo**

- Selecione a opção **Igual (=)**.

**3º campo**

- Informe **0** - **<SEM PARCEIRO>**.

2. **Ajuste de estoque**

- Acesse a tela **Ajuste de Estoque**
  Menu: Inventário » Arquivo » Ajuste de Estoque.
- Informe a **Empresa** no campo indicado.
- Caso tenha realizado a cópia e a contagem por **Local**, informe no campo indicado.
- No campo **Preço unitário** selecione a opção **Usar o preço informado na TOP.**
- Informe as datas de **Cópia** e **Contagem** nos campos indicados.
- Clique no botão “**Ajustar**”.

**Pop-up Notas Geradas**

- As notas de Saída e Entrada para ajuste do estoque serão apresentadas nesta caixa

**Entrada**

- Dê um duplo clique sobre a nota de entrada gerada para ser direcionado à Central de Compras
- Retorne ao relatório emitido no início da aula e verifique a quantidade e os produtos descritos
- Ajuste as quantidades conforme o relatório
- Clique em “**Confirmar**” para aprovar a nota.

**Saída**

- Dê um duplo clique sobre a nota de saída gerada para ser direcionado à Central de Vendas
- Retorne ao relatório emitido no início da aula e verifique a quantidade e os produtos descritos
- Ajuste as quantidades conforme o relatório
- Clique em “**Confirmar**” para aprovar a nota.

**Observação:** As operações de correção utilizam as TOPs de Ajuste de Estoque e não geram lançamentos no financeiro. Elas servem exclusivamente para realizar entradas e saídas no estoque, com o objetivo de alinhar os saldos físicos aos registros do sistema.

#### Correção e Repetição

- Revise os registros para confirmar se as operações foram concluídas.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo, retorne no vídeo demonstrativo novamente caso necessário.
