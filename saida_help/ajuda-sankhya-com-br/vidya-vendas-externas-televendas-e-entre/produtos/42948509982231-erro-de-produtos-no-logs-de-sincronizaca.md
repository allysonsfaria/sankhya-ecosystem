---
id: "42948509982231"
titulo: "Erro de Produtos no Logs de sincronização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948509982231-Erro-de-Produtos-no-Logs-de-sincroniza%C3%A7%C3%A3o"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Produtos"
atualizado_em: "2026-08-24T16:40:54Z"
rotulos: ["sync_hc", "vidya", "vidya_476108", "sync_hash_1609840e1522"]
---

# Erro de Produtos no Logs de sincronização

Error: Attempting to create an object of type ‘ProductData’ with an existing primary key value ‘1409200’.

![Imagem 1: Error: Attempting to create an object of type ‘ProductData’ with an existing primary key value ‘1409200’.](https://ajuda.sankhya.com.br/hc/article_attachments/42956879816087)

O problema ocorre quando algum produto possui duas unidades marcadas com a unidade padrão de venda dentro de seu cadastro na tela de Produtos no Sankhya. Para verificar siga os passos:

1. Dentro do Sankhya acesse a tela de Produtos, pesquise pelo produto informado na mensagem de erro
   ![Imagem 2: Dentro do Sankhya acesse a tela de Produtos, pesquise pelo produto informado na mensagem de erro](https://ajuda.sankhya.com.br/hc/article_attachments/42956855339031)
2. Na aba de Unidades Alternativas, verifique se existe mais de uma Unidade Padrão de venda, pois, só pode ser configurada apenas uma unidade.
3. Após, siga para o Consolidador de Dados marque o Nome da Tabela no Banco de Dados : **CND\_PRO\_VDYFRC**, clique na seta ao lado dos três pontos (…), e selecione Executar consolidação agora. Faça o mesmo procedimento para **CND\_TGFPRO\_VDYFRC**.

   ![Imagem 3: Após, siga para o Consolidador de Dados marque o Nome da Tabela no Banco de Dados : CND_PRO_VDYFRC , clique na seta ao…](https://ajuda.sankhya.com.br/hc/article_attachments/42956868780567)
