---
id: "31091799144983"
titulo: "Erro ao remover entidade: O documento de número único xxxxxx não pode ser excluído. Existe parcela recebida com POS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31091799144983-Erro-ao-remover-entidade-O-documento-de-n%C3%BAmero-%C3%BAnico-xxxxxx-n%C3%A3o-pode-ser-exclu%C3%ADdo-Existe-parcela-recebida-com-POS"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:33:38Z"
rotulos: ["Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "PEREXCFINPOS", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro ao remover entidade:", "Existe parcela recebida com POS.", "O documento de número único xxxxxx não pode ser excluído.", "CARTÃO POS", "PIX POS", "Erro"]
---

# Erro ao remover entidade: O documento de número único xxxxxx não pode ser excluído. Existe parcela recebida com POS

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31091815928599) **MENSAGEM:**

Erro ao remover entidade: O documento de número único xxxxxx não pode ser excluído. Existe parcela recebida com POS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31091815930519) SOLUÇÃO:**

Na tela **''Preferências''** (Configurações» Avançado» Preferências) ligue o parâmetro **''Permite excluir financeiros POS - PEREXCFINPOS''** para realizar a exclusão de notas com recebimento no cartão POS.

![Imagem 3: Na tela ''Preferências'' (Configurações» Avançado» Preferências) ligue o parâmetro ''Permite excluir financeiros POS -…](https://ajuda.sankhya.com.br/hc/article_attachments/33374274365591)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31091799139607) CAUSA:**

Este erro ocorre quando se tenta excluir notas que possuem recebimento por meio de **cartão pos e PIX pos,** enquanto o parâmetro mencionado acima está desativado.
