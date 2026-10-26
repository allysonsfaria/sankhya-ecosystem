---
id: "360043796574"
titulo: "Importar dados da DI-Declaração da Importação via XML - Nota de Nacionalização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043796574-Importar-dados-da-DI-Declara%C3%A7%C3%A3o-da-Importa%C3%A7%C3%A3o-via-XML-Nota-de-Nacionaliza%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-09-19T02:26:08Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "Impostos", "Despacho Alfandegário", "Importação Simplificada", "Geração Automática de NF-e", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# Importar dados da DI-Declaração da Importação via XML - Nota de Nacionalização

#### **(1)**Nacionalização de Produtos

A nacionalização de um produto é o ato de tornar nacional uma mercadoria que era de origem estrangeira. Ou seja, um produto de procedência estrangeira sendo importado de forma definitiva, realizando os procedimentos necessários para que sua entrada no país ocorra em conformidade com a legislação.

Com base nessas informações um despachante realiza o desembaraço alfandegário da mercadoria, desde a geração dos documentos oficiais até o cumprimento das normas comerciais, cambiais e fiscais.

Depois de finalizadas todas essas obrigações, o adquirente da mercadoria precisa realizar a geração da NF-e de entrada no sistema. O processo manual de lançamento deve ser feito item a item e, dependendo da quantidade de itens, isso pode demorar.

Para agilizar o processo foi criada uma rotina no Sankhya-W, que importa um XML no formato da NF-e e inclui os itens do mesmo de forma automática.

(1)** Formato do arquivo XML**

Para conseguir importar o arquivo, o despachante deverá encaminhar o arquivo XML no mesmo formato da NF-e, porém com as tags específicas do processo de importação.

(1)** Importando o arquivo**

![Imagem 1: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/17371087159191) Acesse: Configurações » Avançado » Preferências

Para que o sistema consiga ler as tags referentes à importação, ligue o parâmetro **“IMPTAGDINOTNAC - Importar tag declaração de importação para nota de nacionalização?”.** Desta forma, ao processar o arquivo, o sistema irá considerar as tags referentes ao processo de importação, conforme exemplificado anteriormente. 

