---
id: "360044174473"
titulo: "O título número XXXXX foi movimentado por uma transferência de cheque. Não pode ser estornado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044174473-O-t%C3%ADtulo-n%C3%BAmero-XXXXX-foi-movimentado-por-uma-transfer%C3%AAncia-de-cheque-N%C3%A3o-pode-ser-estornado"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:55Z"
rotulos: ["#criadoRoger", "CORE_E01775", "Estorno", "Movimentação Financeira", "Financeiro", "Título transferido impede estorno", "Exclua na Movimentação Bancária", "Estorne todos os títulos agrupados", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# O título número XXXXX foi movimentado por uma transferência de cheque. Não pode ser estornado

**MENSAGEM**:

[CORE\_E01775]  O título número XXXXX foi movimentado por uma transferência de cheque. Não pode ser estornado.

**SOLUÇÃO**:

Para correção, siga os passos abaixo:

**(1)** Acesse a tela [**"Movimentação Bancária"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653) (Caminho de acesso: Financeiro » Rotinas »  Movimentação Bancária):

- Pelo número da Transferência, que representa o campo **"Número"** da rotina Movimentação Bancaria, faça a exclusão desse registro nesta tela.

**(2)** Acesse a tela [**"Movimentação Financeira"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) (Caminho de acesso: Financeiro » Rotinas » Movimentação Financeira):

- Realize o estorno do título.

**IMPORTANTE:**

Se houver baixa de títulos agrupados, o estorno deverá ser feito de todos os títulos envolvidos, então avalie a melhor alternativa caso não possa estornar todos os títulos agrupados.

**CAUSA**:

Ocorre quando após a baixa de um título, houve a Transferência de títulos e para que o mesmo seja estornado, se faz necessário excluí-lo da Movimentação Bancaria.
