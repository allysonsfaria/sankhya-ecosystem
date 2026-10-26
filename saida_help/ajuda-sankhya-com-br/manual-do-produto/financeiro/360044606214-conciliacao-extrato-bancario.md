---
id: "360044606214"
titulo: "Conciliação Extrato Bancário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-10-12T13:35:53Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Layout", "Movimentação Financeira", "Importação", "EDI", "Extrato", "Financeiro", "banco", "Bancário", "cheque", "Conciliação", "Conciliação de Extrato Bancário", "conta", "Número Importação", "br.com.sankhya.mgefin.mov.conciliacaoextratobancario", "Conciliação Extrato Bancário manual", "Conciliação Bancária", "Importação automática de extratos com identificação de cheques", "Configuração inicial de contas e layout para importação", "Conciliação com gerenciamento de despesas por data e valor"]
---

# Conciliação Extrato Bancário

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312281170711) Módulo: Financeiro > Rotinas
```

---

Essa rotina permite a realização de conciliações de extratos bancários automaticamente, por meio de um arquivo, disponibilizado pelo banco, e importado no sistema. Com esse processo o sistema identificará cheques presentes no sistema e no arquivo, e lançamentos por meio do número do documento. Será permitido o vínculo manual de lançamentos do sistema com dados do arquivo, para os que não forem encontrados automaticamente; por fim, você pode conciliar os que já estiverem lançados, gerando lançamentos no financeiro para registros, que constam no arquivo e não constam no sistema, esses lançamentos já serão automaticamente baixados e conciliados. Referente a essa tela, teremos os seguintes tópicos:

| [Configurações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#configura%C3%A7%C3%B5esiniciais) |  | [Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#cheques) |
| --- | --- | --- |
| [Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#despesas) |  | [Busca de Data e valor de lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#buscadedataevalordelan%C3%A7amento) |
| [Conciliação manual](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#concilia%C3%A7%C3%A3omanual) |  |  |

---

## Configurações Iniciais

Para utilização desta rotina, são necessárias as seguintes configurações:

![Imagem 2: No Cadastro de Contas Bancárias , aba Intercâmbio Eletrônico de Dados (EDI) , configure o campo "Categoria p/…](https://ajuda.sankhya.com.br/hc/article_attachments/16196134676887) No [Cadastro de Contas Bancárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113), aba [Intercâmbio Eletrônico de Dados (EDI)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113#abaintercmbioeletrnicodedadosedi), configure o campo **"Categoria p/ lançamento de cheque"**; essa categoria é utilizada para identificar no arquivo importado quais registros devem ser considerados como cheques. Trata-se de um número de 3 (três) dígitos disponibilizado pelo banco. Por exemplo: no layout do Banco do Brasil, o código é 101.

![Imagem 3: Depois, na tela Configuração Arquivo de Retorno , você deve criar um layout de importação do arquivo marcando…](https://ajuda.sankhya.com.br/hc/article_attachments/16196119597719) Depois, na tela [Configuração Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033), você deve criar um layout de importação do arquivo marcando **"Conciliação Extrato Bancário"**, esse layout deve conter:

**- No Header:** CONVENIO, CODBCO.

**- Nos Registros de Lançamento:** NROCTA, DTLANC, VALOR, NRODOC, CODCATEG, CNPJ\_CPF, HIST.

![Imagem 4: Em seguida, na tela Conf. Lançamento de Conciliação de Ext. Bancário configure alguns registros com parâmetros que…](https://ajuda.sankhya.com.br/hc/article_attachments/16196119600663) Em seguida, na tela [Conf. Lançamento de Conciliação de Ext. Bancário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115273) configure alguns registros com parâmetros que servirão para lançamento, baixa e conciliação das despesas, que o sistema irá identificar no arquivo. Essas despesas são aquelas que não estão presentes no sistema ainda e estão apenas no arquivo, elas serão apresentadas na etapa despesas no momento da conciliação. Elas serão identificadas no arquivo por meio do campo **"Histórico"** (campo HIST do layout). Você deve se atentar para o correto preenchimento do histórico em cada registro criado nesta tela.

Feitas as devidas configurações, na tela **Conciliação Extrato Bancário** complete os campos a seguir:

![Imagem 5: Feitas as devidas configurações, n a tela Conciliação Extrato Bancário complete os campos a seguir:](https://ajuda.sankhya.com.br/hc/article_attachments/4408405470231)

No campo **"Conta"** informe a Conta bancária referente ao extrato bancário.

Depois, preencha no campo **"Empresa do Financeiro"** a empresa que será utilizada para lançamento de títulos financeiros de despesas no sistema. Essa empresa deve ser a mesma utilizada nos cadastros feitos na tela Conf. Lançamento de Conciliação de Ext. Bancário, pois o sistema utilizará a empresa informada neste campo para encontrar a configuração a ser aplicada no lançamento dos títulos.

Em **"Período de Lançamento"** informe o período dos títulos que se deseja conciliar.

O campo **"Número Importação"** é utilizado quando uma importação foi previamente realizada, ou seja, pode-se importar um arquivo e fazer parte de sua conciliação, sendo possível retornar posteriormente à tela e continuar o processo, sem que seja preciso importar novamente o arquivo. Caso ainda não tenha sido importado o arquivo, esse campo será preenchido automaticamente, após o processamento do arquivo. Sendo informado um Número Importação o sistema irá inabilitar os campos **"Layout EDI"** e **"Arquivo"**, e o botão **"Processar"**.

Por meio do botão ![Imagem 6: Por meio do botão "Excluir importação OFX" , pode-se excluir a importação de um arquivo OFX realizado indevidamente.…](https://ajuda.sankhya.com.br/hc/article_attachments/21492294032279) **"Excluir importação OFX"**, pode-se excluir a importação de um arquivo OFX realizado indevidamente. Porém, esse botão estará disponível apenas quando o parâmetro **"Permitir exclusão do arquivo OFX importado - OFXCONFIG"** for habilitado e o campo Número Importação configurado. 

Caso o arquivo tenha sido apenas importado, basta que essa importação seja excluída e realizada uma nova com o arquivo correto. Entretanto, se o arquivo foi importado e em seguida, realizadas as criações das tarifas bancárias e conciliação manual, ao tentar excluir a importação, a mensagem abaixo será exibida:

**"Existem títulos vinculados a essa importação. Faça a exclusão ou desconciliação dos mesmos. Nros únicos: xxx, xxxx."**

Assim, para realizar a exclusão, os títulos exibidos na mensagem devem ser desconciliados na tela [Conciliação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673) e, em seguida, a importação do arquivo OFX deletada. 

Após isso, quando pressionar novamente o botão Excluir importação OFX, outra mensagem será aberta, que informa:

**“Excluir Importação de Arquivo OFX**

**Esta ação não poderá ser desfeita. Deseja Excluir?”**

Ao selecionar a opção **"Sim"** o processo é executado e os arquivos são excluídos.

**Nota:** é possível, se desejar, realizar a importação de um arquivo anteriormente excluído, basta seguir a mesma rotina.

**Observação:** as tarifas bancárias criadas pela importação não serão excluídas automaticamente, de forma que, estas devem ser excluídas manualmente, caso deseje.

Ao buscar um arquivo pelo Número Importação, o pop-up aberto para realização desta busca, conta com os campos **"Núm. Importação"**, **"Data da Importação"**, **"Nome do Arquivo"** e **"Data do Processamento"** que visam auxiliar no refinamento e melhoria da pesquisa.

Selecione no campo **"Tipo do Arquivo"** a categoria do arquivo, conforme as seguintes opções:

- Texto: arquivos no formato padrão CNAB (linhas e colunas);
- OFX: arquivos no formato OFC/OFX.

**Observação:** A respeito do arquivo OFX, o campo **"Memo"** é histórico e o campo **"TRNTYPE"** corresponde ao **"Tipo de Transação OFX"**.

Informe em **"Layout EDI"** o número do layout previamente cadastrado.

**Nota:** Ao selecionar no campo Tipo do Arquivo, a opção OFX, o campo Layout EDI será desabilitado.

**Observação:** para conciliar o arquivo OFX, de forma a aumentar ou diminuir a quantidade da cláusula IN, ligue o parâmetro **"Limite hash por consulta no extrato bancário - LIMITEHASHCONST"**. Porém, ao utilizá-lo, pode ser necessário diminuir a quantidade informada no parâmetro até que a seguinte mensagem pare de ser exibida:

**"ORA-01013: o usuário solicitou o cancelamento da operação atual"**

No campo **"Arquivo"** clique no botão ![Imagem 7: No campo " Arquivo" clique no botão para selecionar e efetuar o upload do arquivo de extrato bancário.](https://ajuda.sankhya.com.br/hc/article_attachments/4408404896407)para selecionar e efetuar o upload do arquivo de extrato bancário.

Feita a escolha do Layout EDI e do Arquivo, clique no botão **"Processar"** para aferição do arquivo; cada arquivo poderá ser processado apenas uma vez. Dado que o arquivo tenha sido processado, o campo Número Importação será preenchido automaticamente e o botão **"Próximo"** localizado na parte inferior direita da tela será habilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#top)

## Cheques

![Imagem 8: Cheques](https://ajuda.sankhya.com.br/hc/article_attachments/4409283436951)

Ao clicar no botão Próximo, a etapa dos Cheques apresentará todos os lançamentos nos quais o campo TRNTYPE esteja com a informação CHECK (arquivo OFX) ou que o campo **"Cód. Categoria"** seja igual ao configurado na conta e estes lançamentos estejam na tabela de Movimento Bancário (TGFMBC) como não conciliados.

Esta etapa é apenas para visualização, assim, clique em **"Próximo"** para dar continuidade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#top)

## Despesas

![Imagem 9: Despesas](https://ajuda.sankhya.com.br/hc/article_attachments/4409291830551)

Visualize esta etapa quando o sistema localizar despesas.

A origem das despesas está em títulos que existem apenas no arquivo e que o Sankhya OM identificou ao comparar os campos HIST e CODCATEG do layout com o **Histórico** e Categoria de Lançamento cadastrados na tela [Conf. Lançamento de Conciliação de Ext. Bancário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115273).

Assim como na etapa anterior, esta tela é apenas para conferência. Para prosseguir, clique em **Próximo**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#top)

## Conciliação Manual

![Imagem 10: Conciliação Manual](https://ajuda.sankhya.com.br/hc/article_attachments/4409291881879)

Esta etapa sempre será apresentada e nela você pode visualizar duas grades, sendo que a da esquerda exibe os registros no sistema da conta em análise e que ainda não foram conciliados; já a grade da direta, apresenta os registros do arquivo que não foram conciliados nos passos anteriores. Ambas as grades também filtram pelo período selecionado no início da utilização da rotina.

De acordo com a coloração, tem-se a distinção entre os registros apresentados nas grades. Deste modo, as receitas são exibidas na cor **azul** e as despesas na cor **vermelha**.

Por meio desta etapa, você pode selecionar os registros nas duas grades para proceder com a conciliação e clicar em **"Salvar"**. É importante mencionar que, para que seja possível salvar a conciliação, os Totais selecionados nas grades estejam iguais.

A conciliação pode ser feita selecionando todos os registros de uma só vez, ou separadamente e clicando em Salvar. Ao Salvar, o sistema removerá os registros previamente selecionados de ambas as grades.

**Observação:** Você poderá conciliar lançamentos financeiros que foram desconciliados do arquivo de extrato bancário, ou seja, é possível desconciliar mais de um registro no sistema que foi conciliado pelo arquivo bancário, sem limitação na quantidade de registros.

Uma vez finalizadas e salvas as seleções, ao clicar em **"Concluir"**, o sistema irá conciliar todos os cheques e títulos correspondentes às etapas anteriores, lançando, baixando e conciliando os títulos de despesas, que não estavam lançados no sistema e conciliando os registros selecionados manualmente neste último passo. Após esses procedimentos, será apresentada uma tela de finalização.

![Imagem 11: O sistema permitirá a inclusão apenas de lançamentos de despesas, sem a possibilidade de registrar receitas.](https://ajuda.sankhya.com.br/hc/article_attachments/27251341957911) O sistema permitirá a inclusão apenas de lançamentos de despesas, sem a possibilidade de registrar receitas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#top)

## Busca de Data e Valor e Lançamento

Para buscar corretamente a data de lançamento, é necessário preencher na coluna **"Nome do Campo"** o campo correspondente à DTLANC o valor de DTLANCDDMMYYYY na tela [Configuração de Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033). Isso porque, no arquivo de retorno a data está no formato DDMMYYYY (08092017).

Já em relação ao valor de lançamento, para que seja efetuada a busca corretamente, você deve realizar a configuração do campo **"VALOR"** indicando a posição de **"Inicio"** e **"Fim"** na tela Configuração de Arquivo de Retorno.

**Observação:** Para os campos DTLANC e VALOR existe a possibilidade de se utilizar configurações diferentes de acordo com o layout do arquivo, ou seja:

- Os formatos válidos para DTLANC são:

DTLANC (Padrão DDMMYY), DTLANCDDMMYYYY, DTLANCYYYYMMDD, DTLANCYYMMDD

- O ajuste para o campo VALOR, por padrão são 2 decimais. Quando se desejar 3 ou 4 decimais, deve-se utilizar:

VALOREEE (3 decimais) e VALOREEEE (4 decimais).

Na configuração de um arquivo de retorno de conciliação de extrato bancário, as variáveis abaixo possuem as respectivas representações:

**DTLANC**                                   Formato de data importada: DDMMYY

**DTLANCDDMMYYYY**            Formato de data importada: DDMMYYYY

**NROCTADIGITO**                      Digito da conta bancaria

**Nota:** Nos casos da configuração do processamento do retorno bancário, o identificador **"DigitodaConta"** atende aos padrões do banco ITAÚ para número de conta, e também diferencia pelo "dígito" as contas que eventualmente tenham números iguais. Este campo é ligado ao campo **"Conta"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606214-Concilia%C3%A7%C3%A3o-Extrato-Banc%C3%A1rio#top)
