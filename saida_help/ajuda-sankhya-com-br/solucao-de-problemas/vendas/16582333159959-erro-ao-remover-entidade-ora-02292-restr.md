---
id: "16582333159959"
titulo: "Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.AD_FK_XXXXXXXXXXXXX) violada - registro filho localizado\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16582333159959-Erro-ao-remover-entidade-ORA-02292-restri%C3%A7%C3%A3o-de-integridade-SANKHYA-AD-FK-XXXXXXXXXXXXX-violada-registro-filho-localizado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-20T13:43:57Z"
rotulos: ["Configuração", "Construtor de Telas", "Financeiro", "DBExplorer", "SANKHYA.AD_FK_", "Restrição de integridade violada", "Localize e exclua registros relacionados", "Tabela adicional impede cancelamento", "ORA-02292", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.AD_FK_XXXXXXXXXXXXX) violada - registro filho localizado"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16582297238423)  MENSAGEM:**

Erro ao remover entidade: ORA-02292: restrição de integridade (SANKHYA.AD\_FK\_XXXXXXXXXXXXX) violada - registro filho localizado

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16582272915735) CAUSA:**

Ocorre quando a tabela adicional a qual a FK está relacionada impossibilita o cancelamento.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16582304226711) SOLUÇÃO:**

![Imagem 4: Acesse a tela DBExplorer ( Configurações » Avançado » DBExplorer)](https://ajuda.sankhya.com.br/hc/article_attachments/16582333148951) Acesse a tela **DBExplorer** (Configurações » Avançado » DBExplorer)

Realize o SELECT a seguir na FK que o Sankhya está indicando o erro.

Copie o **AD\_FK\_XXXXXXXXXXXX** e cole onde está essa mesma informação no SELECT:

**Query para Banco de Dados Oracle:**

SELECT TABLE\_NAME AS TABELA, COLUMN\_NAME AS COLUNA, CONSTRAINT\_NAME AS FK
FROM USER\_CONS\_COLUMNS
WHERE CONSTRAINT\_NAME LIKE '%AD\_FK\_XXXX%'

**Query para Banco de Dados SQL Server:**

SELECT TABLE\_NAME AS TABELA, COLUMN\_NAME AS COLUNA, CONSTRAINT\_NAME AS FK
FROM INFORMATION\_SCHEMA.CONSTRAINT\_COLUMN\_USAGE
WHERE CONSTRAINT\_NAME LIKE '%AD\_FK\_XXXX%'

![Imagem 5: SELECT TABLE_NAME AS TABELA, COLUMN_NAME AS COLUNA, CONSTRAINT_NAME AS FK FROM USER_CONS_COLUMNS WHERE CONSTRAINT_NAME…](https://ajuda.sankhya.com.br/hc/article_attachments/16583716247447)

![Imagem 6: SELECT TABLE_NAME AS TABELA, COLUMN_NAME AS COLUNA, CONSTRAINT_NAME AS FK FROM USER_CONS_COLUMNS WHERE CONSTRAINT_NAME…](https://ajuda.sankhya.com.br/hc/article_attachments/16583733408535)

![Imagem 7: Acesse a tela Construtor de Telas ( Configurações » Avançado » Construtor de Telas)](https://ajuda.sankhya.com.br/hc/article_attachments/16582288328983) Acesse a tela **Construtor de Telas** (Configurações » Avançado » Construtor de Telas)

- Filtre o resultado da TABLE\_NAME "TABELA" no campo Nome da Tabela que foi apresentado no DBExplorer:
- Selecione a linha e acesse o botão Outras opções » Lançador » Localizar lançador

![Imagem 8: Selecione a linha e acesse o botão Outras opções » Lançador » Localizar lançador](https://ajuda.sankhya.com.br/hc/article_attachments/16583742127127)

-  Logo será aberto o caminho em que NUNOTA se encontra:

![Imagem 9: - Logo será aberto o caminho em que NUNOTA se encontra:](https://ajuda.sankhya.com.br/hc/article_attachments/16583743410839)

![Imagem 10: Acesse o caminho que foi apresentado e filtre pelo Nro Único da nota que está apresentado o erro. Exclua o registro,…](https://ajuda.sankhya.com.br/hc/article_attachments/16582304232343) Acesse o caminho que foi apresentado e filtre pelo Nro Único da nota que está apresentado o erro. Exclua o registro, retorne ao Portal e Cancele a nota novamente.

**![Imagem 11: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16585141368599) OBSERVAÇÃO:**

O erro pode aparecer em qualquer outra tela do sistema, não somente no cancelamento de notas e não necessariamente a tabela relacionada em questão poderá estar vinculada a uma tela especificamente.
