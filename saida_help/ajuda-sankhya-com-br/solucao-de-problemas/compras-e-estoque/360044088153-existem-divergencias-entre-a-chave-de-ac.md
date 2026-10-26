---
id: "360044088153"
titulo: "Existem divergências entre a chave de acesso da nota e seus dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088153-Existem-diverg%C3%AAncias-entre-a-chave-de-acesso-da-nota-e-seus-dados"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-09-03T19:07:13Z"
rotulos: ["CORE_E02961", "Configuração", "Fiscal", "Parceiro", "NF-e", "XML", "Ajuste de parâmetros", "Identificação de Informações", "Divergências na Chave de Acesso", "Erro"]
---

# Existem divergências entre a chave de acesso da nota e seus dados

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16363221160471) MENSAGEM:**

[CORE\_E02961] Existem divergências entre a chave de acesso da nota e seus dados: (...)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363226832791)SOLUÇÃO:**

![Imagem 3: Identifique na mensagem de validação apresentada quais são as informações causadoras da divergência.](https://ajuda.sankhya.com.br/hc/article_attachments/16363221166103) Identifique na mensagem de validação apresentada quais são as informações causadoras da divergência.

**Exemplo:**

Existem divergências entre a chave de acesso da nota e seus dados:

- AAMM (Chave) = 1902
- Dt. Neg. (Sistema) = 1903

Para o caso acima, a data de negociação no sistema consta como 19/03 e na chave enviada pelo parceiro como 19/02. Dessa forma, a opção seria **ajustar esse campo data no sistema**, para que a confirmação seja permitida.

![Imagem 4: Caso a divergência de fato deva existir, ajuste o parâmetro abaixo para " Não Valida" ou " Valida e avisa" :](https://ajuda.sankhya.com.br/hc/article_attachments/16363226838295) Caso a divergência de fato deva existir, ajuste o parâmetro abaixo para "**Não Valida"** ou "**Valida e avisa"**:

- Configurações » Avançado » Preferências: Chave **"VALCHAVETERC"**

![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16363226839959) **CAUSA:**

Ao realizar o lançamento/importação de nota de "**Terceiros"**, quando existir divergências entre as informações apresentadas no sistema e as informações do XML, se o parâmetro VALCHAVETERC encontrar-se configurado como Valida, será apresentada a mensagem.
