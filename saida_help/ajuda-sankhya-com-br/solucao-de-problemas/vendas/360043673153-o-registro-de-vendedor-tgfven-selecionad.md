---
id: "360043673153"
titulo: "O registro de \"Vendedor\" (TGFVEN) selecionado não está cadastrado, ou não está ativo, ou não é analítico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673153-O-registro-de-Vendedor-TGFVEN-selecionado-n%C3%A3o-est%C3%A1-cadastrado-ou-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:44Z"
rotulos: ["Configuração", "Parceiro", "Central de Vendas", "Vendedores", "ORA-20101", "Ajuste o status do vendedor ou substitua", "Mensagem: Vendedor não cadastrado ou ativo", "Verifique códigos de vendedores e status", "Erro"]
---

# O registro de "Vendedor" (TGFVEN) selecionado não está cadastrado, ou não está ativo, ou não é analítico

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16135018496151) MENSAGEM:**

ORA-20101: O registro de "Vendedor" (TGFVEN) selecionado não está cadastrado, ou não está ativo, ou não é analítico.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16135005088279) SOLUÇÃO:**

![Imagem 3: Busque no lançamento realizado todos os códigos de vendedores vinculados.](https://ajuda.sankhya.com.br/hc/article_attachments/16135018503063) Busque no lançamento realizado todos os códigos de vendedores vinculados.

![Imagem 4: Para lançamentos na "Central (Vendas/Compras/Mov.Interna)" essa informação pode ser observada no cabeçalho, nos itens e…](https://ajuda.sankhya.com.br/hc/article_attachments/16135018503831) Para lançamentos na **"Central (Vendas/Compras/Mov.Interna)"** essa informação pode ser observada no cabeçalho, nos itens e na aba financeiro, conforme abaixo:

![Imagem 5: Para lançamentos na "Central (Vendas/Compras/Mov.Interna)" essa informação pode ser observada no cabeçalho, nos itens e…](https://ajuda.sankhya.com.br/hc/article_attachments/14635574913047)

![Imagem 6: Identificado os códigos de vendedores vinculados no respectivo lançamento, acesse a tela "Vendedores/Compradores"…](https://ajuda.sankhya.com.br/hc/article_attachments/16135018504727) Identificado os códigos de vendedores vinculados no respectivo lançamento, acesse a tela **"Vendedores/Compradores"** (Configurações » Cadastros), selecione os mesmos e faça uma análise do campo **Ativo**:

![Imagem 7: Identificado os códigos de vendedores vinculados no respectivo lançamento, acesse a tela "Vendedores/Compradores"…](https://ajuda.sankhya.com.br/hc/article_attachments/14635491239319)

![Imagem 8: Caso esse campo esteja desmarcado, sintonize internamente o responsável por tê-lo desativado, avaliando se a ativação…](https://ajuda.sankhya.com.br/hc/article_attachments/16135005091863) Caso esse campo esteja desmarcado, sintonize internamente o responsável por tê-lo desativado, avaliando se a ativação ocorrerá ou se um vendedor que difere desse deverá ser utilizado em seu lançamento.

![Imagem 9: Realizado os devidos ajustes, prossiga com o lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16135005092759) Realizado os devidos ajustes, prossiga com o lançamento.

**![Imagem 10: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16135018506391) OBSERVAÇÃO:**

Saiba como configurar campos invisíveis no Layout da nota, acessando este artigo: **"**[**Como inserir um campo no layout da nota?**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)**"**

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16135018507543) CAUSA:**

Ao faturar/devolver um pedido/nota, a mensagem ocorre quando o Vendedor/Comprador, vinculado ao parceiro como preferencial ou digitado direto na nota está 'inativo' em seu cadastro.

![495b9bfc-3e43-423b-ba7c-4aef8cbd564c](https://ajuda.sankhya.com.br/hc/article_attachments/32231406945943) Caso o vendedor/comprador seja um ex-colaborador, será necessário reativar seu cadastro, seguir com o lançamento e depois desativá-lo novamente. Nativamente não é possível utilizar cadastros inativos.
