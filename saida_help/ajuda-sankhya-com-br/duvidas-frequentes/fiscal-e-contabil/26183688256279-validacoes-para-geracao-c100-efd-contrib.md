---
id: "26183688256279"
titulo: "Validações para geração C100 - EFD CONTRIBUIÇÕES - PIS/COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26183688256279-Valida%C3%A7%C3%B5es-para-gera%C3%A7%C3%A3o-C100-EFD-CONTRIBUI%C3%87%C3%95ES-PIS-COFINS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:43:05Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "TOP", "EFD Contribuições", "PIS/COFINS", "Documentos Eletrônicos"]
---

# Validações para geração C100 - EFD CONTRIBUIÇÕES - PIS/COFINS

Veja neste artigo as regras e critérios do sistema para geração do registro C100, separando as regras pelo Tipo de Movimento das TOP's usada no lançamento dos documentos.

#### **(1)** Regras gerais:

![Imagem 1: Os documentos devem estar na tela "Cadastro Livro ICMS/IPI" com o campo "Origem" igual a: Estoque ou Complemento .](https://ajuda.sankhya.com.br/hc/article_attachments/26350256473239) Os documentos devem estar na tela **"Cadastro Livro ICMS/IPI"** com o campo **"Origem"** igual a: **Estoque ou Complemento**.

![Imagem 2: O sistema busca na tela Cadastro Livro ICMS/IPI os documentos, olhando o campo de "data do movimento" e não pelo campo…](https://ajuda.sankhya.com.br/hc/article_attachments/26350240540311) O sistema busca na tela Cadastro Livro ICMS/IPI os documentos, olhando o campo de **"data do movimento"** e **não** pelo campo **"data do documento"**.

![Imagem 3: No cadastro das preferências da empresa (Comercial), na aba "Regime de Apuração da Contrib. Social e Aprop. Crédito"…](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) No cadastro das preferências da empresa (Comercial), na aba **"Regime de Apuração da Contrib. Social e Aprop. Crédito"**  deve existir uma configuração para a empresa geradora do TXT, onde a **"data inicial"** e **"data final"** da configuração esteja acobertada pelas datas de geração do TXT.

![Imagem 4: Se estiver sendo gerado com data maior ou igual 01/09/2014 e nas Preferências da empresa (Caminho: Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/26350240549271) Se estiver sendo gerado com data **maior** ou **igual** 01/09/2014 e nas Preferências da empresa (Caminho: Comercial » Preferências » Empresa), na aba **"EFD - Escrituração Fiscal Digital"**, no tipo de escrituração **"EFD Contribuições"**, o campo **"Indicador da apuração das contribuições e créditos"** estiver como **"2 - Apuração com base nos registro individualizado de NF-e e ECF",**  o sistema filtrará os seguintes modelos: **1, 4, 55, 65, 901.** Por outro lado, caso uma das duas informações acima não seja verdadeira, o sistema filtrará os modelos dos documentos da seguinte maneira: **1, 4, 55, 901**.

Estas são as regras gerais pelas quais passarão todos os tipos de movimentos de TOP usados nos lançamentos dos documentos, sejam eles: compras, vendas, devoluções de venda, entre outros.

Diante disso, confira as condições individualizadas de cada **Tipo de movimento** das TOP's:

#### **(1)** Validações para cenário para "Compras":

![Imagem 5: Documento lançado com Tipo de movimento diferente de "Devolução de Venda" ;](https://ajuda.sankhya.com.br/hc/article_attachments/26350256473239) Documento lançado com Tipo de movimento **diferente** de **"Devolução de Venda"**;

![Imagem 6: Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como Estoque;](https://ajuda.sankhya.com.br/hc/article_attachments/26350240540311) Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como **Estoque;**

![Imagem 7: Na tela C adastro Livro ICMS/IPI o Campo " entrada/saída " deve estar como Entrada;](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) Na tela Cadastro Livro ICMS/IPI o Campo "**entrada/saída**" deve estar como **Entrada;**

![Imagem 8: No documento, deve-se ter obrigatoriamente as linhas de PIS/COFINS na tabela de impostos;](https://ajuda.sankhya.com.br/hc/article_attachments/26350240549271) No documento, deve-se ter **obrigatoriamente** as linhas de PIS/COFINS na tabela de impostos;

![Imagem 9: Estando com algum desses CST's, deve-se obrigatoriamente ter valor de PIS/COFINS: 50, 51, 52, 53, 54, 55, 56, 60, 61,…](https://ajuda.sankhya.com.br/hc/article_attachments/26350240551447) Estando com algum desses CST's, deve-se obrigatoriamente ter valor de PIS/COFINS: 50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66 **ou** se for lançado com algum dos CST's a seguir, o parâmetro **"CSTSEMCREDEFDCT"** tem que estar ativado: 70, 71, 72, 73, 74, 75;

#### **(1)** Validações para cenário para "Devolução de venda":

![Imagem 10: Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como Estoque;](https://ajuda.sankhya.com.br/hc/article_attachments/26350256473239) Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como **Estoque;**

![Imagem 11: Na tela Cadastro Livro ICMS/IPI o Campo entrada/saída deve estar como Entrada;](https://ajuda.sankhya.com.br/hc/article_attachments/26350240540311) Na tela Cadastro Livro ICMS/IPI o Campo entrada/saída deve estar como **Entrada;**

![Imagem 12: Tipo de movimento da top deve ser obrigatoriamente "devolução de venda";](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) Tipo de movimento da top deve ser obrigatoriamente **"devolução de venda";**

![Imagem 13: Na tela Cadastro Livro ICMS/IPI o Campo CFOP deve estar com algumas das seguintes opções: 1201, 1202, 1203, 1204, 1410,…](https://ajuda.sankhya.com.br/hc/article_attachments/26350240549271) Na tela Cadastro Livro ICMS/IPI o Campo **CFOP** deve estar com algumas das seguintes opções: 1201, 1202, 1203, 1204, 1410, 1411, 1660, 1661, 1662, 2201, 2202, 2203, 2204, 2410, 2411, 2660, 2661, 2662, 3201, 3202, 3211, 3503, 3553 **ou** o campo **NF-e** da TOP deve estar como **"Terceiro"** e nos livros fiscais devem estar com os seguintes CFOP's: 1206, 2206.

![Imagem 14: No documento deve-se ter obrigatoriamente as linhas de PIS/COFINS na tabela de impostos e nas linhas devem ter valores…](https://ajuda.sankhya.com.br/hc/article_attachments/26350240551447) No documento deve-se ter **obrigatoriamente** as linhas de PIS/COFINS na tabela de impostos e nas linhas devem ter valores dos impostos.

Porém, a ativação do parâmetro **"OENSEMCREDEFDCT"** implica em outro comportamento: dispensa a regra de haver valores de PIS/COFINS na nota, na qual se a TOP estiver com o campo **"Considerar NFe relacionada como cancelada no EFD Contribuições"** ativado (juntamente com o parâmetro) fica desobrigado esses valores de impostos. Entretanto, há uma dupla mudança de comportamento com a ativação do parâmetro, que citaremos abaixo;

![Imagem 15: Quando nas preferências da empresa (Caminho: Comercial » Preferências » Empresa) , na aba "Regime de Apuração da…](https://ajuda.sankhya.com.br/hc/article_attachments/26355315442583) Quando nas preferências da empresa (Caminho: Comercial » Preferências » Empresa), na aba **"Regime de Apuração da Contrib. Social e Aprop. Crédito"** o campo **"Incidência tributária:"** estiver com uma das seguintes opções:

**(2)** Incidência exclusivamente no regime não-cumulativo

**(2)**Incidência nos regimes não-cumulativo e cumulativo

Deve-se ter no documento as seguintes CST's:  50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 66.

**Observação:** se há necessidade de gerar o documento com CST's: 70, 71, 72, 73, 74, 75... se faz necessário ativar o parâmetro **"CSTSEMCREDEFDCT"**

Porém, se campo "Incidência tributária:" estiver com uma das seguintes opções:

**(2)**Incidência exclusivamente no regime cumulativo

**(2)**Incidência nos regimes não-cumulativo e cumulativo

O documento deve estar com uma das seguintes CST's: 98 e 99.

**Observação:** se houver a necessidade de gerar **dev. de vendas** com o campo **"Incidência tributária:"** estando igual a **"Incidência exclusivamente no regime não-cumulativo"** e a nota estando com **CST's: 98 e 99,** se faz necessário ativar o parâmetro OENSEMCREDEFDCT**.**

#### **(1)** Validações para cenário para "Venda":

As validações para as TOP's que estiverem com o tipo de movimento igual a "venda" são poucas, sendo apenas:

![Imagem 16: Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como Estoque;](https://ajuda.sankhya.com.br/hc/article_attachments/26350256473239) Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como **Estoque;**

![Imagem 17: Na tela Cadastro Livro ICMS/IPI o Campo entrada/saída deve estar como Saída;](https://ajuda.sankhya.com.br/hc/article_attachments/26350240540311) Na tela Cadastro Livro ICMS/IPI o Campo entrada/saída deve estar como **Saída;**

![Imagem 18: No documento, deve-se ter obrigatoriamente as linhas de PIS/COFINS na tabela de impostos;](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) No documento, deve-se ter obrigatoriamente as linhas de PIS/COFINS na tabela de impostos;

![Imagem 19: Algum item da nota tem que estar com CST diferente de 49, OU , se for CST 49, no livro fiscal o CFOP deve ser 5927 ;](https://ajuda.sankhya.com.br/hc/article_attachments/26350240549271) Algum item da nota tem que estar com CST diferente de 49, **OU,** se for CST 49, no livro fiscal o CFOP deve ser **5927**;

#### Validações para cenário para "Devolução de Compra":

![Imagem 20: Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como Estoque;](https://ajuda.sankhya.com.br/hc/article_attachments/26350256473239) Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como **Estoque;**

![Imagem 21: Na tela Cadastro Livro ICMS/IPI o Campo entrada/saída deve estar como Saída;](https://ajuda.sankhya.com.br/hc/article_attachments/26350240540311) Na tela Cadastro Livro ICMS/IPI o Campo entrada/saída deve estar como **Saída;**

![Imagem 22: Tipo de movimento da top deve ser obrigatoriamente "devolução de compra";](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) Tipo de movimento da top deve ser obrigatoriamente **"devolução de compra";**

![Imagem 23: Nos livros fiscais, os itens da nota devem estar com uma das seguintes opções CFOP's: 5124, 5201, 5202, 5205, 5206,…](https://ajuda.sankhya.com.br/hc/article_attachments/26350240549271) Nos livros fiscais, os itens da nota devem estar com uma das seguintes opções **CFOP's:** 5124, 5201, 5202, 5205, 5206, 5207, 5210, 5410, 5411, 5413, 5556, 5660, 5661, 5662, 6124, 6201, 6202, 6205, 6206, 6207, 6210, 6410, 6411, 6413, 6556, 6660, 6661, 6662, 7201, 7202, 7205, 7206, 7207, 7210, 7211.

![Imagem 24: No documento, deve ter obrigatoriamente as linhas de PIS/COFINS na tabela de impostos;](https://ajuda.sankhya.com.br/hc/article_attachments/26350240551447) No documento, deve ter obrigatoriamente as linhas de PIS/COFINS na tabela de impostos;

![Imagem 25: Deve ser lançada com a CST igual a 49;](https://ajuda.sankhya.com.br/hc/article_attachments/26355315442583) Deve ser lançada com a **CST** igual a 49;

#### Validações para cenário para "Nota de Complemento":

![Imagem 26: Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como Complemento;](https://ajuda.sankhya.com.br/hc/article_attachments/26350256473239) Na tela Cadastro Livro ICMS/IPI o Campo origem deve estar como **Complemento;**

![Imagem 27: No documento, deve-se ter obrigatoriamente as linhas de PIS/COFINS na tabela de impostos;](https://ajuda.sankhya.com.br/hc/article_attachments/26350240540311) No documento, deve-se ter obrigatoriamente as linhas de PIS/COFINS na tabela de impostos;

![Imagem 28: Deve ser lançada com a CST diferente de 49;](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE)  Deve ser lançada com a CST diferente de **49;**

![Imagem 29: Na tela Cadastro Livro ICMS/IPI o Campo "entrada/saída" deve estar como Saída ou, no documento, além de ter as linhas…](https://ajuda.sankhya.com.br/hc/article_attachments/26350240549271) Na tela Cadastro Livro ICMS/IPI o Campo "entrada/saída" deve estar como **Saída ou,** no documento, além de ter as linhas de PIS/COFINS, deve haver valor maior que **zero,** tanto o valor normal quanto o campo de valor de crédito da tela de impostos do item da nota.

**Observação:** se há necessidade de gerar o documento com CST's: 70, 71, 72, 73, 74, 75 ative o parâmetro **CSTSEMCREDEFDCT.**

#### Validações para cenário para "Notas canceladas":

Validação que apenas esteja nos livros com o campo origem igual a cancelada;

#### Validações para cenário para "Nota de compra de energia elétrica":

Caso exista a necessidade de se gerar a nota de compra de elétrica, no registro **C500** e não no **C100**, temos o parâmetro **GERNFENERC500**, que deve estar ativado. Assim, **não** será gerada no C100 se a nota de compra estiver com o produto lançado e este produto tiver em seu cadastro o campo "**Usado Como**" igual a "**Consumo**" e algum dos CFOP's a seguir, : 1251, 1252, 1253, 1254, 1255, 1256, 1257, 2251, 2252, 2253, 2254, 2255, 2256, 2257.
