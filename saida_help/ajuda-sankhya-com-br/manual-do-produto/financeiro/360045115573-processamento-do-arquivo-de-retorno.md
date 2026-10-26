---
id: "360045115573"
titulo: "Processamento do Arquivo de Retorno"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:44:54Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "Ocorrências", "Financeiro", "Arquivo de Retorno", "Processamento do Arquivo de Retorno", "br.com.sankhya.processamento.arquivo.retorno", "Processamento do Arquivo de Retorno manual", "Processamento automático de retornos bancários", "Configurações de layout taxas e log", "Parâmetros para baixa e validação de títulos", "EDI Bancário"]
---

# Processamento do Arquivo de Retorno

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312491990807) Módulo: Financeiro > EDI Bancário
```

---

Depois de enviar ao banco o arquivo gerado pela tela [Geração de arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914), o banco efetua os devidos processamentos e retorna para a empresa um arquivo de retorno, com o posicionamento dos títulos.

[Procedimentos iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#procedimentosiniciais)                                            [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#botesdatela)              

[Log de Processamento...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#logdoprocessamentodearquivoderetorno)                                        [Relatórios e análises das ocorrências...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#relatrioseanlisesdasocorrnciasderetorno)

[Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#parmetrosqueinfluenciamestarotina)

![Imagem 2: Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360091394954)

## Procedimentos iniciais

Nesta tela, primeiramente escolha o **"Layout de Retorno"** que foi configurado, além do **"Arquivo"** de Retorno, através do ícone  para realização do processamento.

**Observação:** em situações em que o arquivo EDI seja retornado do banco, quando você realizar o processamento do arquivo, o sistema efetuará automaticamente na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753), a baixa dos títulos dos boletos enviados para o banco.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#top)

## Botões da tela

Ao acionar o botão ![Imagem 3: Ao acionar o botão "Preferências" teremos as seguintes configurações:](https://ajuda.sankhya.com.br/hc/article_attachments/15500127510935) **"Preferências"** teremos as seguintes configurações:

![Imagem 4: Ao acionar o botão "Preferências" teremos as seguintes configurações:](https://ajuda.sankhya.com.br/hc/article_attachments/360091394414)

Efetue a marcação **"Usar o banco junto com Nosso Número para localizar o título"** para que a busca pelo título no banco de dados seja feita tanto pelo Nosso Número do título quanto pelo Código do Banco.

Em relação à marcação **"Obter o valor do título do próprio título"**, teremos o seguinte exemplo:

Se nas ocorrências foi marcada para fazer a baixa no processamento do retorno, ao fazer a baixa em vez de pegar o valor do arquivo de retorno será pego o valor que está no banco de dados.

Quando os parâmetros **"Subtrai taxa ao valor da baixa no retorno bancário - SUBTXVLRBAIXA"** e **"Soma taxa ao valor da baixa no retorno bancário - SOMATXVLRBAIXA"** estiverem desligados e o título possuir juros/multas negociados e taxa administrativa, ao processar o arquivo, será levada a taxa administrativa para o título;

**Observação:** para o comportamento acima, a marcação **"Considerar juros e multas negociados"** deve estar habilitada.

**Seção Log de Processamento**

Nesta seção, efetue as configurações pertinentes à limpeza dos registros de Log de Processamento de Retorno. Através do parâmetro **"Período p/ manter log de processamento de retorno - PERMANTPROCRET"** defina, em dias, o período ao qual o log de processamento será armazenado.

Caso seja a primeira configuração, o sistema verificará a necessidade de limpeza e perguntará o que você deseja fazer. Através de um pop-up de **"Aviso"**, serão apresentadas as seguintes opções:

**1-** Remover os registros mais antigos (Altamente recomendável)

**1.1** Manter automaticamente apenas os registros mais recentes

**2-** Não remover (Pode causar lentidão em curto prazo)

Apontando apenas a marcação 1, o sistema efetuará a limpeza imediatamente, removendo os arquivos antigos de acordo com o período de armazenamento configurado. Futuramente, o log estará cheio e novamente ocorrerá este questionamento.

Ao selecionar a marcação 1 em conjunto com a marcação 1.1, o sistema executará a limpeza imediatamente e, posteriormente, irá executa-la automaticamente.

Ao final, indicando a marcação 2, a limpeza não será realizada, o que pode causar lentidão na rotina de processamento em curto prazo.

**Nota:** as alterações realizadas no pop-up Aviso refletem nas preferências da tela. A configuração de limpeza, assim como as demais preferências, são realizadas por usuário.

O botão ![Imagem 5: O botão "Prévia" simulará o processamento do arquivo, inclusive com as mensagens de erro, caso existam.](https://ajuda.sankhya.com.br/hc/article_attachments/15500175185559) **"Prévia"** simulará o processamento do arquivo, inclusive com as mensagens de erro, caso existam.

**Observação:** o Sankhya Om difere em alguns aspectos do MGE, neste caso. As linhas gravadas na tabela TSIOBCLOG correspondem à erros de validação básica do arquivo de retorno. A gravação destes erros ocorre em uma transação separada do processamento, ou seja, apesar do sistema gravar erros de validação básica, ele não grava linhas de processamento propriamente ditas (financeiro, por exemplo).

Caso existam erros, será exibido um pop-up intitulado **"Mensagem de retorno"**. Não existindo erros, será apresentada a mensagem de prévia realizada com sucesso e, em seguida, você pode processar o arquivo de retorno.

O botão ![Imagem 6: O botão "Processar" processará, efetivamente, o arquivo de retorno escolhido.](https://ajuda.sankhya.com.br/hc/article_attachments/15500175187991) **"Processar"** processará, efetivamente, o arquivo de retorno escolhido.

![Imagem 7: O botão "Processar" processará, efetivamente, o arquivo de retorno escolhido.](https://ajuda.sankhya.com.br/hc/article_attachments/360091394794)

Ao processar o retorno, dependendo da Ocorrência que retornar nos títulos, poderão ser executadas várias ações como: Registrar no Log, Reportar, Baixar, Conciliar, Alterar, Registrar Nosso Número e etc.

Por exemplo, num Arquivo de Retorno com:

- 4 títulos com ocorrência de Liquidação **-** **06**.
- 3 títulos com ocorrência de Entrada Confirmada **–** **02**.

Na configuração de Ocorrências do layout, marque **06** para Baixar, Conciliar e Registrar no Log e **02** para Registrar Nosso Número e Log.

Após o Processamento do Arquivo, encontram-se:

- 7 títulos registrados no Log (TSIOBCLOG);
- 4 títulos Baixados e Conciliados;
- 3 títulos com Registro de Nosso Número.

Todas as observações ou erros ocorridos após o processamento do retorno, serão exibidos no pop-up Mensagem de retorno.

**Nota:** ao realizar o Processamento do Arquivo de Retorno, caso o layout estruturado para processar o arquivo (tela [Configuração Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033)) não possua Identificador devidamente configurado, ou a marcação Detalhe não esteja realizada, será apresentada a seguinte mensagem:

**"Layout de arquivo divergente ao modelo cadastrado."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#top)

## Log do Processamento de Arquivo de Retorno

Note na tela, a seção Log de Processamento do Arquivo de Retorno que permitirá a visualização das informações geradas no Processamento do Arquivo. Você pode configurar um filtro personalizado, a fim de agilizar as consultas às prévias e aos processamentos, ou ainda, utilizar do preenchimento dos filtros fixos, ou seja, Número Único do Procesasmento/Prévia, Período de Ocorrência, o Tipo do procedimento realizado (Todos, Prévia ou Processado), Nome do Arquivo ou ainda, buscar os processamentos por meio das pessoas/usuários que o fizeram.

![Imagem 8: Note na tela, a seção Log de Processamento do Arquivo de Retorno que permitirá a visualização das informações geradas…](https://ajuda.sankhya.com.br/hc/article_attachments/360093554733)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#top)

## Relatórios e análises das ocorrências de Retorno

Acessando a tela [Logs de Ocorrências Bancárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606654), você poderá proceder com as análises de todas as Ocorrências que geraram Log e de todo o resultado do processamento.

![Imagem 9: Acessando a tela Logs de Ocorrências Bancárias , você poderá proceder com as análises de todas as Ocorrências que…](https://ajuda.sankhya.com.br/hc/article_attachments/360093555333)

Após o Processamento do Retorno Bancário, será possível acompanhar de uma forma bem ampla o resultado do processamento, por meio de relatórios aqui formatados. Pode-se, por exemplo, formatar um relatório contendo informações do Arquivo de Retorno processado, tais como:

- Nro. Financeiro;
- Nro. Linha;
- Dt. Ocorrência etc.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#top)

## Parâmetros que influenciam esta rotina

**Código do reg. de transação do retorno bancário - CODREGTRANSRET:** este parâmetro não é utilizado quando se trabalha com o processo de Configurações de ocorrências no Layout de Retorno bancário. Deverá ser configurado no Processamento de Retorno Bancário com chamada de Stored Procedure. O sistema lê apenas os Detalhes do arquivo. Informe, neste parâmetro, o código para se identificarem as Linhas de Detalhes.

Por exemplo, se no arquivo, as Linhas de Detalhes começam com o dígito **"1"**, informe **1** nesse parâmetro.

**Importante:** Só é válido para arquivos do tipo CNAB.

**Cód. lançamento bancário para baixa - CODLANCBAIXA:** informe neste parâmetro o código de Lançamento Bancário que será utilizado na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) para baixa de recebimentos no Processamento do Retorno Bancário.

**Cód. lançamento bancário para baixa de pagamentos - CODLANCBAIXAPAG:** insira neste parâmetro o código de Lançamento Bancário que será utilizado na Movimentação Financeira para baixa de pagamentos no Processamento do Retorno Bancário.

**TOP para baixa de recebimentos - TOPBAIXA:** neste parâmetro informe o código do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) que será empregado para baixa de recebimento no Processamento do Retorno Bancário, em relação à baixa automática de títulos.

**TOP para baixa de pagamentos - TOPBAIXAPAG:** ao inserir neste parâmetro o código do Tipo de Operação - TOP que será utilizado para baixa de pagamentos no Processamento do Retorno Bancário, em relação à baixa automática de títulos.

**Somar taxa ao valor da baixa no ret.banc. - SOMATXVLRBAIXA:** quando habilitado, ao realizar o Processamento de Arquivo de Retorno, o sistema somará o valor da Taxa Administrativa enviada pelo banco ao valor da baixa. Caso o arquivo já tenha sido processado, será exibida a seguinte mensagem:

**"ERRO: NUFIN=109100, NOSSONUM=029700032879, V.TITULO=0000000000200, V.RECEBIDO=0000000020000, TÍTULO JÁ BAIXADO."**

**Agrup. titulos receita na geração remessa edi - AGTITRECGERCEDI:** ao habilitar este parâmetro, o sistema estará apto a realizar o processamento de títulos agrupados desde que sejam consideradas as informações contidas no campo NUFIN, campo este que está inserido no layout de retorno e no arquivo de retorno.

**Validar Vlr no retorno diferente do Vlr do financeiro - VALVLRRETDIFFIN:** com este parâmetro habilitado será realizada a baixa do título de acordo com o valor que consta no arquivo e não conforme o valor informado na tela Movimentação Financeira.

**Manter Juros/Multas no Retorno de EDI Bancário - MANJURMULRETEDI:** este parâmetro tem o objetivo de não limpar o campo de juros e multa no processamento de retorno, quando o campo DTVENCINIC for menor que o campo DTVENC.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno#top)
