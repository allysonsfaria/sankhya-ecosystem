---
id: "14438353074199"
titulo: "Título já está baixado. Não pode ser alterado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14438353074199-T%C3%ADtulo-j%C3%A1-est%C3%A1-baixado-N%C3%A3o-pode-ser-alterado"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:58:44Z"
rotulos: ["Configuração", "Liberação de Limites", "TOP", "Financeiro", "CORE_E02843", "Título já baixado não pode ser alterado.", "Bloqueio ocorre ao alterar título pós-compensação.", "Desfaça e refaça a compensação para liberar evento", "Erro"]
---

# Título já está baixado. Não pode ser alterado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16859483851671) MENSAGEM:**

[CORE\_E02843]: Título já está baixado. Não pode ser alterado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16859483854103) SOLUÇÃO:**

A função nativa do sistema é sempre solicitar a liberação de limite para o evento 24, quando o valor do título está acima do valor mínimo estipulado dentro do cadastro de [TOP,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) campo **"Valor mínimo p/Autorização de Pagamento"**, o sistema bloqueará a baixa e solicitará a liberação. Quando o título sofre alterações de valores após a compensação, desfaça a compensação para liberação do evento pendente e faça a compensação novamente.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16859483858839) CAUSA:**

Ocorre ao tentar liberar um título na tela de "Liberação de limites", evento 24 (autorização de pagamento).
