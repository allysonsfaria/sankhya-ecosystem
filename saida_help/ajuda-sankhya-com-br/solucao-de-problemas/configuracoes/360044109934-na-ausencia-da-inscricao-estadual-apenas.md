---
id: "360044109934"
titulo: "Na ausência da Inscrição Estadual, apenas a Classificação ICMS: \"Consumidor Final Não Contribuinte\" e \"Produtor Rural\" são permitidas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109934-Na-aus%C3%AAncia-da-Inscri%C3%A7%C3%A3o-Estadual-apenas-a-Classifica%C3%A7%C3%A3o-ICMS-Consumidor-Final-N%C3%A3o-Contribuinte-e-Produtor-Rural-s%C3%A3o-permitidas"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:12Z"
rotulos: ["CORE_E05370", "Configuração", "Fiscal", "Parceiro", "ICMS", "Restrições na Ausência de Inscrição Estadual", "Inscrição Estadual"]
---

# Na ausência da Inscrição Estadual, apenas a Classificação ICMS: "Consumidor Final Não Contribuinte" e "Produtor Rural" são permitidas

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16593687797143) MENSAGEM:**

[CORE\_E05370]: Na ausência da Inscrição Estadual, apenas a Classificação ICMS: "Consumidor Final Não Contribuinte" e "Produtor Rural" são permitidas.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16593687798935) SOLUÇÃO:**

Valide com o respectivo parceiro se sua 'Classificação de ICMS' foi configurada corretamente no sistema, em caso positivo preencha sua 'Inscrição Estadual' conforme dados do Sintegra:

(1)** PESSOA FÍSICA:**

![Imagem 3: Se o parceiro a ser cadastrado for pessoa física e não informado o RG, então na aba "Fiscal" , campo " Classificação…](https://ajuda.sankhya.com.br/hc/article_attachments/16593687804055) Se o parceiro a ser cadastrado for pessoa física e não informado o RG, então na aba **"Fiscal"**, campo "**Classificação ICMS**", as opções selecionadas devem ser "**Consumidor Final Não Contribuinte"** ou "**Produtor Rural"**:

![Imagem 4: Se o parceiro a ser cadastrado for pessoa física e não informado o RG, então na aba "Fiscal" , campo " Classificação…](https://ajuda.sankhya.com.br/hc/article_attachments/15185982659095)

(1)** PESSOA JURÍDICA:**

![Imagem 5: Se o parceiro a ser cadastrado for pessoa jurídica e não informada a Inscrição Estadual (IE), realize a pesquisa pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/16593687805207) Se o parceiro a ser cadastrado for pessoa jurídica e não informada a Inscrição Estadual (IE), realize a pesquisa pelo CNPJ do parceiro no [http://www.sintegra.gov.br](http://www.sintegra.gov.br/), certifique-se sobre a existência de IE vinculado para o mesmo e, em caso positivo, preencha essa informação no sistema, campo "**Insc. Estadual / Identidade"** do cadastro do parceiro.

![Imagem 6: Caso o cliente não tenha a inscrição, o parceiro pode ser isento, então no campo " Insc. Estadual / Identidade " o…](https://ajuda.sankhya.com.br/hc/article_attachments/16593693358615) Caso o cliente não tenha a inscrição, o parceiro pode ser isento, então no campo "**Insc. Estadual / Identidade**" o valor a ser inserido deve ser '**Isento**' (maiúsculo e sem aspas) e o valor do campo Classificação ICMS (aba Fiscal) tem que ser '**Isento De ICMS**'.

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16593687811607) IMPORTANTE:**

Para o Estado do RJ é possível inserir um parceiro MEI (Revendedor/ IE não informado): Nesse caso é preciso que a opção **"Micro empresário individual"**, localizada na aba Fiscal esteja marcada.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16593693361815) CAUSA:**

Ao fazer o cadastro de parceiro sem o valor do campo Insc. Estadual / Identidade preenchido, e essa ausência for incompatível com a 'Classificação de ICMS' do mesmo, será apresentada a mensagem.
