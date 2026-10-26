---
id: "42426645112855"
titulo: "Cruzamento de Obrigações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426645112855-Cruzamento-de-Obriga%C3%A7%C3%B5es"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Auditoria e Cruzamentos"
atualizado_em: "2026-08-03T12:27:28Z"
rotulos: ["asis", "sync_hc", "asis_52941202021267", "sync_hash_af76926edae6"]
---

# Cruzamento de Obrigações

Através dos cruzamentos das obrigações é possível identificar divergências entre os documentos.

O cruzamento realizado na plataforma compara campos idênticos nas obrigações.

Temos a possibilidade de cruzar notas com as obrigações acessórias, sendo possível identificar se a escrituração foi feita de acordo com as informações do documento, também é possível cruzar o SPED FISCAL com as obrigações estaduais e as GIAs-ST, onde podemos visualizar todos os valores informados em ambas as escriturações e arrumar possíveis divergências, temos também o cruzamento do SPED Fiscal com o SPED Contribuições, que nos ajuda a enxergar possíveis notas faltantes ou valores divergentes e também o cruzamento do SPED Contribuições com a DCTF e o ECAC, amarrando de todos os lados as informações, para que nenhuma informação seja enviada incorretamente.

**Dica de Uso:**Considerar sempre a obrigação do lado esquerdo como a principal, isto é, será necessário selecionar a obrigação e escolher com qual você deseja cruzar.

Exemplo:  SPED FISCAL vs NFE

