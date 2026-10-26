---
id: "13423252216983"
titulo: "Não foi possível resolver o filtro para obtenção da alíquota de ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13423252216983-N%C3%A3o-foi-poss%C3%ADvel-resolver-o-filtro-para-obten%C3%A7%C3%A3o-da-al%C3%ADquota-de-ICMS"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:00:11Z"
rotulos: ["CT-e", "Alíquotas", "Configuração", "Empresa", "ICMS", "CORE_E04499", "Erro no filtro de alíquota ICMS", "Verifique filtros em \"Alíquotas de ICMS\" e \"Empresa\". Ajuste filtros inválidos", "Alíquota de ICMS não respeitada no CTE", "Erro"]
---

# Não foi possível resolver o filtro para obtenção da alíquota de ICMS

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17121230163735) MENSAGEM:**

[CORE\_E04499] Não foi possível resolver o filtro para obtenção da alíquota de ICMS. Verifique a aba "Filtro de Alíquota ICMS" nas preferências da empresa ou a configuração de Filtro para obtenção de alíquota da tela "Alíquotas de ICMS'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17121230170903) SITUAÇÃO:**

Ao inserir o item do CTE a prioridade da alíquota de ICMS não está sendo respeitada e a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17121204439959) SOLUÇÃO:**

![Imagem 4: Verifique na tela " Alíquotas de ICMS" ( Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de…](https://ajuda.sankhya.com.br/hc/article_attachments/17121204443159) Verifique na tela **"Alíquotas de ICMS"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS) se possui algum filtro:

![Imagem 5: Verifique na tela " Alíquotas de ICMS" ( Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de…](https://ajuda.sankhya.com.br/hc/article_attachments/13423115184919)

![Imagem 6: Verifique na tela " Alíquotas de ICMS" ( Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de…](https://ajuda.sankhya.com.br/hc/article_attachments/13423117386135)

![Imagem 7: Verifique também se na tela " Empresa" (Caminho de acesso: Comercial » Preferências » Empresa), aba "Filtro de alíquota…](https://ajuda.sankhya.com.br/hc/article_attachments/17121204453015) Verifique também se na tela **"Empresa"** (Caminho de acesso: Comercial » Preferências » Empresa), aba **"Filtro de alíquota ICMS",** existe algum filtro.

Vale lembrar que essa aba só estará visível se o parâmetro **"Permite duplicar cad. de tributação alíquota ICMS? - PODEDUPALIQICMS"** estiver habilitado.

![Imagem 8: Vale lembrar que essa aba só estará visível se o parâmetro "Permite duplicar cad. de tributação alíquota ICMS? -…](https://ajuda.sankhya.com.br/hc/article_attachments/13423850789527)

![Imagem 9: Caso possua algum filtro em alguma das telas citadas acima será necessário que o criador do filtro revise o mesmo e…](https://ajuda.sankhya.com.br/hc/article_attachments/17121230197527) Caso possua algum filtro em alguma das telas citadas acima será necessário que o criador do filtro revise o mesmo e faça os devidos ajustes.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17121204465815) CAUSA:**

Ocorre quando o filtro utilizado retorna mais de um valor em sua consulta, tornando o mesmo inválido.
