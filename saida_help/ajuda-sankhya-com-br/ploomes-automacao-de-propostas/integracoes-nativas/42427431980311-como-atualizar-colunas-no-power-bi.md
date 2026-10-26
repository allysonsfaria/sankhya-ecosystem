---
id: "42427431980311"
titulo: "Como atualizar colunas no Power BI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427431980311-Como-atualizar-colunas-no-Power-BI"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:07Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11395888", "sync_hash_f645a2c67256"]
---

# Como atualizar colunas no Power BI

Quando você altera colunas na aba do Ploomes, essas alterações **não são refletidas automaticamente** na fonte de dados já configurada no Power BI.
Para que o Power BI reconheça as novas colunas, é necessário **configurar a aba como uma nova fonte de dados**.

## Como atualizar as colunas

Para trazer novas colunas inseridas na aba (tabela no Ploomes) para o Power BI, é necessário configurá-la como uma nova fonte de dados.

1. No Ploomes, copie o link de exportação gerado para a aba.
2. No Power BI Desktop, acesse **Página Inicial**.
3. Clique em **Obter dados** e selecione **Web**.
4. No campo solicitado, cole o link copiado do Ploomes.
5. Confirme em **OK** para carregar a nova fonte de dados.

[GIF animado: Imagem 1: Confirme em OK para carregar a nova fonte de dados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1845736615/2a66334dcdb0ec9cc59fb1ca7a52/Nova+se%C3%A7a+%282%29.gif?expires=1786536000&signature=6cf329c0f02ad7737b0c209dc4ceb385806f65487a9cc7f332f8838b1ae32179&req=dSgjE859m4deXPMW3nq%2BgTsdbN4Ep6AZr5TX5AUudvVqgmrPIGltCJV6WR6R%0AGErrpJnG9gt%2BdqvJInDZmyvt1wE%3D%0A)

⚠️ **Importante**: qualquer alteração nas colunas exige essa reconfiguração.

## Realizei o procedimento e ainda não atualizou. O que fazer?

Isso pode acontecer por conta de **cache armazenado no Power BI**. Para limpar o cache:

1. No Power BI Desktop, vá em **Arquivo > Opções e configurações > Opções**.
2. Na seção **Global**, selecione **Carregamento de dados**.
3. Clique em **Limpar cache**.
4. Reimporte o link da aba, se necessário.

[GIF animado: Imagem 2: Reimporte o link da aba, se necessário.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1528136865/b0c79edfb739302c8359e63b7cd6/Animacao14.gif?expires=1786536000&signature=7c4032006a153db68b028040c988833e5337923bbe6fcfbb95bc5a00ab55335a&req=dSUlHsh9m4lZXPMW3nq%2BgcZc7GE%2Fe0cU%2F9mx7Tt%2B65brjBockHaYvF%2FzGOs1%0A6yk9s35PRjnT1CjIqRwn3P493uM%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