**![Imagem 2: NOTA:](https://ajuda.sankhya.com.br/hc/article_attachments/17371098284439) NOTA:**

Este parâmetro deve ser **desligado** depois que o processo de importação (nota de nacionalização) for realizado. Pois, caso o usuário faça a importação de uma nota de compra normal, o sistema emitirá um erro informando que não localizou as tags do processo de nacionalização.

![Imagem 3: Este parâmetro deve ser desligado depois que o processo de importação (nota de nacionalização) for realizado. Pois,…](https://ajuda.sankhya.com.br/hc/article_attachments/13164002497559)

![Imagem 4: Acesse: Comercial » Consulta » Portal de Compras](https://ajuda.sankhya.com.br/hc/article_attachments/17371098285463) Acesse: Comercial » Consulta » Portal de Compras

- Com o parâmetro ligado, inclua a nota de compra (nacionalização) e informe os dados de cabeçalho manualmente;
- Após digitar o cabeçalho da nota, no botão **“Outra Opções(...)”,** escolha a opção “**Importar Xml da nota fiscal eletrônica**”, selecione o arquivo XML (no formato da NF-e) e envie;
- Feito isso, o sistema irá incluir os itens e as respectivas informações referentes ao processo de importação;
- Para conferência dos valores e possíveis ajustes, selecione o item e clique no botão Outras Opções(...), da grade de Itens, opção: **"Declaração de Importação e Adições"**. Será possível identificar os valores importados pelo XML.

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/17371087166359) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Para que o Sistema faça a importação da DI 'Declaração de Importação e Adições' de forma correta e traga os impostos, o campo **"Tem II"**: deve esta marcado.

![Imagem 6: Para que o Sistema faça a importação da DI 'Declaração de Importação e Adições' de forma correta e traga os impostos, o…](https://ajuda.sankhya.com.br/hc/article_attachments/13172204070807)

#### **(1)** Informações sobre o lançamento da nota de nacionalização (Importação)

O valor dos produtos deve ser composto da seguinte forma, conforme valores destacados na DI: Valor do produto = Valor do Produto no Embarque + Valor do II + Frete + Seguro + THC.

A base de cálculo de ICMS deve ser composta por Valor do Produto + Valor das despesas aduaneiras + PIS Importação + COFINS Importação + ICMS do item. + o TUS (SISCOMEX)

Assim, deve ser lançado no valor de Destaque da nota o valor de despesas aduaneiras + Total PIS + Total COFINS + ICMS da nota para que o total da nota fique igual a base de ICMS.

#### **(1)** Parâmetros que influenciam na emissão de nota de nacionalização:

**(2)** **"Tratar Despesa Aduaneira em NF-e Nacionalização - SOMDESADUNFENAC":** O parâmetro **"Tratar Despesa Aduaneira em NF-e Nacionalização - SOMDESADUNFENAC"** define como o sistema irá considerar o valor da despesa aduaneira no total da nota de nacionalização. Existem duas opções de configuração.

**(2)** **"Tratar ICMS em NF-e Nacionalização - SOMAICMSNFENAC": irá tratar o destaque do ICMS em operações de Nacionalização/Importação na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras). O parâmetro pode ter três comportamentos conforme a opção selecionada.**

(2)** "Tratar II em NF-e Nacionalização - SUMVLRIIOUTNOTA":** Quando se tratar de uma nota cuja TOP é Compra ou Devolução, o "Valor de Imposto da Importação" poderá ser somado ao valor total da nota através da utilização do parâmetro **"Tratar II em NF-e Nacionalização - SUMVLRIIOUTNOTA"**, que poderá assumir alguns comportamentos.

**(2)** **"Tratar PIS e COFINS em NF-e Nacionalização - SOMPISCOFNFENAC":** irá ajustar a apresentação do destaque do PIS e COFINS em operações de Nacionalização/Importação na Central de Compras. Você poderá selecionar a opção conforme seus respectivos comportamentos.

**(2)** **"Imposto só em tag exclusiva em nota nacionalização - IMPTAGEXCNOTNAC":**

Utilizando o parâmetro mencionado tem-se que os valores de impostos não serão inseridos em outros campos de valor para compor o total das notas de nacionalização. Diante disso, os valores dos impostos ficarão apenas em seus campos e tags exclusivas, compondo assim, o total da NFe.

Ainda referente ao parâmetro citado, tem-se que, quando o parâmetro **"Utiliza MGE Import para nota de importação? - USAMGEIMPORT"** estiver habilitado, na geração do XML será identificado que a chave de parâmetro **IMPTAGEXCNOTNAC** já foi utilizada no MGE Importação, sendo assim, os impostos da tag <vOutros> não serão subtraídos novamente.

**(2)** **"Separar <vII> do <vProd> no XML da NFE? - SEPVIIVPRODNFE":** Quando o parâmetro Tratar II em NF-e Nacionalização - SUMVLRIIOUTNOTA estiver selecionado com alguma das opções diferente de Não se aplica, os parâmetros **"Separar <vII> do <vProd> no XML da NFE? - SEPVIIVPRODNFE"** e **"Imposto só em tag exclusiva em nota nacionalização - IMPTAGEXCNOTNAC"** devem estar desligados. Caso a configuração seja feita contrária ao exposto acima, o sistema exibirá uma mensagem de alerta no momento da confirmação da nota e não realizará a aprovação da mesma.

**(2)** **"Importação, tag vOutro da nota sem valor do ICMS e - VOUTNOTASEMICMS":** Quando o parâmetro Tratar ICMS em NF-e Nacionalização - SOMAICMSNFENAC for definido com alguma das opções diferentes de Não se aplica, os parâmetros **"Imposto só em tag exclusiva em nota nacionalização - IMPTAGEXCNOTNAC"**, **"Importação, tag vOutro da nota sem valor do ICMS e - VOUTNOTASEMICMS"** e **"Somar impostos no total da NF-e de nacionalizao e SOMAIMPNFNAC"** não poderão estar ligados; do contrário, o sistema exibirá mensagens ao confirmar a nota e não realizará a aprovação da mesma.

**(2)** **"Importação, tag vOutro do item sem valor do ICMS - VOUTITEMSEMICMS":**Caso o parâmetro "Importação, tag vOutro do item sem valor do ICMS - VOUTITEMSEMICMS" esteja ativado, em notas de importação, quanto a geração da tag <vOutro> correspondente aos itens da nota, o valor do ICMS não será considerado. O valor será composto pelo:

"Valor das Despesas Aduaneiras + Vlr.PIS Importação + Vlr.COFINS Importação" do item.

**As informações completas sobre a função e influência de cada um desses parâmetros citados deverão ser verificados no artigo** [Central de Compras | Grade Itens > Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974-Central-de-Compras-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es).

**Nota:** A combinação de configuração dos parâmetros mencionados acima não segue um único "padrão", pois existem diversas maneiras de configurar a rotina, que variam conforme o processo de cada cliente.

**![Imagem 7: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/17371087168279) OBSERVAÇÕES:**

- Se os valores não vierem informados por item na DI, faça os cálculos e lance o proporcional em cada item;
- As opções de proporcionalização de impostos, em despesas acessórias, da aba **"Despesas acessórias",** do cadastro da TOP, devem estar desmarcadas e a TOP deve estar configurada com a opção de **"Não calcula e Digita",** na parte de impostos;
- Isto porque todos os impostos serão digitados pelo usuário ou importados automaticamente utilizando o arquivo XML no padrão da NF-e (enviado pelo despachante);
- Valor do destaque - o ICMS - PIS - COFINS = Despesa Aduaneira na DI
