---
id: "360044600174"
titulo: "Lei da Transparência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600174-Lei-da-Transpar%C3%AAncia"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:49:47Z"
rotulos: ["Configuração", "NF-e", "Impostos", "Lei da Transparência manual", "NFS-e", "Transparência Tributária e Flexibilidade Fiscal", "Documentos Eletrônicos"]
---

# Lei da Transparência

Conforme a Lei 12.741/2012 e informações do órgão IBPT (Instituto Brasileiro de Planejamento e Tributação), as alíquotas médias dos impostos a serem destacadas em documentos fiscais eletrônicos (Cupom Fiscal, NFC-e, NF-e, CT-e), serão melhores exibidas se separadas em **"Federal"**, **"Estadual"** e **"Municipal"**.

O sistema está preparado para trabalhar com esta nova forma de envio da informação das alíquotas médias, trazendo maior flexibilidade às empresas, que poderão enviar as alíquotas médias dos impostos referentes às vendas de forma geral (Nacional) ou fracionada (Federal, Estadual e Municipal). Além de ser possível definir em qual operação, ou para quais Parceiros, estas informações serão enviadas.

Vale salientar, que a carga média para importação depende da origem do produto. Sendo de origem Nacional, pode-se escolher em gerar os dados de forma agrupada ou separada; porém, se a origem for Estrangeira, a carga média utilizada será para importação.

Vejamos as configurações a serem consideradas no sistema:

#### [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)

Nas abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostos) e [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostosinformaesporempresa), temos os seguintes campos, onde informam-se os percentuais médios de tributação:

- % Carga Média Trib. Nacional;
- % Carga Média Trib. Federal;
- % Carga Média Trib. Estadual;
- % Carga Média Trib. Importação.

![Imagem 1: Para configurações do envio da Lei da transparência para NFS-e, acesse a Lei da Transparência dos Tributos na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16640713621655) Para configurações do envio da Lei da transparência para NFS-e, acesse a [Lei da Transparência dos Tributos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046970974#leidatransparnciadostributos) na tela Informações Complementares.

#### [Cadastros de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553)

Na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaimpostos) desta tela, temos os campos abaixo para preenchimento dos percentuais médios de tributação:

- % Carga Média Trib. Nacional;
- % Carga Média Trib. Federal;
- % Carga Média Trib. Estadual.

O sistema valida se todos os serviços do documento possuem os mesmos percentuais de Carga Média Tributária Municipal e Federal ou somente a Carga Média Tributária Nacional. Caso algum serviço possua tais cargas médias diferentes será apresentada a seguinte mensagem:

**"As cargas médias tributárias entre os serviços não podem ser diferentes entre si."**

Consideremos dois exemplos:

| Serviço | Carga Média Municipal | Carga Média Federal | Carga Média Nacional |
| --- | --- | --- | --- |
| A | 5 | 2 |  |
| B | 5 | 2 |  |
| C |  |  | 7 |

Neste exemplo, a mensagem acima descrita será apresentada.

| Serviço | Carga Média Municipal | Carga Média Federal | Carga Média Nacional |
| --- | --- | --- | --- |
| A | 5 | 2 |  |
| B | 5 | 2 |  |
| C | 5 | 2 |  |

Já com esta configuração, a mensagem não será exibida.

#### [Cadastros de Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602054)

No **"Painel Geral"** e na aba **"Impostos"** desta tela, tem-se os seguintes campos onde informam-se os percentuais médios de tributação:

- % Carga Média Trib. Nacional;
- % Carga Média Trib. Federal;
- % Carga Média Trib. Estadual;
- % Carga Média Trib. Municipal;
- % Carga Média Trib. Importação.

**Importante:** quando o campo **"% Carga Média Trib. Nacional"** estiver vazio, a alíquota que calcula a tag **<vTotTrib>** será definida através da soma das alíquotas dos campos **"% Carga Média Trib. Estadual"** e **"% Carga Média Trib. Federal"**. Sendo assim, caso você queira utilizar a soma nas alíquotas, é preciso apagar manualmente o campo de alíquota nacional.

#### [Cadastros de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)

Na aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), você realizará a marcação **"Aplicar a lei da transparência"**.

#### [Cadastros de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)

Na aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes), deve-se realizar a configuração do campo Aplicar a lei da transparência, que possui três opções de definição:

- Aplicar sempre;
- Nunca aplicar;
- Usar do parceiro.

Caso o referido campo esteja definido com a opção **"Nunca aplicar"**, a informação pertinente à Lei da Transparência não será gerada.

Para que a informação seja impressa, o campo deve estar definido com as opções, **"Aplicar sempre"** ou **"Usar do parceiro"**; além disso, o parâmetro **"Fonte do cálculo da Carga Média Tributária - LEI12741FONTE"** deve estar devidamente preenchido.

Definindo-se o campo com a opção Usar do parceiro, o sistema verifica se no [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), a marcação Aplicar a lei da transparência presente na aba Fiscal está realizada, ou se o campo **"Classificação de ICMS"** do Parceiro (também presente na aba Fiscal) está determinado como Consumidor Final, Produtor Rural ou Consumidor Contribuinte, para geração das informações.

**Importante:** pode-se criar os percentuais da carga média tributária informando-se o percentual agrupado (Nacional) ou separado (Federal, Estadual e Municipal). Caso seja feita a tentativa de se informar os dois ao mesmo tempo, o sistema irá exibir as mensagens alertando tal inconsistência.

