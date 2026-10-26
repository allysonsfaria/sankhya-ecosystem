---
id: "360044216533"
titulo: "Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.FK_TGFREF_NUFIN_TGFFIN) violada - registro filho localizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044216533-Erro-ao-remover-entidade-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFREF-NUFIN-TGFFIN-violada-registro-filho-localizado"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:31Z"
rotulos: ["#validadoElisangela", "Parceiro", "NF-e", "Movimentação Financeira", "Portal de Vendas", "Financeiro", "Restrição de integridade ao cancelar Nota", "Excluir registros no \"Histórico Cobrança\"", "NF-e após exclusão", "Erro"]
---

# Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.FK_TGFREF_NUFIN_TGFFIN) violada - registro filho localizado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16582861217943) MENSAGEM:**

Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.FK\_TGFREF\_NUFIN\_TGFFIN) violada - registro filho localizado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16582861221271) SITUAÇÃO:**

Ao acessar o Portal de Vendas, e tentar efetuar o Cancelamento de uma Nota, a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16582861228183) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Financeiro » Gerente » Gerência de Cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/16582846497303) Acesse: Financeiro » Gerente » Gerência de Cobrança

Faça um filtro pelo parceiro da Nota ou um filtro personalizado pelo Número único do Financeiro da Nota, que precisa ser cancelado.

Apresentará na grade de 'Títulos' os titulo(s) da Nota que esta tentando cancelar.

Acesse a aba: **"Histórico Cobrança"** e exclua todos os registros para um ou cada título financeiro da Nota.

![Imagem 5: Após o processo, a NF-e pode ser cancelada.](https://ajuda.sankhya.com.br/hc/article_attachments/16582846498455) Após o processo, a NF-e pode ser cancelada.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16582861238551) CAUSA:**

Ocorre quando os títulos financeiro da NF-e que está tentando Cancelar possui registro de Histórico de Cobrança, impedindo o cancelamento.
