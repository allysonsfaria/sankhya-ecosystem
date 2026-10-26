---
id: "37341372981015"
titulo: "Documento XXXX: Não foi possível encontrar o modelo na tela de preferência da empresa na aba Estoque/Preço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37341372981015-Documento-XXXX-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-modelo-na-tela-de-prefer%C3%AAncia-da-empresa-na-aba-Estoque-Pre%C3%A7o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:13:18Z"
rotulos: ["Configuração", "Impressão", "Estoque", "Preferências", "Passos para resolver", "Detalhe do erro", "Erro", "não foi possivel encontrar o modelo", "expedição", "expedicao", "estoque/preço", "estoque/preco"]
---

# Documento XXXX: Não foi possível encontrar o modelo na tela de preferência da empresa na aba Estoque/Preço.

**MENSAGEM:**

Documento XXXX: Não foi possível encontrar o modelo na tela de preferência da empresa na aba Estoque/Preço.

**SITUAÇÃO:**

Ao tentar imprimir um **Pedido de Venda** no processo de **Expedição**, o sistema apresenta a mensagem acima e a impressão não é realizada.

**SOLUÇÃO:**

**(1)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

**(2)** Selecione a empresa utilizada no Pedido de Venda.

**(3)** Na aba **''Estoque/Preço''**, sub-aba **''Expedição''** no campo **''Modelo''**.

**(4)** Selecione o modelo adequado conforme o padrão utilizado pela empresa.

**(5)** Salve as alterações.

**(6)** Retorne ao **Pedido de Venda** e realize novamente a impressão da expedição.

**(7)** Após essa configuração, a impressão do pedido de expedição será realizada com sucesso.

##### OBSERVAÇÃO: A configuração do modelo de expedição é por empresa. Caso existam múltiplas empresas no ambiente, o ajuste deve ser realizado e validado individualmente.  Certifique-se de que o modelo selecionado esteja corretamente cadastrado e ativo no sistema.

**CAUSA:**

O erro ocorre porque **não há um modelo de impressão de expedição configurado** nas preferências da empresa vinculada ao pedido.

Para que o sistema consiga gerar o documento de expedição, é obrigatório que exista um modelo de impressão definido. Quando esse campo não está preenchido, o sistema não encontra o layout necessário e impede a impressão.
