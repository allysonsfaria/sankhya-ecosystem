---
id: "44033006681751"
titulo: "Tela Movimento de Documentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44033006681751-Tela-Movimento-de-Documentos"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Comece por aqui > Processos do Portal da Reforma Tributária"
atualizado_em: "2026-10-06T17:59:34Z"
---

# Tela Movimento de Documentos

**Versão mínima SankhyaOm 4.36:** 4.36b88 + erpcore-module 5.19.0
**Versão mínima Livros:** 5.47.0
**Módulo:** Livros Fiscais › Cadastros › Portal da Reforma Tributária

**Caminho de acesso:** Menu Principal › Livros Fiscais › Cadastros › Portal da Reforma Tributária › Movimentações › Documentos › Movimento

---

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/44033006681751-Tela-Movimento-de-Documentos#o-que-e)
- [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/44033006681751-Tela-Movimento-de-Documentos#como-usar)
- [Listagem de Documentos Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/44033006681751-Tela-Movimento-de-Documentos#listagem)
- [Detalhe do Documento](https://ajuda.sankhya.com.br/hc/pt-br/articles/44033006681751-Tela-Movimento-de-Documentos#detalhe)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/44033006681751-Tela-Movimento-de-Documentos#pontos-atencao)
- [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44033006681751-Tela-Movimento-de-Documentos#faq)

## O que é e para que serve

A tela **Movimento de Documentos** reúne, dentro do [Portal da Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/41261558111255-Tela-Portal-da-Reforma-Tribut%C3%A1ria), os documentos fiscais eletrônicos, os títulos financeiros vinculados a eles e os tributos CBS e IBS calculados sobre esses títulos. Use a tela para partir de um documento fiscal e rastrear, no mesmo lugar, os títulos a receber ou a pagar originados por ele, o pedido relacionado e os documentos referenciados.

A tela não realiza apuração fiscal, não calcula os tributos e não substitui as rotinas de documentos fiscais do Sankhya Om: ela apenas consolida, para consulta, informações que já existem em outras rotinas.

## Como usar a tela

Ao abrir a tela, os documentos dos últimos 30 dias são carregados automaticamente, com o filtro **Período** já preenchido com esse intervalo. Para ver outro recorte, ajuste os filtros **Empresa** e **Período**.

**⚠️ Atenção**

Ao escolher um período maior que 30 dias, o Sankhya Om exibe o aviso "Você selecionou um período maior que 30 dias. Essa operação pode levar alguns minutos. Deseja continuar?", com as opções de confirmar ou cancelar a busca.

São listados apenas documentos fiscais eletrônicos com data de negociação a partir de 01/01/2026. Pedidos, ordens de produção e documentos cancelados não aparecem na listagem.

## Listagem de Documentos Fiscais

A listagem exibe os documentos fiscais que atendem aos filtros aplicados, com uma linha por documento e as colunas: **Dt. Negociação**, **Empresa**, **Parceiro**, **Tipo de Movimento**, **Finalidade**, **Nro Único**, **Número**, **Chave DFe**, **Valor**, **Total IBS** e **Total CBS**, além da ação **Detalhar**.

### Filtros

- **Empresa:** filtra os documentos pela empresa selecionada.
- **Período (De/Até):** filtra pela data de negociação do documento.

Clique em **Limpar** para apagar os filtros. Enquanto nenhuma empresa ou período estiver informado, a tela exibe a mensagem "Informe a empresa ou o período nos filtros acima para visualizar as movimentações." Se nenhum documento for encontrado com os filtros aplicados, a tela exibe um estado vazio com uma mensagem orientativa. A listagem é paginada.

## Detalhe do Documento

Clique em **Detalhar** em qualquer linha da listagem para abrir o detalhe completo do documento. No topo da tela, antes das seções de conteúdo, fica o botão de acesso ao portal: **Portal de Vendas** para documentos de venda e **Portal de Compras** para documentos de compra. O portal abre em uma nova aba, já no registro do documento visualizado. O botão **Voltar** retorna para a listagem com os filtros preservados.

### Resumo do Documento

Apresenta uma visão rápida do documento, com os campos: **Dt. Negociação**, **Empresa**, **Parceiro**, **Tipo de Movimento**, **Número**, **Chave DFe**, **Valor**, **Total IBS** e **Total CBS**.

### Detalhes do Cabeçalho

Traz as informações completas do cabeçalho do documento fiscal: **Chave DFe**, **Empresa**, **Empresa da Negociação**, **Parceiro**, **Tipo de Movimento**, **Tipo Operação**, **Tipo Negociação**, **Dt. Entrada/Saída**, **Dt. do Faturamento**, **Dt. do Movimento**, **Dt. Negociação**, **Finalidade da Operação**, **Nro. NFS-e**, **Nro. Nota**, **Nro. Único**, **Série da Nota**, **Status da Nota**, **Nota Modelo** e **Vlr. Nota**. Campos sem valor são exibidos em branco, e nenhum campo é omitido da tela.

**ℹ️ Nota**

O campo **Tipo de Movimento** determina se o documento é tratado como venda ou como compra nas demais seções da tela, inclusive qual pedido aparece em **Pedido** e qual portal o botão no topo da tela abre.

### Pedido

Para documentos de venda, esta seção exibe o **Pedido de Venda** vinculado. Para documentos de compra, exibe o **Pedido de Compra** vinculado. Nos dois casos, os campos exibidos são: **Número**, **Dt. Negociação**, **Empresa**, **Parceiro**, **Nro Único**, **Tipo Operação** e **Valor**. Se não houver pedido vinculado, a seção exibe "Não existem dados a serem exibidos".

### Documentos Referenciados

Exibe os documentos fiscais que o documento visualizado declara como referenciados, com os campos: **Dt. Negociação**, **Empresa**, **Parceiro**, **Tipo de Movimento**, **Número**, **Chave DFe**, **Valor** e **Status Nota**. Se não houver documentos referenciados, a seção exibe "Não existem dados a serem exibidos".

**ℹ️ Nota**

Esta seção lista apenas documentos declarados como referência no próprio documento fiscal (grupo `NFref` do XML). O vínculo com um pedido, que não é um documento fiscal e não tem chave de acesso, aparece na seção **Pedido**.

### Títulos do Documento

Lista os títulos financeiros vinculados ao documento, com uma linha por título e os campos: **Dt. Negociação**, **Empresa**, **Parceiro**, **Tipo** (Receita/Despesa), **Tipo de Movimento**, **Nro Único**, **Vlr Desdobramento**, **IBS** e **CBS**, além da ação **Detalhar**. O cabeçalho da seção mostra o total de títulos encontrados, por exemplo, "Títulos do Documento (3)".

Clique em **Detalhar** para abrir o título. Títulos do tipo Receita abrem na [tela Movimento de Receitas](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032913295639-Tela-Movimento-de-Receitas), e títulos do tipo Despesa, na [tela Movimento de Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/44032956912407-Tela-Movimento-de-Despesas), já com o registro aberto. Ao clicar em **Voltar** no detalhe do título, você retorna para o detalhe do documento com a seção preservada. Títulos cancelados não são exibidos. Se não houver título vinculado, a seção exibe "Não existem dados a serem exibidos".

## Pontos de atenção

- São exibidos apenas documentos fiscais com data de negociação a partir de 01/01/2026. A tela não traz histórico anterior a essa data.
- Apenas documentos fiscais eletrônicos aparecem na listagem. Pedidos e ordens de produção ficam de fora.
- Documentos e títulos cancelados não são exibidos em nenhuma seção da tela.
- As seções **Pedido**, **Documentos Referenciados** e **Títulos do Documento** são sempre exibidas. Sem dados, aparecem com a mensagem de estado vazio.
- Os valores de IBS e CBS aparecem apenas nos títulos gerados depois da atualização para a versão que calcula esses tributos na movimentação financeira. Para saber mais, acesse [Processo Rateio de IBS e CBS na movimentação financeira por parcela](https://ajuda.sankhya.com.br/hc/pt-br/articles/43367764153111).

## Perguntas frequentes

### Por que a seção Documentos Referenciados aparece vazia, mesmo quando eu sei que o documento nasceu de um pedido?

Um pedido não é um documento fiscal eletrônico e não tem chave de acesso. Por isso ele nunca aparece em **Documentos Referenciados**, que só relaciona documentos fiscais pela chave declarada no XML. O vínculo do documento com o pedido que o originou aparece na seção **Pedido**.

### Por que um documento que eu sei que existe não aparece na listagem?

Confira três pontos: se o documento tem data de negociação a partir de 01/01/2026, se ele é um documento fiscal eletrônico (pedidos e ordens de produção não aparecem) e se ele não está cancelado. A tela só exibe documentos que atendam a essas três condições.