Notemos abaixo as regras para geração ou não da Carga Média Tributária referente à Lei da Transparência:

- O parâmetro **"Fonte do cálculo da Carga Média Tributária - LEI12741FONTE"** deve estar devidamente preenchido;
- O Tipo de Movimentação da nota deve ser **"Venda"** (TGFCAB.TIPMOV = V);
- O campo Aplicar a lei da transparência na tela Tipos de Operação - TOP, aba Validações deve ser igual a Usar do parceiro ou Aplicar sempre; se for igual a Usar do parceiro, o campo Aplicar a lei da transparência na tela Parceiros,  aba Fiscal deve estar assinalado, ou o campo **"Classificação ICMS"** (nesta mesma tela e aba) deve estar definido como **"Consumidor Final"**, **"Produtor Rural"** ou **"Consumidor Contribuinte"**.
- Se o campo **"Origem do produto"** (tela Produtos, aba Geral) estiver entre **0**, **3**, **4**, **5** ou **8**, significa que a origem do item em questão, é Nacional. Neste caso, as cargas médias geradas serão agrupadas (Nacional) ou separadas (Federal, Estadual e Municipal); se for diferente dos valores inicialmente citados, significa que a origem é Estrangeira. Nesse caso as cargas médias geradas serão de importação.
- Se todas as condições até aqui mencionadas forem atendidas, o sistema irá buscar os percentuais para fazer o cálculo. Tem-se uma ordem para busca de tais valores. A saber:

**Para Produto:**

 **1º -** Cadastro de Produtos, aba Impostos / Informações por empresa (TGFPEM);

 **2º -** Cadastro de Produtos, aba Impostos (TGFPRO);

 **3º -** Cadastro de Grupo de Produtos/Serviços, aba Impostos por Empresa (TGFGEM);

 **4º -** Cadastro de Grupo de Produtos/Serviços, Painel Geral (TGFGRU).

**Para Serviço:**

 **1º -** Cadastro de Produtos, aba Impostos (TGFPRO);

 **2º -** Cadastro de Grupo de Produtos/Serviços, aba Impostos por Empresa (TGFGEM);

 **3º -** Cadastro de Grupo de Produtos/Serviços, Painel Geral (TGFGRU).

Ao gerar o lote da nota, o sistema irá verificar se as condições acima foram atendidas e gerar os dados no XML.

O cálculo acima será realizado e o sistema irá preencher a tag **<vTotTrib>** tanto para os itens, quanto para o grupo de total da nota. Contudo, para que essas informações sejam inseridas como **"Dados Adicionais"** da nota, é necessária uma configuração no sistema:

Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#botooutrasopes), **"Complemento p/ Itens da Nota (Web)"** é necessário adicionar o campo **"Total dos Tributos"** contido no grupo de Variáveis, à coluna **"Campos em Uso"**:

![Imagem 2: Na tela Preferências da Empresa , botão Outras Opções , "Complemento p/ Itens da Nota (Web)" é necessário adicionar o…](https://ajuda.sankhya.com.br/hc/article_attachments/5701190262551)

Deste modo, o sistema irá gerar a tag **<infAdProd>** por item, com as informações das cargas médias calculadas. É importante lembrar que somente as cargas com valor serão adicionadas a essa tag.

O grupo total também possui uma tag que receberá a carga média tributária total da nota, a **<infAdic>**. Dentro dessa, a tag **<infCpl>** receberá os valores totais.

**Observação:** a variável &tottributosnfe, totaliza os campos % Carga Média Trib. Nacional; % Carga Média Trib. Federal; % Carga Média Trib. Estadual e % Carga Média Trib. Importação de cada um dos itens da notas, geralmente informados na tag **<infAdProd>**. Consideremos abaixo um exemplo do uso desta variável :

<det nItem="1">

<infAdProd>3,45 PECAS/ML | Val. aprox. tributos: R$73.44 (13.45% Fed Nac) R$65.52 (12.00% Est)</infAdProd>

</det>

<det nItem="2">

<infAdProd>3,45 PECAS/ML | Val. aprox. tributos: R$73.44 (13.45% Fed Nac) R$65.52 (12.00% Est)</infAdProd>

</det>

Com o uso desta variável no modelo .txt, as informações complementares somariam os tributos acima:

<infAdic>

<infCpl> SUA VARIAVEL : Total aproximado de tributos da nota: R$382.12 (13.45% Fed Nac) R$340.92 (12.00% Est) </infCpl>

</infAdic>"

#### Impressão de Variáveis

Em relação às variáveis que buscam as informações dos itens da nota, suponhamos que queira-se configurar um **"arquivo.txt"** com algumas variáveis que deseja-se que sejam impressas nas observações do DANFE.

Para isso, cria-se o arquivo e faz-se seu salvamento no diretório do computador cujo o parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"** esteja apontando.

Exemplo: D:\Modelos\

Na tela **"Configurações > Avançado > Modelos de Nota Fiscal/Duplicatas/Boleto(s)"** cria-se um modelo e informa-se o caminho que o arquivo anteriormente criado, esteja salvo.

Exemplo: D:\Modelos\OBSNOTA.txt

Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos) informa-se o modelo criado na tela anterior; o campo irá depender do documento que será emitido.

A variável que trará as informações das cargas médias tributárias é a **"&vlrtributos01"**. Com estas configurações, os valores serão informados na tag **<infCpl>**.
