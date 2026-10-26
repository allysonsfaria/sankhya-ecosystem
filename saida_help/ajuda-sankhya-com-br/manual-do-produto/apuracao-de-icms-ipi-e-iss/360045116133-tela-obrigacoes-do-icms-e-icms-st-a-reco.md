---
id: "360045116133"
titulo: "Tela Obrigações do ICMS e ICMS ST a Recolher"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Apuração de ICMS, IPI e ISS"
atualizado_em: "2026-09-23T14:39:32Z"
rotulos: ["AJUDA DO SKW", "manual", "Fiscal", "SEFAZ", "ICMS", "Impostos", "EFD", "ICMS DIFAL", "ICMS FCP", "Obrigações do ICMS e ICMS ST a Recolher", "br.com.sankhya.mgeliv.cad.obrigacoesicmsstrecolher", "Obrigações do ICMS e ICMS ST a Recolher manual", "ICMS ST", "Informe obrigações ICMS/ICMS ST", "Preencha campos e selecione tipo de apuração", "Dados alimentam registros E116 ou E250 no SPED"]
---

# Tela Obrigações do ICMS e ICMS ST a Recolher

**Módulo:** Livros Fiscais › Avançado

**Caminho de acesso:** Menu Principal › Livros Fiscais › Avançado › Escrituração Fiscal Digital › Obrigações do ICMS e ICMS ST a Recolher

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#oque)
- [Campos da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#campos)
- [Integração com o Cadastro de Estados (GNRE)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#gnre)
- [Registros gerados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#registros)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#atencao)

## O que é e para que serve

A **Tela Obrigações do ICMS e ICMS ST a Recolher** registra os dados das obrigações a recolher referentes ao ICMS ou ao ICMS ST, discriminando os pagamentos realizados ou a realizar do período. Conforme o imposto informado, os dados alimentam registros diferentes do SPED Fiscal: o `E116` (ICMS) ou o `E250` (ICMS ST). A tela **não** apura o imposto nem gera o arquivo da EFD — ela apenas registra as obrigações que serão levadas ao arquivo na geração da escrituração.

![Imagem 1: A Tela Obrigações do ICMS e ICMS ST a Recolher registra os dados das obrigações a recolher referentes ao ICMS ou ao…](https://ajuda.sankhya.com.br/hc/article_attachments/4403007159447)

---

## Campos da tela

Preencha os campos abaixo para lançar a obrigação a recolher:

- **Empresa** — a empresa para a qual a obrigação de recolhimento está sendo lançada.
- **Referência** — uma data de preferência para o seu controle, como a data de referência do imposto.
- **Desc. Processo** — o descritivo dos dados pertinentes à obrigação a recolher.
- **UF** — o estado ao qual a empresa do recolhimento pertence.
- **Código** — o tipo de recolhimento que está sendo lançado, com as opções **Antecipação do diferencial de alíquotas do ICMS**, **ICMS da substituição tributária pelas entradas**, **ICMS resultante da alíquota adicional dos itens incluídos no Fundo de Combate à Pobreza**, **Antecipação do ICMS da importação**, **ICMS normal a recolher**, **Outras obrigações do ICMS**, **Antecipação tributária**, **ICMS da substituição tributária pelas saídas para o Estado** e **ICMS da substituição tributária pelas saídas para outro Estado**. Quando o campo **Código** da aba GNRE Unidade Federativa da tela **Cadastro de Estados** estiver preenchido, este campo é configurado com a mesma opção.
- **Código da Receita (DIME)** — o código da receita DIME, conforme a Portaria 164 de 14/07/2004.
- **Código Classe Vencimento (DIME)** — a classe de vencimentos conforme a Portaria 269, de até 20 caracteres.
- **Valor** — o valor da obrigação a recolher.
- **Data Vencimento** — a data de vencimento da obrigação de recolhimento lançada.
- **Código Receita** — preenchido de acordo com a Tabela de Códigos de Receita definida pelas Secretarias de Fazenda dos Estados ou do Distrito Federal.
- **Nro. Processo** — o número do processo ou auto de infração ao qual a obrigação está vinculada, se houver. Até 2022 permite até 15 caracteres; a partir de 2023, até 60 caracteres.
- **Indicador** — o órgão responsável pela origem do processo, com as opções **Sefaz**, **Justiça Federal**, **Justiça Estadual** e **Outro**.
- **Desc. Complementar** — o descritivo dos dados complementares pertinentes à obrigação a recolher.
- **Indicador de Sub-Apuração** — indica se a obrigação pertence ou não a uma sub-apuração.

#### Tipo Apuração

**O que faz:** define qual imposto está tendo o recolhimento lançado, com as opções **ICMS**, **ICMS ST**, **ICMS DIFAL** e **ICMS FCP**.

**Como funciona:** quando o campo **Tipo Apuração** da aba GNRE Unidade Federativa da tela **Cadastro de Estados** estiver preenchido, este campo é configurado automaticamente com a mesma opção.

**Impacto no sistema:** com **ICMS**, os dados alimentam o registro `E116`; com **ICMS ST**, alimentam o `E250` (ver [Registros gerados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#registros)).

**⚠️ Atenção**

Os campos **Empresa**, **Referência** e **Tipo Apuração** são campos chave: uma vez informados e confirmados, não podem mais ser alterados. Ao tentar alterá-los, o sistema exibe "Não é possível alterar o valor de um campo chave do registro."

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#sumario)

---

## Integração com o Cadastro de Estados (GNRE)

Os campos **Tipo Apuração** e **Código** são preenchidos automaticamente a partir da aba **GNRE Unidade Federativa** da tela **Cadastro de Estados**, quando lá estiverem preenchidos. Para a busca do **Código da Receita (DIME)** e do **Código Classe Vencimento (DIME)** usados no financeiro, o sistema segue esta hierarquia:

1. Se os campos **Código da Receita (DIME)** e **Código Classe de Vencimento (DIME)** da aba **Geral** do Cadastro de Estados estiverem preenchidos, o sistema usa essas informações no financeiro.
2. Se esses campos não tiverem dados, o sistema os busca nos campos **Código da Receita (DIME) p/ FCT ST** e **Código Classe Vencimento (DIME) p/ FCP ST** da aba Geral do Cadastro de Estados.
3. Se os campos da aba Geral também não estiverem preenchidos, o sistema busca os valores nos campos **Código da Receita (DIME)** e **Código Classe Vencimento (DIME)** desta própria tela.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#sumario)

---

## Registros gerados

Os dados informados alimentam os registros da EFD conforme o **Tipo Apuração**:

- **Tipo Apuração = ICMS** → registro `E116`. A soma do valor das obrigações deve ser igual à soma dos campos `VL_ICMS_RECOLHER` e `DEB_ESP` do registro `E110`.
- **Tipo Apuração = ICMS ST** → registro `E250`. A soma do valor das obrigações deve ser igual à soma dos campos `VL_ICMS_RECOL_ST` e `DEB_ESP_ST` do registro `E210`.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116133-Tela-Obriga%C3%A7%C3%B5es-do-ICMS-e-ICMS-ST-a-Recolher#sumario)

---

## Pontos de atenção

- Os campos **Empresa**, **Referência** e **Tipo Apuração** ficam bloqueados após a confirmação e não podem ser alterados.
- Os campos **Tipo Apuração** e **Código** são autopreenchidos a partir da aba GNRE Unidade Federativa do Cadastro de Estados quando lá estiverem preenchidos.
- O limite do campo **Nro. Processo** muda por ano de referência: até 15 caracteres até 2022 e até 60 caracteres a partir de 2023.
- O texto do artigo detalha o comportamento apenas para ICMS e ICMS ST; para **ICMS DIFAL** e **ICMS FCP** não há comportamento descrito.
