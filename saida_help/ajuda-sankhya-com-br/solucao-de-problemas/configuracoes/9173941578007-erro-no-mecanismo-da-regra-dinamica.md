---
id: "9173941578007"
titulo: "Erro no mecanismo da regra dinâmica"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9173941578007-Erro-no-mecanismo-da-regra-din%C3%A2mica"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:44Z"
rotulos: ["Configuração", "Eventos", "CORE_E01365", "Problema com Regra Dinâmica", "Regra de validação", "Erro"]
---

# Erro no mecanismo da regra dinâmica

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18583359570199) MENSAGEM:**

[CORE\_E01365] Erro no mecanismo da regra dinâmica.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18583374922135) SITUAÇÃO:**

Mensagem é apresentada ao utilizar algumas regras de negócios.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18583374928279) SOLUÇÃO:**

Revisar as configurações da regra de negócio apresentada na mensagem pois não foi possível executá-la nos parâmetros definidos.

Uma situação comum para este erro é o fato do eventual liberador definido numa regra de negócio com uma evento personalizado, não ter esta alçada definida no cadastro de usuários.

![Imagem 4: Uma situação comum para este erro é o fato do eventual liberador definido numa regra de negócio com uma evento…](https://ajuda.sankhya.com.br/hc/article_attachments/9173755244823)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18583359589015) CAUSA:**

Quando for encontrada alguma inconsistência na regra de negócio.
