---
id: "360042871374"
titulo: " Preço de venda não pode ser zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042871374--Pre%C3%A7o-de-venda-n%C3%A3o-pode-ser-zero"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:21Z"
rotulos: ["#PUBLIFER", "CORE_E04667", "Produtos", "Configuração", "NF-e", "SEFAZ", "TOP", "Preço", "Preço Venda Zero", "Verificação Tabela Preços", "Configuração Precificação Ajuste"]
---

#  Preço de venda não pode ser zero

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16114624259351) MENSAGEM:**

[CORE\_E04667] Preço de venda não pode ser zero.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16114624265111) SOLUÇÃO:**

![Imagem 3: Acesse a tela "Preferências" (Configurações » Avançado) .](https://ajuda.sankhya.com.br/hc/article_attachments/16114624268823) Acesse a tela **"Preferências"** (Configurações » Avançado).

Chave **"TIPTABPRECO - Tabela de Preços por"**

![Imagem 4: Chave "TIPTABPRECO - Tabela de Preços por"](https://ajuda.sankhya.com.br/hc/article_attachments/14559842334359)

![Imagem 5: De acordo com o definido acima, verifique se existe uma tabela de preço vinculada no respectivo cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/16114659394839) De acordo com o definido acima, verifique se existe uma tabela de preço vinculada no respectivo cadastro.

**Exemplo:** TIPTABPRECO =Tipo de Negoc.

**(2)** Tela **"[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)["](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)** (Caminho de acesso: Comercial » Arquivo » Cadastros), Aba Características, Campo **"Tabela de Preço"**.

![Imagem 6: Realizada a conferência da tabela de preço conforme acima, certifique-se que existe preço/custo inserido para a…](https://ajuda.sankhya.com.br/hc/article_attachments/16114624280599) Realizada a conferência da tabela de preço conforme acima, certifique-se que existe preço/custo inserido para a respectiva tabela/itens do lançamento conforme próximos passos.

![Imagem 7: Acesse a tela " Tipos de Operação - TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros), Aba "Geral"](https://ajuda.sankhya.com.br/hc/article_attachments/16114659408919) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros), Aba **"Geral"**

**(2)** Verifique o Campo: **"Usar como Preço":** Caso esteja **diferente** de Preço de Venda, se faz necessário o produto ter um custo de acordo com que está configurado nesta opção. Para verificar os custos do produto acesse a tela de **"[Variação de Custo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594114-Varia%C3%A7%C3%A3o-de-Custos-de-Produtos)"**.

**(2)** Caso esteja como Preço de Venda, utilize a rotina Comercial » Consulta » **"[Variação de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753-Varia%C3%A7%C3%A3o-de-Pre%C3%A7os-de-Produtos) [de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119753-Varia%C3%A7%C3%A3o-de-Pre%C3%A7os-de-Produtos)"** para identificar se existe preço para esse item.

![Imagem 8: Identificado o preço e/ou custo a ser utilizado, solicite apoio a um usuário certificado de sua empresa que tenha…](https://ajuda.sankhya.com.br/hc/article_attachments/16114624286615) Identificado o preço e/ou custo a ser utilizado, solicite apoio a um usuário certificado de sua empresa que tenha conhecimento no processo de precificação através das rotinas abaixo, para que o preço torne-se diferente de zero, e a mensagem seja sanada:

**(2)** Atualização de preço de venda

**(2)** Tabelas de Preço

**(2)** Atualização de Custos

Realizada a precificação, consulte nas rotinas de variação mencionadas no Item 1, sendo o preço devidamente apresentado prossiga com o lançamento.

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17802233840663) IMPORTANTE:**

Caso o lançamento seja em uma NF-e (Nota Fiscal Eletrônica) e o produto realmente tenha que ter valor unitário 0(zero), o Tipo de Emissão deve ser: **Complementar** ou **Ajuste** e o parâmetro **"ACEITARVLRZERO"** ligado. A Sefaz rejeita NF-e de emissão Normal com valor zerado.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16114624295063) CAUSA:**

Mensagem apresentada quando utilizado no lançamento um tipo de operação que use como preço um valor não localizado no sistema para o respectivo item.
