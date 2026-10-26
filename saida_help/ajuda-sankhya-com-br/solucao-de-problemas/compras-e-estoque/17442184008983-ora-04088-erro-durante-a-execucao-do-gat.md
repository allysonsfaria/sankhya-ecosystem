---
id: "17442184008983"
titulo: "ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_TGFITE_AFTER'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17442184008983-ORA-04088-erro-durante-a-execu%C3%A7%C3%A3o-do-gatilho-SANKHYA-TRG-INC-TGFITE-AFTER"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:53:23Z"
rotulos: ["Financeiro", "ORA-04088", "Restrição exclusiva violada", "Limpar tabelas temporárias e verificar triggers", "Linhas indevidas na tabela TGFITE_INC", "Erro", "Gatilho", "Tabelas Temporárias"]
---

# ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_INC_TGFITE_AFTER'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17442183944343) **MENSAGEM:**

[ORA-00001]: restrição exclusiva (SANKHYA.PK\_TGFITE) violada
[ORA-06512]: em "SANKHYA.TRG\_INC\_TGFITE\_AFTER", line 27
[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_TGFITE\_AFTER'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17442192929943)SOLUÇÃO:**

![Imagem 3: Consulte as tabelas: TGFITE_INC, TGFITE_UPD, TGFITE_DLT, TGFCAB_UPT, TGFCAB_DLT;](https://ajuda.sankhya.com.br/hc/article_attachments/17444986455447) Consulte as tabelas: TGFITE\_INC, TGFITE\_UPD, TGFITE\_DLT, TGFCAB\_UPT, TGFCAB\_DLT;

Se houver alguma informação nas tabelas mencionadas acima, as mesmas deverão ser excluídas, pois são tabelas temporárias.

![Imagem 4: Consulte também se no momento tem alguma trigger da TGFCAB e TGFITE desabilitada;](https://ajuda.sankhya.com.br/hc/article_attachments/17444986461463) Consulte também se no momento tem alguma trigger da TGFCAB e TGFITE desabilitada;

SELECT \* FROM USER\_TRIGGERS WHERE STATUS <> 'ENABLED' AND TABLE\_NAME IN ('TGFCAB', 'TGFITE')

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17442161902487)CAUSA:**

Ocorre quando existe linhas indevidamente na tabela: TGFITE\_INC. Essa tabela recebe apenas o INSERT e DELETE em tempo de execução e sempre deve ficar vazia. Isso é controlado pelas triggers da TGFCAB e TGFITE, que em algum momento, podem ter sido desabilitadas e deixado os registros lá.

Esse erro pode ocorrer em qualquer rotina que envolta as tabelas TGFCAB e TGFITE.
