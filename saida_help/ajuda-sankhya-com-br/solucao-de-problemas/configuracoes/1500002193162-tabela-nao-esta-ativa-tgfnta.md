---
id: "1500002193162"
titulo: "Tabela não está Ativa.(TGFNTA)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002193162-Tabela-n%C3%A3o-est%C3%A1-Ativa-TGFNTA"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:44Z"
rotulos: ["Configuração", "#formatadoroger", "ORA-20101", "Ativação de Tabela de Preços Inativa", "Erro", "Comercial", "Tabela de Preços"]
---

# Tabela não está Ativa.(TGFNTA)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16302205477783) MENSAGEM:**

[ORA-20101]: Tabela não está Ativa.(TGFNTA)
[ORA-06512]: em "TESTE.TRG\_INC\_TGFTAB", line 90
[ORA-04088]: erro durante a execução do gatilho 'TESTE.TRG\_INC\_**TGFTAB**'

**![Imagem 2: OBSERVAÇÃO: Neste caso a tabela que não esta ativa é a Tabela de Preços (TGFTAB), como mencionado na descrição do erro.](https://ajuda.sankhya.com.br/hc/article_attachments/16302205479319) OBSERVAÇÃO:** Neste caso a tabela que não esta ativa é a Tabela de Preços (TGFTAB), como mencionado na descrição do erro.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16302205480983) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse a rotina de Tabela de Preços em: Comercial » Arquivo » Tabelas de Preços](https://ajuda.sankhya.com.br/hc/article_attachments/16302202221847) Acesse a rotina de Tabela de Preços em: Comercial » Arquivo » Tabelas de Preços

Verifique a tabela de preço que incidiu nos itens da nota e verifique se o campo **"Ativo"** está: **sim**.

Marque a tabela como **ativo,** ou verifique com a área responsável se os produtos da nota deveriam ter recebido outra tabela de preço, efetue o ajuste necessário.

![Imagem 5: Marque a tabela como ativo, ou verifique com a área responsável se os produtos da nota deveriam ter recebido outra…](https://ajuda.sankhya.com.br/hc/article_attachments/15027304475287)

![Imagem 6: Após os ajustes, confirme novamente o documento.](https://ajuda.sankhya.com.br/hc/article_attachments/16302202223127) Após os ajustes, confirme novamente o documento.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16302202224279) CAUSA:**

Ocorre porque no momento da confirmação da nota a tabela de preço a ser utilizada não ativa.
