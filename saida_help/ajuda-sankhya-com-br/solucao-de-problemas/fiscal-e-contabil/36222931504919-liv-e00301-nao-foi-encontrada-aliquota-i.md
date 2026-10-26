---
id: "36222931504919"
titulo: "LIV_E00301 - Não foi encontrada alíquota interna para a empresa selecionada. Verifique o Cadastro de Alíquota de ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36222931504919-LIV-E00301-N%C3%A3o-foi-encontrada-al%C3%ADquota-interna-para-a-empresa-selecionada-Verifique-o-Cadastro-de-Al%C3%ADquota-de-ICMS"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:23:27Z"
rotulos: ["Configuração", "NF-e", "ICMS", "Impostos", "Alíquotas de ICMS", "Alíquota de ICMS", "Alíquota interna", "LIV_E00301"]
---

# LIV_E00301 - Não foi encontrada alíquota interna para a empresa selecionada. Verifique o Cadastro de Alíquota de ICMS

**MENSAGEM:**

[LIV\_E00301] Não foi encontrada alíquota interna para a empresa selecionada. Verifique o Cadastro de Alíquota de ICMS.

**SOLUÇÃO:**

**(1)** Acesse a tela [**''Alíquota de ICMS''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS) (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS).

**(2)** Localize o **estado (UF)** correspondente ao cadastro da empresa, e em seguida, **cadastre uma alíquota interna** para essa UF, garantindo que:

- Não exista **exceção** configurada;
- A alíquota seja cadastrada como **interna**;
- O campo **“Alíquota”** possua um valor **maior que zero**.

**CAUSA:**

A rotina exige uma **alíquota interna de ICMS sem exceções** para realizar o processamento.

Quando essa alíquota não está configurada, o sistema não encontra um valor válido para aplicar, gerando a mensagem de erro.
