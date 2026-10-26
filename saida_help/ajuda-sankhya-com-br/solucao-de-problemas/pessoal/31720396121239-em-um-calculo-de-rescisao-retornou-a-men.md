---
id: "31720396121239"
titulo: "Em um cálculo de rescisão retornou a mensagem: \"A subconsulta retornou mais de 1 valor. Isso não é permitido...\" O que fazer?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31720396121239-Em-um-c%C3%A1lculo-de-rescis%C3%A3o-retornou-a-mensagem-A-subconsulta-retornou-mais-de-1-valor-Isso-n%C3%A3o-%C3%A9-permitido-O-que-fazer"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:41Z"
rotulos: ["Folha", "Rescisão", "Férias", "Isso não é permitido quando a subconsulta segue um", "ou quando ela é usada como uma expressão.", "java.sql.SQLException", "A subconsulta retornou mais de 1 valor", "cálculo de rescisão", "Erro", "TFPFER"]
---

# Em um cálculo de rescisão retornou a mensagem: "A subconsulta retornou mais de 1 valor. Isso não é permitido..." O que fazer?

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31991515942935) MENSAGEM:**

**Falha:** java.sql.SQLException: A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, <, <= , >, >= ou quando ela é usada como uma expressão.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31991499498519) SITUAÇÃO:**

Durante a tentativa de cálculo de rescisão, foi apresentada a mensagem abaixo impedindo a conclusão do cálculo.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31991499499159) SOLUÇÃO:**

Avalie os registros de férias (TFPFER) do colaborador para identificar se existe algum período aquisitivo duplicado, sem a devida marcação de **"gozado"**.

(1)**Se existir duas sequências para o mesmo período de férias usufruídas e ambas sem marcação de gozadas:**

Apenas a última sequência deve constar com a marcação de "gozada", pois a marcação só é feita para indicar que o período aquisitivo foi finalizado.

(1)** Se existir dois período de férias em aberto que não foram usufruídas:**

O segundo período aquisitivo em aberto deve ser excluído, mantendo apenas um único período aquisitivo válido. Dessa forma, ao calcular as férias, o sistema gerará automaticamente o novo período correspondente.

Essa ação de correção resolve o conflito de registros duplicados e permite a realização correta do cálculo da rescisão.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31991515948823) CAUSA:**

O sistema, ao buscar informações sobre férias para o cálculo da rescisão, encontrou duplicidade das informações e não conseguiu definir um único valor a ser utilizado, gerando a falha no processo.
