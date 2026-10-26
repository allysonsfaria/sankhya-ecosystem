---
id: "360044608374"
titulo: "Tela Relatório de Conferência PIS/COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD Contribuições"
atualizado_em: "2026-09-30T11:14:49Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Impostos", "CFOP", "Financeiro", "CST", "Relatório de Conferência PIS/COFINS", "br.com.sankhya.mgeliv.rel.conferenciapiscofins", "Relatório de Conferência PIS/COFINS manual", "EFD Contribuições", "Resumo por CST/CFOP; opções para cupons e consolidação", "Escolha \"Empresa\" e \"Período\"; configure o regime de apuração", "Inclui PIS/COFINS exclui ajustes; considera notas modelo 66", "PIS/COFINS"]
---

# Tela Relatório de Conferência PIS/COFINS

**Caminho de acesso:** Livros Fiscais › Relatórios

---

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#oque) [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#como) [Resumo de PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#resumo) | [Outros Resumos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#outros) [Cálculo do Bloco F100](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#f100)    ↳ [Grupo de Receitas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#f100-receitas)    ↳ [Grupo de Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#f100-despesas)    ↳ [Regras para o cálculo dos títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#f100-regras) |
| --- | --- |

## O que é e para que serve

A **Tela Relatório de Conferência PIS/COFINS** reúne as configurações para gerar um relatório em que você verifica os valores de PIS e COFINS dentro de um período determinado, com os respectivos débitos e créditos, destinado a análises simples desses impostos.

Este relatório não considera ajustes, exclusões e compensações referentes à apuração de PIS e COFINS. Ele segue como regra o guia prático do EFD Contribuições, apresentando somente o que tem PIS e COFINS e respeitando as regras de CST, CFOP e demais contidas no manual.

