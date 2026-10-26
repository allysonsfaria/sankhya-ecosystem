---
id: "42427059626007"
titulo: "MANUAL RAPA - Importação Automática"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427059626007-MANUAL-RAPA-Importa%C3%A7%C3%A3o-Autom%C3%A1tica"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Automação e Importação"
atualizado_em: "2026-08-03T12:44:27Z"
rotulos: ["asis", "sync_hc", "asis_52907400333971", "sync_hash_192c78c0b279"]
---

# MANUAL RAPA - Importação Automática

## Importação Automática

Em busca de otimizar o método de upload de arquivos para o KOLOSSUS, a ASIS desenvolveu um programa RPA (Robotic Process Automation) que automatiza o processo de identificação e importação dos arquivos, essa importação é feita através da leitura de Diretórios/pastas que você adiciona dentro da Importação Automática, feito isso, ele realizará uma ponte entre a pasta e o Kolossus/Oráculo, enviando todos os arquivos que você adicionar dentro dela.

As premissas técnicas do aplicativo são:

- Sistema operacional: Microsoft Windows 7 ou superior com Java Virtual Machine instalada.
- Processamento: Processador de 1.8 gigahertz (GHz) ou mais rápido. Para uma melhor performance recomendamos um processador de 64 bits multicore.
- Memória RAM disponível: 2 gigabytes (GB) para 32 bits ou 4 GB para 64 bits.
- Espaço em disco rígido: 1 GB para um sistema operacional de 32 bits ou 2 GB para um de 64 bits. Neste espaço não está contemplando os arquivos que serão importados.
- Conectividade: Conexão estável com a Internet, com no mínimo 1 mbps de Largura de Banda. Uma conexão mais rápida é indicada para acelerar a importação dos arquivos.

## Instalar o Programa

Para instalar o programa “Importação Automática” você acessa o Kolossus com o seu login e em seguida clica na opção “Central de Downloads” nela estará disponível o link para download do programa.

![Interface gráfica do usuário, Texto, Aplicativo, chat ou mensagem de texto Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427068414231)

![Interface gráfica do usuário, Aplicativo, Word Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427068471191)

## RAPA versão LINUX

Para os sistemas operacionais que utilizam o LINUX é necessário instalar o programa próprio para tal sistema, abaixo está o link para download.

<https://storage.googleapis.com/kolossus-static/dowloads/rapa_linux.zip>

## Recomendamos que você utilize o aplicativo de importação automática

Com o aplicativo Importação Automática você irá economizar o seu tempo, ao utilizá-lo, você não precisará acessar o Kolossus para realizar as importações, basta salvar os arquivos diretamente dos validadores (Ex. PVA) na pasta mapeada e pronto, ele será importado de forma automática e após a conclusão da auditoria, você receberá os resultados diretamente em seu e-mail, além disso, você garante a efetividade no Upload, no processo de importação via web, qualquer intercorrência na internet afetará diretamente o upload dos arquivos no Kolossus, isso acontece com frequência quando o tamanho dos arquivos ou lote excedem 100MB. Com o aplicativo Importação Automática não há esse risco, visto que ele funciona como uma ponte direta entre o local do arquivo e os nossos servidores

## Premissas operacionais do aplicativo Importação Automática

Todos os arquivos submetidos ao aplicativo devem possuir o leiaute exigido pela regulamentação os Órgãos Oficiais e é imprescindível submeter os arquivos aos programas validadores específicos, para checagem de estrutura dos arquivos antes da importação/processamento. Os arquivos que contenham erros estruturais não serão processados, pois a ferramenta processa apenas arquivos que estejam dentro das especificações do Fisco. É de suma importância o saneamento de todas as ocorrências estruturais dos arquivos antes de submetê-los à auditoria, pois estes erros poderão comprometer seriamente os retornos das auditorias e o cruzamento das informações.

São suportados arquivos com as seguintes extensões:

![Texto, Carta Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427068612759)

## Configuração dos diretórios do aplicativo Importação Automática

Antes de fazer o processamento dos arquivos, você deverá configurar a pasta(s)/diretórios onde serão colocados os arquivos a serem processados. Para efetuar a configuração, você vai selecionar o botão “Configurações>Diretórios”:

![Interface gráfica do usuário, Texto, Aplicativo, chat ou mensagem de texto Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427053209111)

Após clicar em “Diretórios”, será direcionado para uma nova janela, na qual você fará a configuração das pastas que serão origem do processamento dos arquivos.

AVISO: Por favor verifique se a pasta selecionada é a correta para o envio de dados pois não há como reverter processos que já foram executados pelas pastas direcionadas.

## Funções do “Preferências” do Aplicativo Importação Automática

Dentro da função preferências temos disponibilizado para você, as seguintes configurações:

Modo de operação 🡪 Essa opção é composta por duas funções “Não mover arquivos” através dele não realizaremos nenhuma alteração nos arquivos ou até mesmo nas estruturas da pasta; a segunda função seria “Mover arquivos” já ela seria o oposto do primeiro, através dela movemos os arquivos enviados com sucesso ou com erro para as pastas chamadas “enviados” ou “erros” na raíz do diretório/pasta, ou seja, criamos duas pastas com o intuito de você administrar o que foi importado com sucesso e o que deu erro. As duas opções são viáveis de acordo com a sua necessidade.

