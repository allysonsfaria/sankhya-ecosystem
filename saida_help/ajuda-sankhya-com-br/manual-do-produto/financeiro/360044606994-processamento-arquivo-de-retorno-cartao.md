---
id: "360044606994"
titulo: "Processamento arquivo de retorno cartão de crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606994-Processamento-arquivo-de-retorno-cart%C3%A3o-de-cr%C3%A9dito"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:41:18Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "br.com.sankhya.mgefin.kaplen", "Processamento arquivo de retorno cartão de crédito manual", "TOP", "Financeiro", "Conciliação Bancária", "Validações de arquivo e inconsistências processadas no sistema", "Automatiza baixa e conciliação de vendas via cartão", "Configurações de parâmetros influenciam baixa e ajustes financeiros", "Cartão de Crédito"]
---

# Processamento arquivo de retorno cartão de crédito

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312372358423)Módulo: Financeiro > Rotinas
```

---

![Imagem 2: A apresentação/utilização desta tela, é vinculada ao produto "20490 - JIVA-PROCES. DO RETORNO CARTÃO CREDITO" .](https://ajuda.sankhya.com.br/hc/article_attachments/16540202973975) A apresentação/utilização desta tela, é vinculada ao produto **"20490 - JIVA-PROCES. DO RETORNO CARTÃO CREDITO"**.

O objetivo dessa rotina, é permitir a realização de maneira automatizada, a baixa e a conciliação bancária das movimentações financeiras que utilizaram como forma de pagamento o cartão, seja ele credito ou débito.

Esse processo acontece com base em um extrato de pagamento, onde a operadora de cartão demonstra o valor repassado ao estabelecimento comercial, considerando as operações (vendas) de um determinado período. Normalmente, esse arquivo é disponibilizado pela operadora de cartão a partir da adesão de um serviço adicional.

Essa rotina faz sentido em estabelecimentos comerciais, onde existe um alto volume de transações, pois permite realizar o processo de baixa e conciliação bancária de suas vendas de uma forma bastante rápida e segura.

[Layout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606994-Processamento-arquivo-de-retorno-cart%C3%A3o-de-cr%C3%A9dito#layout)                                                                               [Rotina de Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606994-Processamento-arquivo-de-retorno-cart%C3%A3o-de-cr%C3%A9dito#rotinadeprocessamento)

[Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606994-Processamento-arquivo-de-retorno-cart%C3%A3o-de-cr%C3%A9dito#par%C3%A2metrosqueinfluenciamestarotina)

![Imagem 3: Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4416134072727)

## Layout

O arquivo esperado pela rotina Processamento arquivo de retorno cartão de crédito, deverá ser da extensão **".txt"**, com base no layout detalhado abaixo, composto por um cabeçalho (header) e um detalhe referente ao crédito de venda:

![Imagem 4: O arquivo esperado pela rotina Processamento arquivo de retorno cartão de crédito , deverá ser da extensão ".txt" , com…](https://ajuda.sankhya.com.br/hc/article_attachments/4416141321367)

![Imagem 5: O arquivo esperado pela rotina Processamento arquivo de retorno cartão de crédito , deverá ser da extensão ".txt" , com…](https://ajuda.sankhya.com.br/hc/article_attachments/4416123937815)

Abaixo, temos as tabelas citadas na coluna Detalhes:

![Imagem 6: Abaixo, temos as tabelas citadas na coluna Detalhes :](https://ajuda.sankhya.com.br/hc/article_attachments/4416141357207)

**Nota:** as informações especificadas nas tabelas acima não são utilizadas pelo sistema para efetuar o processamento do arquivo. Contudo, estes dados podem ser retornados no arquivo que corresponde ao seu fornecedor.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606994-Processamento-arquivo-de-retorno-cart%C3%A3o-de-cr%C3%A9dito#top)

## Rotina de Processamento

Quando o botão ![Imagem 7: Quando o botão "Prévia" for acionado, exibe para você uma prévia do processamento do arquivo de retorno; exibe…](https://ajuda.sankhya.com.br/hc/article_attachments/16540477693591) **"Prévia"** for acionado, exibe para você uma prévia do processamento do arquivo de retorno; exibe informações dos registros que não podem ser baixados por algum motivo, pela rotina, em um arquivo texto. A prévia roda uma simulação de baixa e mostra os retornos do processamento, porém, não efetua a baixa.

O botão ![Imagem 8: O botão "Processar" realiza o processamento do arquivo de retorno, baixando os títulos presentes com suas respectivas…](https://ajuda.sankhya.com.br/hc/article_attachments/16540477696151)**"Processar"** realiza o processamento do arquivo de retorno, baixando os títulos presentes com suas respectivas taxas administrativas e, se configurado, fazendo a conciliação bancária dos mesmos.

Ao solicitar a prévia ou processar o arquivo, teremos na tela, a grade de informações **"Créditos de vendas"** e o formulário de **"Financeiro"** que serão alimentados com os dados do arquivo de retorno da operadora de cartão, e as informações do financeiro do sistema em formulário, respectivamente. As mensagens pertinentes ao processamento, serão apresentadas na referida grade, na coluna **"Mensagem"**.

**(1)** **Como é feito o processamento?**

O arquivo de processamento deve seguir o layout do arquivo de retorno cartão de crédito, respeitando o tipo de registro 3 - Créditos de venda.

O sistema tenta identificar o título financeiro do Sankhya Om, comparando as seguintes informações do arquivo com as informações da tabela TGFTEF:

- DTTRANSACAO – Data da venda.
- DESDOBRAMENTO – Número da parcela.
- VLRTRANSACAO – Valor líquido da parcela.
- AUTORIZACAO – Número da autorização gerado pela operadora (a verificação pode ser ignorada no arquivo de retorno).
- NSU - Sendo que a pesquisa compara o resultado do arquivo com os seguintes campos da TGFTEF:
- NUMCV – Número do comprovante de venda gerado pela operadora.
- NUMDOC – Número do documento gerado pela operadora.
- NUMNSU – Número sequencial único (NSU) gerado pela operadora

**Importante:** o sistema utiliza o valor da taxa de administração, valor líquido da parcela e número do desdobramento vindos do arquivo de processamento. Por isso, é importante que as informações da TGFTEF (tabela das transferências eletrônicas de fundos) estejam de acordo com as informações da TGFFIN (tabela do financeiro), para que não seja gerada inconsistência.

**Validações realizadas:**

**1)** Extensão do arquivo, se arquivo em branco ou fora do layout aceitável:

**Aviso: Arquivo inválido.**

**2)** Se o título já foi baixado:

**ERRO: NSU: 000000000, Autorização: 000000, Data da Venda: XX/YY/ZZZZ, Parcela: X, Título Financeiro: YYY, Título já baixado!**

**3)** Se o título não foi encontrado:

**ERRO: NSU: 000000000, Autorização: 000000, Data da Venda: XX/YY/ZZZZ, Parcela: X, Título não encontrado!**

**4)** Se existem inconsistência nos valores:

**ERRO: NSU: 000000000, V.TITULO= 000000, V.RECEBIDO= 00000, Valor da baixa maior que o calculado!, NUFIN= XXX**

**Importante:** vale mencionar que estas validações serão apresentadas na coluna **"Mensagem"**, presente na grade **"Critérios de vendas"**.

O sistema realizará a baixa e conciliação bancária de acordo com a configuração dos parâmetros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606994-Processamento-arquivo-de-retorno-cart%C3%A3o-de-cr%C3%A9dito#top)

## Parâmetros que influenciam esta rotina

No parâmetro**"TOP para baixa de recebimentos - TOPBAIXA"** informe o código do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) que será empregado para baixa de recebimento no Processamento do Retorno Bancário, em relação à baixa automática de títulos.

Informe no parâmetro**"Cód. lançamento bancário para baixa - CODLANCBAIXA"**o código de Lançamento Bancário que será utilizado na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) para baixa de recebimentos no Processamento do Retorno Bancário.

Quando o parâmetro **"Tipo de ajuste no Retorno Kaplen - KPLOPCBAIXA"**estiver configurado com a opção **"Baixar mantendo o valor do financeiro"**, o sistema utilizará o arquivo da operadora de cartão apenas para identificar o título a ser baixado, e considerará os valores do financeiro, independente de divergências.

**Observação:** quando o parâmetro KPLOPCBAIXA estiver configurado com a outra opção, **"Baixar mantendo o valor do arquivo"**, o sistema verificará qualquer divergência de valores da taxa administradora e valor do título, entre o título do financeiro e o valor. Se a divergência estiver dentro do aceitável, será atualizado o valor do título financeiro de acordo com o valor do arquivo.

Ao clicar em **"Prévia/Processar"**, será verificado o valor informado no parâmetro **"Valor limite diverg. arred. baixa retorno Kaplen - KPLLIMTDIVERGBX"**; sendo maior que 1 real, será apresentada a seguinte mensagem:

**"Atenção! A tolerância para divergência não deve ser maior que 1, ajuste o parâmetro "KPLLIMTDIVERGBX" para prosseguir."**

Se existir divergência no valor bruto e/ou taxa do arquivo, o sistema irá verificar se esta se encontra dentro do limite do parâmetro KPLLIMTDIVERGBX para realizar a baixa.

**Observação:** os parâmetros KPLOPCBAIXA e KPLLIMTDIVERGBX atuam sobre o processamento de arquivo da KAPLEN.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606994-Processamento-arquivo-de-retorno-cart%C3%A3o-de-cr%C3%A9dito#top)
