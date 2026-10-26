---
id: "9038402484247"
titulo: "Financeiros não encontrados para imprimir boleta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9038402484247-Financeiros-n%C3%A3o-encontrados-para-imprimir-boleta"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-08-27T11:38:59Z"
rotulos: ["Configuração", "Movimentação Financeira", "Atualização", "Financeiro", "CORE_E01378", "Falta do número da nota no financeiro ao tentar imprimir boletos", "Financeiros não encontrados para imprimir boletos", "Verifique existência de STP_CONFIRMANOTA2 e TRG_UPD_TGFCAB", "Erro"]
---

# Financeiros não encontrados para imprimir boleta

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16672326309911) MENSAGEM:**

[CORE\_E01378]: Financeiros não encontrados para imprimir boleta!

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16672342159767) SITUAÇÃO:**

Ao tentar emitir boletos a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16672342163991) SOLUÇÃO:**

Verifique se a 'PROCEDURE  STP\_CONFIRMANOTA2' e a 'TRIGGER  TRG\_UPD\_TGFCAB' existem no banco de dados. Caso não existam, realize a atualização de versão para que as mesmas sejam criadas. Elas são responsáveis por confirmar a nota e inserir corretamente o número da nota no financeiro.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16672326319255) CAUSA:**

Ao tentar fazer a impressão de boletos e por algum motivo o financeiro fica sem o número da nota.
