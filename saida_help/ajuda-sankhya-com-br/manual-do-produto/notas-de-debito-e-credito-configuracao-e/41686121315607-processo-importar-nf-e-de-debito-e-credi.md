---
id: "41686121315607"
titulo: "Processo importar NF-e de Débito e Crédito (Reforma Tributária)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão"
atualizado_em: "2026-09-01T20:13:21Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "TOP", "Reforma Tributária", "nota de credito", "importar", "nota de debito", "reforma tributaria"]
---

# Processo importar NF-e de Débito e Crédito (Reforma Tributária)

**Módulo:** Comercial
**Caminho de acesso — Tipos de Operação:** Comercial › Arquivo › Cadastros › Tipos de Operação - TOP
**Caminho de acesso — Portal de Importação de XML:** Comercial › Rotinas › Portal de Importação de XML

---

Neste artigo

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#o-que-e)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#antes)
- [Etapa 1 — Cadastrar a TOP com a nova finalidade e o subtipo](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#etapa-1)
- [Campos da finalidade de débito e crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#campos)
- [Etapa 2 — Vincular subtipos a TOPs nas Preferências do Portal](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#etapa-2)
- [Grade de parametrização](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#grade)
- [Etapa 3 — Importar o XML no Portal](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#etapa-3)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#pontos)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/41686121315607-Processo-importar-NF-e-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria#faq)

## O que é e para que serve

Este processo parametriza o Sankhya Om para importar NF-e de Nota de Crédito (`finNFe=5`) e Nota de Débito (`finNFe=6`) emitidas sob a Reforma Tributária (LC 214/2025), quando a nota é de **emissão própria** — emitida pelo próprio parceiro fora do Sankhya Om, como em um marketplace ou outra solução fiscal. **Ele não se aplica** a NF-e de Débito e Crédito emitidas por fornecedores ou clientes na relação comercial padrão, nem às finalidades já existentes (Normal, Complementar, Ajuste e Devolução), cujo comportamento permanece inalterado. Sem essa parametrização, o Sankhya Om bloqueia a importação de qualquer XML com `finNFe=5` ou `finNFe=6`.

## Antes de começar

| **⚠️ Ainda não sabe se a sua nota é de emissão própria**?  Ela é de emissão própria quando o parceiro emite a NF-e fora do Sankhya Om — em marketplace ou outra solução fiscal — e depois importa o XML aqui. Se a nota de Débito ou Crédito chegou a você pela relação comercial padrão (emitida por fornecedor ou cliente), ela continua sendo tratada como documento de terceiros: não use este fluxo, **nenhuma configuração é necessária.** |
| --- |

Antes de criar as TOPs, resolva estes dois pontos:

- Valide com a equipe fiscal o significado de cada subtipo de `tpNFCredito` e `tpNFDebito` que sua operação usa. Uma TOP configurada com o subtipo errado gera escrituração incorreta de IBS/CBS.
- Planeje uma TOP separada para cada subtipo que sua operação emite ou recebe. Subtipos sem TOP vinculada não aparecem na grade de Preferências e bloqueiam a importação do documento correspondente.

## Etapa 1 — Cadastrar a TOP com a nova finalidade e o subtipo

Acesse **Comercial › Arquivo › Cadastros ›** [**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e crie ou edite a TOP que será usada para o subtipo em questão.

### Campos da finalidade de débito e crédito

- **Finalidade da NF-e** — selecione **Import. Doc. Débito (Emissão Própria)** para NF-e com `finNFe=6`, ou **Import. Doc. Crédito (Emissão Própria)** para NF-e com `finNFe=5`. Cada finalidade habilita exclusivamente o campo de subtipo correspondente.
- **Tipo de Nota Fiscal de Débito** — exibido quando a finalidade selecionada for "Import. Doc. Débito (Emissão Própria)". Selecione o subtipo de `tpNFDebito` correspondente ao documento que esta TOP cobrirá.
- **Tipo de Nota Fiscal de Crédito** — exibido quando a finalidade selecionada for "Import. Doc. Crédito (Emissão Própria)". Selecione o subtipo de `tpNFCredito` correspondente ao documento que esta TOP cobrirá.

| ℹ️ Nota  As finalidades "Import. Doc. Débito (Emissão Própria)" e "Import. Doc. Crédito (Emissão Própria)" são exclusivas para documentos da Reforma Tributária. A finalidade "Import. Doc. (Emissão Própria)" existente não foi alterada e continua funcionando normalmente para os cinco tipos de movimento já parametrizados. |
| --- |

| ⚠️ Atenção  Crie uma TOP separada para cada subtipo que sua operação utiliza. Uma mesma TOP não pode cobrir mais de um subtipo — a grade de Preferências vincula exatamente um subtipo a uma TOP por linha. |
| --- |

## Etapa 2 — Vincular subtipos a TOPs nas Preferências do Portal

Acesse **Comercial › Rotinas ›** [**Portal de Importação de XML**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), abra [**Outras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)[**Opções**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) **›** [**Preferências para importação de NF-e de Emissão Própria**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#pref.paraimport.denf-edeemiss%C3%A3o...) e localize a seção **Notas de Débito e Crédito (Reforma Tributária)**.

### Grade de parametrização

A grade lista automaticamente os subtipos já cadastrados nas TOPs criadas na Etapa 1, agrupados por natureza:

- **Nota de Crédito** — subtipos de `tpNFCredito` vinculados a TOPs com finalidade "Import. Doc. Crédito (Emissão Própria)".
- **Nota de Débito** — subtipos de `tpNFDebito` vinculados a TOPs com finalidade "Import. Doc. Débito (Emissão Própria)".

Para cada linha da grade, selecione a TOP correspondente na coluna **Tipo de Operação**. O seletor exibe apenas TOPs elegíveis para a natureza da linha: TOPs de crédito para linhas de `finNFe=5` e TOPs de débito para linhas de `finNFe=6`.

| ℹ️ Nota  A grade é extensível: ao cadastrar uma nova TOP com finalidade de débito ou crédito e um subtipo ainda não listado, a linha aparece automaticamente na grade sem necessidade de alteração de tela ou código. O preenchimento por linha é opcional — subtipos sem TOP configurada não bloqueiam a abertura das Preferências, mas bloqueiam a importação do documento correspondente. |
| --- |

| 💡 Dica  Se a grade estiver vazia ou não listar o subtipo esperado, verifique se a TOP foi salva corretamente com a finalidade e o subtipo preenchidos na Etapa 1. |
| --- |

## Etapa 3 — Importar o XML no Portal

Com as etapas 1 e 2 concluídas, acesse **Comercial › Rotinas ›** [**Portal de Importação de XML**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#pref.paraimport.denf-edeemiss%C3%A3o...) e importe normalmente o XML da NF-e de Débito ou Crédito.

Durante a importação, o Sankhya Om inspeciona o campo `finNFe` do XML. Para `finNFe=5`, consulta a grade com a chave (Nota de Crédito + subtipo de `tpNFCredito`) para resolver a TOP. Para `finNFe=6`, consulta com a chave (Nota de Débito + subtipo de `tpNFDebito`). A importação é concluída normalmente com a TOP configurada.

| 🚨 Risco operacional  Se o subtipo do XML não estiver configurado na grade, o Sankhya Om bloqueia a importação e exibe a mensagem "Tipo de Operação não informado em Outras Opções Preferências para importação de NF-e de Emissão Própria". Retorne à Etapa 1, crie a TOP para o subtipo indicado, vincule-a na grade (Etapa 2) e tente importar novamente. |
| --- |

## Pontos de atenção

- O comportamento de importação para NF-e com `finNFe=1` (Normal), `finNFe=2` (Complementar), `finNFe=3` (Ajuste) e `finNFe=4` (Devolução) permanece inalterado. Os campos fixos de Venda, Devolução de Venda, Compra, Devolução de Compra e Complemento nas Preferências também não foram alterados.
- Uma TOP com finalidade "Import. Doc. Débito (Emissão Própria)" só é elegível para seleção em linhas de `finNFe=6` na grade. Uma TOP com finalidade "Import. Doc. Crédito (Emissão Própria)" só é elegível para linhas de `finNFe=5`. O seletor de Tipo de Operação aplica esse filtro automaticamente.
- A resolução de TOP na importação é feita por chave exata (finalidade + subtipo). Não há fallback para uma TOP genérica — cada subtipo precisa de sua própria linha configurada na grade.

## Perguntas frequentes

### A mensagem "Tipo de Operação não informado em Outras Opções > Preferências para importação de NF-e de Emissão Própria" continua aparecendo depois que configurei a grade. O que verifico?

Confirme que a TOP foi salva com a finalidade correta ("Import. Doc. Débito (Emissão Própria)" ou "Import. Doc. Crédito (Emissão Própria)") e com o subtipo preenchido. Em seguida, abra as Preferências e verifique se o subtipo do XML aparece na grade e se a coluna Tipo de Operação está preenchida para aquela linha. Se o subtipo não aparecer na grade, a TOP não foi salva corretamente — refaça o cadastro.

### Preciso criar uma TOP para cada subtipo ou posso reutilizar a mesma TOP para vários subtipos?

Cada subtipo exige uma TOP própria. A grade vincula exatamente um subtipo a uma TOP por linha, e o campo de subtipo no cadastro de TOP aceita apenas um valor. Reutilizar a mesma TOP para subtipos diferentes não é possível pelo design da parametrização.

### Um novo subtipo de `tpNFDebito` ou `tpNFCredito` foi publicado por uma NT. Preciso atualizar alguma tela?

Não. Basta cadastrar uma TOP com a nova finalidade e o novo subtipo. A grade de Preferências absorve a linha automaticamente sem necessidade de alteração de tela ou código.
