---
id: "10063583581975"
titulo: "Conta não preparada para Criação de Cobrança PIX via API. Impressão cancelada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10063583581975-Conta-n%C3%A3o-preparada-para-Cria%C3%A7%C3%A3o-de-Cobran%C3%A7a-PIX-via-API-Impress%C3%A3o-cancelada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:04:52Z"
rotulos: ["Configuração", "Contas", "Cobrança", "Financeiro", "PIX", "CORE_E07223", "API", "Configurar conta para PIX", "Impressão cancelada sem configuração", "Erro ao alterar conta com PIX"]
---

# Conta não preparada para Criação de Cobrança PIX via API. Impressão cancelada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18971679523607) MENSAGEM:**

[CORE\_E07223] Conta não preparada para Criação de Cobrança PIX via API. Impressão cancelada.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18971693916567) SITUAÇÃO:**

Ao tentar realizar a impressão de boleto de cobrança por PIX a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18971693922455) CAUSA:**

Ocorre quando as configurações no cadastro da conta não foram realizadas para a impressão do PIX.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18971693923607) SOLUÇÃO:**

Para gerar uma cobrança avulsa como meio de pagamento via PIX, configure a Conta bancária para emitir cobranças através da marcação: Cobranças Pix API, na aba Boleto(s)/Duplicatas, da tela **Contas** (Caminho de acesso à tela: Configurações » Cadastros » Bancários » Contas).

![Imagem 5: Para gerar uma cobrança avulsa como meio de pagamento via PIX, configure a Conta bancária para emitir cobranças através…](https://ajuda.sankhya.com.br/hc/article_attachments/18971679535255)

Na tela **Movimentação financeira** (Caminho de acesso à tela: Financeiro » Rotinas » Movimentação Financeira) realize a geração de um lançamento financeiro de receita por meio do botão![Imagem 6: Na tela Movimentação financeira (Caminho de acesso à tela: Financeiro » Rotinas » Movimentação Financeira) realize a…](https://ajuda.sankhya.com.br/hc/article_attachments/18971679539863)**"Cadastrar Financeiro [F8]"**e preencha os campos obrigatórios da tela.

Em seguida, utilize a opção **"Imprimir Pix",** no botão Outras Opções, para que assim, o documento de cobrança seja gerado. Na geração deste, os dados do QR Code e o ID da Transação ficarão gravados nos campos **"PIX Copia e Cola",** da aba [Cobrança,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abacobran%C3%A7a) e **"TXID Pix",** da aba  [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abageral), respectivamente.

**Nota:** a conta bancária informada na geração de Cobrança Pix não poderá ser alterada. Se houver a tentativa de alterar os dados do Banco e/ou Conta o sistema o alertará através da mensagem:

**"Há uma cobrança PIX vinculada ao título [XXX] e, por isso, a conta não pode ser alterada. Caso haja necessidade, este título deve ser renegociado."**

Caso já exista um título de receita real e pendente e possua os dados do QR Code e ID da Transação gravado nos seus respectivos campos, ao acionar a opção Imprimir Pix a reimpressão do documento de cobrança será realizada.

**Nota:** se a conta bancária não estiver preparada para a geração de Cobrança Pix no momento da impressão, ou seja, se os dados não estiverem preenchidos corretamente, você será informado por meio da mensagem:

**"Não foi possível imprimir pix. Conta não preparada para Criação de Cobrança Pix via API. Impressão cancelada."**