Máximo de uploads simultâneos 🡪 É a quantidade de arquivos que ele vai enviar ao mesmo tempo, nessa opção você consegue configurar somente até o 3, caso coloque um número maior que esse, dará erro.

Receber um e-mail com o resultado das auditorias 🡪 Através dessa opção você será notificado quando for processado obrigações acessórias como SPED Fiscal, EFD Contribuições etc.

Importar notas para o Oráculo 🡪 Essa opção deverá ser selecionada apenas se você possuir acesso a nossa plataforma Oráculo, caso você tenha somente acesso a plataforma Kolossus, por favor, não selecione essa opção, pois impactará em suas importações futuras.

Enviar um relatório diário por e-mail dos arquivos com erro de envio 🡪 Através dessa opção você terá uma forma de gerenciar caso algum arquivo não tenha sido encaminhado da Importação Automática para o Kolossus.

## Status do aplicativo Importação Automática

No aplicativo Importação Automática você consegue filtrar por status os arquivos que você adicionou no diretório, para visualizá-los, você acessa a opção “Todos os Arquivos” e seleciona o status que tem interesse:

![Interface gráfica do usuário, Texto, Aplicativo, Email Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427053304727)

Significado de cada Status:

- Disponível: Pasta se encontra para ser submetida a importação.
- Em Fila: Em fila para ser importado.
- Enviando: Foi enviado para a plataforma Kolossus (não significa que o processo esteja concluído)
- Descompactado: Abrindo o pacote zip e realizando a leitura do documento.
- Enviado: Arquivos enviados para a plataforma Kolossus, concluído.
- Descompactado: Finalização do descompactando.
- Ignorado: Problema sistémico (Ex: Internet)
- Não identificado: Arquivo/documento ou extensão não aceito pela ferramenta
- Interrompido: Instabilidade na leitura da pasta (Ex: internet)

### O aplicativo importação automática consegue ler pastas que estão no servidor?

Sim! Caso você tenha uma pasta do servidor mapeada em sua máquina, basta selecioná-la na parte de diretório.

## Importar CTes diretamente para o Oráculo

Para importar CTEs para o Oráculo, basta flegar a opção “Importar CTe para o Oráculo”:

![Interface gráfica do usuário, Texto, Aplicativo, Email Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427068911255)

Essa opção está disponível através da opção Configurações> Preferências

![Interface gráfica do usuário Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427036166295)

### O que eu faço quando aparece uma tela de erro ao tentar logar na importação automática?

Quando você acessar o aplicativo e por desventura, aparecer essa mensagem:

![Interface gráfica do usuário Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427069094423)

Você precisará verificar a sua conexão com a internet; As configurações de proxy; O seu antivírus e Firewall.

O aplicativo precisa ter acesso às URLs abaixo:

- [https://file.asisprojetos.com.br](https://file.asisprojetos.com.br/)
- [https://auth.asisprojetos.com.br](https://auth.asisprojetos.com.br/)
- [https://corewebapi.asisprojetos.com.br](https://corewebapi.asisprojetos.com.br/)

Se a opção "Otimizar envio de arquivos grandes" estiver marcada:

- [https://large.asisprojetos.com.br](https://large.asisprojetos.com.br/)

Se a opção de enviar as notas para o Oráculo estiver marcada (NFe ou CTe):

- [https://nfe-data-lake.s3-sa-east-1.amazonaws.com](https://nfe-data-lake.s3-sa-east-1.amazonaws.com/)
- [https://cte-data-lake.s3-sa-east-1.amazonaws.com](https://cte-data-lake.s3-sa-east-1.amazonaws.com/)

 Como configurar o proxy no aplicativo importação automática?

Atualmente você tem duas opções de configuração do proxy:

A primeira é acessando a tela de login:

![Interface gráfica do usuário, Site Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427036317463)

A segunda opção é, você acessa o aplicativo Importação Automática> Configurações> Proxy.

![Interface gráfica do usuário, Texto, Aplicativo, chat ou mensagem de texto Descrição gerada automaticamente](https://ajuda.sankhya.com.br/hc/article_attachments/42427060540311)

## Atualizar RAPA

Para a atualização do RAPA, não é necessário realizar a exclusão do aplicativo. Indo na central de Downloads, e realizando a instalação do aplicativo, automaticamente ele será atualizado, sendo assim, não é necessário configurá-lo novamente, a não ser que antes da atualização você coloque para apagar dados.

![Imagem 11: Para a atualização do RAPA, não é necessário realizar a exclusão do aplicativo. Indo na central de Downloads, e…](https://ajuda.sankhya.com.br/hc/article_attachments/42427036473751)

![Imagem 12: Para a atualização do RAPA, não é necessário realizar a exclusão do aplicativo. Indo na central de Downloads, e…](https://ajuda.sankhya.com.br/hc/article_attachments/42427053920023)

## Status de Processamento

![Imagem 13: Status de Processamento](https://ajuda.sankhya.com.br/hc/article_attachments/42427060721047)

É possível diagnosticar o erro passando o mouse por cima do X.
