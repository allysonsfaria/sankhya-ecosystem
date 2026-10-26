---
id: "42426766603927"
titulo: "Manual Mapa Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426766603927-Manual-Mapa-Fiscal"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Manuais Kolossus"
atualizado_em: "2026-08-03T12:32:38Z"
rotulos: ["asis", "sync_hc", "asis_52941212051475", "sync_hash_0fc8e3ae6a54"]
---

# Manual Mapa Fiscal

Sumário

[O Que Compõe o Módulo?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426766603927-Manual-Mapa-Fiscal#h2130slt5w1um9qasowy1yuuedb1l0tj9z)

Obtendo matriz tributária

[Importação em lote da base de itens para consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426766603927-Manual-Mapa-Fiscal#h2221slt5w2fl1hzbjf1g1v4m7jei8ai)

Consulta em tela

[Informações gerais](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426766603927-Manual-Mapa-Fiscal#h2342slt5w2zdq1quc7o81mapthh19piii1)

[Emitentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426766603927-Manual-Mapa-Fiscal#h2355slt5w35l7h7k9hl15xlm461oaiuhs)

[Destinatário](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426766603927-Manual-Mapa-Fiscal#h2365slt5w3bjj15gf1ns19grtj1jhdsyp)

## Mapa Fiscal

Este Módulo demonstra cenários tributários de acordo com as operações e itens desejados.

A Ferramenta faz atribuição em lote de alíquotas de ICMS, IPI, PIS, COFINS e ICMS-ST (MVA, Convênios e Protocolos), demonstrando também os benefícios do produto ou para operação,  automatizando e facilitando a análise dos tributos incidentes sobre as mercadorias e respectivas operações. 

Os cenários tributários consideram variações comuns nas operações tributárias, como Atividade da empresa, Natureza da Operação, Importação, Exportação, CEST, CFOP, Tributação Diferenciada, Possibilidade de Crédito, operações com consumidor final entre outros. Permitindo gerar relatórios específicos da operação considerando o maior número de detalhes que influenciam a tributação. 

É possível obter relatório com  a correta aplicação de CFOP, CST, alíquota e ainda cálculo dos tributos na operação obtendo o resultado rapidamente. 

A ferramenta permite analisar vários cenários tributários através de um layout específico, ou seja, um arquivo .csv com os dados que influenciam a tributação, ou pode ser criado cenário em tela.   

### O Que Compõe o Módulo?

TELA – HOME- Descrição das funcionalidades do Aplicativo.

TELA-  CONSULTA-  Esta é a área de consulta à  matriz tributária.

TELA – PROCESSOS – Na tela de processos você pode verificar tudo o que importou no módulo matriz de operações tributária e obter o resultado dos arquivos csv. 

 
Obtendo matriz tributária

É possível obter uma matriz tributária analisando vários cenários através de um layout específico, em formato CSV importado na plataforma.

Ou opcionalmente o cenário pode ser cadastrado em tela:

O ideal é realizar cenários de entrada e saída ou operações de venda ou transferência de formas separadas, para melhor performance do resultado.

Os cenário irão retornar exatamente conforme o cenário estipulado em consulta, desta forma é muito importante se atentar para:

CEST: ( Tributação ICMS-ST não retorna sem este código. Opcionalmente realizar consulta em lote para este enquadramento caso ainda não tenha para seu produto)

CFOP: ( Colocar o mais aproximado. Para algumas operações mais particulares este código fará toda diferença no retorno. Exemplos comuns: Combustíveis)

Natureza de operação: 2- Venda ou 1-Compra, por exemplo

CNAE: ( Este código permite uma informação mais adequada da atividade da empresa. Se não souber colocar aproximado na posição do código que se enquadre a sempre)

Tipo de item: De acordo com o Sped-Fiscal exemplo 00 – Mercadoria para Revenda; 04 – Produto Acabado; 08 – Ativo Imobilizado;

As informações acima são vinculadas para retornar os cenários mais exatos possíveis.

Importante: Todas as informações solicitadas no Módulo são de preenchimento obrigatório para obter uma matriz tributária correta. O preenchimento de informação inexata no momento de montar o cenário, pode comprometer o resultado final. Por este motivo sugerimos que o cenário seja feito com o máximo de exatidão possível. Os cenários cadastrados ficam salvos e não precisa refazer as próximas consultas. 

## Importação em lote da base de itens para consulta

A consulta em massa dos cenários tributários, deve ser feita por meio de importação de layout específico, em formato CSV .

Para a consulta é importante se atentar para os campos obrigatórios.

Basta fazer o [download](https://kolossus.asisprojetos.com.br/utils/layout_matriz_de_operacoes_tributarias.csv) e preencher as informações conforme as instruções.

Clique aqui: [Modelo](https://kolossus.asisprojetos.com.br/utils/layout_matriz_de_operacoes_tributarias.csv)

No link a seguir o usuário encontrará orientações para o preenchimento da planilha que será utilizada para consulta.

Deve respeitar os campos obrigatórios, eles são obrigatórios pois influenciam diretamente no tratamento tributário do produto.

Confira também o exemplo de preenchimento. Clique aqui: [Orientação de preenchimento](https://docs.google.com/spreadsheets/d/11oQw-kUOa0pkM8luJFSZt6VForiMu_G8/edit?usp=sharing&ouid=107630366100300172331&rtpof=true&sd=true)

 
Consulta em tela

Para consulta a tributação cadastrando cenário em tela será necessário seguir os passos:

 

Passo 1

Adicionar Item:

 ![Imagem 1: Adicionar Item:](https://ajuda.sankhya.com.br/hc/article_attachments/42426812536471)

Passo 2

Montar o cenário que deseja.

 ![Imagem 2: Montar o cenário que deseja.](https://ajuda.sankhya.com.br/hc/article_attachments/42426766871575)

Todos os campos da tela são editáveis.

Depois de montar cenário:

![Imagem 3: A quantidade de cenários montados aparecerá no botão.](https://ajuda.sankhya.com.br/hc/article_attachments/42426780912919)A quantidade de cenários montados aparecerá no botão. 

## Informações gerais

 ![Imagem 4: Informações gerais](https://ajuda.sankhya.com.br/hc/article_attachments/42426781026071)

 

Tipo de Operação: Saída/Entrada- A ferramenta traz cenário tributário de débito na saída e crédito na entrada.

Consumidor Final: Indique se a saída é para consumidor final

Data: Retornaremos o cenário com a data de vigência escolhida

Natureza da Operação: Esta informação é de suma importância para retorno de um cenário tributário exato, 2- Venda ou 1-Compra, por exemplo;

## Emitentes

 

UF: Informar Estado do Emitente.

CNAE: Informar CNAE do Emitente.  Este código permite uma informação mais exata pela atividade da empresa. Se não souber colocar aproximado na posição do código que se enquadre. Exemplo. A Indústria tem uma posição específica no CNAE.

Regime de ICMS: Informar quando o cenário desejado envolve emitente do Simples Nacional.  Ou regime normal para os demais casos. 

Contribuinte do IPI:  Selecionar quando o Emitente for contribuinte do IPI.

Regime de Pis e Cofins: Cumulativo para Lucro Presumido e Simples Nacional, não cumulativo para Lucro real. 

+ Emitente: É possível realizar cenário para dois ou mais Emitentes.

 Quando for preenchido mais de um emitente o painel será visualizado assim:

![Imagem 5: Quando for preenchido mais de um emitente o painel será visualizado assim:](https://ajuda.sankhya.com.br/hc/article_attachments/42426781121431)

## Destinatário

![Imagem 6: Destinatário](https://ajuda.sankhya.com.br/hc/article_attachments/42426781215767)

![Imagem 7: Destinatário](https://ajuda.sankhya.com.br/hc/article_attachments/42426767426071)

UF: Informar Estado do Destinatário.

CNAE: Informar CNAE do Destinatário.  Este código permite uma informação mais exata pela atividade da empresa. Se não souber colocar aproximado na posição do código que se enquadre. Exemplo. A Indústria tem uma posição específica no CNAE.

Regime de ICMS: Informar quando o cenário desejado envolve emitente do Simples Nacional.  Ou regime normal para os demais casos. 

Contribuinte do IPI:  Selecionar quando o Destinatário for contribuinte do IPI.

Regime de Pis e Cofins: Cumulativo para Lucro Presumido e Simples Nacional. Não cumulativo para Lucro real. 

+ Destinatários: É possível realizar cenário para dois ou mais Destinatários.
