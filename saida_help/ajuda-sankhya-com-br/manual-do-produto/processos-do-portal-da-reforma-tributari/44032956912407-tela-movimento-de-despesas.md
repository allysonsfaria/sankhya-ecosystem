---
id: "44032956912407"
titulo: "Tela Movimento de Despesas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Comece por aqui > Processos do Portal da Reforma Tributária"
atualizado_em: "2026-10-06T17:59:29Z"
---

# Tela Movimento de Despesas

**Versão mínima SankhyaOm 4.36:** 4.36b88 + erpcore-module 5.19.0
**Versão mínima Livros:** 5.47.0
**Módulo:** Livros Fiscais › Cadastros › Portal da Reforma Tributária

**Caminho de acesso:** Menu Principal › Livros Fiscais › Cadastros › Portal da Reforma Tributária › Movimentações › Despesas › Movimento

---

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas#o-que-e)
- [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas#como-usar)
- [Listagem de Títulos a Pagar](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas#listagem)
- [Detalhe do Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas#detalhe)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas#pontos-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas#faq)

## O que é e para que serve

A tela **Movimento de Despesas** reúne, dentro do [Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria), os títulos a pagar, com os tributos CBS e IBS calculados para cada título. Use a tela para localizar um título a pagar e rastrear, no mesmo lugar, o documento fiscal de origem, o pedido de compra relacionado e a composição tributária da operação.

A tela não realiza apuração fiscal, não calcula os tributos e não substitui o módulo financeiro do Sankhya Om: ela apenas consolida, para consulta, informações que já existem em outras rotinas.

## Como usar a tela

Ao abrir a tela, os títulos dos últimos 30 dias são carregados automaticamente, com o filtro **Período** já preenchido com esse intervalo. Para ver outro recorte, ajuste os filtros **Empresa**, **Período** e **Tipo de Título**.

**⚠️ Atenção**

Ao escolher um período maior que 30 dias, o Sankhya Om exibe o aviso "Você selecionou um período maior que 30 dias. Essa operação pode levar alguns minutos. Deseja continuar?", com as opções de confirmar ou cancelar a busca.

São listados apenas títulos do tipo **Despesa** com data de negociação a partir de 01/01/2026 e que tenham pedido ou nota fiscal vinculada. Títulos cancelados e títulos de provisão não aparecem na listagem.

## Listagem de Títulos a Pagar

A listagem exibe os títulos a pagar que atendem aos filtros aplicados, com uma linha por título e as colunas: **Dt. Negociação**, **Empresa**, **Parceiro**, **Tipo de Movimento**, **Nro Único**, **Tipo Título**, **Valor**, **IBS** e **CBS**, além da ação **Detalhar**.

### Filtros

- **Empresa:** filtra os títulos pela empresa selecionada.
- **Período (De/Até):** filtra pela data de negociação do título.
- **Tipo de Título:** filtra pela forma de pagamento do título, por exemplo, Boleto, PIX ou Cartão.

Clique em **Limpar** para apagar os filtros. Enquanto nenhuma empresa ou período estiver informado, a tela exibe a mensagem "Informe a empresa ou o período nos filtros acima para visualizar as movimentações." Se nenhum título for encontrado com os filtros aplicados, a tela exibe um estado vazio com uma mensagem orientativa. A listagem é paginada e disponibiliza exportação nos formatos **PDF**, **XLS** e **XLSX**.

## Detalhe do Título

Clique em **Detalhar** em qualquer linha da listagem para abrir o detalhe completo do título. No topo da tela, antes das seções de conteúdo, ficam os botões **Portal de Compras** e **Movimentação Financeira**, que abrem em uma nova aba o registro correspondente no Sankhya Om. O botão **Voltar** retorna para a listagem com os filtros preservados.

### Resumo do Título

Apresenta uma visão rápida do título, com os campos: **Dt. Negociação**, **Empresa**, **Parceiro**, **Nro Único**, **Vlr Desdobramento**, **Total IBS** e **Total CBS**.

### Detalhes do Título

Traz as informações financeiras completas do título: **Nro Único**, **Empresa**, **Parceiro**, **Nro Nota**, **Desdobramento**, **Tipo Operação**, **Dt. Negociação**, **Dt. Entrada/Saída**, **Dt. Vencimento**, **Vlr Desdobramento**, **Vlr Desconto**, **Vlr Multa**, **Vlr Juros**, **Vlr Baixa** e **Data Baixa**. Campos sem valor são exibidos em branco, e nenhum campo é omitido da tela.

### Pedido de Compra

Quando o título tem um pedido de compra vinculado, a seção exibe: **Número**, **Dt. Negociação**, **Empresa**, **Parceiro**, **Nro Único**, **Tipo Operação** e **Valor**. Se não houver pedido vinculado, a seção exibe "Não existem dados a serem exibidos".

### Documentos Fiscais Vinculados

Lista os documentos fiscais eletrônicos vinculados ao título, com uma linha por documento e os campos: **Nro Único**, **Nro Nota**, **Chave DFe**, **Status DFe** e **Finalidade**, além da ação **Detalhar**. Clique em **Detalhar** para abrir a [tela Movimento de Documentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas) com o documento já aberto. Ao voltar, você retorna para o detalhe do título com a seção preservada. Documentos cancelados não são exibidos. Se não houver documento vinculado, a seção exibe "Não existem dados a serem exibidos".

### Tributos do Título

Exibe uma linha por tributo incidente sobre o título, com os campos: **Imposto**, **Incidência**, **CST**, **Base**, **Base Cálc. Reduzida**, **Alíquota**, **Valor** e **Digitado**. O campo **Digitado** indica se o valor do tributo foi informado manualmente ou calculado pelo Sankhya Om. São exibidos apenas os tributos **CBS** e **IBS**. Se não houver tributos calculados para o título, a seção exibe "Não existem dados a serem exibidos".

## Pontos de atenção

- São exibidos apenas títulos do tipo Despesa com data de negociação a partir de 01/01/2026. A tela não traz histórico anterior a essa data.
- Apenas títulos vinculados a um pedido ou a uma nota fiscal aparecem na listagem. Títulos sem esse vínculo ficam de fora.
- Títulos cancelados e títulos de provisão não são exibidos.
- Os valores de IBS e CBS aparecem apenas nos títulos gerados depois da atualização para a versão que calcula esses tributos na movimentação financeira. Para saber mais, acesse [Processo Rateio de IBS e CBS na movimentação financeira por parcela](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111).

## Perguntas frequentes

### Por que um título que eu sei que existe não aparece na listagem?

Confira três pontos: se o título tem data de negociação a partir de 01/01/2026, se ele está vinculado a um pedido ou a uma nota fiscal e se ele não está cancelado. A tela só exibe títulos de Despesa que atendam a essas três condições. Títulos de provisão também não aparecem.
