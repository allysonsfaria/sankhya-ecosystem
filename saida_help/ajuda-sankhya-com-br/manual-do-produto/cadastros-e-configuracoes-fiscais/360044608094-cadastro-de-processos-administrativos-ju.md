---
id: "360044608094"
titulo: "Cadastro de Processos Administrativos Judiciais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Cadastro-de-Processos-Administrativos-Judiciais"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-09-15T14:02:02Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Fiscal", "NF-e", "XML", "br.com.sankhya.mgeliv.cad.processoadmjudicial", "Processos Administrativos Judiciais manual", "EFD Contribuições", "Preencha informações principais validade e autoria", "Defina tipo órgão e tags XML para EFD-Reinf", "Informe detalhes de suspensão e ajuste validade", "EFD-REINF"]
---

# Cadastro de Processos Administrativos Judiciais

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Cadastro-de-Processos-Administrativos-Judiciais#oqueepara) [Dados principais do processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Cadastro-de-Processos-Administrativos-Judiciais#dados-principais) [Configurações para EFD-Reinf e EFD-Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Cadastro-de-Processos-Administrativos-Judiciais#efd-reinf-contribuicoes) | [Configurações XML NF-e (Grupo procRef)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Cadastro-de-Processos-Administrativos-Judiciais#xml-nfe)    ↳ [Retorno de OPME e Notas de Devolução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Cadastro-de-Processos-Administrativos-Judiciais#opme) [Aba Informações da Suspensão de Exigibilidade dos Tributos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Cadastro-de-Processos-Administrativos-Judiciais#suspensao)    ↳ [Uso de fórmulas na sub-aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Cadastro-de-Processos-Administrativos-Judiciais#formulas) |
| --- | --- |

**Módulo:** Livros Fiscais › Arquivos
**Caminho de acesso:** Menu Principal › Livros Fiscais › Arquivos › Processos Administrativos Judiciais

---

## O que é e para que serve

O **Cadastro Processos Administrativos Judiciais** é a tela onde você registra e gerencia os processos administrativos e judiciais da sua empresa. Use-a para alimentar a geração do evento R1070 na [EFD-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553-EFD-Reinf) e do registro 1011 na [EFD-Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es), além de parametrizar a geração automática do grupo de tags `procRef` no XML da NF-e para operações de venda e devolução. A tela não realiza o cálculo ou a apuração dos tributos envolvidos no processo — ela apenas parametriza como o sistema deve tratá-los nas obrigações acessórias.

