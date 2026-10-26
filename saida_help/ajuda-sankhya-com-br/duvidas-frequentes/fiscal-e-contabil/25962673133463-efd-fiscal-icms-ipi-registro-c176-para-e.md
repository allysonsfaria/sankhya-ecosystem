---
id: "25962673133463"
titulo: "EFD FISCAL - ICMS/IPI - Registro C176 para empresas de Minas Gerais - MG"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25962673133463-EFD-FISCAL-ICMS-IPI-Registro-C176-para-empresas-de-Minas-Gerais-MG"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:43:39Z"
rotulos: ["Configuração", "IPI", "ICMS", "EFD", "Minas Gerais", "EFD FISCAL - ICMS/IP", "empresas de Minas Gerais - MG", "Registro C176", "Documentos Eletrônicos"]
---

# EFD FISCAL - ICMS/IPI - Registro C176 para empresas de Minas Gerais - MG

Hoje a nossa aplicação tem a geração do registro C176 SPED ICMS/IPI de forma automática apenas para as empresas que estiverem gerando o TXT de Minas Gerais. Confira abaixo as regras dessa geração:

O sistema valida se a UF presente no registro 0000 é MG, se for positivo essa avaliação, o sistema validará as seguintes informações e, se alguma delas for verdadeira, o sistema não criará o registro:

**(1)** Se o CFOP do item em questão for menor que 6000, **Ou**

**(1)** Se a nota não for dos modelos: 1,55 e 65, **Ou**

**(1)** Se nas Preferências da empresa (Caminho: Comercial » Preferências » Empresa), na aba **"EFD - Escrituração Fiscal Digital"**, na sub-aba  **"Blocos e Registros"**, o registro C176 não estiver criado e também não estiver marcado para gerar, **Ou**

**(1)** Se no registro C100 do documento em questão, o campo 03 - IND\_EMIT, for igual a **"0 - Emissão própria"** e o modelo do documento for 65, **Ou**

**(1)** Se o valor de ICMS **não** for maior que zero, no item em questão do documento, **Ou**

**(1)** Se o tipo de substituição cadastrada no Produto, tanto na aba **"Impostos"**, quanto na aba **"Impostos por empresa"**, **não** for uma das seguintes opções: Subst. na compra e na venda OU Revenda com subst. tributária (cálculo de Subst. na compra)

#### Consulta de busca dos documentos que serão gerados no C176

Feitas as validações acima, o sistema executará uma consulta nos lançamentos/documentos das telas livros fiscais **"Cadastro Livro ICMS/IPI"** com ligação nas centrais de notas, buscando documentos, a fim de vincula-los ao C170 através do C176, com as seguintes regras:

**(1)** Documentos que estejam nos livros da empresa geradora do TXT;

**(1)** Para o produto em questão do documento C100;

**(1)** Com **"Dt. do documento"**, nos livros fiscais, menor que a data do documento do C100 em questão, conforme print abaixo;

![Imagem 1: (1) Com "Dt. do documento" , nos livros fiscais, menor que a data do documento do C100 em questão, conforme print…](https://ajuda.sankhya.com.br/hc/article_attachments/25973579805463)

Documento este, que nos livros esteja como "entrada", conforme print abaixo;

![Imagem 2: Documento este, que nos livros esteja como "entrada", conforme print abaixo;](https://ajuda.sankhya.com.br/hc/article_attachments/25973579813271)

Nos livros, este documento deve estar com o campo **"Destino"** como **"parceiro"**, conforme print

![Imagem 3: Nos livros, este documento deve estar com o campo "Destino" como "parceiro" , conforme print](https://ajuda.sankhya.com.br/hc/article_attachments/25973584773655)

Sua origem nos livros deve ser: estoque ou Complemento;

![Imagem 4: Sua origem nos livros deve ser: estoque ou Complemento;](https://ajuda.sankhya.com.br/hc/article_attachments/25973579821079)

**(1)** Ainda nos livros, tal documento não pode estar com um desses CFOP's: 5929,6929,1409,1915,1916,1925,1949,2409,2915,2916,2925,2949

**(1)** Na central de notas, este documento deve ter sido lançado com uma TOP que atualiza estoque;

**(1)** Na central de notas a quantidade negociada do produto deve ser diferente de zero;

**(1)** Não pode ser um documento, cujo tipo de movimento da TOP, seja 'devolução de venda';

Nesta consulta, podem haver mais de um retorno. Para resolver esse problema, o sistema ordena pelo campo Dt. do movimento do maior para o menor, assim a nota com a maior data (lembrando que essa data tem que ser menor do que a nota que está sendo gerada no C100/C170) será a considerada para ser gerada no C176.

**Observação:** para os demais estados informe as Notas de compras para Ressarcimento de ICMS-ST no caminho: Livros Fiscais » Arquivos » Cadastro Livro ICMS/IPI', aba: **"Notas p/ Ressarcimento de ST"** de forma manual, ou por meio de uma personalização que automatize essa geração.
