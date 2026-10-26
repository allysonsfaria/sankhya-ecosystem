---
id: "27107398837655"
titulo: "Ao confirmar a nota, o financeiro está sendo recalculado? Saiba como resolver."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27107398837655-Ao-confirmar-a-nota-o-financeiro-est%C3%A1-sendo-recalculado-Saiba-como-resolver"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:40:04Z"
rotulos: ["Configuração", "Nota Fiscal", "Parâmetros", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Ao confirmar a nota o financeiro está sendo recalculado", "Artigo atualizado KCS", "Financeiro - KCS", "ERP"]
---

# Ao confirmar a nota, o financeiro está sendo recalculado? Saiba como resolver.

O recálculo do financeiro ao confirmar uma nota de venda é um processo automático do ERP Sankhya que garante que os **"Títulos Financeiros"** reflitam exatamente o **"Valor total da nota fiscal"**, considerando todos os impostos calculados, despesas acessórias e ajustes aplicados durante a confirmação.

### Quando ocorre o recálculo do financeiro

O sistema verifica automaticamente se é necessário refazer o financeiro quando há alterações:

- Data de negociação/faturamento/entrada e saída,
- Inclusão/exclusão de produtos,
- Alteração do tipo de negociação.

![Imagem 1: SOLUÇÃO: Para que o financeiro não seja recalculado ao confirmar a nota, o parâmetro "RECALCFINDIFAL" deve estar…](https://ajuda.sankhya.com.br/hc/article_attachments/27123888190231)

**SOLUÇÃO:**

Para que o financeiro não seja recalculado ao confirmar a nota, o parâmetro **"RECALCFINDIFAL"** deve estar **desligado**. Esse parâmetro foi criado para gerenciar o comportamento de  refazer o financeiro ao confirmar a nota.  Foi adicionado verificação dos valores pertinentes para refazer o financeiro após a liberação de margem mínima do evento 48 e também do Difal.

Funcionando a partir da versão 4.29b78

![Imagem 2: Funcionando a partir da versão 4.29b78](https://ajuda.sankhya.com.br/hc/article_attachments/27107410305687)

Existem outros parâmetros que podem impactar no recálculo das parcelas financeiros, que podem ser revisados no artigo [**Parâmetros que influenciam no cálculo da Data de Vencimento**](https://ajuda.sankhya.com.br/hc/pt-br/articles/25144670234135-Par%C3%A2metros-que-influenciam-no-c%C3%A1lculo-da-Data-de-Vencimento).

**CAUSA:**

Quando o parâmetro RECALCFINDIFAL está ligado o sistema faz o recalculo do financeiro.

Outro fator importante é o parâmetros DTCALCVENC que é a base para o vencimento do financeiro.

Caso seja lançado uma nota/pedido com data anterior a data atual, o financeiro pode ser recalculado.

Essas são as datas que podem influenciar no financeiro: datas de Negociação, de faturamento ou de Entrada e saída. Importante verificar se elas foram alteradas ao confirmar a nota e se é a que está sendo usada no parâmetro DTCALCVENC.
