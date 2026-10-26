---
id: "35468768501399"
titulo: "[CORE_E04895] O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é válido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35468768501399--CORE-E04895-O-valor-do-campo-CNPJ-CNPJ-do-emitente-do-documento-fiscal-referenciado-informado-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T14:25:08Z"
rotulos: ["CORE_E04895", "Configuração", "CNPJ", "Parceiro", "NF-e", "Portal de Vendas", "Financeiro", "Jurídica", "Tipo de Título", "Passos para resolver", "Razão do erro", "Detalhe do erro", "PIX/Cartão", "Erro em venda", "Pac.Administradora", "Squad Varejo"]
---

# [CORE_E04895] O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é válido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35468782566551) **MENSAGEM:**

[CORE\_E04895] O valor do campo CNPJ (CNPJ do emitente do documento fiscal referenciado) informado não é válido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35468768472343)SOLUÇÃO:**

**(1)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal desejada.

**(2)** Na aba **''Financeiro''**, no campo **''Tipo de Título''** valide o título utilizado no recebimento PIX/Cartão.

![Imagem 3: (2) Na aba ''Financeiro'' , no campo ''Tipo de Título'' valide o título utilizado no recebimento PIX/Cartão.](https://ajuda.sankhya.com.br/hc/article_attachments/36627313239575)

**(3)** Em seguida, acesse a tela [**''Tipos de Título'**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)**'** (Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título).

**(4)** Na aba **''Geral''**, no campo **''Parc.Administradora''**, identifique o parceiro ativo.

![Imagem 4: (4) Na aba ''Geral'' , no campo ''Parc.Administradora'' , identifique o parceiro ativo.](https://ajuda.sankhya.com.br/hc/article_attachments/36627315639831)

O campo **"Parc. Administradora"** representa as empresas responsáveis por intermediar as transações realizadas com cartões de crédito entre os estabelecimentos comerciais e as instituições financeiras. Elas fornecem os equipamentos, como máquinas de cartões de crédito/débito e os sistemas necessários para que os estabelecimentos aceitem pagamentos com cartões.

No ícone será apresentada a seguinte informação:

![Imagem 5: No ícone será apresentada a seguinte informação:](https://ajuda.sankhya.com.br/hc/article_attachments/36627496441239)

**(5)** Após localizar o parceiro ativo, acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros) e abra o seu cadastro.

**(6)** No campo **''Tipo de Pessoa''**, marque como **''Jurídica''**.

![Imagem 6: (6) No campo ''Tipo de Pessoa'' , marque como ''Jurídica'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36627209643031)

**(7)** Já na aba **''Identificação''** no campo **“CNPJ/CPF”**, deve ser informado o CNPJ da instituição responsável pelo processamento das transações.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35468768486807)CAUSA:**

Conforme a **Nota Técnica NT2023.004 – v1.11**, quando o valor **1** é informado na tag `<tpIntegra>`, o sistema passa a exigir o preenchimento do **CNPJ da instituição de pagamento** na tag `<CNPJ>`, correspondendo ao responsável pelo processamento da transação.

![Imagem 8: Conforme a Nota Técnica NT2023.004 – v1.11 , quando o valor 1 é informado na tag <tpIntegra> , o sistema passa a exigir…](https://ajuda.sankhya.com.br/attachments/token/jiSyB8yJmpLG8Lfd6GXQseg0h/?name=image.png)

Saiba mais em: [Notas Técnicas](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=)

[Nota Técnica 2023.004 - v.1.11](https://ajuda.sankhya.com.br/hc/pt-br/articles/24258905713815-Nota-T%C3%A9cnica-2023-004-v-1-11)
