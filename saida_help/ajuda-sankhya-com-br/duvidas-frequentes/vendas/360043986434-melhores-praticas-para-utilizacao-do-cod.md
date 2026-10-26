---
id: "360043986434"
titulo: "Melhores práticas para utilização do 'Código Benefício' por Produto/Empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043986434-Melhores-pr%C3%A1ticas-para-utiliza%C3%A7%C3%A3o-do-C%C3%B3digo-Benef%C3%ADcio-por-Produto-Empresa"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-08-31T16:39:55Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Automatizar cBenef no XML", "Configurar Finalidade e Benefícios", "Parâmetro UFPER8CTAGCBENE"]
---

# Melhores práticas para utilização do 'Código Benefício' por Produto/Empresa

**(1)** Com a entrada em vigor das regras de validação da Nota Técnica 2019.001 (Versão 1.10 – Julho de 2019), se fez necessário automatizar o preenchimento do 'Código de Benefício Fiscal' (tag cBenef) do grupo de 'Detalhamento de Produtos e Serviços'. 

**(1)** Como ocorrem operações com o mesmo produto envolvendo diferentes estados, foram criadas as telas **"Finalidade de Operação"** e **"Cadastro de Benefícios"**, que atendem a configuração "**Impostos / Informações por Empresa"**, para que ao efetuar a operação, o sistema leve o Código do Benefício e, consequentemente, preencha a tag cBenef no xml da NFe, para o respectivo estado da empresa.

**(1)** [Nota Técnica 2019.001](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=%20%20https://www.sef.sc.gov.br/arquivos_portal/servicos/128/Correio_Eletronico_2022_23__DIAT__Preenchimento_do_campo__cBenef__na_emissao_da_Nota_Fiscal_eletronica__NF_e__e_Nota_Fiscal_de_Consumidor_eletronica__NFC_e.pdf) do portal da Fazenda.

**![Imagem 1: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16833792557335) IMPORTANTE:**

Nada impede que a funcionalidade seja utilizada por outros estados, desde que sejam respeitadas as tabelas de códigos instituídas por cada estado. Hoje o sistema deixa o campo aberto e o usuário faz o cadastro que necessitar.

**![Imagem 2: Vejamos as configurações:](https://ajuda.sankhya.com.br/hc/article_attachments/16833792559895) Vejamos as configurações:**

![Imagem 3: Finalidade de Operação](https://ajuda.sankhya.com.br/hc/article_attachments/16833792563863) **Finalidade de Operação**

 Na tela Finalidade de Operação cadastre uma respectiva finalidade:

![Imagem 4: Na tela Finalidade de Operação cadastre uma respectiva finalidade:](https://ajuda.sankhya.com.br/hc/article_attachments/14658913659927)

**Veja mais detalhes em:**

-  [Finalidade da Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599434).
 - [Finalidade da Operação - Onde informar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596074)

**![Imagem 5: Cadastro de Benefícios](https://ajuda.sankhya.com.br/hc/article_attachments/16833792568343)  Cadastro de Benefícios**

É cadastrado o Código de Benefício vinculando a Empresa e a Finalidade da Operação que deseja-se buscar.

![Imagem 6: É cadastrado o Código de Benefício vinculando a Empresa e a Finalidade da Operação que deseja-se buscar.](https://ajuda.sankhya.com.br/hc/article_attachments/14658948308119)

Para mais detalhes, consulte o artigo:**[Cadastro Benefícios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596014).**

**![Imagem 7: Cadastro do Produto](https://ajuda.sankhya.com.br/hc/article_attachments/16833765265815) Cadastro do Produto**

Na aba Impostos / Informações por empresa será inserida a empresa já relacionada anteriormente na tela Cadastro de Benefícios.

![Imagem 8: Na aba Impostos / Informações por empresa será inserida a empresa já relacionada anteriormente na tela Cadastro de…](https://ajuda.sankhya.com.br/hc/article_attachments/14658985556887)

**![Imagem 9: Cadastro do Parceiro:](https://ajuda.sankhya.com.br/hc/article_attachments/16833792576151)  Cadastro do Parceiro:**

Na aba **"Fiscal"**, campo **"Finalidade da Operação",** poderá ser vinculada tal finalidade, criada na tela de mesmo nome.

![Imagem 10: Na aba "Fiscal" , campo "Finalidade da Operação", poderá ser vinculada tal finalidade, criada na tela de mesmo nome.](https://ajuda.sankhya.com.br/hc/article_attachments/14658991310615)

Porém, caso não haja tal informação, o sistema buscará no cadastro da TOP: 

![Imagem 11: Porém, caso não haja tal informação, o sistema buscará no cadastro da TOP:](https://ajuda.sankhya.com.br/hc/article_attachments/14659085024023)

**![Imagem 12: Tela Empresa ( Comercial » Preferências), filtrar a respectiva empresa) :](https://ajuda.sankhya.com.br/hc/article_attachments/16833765276567) Tela Empresa** (Comercial » Preferências), filtrar a respectiva empresa):

- Aba **"NF-e/NFC-e"**
- **Considerar Benefícios ao incluir/alterar item da nota:** marque

![Imagem 13: Considerar Benefícios ao incluir/alterar item da nota: marque](https://ajuda.sankhya.com.br/hc/article_attachments/14659142812823)

**![Imagem 14: Lançamento da nota:](https://ajuda.sankhya.com.br/hc/article_attachments/16833765281047) Lançamento da nota:**

Realizando o lançamento conforme os cadastros acima, o sistema preenche corretamente o campo "**Cód. de Benefício Fiscal na UF"**:

![Imagem 15: Realizando o lançamento conforme os cadastros acima, o sistema preenche corretamente o campo " Cód. de Benefício Fiscal…](https://ajuda.sankhya.com.br/hc/article_attachments/14659273521687)

**![Imagem 16: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16833792557335) IMPORTANTE:**

A Finalidade de Operação não é um campo a ser levado no XML, deste modo, ele não é preenchido automaticamente. Todas as configurações acima realizadas só fazem o preenchimento do Cód. de Benefício Fiscal na UF. Feito o lançamento, levaremos ao XML.

![Imagem 17: Parâmetro UFPER8CTAGCBENE](https://ajuda.sankhya.com.br/hc/article_attachments/17968947065239) Parâmetro **UFPER8CTAGCBENE**

Para geração da tag <cBenef> são permitidos 10 caracteres conforme a NT 2016.002, porém há casos em que a UF do Emitente permite apenas 8. Sendo assim, a UF do Emitente que permite apenas 8 caracteres deve estar informada no parâmetro '**UFPER8CTAGCBENE** **- 'UFs permitem o envio de 8 caracteres na tag cBenef'**.

- Tela 'Preferências' (Configurações » Avançado » Preferências)
- Chave: **UFPER8CTAGCBENE**

![Imagem 18: Chave: UFPER8CTAGCBENE](https://ajuda.sankhya.com.br/hc/article_attachments/17968908889239)

**![Imagem 19: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16833765283095) OBSERVAÇÕES:**

Caso utilize o faturamento de notas a partir de um pedido, habilite o parâmetro **"ATUALFINFAT"**, para que no faturamento o sistema leve em consideração a Finalidade da Operação informada na nota.
