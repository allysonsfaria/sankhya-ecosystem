---
id: "30873896302359"
titulo: "Não é permitido fechar o caixa com diferença"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30873896302359-N%C3%A3o-%C3%A9-permitido-fechar-o-caixa-com-diferen%C3%A7a"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:34:34Z"
rotulos: ["Configuração", "Movimentação Financeira", "GERDIFACOC", "Adiantamento", "Preferências", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Não é permitido fechar o caixa com diferenç", "Valor Total retornado", "Gerar Diferença do Acerto de OC p/ Financeiro - GERDIFACOC", "Erro"]
---

# Não é permitido fechar o caixa com diferença

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30873896293143) **MENSAGEM:**

Não é permitido fechar o caixa com diferença.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30873886915095)SOLUÇÃO:**

O fechamento de caixa é um procedimento que aconselhamos ser realizado sem que exista nenhuma diferença entre o valor utilizado como "**Adiantamento**" e o "**Valor Total retornado**".

Será permitido o fechamento com divergência entre estes valores apenas se o parâmetro **"Gerar Diferença do Acerto de OC p/ Financeiro - GERDIFACOC"** estiver **desligado**.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30873896295447)

Se este parâmetro estiver habilitado, será preciso **Gerar a diferença para financeiro:** a configuração para esta geração é realizada nas [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#preferncias) de **Acerto de Ordem de Carga**.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30873886916503)CAUSA:**

Ocorre ao tentar fechar um Acerto de Ordem de Carga quando a preferência **GERDIFACOC** está habilitada e há divergência entre o **Adiantamento** e o **Valor Total Retornado**, sem que a diferença tenha sido gerada para o financeiro.
