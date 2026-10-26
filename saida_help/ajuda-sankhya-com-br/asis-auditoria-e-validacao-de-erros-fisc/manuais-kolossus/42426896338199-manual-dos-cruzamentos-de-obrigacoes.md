---
id: "42426896338199"
titulo: "Manual dos Cruzamentos de Obrigações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426896338199-Manual-dos-Cruzamentos-de-Obriga%C3%A7%C3%B5es"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Manuais Kolossus"
atualizado_em: "2026-08-03T12:36:49Z"
rotulos: ["asis", "sync_hc", "asis_52941167077651", "sync_hash_69451e43b2e2"]
---

# Manual dos Cruzamentos de Obrigações

## Sumário

[Quais arquivos cruzamos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426896338199-Manual-dos-Cruzamentos-de-Obriga%C3%A7%C3%B5es#h386slt4d370vtglfl06w7tbd1prsc48)

[Como realizar um cruzamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426896338199-Manual-dos-Cruzamentos-de-Obriga%C3%A7%C3%B5es#h422slt4d3fzlm336lfcuuqtdnace3o)

[Agendamento X Automação](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426896338199-Manual-dos-Cruzamentos-de-Obriga%C3%A7%C3%B5es#h453slt4d3npwkwhudlhc6ee1aha30f)

[Função “Agrupamento”](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426896338199-Manual-dos-Cruzamentos-de-Obriga%C3%A7%C3%B5es#h469slt4d3us3n9fn50vvbirj106bj2e)

[Status de Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/42426896338199-Manual-dos-Cruzamentos-de-Obriga%C3%A7%C3%B5es#h486slt4d46nxtd5cr5c4lqrymvbva8)

## Manual dos Cruzamentos de Obrigações

Através dos cruzamentos das obrigações é possível identificar divergências entre os documentos. 

O cruzamento realizado na plataforma compara campos idênticos nas obrigações.

Temos a possibilidade de cruzar notas com as obrigações acessórias, sendo possível identificar se a escrituração foi feita de acordo com as informações do documento, também é possível cruzar o SPED FISCAL com as obrigações estaduais e as GIAs-ST, onde podemos visualizar todos os valores informados em ambas as escriturações e arrumar possíveis divergências, temos também o cruzamento do SPED Fiscal com o SPED Contribuições, que nos ajuda a enxergar possíveis notas faltantes ou valores divergentes e também o cruzamento do SPED Contribuições com a DCTF e o ECAC, amarrando de todos os lados as informações, para que nenhuma informação seja enviada incorretamente.

### Quais arquivos cruzamos

A seguir estão os arquivos que aceitamos e seus determinados formatos.

| | ÍCONE AUDITOR | EXTENSÕES | CLASSIFICAÇÃO | | --- | --- | --- | | CUPOM FISCAL ELETRÔNICO - SAT | .XML | Auditorias | | ECD | .TXT | Auditorias | | ECF | .TXT | Auditorias | | EFD CONTRIBUIÇÕES | .TXT | Auditorias | | LIVRO ELETRÔNICO - DF | .TXT | Auditorias | | NFCe | .XML | Auditorias | | NFe | .XML | Auditorias | | SEF II | .TXT | Auditorias | | SINTEGRA | .TXT | Auditorias | | SINTEGRA - ST | .TXT | Auditorias | | SPED FISCAL | .TXT | Auditorias | | DAMEF vs SPED | - | Cruzamentos | | DCTF vs ECAC | - | Cruzamentos | | DIRF vs DCTF | - | Cruzamentos | | DIRF vs ECAC | - | Cruzamentos | | ECD vs DCTF | - | Cruzamentos | | ECF vs DCTF | - | Cruzamentos | | ECF vs DIRF | - | Cruzamentos | | ECF vs ECD | - | Cruzamentos | | ECF vs SPED FISCAL | - | Cruzamentos | | EFD CONTRIBUIÇÕES vs DCTF | - | Cruzamentos | | EFD Contribuições vs ECD | - | Cruzamentos | | EFD Contribuições vs NFE | - | Cruzamentos | | EFD CONTRIBUIÇÕES vs SPED FISCAL | - | Cruzamentos | | ESOCIAL vs REINF | - | Cruzamentos | | ESOCIAL vs REINF PAINEL | - | Cruzamentos | | SPED FISCAL vs CTE | - | Cruzamentos | | SPED FISCAL vs DCTF | - | Cruzamentos | | SPED FISCAL vs NFE | - | Cruzamentos | | SPED FISCAL vs OBRIGAÇÕES ESTADUAIS | - | Cruzamentos | | SPED vs SEF | - | Cruzamentos | | CTe | .XML | Processamento dos dados para fins de cruzamentos | | DAC-AL | .DAC | Processamento dos dados para fins de cruzamentos | | DAM-AC | .PDF | Processamento dos dados para fins de cruzamentos | | DAM-AM | .PDF | Processamento dos dados para fins de cruzamentos | | DAMEF | .PDF | Processamento dos dados para fins de cruzamentos | | DAPI-MG | .XML | Processamento dos dados para fins de cruzamentos | | DCTF | .DEC | Processamento dos dados para fins de cruzamentos | | DIAP-AP | .PDF | Processamento dos dados para fins de cruzamentos | | DIC-SE | .TXT | Processamento dos dados para fins de cruzamentos | | DIEF-CE | .PDF | Processamento dos dados para fins de cruzamentos | | DIEF-ES | .PDF | Processamento dos dados para fins de cruzamentos | | DIEF-MA | .PDF | Processamento dos dados para fins de cruzamentos | | DIEF-PA | .TXT | Processamento dos dados para fins de cruzamentos | | DIEF-PI | .PDF | Processamento dos dados para fins de cruzamentos | | DIME-SC | .TXT | Processamento dos dados para fins de cruzamentos | | DIRF | .DEC | Processamento dos dados para fins de cruzamentos | | DMA-BA | .TXT | Processamento dos dados para fins de cruzamentos | | DPI-GO | .PDF | Processamento dos dados para fins de cruzamentos | | ECAC | .PDF | Processamento dos dados para fins de cruzamentos | | GIAM-RO | .TXT | Processamento dos dados para fins de cruzamentos | | GIA-MS | .TXT | Processamento dos dados para fins de cruzamentos | | GIA-MT | .XML | Processamento dos dados para fins de cruzamentos | | GIAM-TO | .PDF | Processamento dos dados para fins de cruzamentos | | GIA-PR | .TXT | Processamento dos dados para fins de cruzamentos | | GIA-RJ | .TXT | Processamento dos dados para fins de cruzamentos | | GIA-RS | .TXT | Processamento dos dados para fins de cruzamentos | | GIA-SP | .TXT | .PRF | Processamento dos dados para fins de cruzamentos | | GIM-PB | .TXT | Processamento dos dados para fins de cruzamentos | | GIM-RN | .PDF | Processamento dos dados para fins de cruzamentos | | GIM-RR | .PDF | Processamento dos dados para fins de cruzamentos | | NFe - Cancelada | - | Processamento dos dados para fins de cruzamentos | | OUTRAS OBRIGAÇÕES ESTADUAIS | - | Processamento dos dados para fins de cruzamentos | | PERDCOMP | .PDF | Processamento dos dados para fins de cruzamentos | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Observação: 

PDF

Para os arquivos que será necessário a importação de PDF, aceitamos somente aqueles que são passíveis de captura de informações, PDFs em formato de imagem, não aceitamos. Para validar o arquivo, é bem simples, basta tentar copiar as informações dentro dele, se você conseguir, aceitamos, caso não consiga copiar as informações, é sinal que está em formato de imagem. 

DEC e REC

Não aceitamos arquivos criptografados, deve ser um TXT puro. 

### Como realizar um cruzamento

Para realizar o cruzamento, primeiramente você precisará importar os arquivos, eles poderão ser importados tanto pelo Upload ou pelo nosso programa Importação Automática (Disponível em nossa central de downloads), e depois aguardar o processamento deles Importante: enquanto o arquivo não estiver processado não deve dar andamento em seu cruzamento, pois o resultado será comprometido.

Depois que o processamento for concluído aparecerá o ícone  e você poderá dar andamento em seu cruzamento.

\*\* Para verificar o andamento do processamento você pode acessar o módulo Auditoria e Cruzamentos> Processos. \*\*

![Imagem 1: ** Para verificar o andamento do processamento você pode acessar o módulo Auditoria e Cruzamentos> Processos . **](https://ajuda.sankhya.com.br/hc/article_attachments/42426896525719)

Processado o arquivo você vai acessar o módulo Auditoria e Cruzamentos> Cruzamentos> Preencha o que você deseja cruzar> Selecione o arquivo> Em seguida selecione com o que o seu arquivo vai cruzar, e prontinho, basta selecionar para CRUZAR.

![Imagem 2: Processado o arquivo você vai acessar o módulo Auditoria e Cruzamentos> Cruzamentos> Preencha o que você deseja cruzar>…](https://ajuda.sankhya.com.br/hc/article_attachments/42426896650903)

![Imagem 3: Processado o arquivo você vai acessar o módulo Auditoria e Cruzamentos> Cruzamentos> Preencha o que você deseja cruzar>…](https://ajuda.sankhya.com.br/hc/article_attachments/42426850462871)

![Imagem 4: Processado o arquivo você vai acessar o módulo Auditoria e Cruzamentos> Cruzamentos> Preencha o que você deseja cruzar>…](https://ajuda.sankhya.com.br/hc/article_attachments/42426850568599)

A parte de “Produto” você vai selecionar com qual arquivo você quer realizar no cruzamento:

![Imagem 5: A parte de “Produto” você vai selecionar com qual arquivo você quer realizar no cruzamento:](https://ajuda.sankhya.com.br/hc/article_attachments/42426879771671)

![Imagem 6: A parte de “Produto” você vai selecionar com qual arquivo você quer realizar no cruzamento:](https://ajuda.sankhya.com.br/hc/article_attachments/42426897062551)

“Deixe que o auditor busque automaticamente os arquivos / protocolos para que efetue o Cruzamento”, se você selecionar essa opção realizaremos a busca automática dos arquivos/protocolos na plataforma. 

Agora se você deseja selecionar um arquivo específico para esse cruzamento, você pode selecionar a opção “Informar os protocolos para cruzamento” e informar o protocolo do arquivo, você consegue adicionar mais de um protocolo nesse caso, basta separá-lo por vírgula.

Exemplo: 

![Imagem 7: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/42426911715223)

Depois de preenchido tudo, basta clicar em   ![Imagem 8: Depois de preenchido tudo, basta clicar em](https://ajuda.sankhya.com.br/hc/article_attachments/42426897313815)

Entretanto, a plataforma não irá validar o CNPJ e o período das obrigações dos protocolos informados.

## Agendamento X Automação

Há a possibilidade de deixar os cruzamentos agendados para que sejam feitos em uma determinada data de forma automatizada, ou seja, você importa os arquivos nesse meio tempo e no dia programado ele realizará o cruzamento deles.  

Para agendar o cruzamento basta acessar Cruzamentos> Agenda, clicar em “Novo”, selecionar o cruzamento e a data desejada, e configurar se o agendamento será padrão ou segmentado. 

![Imagem 9: Para agendar o cruzamento basta acessar Cruzamentos> Agenda, clicar em “Novo”, selecionar o cruzamento e a data…](https://ajuda.sankhya.com.br/hc/article_attachments/42426880126743)

![Imagem 10: Para agendar o cruzamento basta acessar Cruzamentos> Agenda, clicar em “Novo”, selecionar o cruzamento e a data…](https://ajuda.sankhya.com.br/hc/article_attachments/42426851078935)

Você vai selecionar o tipo de cruzamento e o dia:

![Imagem 11: Você vai selecionar o tipo de cruzamento e o dia:](https://ajuda.sankhya.com.br/hc/article_attachments/42426835537303)

Agendamento Padrão: nesta opção, o aplicativo Auditoria e Cruzamentos irá buscar todos os processos da obrigação predominante e criará um cruzamento para cada usuário baseado no usuário proprietário do arquivo/processo e na UF do mesmo.

Agendamento segmentado: nesta opção, você especifica os usuários que terão um cruzamento criado para sua propriedade de acordo com a seleção das empresas e suas respectivas UF's

Depois de preenchido tudo, basta clicar em   ![Imagem 12: Depois de preenchido tudo, basta clicar em](https://ajuda.sankhya.com.br/hc/article_attachments/42426868722583)

Já a automação funciona da seguinte forma, assim que você importar os arquivos ele realiza o cruzamento na mesma hora (não há uma data estabelecida, pois, ele identifica que será realizado o cruzamento assim que os arquivos estiverem processados na conta)

Para criar uma automação de cruzamento, você vai acessar o módulo conta > Automação > Selecionar o tipo do cruzamento e clicar em ![Imagem 13: Para criar uma automação de cruzamento, você vai acessar o módulo conta > Automação > Selecionar o tipo do cruzamento e…](https://ajuda.sankhya.com.br/hc/article_attachments/42426851433367)

![Imagem 14: Para criar uma automação de cruzamento, você vai acessar o módulo conta > Automação > Selecionar o tipo do cruzamento e…](https://ajuda.sankhya.com.br/hc/article_attachments/42426835875223)

## Função “Agrupamento”

Em Cruzamentos, disponibilizamos uma nova funcionalidade, chamada “Agrupador”. Nela, é possível agrupar os resultados dos cruzamentos de Sped Fiscal vs CTE, Sped Fiscal vs NFE e/ou Sped Fiscal vs Obrigações Estaduais, para um mesmo estabelecimento e período de referência. 

Esta funcionalidade só pode ser utilizada se o cruzamento já foi feito,  pois funciona como um relatório de cruzamento agrupado. 

Para agrupar os resultados você acessa a opção Cruzamentos> Agrupador> Preenche as informações e clica em ![Imagem 15: Para agrupar os resultados você acessa a opção Cruzamentos> Agrupador> Preenche as informações e clica em .](https://ajuda.sankhya.com.br/hc/article_attachments/42426868966551).

![Imagem 16: Para agrupar os resultados você acessa a opção Cruzamentos> Agrupador> Preenche as informações e clica em .](https://ajuda.sankhya.com.br/hc/article_attachments/42426851708695)

Assim que você solicitar, aparecerá essa tela:

![Interface gráfica do usuário, Texto, Aplicativo Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42426898240279)

E você poderá clicar no hiperlink “aqui” para acessar o relatório.

## Status de Processamento

![Imagem 18: Status de Processamento](https://ajuda.sankhya.com.br/hc/article_attachments/42426851941911)

#### É possível diagnosticar o erro passando o mouse por cima do X.
