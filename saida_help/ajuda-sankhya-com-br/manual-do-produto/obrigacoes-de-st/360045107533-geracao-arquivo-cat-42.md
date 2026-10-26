---
id: "360045107533"
titulo: "Geração Arquivo CAT 42"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Obrigações de ST"
atualizado_em: "2026-09-15T17:21:13Z"
rotulos: ["AJUDA DO SKW", "manual", "br.com.sankhya.mgeliv.mov.geracaoarquivocat42", "Geração Arquivo CAT 42 manual", "Configuração", "Livros Fiscais", "SEFAZ", "Estoque", "Incluem R0000 R0150 R0200 R1050 R1100 R1200", "Demonstrar valores de ICMS ST na CAT 42/2018", "Ajustes para cálculo filtragem e validação de dados", "ICMS ST", "Obrigação Acessória", "CAT 42"]
---

# Geração Arquivo CAT 42

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42313071815703) Módulo: Livros Fiscais > Conexão
```

---

A obrigação acessória CAT 42/2018 foi criada pelo Estado de São Paulo e tem como objetivo demonstrar os documentos e valores relacionados à apuração do ressarcimento e/ou complemento referente à diferença dos valores apresentados na Apuração de ICMS ST. Desta forma, utiliza-se esta rotina para realizar a geração da obrigação acessória.

Serão apresentadas aqui todas as notas que compõem o ressarcimento de ST juntamente com seus respectivos valores e itens para facilitar a validação das informações.

| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#painelprincipal) |  | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abageral) |
| --- | --- | --- |
| [Aba R0000](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar0000) |  | [Aba R0150](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar0150) |
| [Aba R0200](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar0200) |  | [Aba R1050](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar1050) |
| [Aba R1100](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar1100) |  | [Aba R1200](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar1200) |
| [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#botesnotopodatela) |  | [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#botooutrasopes...) |
| [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#parmetrosqueinfluenciamnestarotina) |  |  |

**Importante:** antes de iniciar a geração da CAT 42 será necessário realizar a [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514-C%C3%B3pia-de-Estoque), visto que, é de acordo com as informações relacionadas nesta cópia que serão efetuados os cálculos dos saldos iniciais listados no arquivo.

## Painel Principal

Localizado no alto da tela, o Painel Principal agrupa os dados que servirão de base para todo o restante da Geração do Arquivo CAT 42.

![CAT02](https://ajuda.sankhya.com.br/hc/article_attachments/360060981654)

O campo **"Finalidade de Apresentação do Arquivo"** possui 3 opções:

- **0 - Remessa regular de arquivo:** Esta opção deverá ser selecionada quando tratar-se do arquivo enviado todos os meses.
- **1 - Remessa de arquivo requerido por intimação específica:** Deve-se utilizar esta opção quando por algum motivo o fisco solicitar o envio das informações fora da data definida para entrega da obrigação.
- **2 - Remessa de arquivo para substituição de arquivo remetido anteriormente:** Seleciona-se esta opção quando for necessário reenviar o arquivo da referência por alguma inconsistência nas informações.

Quando a marcação **"Arquivo Confirmado?"** estiver realizada tem-se que as informações geradas já encontram-se disponíveis para serem consolidadas no arquivo que, posteriormente, terá sua estrutura validada no programa de validação disponibilizado pela SEFAZ.

Habilita-se a marcação **"Tem divergência?"** quando, após o processamento das informações para geração da obrigação acessória, são apresentadas divergências nas mesmas.

**Nota:** a marcação acima apenas será desabilitada quando os produtos com divergências forem ajustados ou retirados da movimentação do período.

Quando a marcação **"Considerar filtro nativo?"** estiver habilitada, os produtos que possuírem as configurações abaixo não serão gerados na CAT 42:

1)O campo **"Tipo"** configurado com a opção **"Não tem"** ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-#abaimpostosinformaesporempresa));

2)O campo **"Tipo de substituição"** configurado com a opção "Não tem" (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostos));

3)O campo **"Usado como"** configurado com as opções **"Consumo"**, **"Brinde" e "Brinde (NF)"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral)).

A marcação **"Considerar marcação no produto?"** possui relação com a marcação **"Considerar produto na geração da Cat 42"** localizada no Cadastro de Produtos, aba Impostos. Desta forma, ao utilizar esta marcação, o sistema considerará para realizar o processamento de informações apenas estes produtos.

Em relação à marcação **"Considerar marcação no grupo de produto?"**, esta também possui vinculo com a marcação Considerar produto na geração da Cat 42 localizada no Cadastro de Produtos, aba Impostos, porém, o sistema irá considerar para a realização do processamento de informações apenas os produtos que encontram-se vinculados à este grupo.

No campo **"Tipo de Apuração"** estão disponíveis as formas de apuração suportadas pela rotina, sendo elas:

- **1 - Rastreamento de Estoque:** Esta opção deverá ser utilizada pelas empresas que já realizam o rastreamento de estoque de seus produtos para geração das informações nas tag's do Grupo de ICMS 060;
- **2 - Notas p/ Ressarcimento de ST (Digitadas no Livro):** Utilizam esta opção as empresas que executam o vínculo de suas notas de entradas com suas notas de saídas através da tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI), aba [Notas p/ Ressarcimento de ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI#abanotaspressarcimentodest);

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Aba Geral

![CAT03](https://ajuda.sankhya.com.br/hc/article_attachments/360060981674)

O campo **"Filtro Personalizado"** disponível nesta aba, tem como finalidade a criação de algum tipo de restrição para buscar produtos específicos na geração da CAT 42.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Aba R0000

![CAT04](https://ajuda.sankhya.com.br/hc/article_attachments/360061911573)

Na aba do **"Registro 0000 - Abertura do Arquivo Digital e Identificação do Contribuinte"** serão inseridas as informações cadastrais da Empresa que está gerando o arquivo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Aba R0150

![CAT05](https://ajuda.sankhya.com.br/hc/article_attachments/360061911593)

Tem-se nesta aba as informações referentes ao **"Registro 0150 - Tabela de Cadastro do Participante"**. Neste registro deverão ser inseridos os registros cadastrais dos Parceiros que participaram das movimentações de mercadoria com a empresa geradora no período da geração do arquivo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Aba R0200

![CAT06](https://ajuda.sankhya.com.br/hc/article_attachments/360061911613)

O **"Registro 0200 - Tabela de Identificação do Item"** tem por objetivo informar as mercadorias, serviços, produtos ou quaisquer outros itens referentes às transações comerciais praticadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Aba R1050

![Imagem 7: Aba R1050](https://ajuda.sankhya.com.br/hc/article_attachments/360101630493)

O registro **"1050 - Registros de Saldos em Estoque da CAT 42"** tem como finalidade realizar a apuração do estoque inicial e final do período de geração do arquivo e também o Saldo Inicial e Final do ICMS Suportado do item.

Esse registro dispõe de 6 campos quando gerados no arquivo TXT conforme detalhado abaixo:

1050|46733139000|10,000|21,00|10,00|21,00

**1050:** Na geração do TXT, conterá o texto fixo contendo **"1050"** (Campo 01).

**Cód. Item:** Este refere-se ao Código do item (Campo 02) conforme Registro 0200.

**Qtd. Inicial:** Neste (Campo 03), conterá a informação da quantidade inicial do estoque do item no início do primeiro dia do período. Referente ao preenchimento desse campo, teremos que na geração da primeira CAT 42 do sistema, esse estoque inicial será referente a cópia ou contagem de estoque do último dia do mês anterior ao período de geração do arquivo. Teremos o exemplo:

Se a primeira geração CAT 42 no sistema ocorrer no período de 01/01/2019 a 31/01/2019, dessa forma, o sistema irá adotar o estoque inicial conforme configurado na cópia ou contagem do dia 31/12/2018.

**Observação:** o sistema buscará as notas relacionadas ao estoque inicial, de acordo com as seguintes configurações:

- Se nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), o campo **"Rastreamento de Estoques"** estiver com a opção **"Rastrear Doc. Fiscais"** selecionada, o sistema só buscará as notas de entrada para amparar o estoque inicial, quando o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) do lançamento estiver configurado para atualizar livro fiscal (aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal), campo **"Atualização de Livro ICMS"**, opção **"Livro de entrada"**) e estoque de entrada (aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque), campo **"Atualização de Estoque"**, opção **"Entrar"**).
- Caso o campo Rastreamento de Estoques, da tela mencionada anteriormente, esteja selecionado com a opção **"Rastrear Doc. Fiscais e Não Fiscais"**, o sistema buscará as notas de entrada que não atualizam livro fiscal ou estoque, desde que, o parâmetro **"Utiliza Doc. não fiscais no Rast. Est.? - DOCNFISCRASTST"** esteja ligado e a TOP utilizada no lançamento esteja informada no parâmetro **"Lista de TOP Entrada no rastr. de Doc. Não Fiscais - TOPENTNFISRAST"**.

**Vlr. ICMS + ST Inicial:** Neste campo (Campo 04) será registrado o valor inicial acumulado do total de ICMS suportado pelo contribuinte, relativo ao item no início do primeiro dia do período.

**Qtd. Final:** Neste (Campo 05), será registrado a quantidade do saldo final do estoque do item no final do último dia do período.

**Vlr. ICMS + ST Final:** Tem-se nesse (Campo 06), o Valor final acumulado do total do ICMS suportado pelo contribuinte, relativamente ao item, no final do primeiro dia do período.

**Sub-aba Notas q/ Amparam Estoque**

![Imagem 8: Sub-aba Notas q/ Amparam Estoque](https://ajuda.sankhya.com.br/hc/article_attachments/360099504914)

A sub-aba **"Notas q/ Amparam Estoque"** da aba R1050 tem a finalidade de exibir todas as notas de entrada que amparam o estoque inicial da CAT 42 (campo **"Qtd. Inicial"**) e as notas de entrada do período de geração do arquivo.

**Observação:** esta sub-aba não gera nenhuma informação para a CAT 42, servindo apenas para conferência de valores.

Temos os seguintes campos disponíveis nesta sub-aba:

No campo **"Nro. Único da Nota"** teremos o número único da nota de entrada.

O campo **"Sequência"** é preenchido com o número de sequência do lançamento do item.

No campo **"Quantidade"** temos a quantidade que foi utilizada do item da nota no rastreamento de estoque.

O campo **"Tributação"** é preenchido com o CST de ICMS do lançamento do item.

Teremos também, no campo **"Base do ST"**, o valor da base do ST do item, proporcional à quantidade.

O valor informado no campo **"Vlr. ICMS + ST"** compreende a soma do Vlr. ICMS com o ST do item.

Nos campos **"Vlr. ST"** e **"Vlr. ICMS"** teremos o valor total do ST e ICMS do item, respectivamente.

O campo **"Base do ST Unitário"** terá o valor da base de ST unitária do item.

No campo **"Vlr. ICMS + ST Unitário"** teremos o valor do ICMS + ST unitário do item.

**Nota:** este campo será a soma dos valores do ICMS e do ST do lançamento da nota de entrada, neste caso, quando não há um valor de ST, o sistema preencherá o referido campo com o valor do ICMS.

Nos campos **"Vlr ST Unitário"** e **"Vlr ICMS Unitário"** temos o valor do ST e ICMS unitário do item, respectivamente.

O campo **"Tipo de Movimento"** trará o tipo de movimentação da TOP do lançamento de entrada do item.

Teremos o campo **"Dt Entrada Mercadoria"**, que exibirá a data de entrada da mercadoria do lançamento do item.

Por fim, o campo **"Vlr. ST Unitário"** desta tela, realizará o cálculo: VLR. SUBS UNIR - VLR ICMS UNIT, e no campo **"Vlr. ST"**, o cálculo será realizado da seguinte forma: VLRSUBST - VLR ICMS, para que assim, seja possível fazer a validação dos impostos gerados pelo sistema e confrontar com as notas de saída no registro **"R1100"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Aba R1100

Esta aba trata do **"Registro 1100 - Registro de Documento Fiscal Eletrônico para Fins de Ressarcimento de Substituição Tributária ou Antecipação"** e tem como finalidade listar as notas que enquadram-se às regras de ressarcimento.

![CAT08](https://ajuda.sankhya.com.br/hc/article_attachments/360061911633)

**Observação:** tem-se no botão Outras Opções... desta aba e da aba [R1200](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar1200) a opção **"Abrir Documento (Ctrl + K)"** que, ao ser acionada, abrirá a Central de Notas a partir de uma nota selecionada.

Referente ao campo **"Valor de Confronto"**, este terá cálculos que diferem-se de acordo com a opção selecionada no campo **"Cód. de Enquadramento Legal"**, sendo assim vejamos:

- Venda

Caso o Enquadramento selecionado neste campo seja os códigos **"1 - Operação ensejadora de Ressarcimento ou Compl. de ICMS-ST - inciso I Art. 269 RICMS"** ou **"3 - Operação ensejadora de Ressarcimento ICMS-ST - Inciso III Art. 269 RICMS"**, o valor incluído no campo **"vlr. Confronto das Operações"** deverá corresponder ao valor do produto da multiplicação da alíquota interna da mercadoria.

Se o enquadramento selecionado for **"2 - Operação ensejadora de Ressarcimento ICMS-ST - Inciso II Art. 269 RICMS"**, tem-se então que o valor inserido no campo Vlr. Confronto das Operações será o valor do ICMS da operação própria, do sujeito passivo por substituição do qual a mercadoria tenha sido recebida diretamente ou cobrado na operação interestadual anterior.

Tem-se ainda que em caso de antecipação, ou em que o valor do ICMS que seria atribuído à operação própria do contribuinte substituído sendo que a mercadoria tenha sido recebida, e estivesse submetida ao regime comum de tributação.

**Observação:** para este, quando aplicável, deve-se consultar o artigo 271 do RICMS.

- Devolução de Venda

Caso o enquadramento selecionado seja o **"1 - Operação ensejedora de Ressarcimento ou Compl. de ICMS-ST - Inciso I Art. 269 RICMS"** ou **"3 - Operação ensejedora de Resarcimento ICMS-ST - Inciso III Art. 269 RICMS"** o valor a ser inserido no campo Vlr Confronto das Operações deverá ser correspondente ao valor da multiplicação da alíquota interna da mercadoria.

Através da sub-aba **"Ligação entre as notas de saída e entrada"** você consegue visualizar as notas de entrada que estão ligadas com as saídas geradas pelo sistema, podendo validar os campos **"Vlr. p/ atualizar saldo"** e **"Vlr. Confronto das Operações"** da aba R1100.

**Nota:** no botão ![Imagem 10: Nota: no botão "Outras Opções..." dessa sub-aba, temos a opção "Abrir Documento (Ctrl + K)" , que permite que você veja…](https://ajuda.sankhya.com.br/hc/article_attachments/16310962859671) **"Outras Opções..."** dessa sub-aba, temos a opção **"Abrir Documento (Ctrl + K)"**, que permite que você veja diretamente o lançamento de entrada.

Os campos 09 - ICMS\_TOT, 10 - VLR\_CONFR e 11 - COD\_LEGAL do registro R1100, buscarão as informações contidas nos campos **"Vlr. p/ atualizar saldo"**, **"Vlr. Confronto das Operações"** e **"Cód. Enquadramento Legal"** dessa aba, respectivamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Aba R1200

![CAT09](https://ajuda.sankhya.com.br/hc/article_attachments/360061911653)

Nesta aba insere-se informações referentes ao **"Registro 1200 - Registro de Documento Fiscal Não-Eletrônico para Fins de Ressarcimento de Substituição Tributária - SP"**.

Referente ao campo **"Valor de Confronto"**, este terá cálculos que diferem-se de acordo com a opção selecionada no campo **"Cód. de Enquadramento Legal"**, sendo assim vejamos:

- Venda

Caso o Enquadramento selecionado neste campo seja os códigos **"1 - Operação ensejadora de Ressarcimento ou Compl. de ICMS-ST - inciso I Art. 269 RICMS"** ou **"3 - Operação ensejadora de Ressarcimento ICMS-ST - Inciso III Art. 269 RICMS"**, o valor incluído no campo **"vlr. Confronto das Operações"** deverá corresponder ao valor do produto da multiplicação da alíquota interna da mercadoria.

Se o enquadramento selecionado for **"2 - Operação ensejadora de Ressarcimento ICMS-ST - Inciso II Art. 269 RICMS"**, tem-se então que o valor inserido no campo Vlr. Confronto das Operações será o valor do ICMS da operação própria, do sujeito passivo por substituição do qual a mercadoria tenha sido recebida diretamente ou cobrado na operação interestadual anterior.

Tem-se ainda que em caso de antecipação, ou em que o valor do ICMS que seria atribuído à operação própria do contribuinte substituído sendo que a mercadoria tenha sido recebida, e estivesse submetida ao regime comum de tributação.

**Observação:** para este, quando aplicável, deve-se consultar o artigo 271 do RICMS.

- Devolução de Venda

Caso o enquadramento selecionado seja o **"1 - Operação ensejedora de Ressarcimento ou Compl. de ICMS-ST - Inciso I Art. 269 RICMS"** ou **"3 - Operação ensejedora de Resarcimento ICMS-ST - Inciso III Art. 269 RICMS"** o valor a ser inserido no campo Vlr Confronto das Operações deverá ser correspondente ao valor da multiplicação da alíquota interna da mercadoria.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Botões no topo da tela

A Geração Arquivo CAT 42 é composta por abas, as quais descrevemos até aqui e também por botões que executam diversas funções dentro desta rotina. Vejamos sobre eles:

| ![CP82](https://ajuda.sankhya.com.br/hc/article_attachments/42313071818007) | **Filtros:** este botão abre o assistente de configuração de filtros personalizados para a tela. |
| --- | --- |
| ![CP72](https://ajuda.sankhya.com.br/hc/article_attachments/42313071819671) | **Modo grade [F6]/Configurar grade:** por meio deste botão, alterna-se a visualização da tela entre modo grade e modo formulário; além disto, configura-se a grade da maneira almejada, ou seja, pode-se selecionar, ordenar ou ocultar as colunas da forma mais confortável para o usuário. |
| ![CP04](https://ajuda.sankhya.com.br/hc/article_attachments/42313054718871) | **Cadastrar Portaria CAT 42 [F8]:** por meio deste botão, tem-se a inicialização da Geração do Arquivo CAT 42. |
| ![CP73](https://ajuda.sankhya.com.br/hc/article_attachments/42313071826455) | **Anterior e Próximo:** tem-se aqui, os botões de navegação entre os registros já cadastrados. |
| ![CP74](https://ajuda.sankhya.com.br/hc/article_attachments/42313071827351) | **Excluir [F9]:** acionando-se este botão, realiza-se a exclusão do registro selecionado na tela. |
| ![CP75](https://ajuda.sankhya.com.br/hc/article_attachments/42313054724119) | **Duplicar:** este botão replica o registro selecionado, criando um novo com as configurações equivalentes àquele primeiramente selecionado. |
| ![CP76](https://ajuda.sankhya.com.br/hc/article_attachments/42313054724759) | Atualizar: por meio deste botão, recarrega-se toda a tela de Geração de Arquivo CAT 42. |
| ![clip9773](https://ajuda.sankhya.com.br/hc/article_attachments/42313054726039) | **Processar:** ao acionar este botão, o sistema processará os documentos e preencherá as tabelas dos registros, mantendo o saldo inicial caso o mesmo já tenha sido calculado. |
| ![clip9769](https://ajuda.sankhya.com.br/hc/article_attachments/42313054727575) | **Gerar Arquivo:** através deste botão, será gerado o arquivo .txt exigido pela Portaria CAT 42.  **Nota:** a primeira geração da empresa exigirá que uma [Cópia do Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514-C%C3%B3pia-de-Estoque) tenha sido realizada. Isto é necessário para que o sistema consiga apurar o saldo inicial dos produtos em estoque. |
| ![CP78](https://ajuda.sankhya.com.br/hc/article_attachments/42313071833495) | **Exportar grade para PDF:** este botão apresenta opções de exportação e visualização das informações da tela. Pode-se **"Exportar para PDF"**, **"Exportar para planilha"** ou **"Exportar para cubo"**. |
| ![CP79](https://ajuda.sankhya.com.br/hc/article_attachments/42313054731671) | **Anexo:** por meio deste botão pode-se anexar qualquer documento que seja relevante para a rotina de Geração do Arquivo CAT 42. |
| ![CP60](https://ajuda.sankhya.com.br/hc/article_attachments/360060981734) | **Outras Opções:** as funcionalidades disponibilizadas por este botão podem ser visualizadas no link [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#botooutrasopes...) |
| ![CP81](https://ajuda.sankhya.com.br/hc/article_attachments/42313071837335) | **Configuração da Tela:** por meio deste botão, pode-se realizar a configuração da tela e suas respectivas abas e campos de forma mais proveitosa e adequada para o usuário. Além disto, será possível determinar como ocorrerá a geração da numeração da tela, seja **"Automática"** ou **"Manual"**. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Botão Outras Opções...

O botão **"Outras Opções..."** é acionado por meio do ícone ![CP60](https://ajuda.sankhya.com.br/hc/article_attachments/360060981734) localizado no alto da tela, conforme mencionado acima; tem-se aqui, as seguintes funcionalidades:

| ![clip9774](https://ajuda.sankhya.com.br/hc/article_attachments/42313054735127) | Esta opção quando acionada irá alterar a marcação **"Arquivo Confirmado?"** localizada no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#painelprincipal). Uma vez que o arquivo foi confirmado, o usuário não poderá mais processar os dados, apenas gerar o arquivo. Desta forma, este botão será útil para que, uma vez entregue o arquivo, os dados não sejam alterados.  **Observação:** apenas os usuários que possuírem permissão para alteração nesta tela (realizada na tela [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos)) poderão utilizar esta opção. |
| --- | --- |
|  |  |

| ![clip9775](https://ajuda.sankhya.com.br/hc/article_attachments/42313071841047) | Esta opção possui a mesma funcionalidade da opção **"Marcar Arquivo como Confirmado"**, mencionada acima. |
| --- | --- |

| ![clip9777](https://ajuda.sankhya.com.br/hc/article_attachments/42313054742167) | Esta opção possui uma funcionalidade similar à do botão **"Processar"** da tela, porém, com uma diferença: esta opção deletará o saldo inicial e irá refazê-lo. |
| --- | --- |

| ![clip9779](https://ajuda.sankhya.com.br/hc/article_attachments/42313054744343) | Através desta opção, calcula-se o saldo inicial do estoque desde que não existe movimentação já gerada. Se houver, será apresentada uma mensagem de que não será possível refazer apenas o saldo da referência pois existem movimentações geradas e, assim, será orientado a utilizar a opção **"Processar e Refazer Saldo"**. |
| --- | --- |

| ![clip9780](https://ajuda.sankhya.com.br/hc/article_attachments/42313054745367) | Se as notas que deveriam amparar o estoque de um produto não possuem o valor de ST ou se o rastreamento foi realizado de forma errada, pode ser que os dados de saldo do produto enviado no [Registro R1050](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar1050) fiquem negativos em algum dos campos do registro. Esta opção deverá ser utilizada nestes casos, visto que o validador da CAT42 não aceita valores negativos nos registros.  **Importante:** uma vez que o usuário descartou algum produto, caso seja acionado o botão Processar novamente, pode ser que alguma movimentação da referência possua o produto descartado, se existir, o produto será inserido novamente nos registros. Contudo, ao finalizar a geração, o sistema verificará se algum produto descartado foi inserido outra vez; caso tenha sido inserido, os registros que apontam para este produto serão deletados da mesma forma que ocorre no descarte do produto. |
| --- | --- |

| ![clip9781](https://ajuda.sankhya.com.br/hc/article_attachments/42313054746775) | Caso o usuário utilize a opção acima mencionada, o backup dos produtos descartados terá sido feito. Portanto, a opção **"Visualizar Produtos Descartados"** apresentará um pop-up com os dados de saldo dos produtos descartados.  **Nota:** os valores dos produtos apresentados serão os mesmos que existiriam na tabela do Registro R1050 se não tivessem sido descartados. |
| --- | --- |

| ![GAC01](https://ajuda.sankhya.com.br/hc/article_attachments/42313054749335) | Esta opção tem a finalidade de percorrer o Registro 1050, buscando por qualquer registro que não possua **"Qtd Final"** mas que tenha um **"Vlr. ICMS Final"** diferente de zero; assim, o Vlr. ICMS Final será zerado e então, será possível consultar os produtos que foram ajustados e os valores anteriores ao ajuste. |
| --- | --- |

| ![GAC02](https://ajuda.sankhya.com.br/hc/article_attachments/42313071855383) | Deve-se acionar esta opção para visualizar os produtos que foram ajustados, bem como seus respectivos valores.  **Observação:** ao acionar esta opção, será aperto o pop-up **"Produtos Ajustados (R1050)"**. |
| --- | --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)

## Parâmetros que influenciam nesta rotina

Com o parâmetro **"Gerar CAT 42 em modo debug? - GERCATMODDEBUG"** habilitado, a geração da CAT 42 irá gravar no log do sistema o passo a passo que está sendo executado durante o processamento; isto será útil para identificar uma possível demora no processamento.

O parâmetro **"Considerar produto apenas se existir compra c/ ST? - GERCATCONSCOMST"** definirá os produtos que serão considerados para processamento do saldo. Caso o parâmetro encontre-se habilitado, apenas produtos amparados por pelo menos uma compra confirmada serão considerados para cálculo/processamento do saldo inicial.

**Nota:** quando este parâmetro estiver desligado, serão considerados todos os produtos que possuem estoque na data da contagem.

Deve-se inserir no parâmetro **"Dt. Inicial de compra confirmada com Subst. Tributária - DTINICOMCONFST"** a data limite para buscar as notas de entrada que amparam o estoque.

O parâmetro **"Gerar informação da empresa no registro R0150 do arquivo da CAT42? - INFEMP150CAT42"** definirá se a empresa será inserida ou não no Registro 0150 da CAT 42. Sendo assim, caso o parâmetro encontre-se desabilitado, a empresa não será incluída no [R0150](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar0150).

Ao habilitar o parâmetro **"Utilizar o CNPJ como COD\_PART no arquivo da CAT42? - CDPARTCNPJCAT42"** tem-se que o COD\_PART será o CNPJ do Parceiro na geração do [Registro 1200](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#abar1200). Por outro lado, quando este encontrar-se desabilitado, será utilizado o Código do Parceiro na geração deste registro.

**Observação:** desta forma, deve-se inserir no campo **"CNPJ / CPF"** da aba R1200 desta tela, o CNPJ ou CPF do Parceiro envolvido e, assim, no momento da geração, o sistema verificará a configuração do parâmetro para inserir as informações no arquivo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107533-Gera%C3%A7%C3%A3o-Arquivo-CAT-42#top)
