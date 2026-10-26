---
id: "360058189514"
titulo: "Restrição de integridade (SANKHYA.FK_TGFMBC_TGFHBC) violada - chave mãe não localizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058189514-Restri%C3%A7%C3%A3o-de-integridade-SANKHYA-FK-TGFMBC-TGFHBC-violada-chave-m%C3%A3e-n%C3%A3o-localizada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:26:35Z"
rotulos: ["#criadoRoger", "Configuração", "Movimentação Financeira", "Histórico", "Financeiro", "Sankhya Checkout", "Erro ORA-02291: chave mãe não localizada", "Código de histórico não configurado", "Cadastrar códigos e reprocessar movimentações", "Erro"]
---

# Restrição de integridade (SANKHYA.FK_TGFMBC_TGFHBC) violada - chave mãe não localizada

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16272155085591) MENSAGEM**:

[ORA-02291] Restrição de integridade (SANKHYA.FK\_TGFMBC\_TGFHBC) violada - chave mãe não localizada

**![Imagem 2: (ORA-02291) Restrição de integridade (SANKHYA.FK_TGFMBC_TGFHBC) violada - chave mãe não localizada SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16272155086615) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o Histórico de Lançamentos Bancários em: Financeiro » Arquivos » Cadastros » Históricos Lançamentos Bancários](https://ajuda.sankhya.com.br/hc/article_attachments/16272155088407) Acesse o Histórico de Lançamentos Bancários em: Financeiro » Arquivos » Cadastros » Históricos Lançamentos Bancários

Caso não haja, faça o cadastro do tipo de lançamento para Sangria e Suprimento, conforme o exemplo abaixo.

- 33 - Sangria - Débito
- 34 - Suprimento - Crédito

![Imagem 4: Acesse o Sankhya Checkout , Menu "Preferências" , aba: "Integração"](https://ajuda.sankhya.com.br/hc/article_attachments/16272111595031) Acesse o **Sankhya Checkout**, Menu **"Preferências"**, aba: **"Integração"**

- Código do Lançamento Bancário para Sangria: insira o código da **sangria**
- Código do Lançamento para Suprimento: insira o código do **suprimento**

![Imagem 5: Código do Lançamento para Suprimento: insira o código do suprimento](https://ajuda.sankhya.com.br/hc/article_attachments/14628709807383)

![Imagem 6: Ainda no Sankhya Checkout , acesse o ícone de notificações 'Sino'. Clique no botão "Atualizar agora" , para que as…](https://ajuda.sankhya.com.br/hc/article_attachments/16272111597975) Ainda no **Sankhya Checkout**, acesse o ícone de notificações 'Sino'. Clique no botão **"Atualizar agora"**, para que as alterações feitas nas preferências do Checkout tenham efeito.

![Imagem 7: Ainda no Sankhya Checkout , acesse o ícone de notificações 'Sino'. Clique no botão "Atualizar agora" , para que as…](https://ajuda.sankhya.com.br/hc/article_attachments/14629538355479)

![Imagem 8: Acesse a Administração de Checkout em: Configurações » Sankhya Checkout » Administração de Checkout](https://ajuda.sankhya.com.br/hc/article_attachments/16272111599639) Acesse a Administração de Checkout em: Configurações » Sankhya Checkout » Administração de Checkout

Menu: **"Importações de Movimentos"**
Opção: **"Reprocessar movimentação selecionada ou reprocessar todas as movimentações"**

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16272111603223) CAUSA:**

Ocorre quando há algum movimento no caixa de sangria e/ou suprimento, porém não foi determinado o código dos históricos de lançamentos de tais movimentos nas preferências do checkout.
