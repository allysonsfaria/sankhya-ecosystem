---
id: "360044609574"
titulo: "Importação de Dados Coletor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609574-Importa%C3%A7%C3%A3o-de-Dados-Coletor"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-07-29T14:48:59Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "WMS", "Importação de Dados Coletor", "LIFETEMPFILE", "br.com.sankhya.mgeinvent.importacao.dados.coletor", "Importação de Dados Coletor manual", "Importação", "Estoque", "Leitura Arquivos: Contagem estoque layout definido.", "Revisão Importação: Correção log rollback", "Modelos Arquivos: Modelos 1 2 3"]
---

# Importação de Dados Coletor

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312596710807) Módulo: Inventário > Avançado
```

---

Nesta tela, efetue a leitura de arquivos indicados pelo usuário, com layout definido para fazer a contagem do estoque.

![Imagem 2: Nesta tela, efetue a leitura de arquivos indicados pelo usuário, com layout definido para fazer a contagem do estoque.](https://ajuda.sankhya.com.br/hc/article_attachments/360081996914)

Preencha no campo **"Data Contagem"** a data em que a contagem de estoque foi realizada.

Em **"Arquivo de Origem"**, defina o arquivo no qual será feita a leitura dos produtos.

**Observação:** os arquivos importados devem ter o charset definido como UTF-8.

**Nota:** o formato do arquivo utilizado pelo sistema será o txt.

Determine no campo **"Modelo de Arquivos"** o modelo a ser utilizado na contagem.

Caso seja feita a escolha dos modelos **"Modelo 1"** e **"Modelo 2"**, os campos **"Empresa"** e **"Local"** serão habilitados para preenchimento.

A marcação **"Confirma contagem correta quando existirem erros"** ao efetuar a Contagem de Estoque, se marcada, irá efetuar a contagem com a série que não houve problemas e apresentará no log somente as séries que tiveram problemas; se desmarcada o sistema não irá efetuar a contagem mesmo que a série não possua problemas, pois uma vez identificado o problema em uma série do arquivo o sistema irá desfazer todo o processo.

A opção **"Somar quantidades em contagens da mesma data"** quando acionada, na importação de vários arquivos com uma mesma data onde algum produto se repita, ao invés de criar uma nova contagem com uma nova sequencia o sistema irá agregar na quantidade contada à contagem já existente.

Ao clicar no botão **"Importar"**, o arquivo indicado será lido e os códigos contados na tabela de contagem.

O Modelo 1 e Modelo 3 realizam a contagem pelo código de barras na tabela de contagem do estoque (TGFCTE) e o Modelo 2 efetua a contagem de estoque por série na tabela (TGFCTS).

**Importante:** se importado um arquivo sem erros mais de uma vez, a quantidade da contagem será adicionada a já existente; essa adição a contagem já existente irá ocorrer para as opções Modelo 1 e Modelo 3.

Para o Modelo 2, se já existir contagem para um determinado produto e série, o sistema não irá contar, pois para produtos com série, só podem haver uma unidade.

Caso ocorram inconsistências com os produtos lidos, um arquivo de log será gerado e nada será gravado, ou seja, o sistema dará um roll back na transação (esta será desfeita) e será apresentada na tela uma janela com o resultado da importação do arquivo e um botão de **"Download"** para salvar o arquivo de log na máquina. O arquivo de log ficará na sessão do navegador do usuário por um determinado tempo, porém, se o arquivo não for salvo para a máquina, o mesmo irá expirar e o usuário deverá realizar a importação novamente para geração do arquivo de log. O tempo que o arquivo de log ficará na sessão do usuário, depende da configuração realizada no parâmetro **"Tempo (em minutos) de vida p/ arquivos temporários - LIFETEMPFILE"**.

No Sankhya-Om pode-se ler 3 (três) layout's de arquivos:

**1) Modelo 1**

Layout: 99999,999

Exemplo: 80003,1

            80017,2

            80022

Serão lidos um ou dois campos separados por vírgula, onde o primeiro se refere a um código de barras e o segundo a quantidade contada. Caso a linha do arquivo não possua o segundo campo, o sistema irá contar como quantidade zero. Para que o código de barras indicado seja contado, será necessário que o código de barras inserido no arquivo esteja no cadastro do produto no campo **"Referência"** ou na tabela de volume alternativo no campo **CODBARRA**.

Será gerada a contagem na tabela TGFCTE da seguinte forma:

- DTCONTAGEM – Data da contagem indicada na tela
- CODPROD – Código do produto encontrado no cadastro de produto
- CODEMP – Código da empresa indicado na tela
- CODLOCAL - Código do local indicado na tela
- CONTROLE – Espaço em branco ou 99999999, caso o código de barras seja 99999999.
- CODVOL – Código de volume encontrado no cadastro de produto
- QTDEST – Quantidade indicada no arquivo, ou zero quando não indicado.

Caso o código de barras do arquivo seja diferente do campo **"Referência"** do cadastro do produto, o código do volume será encontrado na tabela de volume alternativo.

Se já existir uma contagem com a mesma data, produto, empresa, local, controle e volume a quantidade será somada a existente.

**Importante:** pode-se trabalhar com a importação dos arquivos do Modelo 1 também no seguinte formato:

<EAN13>,<QTD>,<\*DTVAL>,<\*DTFAB>

DTVAL = Data de validade no formato DDMMAAAA

DTFAB = Data de fabricação no formato DDMMAAAA

\* As datas de validade e fabricação são campos opcionais.

Vejamos alguns exemplos de registros válidos:

7894900531008,0104

7894900531008,0107,01012018,01012017

7894900531008,0120,01012017

**2) Modelo 2**

Layout: 999999999999

Exemplo: 120000006664

            120000006748

            120000014825

Onde cada linha do arquivo é um número de série e a quantidade contada é um. Para que o número de série indicado seja contado, será necessário que o número de série inserido no arquivo esteja no cadastro de séries (TGFSER), com a máxima nota e na empresa indicada no campo **"Empresa"** desta tela.

Será gerada a contagem na TGFCTS da seguinte forma:

- DTCONTAGEM – Data da contagem indicada na tela
- TIPCONTAGEM – Tipo "C" - contagem
- CODPROD – Encontrada na tabela de série (TGFSER)
- CODEMP – Código da empresa da tela
- CODLOCAL - Código do local da tela
- ESTOQUE – Quantidade um se for contagem nova.

Se já existir uma contagem com a mesma data, tipo, produto, empresa, local será somada a existente.

**3) Modelo 3**

Layout: EEELLLCCCCCCCCCCCCCCCCCQQQQQQQQQ

           EEE                                - 01 a 03 EMPRESA

           LLL                                - 04 a 06 LOCAL

           ccCCCCCCCCCCCCCCC        - 07 a 23 CODIGO DE BARRA sendo que os 2 primeiros é o controle.

           QQQQQQQQQ                - 24 a 32 QUANTIDADE

Exemplo: 01101112000000000000501000000002

            00100052000000000080018000000001

Para que o código de barras indicado seja contado, será necessário que o código de barras inserido no arquivo esteja no cadastro de estoque no campo CODBARRA.

Será gerada a contagem na TGFCTE da seguinte forma:

- DTCONTAGEM – Data da contagem indicada na tela
- CODPROD – Código do produto encontrado no cadastro de estoque
- CODEMP – Código da empresa do arquivo
- CODLOCAL - Código do local do arquivo
- CONTROLE – Controle do cadastro de estoque.
- CODVOL – Código de volume encontrado no cadastro de produto
- QTDEST – Quantidade indicada no arquivo, ou zero quando não indicado.

Se já existir uma contagem com a mesma data, produto, empresa, local, controle e volume a quantidade será somada a existente.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609574-Importa%C3%A7%C3%A3o-de-Dados-Coletor#top)
