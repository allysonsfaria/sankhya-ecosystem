---
id: "360044617593"
titulo: "CR obrigatório não informado. Conta reduzida XXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617593-CR-obrigat%C3%B3rio-n%C3%A3o-informado-Conta-reduzida-XXX"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:44Z"
rotulos: ["Configuração", "Centro de Resultado", "Contabilização", "Financeiro", "Centro Resultado", "Corrigir Cadastro", "Reprocessar Contabilização", "Erro"]
---

# CR obrigatório não informado. Conta reduzida XXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16979602148247) MENSAGEM:**

CR obrigatório não informado. Conta reduzida XXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16979586560535) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Contabilização » Cadastros » Plano de Contas :](https://ajuda.sankhya.com.br/hc/article_attachments/16979602154135) Acesse: Contabilização » Cadastros » Plano de Contas:

- Busque pela conta contábil que está sendo contabilizado e verifique se a mesma possui a opção **"Centro de Resultado Obrigatório"**. Caso no processo de contabilização não se faça o uso de CR-Centro de Resultado, pode-se desmarcar esta.
- Caso a fórmula da contabilização possua a variável de CR, então faz-se necessário que o documento contabilizado possua um CR informado.

![Imagem 4: Após os ajustes, efetue novamente a Contabilização.](https://ajuda.sankhya.com.br/hc/article_attachments/16979602155671) Após os ajustes, efetue novamente a Contabilização.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16979586567319) CAUSA:**

Ocorre quando a Fórmula de Contabilização possui a variável que busca o CR Constante e o(s) documento(s) contabilizados não possui CR.

Ocorre também quando a Conta Contábil, no cadastro de Plano de Contas, possui a marcação 'Centro de Resultado Obrigatório'.
