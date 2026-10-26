---
id: "1500004469322"
titulo: "O(s) financeiro(s) da nota XX não possue(m) informações de boleto previamente gerados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500004469322-O-s-financeiro-s-da-nota-XX-n%C3%A3o-possue-m-informa%C3%A7%C3%B5es-de-boleto-previamente-gerados"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-09-16T11:14:26Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "Boleto", "Financeiro", "não apagar", "#validadoSheyla", "CORE_E03787", "Mensagem: Boleto não gerado", "Pré-visualização só após confirmação", "Não é erro é comportamento do sistema"]
---

# O(s) financeiro(s) da nota XX não possue(m) informações de boleto previamente gerados

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16335362984215) MENSAGEM**:

[CORE\_E03787] O(s) financeiro(s) da nota XX não possuem informações de boleto previamente gerados.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16335347516183) SOLUÇÃO:**

Se tentarem utilizar a opção de Pré-visualização do boleto antes do mesmo ter sido criado, como ainda não foram geradas as informações (Linha digitável e Cód.Barras), o comportamento é apresentar a mensagem de erro. A pré–visualização do boleto só será permitida após ser criado o boleto.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16335347517719) CAUSA:**

Não se trata de um erro e sim de um comportamento do sistema, pois o boleto só é gerado no momento da confirmação da nota (na confirmação o financeiro é gerado, com as informações que devem ser utilizadas para formar o boleto). Então, diferente da pré-visualização da nota (Danfe) é necessário a confirmação da nota e aprovação da mesma. A funcionalidade do botão **"Pré-Visualizar Boleto"** deve ser utilizada para “reimpressão” onde a nota já esteja confirmada e aprovada na SEFAZ.

**Artigos de referência:**

[Configurações para Impressão de Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107133-Configura%C3%A7%C3%B5es-para-Impress%C3%A3o-de-Boletos)

[Impressão de boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094#telaimpress%C3%A3odeboletos)
