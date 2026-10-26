---
id: "1500003168922"
titulo: "Geração do Arquivo ADRC-ST PR"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Obrigações de ST"
atualizado_em: "2026-09-15T17:21:00Z"
rotulos: ["Configuração", "Livros Fiscais", "Impostos", "br.com.sankhya.mgeliv.cad.adrcst", "Paraná", "Define regras e campos para o arquivo da ADRC-ST", "Configura dados da empresa e identificações analíticas", "Detalha cálculo e ajustes de ICMS-ST e FECOP", "Documentos Eletrônicos", "ICMS-ST"]
---

# Geração do Arquivo ADRC-ST PR

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312866046487) Módulo: Livros Fiscais > Arquivos
```

---

Por meio dessa tela, você realizará as configurações necessárias para a geração do arquivo da ADRC-ST do Estado do Paraná destinado à apuração, recuperação, ressarcimento e complementação do ICMS-ST e FECOP nas hipóteses previstas na legislação do Estado.

Sendo que, a ADRC-ST é uma obrigação aplicável somente aos produtos sujeitos à Substituição Tributária que possuem como objetivo, a aquisição para revenda.

Dessa forma, antes da geração do arquivo, é necessário que você se atente à algumas regras:

- As notas fiscais de vendas/devoluções que serão englobadas na geração do ADRC-ST, deverão estar todas com o status = **"Aprovada"**.
- O contribuinte substituído deve efetuar o levantamento dos estoques existentes no último dia do mês anterior ao mês de referência do arquivo, escriturando-o no Bloco H da EFD, sempre que houver a solicitação de recuperação, ressarcimento ou complementação do imposto.
- Ainda referente ao contribuinte substituído, sendo ele optante do regime do Simples Nacional que não utiliza a EFD, deve-se preencher o Registro 1010 - Identificação do Inventário do Produto do ADCR-ST, para cada item de mercadoria identificada no Registro 1000 do mesmo arquivo, a fim de discriminar os produtos sujeitos à Substituição Tributária existentes no estoque no último dia do mês anterior à referência do arquivo.
- Todo parceiro optante do Simples Nacional utilizado na geração do arquivo, deve estar com a marcação **"Optante pelo SIMPLES?"** ([Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913), aba [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas)) selecionada.
- Lembre-se também que, o Parceiro PF não será o contribuinte consumidor final.
- No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos)), habilite a marcação **"Considerar geração da ADRC-ST (PR)"** dos produtos que estarão sujeitos à entrega da ADRC-ST, bem como o preenchimento do campo **"MVA Original para ADRC-ST (PR)"** com o MVA do produto que vai ser utilizado nas operações de Substituição Tributária.

**Importante:** os dados inseridos nessa tela, devem ser conferidos e ajustados antes da geração do arquivo.

Assim, teremos as seguintes abas:

| [Aba Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#abaconfigura%C3%A7%C3%B5es) |  | [Aba 0000](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba0000) |
| --- | --- | --- |
| [Aba 1000](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1000) |  | [Aba 1999](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1999) |
| [Aba 9000](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba9000) |  | [Aba 9999](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba9999) |
| [Processamento e geração do arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#processamentoegera%C3%A7%C3%A3odoarquivo) |  |  |

                           

![Imagem 2: Processamento e geração do arquivo](https://ajuda.sankhya.com.br/hc/article_attachments/4419761831319)

## Aba Configurações

Nessa aba, você informará primeiramente a **"Empresa"** a ser gerada no Arquivo, junto à sua **"Referência"**.

Logo depois, no campo **"Qtd. de caracteres para CST\_CSOSN"**, determine a quantidade de caracteres referente ao CST e CSOSN, sendo que ele poderá possuir até três caracteres.

Ao realizar a marcação **"Considerar sequência quando não encontrar sequência fiscal"**, o sistema irá considerar a **"Sequência"** do item informado na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens) da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) quando o item não encontrar a sequência fiscal. Quando estiver desativada e o sistema não encontrar uma sequência fiscal, o valor da Sequência do item ficará negativo no campo **"N\_ITEM"** do XML.

Preencha o campo **"Desconsiderar Registro no Processamento"**, com o número do registro que a empresa tem a obrigação de gerar, como os Registros informados abaixo:

- Registros do Bloco 1010 aplicável somente às empresa optantes ao Simples Nacional, e que não realizam a entrega da EFD ICMS/IPI, portanto, não declaram o levantamento de estoque previsto no Bloco H da EFD;
- Registros do Bloco 1300 aplicável às saídas para outros estados;
- Os Registros do Bloco 1400 aplicáveis às saídas internas com produtos alimentícios, destinados à merenda escolar, órgãos da administração pública, cozinhas industriais, restaurantes, hotéis e similares, pizzarias e lanchonetes, nos termos do art. 119 no Anexo IX do RICMS/2017;
- Registros referentes ao Bloco 1500 aplicáveis às saídas internas destinadas a contribuinte do Simples Nacional de classificados nas Seções VI, VII, XVIII e XXII do Anexo IX do RICMS/17 com imposto retido calculado com a aplicação do percentual integral da MVA.

O campo **"NCM's dos produtos relacionados aos Registros 1410/1420"**, destina-se a informar o NCM das mercadorias que trata o art. 119, anexo IX do RICMS/17. Sendo que, esse campo deve ser preenchido com 8 caracteres.

Em **"NCM's dos produtos relacionados aos Registros 1510/1520"**, o NCM das mercadorias classificadas nas seções VI, VII, XVIII e XXII, do Anexo IX do RICMS/17 deve ser especificado. Sendo que, esse campo deve ser preenchido com 8 caracteres.

Através do campo **"Código da versão do leiaute do arquivo"** você poderá definir a versão do leiaute do arquivo que deseja gerar da ADRC-ST.

**Observação:** ao gerar o arquivo de um período de referência anterior à 2020, o Código de versão do leiaute do arquivo será **"110"**.

Quando a nota fiscal do CST for igual a 60, você poderá selecionar a marcação **"Considerar valores do ICMS ST Normal nos itens de entrada com CST 60?"**. Assim, quando esta for marcada, teremos algumas particularidades referentes às gerações dos registros [1100](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1100), [1300](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1300) e [1400](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1400). Observe:

Ao gerar o Registro 1100, o cálculo dos campos informados a seguir, ocorrerão da seguinte forma:

**Valor Unitário médio da Base de Cálculo do ICMS ST** = Somatório do campo Base de Cálculo do ICMS ST (R1110) / Quantidade do campo Quantidade total do item adquirido no período (R1100).

**Valor total do ICMS do item suportado na entrada** = Somatório dos campos Valor do ICMS Suportado na entrada (R1110).

**Valor unitário médio do ICMS suportado na entrada** = Valor total do ICMS do item suportado na entrada / Quantidade total do item adquirido no período.

Referente à geração do Registro 1300, teremos:

- Se o campo **"Código para reaver o imposto nas saídas interestaduais (R1300)"** da aba [0000](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba0000) estiver configurado com a opção **"Recuperação em conta gráfica"**, o valor deste será o mesmo do campo Valor de confronto do ICMS das entradas.
- Porém, caso o campo Código para reaver o imposto nas saídas interestaduais (R1300) estiver com a opção **"Ressarcimento para fornecedor"**, o sistema fará o seguinte cálculo:

**Código para reaver o imposto nas saídas interestaduais (R1300)** = Valor de confronto do ICMS das entradas - Valor total do ICMS efetivo nas saídas para outros estados

Considere ainda que, caso o resultado acima for negativo, o sistema o considerará como 0.

Na geração do Registro 1400, tem-se o seguinte comportamento:

- Se o campo **"Código para reaver o imposto nas saídas de que trata o art.119 do Anexo IX do RICMS/17 (R1400)"** estiver com a opção **"Recuperação em conta gráfica"** selecionada, o referido campo terá o mesmo valor do campo Valor de confronto do ICMS das entradas;
- No entanto, se a opção **"Ressarcimento para fornecedor"** do campo Código para reaver o imposto nas saídas de que trata o art.119 do Anexo IX do RICMS/17 (R1400) for configurada, o sistema realizará o seguinte cálculo:

**Código para reaver o imposto nas saídas de que trata o art.119 do Anexo IX do RICMS/17 (R1400)** = Valor de confronto do ICMS das entradas - Valor total do ICMS efetivo nas saídas para outros estados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#top)

## Aba 0000

Na aba 0000, os campos **"Código da versão do leiaute do arquivo"**, **"Mês e Ano de referência do arquivo"**, **"CNPJ do estabelecimento declarante"** e **"Inscrição Estadual do estabelecimento"** serão preenchidos automaticamente de acordo com as informações dos campos Empresa e Referência da aba Configurações.

![Imagem 3: Na aba 0000 , os campos "Código da versão do leiaute do arquivo" , "Mês e Ano de referência do arquivo" , "CNPJ do…](https://ajuda.sankhya.com.br/hc/article_attachments/360104220593)

O campo **"Código da finalidade do arquivo"**, determina se a geração dele é referente à um **"Arquivo original"** ou **"Arquivo substituto"** ao original.

Informe no campo **"Número do regime especial"**, se o declarante mantiver vigente o regime especial em relação à Substituição Tributária; caso ele não o possua, o campo deve permanecer em branco.

Os campos **"CNPJ do Centro de Distribuição"** e **"Inscrição Estadual do Centro Distribuição"**, devem ser preenchidos se os CFOP's 5151, 5152, 5408, 5409, 5658, 5659 forem informados no campo **"Código fiscal de operação e prestação"** do Registro 1110 que referencia notas fiscais de entrada.

**Observação:** caso haja uma operação de transferência entre filiais, e não existir Centro de Distribuição no PR, o próprio CNPJ do declarante deve inserido no campo CNPJ do Centro de Distribuição.

Os campos **"Código para reaver ou recolher o imposto nas saídas para consumidor final (R1200)"**, **"Código para reaver o imposto nas saídas interestaduais (R1300)"**, **"Código para reaver o imposto nas saídas de que trata o art. 119 do Anexo IX do RICMS/17 (R1400)"** e **"Código para reaver o imposto nas saídas destinadas ao Simples Nacional (R1500)"** indicarão o modo que a empresa adotará para recuperar ou ressarcir o ICMS, eles serão utilizados para geração do Registro 0000, e irão impactar diretamente no cálculo de ICMS a Recuperar/Ressarcir dos Registros 1300 e 1400.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#top)

## Aba 1000

Essa aba irá realizar a identificação analítica do produto. Sendo que, esse registro deve conter os códigos das mercadorias e suas respectivas descrições atribuídas pelo contribuinte para a identificação da mercadoria que integra o ciclo de aquisição e comercialização do estabelecimento. Assim, além dos campos disponíveis nessa aba, temos também algumas sub-abas:

| [Sub-aba 1010](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1010) |  | [Sub-Aba 1100](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1100) |  | [Sub-aba 1200](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1200) |
| --- | --- | --- | --- | --- |
| [Sub-aba 1400](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1400) |  | [Sub-aba 1300](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1300) |  | [Sub-aba 1500](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1500) |

                         

![Imagem 4: Sub-aba 1500](https://ajuda.sankhya.com.br/hc/article_attachments/360102165194)

Em **"Indicador de produto ao Fundo de Combate à Pobreza"**, você indicará se o produto cadastrado nessa aba será ou não sujeito ao FECOP, por meio das opções **"Produto está sujeito ao FECOP"** ou **"Produto não está sujeito ao FECOP"**.

Preencha no **"Código do item"** o código de identificação da mercadoria utilizado na aquisição e na comercialização do produto; sendo que, é a sequência de números e/ou letras atribuídas pelo contribuinte para a identificação da mercadoria que integra o ciclo de aquisição, produção e venda do estabelecimento. Ele também deve corresponder ao **"Cód. item"** declarado no [Registro 0200](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar0200) da EFD.

Não é possível reutilizar o Código do Item, e ele não poderá ser alterado, caso ocorra, o contribuinte deve informar o Registro 0205 da EFD, e no caso de um contribuinte não declarar a EFD, informe o Código do Item utilizado para identificar o produto nas suas operações.

O preenchimento do campo **"Código GTIN/EAN Tributável do produto"**, é referente ao código GTIN/EAN da menor unidade do produto.

Informe em **"Código conforme tabela ANP"**, o código do produto conforme a tabela da Agência Nacional de Petróleo - ANP.

O **"Código NCM"** da mercadoria a ser informado, deverá conter 8 dígitos.

Preencha no campo **"Código Especificador da Substituição Tributária"**, o código específico para cada item da mercadoria comercializada sujeita à Substituição Tributária.

O campo **"Informar a unidade de medida utilizada na quantificação do estoque"**, deve corresponder à unidade de medida utilizada na quantificação do estoque.

Digite no campo **"Alíquota do ICMS aplicável ao item nas operações internas"**, a alíquota da mercadoria prevista para as operações internas, incluindo o FECOP. Caso a mercadoria seja beneficiada com redução da base de cálculo, deve-se adotar a carga tributária efetiva.

A **"Alíquota de FECOP"** informa o percentual da alíquota do ICMS destinada ao FECOP. O valor que você inserir nesse campo deve ser igual a **"2"**, **"2,0"** ou **"2,00"**.

Em **"Quantidade total do item adquirido no período"**, informe o mesmo valor do campo **"Quantidade total do item adquirido no período"** do Registro 1100.

O campo **"Quantidade total de saídas do item no período"** é a somatória da quantidade de operações de saída do item declaradas nos campos **"Quantidade total de saídas para consumidor final"** (Registro 1200), **"Quantidade total de saídas para outros estados"** (Registro 1300), **"Quantidade total de saídas para outros estados"** (Registro 1400), **"Quantidade total de saídas destinadas a contribuintes do Simples Nacional"** (Registro 1500).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1000)

## Sub-aba 1010

Esse Registro deve ser preenchido pelos contribuintes enquadrados no regime do Simples Nacional no caso de pedido de ressarcimento, ou de complementação do imposto previsto no Registro 1200. Sendo assim, deverão identificar para cada item de mercadoria tratada no Registro 1000, o estoque existente no último dia do mês anterior ao do mês de referência.

![Imagem 5: Esse Registro deve ser preenchido pelos contribuintes enquadrados no regime do Simples Nacional no caso de pedido de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003341701)

No campo **"Quantidade do produto no estoque"**dessa aba, informe a quantidade do produto existente no estoque no último dia do mês anterior ao mês de referência do arquivo.

O **"Valor total do produto"** refere-se ao valor total do produto existente no estoque no último dia do mês anterior ao do mês da referência do arquivo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1000)

## Sub-aba 1100

![Imagem 6: Sub-aba 1100](https://ajuda.sankhya.com.br/hc/article_attachments/360104356213)

Você irá utilizar esta aba para identificar a totalização das notas fiscais de entrada declaradas no Registro 1110, deduzidas das devoluções ocorridas no próprio mês da aquisição do produto, sendo ele identificado no Registro 1000. Importante salientar que para cada mercadoria identificada no Registro 1000, um Registro 1010 deve ser preenchido, de forma que discrimine os produtos sujeitos à Substituição Tributária existentes no estoque do último dia do mês anterior ao de referência do arquivo. Assim, insira nesses campos os valores provenientes dos resultados dos seguintes cálculos:

**Quantidade total do item adquirido no período** = Somatória do campo Quantidade do item adquirido (Registro 1110) - Somatória do campo Quantidade do item devolvida (Registro 1120)

**Menor valor unitário do item adquirido no período** = Menor valor de aquisição dentre os produtos declarados no campo **"Valor unitário do item"** do Registro 1110.

**Valor unitário médio da base de cálculo do ICMS ST** = (Somatória do campo Base de cálculo do ICMS ST (Registro 1110)- Somatória do campo Base de cálculo do ICMS ST (Registro 1120)) / Quantidade total do item adquirido no período (Registro 1110)

**Nota:** em caso de algum campo ou registro não ser informado, considere como valor zero.

**Valor total do ICMS do item suportado na entrada** = Somatória do campo Valor do ICMS do item suportado na entrada (Registro 1110) - Somatória do campo Valor unitário do item (Registro 1120)

**Valor total do ICMS do item suportado na entrada** = Somatória do campo Base de cálculo do ICMS ST (Registro 1110) - Somatória campo Valor do ICMS do item suportado na entrada (Registro 1120)

**Observação:** em caso de algum campo ou registro não ser informado, considere como valor zero.

**Valor unitário médio do ICMS suportado na entrada** = Valor total do ICMS do item suportado na entrada (Registro 1100) / Quantidade total do item adquirido no período (Registro 1100)

**Sub-aba 1110**

O referido Registro, deve conter todas as notas fiscais modelo 55 de entrada da mercadoria declarada no Registro 1000 no período de referência. Se a quantidade declarada no mês de referência for insuficiente para acobertar o total das saídas declaradas nos Registros 1200, 1300, 1400 e 1500, o contribuinte deverá retroagir aos meses anteriores até obter a quantidade suficiente para acobertar a quantidade das saídas da mesma mercadoria.

Além disso, irão compor esse registro os CFOP's 1101, 1102, 1111, 1113, 1116, 1117, 1118, 1120, 1121, 1122, 1126, 1128, 1131, 1132, 1135, 1152, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1401, 1403, 1406, 1407, 1409, 1551, 1556, 1651, 1652, 1653, 1659, 1910, 2101, 2102, 2111, 2113, 2116, 2117, 2118, 2120, 2121, 2122, 2126, 2128, 2131, 2132, 2135, 2152, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2401, 2403, 2406, 2407, 2409, 2551, 2556, 2651, 2652, 2652, 2653, 2659, 2910, 3101, 3102, 3126, 3127, 3128, 3129, 3251, 3551, 3556, 3651, 3652, 3653.

**Observação:** os CFOP's 1910 e 2910 estarão disponiveis na versão 4.12.

Dessa forma, você terá disponível os seguintes campos:

Em **"Código que indica o responsável pela retenção do ICMS-ST"**, o sistema disponibiliza as seguintes opções:

- **Próprio declarante:** Por meio dessa opção, você indicará as operações em que o ICMS-ST foi recolhido de forma antecipada pelo adquirente da mercadoria, ou seja, a opção será utilizada no lançamento da Nota de Entrada cuja mercadoria foi adquirida para a revenda, e o cálculo do ICMS-ST realizado, uma vez que, ele será calculado por meio dos campos **"Base ST Extra Nota"** e **"Valor ST Extra Nota"** dos itens da nota. Considere os código de Entrada CST 00, 20, 40,90 ou CSOSN 101 e 102.
- **Remetente direto:** Essa opção será selecionada quando a responsabilidade pelo recolhimento do ICMS-ST for do remetente da mercadoria, caso ele seja o remetente Substituto Tributário. Os valores da substituição devem ser inseridos nos campos **"Base substituição"** e **"Vlr. substituição"** localizados nos itens da nota. Sendo que, deve-se considerar as Entradas com CST 10, 30, 70 ou CSOSN 201 ou 202.
- **Remetente indireto:** você irá selecionar essa opção, quando na operação de entrada o remetente da mercadoria já foi substituído, ou seja, o ICMS-ST não foi retido na nota fiscal. Os valores referentes à essa opção, devem ser inserido nos campos **"Base de Cálc. da ST de oper. ant."** e **"Vlr. do ICMS da ST de oper. ant."** nos itens da nota. Considere as Entradas CST 60 ou CSOSN 500.

A seguir, teremos alguns campos que devem ser preenchidos com as mesmas informações contidas no documento fiscal declarado, sendo elas:

- **"Chave de acesso do documento fiscal"**;
- **"Número do documento Fiscal"**;
- **"CNPJ Emitente"**;
- **"UF Emitente"**;
- **"CNPJ do destinatário"**;
- **"UF do destinatário"**;
- **"Código fiscal de operação e prestação"**;
- **"Número do item no documento fiscal"**.

**Nota:** o modelo a ser informado no campo Chave de acesso do documento fiscal eletrônico, deverá ser o modelo 55.

**Observação:** o preenchimento dos campos CNPJ do Centro de Distribuição e CNPJ do Centro de Distribuição, serão obrigatórios se você informar um dos CFOP's 5151, 5152, 5408, 5409, 5658 ou 5659, no campo Código fiscal de operação e prestação.

Preencha em **"Unidade de medida do item"**, a mesma unidade de medida utilizada para quantificação do estoque declarada no campo Informar a unidade de medida utilizada na quantificação do estoque do Registro 1000.

No campo **"Quantidade do item adquirido"**, deve conter a quantidade do item adquirido, sendo ele convertido na mesma medida declarada no campo Informar a unidade de medida utilizada na quantificação do estoque do Registro 1000, considerando que, uma vez que a quantidade de cada item de mercadoria será utilizada na quantificação de comercialização adotada pelo contribuinte, aplicando-se às operações de entradas, saídas e ao estoque de mercadorias.

**Nota:** sempre que a quantidade das entradas de cada item de mercadoria for menor que o somatório das saídas, será obrigatória a adição das entradas ocorridas no(s) período(s) de referência anterior(es) suficiente(es) para comportar a quantidade proveniente da mesma mercadoria.

Em **"Valor unitário do item"**, preencha o valor unitário líquido de aquisição do item convertido na mesma unidade de medida declarada no campo Informar a unidade de medida utilizada na quantificação do estoque.

No campo **"Base de cálculo do ICMS ST"**, deve conter a informação da base de cálculo utilizada para o cálculo do ICMS ST.

O **"Valor do ICMS do item suportado na entrada"**, corresponde ao valor do total do imposto suportado pelo contribuinte substituído, abrangendo o imposto incidente na operação própria do substituído e o retido por ST e, caso haja, a parcela do FECOP, ou ainda o antecipado pelo destinatário do Paraná nas operações de entrada, ou na ausência da informação da base.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

**Observação:** ao habilitar o parâmetro **"Considerar notas que não atualizam estoque na geração da ADRCST - USAESTADRCST"**, as notas que não atualizam o estoque também serão geradas no Registro 1110.

**Sub-aba 1120**

O Registro 1120 deverá conter as notas fiscais modelo 55 referentes às devoluções de compras ocorridas no mesmo mês em que foram computadas as entradas das mesmas mercadorias. As devoluções de compras são saídas que têm por objetivo anular os efeitos da operação entrada original da qual resultou o recebimento da mercadoria.

Ainda considerando apenas as notas fiscais modelo 55, inclusive as de emissão própria referente a produtos relacionados no Registro 1000, irão compor esse Registro os CFOP's 5201, 5202, 5205, 5206, 5207, 5208, 5209, 5210, 5213, 5214, 5215, 5410, 5411, 5660, 5661, 5662, 6201, 6202, 6205, 6206, 6207, 6208, 6209, 6210, 6213, 6214, 6215, 6410, 6411, 6660, 6661, 6662, 7200, 7201, 7202, 7205, 7206, 7207, 7210, 7211 e 7212.

Temos aqui, alguns campos que devem ser preenchidos com as mesmas informações contidas no documento fiscal declarado, sendo elas:

- **"Data de emissão do documento fiscal";**
- **"Código da Situação Tributária";**
- **"Chave de acesso do documento fiscal"**;
- **"Número do documento Fiscal"**;
- **"CNPJ Emitente"**;
- **"UF Emitente"**;
- **"CNPJ do destinatário"**;
- **"UF do destinatário"**;
- **"Código fiscal de operação e prestação"**;
- **"Número do item no documento fiscal"**.

O campo **"Unidade de medida do item"** utilizará a mesma unidade de medida informada no campo **"Unidade"** da grade **"Itens"** das centrais.

No campo **"Quantidade do item devolvida"**, deve conter a quantidade do item devolvida e convertida a mesma unidade de medida do campo Informar a unidade de medida utilizada na quantificação do estoque do Registro 1000.

Preencha no campo **"Valor unitário do item"**, o valor unitário líquido de aquisição do item, convertido na mesma unidade de medida declarada no campo Informar a unidade de medida utilizada na quantificação do estoque do Registro 1000.

Em **"Base de cálculo do ICMS ST"**, informe o valor da base e cálculo utilizada para o cálculo do ICMS-ST.

O campo **"Valor do ICMS do item suportado na entrada"**, corresponde ao valor total do imposto suportado pelo contribuinte substituído, abrangendo o imposto incidente na operação própria do substituto e o retido por ST, e caso haja, a parcela do FECOP.

Você irá completar o campo **"Chave de acesso do documento fiscal referenciado"**, com a chave de acesso do documento fiscal de modelo 55 da mercadoria que está sendo devolvida.

O **"Número do item no documento fiscal referenciado"** corresponde ao número do item do documento fiscal da mercadoria que está sendo devolvida.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1000)

## Sub-aba 1200

![Imagem 7: Sub-aba 1200](https://ajuda.sankhya.com.br/hc/article_attachments/1500003371101)

Esse registro deve ser preenchido, a fim de identificar a totalização das notas fiscais de saídas emitidas em operações internas de venda ao consumidor final declaradas no Registro, deduzidas das devoluções ocorridas no próprio mês da venda do produto identificado no Registro 1000.

Sendo assim, os valores dos campos a serem inseridos aqui, acontecerão da seguinte forma:

**Quantidade total de saídas para consumidor final** = Somatória do campo Quantidade do produto na saída (Registro 1210) - Somatória do campo Quantidade do item devolvida (Registro 1220)

**Valor total do ICMS efetivo nas saídas para consumidor final** = Somatória do campo Quantidade do produto na saída (Registro 1210) - Somatório do campo Quantidade do item devolvida (Registro 1220)

**Valor de confronto do ICMS das entradas** = Quantidade total de saídas para consumidor final \* Valor unitário médio do ICMS suportado na entrada (Registro 1100)

**Nota:**o campo Valor de confronto do ICMS das entradas, irá considerar somente duas casas decimais.

**Resultado do valor a recuperar ou a ressarcir** = Valor de confronto do ICMS das entradas - Valor total do ICMS efetivo nas saídas para consumidor final

**Observação:** se o resultado desse campo for negativo, preencha o campo com zero.

**Resultado do valor a complementar** = Valor de confronto do ICMS das entradas - Valor total do ICMS efetivo nas saídas para consumidor final

**Nota:** caso resultado dessa equação for positivo, preencha o campo com zero.

**Apuração do ICMS ST a recuperar ou a ressarcir** = Resultado do valor a recuperar ou a ressarcir \* ((Alíquota do ICMS aplicável ao item nas operações internas - Alíquota do FECOP) / Alíquota do ICMS aplicável ao item nas operações internas)

**Observação:** os campos aqui apresentados, encontram-se no Registro 1000 dessa tela.

**Apuração do ICMS ST a complementar** = Resultado do valor a complementar (Registro 1200)\* ((Alíquota do ICMS aplicável ao item nas operações internas - Alíquota do FECOP)/Alíquota do ICMS aplicável ao item nas operações internas)

**Nota:** os campos aqui apresentados, encontram-se no Registro 1000 dessa tela.

**Apuração do FECOP a ressarcir** = Resultado do valor a recuperar ou a ressarcir (Registro 1200) \* (Alíquota do FECOP (Registro 1000)/Alíquota do ICMS aplicável ao item nas operações internas (Registro 1000))

**Apuração do FECOP a complementar** = Resultado do valor a complementar (Registro 1200) \* (Alíquota do FECOP (Registro 1000)/Alíquota do ICMS aplicável ao item nas operações internas (Registro 1000))

**Sub-aba 1210**

Nessa sub-aba deve conter o Registro com todas as notas fiscais de saídas emitidas em operações internas de venda aos consumidores finais do produto declarado no Registro 1000,. Você deve inserir também, a totalidade das operações de saídas realizadas no período de apuração para cada produto comercializado sujeito à Substituição Tributária, ainda que não exista valor a recuperar, ressarcir, ou a complementar. Esse Registro visa atender ao disposto no art. 6º do Anexo IX do RICMS/17.

**Observação:** no sistema temos o uso de dois parâmetros que refletirão nos registros desta aba, são eles:

- O parâmetro **"Considerar notas de vendas para Produtor Rural na ADRC-ST PR - USAPRADRCST"**, que quando ligado, o sistema buscará as notas cuja o Parceiro seja Produtor Rural ("P");
- Além do parâmetro **"Considerar NFC-e na geração do R1210 na ADRC-ST PR - USANFCADRCST"**, ao ligá-lo, o sistema também buscará as notas fiscais com o modelo 65.

**Observação:** os Registros atribuídos aqui, devem ser somente as CFOP's iniciados em 5, com exceção daqueles cuja natureza represente devolução de compra.

A **"Data de Emissão do documento fiscal"**, deve ser preenchida com a mesma data de emissão declarada no documento fiscal.

No campo **"Código da Situação Tributária"**, informe o mesmo código da Situação Tributária declarado no documento fiscal.

Referente à **"Chave de acesso do documento eletrônico fiscal"**, você deve informar a chave de acesso do documento fiscal eletrônico modelo 55 ou 65.

**Nota:** se o número do documento fiscal for 55, o campo **"Finalidade da Operação"** do Cabeçalho da Central de Notas, representado pela tag <**indFinal**> do XML da NF-e, deve ser definido para Consumidor Final = 1.

Aqui, teremos alguns campos que devem ser preenchidos com as mesmas informações contidas no documento fiscal declarado, sendo elas:

- **"Número do documento Fiscal"**;
- **"CNPJ Emitente"**;
- **"UF Emitente"**;
- **"CNPJ ou CPF do destinatário"**;
- **"Código fiscal de operação e prestação"**;
- **"Número do item no documento fiscal"**.

Na **"Unidade de medida do item"**, informe a mesma unidade de medida utilizada no campo Informar a unidade de medida utilizada na quantificação do estoque do Registro 1000.

Preencha o campo **"Quantidade do produto na saída"**, com a quantidade do item convertida na mesma unidade de medida do campo anterior.

O **"Valor unitário do item"** deve ser preenchido com o valor unitário do item.

Preencha o campo **"Valor do ICMS efetivo na saída"**, com o resultado da multiplicação da alíquota interna da mercadoria sobre o valor da operação de venda ao consumidor final, ou na hipótese de operação beneficida com redução da base de cálculo, sobre a base de cálculo reduzida.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

**Sub-aba 1220**

As definições do Registro 1220 dessa aba, devem conter as notas fiscais de devolução de venda ocorridas no mesmo mês em que a saída da mesma mercadoria foi apurada. Assim, você terá disponível nessa aba todos os campos mencionados na aba anterior, além dos seguintes campos:

Em **"Chave de acesso do documento fiscal referenciado"**, você irá inserir a chave de acesso do documento fiscal modelo 55 ou 65 que acobertou a mercadoria que está sendo devolvida.

O **"Número do item no documento fiscal referenciado"**, corresponde ao número do item do documento fiscal que acobertou a mercadoria que está sendo devolvida.

**Observação:** o campo **"Finalidade da Operação"** do Cabeçalho da Central de Notas, representado pela tag <**indFinal**> do XML da NF-e, deve ser definido para Consumidor Final = 1.

**Nota:** os Registros a serem atribuídos aqui, devem ser somente as CFOP's iniciados em 1, cuja natureza represente Devolução de Venda em operação interna.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1000)

## Sub-aba 1300

Nesse registro deve ser informado para a identificação da totalização das notas fiscais de saída emitidas para outros estados, sendo essas declaradas no Registro 1310 do produto identificado no Registro 1000.

![Imagem 8: Nesse registro deve ser informado para a identificação da totalização das notas fiscais de saída emitidas para outros…](https://ajuda.sankhya.com.br/hc/article_attachments/360102190034)

Assim, os valores dos campos dessa aba serão realizados da seguinte forma:

**Quantidade total de saídas para outros estados** = Somatória Quantidade do produto na saída (Registro 1310) - Somatória Quantidade do item devolvida (Registro 1320)

**Valor total do ICMS efetivo nas saídas para outros estados** = Somatória Valor do ICMS efetivo na saída (Registro 1310) - Somatória Valor do ICMS efetivo na saída (Registro 1320)

**Valor de confronto do ICMS das entradas** = Quantidade total de saídas para outros estados \* Valor unitário médio do ICMS suportado na entrada (Registro 1100)

**Resultado do valor a recuperar ou a ressarcir** = Valor de confronto do ICMS das entradas - Valor total do ICMS efetivo nas saídas para outros estados

**Nota:** o cálculo a ser realizado no campo acima, será da forma que foi apresentada caso a opção a opção 1 - Recuperação em conta gráfica estiver selecionada do campo Código para reaver imposto nas saídas interestaduais (R1300) for selecionada.

Caso a opção 0 - Ressarcimento para fornecedor seja selecionada, e o resultado do cálculo do campo  Resultado do valor a recuperar ou a ressarcir for positivo ou zero, teremos o cálculo:

**Código para reaver imposto nas saídas interestaduais (R1300)** = 0 - Ressarcimento para fornecedor, então, Resultado do valor a recuperar ou a ressarcir = Valor de confronto do ICMS das entradas

**Apuração do ICMS ST a recuperar ou a ressarcir** = Resultado do valor a recuperar ou a ressarcir - Apuração do FECOP a ressarcir

**Apuração do FECOP a ressarcir** = (Valor unitário médio da base de cálculo do ICMS ST (Registro 1100) \* Alíquota do FECOP(Registro 1000)) \* Quantidade total de saídas para outros estados

**Sub-aba 1310**

Esse registro deve conter todas as notas fiscais de saída emitidas para outros estados do produto que foi declarado no Registro 1000, sendo que, ele visa atender à regra disposta no Art. 6º do Anexo IX do RICMS/17.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

**Observação:** nessa aba, temos alguns campos referentes às saídas, em cada um destes, você poderá inserir um número limitado de caracteres, observe:

- Ao informar um valor com mais de 3 caracteres nos campos **"Quantidade do produto na saída"** e/ou **"Quantidade total de saída para outros estados"**, o sistema irá arrendondar esse valor para somente os 3 (três) caracteres aceitos no campo.
- Esse arredondamento acontecerá também no campo **"Valor do ICMS efetivo na saída"**, porém neste, o valor é de 2 (dois) caracteres. Referente a esse campo, considere o exemplo a seguir:

Ao realizar o cálculo 1,022 \* 1,50 \* 0,18 = **0,2759**, o sistema arredondará o valor final para **0,28**.

**Nota:** os campos presentes nessa sub-aba, equivalem aos mesmo campos presentes na sub-aba 1210 da aba 1200.

**Sub-aba 1320**

Esse Registro corresponde às notas fiscais de devoluções de vendas ocorridas no mesmo mês em que foi computada a saída da mesma mercadoria, uma vez que, as devoluções de vendas são entradas que têm por objetivo anular os efeitos da operação original da qual resultou a saída da mercadoria.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

**Observação:** os campos presentes nessa sub-aba, equivalem aos mesmo campos presentes na sub-aba 1220 da aba 1200.

O valor inserido no campo **"Valor do ICMS efetivo na saída"**, deverá conter no máximo 3 (três) casas decimais.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1000)

## Sub-Aba 1400

O objetivo desse registro é identificar a totalização das notas fiscais de venda emitidas em operações internas com produtos alimentícios, destinados à merenda escolar, órgãos da administração pública, cozinhas industriais, restaurantes e similates, hotéis e similares, pizzares que trata o art. 119 do Anexo IX do RICMS/2017, declaradas no registro 1410 do produto que foi identificado no registro 1000.

![Imagem 9: O objetivo desse registro é identificar a totalização das notas fiscais de venda emitidas em operações internas com…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003314922)

Nos campos aqui apresentados, temos os cálculos que serão realizados para inserir os valores nos mesmos. Observe:

**Quantidade total de saídas para outros estados** = Somatória Quantidade do produto na saida (Registro 1410) - Somatória Quantidade do item devolvida (Registro 1420)

**Valor total do ICMS efetivo nas saídas** = Somatória Valor do ICMS efetivo na saida (Registro 1410) - Somatória Valor do ICMS efetivo na saida (Registro 1420)

**Valor de confronto do ICMS das entradas** = Quantidade total de saídas para outros estados (Registro 1400) \* Valor unitário médio do ICMS suportado na entrada (Registro 1100)

**Apuração do ICMS ST a recuperar ou a ressarcir** = Valor de confronto do ICMS das entradas (Registro 1400) - Valor unitário médio do ICMS suportado na entrada (Registro 1100)

**Nota:** quando o resultado do campo Valor do ICMS efetivo na saída possuir mais de 2 (duas) casas decimais, o sistema o arrendodará para que este fique com apenas 2 (dois) caracteres.

**Nota:** quando você realização a habilitação da marcação **"Desconsiderar TOP na geração da ADRC-ST no R1400?"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) do [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), os itens das notas fiscais emitidas não serão abordados na geração do arquivo da TOP utilizada.

**Sub-aba 1410**

O referido Registro deve conter as notas fiscais emitidas em operações internas do produto que foi identificado no Registro 1000, sendo que, ele visa atender as regras dispostas no Art. 119 do anexo IX do RICMS/17. Considere para esse Registro, os CFOP's 5101,5102, 5103, 5104, 51005, 5106, 5109, 5110, 5112, 5113, 5114, 5115, 5116, 5117, 5118, 5119, 5120, 5122, 5123, 5129, 5131, 5132, 5401, 5402, 5403, 5408, 5409, 5414, 5414, 5415, 5551, 5552, 5557,5910, 5911, 5912, 5913, 5922 e 5949.

**Importante:** para que esse registro seja gerado, é necessário que você realize a habilitação da marcação **"Produto alimentício conforme art. 119 do Anexo IX do RICMS/2017 PR?"** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos) do Cadastro de produtos.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

Quando você realizar o preenchimento do campo **"Quantidade do produto na saída"**, o sistema arrendondará esse valor para 3 (três) caracteres, quando o valor inserido no campo possuir mais de três caracteres.

**Nota:** os campos presentes nessa sub-aba, equivalem aos mesmo campos presentes na sub-aba 1310 da aba 1300.

**Sub-aba 1420**

No Registro 1420 devem conter as notas fiscais de devoluções de vendas ocorridas no mesmo mês em que a saída dessas mercadorias foram computadas. Sendo que, serão atribuídas a esse Registro as CFOP's 1201, 1202, 1203, 1205, 1206, 1207, 1208, 1209, 1212, 1213, 1214, 1410, 1411, 1660, 1661 e 1662. Nas notas de devolução devem constar para o item devolvido, o mesmo NCM informado na nota de saída que tenha item classificado dentre os NCM's apontado no Registro 1410.

**Observação:** os campos presentes nessa sub-aba, equivalem aos mesmo campos presentes na sub-aba 1320 da aba 1300.

**Observação:** caso você insira um valor com mais de 3 (três) casas decimais no campo **"Quantidade do item devolvida"**, o sistema arrendondará esse valor para que este permaneça apenas com 3 (três) caracteres.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1000)

## Sub-aba 1500

O Registro 1500 será utilizado para identificar a totalização das notas fiscais de saídas internas destinadas ao contribuinte do Simples Nacional, sendo essas devem ser declaradas nos Registros 1510 do produto que foi identificado no Registro 1000.

![Imagem 10: O Registro 1500 será utilizado para identificar a totalização das notas fiscais de saídas internas destinadas ao…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003372801)

Assim, temos os seguintes cálculos a serem realizados no preenchimento dos campos dessa sub-aba:

**Quantidade total de saídas destinadas a contribuintes do Simples Nacional** = Somatória Quantidade do produto na saída (Registro 1510) - Quantidade do item devolvida (Registro 1520)

**É o valor do ICMS ST a recuperar por unidade** = (Valor unitário médio da base de cálculo do ICMS ST (Registro 1100) / (1+ MVA)) \* (Coeficiente da MVA \* Percentual de redução) \* (Alíquota do ICMS aplicável ao item nas operações internas (Registro 1000)

Referente ao campo acima, destacamos que:

- Este aceitará valores somente até duas casas decimais;
- O MVA especificado na equação acima, é o MVA utilizado para retenção do ICMS ST;
- O coeficiente, corresponde ao percentual de redução a ser aplicado sobre a MVA, sendo 70% se a alíquota for de 18%, e 50% se a alíquota for de de 12%.

**Nota:** quando o resultado do campo acima possuir mais de 2 (duas) casas decimais, o sistema o arrendará para que este fique com apenas 2 (dois) caracteres.

**Apuração do ICMS ST a recuperar ou a ressarcir** = Quantidade total de saídas destinadas a contribuintes do Simples Nacional \* É o valor do ICMS ST a recuperar por unidade

**Nota:** assim como o campo anterior, quando o resultado do campo Apuração do ICMS ST a recuperar ou a ressarcir possuir mais de 2 (duas) casas decimais, o sistema o arrendará para que este fique com apenas 2 (dois) caracteres.

Quando o sistema realizar o cálculo do campo Apuração do ICMS ST a recuperar ou ressarcir, o resultado do campo É o valor do ICMS ST a recuperar por unidade será cosiderado no resultado com duas casas decimais. Observe o exemplo:

É o valor do ICMS ST a recuperar por unidade: **4,19** \* Quantidade total de saídas destinadas a contribuintes do Simples Nacional: **6,00** = Apuração do ICMS ST a recuperar ou a ressarcir: **25,16**

O **"MVA da operação"**, corresponde ao MVA utilizado no cálculo do campo É o valor do ICMS ST a recuperar por unidade desse Registro.

**sub-aba 1510**

Nesse registro, devem conter as notas fiscais de saída interna destinadas ao contribuinte do Simples Nacional do produto declarado no Registro 1000, em caso de aquisição de mercadorias, que se referem as Seções VI, VII, XVIII e XXII, do Anexo IX do RICMS/17 com o imposto retido calculado com a aplicação do percentual integral da MVA. Considere que, nesse Registro serão tratados somente as saídas internas CFOP, com exceção das CFOP's de devolução, sendo eles, 5101, 5102, 5103, 5104, 5105, 5106, 5109, 5110, 5111, 5112, 5113, 5114, 5115, 5116, 5117, 5118, 5119, 5120, 5122, 5123, 5129, 5131, 5132, 5401, 5402, 5403, 5405, 5408, 5409, 5414, 5415, 5551, 5552, 5557, 5910, 5911, 5912, 5913, 5922 e 5949.

Informe no campo **"Código da Situação Tributária"**, o mesmo código da Situação Tributária declarado no documento fiscal, sendo que ele deve ser o mesmo do CST/CSOSN declarado no XML.

Na **"Data de Emissão do documento fiscal"**, deve ser informada a mesma data de emissão declarada na chave de acesso.

Referente à **"Chave de acesso do documento fiscal eletrônico"**, informe a chave de acesso do modelo 55.

Posteriormente, pereceba que a tela dispõe de alguns campos, eles devem ser preenchidos de acordo com as informações contido no documento fiscal, são eles:

- **"Número do documento Fiscal"**;
- **"CNPJ Emitente"**;
- **"UF Emitente"**;
- **"CNPJ do destinatário"**;
- **"UF do Destinatário"**;
- **"Código fiscal de operação e prestação"**;
- **"Número do item no documento fiscal".**

Informe no campo **"Unidade de medida do item"**, a unidade de medida utilizada na quantificação do estoque identificado no campo Informar a unidade de medida utilizada na quantificação do estoque do Registro 1000.

No campo **"Quantidade do produto na saída"**, deve possuir a informação da quantidade do item convertido na mesma unidade de medida que constar no campo Informar a unidade de medida utilizada na quantificação do estoque do registro 1000.

Insira o valor unitário líquido do item no campo **"Valor unitário do item"**.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

**Sub-aba 1520**

No referido Registro, deve conter as notas fiscais de devolução de venda ocorridas no mesmo mês em que foi computada a saída da mesma mercadoria. As CFOP's a serem atribuídas neste serão 1201, 1202, 1203, 1204, 1506, 1207, 1208, 1209 1212, 213, 1214, 1410, 1411, 1660, 1661 e 1662.

**Observação:** os campos dessa sub-aba, correspondem aos campos  apresentados na sub-aba 1510.

Informe em **"Chave de acesso documento fiscal eletrônico"**, a chave de acesso apresentado no documento fiscal.

Nos campos **"Chave de acesso do documento fiscal referenciado"** e **"Número do item no documento fiscal referenciado"**, insira a chave de acesso e o número do item do documento fiscal da mercadoria devolvida, respectivamente.

No botão **"Outras Opções..."**, você tem a opção **"Abrir documento (Ctrl + K)"**, em que, ao clicar, o sistema abrirá a nota de Compra/Venda selecionada no registro.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#aba1000) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#top)

## Aba 1999

O Registro 1999 destina-se à identificação do encerramento do Bloco 1 e a quantidade de Registros, ou linhas, existentes nele.

![Imagem 11: O Registro 1999 destina-se à identificação do encerramento do Bloco 1 e a quantidade de Registros, ou linhas,…](https://ajuda.sankhya.com.br/hc/article_attachments/360102191794)

Você informará no campo **"Quantidade total de linhas"**, a quantidade de linhas do bloco 1, considerando também o próprio Registro 1999.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#top)

## Aba 9000

O Registro 9000 irá identificar a totalização dos campos de apuração dos valores a ressarcir, a recuperar ou a complementar dos Registros totalizadores 1200, 1300, 1400 e 1500.

![Imagem 12: O Registro 9000 irá identificar a totalização dos campos de apuração dos valores a ressarcir, a recuperar ou a…](https://ajuda.sankhya.com.br/hc/article_attachments/360104358573)

Assim, nos campos dessa aba teremos os seguintes cálculoa a serem realizados:

**Valor a recuperar ou a ressarcir nas saídas para consumidor final** = somatório Apuração do ICMS ST a recuperar ou a ressarcir (Registro 1200) - Somatório Apuração do ICMS ST a complementar (Registro 1200)

**Observação:** caso o resultado desse campo for negativo, o valor dele será igual a zero.

**Valor a complementar nas saídas para consumidor final** = Somatório Apuração do ICMS ST a recuperar ou a ressarcir (Registo 1200) - Somatório Apuração do ICMS ST a complementar (Registro 1200)

**Nota:** se o resultado desse campo for positivo, o valor dele será zero.

**Valor a recuperar ou a ressarcir nas saídas para outros estados** = Somatório dos valores declarados no campo Apuração do ICMS ST a recuperar ou a ressarcir do Registro 1300.

**Valor a recuperar ou a ressarcir nas saidas de que trata o art. 119** = Somatória dos valores do campo Apuração do ICMS ST a recuperar ou a ressarcir do Registro 1400.

**Valor a recuperar ou a ressarcir nas saídas destinadas a contribuinte do Simples Nacional** = Somatória dos valores declarados no campo Apuração do ICMS ST a recuperar ou a ressarcir de todos os Registros 1500.

**Valor a ressarcir do FECOP** = Somatório Apuração do FECOP a ressarcir (Registro 1200) + Somatório Apuração do FECOP a ressarcir (Registro 1300) - Apuração do FECOP a complementar (Registro 1200)

**Nota:** se o resultado desse campo for negativo, o valor será igual a zero.

**Valor a complementar do FECOP** = Somatório Apuração do FECOP a ressarcir (Registro 1200) + Somatório Apuração do FECOP a ressarcir (Registro 1300) - Apuração do FECOP a complementar (Registro 1200)

**Observação:** se o resultado desse campo for positivo, o valor desse campo será igual a zero.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#top)

## Aba 9999

O referido Registro destina-se a identificar o encerramento do arquivo digital e a informar a quantidade de Registro, ou linhas existentes no arquivo.

![Imagem 13: O referido Registro destina-se a identificar o encerramento do arquivo digital e a informar a quantidade de Registro,…](https://ajuda.sankhya.com.br/hc/article_attachments/360104358693)

Assim, informe no campo **"Quantidade total de linhas do arquivo"** a quantidade de linhas do Registro, sendo que, ele deve considerar também o próprio Registro 9999.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#top)

## Processamento e Geração do Arquivo

Quando você clicar no botão ![Imagem 14: Quando você clicar no botão "Processar" , o sistema irá iniciar o processo de busca das informações referentes aos…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003341501) **"Processar"**, o sistema irá iniciar o processo de busca das informações referentes aos documentos fiscais de entrada e saída que tenham produtos qualificados como sujeitos à Substituição Tributária e destinados à revenda.

[GIF animado: Imagem 15: Quando você clicar no botão "Processar" , o sistema irá iniciar o processo de busca das informações referentes aos…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003390102)

Como exibido no gif acima, ao clicar no botão ![Imagem 16: Como exibido no gif acima, ao clicar no botão "Ver Histórico" do pop-up "Processos" , você poderá consultar o histórico…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003436381) **"Ver Histórico"** do pop-up **"Processos"**, você poderá consultar o histórico das gerações já realizadas anteriormente. Também é possível consultar esse histórico, por meio do botão ![Imagem 17: Como exibido no gif acima, ao clicar no botão "Ver Histórico" do pop-up "Processos" , você poderá consultar o histórico…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003436421) **"Histórico de Gerações"** do pop-up.

Após o processamento do arquivo e conferência das informações, utilize o botão ![Imagem 18: Após o processamento do arquivo e conferência das informações, utilize o botão "Gerar" para a geração do Arquivo;…](https://ajuda.sankhya.com.br/hc/article_attachments/360102164914) **"Gerar"** para a geração do Arquivo; assim, ao final dela um Arquivo ZIP que conterá o arquivo txt da Geração da ADRC-ST que deverá ser validado junto a SEFAZ do Paraná.

Logo depois, o envio do arquivo será realizado por meio do Portal da Receita PR no site [https://receita.pr.gov.br](https://receita.pr.gov.br/), no menu **"Arquivo Digital ST"** > **"Envio de Arquivo"**.

Após o envio do arquivo referente à ADRC-ST, consulte se o mesmo foi processado ou rejeitado. Em caso de rejeição, consulte a planilha com os erros, a fim de avaliar e verificar a possibilidade de corrigi-los diretamente na tela Geração do Arquivo ADRC-ST PR e preparar uma nova Geração do Arquivo.

Na impossibilidade de correção do erro na própria tela, será necessário analisar a planilha para avaliação e possíveis correções no sistema.

Além disso, caso você realize a edição de algum registro dessa tela, o sistema habilitará as marcações **"Digitado"** automaticamente. Sendo assim, ao reprocessar o registro, a linha correspondente a ele não sofrerá alteração caso a linha seja excluída, de forma que, ocorrerá o reprocessamento normalmente criando assim, a respectiva linha excluída novamente.

**Observação:** quando houver a modificação manual dos registros, o sistema identificará se este é Pai ou Filho. Uma vez que este seja Pai, o Filho também será marcado como Digitado, porém, caso a modificação ocorra em um registro Filho, apenas este será marcado como Digitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#top)
