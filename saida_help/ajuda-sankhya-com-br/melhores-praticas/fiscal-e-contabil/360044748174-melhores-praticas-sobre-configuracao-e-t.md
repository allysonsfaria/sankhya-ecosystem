---
id: "360044748174"
titulo: "Melhores Práticas sobre Configuração e transmissão de Informação de Processos Judiciais - EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044748174-Melhores-Pr%C3%A1ticas-sobre-Configura%C3%A7%C3%A3o-e-transmiss%C3%A3o-de-Informa%C3%A7%C3%A3o-de-Processos-Judiciais-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:33:26Z"
rotulos: ["#criadoRoger", "Configuração", "Fiscal", "Impostos", "avulsa", "EFD Contribuições", "Nova funcionalidade inclui processos judiciais no EFD Contribuições para dedução de ICMS.", "Registros como A170 C170 C175 e outros devem referenciar processos judiciais.", "Cadastrar processos e gerar registros 1010 e 1011 no sistema.", "Processos Judiciais"]
---

# Melhores Práticas sobre Configuração e transmissão de Informação de Processos Judiciais - EFD Contribuições

Abaixo descrevo a funcionalidade criada para a informação do processo judicial vinculada à dedução/exclusão da base de cálculo do ICMS, conforme guia prático do EFD Contribuições.

Como vem sendo uma prática das Empresas o pleito da redução do ICMS na base de cálculo do PIS e COFINS a RFB para ter o controle do que esta embasando esta dedução perante as Empresas, esta promoveu alterações no layout do EFD afim de obrigar que seja informado qual processo Judicial a Empresa/contribuinte se amparou para efetuar tal operação, assim se a Empresa possui esta prática, poderá agora no Sistema para o novo layout gerar estas informações.

**Todos os registros de movimentações envolvidos:**

**BLOCO A** - Documentos Fiscais - Serviços (ISS)

"A170"

**BLOCO C** - Documentos Fiscais I – Mercadorias (ICMS/IPI)

"C170", "C175", "C181/C185", "C381/C385", "C481/C485", "C601/C605", "C870"

**BLOCO D** - Documentos Fiscais II – Serviços (ICMS)

"D201/D205", "D300", "D350", "D601/D605"

**BLOCO F** - Demais Documentos e Operações

"F100", "F500" e "F550"

**BLOCO P** - Apuração da Contribuição Previdenciária sobre a Receita Bruta

"P100"

Desta forma quando for configurada a nova funcionalidade de informação de processos judiciais, os registros filhos responsáveis por gerar esta informação no EFD Contribuições serão gerados conforme vinculação abaixo: 

| REGISTRO DE MOVIMENTO | REGISTRO DO PROCESSO |
| --- | --- |
| A170 - Complemento do Documento - Itens do Documento | A111 - Processo Referenciado |
| C170 - Complemento do Documento - Itens do Documento (Códigos 01, 1B, 04 e 55) | C111 - Processo Referenciado |
| C175 - Registro Analítico do Documento (Código 65) | C111 - Processo Referenciado |
| C181/C185 - Detalhamento da Consolidação – Operações de Vendas – PIS e COFINS | C188 - Processo Referenciado |
| C481/C485 - Resumo Diário de Documentos Emitidos por ECF – PIS/COFINS (Códigos 02 e 2D) | C489 - Processo Referenciado |
| C601/C605 - Complemento da Consolidação Diária (Códigos 06, 28 e 29) – Docs de Saídas - PIS/COFINS | C609 - Processo Referenciado |
| C870 - Resumo Diário de Documentos Emitidos por Equip SAT-Cf-e (Código 59) – PIS/Pasep e COFINS | C890 - Processo Referenciado |
| D201/D205 - Totalização do Resumo Diário – PIS/COFINS | D209 - Processo Referenciado |
| F100 - Demais Documentos e Operações Geradoras de Contribuição e Créditos | F111 - Processo Referenciado |
| F500 - Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da COFINS pelo Regime de Caixa | F509 - Processo Referenciado |
| F550 - Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no  Lucro Presumido – Incidência do PIS/Pasep e da COFINS pelo Regime de Competência | F559 - Processo Referenciado |
| P100 - Contribuição Previdenciária sobre a Receita Bruta | P199 - Processo Referenciado |

**Observações:**

- Todos os registros, exceto o P100 mostram os processos para PIS e COFINS
- O registro P199 mostra somente os processos dos impostos INSS e CPRB

Após os cadastros dos processos na nova tela que veremos a seguir, definindo as configurações/vinculações necessárias, ao ser efetuada a geração do EFD Contribuições os registros informados acima, caso se enquadrem e possuam seus respectivos processos, então serão gerados. Além disto, será gerado um registro 1010 com o detalhamento  do processo judicial (vejam a tela a seguir com os detalhes / campos necessários):

**CADASTRANDO OS PROCESSOS JUDICIAIS:**

Caminho: Menu Livros Fiscais >> Arquivos >> Processos administrativos Judiciais

