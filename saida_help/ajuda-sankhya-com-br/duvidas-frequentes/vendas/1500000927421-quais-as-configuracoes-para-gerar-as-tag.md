---
id: "1500000927421"
titulo: "Quais as configurações para gerar as TAG de Medicamento no XML?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000927421-Quais-as-configura%C3%A7%C3%B5es-para-gerar-as-TAG-de-Medicamento-no-XML"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-08-19T16:41:32Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Impostos", "não apagar", "Preencha \"Tabela PMC\" e \"Tabela PF\" por estado", "Habilite \"LOTEINFO\" e \"LOTEDTVAL\"; marque \"Tem Rastro do Lote\" em Produto", "Informe \"Cód. ANVISA\"; exemplo de XML gerado", "Medicamentos"]
---

# Quais as configurações para gerar as TAG de Medicamento no XML?

**Vejamos as configurações necessárias:**

![Imagem 1: Acesse " Configurações » Cadastros » Endereços » Estados ". O campo " Tabela de Preço PMC " deve ser preenchido o…](https://ajuda.sankhya.com.br/hc/article_attachments/16282379791639) Acesse "Configurações » Cadastros » Endereços » Estados". O campo "**Tabela de Preço PMC**" deve ser preenchido o código da tabela PMC do estado e o campo "**Tabela de Preço P**F" a tabela PF do estado:

![Imagem 2: Acesse " Configurações » Cadastros » Endereços » Estados ". O campo " Tabela de Preço PMC " deve ser preenchido o…](https://ajuda.sankhya.com.br/hc/article_attachments/18189213088791)

Desta forma, cada estado deve ter uma "**Tabela PMC**" e outra "**Tabela PF**" conforme a alíquota de seu respectivo estado em "**Tabela de Preço** - Comercial » Arquivo » Tabelas de Preços".

![Imagem 3: Desta forma, cada estado deve ter uma " Tabela PMC " e outra " Tabela PF " conforme a alíquota de seu respectivo estado…](https://ajuda.sankhya.com.br/hc/article_attachments/18189214282135)

Com as configurações corretas, o sistema busca o preço praticado conforme regra ANVISA. **Se tiver PMC, busca preço PMC, se não tiver busca preço PF:**

![Imagem 4: Com as configurações corretas, o sistema busca o preço praticado conforme regra ANVISA. Se tiver PMC, busca preço PMC,…](https://ajuda.sankhya.com.br/hc/article_attachments/18189215961111)

![Imagem 5: Com as configurações corretas, o sistema busca o preço praticado conforme regra ANVISA. Se tiver PMC, busca preço PMC,…](https://ajuda.sankhya.com.br/hc/article_attachments/18189217279255)

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16282379795607) OBSERVAÇÃO:**

Se os campos Tabela de Preço PMC e Tabela de Preço PF não estiverem preenchidos, o sistema validará a tabela configurada no parâmetro **"Tabela de Preço PMC - CODTABPMC"**.

![Imagem 7: S e os campos Tabela de Preço PMC e Tabela de Preço PF não estiverem preenchidos, o sistema validará a tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/12832432352535)

Parâmetro **"LOTEINFO -Informações adicionais para Lotes?":**  ligado
Parâmetro **"LOTEDTVAL Usar data de validade junto com Lote?":** ligado

![Imagem 8: Acesse cadastro de Produto em: Configurações » Cadastros » Produtos » Produtos Aba: "Geral" Campo "Tem Rastro do Lote"…](https://ajuda.sankhya.com.br/hc/article_attachments/16282379800855) Acesse cadastro de Produto em: Configurações » Cadastros » Produtos » Produtos
Aba: **"Geral"**
Campo **"Tem Rastro do Lote"**: marcado

![Imagem 9: Acesse cadastro de Produto em: Configurações » Cadastros » Produtos » Produtos Aba: "Geral" Campo "Tem Rastro do Lote"…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001150701)

Aba: **"Impostos"**
Campo **"Gênero"**: 30

![Imagem 10: Aba: "Impostos" Campo "Gênero" : 30](https://ajuda.sankhya.com.br/hc/article_attachments/1500001075002)

Aba: **"Medicamentos"**
Campo **"Cód. ANVISA"**: informe um valor válido, conforme regulamentação da Anvisa.

![Imagem 11: Aba: "Medicamentos" Campo "Cód. ANVISA" : informe um valor válido, conforme regulamentação da Anvisa.](https://ajuda.sankhya.com.br/hc/article_attachments/1500001150721)

**(1)** Exemplo Tag gerada no XML da Nota Fiscal Eletrônica(Modelo 55)

`<``med``>`

`<``nLote``>2308Q0723</``nLote``>`

`<``qLote``>5000.000</``qLote``>`

`<``dFab``>2019-09-23</``dFab``>`

`<``dVal``>2020-11-30</``dVal``>`

`<``vPMC``>0.00</``vPMC``>`

`</``med``>`
