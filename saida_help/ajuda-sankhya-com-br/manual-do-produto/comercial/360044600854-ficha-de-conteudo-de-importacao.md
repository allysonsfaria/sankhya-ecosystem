---
id: "360044600854"
titulo: "Ficha de Conteúdo de Importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600854-Ficha-de-Conte%C3%BAdo-de-Importa%C3%A7%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:23:05Z"
rotulos: ["manual", "Configuração", "NF-e", "PARCIMPFICI", "Ficha de Conteúdo de Importação", "nFCI", "br.com.sankhya.rotinas.fichadeconteudodeimportacao", "Ficha de Conteúdo de Importação manual", "XML", "Importação", "Impostos", "Importação ICMS Processo", "FCI"]
---

# Ficha de Conteúdo de Importação

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311810579351) Módulo: Comercial > Rotinas
```

---

![Imagem 2: Para que esta tela seja exibida, é necessário que o parâmetro "Parcela Importada Mínima para FCI - PARCIMPFICI" possua…](https://ajuda.sankhya.com.br/hc/article_attachments/16271914157463) Para que esta tela seja exibida, é necessário que o parâmetro **"Parcela Importada Mínima para FCI - PARCIMPFICI"** possua um valor igual ou maior do que 1 informado.

A funcionalidade foi desenvolvida visando a obtenção do número da Ficha de Conteúdo de Importação - FCI, conforme determinação do Manual do Sistema FCI, não contemplando nenhuma ferramenta de cálculo e apuração para determinar a participação da parcela importada no total do bem ou mercadoria.

A Ficha de Conteúdo de Importação - FCI contém informações que determinam a participação da parcela importada no total do bem ou mercadoria (Conteúdo de Importação), além de identificar o contribuinte e a mercadoria.

## Detalhes do processo

A alíquota do ICMS de 4% (quatro por cento) aplica-se nas operações interestaduais com bens e mercadorias importados do exterior que, após o desembaraço aduaneiro:

I. não tenham sido submetidos a processo de industrialização;

II. ainda que submetidos a processo de transformação, beneficiamento, montagem, acondicionamento, recondicionamento renovação ou recondicionamento, resultem em mercadorias ou bens com Conteúdo de Importação superior a 40% (quarenta por cento).

Os contribuintes deverão prestar informações sobre o Conteúdo de Importação de seus produtos por meio de arquivo digital a ser encaminhado à Administração Tributária.

A rotina que será desenvolvida irá gerar o arquivo a ser encaminhado por meio do programa validador e processará o arquivo de retorno disponibilizado pelo site. Para orientações sobre o validador, envio e recebimento acesse o site <https://portal.fazenda.sp.gov.br/servicos/fci/Paginas/Sobre.aspx>.

## Configurações envolvidas

- Parâmetro PARCIMPFICI;
- Tela Cadastro de produtos;
- Tela Ficha de Conteúdo de Importação;
- Geração do XML da NFe com a TAG nFCI.

## Sequencia do processo

No parâmetro Parcela Importada Mínima para FCI - PARCIMPFICI, deve ser informado um número que corresponde ao percentual mínimo de conteúdo de importação que um produto deve possuir para ser gerado na Ficha de Conteúdo de Importação.

![Imagem 3: No parâmetro Parcela Importada Mínima para FCI - PARCIMPFICI , deve ser informado um número que corresponde ao…](https://ajuda.sankhya.com.br/hc/article_attachments/4408426558103)

Quando o parâmetro for maior que zero, os campos referentes ao parâmetro estarão habilitados no [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos) agrupados na seção **"FIC – Ficha de Conteúdo de Importação"**, são eles:

O campo **"Valor de Comercialização – (R$)"** refere-se ao valor total da operação de saída interestadual;

Preencha no campo **"Valor da Parcela Importada do Exterior – (R$)"** o valor do produto informado no documento fiscal emitido pelo remetente;

O **"Código da FCI"** é gerado para produtos com parcela importada do exterior no site:  <https://portal.fazenda.sp.gov.br/servicos/fci/Paginas/Sobre.aspx>. Estes códigos estarão no arquivo de retorno gerado por este site. Esse campo será habilitado se o campo **"Origem do Produto"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral) estiver configurado com 3, 5 ou 8.

De acordo com o preenchimento do valor de comercialização e do valor da parcela importado do exterior, o sistema calcula o quociente entre o valor da parcela de importação e o valor total da operação de saída (valor de comercialização) multiplicado por 100, ou seja, (Valor da Parcela Importada do Exterior/Valor de Comercialização)\*100.

Se o resultado for menor que do valor da parcela de importação mínima definido no parâmetro PARCIMPFICI, o sistema emite a mensagem abaixo:

**"Para informar o Vlr. da parcela de importação o Vlr. comercialização deve ser informado".**

Se o resultado for menor que o percentual definido no parâmetro, o sistema apresenta a mensagem:

**"Parcela Importada deverá ser maior ou igual a PARCEIMPFCI % "**

Se a **"Origem do Produto"** estiver configurada com 3, 5 ou 8 e o campo **"Código da FCI"**estiver vazio o sistema irá mostrar a mensagem abaixo, mas permitirá salvar as alterações no produto.

**"Atenção! Código da FCI inexistente. Providenciar obtenção".**

Na tela Ficha de Conteúdo de Importação existe a opção para gerar o arquivo para enviar para geração do **"Código da FCI"** e opção para processar o arquivo com o Código da FCI gerado.

Na aba **"Geração do arquivo FCI"** filtram-se todos os produtos, o sistema mostra os produtos cujo **"Origem do Produto"** é 3, 5 ou 8, que tenham **"Valor de Comercialização – (R$)"** e **"Valor da Parcela Importada do Exterior – (R$)"** e que o Código da FCI esteja vazio.

![Imagem 4: Na aba "Geração do arquivo FCI" filtra m-se todos os produtos, o sistema mostr a os produtos cujo "Origem do Produto" é…](https://ajuda.sankhya.com.br/hc/article_attachments/4408436923671)

Nesta mesma tela temos opção de filtrar também os arquivos cujo Código da FCI estejam pendentes, neste caso basta marcar a opção **"Gerar novamente Produtos com Código da FCI pendente"**.

Ao posicionar o mouse sobre o botão ![Imagem 5: Ao posicionar o mouse sobre o botão "Ajuda" , o sistema mostra a seguinte mensagem:](https://ajuda.sankhya.com.br/hc/article_attachments/16271932720023) **"Ajuda"**, o sistema mostra a seguinte mensagem:

**"Ao selecionar a opção 'Sem filtro', será filtrado produtos cujo código FCI é nulo, a origem do produto igual 3, 5 ou 8, e o valor da parcela importada maior que zero. Se a opção 'Gerar novamente produtos com código FCI pendente' estiver marcada será filtrado também produtos cujo código FCI é pendente".**

Ao clicar no botão **"Gerar arquivo"**, o sistema verifica se alguns campos visíveis na grade são preenchidos corretamente, exceto o campo **"Referência"**, pois este é opcional, antes da geração do arquivo. O arquivo gerado possui a nomenclatura a seguir: CNPJ\_AAAAMMDD\_hhmmss.txt. e conterá produtos filtrados na tela e as informações da empresa conforme o layout. Após a geração do arquivo digital, o sistema atualiza o Código FCI de produtos no banco como **"PENDENTE"**, aguardando então a geração dos códigos FCI pela unidade federal responsável no site.

Após processar o arquivo onde será gerado o Código da FCI, com a **"Empresa"** informada, na aba **"Processamento do arquivo FCI"**, clique no botão **"Selecionar arquivo"**, dessa forma será apresentado um pop-up para que você selecione o arquivo desejado. Feito isso, clique em **"Enviar"**.

![Imagem 6: Após processar o arquivo onde será gerado o Código da FCI , com a "Empresa" informada, na aba "Processamento do arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/4408437935639)

Ainda na aba mencionada, ao clicar no botão **"Processar arquivo"** o sistema irá processar o arquivo e mostrará mensagem de confirmação do processo. Além disso, será verificado se o arquivo é de retorno conforme o layout e realiza algumas validações como se as informações da empresa encontradas no arquivo de retorno são iguais da empresa filtrada na tela. Se acontecer, o sistema busca pelos códigos FCI de produtos e os atualiza o cadastro de produtos.

Para que seja gerada a tag <**nFCI**> o campo **"Código da FCI"** (tela [Cadastro de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos)) deve estar preenchido, bem como o campo **"Origem do Produto"** na grade de **"Itens"** da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) deve estar informado com uma das seguintes opções:

- 3-Nacional, mercadoria ou bem com conteúdo de importação superior a 40% e inferior ou igual a 70%;
- 5-Nacional, mercadoria ou bem com conteúdo de importação inferior ou igual a 40%;
- 8-Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%.

Caso as condições mencionadas acima não sejam atendidas, a tag <**nFCI**> não será gerada dentro do agrupamento da tag <**prod**>.

Observe um exemplo de sua geração:

![Imagem 7: Observe um exemplo de sua geração:](https://ajuda.sankhya.com.br/hc/article_attachments/360061919553)

![Imagem 8: A Ficha de Conteúdo de Importação irá gerar as informações pertinentes ao campo Unidade do Registro 5020 , desde que o…](https://ajuda.sankhya.com.br/hc/article_attachments/16271947893143) A Ficha de Conteúdo de Importação irá gerar as informações pertinentes ao campo Unidade do Registro 5020, desde que o campo **"Unidade para FCI"** presente no [Cadastro de Unidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597094), esteja preenchido. Caso o campo esteja em branco, o Registro será preenchido com a informação 99.

Os arquivos TXT criados na geração e processamento dos produtos para geração do Código da FCI tem a estrutura demonstrada e organizadas em 3 blocos.

0000 |CNPJ|NomeContribuinte | versaoLayout.

0001 |Texto\_padrao\_UTF8

0010 |CNPJ|RazaoSocial|Ins\_Estadual|End\_Estab|CEP |Municipio|UF  

0990 |Qtdade\_Linhas

5001

5020|NomeMerc|CodNCM| CodMerc| CodGTIN|Unid|VlrComerc|VlrParc|Cont\_Import  

5990|Qtdade\_Linhas

9001|

9900|Tipo\_registro|Qdade\_linhas\_campo\_ant

9990|Qtdade\_linhas

9999|Qtade\_Tot\_linhas\_arqv

Bloco 0

0000 |CNPJ|NomeContribuinte | versaoLayout.

0001 |Texto\_padrao\_UTF8

0010 |CNPJ|RazaoSocial|Ins\_Estadual|End\_Estab|CEP |Municipio|UF  

0990 |Qtdade\_Linhas

Onde,

Registro 0000: abertura do arquivo digital;

CNPJ: é CNPJ do contribuinte (empresa);

NomeContribuinte: é o nome do contribuinte;

versaoLayout: é a versão do layout por default 1.0

Registro 0001: abertura do bloco 0;

Texto\_padrao\_UTF8

Registro 0010: Dados cadastrais do contribuinte;

CNPJ: é CNPJ do contribuinte;

RazaoSocial: é a razão social do contribuinte;

Ins\_Estadual: a inscrição estadual do contribuinte

End\_Estab: Endereço do estabelecimento do contribuinte

CEP: é o Cep do contribuinte

Municipio: Município do contribuinte

UF: UF do contribuinte.

Registro 0990: é um identificador o tipo de registro 0990;

Qtdade\_Linhas: determina a quantidade de linhas do bloco 0;

Bloco 5

5001

5020|NomeMerc|CodNCM| CodMerc| CodGTIN|Unid|VlrComerc|VlrParc|Cont\_Import  

5990|Qtdade\_Linhas

Onde,

Registro 5001: abertura do bloco 5;

Registro 5020: detalhamento das mercadorias(produtos);

NomeMerc: é a descrição do produto;

CodNCM: é código NCM(Nomenclatura do MercoSul);

CodMerc: é o código do produto

CodGTIN: é o código referência do produto

Unid: é a unidade do produto.

VlrComerc: é o valor da comercialização do produto

VlrParc: Valor da parcela importada do exterior do produto

Cont\_Import: é o percentual do conteúdo de importação

Registro 5990: encerramento do bloco 5;

Qtdade\_Linhas: determina a quantidade de linhas do bloco 5;

Bloco 9

9001|

9900|Tipo\_registro|Qdade\_linhas\_campo\_ant

9990|Qtdade\_linhas

9999|Qtade\_Tot\_linhas\_arqv

Registro 9001: abertura do bloco 9;

Registro 9900: totalizadores de registros anteriores

Tipo\_registro: determina o tipo do registro (0000,0010,5020);

Qdade\_linhas\_campo\_ant: determina a quantidade de linhas conforme o campo anterior (Tipo\_registro)

Registro 9990: encerramento do bloco 9

Qtdade\_linhas: é quantidade total de linhas do bloco 9

Registro 9999: encerramento do arquivo;

Qtade\_Tot\_linhas\_arqv: é a quantidade total de linhas do arquivo;

O arquivo de retorno processado no site da administração tributária traz alguns campos adicionais nos registros 0000 e 5020. Estes registros ficaram assim (campos adicionais destacados na cor **verde**):

0000 |CNPJ|NomeContribuinte|versaoLayout|Hash|Dt\_Recep|Cod\_recep|Dt\_valid|Ind\_valid

||

Onde,

Hash: é o Hash do arquivo

Dt\_Recep: A data em que o arquivo foi recebido;

Cod\_recep: O código de recepção do arquivo

Dt\_valid:A data em que o arquivo foi validado

In\_valid: O indicador de validação do arquivo.

5020|NomeMerc|CodNCM|CodMerc| CodGTIN|Unid|VlrComerc|VlrParc|Cont\_Import|CodFCI|In\_valid  

Onde,

CodFCI: O código de ficha do conteúdo de importação

In\_valid: Indicador de validação da ficha

Foram tratadas algumas validações importantes no processamento do arquivo de retorno:

1- Se o CNPJ no arquivo for diferente do CNPJ filtrado na tela, o sistema emite a mensagem:

**"CNPJ do contribuinte diferente do arquivo de retorno";**

2- Se o número de colunas do registro 0000 for menor que 4, o sistema apresenta a mensagem:

**"Arquivo selecionado não é um arquivo de retorno";**

3- Se o número de colunas do registro 5020 for menor que 11, o sistema exibe a mensagem:

**"Registro 5020 deve conter 11 colunas conforme estrutura do layout 1.0".**

4- Se a coluna décima do registro 5020 for vazia, o sistema emite a mensagem:

**"O registro 5020 não foi validado"**.

5- Se a coluna nona do registro 5020 for vazia, o sistema apresenta a mensagem: 

**"O registro 5020 do arquivo não contem o código FCI válido".**
