---
id: "360044110514"
titulo: "Código do município inválido. Utilizar código da \"Tabela de Municípios do IBGE\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110514-C%C3%B3digo-do-munic%C3%ADpio-inv%C3%A1lido-Utilizar-c%C3%B3digo-da-Tabela-de-Munic%C3%ADpios-do-IBGE"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:32Z"
rotulos: ["Configuração", "SPED", "Fiscal", "Parceiro", "Cidades", "IBGE", "Verifique cadastros", "Use tabela IBGE", "Código município inválido"]
---

# Código do município inválido. Utilizar código da "Tabela de Municípios do IBGE"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16591160010903) MENSAGEM:**

Código do município inválido. Utilizar código da "Tabela de Municípios do IBGE".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16591199514391) SOLUÇÃO:**

![Imagem 3: Identifique no erro apresentado qual "participante/parceiro" está sendo validado.](https://ajuda.sankhya.com.br/hc/article_attachments/16591199518615) Identifique no erro apresentado qual "participante/parceiro" está sendo validado.

**Exemplo:**

|0150|000000006|**SANKHYA GESTÃO DE NEGÓCIOS** |01058|51254159000173||336122330119|3518800||Av Teste|1688||CUMBICA|

No registro 150, a posição 3 refere-se ao 'Nome Participante', ou seja, 'Sankhya Gestão de Negócios'.

![Imagem 4: Realizada a identificação acima, acesse o cadastro do parceiro e verifique na aba "Endereço" a 'Cidade' do mesmo.](https://ajuda.sankhya.com.br/hc/article_attachments/16591160016535) Realizada a identificação acima, acesse o cadastro do parceiro e verifique na aba **"Endereço"** a 'Cidade' do mesmo.

![Imagem 5: Acesse a tela "Cidades" (Caminho de acesso: Configurações » Cadastros » Endereços) e para o cadastros de cidade…](https://ajuda.sankhya.com.br/hc/article_attachments/16591199523863) Acesse a tela **"Cidades"** (Caminho de acesso: Configurações » Cadastros » Endereços) e para o cadastros de cidade localizado no item 1, verifique a informação contida no campo **"Mun. domicílio fiscal":**

![Imagem 6: Acesse a tela "Cidades" (Caminho de acesso: Configurações » Cadastros » Endereços) e para o cadastros de cidade…](https://ajuda.sankhya.com.br/hc/article_attachments/16591160022551) Informe no campo citado anteriormente o "**Mun. domicílio fiscal**" conforme tabela do IBGE, disponível no link [http://www.ibge.gov.br/home/geociencias/areaterritorial/area.shtm.](http://www.ibge.gov.br/home/geociencias/areaterritorial/area.shtm)

![Imagem 7: Acesse a tela "Cidades" (Caminho de acesso: Configurações » Cadastros » Endereços) e para o cadastros de cidade…](https://ajuda.sankhya.com.br/hc/article_attachments/16591199529367) Realizado o ajuste, faça a geração de um novo arquivo do SPED e valide novamente no PVA.

**![Imagem 8: Acesse a tela "Cidades" (Caminho de acesso: Configurações » Cadastros » Endereços) e para o cadastros de cidade…](https://ajuda.sankhya.com.br/hc/article_attachments/16591199532823) CAUSA:**

Mensagem apresentada ao validar o SPED Fiscal através do PVA, quando não informado ou informado um Cód.Município que difere do definido na 'Tabela de Municípios'.
