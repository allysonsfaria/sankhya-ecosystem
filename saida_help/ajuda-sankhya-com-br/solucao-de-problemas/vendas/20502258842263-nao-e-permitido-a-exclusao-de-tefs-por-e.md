---
id: "20502258842263"
titulo: "Não é permitido a exclusão de TEFs por essa rotina"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20502258842263-N%C3%A3o-%C3%A9-permitido-a-exclus%C3%A3o-de-TEFs-por-essa-rotina"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-06T14:42:00Z"
rotulos: ["Movimentação Financeira", "SEFAZ", "Financeiro", "CORE_E03461", "Exclusão de TEF não permitida", "Campo RECEBCARTAO está como \"SIM\"", "Verifique status da transação e use opções administrativas para ajustes", "Erro"]
---

# Não é permitido a exclusão de TEFs por essa rotina

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/20502258816279) **MENSAGEM:**

[CORE\_E03461] Não é permitido a exclusão de TEF's por essa rotina.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/20502272728983)CAUSA:**

Acontece pois o campo RECEBCARTAO está como "SIM".

**![Imagem 3: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20594606700567) SITUAÇÃO:**

![Imagem 4: Ao tentar alterar os dados da nota já aprovada na SEFAZ;](https://ajuda.sankhya.com.br/hc/article_attachments/20594606713367) Ao tentar alterar os dados da nota já aprovada na SEFAZ;

![Imagem 5: Ao tentar confirmar as vendas que passaram cartão no TEF e deram algum erro depois;](https://ajuda.sankhya.com.br/hc/article_attachments/20594589799703) Ao tentar confirmar as vendas que passaram cartão no TEF e deram algum erro depois;

![Imagem 6: Nota denegada na SEFAZ e no sistema está aguardando autorização ou aguardando correção;](https://ajuda.sankhya.com.br/hc/article_attachments/20594589808791) Nota denegada na SEFAZ  e no sistema está aguardando autorização ou aguardando correção;

![Imagem 7: Ocorreu um erro no processamento da transação;](https://ajuda.sankhya.com.br/hc/article_attachments/22215896893847) Ocorreu um erro no processamento da transação;

**![Imagem 8: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20502258821271)SOLUÇÃO:**

- Recomenda-se verificar o status da transação junto a operadora;
  - Caso o Recebimento não tenha sido processado e deseja-se reprocessar, o usuário pode proceder com o Recebimento Administrativo:
  - Abra a Movimentação Financeira (link) relacionada ao TEF do financeiro em questão;
  - Na tela de Movimentação Financeira, clique no botão 'Outras Opções' >> 'Recebimento com cartão (Administrativo)'.

  - Caso o Recebimento não tenha sido processado e deseja-se realizar o cancelamento, o usuário pode proceder com o Cancelamento Normal ou Administrativo:
  - Abra a Movimentação Financeira (link) relacionada ao TEF do financeiro em questão;
  - Na tela de Movimentação Financeira, clique no botão 'Outras Opções' >> 'Cancelar recebimento com cartão'.
  - Na tela de Movimentação Financeira, clique no botão ?Outras Opções? >> 'Cancelar recebimento com cartão (Administrativo)'.

  - Caso o **Recebimento não tenha sido processado e deseja-se realizar a exclusão do financeiro** **em questão**, para proceder com a exclusão do financeiro, o usuário precisará ativar o parâmetro: **PERMEDITRECADM - "Permite editar/excluir tít. receb. administrativo?"**. Porém, é importante ressaltar que se não houver a conferência de lançamentos do cartão e baixa manual na Movimentação Financeira, poderão ocorrer inconsistências nos lançamentos e/ou recebimentos.

![Imagem 9: - Caso o Recebimento não tenha sido processado e deseja-se realizar a exclusão do financeiro em questão , para proceder…](https://ajuda.sankhya.com.br/hc/article_attachments/20594589818647)

![Imagem 10: - Caso o Recebimento não tenha sido processado e deseja-se realizar a exclusão do financeiro em questão , para proceder…](https://ajuda.sankhya.com.br/hc/article_attachments/20594606755991)

![Imagem 11: - Caso o Recebimento não tenha sido processado e deseja-se realizar a exclusão do financeiro em questão , para proceder…](https://ajuda.sankhya.com.br/hc/article_attachments/20594589849239)

**Observação:** Esse procedimento funcionará em todos os modelos de TEF homologados para o Sankhya.
