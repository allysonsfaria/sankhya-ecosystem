---
id: "360042865514"
titulo: "A linha referenciada na tabela TGFVEND não está cadastrada ou não está ativa ou não analítica"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865514-A-linha-referenciada-na-tabela-TGFVEND-n%C3%A3o-est%C3%A1-cadastrada-ou-n%C3%A3o-est%C3%A1-ativa-ou-n%C3%A3o-anal%C3%ADtica"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:48Z"
rotulos: ["Configuração", "Parceiro", "Faturamento", "Vendedores", "ORA-20101", "Erro no faturamento", "Ativar vendedor", "Vendedor inativo", "Erro"]
---

# A linha referenciada na tabela TGFVEND não está cadastrada ou não está ativa ou não analítica

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16090339461271) MENSAGEM:**

Erro durante o processo de faturamento.
Número único XXXXXX.
ORA-20101: A LINHA REFERENCIADA NA TABELA TGFVEND NÃO ESTÁ CADASTRADA OU NAO ESTÁ ATIVA OU NÃO ANALÍTICA.
ORA-06512: em "SANKHYA.STP\_POPULA\_MSG", line 5
ORA-06512: em "SANKHYA\_TRG\_INC\_TGFITE", line 81
ORA-04088: erro durante a execução do gatilho 'SANKHYA\_TRG\_INC\_TGFITE'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16090339464855) SITUAÇÃO:**

Ao faturar/devolver um pedido/nota é apresentado a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16090339468567) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse a Nota/Pedido, verifique no cabeçalho e também nos itens o código do vendedor.](https://ajuda.sankhya.com.br/hc/article_attachments/16090393069079) Acesse a Nota/Pedido, verifique no cabeçalho e também nos itens o código do vendedor.

Empresas que trabalham com **Múltiplas Comissões de Vendedores**, apresentará a aba: **"Comissões no rodapé da nota"** que também terá os códigos dos vendedores.

![Imagem 5: Acesse a tela " Vendedores/Compradores " (Caminho de acesso: Configurações » Cadastros » Vendedores/Compradores)](https://ajuda.sankhya.com.br/hc/article_attachments/16090393073303) Acesse a tela **"[Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores)"** (Caminho de acesso: Configurações » Cadastros » Vendedores/Compradores)

Acesse com o código do vendedor, o cadastro, e verifique o campo **"Ativo"**. Caso esteja desmarcado, verifique a possibilidade de ativá-lo ou substituir por outro vendedor no pedido/nota caso o vendedor esteja desligado da empresa.

Caso seja um Lançamento novo de nota/pedido e ocorrer o mesmo incidente, acesse o **"[Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)"** da nota (Caminho de acesso: Configurações » Cadastros » Parceiros), aba **"Identificação"**, campo **"Vend. Preferencial"**, executar o mesmo procedimento e verifique se está ativo.

![Imagem 6: Após os ajustes, fature novamente o pedido/nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16090393076503) Após os ajustes, fature novamente o pedido/nota.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16090339489559) CAUSA:**

Ocorre quando o Vendedor/Comprador, vinculado ao Parceiro como preferencial ou digitado direto na nota/pedido esta 'inativo' em seu cadastro.
