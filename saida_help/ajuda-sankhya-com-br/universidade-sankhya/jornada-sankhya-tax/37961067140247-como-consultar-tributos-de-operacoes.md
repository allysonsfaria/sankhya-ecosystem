---
id: "37961067140247"
titulo: "Como consultar tributos de operações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37961067140247-Como-consultar-tributos-de-opera%C3%A7%C3%B5es"
trilha: "Universidade Sankhya > Jornada Sankhya Tax"
atualizado_em: "2026-07-22T14:03:38Z"
rotulos: ["Configuração", "Consulta", "SEFAZ", "Impostos", "NCM", "Sankhya Tax", "CEST"]
---

# Como consultar tributos de operações

## Consulta Tributos

#### Qual é o objetivo de consultar tributos no Sankhya TAX?

A consulta de tributos no Sankhya TAX tem como objetivo oferecer ao usuário uma visão clara e confiável das regras tributárias aplicáveis a cada operação. Através da integração com a ASIS, é possível verificar as tributações relacionadas ao NCM, CEST e estados envolvidos, permitindo maior segurança no planejamento de vendas e nas decisões estratégicas da empresa.

#### Quais problemas essa funcionalidade resolve?

- Dificuldade em identificar corretamente a tributação por estado de origem e destino.
- Incerteza ao calcular impostos em novos mercados.
- Dependência de pesquisas externas para validar tributos.
- Risco de aplicar códigos fiscais incorretos (NCM/CEST).
- Falta de agilidade para apoiar decisões comerciais.

#### Quais são os riscos de não utilizar a consulta de tributos?

Sem utilizar a consulta de tributos, a empresa pode tomar decisões comerciais baseadas em premissas equivocadas, o que compromete a precificação e a margem de lucro. Além disso, aumenta a probabilidade de inconsistências fiscais em operações interestaduais, reduzindo a competitividade e elevando a exposição a contingências legais e financeiras.

#### Cenário de aplicação

A Axis LTDA., distribuidora de bebidas, começou a vender para Goiás e precisou validar a tributação de um energético. Para evitar erros na precificação, o analista acessou a Consulta de Tributos no Sankhya TAX, informou NCM, UF de origem (MG) e destino (GO) e obteve o detalhamento do ICMS, PIS/COFINS e benefícios fiscais aplicáveis. Assim, a Axis garantiu segurança fiscal e definiu o preço correto para atuar com competitividade no novo mercado.

**Tarefa:** Assista ao vídeo de demonstração prática no sistema e siga o passo a passo para configurar os filtros do **Monitoramento Tributário**, validar as alterações detectadas e considerar a aplicação dos ajustes necessários na sua base de testes.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1124842678)

#### É o momento de aplicar o conhecimento adquirido! Veja como consultar tributos no ERP Sankhya

1. **Para consultar tributos**

- Acesse a tela **Sankhya TAX -  Consulta Tributos**
- Clique em “**Consultar** **Tributos**”
- No menu de filtros informe:

  - **NCM**
    Campo obrigatório, oito dígitos sem pontos, deve estar vigente na data de referência.
  - **EX**
    Campo não obrigatório, trará a legislação de forma mais assertiva.
  - **CEST**
    Campo não obrigatório, sete dígitos, trará a legislação de forma mais assertiva.
  - **UF Origem**
    Campo obrigatório, origem do item consultado.
  - **UF Destino**
    Campo obrigatório, destinodo item consultado.
  - **Origem** (CST)
    Campo não obrigatório, trará a legislação de forma mais assertiva.
  - **Regime**
    Campo obrigatório para PIS/COFINS e Simples Nacional.
  - **Atividade**
    Campo obrigatório para PIS/COFINS e Simples Nacional.
  - **Data de referência**
    Campo obrigatório, se não tiver referência exata, usar um período mais longo.
- Acione o botão “**Consultar**” para buscar o resultado.

A tela apresenta o resultado em grades nas abas segmentadas por IPI, IMPOSTO SOBRE IMPORTAÇÃO, PIS/COFINS, ICMS - INTERESTADUAL, ICMS - INTERNO, REFORMA e RESUMO.

2. **Para calcular tributos**

- Acesse a tela **Sankhya TAX -  Consulta Tributos**
- Clique em “**Realizar** **um cálculo**”
- No menu de filtros da aba consulta informe:

  - **Recolhimento**
  - **NCM**
  - **EX**
  - **CEST**
  - **Origem** (CST)
  - **UF de origem**
  - **UF de destino**
- Acione o botão “**Consultar**” para buscar o resultado.
- Selecionando a grade de resultado contida nas abas **ICMS INTERNO** ou **BENEFÍCIOS** o usuário será direcionado para aba **CÁLCULO**.
- Informe **Quantidade**, **Valor Unitário**, **frete**, **seguro**, **despesas** e **descontos** e em seguida acione o botão “**Calcular**”.

Com esses dados, o sistema gera automaticamente o detalhamento tributário, apresentando a aplicação do ICMS próprio, a diferença de alíquotas (DIFAL), além do cálculo das bases e valores correspondentes, como ICMS interno, ICMS destino e FCP quando aplicável

#### Recomendação importante:

- Para realizar uma nova consulta mantendo os dados já registrados, clique no ícone ‘+’, localizado na parte superior da tela ao lado do NCM consultado, e repita os passos anteriores com a nova referência desejada