![Imagem 1: Este relatório não considera ajustes, exclusões e compensações referentes à apuração de PIS e COFINS. Ele segue como…](https://ajuda.sankhya.com.br/hc/article_attachments/42431665516951)

## Como usar a tela

Informe, a princípio e obrigatoriamente, a **Empresa** da qual serão verificados os dados dos impostos, bem como o **Período** que a verificação irá abranger.

Verifique também se a aba **Regime de Apuração da Contrib. Social e Aprop. Crédito** da tela **Preferências da Empresa** está configurada. Caso não esteja, o sistema não permite gerar o relatório e exibe a seguinte mensagem ao clicar no botão **Visualizar Relatório**:

**⚠️ Atenção**

O sistema exibe a mensagem "Não foi encontrada a configuração da aba Regime de Apuração da Contrib. Social e Aprop. Crédito da rotina Empresa (Comercial » Preferências » Empresa). Preencha as informações desta aba e gere o relatório novamente."

Ao gerar o relatório, o sistema considera as entradas de notas fiscais de modelo 66 para compor os valores dos créditos de PIS/COFINS, rateados de acordo com os CFOPs dessas entradas. Para que os créditos sejam apresentados no relatório, as notas precisam ser geradas no **Livro ICMS/IPI**.

Após definir os critérios de geração — detalhados nas seções seguintes — clique em **Visualizar Relatório** para apresentar os resultados na tela:

![Imagem 2: Após definir os critérios de geração — detalhados nas seções seguintes — clique em Visualizar Relatório para apresentar…](https://ajuda.sankhya.com.br/hc/article_attachments/42431665518615)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#sumario)

## Resumo de PIS/COFINS

Nesta seção você define os critérios principais de geração do relatório:

- **Resumo por** — determina um dos principais critérios de geração, indicando se o resumo ocorrerá por:
  - **Código de Situação Tributária (CST)**
  - **Código Fiscal de Operações e Prestações (CFOP)**
  - **CFOP/CST**
- **Considerar Cupons fiscais** — define o tratamento dos cupons fiscais na apresentação dos dados:
  - **Sim** — os cupons fiscais também são tratados no relatório
  - **Não** — os cupons não são apresentados no relatório
  - **Somente Cupons** — são considerados apenas os cupons existentes no período definido inicialmente
- **Considera/consolida Matriz e filiais** — determina se as informações da Matriz e de suas filiais são consolidadas na geração do relatório

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#sumario)

## Outros Resumos

Nesta seção, defina os demais critérios a serem analisados na geração do relatório:

- **Todos resumos**
- **Resumo das retenções (F600)**
- **Demonstrativo de Receitas isentas / não tributadas (M400/M800)**
- **Resumo das receitas/despesas financeiras p/ natureza (sem NF – F100)**
- **Resumo crédito PIS/COFINS sobre encargos de depreciação de BENS (F120)**
- **Resumo crédito sobre Bens Incorporados ao Ativo Imobilizado - Créditos com base no Valor de Aquisição (F130)**
- **Resumo Analítico (Quadro F100)**

**ℹ️ Nota**

Ao marcar **Todos resumos**, as demais marcações são desabilitadas para escolha.

Alguns CFOPs e/ou CSTs podem ou não ser considerados no **Programa Validador e Assinador (PVA)** da **Receita Federal do Brasil (RFB)**; isso depende da tributação, do regime e de outros fatores descritos no manual do EFD Contribuições da própria RFB, o que pode divergir deste relatório. É responsabilidade do setor Contábil/Fiscal de cada empresa identificar o que é considerado ou desconsiderado para efeitos de apuração do PIS e COFINS — como, por exemplo, o CST 99 (outras).

O relatório também considera as saídas emitidas a título de devolução de uso e consumo que contêm o registro de cálculo de PIS e COFINS nos impostos do item da nota com CST 49 — os valores dessas saídas são apresentados nos resumos (CST, CFOP ou CFOP/CST) que compõem as linhas totalizadoras a débito.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608374-Tela-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS#sumario)

## Cálculo do Bloco F100

O Bloco F100 refere-se a registros de receitas ou despesas não contempladas pelos demais blocos e que possuem um documento fiscal eletrônico, como recibo, contrato ou nota fiscal de serviço.

### Grupo de Receitas

No grupo de Receitas, são considerados:

- Receitas financeiras
- Juros sobre capital próprio
- Receita sobre aluguéis de bens móveis ou imóveis
- Receitas não operacionais
- Receitas não escrituradas nos blocos A, C e D da EFD Contribuições

### Grupo de Despesas

No grupo de Despesas, são registradas outras operações com direito a crédito, como:

- Contraprestação de arrendamento mercantil
- Aluguel de prédio, máquinas e equipamentos
- Despesas com armazenagem de mercadorias
- Aquisição de bens e serviços a serem utilizados como insumos, com documentação não informada nos blocos A, C e D

### Regras para o cálculo dos títulos

Títulos comuns e tributáveis — como receitas ou despesas de aluguel — são calculados conforme as configurações na natureza do título. Observe as seguintes regras:

- Configure os títulos de receitas e despesas na tela **Movimentação Financeira** de acordo com as preferências dos títulos utilizados.
- Observe se o título está com a opção **Receita** ou **Despesa** definida no campo **Receita/Despesa**.
- No campo **Natureza**, informe a natureza do título conforme definido na tela **Natureza de Receitas e Despesas**.
- Na mesma tela, preencha os campos da aba **PIS/COFINS Todas Empresas**. Para as despesas, configure o respectivo título da mesma forma que no título da receita.

**⚠️ Atenção**

Atente-se ao campo **Regime (EFD PIS/COFINS)** na aba **PIS/COFINS Todas Empresas** da tela **Natureza de Receitas e Despesas** ao utilizá-lo em títulos de Receitas, pois ele determina a forma e o período de cálculo do imposto do título na apuração. Ao definir **Regime de Caixa**, o sistema calcula somente na baixa do título; ao selecionar **Regime de competência**, o cálculo é feito conforme a data de entrada/saída, sem precisar estar baixado.

Para títulos referentes a multa, juros e descontos (receita), o cálculo só ocorre se estes forem parametrizados nas **Preferências da Empresa**, sub-aba **Geração F100** da aba **EFD - Escrituração Fiscal Digital**.

Caso seja necessário alterar dados para o cálculo (ou o não cálculo) do tributo de PIS e COFINS após a conferência prévia — natureza, valor de multa, juros, desconto — atualize-os no campo **Desdob.**, na aba **Geral** da tela **Movimentação Financeira**, para que o sistema recalcule conforme as alterações.

Após as configurações, execute a rotina e confira os dados de maneira sintética com o filtro **Resumo das receitas/despesas financeiras p/ natureza (sem NF – F100)**:

![Imagem 3: Após as configurações, execute a rotina e confira os dados de maneira sintética com o filtro Resumo das…](https://ajuda.sankhya.com.br/hc/article_attachments/42431634960919)

Também é possível gerar o F100 de forma analítica ao acionar a marcação **Resumo Analítico (Quadro F100)**:

![Imagem 4: Também é possível gerar o F100 de forma analítica ao acionar a marcação Resumo Analítico (Quadro F100) :](https://ajuda.sankhya.com.br/hc/article_attachments/42431634968855)
