---
id: "360044606454"
titulo: "Processamento de Retorno Automático"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:39:39Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "TOP", "Financeiro", "br.com.sankhya.mgefin.agendador.processamento.retorno.bancario", "Processamento de Retorno Automático manual", "Processamento automático de arquivos bancários", "Configuração de diretórios e layouts de retorno", "Parâmetros influenciam baixa e registros financeiros", "Parâmetros para baixa e validação de títulos", "Processamento automático de arquivos de retorno bancário", "Configurações de layout diretórios e logs", "EDI Bancário", "Retorno Automático"]
---

# Processamento de Retorno Automático

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312313937303) Módulo: Financeiro > EDI Bancário
```

---

A tarefa de executar o processamento do arquivo de retorno consiste em pegar um arquivo texto disponibilizado pela instituição financeira e processar no sistema, a fim de manter os dados de cobrança/pagamentos da empresa atualizados conforme situação atual junto ao banco. No arquivo de retorno podem existir as seguintes informações:

- **Entrada confirmada:** A cobrança (boleto) ou despesa gerada pela empresa e comunicado ao banco, foi compreendido e está em carteira junto ao banco;
- **Baixa confirmada de cobrança:** A solicitação para retirar a cobrança da carteira de cobrança do título foi acabada;
- **Liquidação da cobrança:** O cliente (pagador) efetuou o pagamento da cobrança (boleto) e o banco comunica a empresa que o pagamento foi realizado e que o dinheiro foi repassado a empresa.

Essa rotina tem o objetivo de substituir a necessidade de se executar essa tarefa manualmente, então, sempre que um arquivo de retorno for disponibilizado em um diretório preestabelecido (conforme configuração), o processamento será executado automaticamente.

O campo **"Código"** pode ser alimentado manualmente ou automática; essa definição é feita pelo botão **"Configuração da tela"** localizado no lado direito do topo da tela. Informe nesse campo, a numeração identificadora do processamento.

O nome do processamento que está sendo criado é indicado por meio do campo **"Descrição"**.

Através da opção **"Ativa"** poderemos apontar se o processamento está ativo ou não.

Dessa forma, você acessar os links abaixo para saber mais sobre a tela: 

| [Aba Configurações de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico#abaconfiguraesderetorno) |  | [Aba Histórico de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico#abahistricoderetorno) |
| --- | --- | --- |
| [Relatórios e análises das ocorrências...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico#relatrioseanlisesdasocorrnciasderetorno) |  | [Parâmetros que influenciam na tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico#parmetrosqueinfluenciamnoprocessamentoderetorno) |

![Imagem 2: Parâmetros que influenciam na tela](https://ajuda.sankhya.com.br/hc/article_attachments/4416141244823)

## Aba Configurações de Retorno

Por meio do campo **"Layout"**, selecione o layout de retorno configurado. Os referidos layouts são configurados na rotina de [Configuração Arquivo Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033).

No campo **"Diretório p/ processamento"**, aponte o diretório ao qual a execução deve buscar o arquivo de retorno que será processado.

O campo **"Diretório p/ processados"**, tem a finalidade de indicar o diretório ao qual a execução irá inserir o arquivo de retorno processado, ou seja, após processamento o sistema move o arquivo lido do Diretório p/ processamento para o diretório Diretório p/ processados.

**Nota:** os campos Diretório p/ processamento e Diretório p/ processados devem ser preenchidos como apresentados no repositório de arquivos. Observe os exemplos abaixo:

- Diretório p/ processamento = EDI/BOAVISTA/retorno/vendas/
- Diretório p/ processados = EDI/BOAVISTA/retorno/processado/vendas

---

| ![Imagem 3: Importante:](https://ajuda.sankhya.com.br/hc/article_attachments/42312313938199) **Importante:** |
| --- |
| Essa rotina utiliza o repositório de arquivos do sistema, então o diretório especificado no campo acima, corresponde a um diretório do repositório de arquivos. De forma que, este sofrerá muita influência do parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"**:   - Se o parâmetro estiver preenchido, a raiz do repositório de arquivos será o caminho indicado no mesmo; - Caso não for preenchido, a raiz do repositório de arquivos será um diretório chamado **".sw\_file\_repository"** no diretório home do usuário (<home\_user>\.sw\_file\_repository). |

---

Ao marcar essa opção **"Usar o banco junto com Nosso Número para localizar o título"**, a busca pelo título no banco de dados, será feita tanto pelo Nosso Número do título quanto pelo Código do Banco.

No campo **"Obter o valor do título do próprio título"**, teremos que, se nas ocorrências você optar por efetuar a baixa, ao realizar a baixa no processamento do retorno, em vez de pegar o valor do arquivo de retorno, o valor no banco de dados que será utilizado.

Quando a marcação **"Considerar juros e multa negociados"** for acionada, o processamento do arquivo utilizará o valor líquido do título, ou seja, os valores de juros e multa do mesmo que serão considerados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico#a)

## Aba Histórico de Retorno

Essa aba contém o histórico de processamento de cada um dos arquivos lidos pela aplicação no diretório Diretório p/ processamento. É possível visualizar informações sobre o arquivo em questão como seu nome, quantidade de linhas, entre outros.

![Imagem 4: Essa aba contém o histórico de processamento de cada um dos arquivos lidos pela aplicação no diretório Diretório p/…](https://ajuda.sankhya.com.br/hc/article_attachments/4416169256855)

| ![Imagem 5: Essa aba contém o histórico de processamento de cada um dos arquivos lidos pela aplicação no diretório Diretório p/…](https://ajuda.sankhya.com.br/hc/article_attachments/42312313938199) | Por meio do botão **"Log de Ocorrências"**, é possível acessar o log do processamento, Esse log, armazena os detalhes sobre uma das linhas lidas do arquivo processado. |
| --- | --- |

Através do botão ![Imagem 6: Através do botão "Outras Opções..." , opção "Manter apenas registros recentes" configure a limpeza automática nos logs…](https://ajuda.sankhya.com.br/hc/article_attachments/16540528288407) **"Outras Opções..."**, opção **"Manter apenas registros recentes"** configure a limpeza automática nos logs de histórico.

![Imagem 7: Através do botão "Outras Opções..." , opção "Manter apenas registros recentes" configure a limpeza automática nos logs…](https://ajuda.sankhya.com.br/hc/article_attachments/4416162943639)

Por meio do parâmetro **"Período p/ manter log de histórico de retorno - PERMANTHISTRET"** defina em dias o período ao qual os logs serão armazenados, ou seja, definindo o referido parâmetro com valor 20, a limpeza automática será realizada para os arquivos com mais de 20 dias de geração. De forma que, somente os arquivos recentes serão mantidos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico#a)

## Relatórios e análises das ocorrências de Retorno

Ao acessar a tela [Logs de Ocorrências Bancárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606654), proceder com as análises de todas as Ocorrências que geraram Log e de todo o resultado do processamento.

![Imagem 8: Ao acessar a tela Logs de Ocorrências Bancárias , proceder com as análises de todas as Ocorrências que geraram Log e de…](https://ajuda.sankhya.com.br/hc/article_attachments/8761315332503)

Após o processamento do retorno bancário, você poderá acompanhar de uma maneira ampla o resultado do processamento, por meio de relatórios aqui formatados. Será possível, por exemplo, formatar um relatório contendo informações do **"Arquivo de Retorno"** processado, tais como:

- Nro. Financeiro;
- Nro. Linha;
- Dt. Ocorrência etc.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico#a)

## Parâmetros que influenciam na rotina

**Código do reg. de transação do retorno bancário - CODREGTRANSRET:** Não é utilizado quando se utiliza o processo de Configurações de ocorrências no Layout de Retorno bancário. Deve ser configurado no processamento de retorno bancário com chamada de Stored Procedure. O sistema lê apenas os Detalhes do arquivo. Assim, informe nesse parâmetro, o código para se identificarem as Linhas de Detalhes. Por exemplo, se no arquivo, as Linhas de Detalhes começam com o dígito "1", informa-se 1 nesse parâmetro. Importante frisarmos ainda que, esse procedimento é válido somente para arquivos do tipo CNAB.

**Cód. lançamento bancário para baixa - CODLANCBAIXA:** Insira nesse parâmetro o código de Lançamento Bancário que será utilizado na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) para baixa de recebimentos no Processamento do Retorno bancário.

**Cód. lançamento bancário para baixa de pagamentos - CODLANCBAIXAPAG:** Aqui, pode-se inserir o código de Lançamento Bancário que será utilizado na Movimentação Financeira para baixa de pagamentos no Processamento do Retorno bancário.

**TOP para baixa de recebimentos - TOPBAIXA:** Configure esse parâmetro com o código do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) que será empregado para baixa de recebimento no Processamento do Retorno bancário, em relação à baixa automática de títulos.

**TOP para baixa de pagamentos - TOPBAIXAPAG:** Deve-se inserir o código do Tipo de Operação - TOP que será utilizado para baixa de pagamentos no Processamento do Retorno bancário, em relação à baixa automática de títulos.

**Somar taxa ao valor da baixa no ret.banc. - SOMATXVLRBAIXA:** Ao realizar o Processamento de Retorno Automático, o sistema soma o valor da Taxa Administrativa enviada pelo banco ao valor da baixa. Caso o arquivo já tenha sido processado, será exibida a seguinte mensagem de erro:

**"ERRO: NUFIN=109100, NOSSONUM=029700032879, V.TITULO=0000000000200, V.RECEBIDO=0000000020000, TÍTULO JÁ BAIXADO."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606454-Processamento-de-Retorno-Autom%C3%A1tico#a)
