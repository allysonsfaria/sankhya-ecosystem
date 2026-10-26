---
id: "360043608674"
titulo: "Nos movimentos originados de recebimento com cartão não é possível alterar os campos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043608674-Nos-movimentos-originados-de-recebimento-com-cart%C3%A3o-n%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-os-campos"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:01:13Z"
rotulos: ["#criadoRoger", "#revisadohugo", "CORE_E03463", "Movimentação Financeira", "Financeiro", "Verifique se é transação TEF/POS", "Restrição de integridade para cartões", "Campos de cartões não podem ser alterados", "Erro", "Cartão", "Integridade"]
---

# Nos movimentos originados de recebimento com cartão não é possível alterar os campos

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16192557141015) MENSAGEM**:

[CORE\_E03463] Nos movimentos originados de recebimento com cartão não é possível alterar os campos:
Taxa Administradora, Vlr Desconto, Vlr Multa, Vlr Juros, Despesas c/ Cartório, Vlr INSS, Vlr ISS, Vlr IRF,
Valor do Desdobramento, TOP, Tipo de Título, Datas de Entrada e Saída, Data de Vencimento, Data de Negociação, Receita/Despesa, Parceiro, Empresa, Provisão, Cód. e Valor da Moeda.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16192557142679) SOLUÇÃO**:

A validação existe para manter a integridade das informações de títulos originados de cartões.

Para consultar que o título é oriundo de um recebimento de cartão, acesse a **"[Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753)"** (Caminho de acesso: Financeiro » Rotinas » Movimentação Financeira) e consulte os campos indicados a seguir.

- Campos "**NSU"** e "**Autorização"**: Quando esses 2 campos estão preenchidos, significa que é um título de transação via Cartão via TEF/POS ] - O título não poderá ser alterado em hipótese alguma.

![Imagem 3: Campos " NSU" e " Autorização" : Quando esses 2 campos estão preenchidos, significa que é um título de transação via…](https://ajuda.sankhya.com.br/hc/article_attachments/14607209229463)

**![Imagem 4: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16192543206167) CAUSA**:

Mensagem ocorre quando um título autorizado por transação TEF/POS está sendo alterado pelo sistema, por restrições de integridade esse título não poderá sofrer nenhuma alteração via sistema.
