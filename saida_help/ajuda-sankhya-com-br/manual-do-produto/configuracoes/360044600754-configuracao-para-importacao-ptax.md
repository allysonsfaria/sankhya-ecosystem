---
id: "360044600754"
titulo: "Configuração para Importação PTAX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-01T17:28:42Z"
rotulos: ["manual", "Configuração", "Moeda", "Agendamento", "Importação", "br.com.sankhya.configuracao.importacao.ptax", "Configuração para Importação PTAX manual", "Financeiro", "Configuração para Importação PTAX", "Banco Central"]
---

# Configuração para Importação PTAX

O PTAX é uma taxa de câmbio calculada diariamente pelo [Banco Central do Brasil](http://www.bcb.gov.br/pt-br#!/home). São feitas quatro consultas às negociações entre as 13 instituições dealers (que são aquelas credenciadas para operar com o governo) entre 10h e 10h10; 11h e 11h10; 12h e 12h10; e 13h e 13h10. É importante saber que o Banco Central do Brasil libera o PTAX contendo os valores de moedas após as 13h10min de cada dia. Portanto, caso ocorra um agendamento antes desse horário, a atualização não será efetuada, sendo necessário executar um novo agendamento.

Cada janela de consulta dura dois minutos e as taxas de câmbio de compra e de venda referentes a cada consulta correspondem, respectivamente, às médias das cotações de compra e de venda efetivamente fornecida pelos dealers, excluídas, em cada caso, as duas maiores e às duas menores.

Esta tela tem por funcionalidade configurar o agendamento do JOB que irá realizar a importação do arquivo que contém as referidas taxas diretamente no site do [Banco Central do Brasil](http://www.bcb.gov.br/pt-br#!/home).

A importação do arquivo será executada três vezes seguidas com intervalo de quinze segundos. Caso não seja possível realizar a importação, é registrada a notificação do e-mail e efetuado um novo agendamento para ser executado depois de uma hora. Permanecendo a impossibilidade de importação, o envio da notificação não ocorrerá novamente. Sendo realizada a importação, será enviada a notificação para os e-mails configurados.

[Configurando o mapeamento...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#configurandoomapeamentodasmoedas)                                [Botões e campos no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#botesecamposnotopodatela)

[Aba E-mails para notificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#abae-mailsparanotificao)                                    [Layout do Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#layoutdoarquivo)

[Parâmetros que atuam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#parmetrosqueatuamnestarotina)

![Imagem 1: Parâmetros que atuam nesta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4405788960151)

### Configurando o mapeamento das moedas

O arquivo contendo a tabela a ser empregada pelo sistema para realizar o mapeamento das moedas utilizadas no ERP, pode ser baixado pelo site <http://www4.bcb.gov.br/Download/fechamento/20171215.CSV>, alterando somente a data apresentada no final que está no padrão "AAAAMMDD" para a data do dia em questão. Este mapeamento visa processar a moeda configurada. Vejamos um exemplo:

Desejando utilizar a moeda dólar, realize o download da tabela para localizar o seu código:

![Imagem 2: Desejando utilizar a moeda dólar, realize o download da tabela para localizar o seu código:](https://ajuda.sankhya.com.br/hc/article_attachments/4405800067351)

Detalhamento da linha:

| - 04/08/2021 = Data da cotação; - 220 = Código da moeda; - A = Tipo da moeda; - USD = Sigla da Moeda; | - 5,2085 = Taxa compra; - 5,2091 = Taxa venda; - 1 = Paridade Compra; - 1 = Paridade Venda. |
| --- | --- |

Na tela [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754-Valores-de-Moedas), informe no campo **"Código tabela BCB"**, o código da moeda que será utilizada. Depois, indique no campo **"Tipo de Taxa"**, qual o tipo de dados será importado, podendo ser a taxa de **"Compra"** ou **"Venda"**.

Após efetuar as configurações descritas acimas, o sistema executará o mapeamento automaticamente. Sendo que, caso você queira utilizar outra moeda, basta realizar o procedimento modificando o código e tipo de taxa da mesma conforme a tabela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#top)

### Botões e campos no topo da tela

O botão **"Ligar/Desligar agendador"** ativa e desativa a configuração para importação do PTAX; quando ligado, o botão será exibido na coloração **verde**; se desligado, o mesmo será apresentado na cor **vermelha**.

Através do botão **"Importar agora"**, teremos a execução da rotina de importação para o registro selecionado, mesmo que esteja fora do horário configurado ou se o registro estiver inativo. Esta importação só será realizada caso exista o arquivo já disponibilizado pelo Banco Central do Brasil. Assim, ao clicar no botão Importar agora, será aberto o pop-up **"Importação"** para definição do período desejado e concretização do procedimento:

![Imagem 3: Através do botão "Importar agora" , teremos a execução da rotina de importação para o registro selecionado, mesmo que…](https://ajuda.sankhya.com.br/hc/article_attachments/4405788865815)

Caso a importação seja realizada fora da data em que o arquivo foi disponibilizado, será exibida a seguinte mensagem:

**"Ocorreu um erro ao efetuar o download do arquivo PTAX. O arquivo ainda não foi disponibilizado ou está corrompido. Endereço: http://www4.bcb.gov.br/Download/fechamento/20171124.CSV".**

Além disso, a mensagem descrita acima será enviada para o(s) e-mail(s) configurado(s).

A marcação **"Substituir cotação existente"** trabalha no momento da importação para o registro, ou seja, caso esteja realizada e seja efetuado o processo de importação, existindo uma cotação, esta será substituída pela nova cotação importada; além disso, no pop-up Importação que é aberto, tem-se no quadrante **"Resumo"** a descrição das cotações que foram sobrescritas. Caso a marcação Substituir cotação existente não seja efetuada, ao proceder com a importação, as cotações existentes não serão sobrepostas.

Tem no campo **"Dh. próxima execução"** a data e hora da execução da próxima importação.

A última data de importação feita pela rotina ou realizada manualmente é gravada e exibida no campo **"Dh. última. Importação"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#top)

### Aba E-mails para notificação

Nesta aba são configurados os dados necessários dos destinatários e o tipo da notificação.

![Imagem 4: Nesta aba são configurados os dados necessários dos destinatários e o tipo da notificação.](https://ajuda.sankhya.com.br/hc/article_attachments/4405791740567)

No campo **"E-mail"**, informe o endereço de correio eletrônico que irá receber as notificações.

Através da marcação **"Notificar"**, indique se a notificação deverá ou não ser enviada para o e-mail cadastrado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#top)

### Layout do Arquivo

Caso ocorra a modificação do layout do arquivo pelo órgão responsável, é possível utilizar um layout diferente do padrão. Para isto, configure o parâmetro Layout do arquivo PTAX - NUARCPTAX com o novo layout. O layout deverá ser previamente construído na tela [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054-Layout-de-Processamento-de-Arquivo).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#top)

### Parâmetros que atuam nesta rotina

Através do parâmetro **"Endereço para download do arquivo PTAX - ENDDOWNARQPTAX"**, informe o endereçamento para baixa do arquivo.

Por meio do parâmetro **"Tempo (ms) limite de conexão p/ download PTAX - CONNTIMEOUTPTAX"**, indique o prazo de limitação de conexão.

Defina no parâmetro **"Tempo (ms) limite de leitura p/ arquivo PTAX - READTIMEOUTPTAX"**, o período de delimitação de leitura.

Através do parâmetro **"Layout do arquivo PTAX - NUARCPTAX"**, configure o layout do arquivo PTAX.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600754-Configura%C3%A7%C3%A3o-para-Importa%C3%A7%C3%A3o-PTAX#top)