![tela Processos Administrativos Judiciais com campos Nro. Único do processo, Ativo, Nro. do Processo, datas de validade,…](https://ajuda.sankhya.com.br/hc/article_attachments/11787938151319)

---

## Dados principais do processo

Preencha os campos abaixo para identificar os dados básicos da ação:

- **Nro. Único do processo** — gerado automaticamente pelo sistema ao salvar o cadastro.
- **Ativo** — marque para habilitar o uso do processo no sistema.
- **Nro. do Processo** — informe o código oficial identificador da ação.
- **Data Início da Validade / Data Fim da Validade** — defina o período de vigência do processo.
- **Autoria da Ação Judicial** — indique se a ação foi ingressada pelo próprio contribuinte ou por outra entidade ou empresa.
- **Cidade / Cód. Identificação da Vara** — preencha a cidade onde a ação foi ingressada e o código da vara responsável.
- **Advogado Atuante no processo** — selecione o parceiro correspondente ao advogado responsável pela ação.

---

## Configurações para EFD-Reinf e EFD-Contribuições

### Seção Configurações Reinf

Indique se o processo é do tipo **Administrativo** ou **Judicial**.

### Seção Configurações EFD Contribuições

Selecione o órgão que deu origem ao processo:

- 1 — Justiça Federal
- 3 — Secretaria da Receita Federal do Brasil
- 9 — Outros

Você também pode preencher a **Descrição Complementar**, que será enviada diretamente para o Registro 1011 da EFD-Contribuições.

---

## Configurações XML NF-e (Grupo procRef)

Esta seção controla como o sistema injeta os dados do processo nas notas fiscais emitidas.

#### Gerar tags do grupo procRef no XML da NF-e

**O que faz**
Preenche os dados de Regime Especial do parceiro e gera as tags `<nProc>` e `<indProc>` — Identificador e Indicador de origem do processo, respectivamente — dentro do grupo `<procRef>` do XML.

**Quando usar**
Marque esta opção quando o processo precisar ser referenciado no XML das NF-e de venda ou devolução.

**Como funciona**
Ao marcar esta opção, o campo **Origem do Processo** fica disponível com as seguintes opções:

- 0 — SEFAZ
- 1 — Justiça Federal
- 2 — Justiça Estadual
- 3 — Secex/RFB
- 4 — Confaz
- 9 — Outros

**💡 Dica**

O campo **Tipo do ato concessório** (Termo de Acordo, Regime Especial etc.) fica habilitado apenas quando você selecionar **0 — SEFAZ** como Origem do Processo. As tags `<procRef>` são geradas quando a origem for **0 — SEFAZ** ou **4 — Confaz**.

**Impacto no sistema**
Ao ligar esta marcação, o sistema desabilita o campo **% de Suspensão do Imposto** (fixando-o em 100%) e desabilita as sub-abas **Impostos** e **Tipos de Serviço**, habilitando em seu lugar a sub-aba **Tipo de Operação**.

### Retorno de OPME e Notas de Devolução (Ajuste SINIEF 02/24)

Para garantir a conformidade com o **Ajuste SINIEF 02/24** no retorno físico de Órteses, Próteses e Materiais Especiais (OPME), o sistema permite gerar o grupo `<procRef>` também em notas de devolução.

Ao ligar a marcação **Gerar tags do grupo procRef...**, o sistema habilita a sub-aba **Tipo de Operação** (na aba Informações da Suspensão). Nela, você pode vincular Tipos de Operação (TOPs) com os seguintes Tipos de Movimento (TIPMOV):

- Venda
- Devolução de Compra
- Devolução de Venda

---

## Aba Informações da Suspensão de Exigibilidade dos Tributos

Acesse esta aba para preencher os detalhes da decisão favorável ao contribuinte.

- **Indicativo da Suspensão** — especifique a espécie de decisão deferida (Configurações Reinf).
- **Indicador da natureza da ação judicial** — indique a natureza que caracteriza a ação (Configurações EFD Contribuições).

### Sub-abas de validação

As sub-abas inferiores determinam para quais cenários a decisão será válida. A habilitação delas depende da marcação **Gerar tags do grupo procRef no XML da NF-e**:

- **Marcação ligada:** habilita a sub-aba **Tipo de Operação** (permitindo Vendas e Devoluções).
- **Marcação desligada:** habilita as sub-abas **Impostos** e **Tipos de Serviço**.

**ℹ️ Nota**

Para que o sistema gere o processo na EFD-Reinf, você precisa preencher, no mínimo, as sub-abas **Empresa** e **Impostos**.

### Uso de fórmulas na sub-aba Impostos (Registro 1011)

Para os impostos **PIS/PASEP** e **COFINS** na EFD-Contribuições, o campo **Grupo de campos que serão calculados com as fórmulas** determina como o sistema preencherá o Registro 1011:

- **Não se aplica** — ignora fórmulas. O sistema usa o método padrão.
- **Conforme a escrituração** — use quando a nota foi calculada com os impostos já ajustados pela decisão judicial. A fórmula reflete nos campos 08 a 15 do Registro 1011; os campos 16 a 23 seguem a nota fiscal.
- **Conforme a decisão judicial** — use quando a nota foi calculada com os valores normais, ignorando o processo. A fórmula reflete nos campos 16 a 23 do Registro 1011; os campos 08 a 15 seguem a nota fiscal.

**⚠️ Atenção**

Ao usar **Conforme a escrituração** ou **Conforme a decisão judicial**, as fórmulas cadastradas devem calcular os valores referentes à **regra contrária** à utilizada na nota fiscal. Além disso, todas as fórmulas precisam ser definidas — se nenhuma for definida, o sistema gera o Registro 1011 pelo método padrão.

Ao usar fórmulas, defina todas as variáveis. O botão **Construtor** oferece quatro opções no banco de dados para facilitar a montagem: `ITEM_NOTA`, `ICMS_DIN`, `PIS_DIN` e `COFINS_DIN`.
