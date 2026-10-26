---
id: "7053152322839"
titulo: "Tela Consultar a Média Diária dos Impostos ICMS/ST"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7053152322839-Tela-Consultar-a-M%C3%A9dia-Di%C3%A1ria-dos-Impostos-ICMS-ST"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Rastreamento e cálculo"
atualizado_em: "2026-09-21T13:50:03Z"
rotulos: ["Relatórios", "Livros Fiscais", "ICMS", "Impostos", "EFD", "br.com.sankhya.mgeliv.mov.consultaimpostos", "Configuração de filtros", "Cálculo de médias", "Exportação de dados", "Média Diária dos Impostos ICMS/ST", "Cálculo de impostos diários", "Exportação para PDF", "ST", "FCP"]
---

# Tela Consultar a Média Diária dos Impostos ICMS/ST

**Módulo:** Livros Fiscais › Relatórios
**Caminho de acesso:** Menu Principal › Livros Fiscais › Relatórios › Consultar a Média Diária dos Impostos ICMS/ST
**Esta tela está disponível a partir da versão 4.13.**

## O que é e para que serve

A **Tela Consultar a Média Diária dos Impostos ICMS/ST** exibe as médias diárias já calculadas dos impostos ICMS, ST e FCP do ST, utilizadas na geração do SPED Fiscal para compor os valores dos registros C181, C185, C186, H010 e H030 — veja o detalhamento desses registros em [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI). Esta tela é apenas de consulta: ela não calcula os valores exibidos nem gera o arquivo da EFD. O cálculo das médias é realizado durante a geração do arquivo da EFD Fiscal, a partir das configurações feitas na aba Restituição/Complementação de ST.

![Painel de filtros da tela Consultar a Média Diária dos Impostos ICMS/ST, com os campos Empresa, Produto, Referência,…](https://ajuda.sankhya.com.br/hc/article_attachments/7053513189143)

## Como usar a tela

No painel de filtros, na lateral da tela, informe os campos abaixo antes de consultar:

- **Empresa** — campo obrigatório.
- **Referência** — campo obrigatório.
- **Produto** — também obrigatório. Se não for informado, o Sankhya Om exibe a mensagem "Não foi informado nenhum produto no filtro rápido ou personalizado. Favor informar um produto e realizar a consulta novamente."

**ℹ️ Nota**

Se você configurar, nos filtros personalizados, a busca por mais de um produto, o Sankhya Om traz as informações desses produtos independentemente do que foi informado no campo **Produto** — os filtros personalizados são soberanos aos filtros padrão da tela.

- **Tipo Imposto** — define quais impostos aparecem na consulta: **ICMS**, **ST**, **BASE ST** ou **FCP**.
- **Tipo Média** — define o tipo de média a consultar: **Diária** ou **Inventário**.

Depois de aplicar os filtros, a grade central exibe os resultados encontrados — veja o detalhamento dos campos em [Grade de Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/7053152322839-Tela-Consultar-a-M%C3%A9dia-Di%C3%A1ria-dos-Impostos-ICMS-ST#grade). Caso não seja localizado nenhum resultado, o Sankhya Om exibe a mensagem "Não foi encontrada nenhuma média diária de Imposto para o Produto/Referência/Empresa informado."

## Grade de Resultados

![Grade de resultados da consulta de média diária dos impostos, com as colunas Qtd. Inicial do Estoque, Total das…](https://ajuda.sankhya.com.br/hc/article_attachments/7057705114519)

### Campos da grade

- **Qtd. Inicial do Estoque** — exibe o valor do estoque do dia anterior.
- **Total das entradas** — soma de todas as entradas de estoque do produto no dia.
- **Total das saídas** — soma de todas as saídas de estoque do produto no dia.

#### Vlr. Unit. do Item

**O que faz**

Apresenta o valor unitário do imposto.

**Como funciona**

O valor é calculado pela fórmula:

`Vlr. Unit. do Item = Vlr. Total do Imposto / Qtd. Inicial do Estoque + Total das entradas`

#### Vlr. Total do Imposto

**O que faz**

Corresponde à soma dos impostos da(s) nota(s) de entrada, incluindo os impostos do dia anterior.

**Como funciona**

`Vlr. Total do Imposto = Vlr. Final do Imposto do dia anterior + Vlr. Total do Imposto no dia`

#### Qtd. Final do Estoque

**O que faz**

Traz o saldo de estoque no final do dia.

**Como funciona**

`Qtd. Final do Estoque = Qtd. Inicial do Estoque + Total das Entradas − Saídas do dia`

#### Vlr. Final do Imposto

**O que faz**

Apresenta o valor final do imposto acumulado no dia.

**Como funciona**

- Se a **Qtd. Final do Estoque** for igual à **Qtd. Inicial do Estoque** mais o **Total das entradas**: `Vlr. Final do Imposto = Vlr. Total do Imposto`.
- Se a **Qtd. Final do Estoque** for diferente desse valor: `Vlr. Final do Imposto = Qtd. Final do Estoque x Vlr. Unit. do Item`.

## Botões da tela

- **Exportar grade para PDF** — exporta as informações da grade. Além do PDF, também é possível **Exportar para planilha (xls)**, **Exportar para planilha (xlsx)** e **Exportar para cubo**.
- **Configurar grade** — configura as colunas exibidas na grade.