![Imagem 1: Caminho: Menu Livros Fiscais >> Arquivos >> Processos administrativos Judiciais](https://ajuda.sankhya.com.br/hc/article_attachments/360061436754)

Indicando os impostos e demais filtros:

![Imagem 2: Indicando os impostos e demais filtros:](https://ajuda.sankhya.com.br/hc/article_attachments/360062338233)

Além da aba “Empresa” e “Impostos” não é obrigatório informar dados nas demais abas, apenas se for necessário delimitar / filtrar mais a aplicação da regra para gerar os processos vinculados.

Após configurado/ cadastrado o(s) processo(s), deverá ser gerado o EFD Contribuições normalmente.

**Importante**: Deverá ser cadastrado o registro 1010 do EFD contribuições e marcado para ser gerado caso não esteja cadastrado/configurado.

Caminho: Acessar as preferências da Empresa, aba EFD – Escrituração Fiscal Digital >> Escolher no tipo de escrituração “EFD Contribuições”.

Exemplo do arquivo do EFD Contribuições gerado com registros dos processos vinculados:

![Imagem 3: Exemplo do arquivo do EFD Contribuições gerado com registros dos processos vinculados:](https://ajuda.sankhya.com.br/hc/article_attachments/19257865678871)

**Importante**: A informação do processo judicial por esta funcionalidade não desobriga o usuário / contribuinte a efetuar as devidas configurações e registros das observações se for o caso nos Notas fiscais de origem que posteriormente serão escriturados no EFD. Esta funcionalidade visa atender a geração apenas no EFD Contribuições.

**Observações**
![Imagem 4: Observações A geração das informações de processos esta preparada apenas para processos de origem “Federal”, desta…](https://ajuda.sankhya.com.br/hc/article_attachments/19257865685655) A geração das informações de processos esta preparada apenas para processos de origem “Federal”, desta forma na tela de processos no campo “Origem do Processo (EFD Contrib)” deverá ser = “1-Justiça Federal”

![Imagem 5: Como esta nova tela poderá ser utilizada para informar os processos judiciais tanto do EFD Contribuições como do EFD…](https://ajuda.sankhya.com.br/hc/article_attachments/19257854482839) Como esta nova tela poderá ser utilizada para informar os processos judiciais tanto do EFD Contribuições como  do EFD REINF deverão ficar atentos aos campos que são necessários para cada uma das obrigações e nem sempre necessário informar todos os dados da tela.

![Imagem 6: A funcionalidade não se baseia em cálculos da base de ICMS, se for o caso o usuário deverá fazer a configuração dos…](https://ajuda.sankhya.com.br/hc/article_attachments/19257854486935) A funcionalidade não se baseia em cálculos da base de ICMS, se for o caso o usuário deverá fazer a configuração dos processos judiciais que amparam esta ação.

**Embasamento (exemplo de um dos registros) no guia prático conforme o registro C100 e filhos:**

**"Observação Importante:** No caso da exclusão da base de cálculo das contribuições ser decorrente de decisão judicial beneficiando e alcançando a pessoa jurídica, decisão esta já aplicável e alcançando o período de apuração a que se refere esta escrituração, deve ser obrigatoriamente escriturado o Registro "C111 - Processo Referenciado", bem como o correspondente registro de detalhamento do processo judicial, no Registro "1010 - Processo referenciado - Ação Judicial".

Este procedimento deve ser adotado pela pessoa jurídica beneficiária ou autora de ação judicial, com sentença favorável à exclusão de impostos incidentes na operação de venda de bens e serviços, destacados no documento fiscal, na determinação da base de cálculo da Contribuição para o PIS/Pasep, da COFINS e/ou da CPRB. Importante ressaltar que estas exclusões na base de cálculo, decorrentes de decisões judiciais, só são aplicáveis se não houver limitação temporal dos efeitos da sentença judicial em relação ao período da escrituração, ou seja, faz-se necessário que a decisão judicial já seja aplicável em relação aos fatos geradores a que se refere a escrituração"

![Imagem 7: A funcionalidade não se baseia em cálculos da base de ICMS, se for o caso o usuário deverá fazer a configuração dos…](https://ajuda.sankhya.com.br/hc/article_attachments/19257854494615) A funcionalidade não se baseia em cálculos da base de ICMS, se for o caso o usuário deverá fazer a configuração dos processos judiciais que amparam esta ação.

**Registro 1011 - Detalhamento das Contribuições com Exigibilidade Suspensa - EFD Contribuições**

Inicialmente esse registro será gerado somente se o registro C111 for gerado, ou seja, os dados gerados terão base nos registro C100 e C170 que originou o registro C111.

Os dados informados no registro 1011 dizem respeito às informações de PIS e COFINS do item. 
Novo campo na tela Processos Administrativos Judiciais onde o usuário poderá informar a descrição complementar que será enviada no registro 1011 do EFD Contribuições
![Imagem 8: Os dados informados no registro 1011 dizem respeito às informações de PIS e COFINS do item. Novo campo na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/19257865704599)

Exemplo arquivo txt do EFD Contribuições gerado.

**#Bloco C**
|C001|0|
|C010|00000000000005|2|
|C100|1|0|000032207|55|00|1|54013|42191194234275001024550010000540134035600915|01012020|01012020|1335000,00|0|0,00|0,00|1335000,00|0|0,00|0,00|0,00|1335000,00|226950,00|0,00|0,00|0,00|18282,83|84211,80|0,00|0,00|
|C111|5012769-50.2017.4.04|1|
|C170|1|1035801||6000,00000|FR|1335000,00|226950,00|0|000|5102|418|1335000,00|17,00|226950,00|0,00|0,00|0,00|0|99|||||01|1108050,00|1,6500|||18282,83|01|1108050,00|7,6000|||84211,80|3.01.01.001.0001|
|C990|6|

**#Bloco 1**
|1001|0|
|1010|5012769-50.2017.4.04|PORTO ALEGRE / RS|13|03||17072017|
|1011|C170|42191194234275001024550010000540134035600915|000032207|1035801|01012020|1335000,00|01|1335000,0000|1,6500|22027,50|01|1335000,0000|7,6000|101