![Imagem 1: Temos a possibilidade de cruzar notas com as obrigações acessórias, sendo possível identificar se a escrituração foi…](https://ajuda.sankhya.com.br/hc/article_attachments/42426623616407)

![Imagem 2: Temos a possibilidade de cruzar notas com as obrigações acessórias, sendo possível identificar se a escrituração foi…](https://ajuda.sankhya.com.br/hc/article_attachments/42426623713815)

### Quais arquivos cruzamos

| | ÍCONE AUDITOR | CLASSIFICAÇÃO | | --- | --- | | DAMEF vs SPED | Cruzamentos | | DCTF vs ECAC | Cruzamentos | | DCTF vs ECAC vs PERDCOMP | Cruzamentos | | DCTF vs PERDCOMP | Cruzamentos | | DIRF vs DCTF | Cruzamentos | | DIRF vs ECAC | Cruzamentos | | ECD vs DCTF | Cruzamentos | | ECD vs EFD CONTRIBUIÇÕES | Cruzamentos | | ECF vs DCTF | Cruzamentos | | ECF vs DCTF vs ECAC | Cruzamentos | | ECF vs DIRF | Cruzamentos | | ECF vs ECD | Cruzamentos | | ECF vs SPED FISCAL | Cruzamentos | | EFD CONTRIBUIÇÕES vs DCTF | Cruzamentos | | EFD CONTRIBUIÇÕES vs CTE | Cruzamentos | | EFD CONTRIBUIÇÕES vs NFE | Cruzamentos | | EFD CONTRIBUIÇÕES vs NFSE | Cruzamentos | | EFD CONTRIBUIÇÕES vs SPED FISCAL | Cruzamentos | | EFD vs DCTF vs ECAC | Cruzamentos | | SINTEGRA vs NFE | Cruzamentos | | SPED FISCAL vs CTE | Cruzamentos | | SPED FISCAL vs DCTF | Cruzamentos | | SPED FISCAL vs NFCE | Cruzamentos | | SPED FISCAL vs SAT | Cruzamentos | | SPED FISCAL vs NFE | Cruzamentos | | SPED FISCAL vs GIA ST | Cruzamentos | | SPED FISCAL vs OBRIGAÇÕES ESTADUAIS | Cruzamentos | | SPED FISCAL vs SEF | Cruzamentos | | SPED FISCAL vs RECOF | Cruzamentos | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Como realizar um cruzamento

Para realizar o cruzamento, primeiramente você precisará importar os arquivos, eles poderão ser importados tanto pelo Upload ou pelo nosso programa Importação Automática (Disponível em nossa central de downloads), e depois aguardar o processamento deles Importante: enquanto o arquivo não estiver processado não deve dar andamento em seu cruzamento, pois o resultado será comprometido.

Depois que o processamento for concluído aparecerá o ícone e você poderá dar andamento em seu cruzamento.

Para verificar o andamento do processamento você pode acessar o módulo Auditoria e Cruzamentos > Processos.

![Imagem 3: Para verificar o andamento do processamento você pode acessar o módulo Auditoria e Cruzamentos > Processos.](https://ajuda.sankhya.com.br/hc/article_attachments/42426629530135)

Processado o arquivo você vai acessar o módulo Auditoria e Cruzamentos > Cruzamentos > Preencha o que você deseja cruzar > Selecione o arquivo > Em seguida selecione com o que o seu arquivo vai cruzar, e prontinho, basta selecionar para CRUZAR.

![Imagem 4: Processado o arquivo você vai acessar o módulo Auditoria e Cruzamentos > Cruzamentos > Preencha o que você deseja…](https://ajuda.sankhya.com.br/hc/article_attachments/42426623616407)

A parte de “Produto” você vai selecionar com qual arquivo você quer realizar no cruzamento:

![Imagem 5: A parte de “Produto” você vai selecionar com qual arquivo você quer realizar no cruzamento:](https://ajuda.sankhya.com.br/hc/article_attachments/42426623713815)

“Deixe que auditor busque automaticamente os arquivos / protocolos para que efetue o Cruzamento”, se você selecionar essa opção realizaremos a busca automática dos arquivos/protocolos na plataforma.

Agora se você deseja selecionar um arquivo específico para esse cruzamento, você pode selecionar a opção “Informar os protocolos para cruzamento” e informar o protocolo do arquivo, você consegue adicionar mais de um protocolo nesse caso, **basta separá-lo por vírgula**.

Exemplo:

![Imagem 6: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/42426624049303)

Depois de preenchido tudo, basta clicar em **Cruzar**.

Entretanto, a plataforma não irá validar o CNPJ e o período das obrigações dos protocolos informados.

## Agendamento X Automação

Há a possibilidade de deixar os cruzamentos agendados para que sejam feitos em uma determinada data de forma automatizada, ou seja, você importa os arquivos nesse meio tempo e no dia programado ele realizará o cruzamento deles.

Para agendar o cruzamento basta acessar Cruzamentos> Agenda, clicar em “Novo”, selecionar o cruzamento e a data desejada, e configurar se o agendamento será padrão ou segmentado.

![Imagem 7: Para agendar o cruzamento basta acessar Cruzamentos> Agenda, clicar em “Novo”, selecionar o cruzamento e a data…](https://ajuda.sankhya.com.br/hc/article_attachments/42426629683223)![Imagem 8: Para agendar o cruzamento basta acessar Cruzamentos> Agenda, clicar em “Novo”, selecionar o cruzamento e a data…](https://ajuda.sankhya.com.br/hc/article_attachments/42426629799703)

Você vai selecionar o tipo de cruzamento e o dia:

Agendamento Padrão: nesta opção, o aplicativo Auditoria e Cruzamentos irá buscar todos os processos da obrigação predominante e criará um cruzamento para cada usuário baseado no usuário proprietário do arquivo/processo e na UF do mesmo.

![Imagem 9: Você vai selecionar o tipo de cruzamento e o dia: Agendamento Padrão: nesta opção, o aplicativo Auditoria e Cruzamentos…](https://ajuda.sankhya.com.br/hc/article_attachments/42426655485207)

Agendamento segmentado: Nesta opção, você poderá segmentar o cruzamento e a data de envio por empresas e por usuários.

![Imagem 10: Agendamento segmentado: Nesta opção, você poderá segmentar o cruzamento e a data de envio por empresas e por usuários.…](https://ajuda.sankhya.com.br/hc/article_attachments/42426646081175)Depois de preenchido tudo, basta clicar em **Salvar**.

Já a automação funciona da seguinte forma, assim que você importar os arquivos ele realiza o cruzamento na mesma hora (não há uma data estabelecida, pois, ele identifica que será realizado o cruzamento assim que os arquivos estiverem processados na conta)

Para criar uma automação de cruzamento, você vai acessar o módulo Conta > Automação > Selecionar o tipo do cruzamento e clicar em **Salvar.**

![Imagem 11: Para criar uma automação de cruzamento, você vai acessar o módulo Conta > Automação > Selecionar o tipo do cruzamento e…](https://ajuda.sankhya.com.br/hc/article_attachments/42426646150935)

## Função “Agrupamento”

Em Cruzamentos, disponibilizamos uma nova funcionalidade, chamada “Agrupador”. Nela, é possível agrupar os resultados dos cruzamentos de Sped Fiscal vs CTE, Sped Fiscal vs NFE e/ou Sped Fiscal vs Obrigações Estaduais, para um mesmo estabelecimento e período de referência.

Esta funcionalidade só pode ser utilizada se o cruzamento já foi feito,  pois funciona como um relatório de cruzamento agrupado.

Para agrupar os resultados você acessa a opção Cruzamentos> Agrupador> Preenche as informações e clica em **Salvar.**

![Imagem 12: Para agrupar os resultados você acessa a opção Cruzamentos> Agrupador> Preenche as informações e clica em Salvar.](https://ajuda.sankhya.com.br/hc/article_attachments/42426655801879)
