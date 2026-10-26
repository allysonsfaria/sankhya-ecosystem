---
id: "360043421533"
titulo: "Alíquota para substituição tributária não encontrada para a UF Y-XX sem restrição"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043421533-Al%C3%ADquota-para-substitui%C3%A7%C3%A3o-tribut%C3%A1ria-n%C3%A3o-encontrada-para-a-UF-Y-XX-sem-restri%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:00Z"
rotulos: ["#criadoRoger", "CORE_E04485", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "Verificar regra ICMS", "ICMS substituição faltante", "Ajustar conforme contador"]
---

# Alíquota para substituição tributária não encontrada para a UF Y-XX sem restrição

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16117172731415) MENSAGEM**:

[CORE\_E04485] Alíquota para substituição tributária não encontrada para a UF Y-XX sem restrição.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16117188915607) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Identifique a regra de ICMS que incidiu nos itens da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16117172737687) Identifique a regra de ICMS que incidiu nos itens da nota.

**(2)** Acesse os itens da nota e verifique o campo **"Cód. Alíq ICMS"**.

**(2)** Em cada item existe este campo, que representa a Regra de ICMS que incidiu na nota.

![Imagem 4: (2) Em cada item existe este campo, que representa a Regra de ICMS que incidiu na nota.](https://ajuda.sankhya.com.br/hc/article_attachments/14605670272151)

![Imagem 5: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16117172749207) Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

**(2)** De posse do código, acesse o cadastro de **"[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS)"** e pesquise pela regra de ICMS.

**(2)** Acesse a aba **"Substituição Tributária"**

**(2)** De acordo com as informações fornecidas pelo Contador/Equipe Fiscal, preencha o campo **"Alíq. Subst. Tributária"**.

**(2)** Salve as alterações e efetue novamente o lançamento do documento.

**![Imagem 6: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16117188927767) CAUSA**:

Ocorre quando as regras de ICMS, estão incompletas.
