---
id: "24414482605463"
titulo: "Soma das partidas do lançamento, a débito, diferente do valor informado no registro de Lançamento Contábil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24414482605463-Soma-das-partidas-do-lan%C3%A7amento-a-d%C3%A9bito-diferente-do-valor-informado-no-registro-de-Lan%C3%A7amento-Cont%C3%A1bil"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:46:49Z"
rotulos: ["ECD", "Fiscal", "XML", "Importação", "Contabilização", "Soma das partidas do lançamento a débito", "registro de Lançamento Contábil", "Erro ao validar o arquivo ECD", "diferente do valor informado", "Erro"]
---

# Soma das partidas do lançamento, a débito, diferente do valor informado no registro de Lançamento Contábil

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24414482597143) **MENSAGEM:**

Erro ao validar o arquivo ECD: "Soma das partidas do lançamento, a débito, diferente do valor informado no registro de Lançamento Contábil."

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24414482601239)SOLUÇÃO:**

Na tela **"Importação de lote"** (Contabilidade » Rotinas » Importação de Lote)**,** caso a marcação "**Adiciona lançamentos em lotes já existentes"** esteja selecionada, as informações importadas serão incluídas em um lote para o qual já existe lançamentos contábeis de origem Contabilização. Com isso, as datas ficarão divergentes dos lançamentos importados.

**(1)** Nessa situação, exclua esses dois lançamentos na empresa de origem, contabilize novamente em outro lote e realize todo o processo de fechamento de lotes, zeramento, consolidação.

**(1)** Também um processo alternativo seria gerar o arquivo novamente, desmarcando a opção **"Gerar registro I200 considerando o número de documento/lançamento**".

Caso ao realizar a geração sem a marcação, o TXT importado no validador deixe de trazer os erros e passa a trazer as seguintes advertências:

**Advertência:** "Um lançamento pode ter vários registros a débito e vários a crédito somente quando relativos ao mesmo fato contábil (Resolução CFC 1299/2010). Verifique se a situação esta correta."
**(1)** **Fatos contábeis são ocorrências que alteram, qualitativa e/ou quantitativamente, o patrimônio.** Esta validação ocorre porque em um mesmo lançamento (I200) aparecem várias (I250) contas debitadas e várias contas creditadas. Na resolução citada acima, ao utilizar esta modalidade de lançamentos só pode se referir a um único fato contábil.

Se observar, esta orientação já está na Resolução:

**Lançamento contábil**
O lançamento contábil deve ter como origem um único fato contábil e conter:

(a) um registro a débito e um registro a crédito; ou

(b) um registro a débito e vários registros a crédito; ou

(c) vários registros a débito e um registro a crédito; ou

(d) vários registros a débito e vários registros a crédito, quando relativos ao mesmo fato contábil.

Ou seja, esta advertência seria apenas para fazer a verificação se os lotes estão corretos. É apenas para chamar a atenção em relação ao fato de um lançamento ter várias contas debitadas e várias contas creditadas, pois não tem como o PVA validar se pertencem ao mesmo fato contábil. 

A advertência apresentada não causa interferência na validação do arquivo ECD, é comum esse tipo de advertência quando existe importação dos lotes de depreciação, folha e etc.
Logo, trata-se de um comportamento normal na geração do arquivo. 

Assim, no momento de geração dos lançamentos contábeis com múltiplas partidas, será gerado o registro I200 separando cada lançamento presente no lote contábil e os registros I250. 

|I200|00101052022000100000000000001|01052022|1000,00|N||
|I250|1.1.1.10.001|0|500,00|C|100||||
|I250|1.1.1.11.001|0|500,00|C|100||||
|I250|2.1.1.10.001|0|1000,00|D|100||||

|I200|00101052022000100000000000002|01052022|1000,00|N||
|I250|1.1.1.10.001|0|500,00|C|100||||
|I250|1.1.1.11.001|0|500,00|C|100||||
|I250|2.1.1.10.001|0|1000,00|D|100||||

Logo, utilizando o método de partida simples/partida dobrada serão gerados os registro I200 separando os lançamentos por dia. 

|I200|0010105202200020000|01052022|3000,00|N||
|I250|1.1.1.11.001|0|1000,00|C|200||||
|I250|2.1.1.10.001|0|1000,00|D|200||||
|I250|1.1.1.10.001|0|2000,00|C|201||||
|I250|2.1.1.10.001|0|2000,00|D|201||||

Portanto, uma possível solução para a advertência apresentada seria a marcação da opção 'Gerar registro I200 considerando o número de documento/lançamento'.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24414438423063)CAUSA:**

Ao validar o ECD a mensagem é apresentada.
