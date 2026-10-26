---
id: "360044595294"
titulo: "Extrator de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595294-Extrator-de-Dados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:44:32Z"
rotulos: ["manual", "Configuração", "Consulta", "Relatórios", "XML", "Agendamento", "br.com.sankhya.core.cfg.extrator.dados", "Extrator de Dados manual", "Guia do Extrator de Dados Sankhya Om", "JSON", "CSV"]
---

# Extrator de Dados

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310581371415) Módulo: Configurações > Avançado
```

---

Nesta tela, pode-se exportar informações do Sankhya Om para diversos formatos e destinos, para serem utilizados de acordo com as necessidades dos usuários.

![Imagem 2: Nesta tela, pode-se exportar informações do Sankhya Om para diversos formatos e destinos, para serem utilizados de…](https://ajuda.sankhya.com.br/hc/article_attachments/8220464254359)

Na parte superior desta tela, tem-se os botões padrão do sistema, além dos botões  **"Executar agora"** e  **"Processos em execução"**.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595294-Extrator-de-Dados#abageral)                                                       [Aba Consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595294-Extrator-de-Dados#abaconsulta)

[Aba Agendamento/Execução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595294-Extrator-de-Dados#abaagendamentoexecucao)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595294-Extrator-de-Dados#top)

## Aba Geral

Nesta aba, tem-se as opções:

No campo **"Formato"**, pode-se escolher entre **"Excel (xlsx)"**, **"XML"**, **"JSON"**, e **"CSV"**.

O campo **"Destino"** possui as opções **"Download"** e **"Repositório de arquivos"** disponíveis para seleção.

**Nota:** quando a opção Download for selecionada, o sistema não permitirá o agendamento e, desta forma, a execução será realizada manualmente pelo usuário por meio do botão Executar agora (localizado na parte superior da tela). Por outro lado, caso a opção Repositório de arquivos encontre-se selecionada, o Destino poderá ser agendado ou executado de maneira imediata, assim, o sistema criará no repositório padrão do sistema, o diretório **"Extrator de Dados"** e irá salvar os arquivos gerados.

Em relação ao campo **"Nome do arquivo"**, tem-se que o usuário escolherá um nome para o arquivo que será gerado.

No campo **"Codificação"**, pode-se definir se o mesmo será **"UTF-8"**, **"ISO-8859-1"** ou **"Automático"**, sendo que este último estabelecerá de forma automática a codificação com base no formato do arquivo.

Quando a marcação **"Compactar arquivo (.zip)?"** está habilitada, o sistema irá gerar o arquivo no formato zip com tamanho reduzido.

Referente aos campos **"Incluir data no nome do arquivo?:"** e **"Incluir hora no nome do arquivo?:"**, estes irão inserir a data e hora no momento da geração da extração no final do nome do arquivo.

**Observação:** a opção Incluir hora no nome do arquivo? é importante, pois criará registros específicos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595294-Extrator-de-Dados#top)

## Aba Consulta

![Imagem 3: Aba Consulta](https://ajuda.sankhya.com.br/hc/article_attachments/8220602824471)

Na aba **"Consulta"**, tem-se o botão ![Imagem 4: Na aba "Consulta" , tem-se o botão "Fonte de Dados" , que listará as fontes de dados previamente configuradas em que a…](https://ajuda.sankhya.com.br/hc/article_attachments/8220566055447) **"Fonte de Dados"**, que listará as fontes de dados previamente configuradas em que a consulta SQL será executada. Além disso, será possível editar a consulta SQL e validar a consulta SQL que executa o script, sendo que, será retornada apenas uma linha para melhorar a perfomance ou executar a consulta com todos os registros, respeitando a quantidade máxima de linhas configuradas na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).

**Nota:** se mesmo com o parâmetro **"Qtd. máx. de reg. para export. de PDF, XLS e Cubo - QTDMAXREGEXPORT"** configurado com a quantidade de linhas não for possível exportar uma quantidade grande de registros , é necessário que você utilize o extrator de dados.

**Observação:** nesta versão do Extrator de Dados a consulta não possui suporte para parâmetros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595294-Extrator-de-Dados#top)

## Aba Agendamento/Execução

![Imagem 5: Aba Agendamento/Execução](https://ajuda.sankhya.com.br/hc/article_attachments/8220565378327)

Nesta aba, tem-se as duas grades a seguir:

#### Grade Agendamento

Nesta grade tem-se a marcação **"Ativo"** e, quando esta estiver habilitada, o sistema exibirá o campo **"Tipos de gatilho"**, que possui as opções **"Expressão CRON"** e **"Intervalo de tempo"**.

Quando a opção Expressão CRON estiver selecionada, o campo **"Expressão do gatilho"** será exibido; neste será definido o intervalo de tempo com base no Tipo de gatilho. Em seguida, o usuário validará a expressão inserida no campo por meio do botão ![Imagem 6: Quando a opção Expressão CRON estiver selecionada, o campo "Expressão do gatilho" será exibido; neste será definido o…](https://ajuda.sankhya.com.br/hc/article_attachments/8220647969559) **"Validar Expressão"**.

**Nota:** será possível utilizar o botão **"Ajuda de uso para sintaxe cron"** para auxílio no uso da expressão.

Ao selecionar a opção **"Intervalo de tempo"**, tem-se que esta exibirá o campo **"Tipo de intervalo"** que pode ser por **"Minutos"** ou **"Hora"**, e o campo **"Valor"** em que o usuário determinará o tempo de sua preferência conforme a opção marcada em Tipo de intervalo.

**Observação:** caso a consulta a ser realizada pelo Extrator de Dados seja externa, toda vez que o agendamento for executado, será necessária a liberação da autorização para a customização.

#### Grade Execução

Esta grade mostrará as últimas execuções da tela.

O campo **"Dt. última execução"** exibirá a data e hora da última execução de agendamento.

No campo **"Tempo de processamento (min)"** será apresentado o tempo total gasto no último processamento.

Em **"Log de erro"**, será mostrada a informação do erro durante a execução.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595294-Extrator-de-Dados#top)
