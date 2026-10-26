---
id: "9173182333719"
titulo: "Alíquota para substituição tributária não encontrada para a UF MG sem restrição"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9173182333719-Al%C3%ADquota-para-substitui%C3%A7%C3%A3o-tribut%C3%A1ria-n%C3%A3o-encontrada-para-a-UF-MG-sem-restri%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:50Z"
rotulos: ["CORE_E04485", "Alíquotas", "Configuração", "NF-e", "ICMS", "Impostos", "Estoque", "Erro de Alíquota para Substituição Tributária"]
---

# Alíquota para substituição tributária não encontrada para a UF MG sem restrição

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18606729084311) MENSAGEM:**

[CORE\_E04485]  Alíquota para substituição tributária não encontrada para a UF MG sem restrição.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18606729089175) SITUAÇÃO:**

Ao tentar confirmar uma nota de devolução de compras ou fazer um inventário no ajuste de estoque a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18606729095959) CAUSA:**

Ocorre quando a alíquota de ICMS não for encontrada.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18606736522647) SOLUÇÃO:**

Nas TOPs utilizadas para o ajuste, quando não atualizam o livro fiscal e estão configuradas como **"Calcula e Digita"**, o sistema irá buscar alguma regra de Alíquota de ICMS para preencher no lançamento que será gerado.
Para eliminar o aviso, teria que utilizar  as TOPs como **"Não calcula e Digita"** ou criar uma regra de Alíquota de ICMS para os produtos que possuem substituição tributária.

Já para os casos de notas de devolução é necessário cadastrar a regra de Alíquota de ICMS corretamente para o estado em questão.
