---
id: "26790340625687"
titulo: "Manual da rotina Follow-Up de Importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26790340625687-Manual-da-rotina-Follow-Up-de-Importa%C3%A7%C3%A3o"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:40:39Z"
rotulos: ["Projeto", "Importação", "TOP", "Estoque", "Manual da rotina Follow-Up de Importação", "br.com.sankhya.FollowUpImportacao", "Follow-up", "Comércio Exterior"]
---

# Manual da rotina Follow-Up de Importação

## Follow Up Importação

Comércio Exterior > Rotinas

O Follow Up de importação é uma ferramenta de controle das datas previstas e realizadas em cada processo de importação. Ele permite a inserção de informações detalhadas sobre cada etapa, facilitando o acompanhamento do status de cada processo.

## 1. Criando o Follow Up

O Follow Up é criado automaticamente, assim que o projeto é vinculado a um Pedido de compra, que seja vinculado a uma TOP (Tipo de Operação), que esteja marcado a opção “Pedido de Compra Importação”.

No Follow Up, serão criados os Follow Ups de cada processo de importação individualmente, onde o usuário poderá ter o controle das datas de previsão e realização de cada etapa da importação, desde a fabricação no exterior até a chegada no estoque da empresa.

![Imagem 1: No Follow Up, serão criados os Follow Ups de cada processo de importação individualmente, onde o usuário poderá ter o…](https://ajuda.sankhya.com.br/hc/article_attachments/26790302355607)

## 2. Datas e Lead Times Follow Up de Importação

O Follow Up de importação, possui Datas previstas, Datas Realizadas e Lead Times, para que o seja possível colocar as informações no sistema e o usuário ter um acompanhamento de todas as etapas previstas do processo de importação.

**Data Fabricação - Prevista:** nesse campo o usuário deve informar qual é a data de início de Fabricação prevista passado pelo fornecedor.

**Lead Time fabricação (Dias):** informar a quantidade de dias que deve se considerar para calcular a “Data de Prontidão Prevista”.

**Data de Prontidão Prevista:** a data de prontidão prevista se dá pelo seguinte cálculo: “Data Negociação Pedido” + “Lead Time fabricação (Dias).

**Data Fabricação - Realizada:** nesse campo o usuário deve informar a Data de Fabricação realizada.

**Data de Prontidão Realizada:** nesse campo o usuário deve informar a Data que a mercadoria está pronta, que vai ser passada pelo fornecedor.

**Lead Time de Embarque (Dias):** informar a quantidade de dias que o sistema deve considerar para calcular a “Data de Embarque Prevista”.

**Data Embarque Previsto:** a data de Embarque Previsto se dá pelo seguinte cálculo: “Data de Prontidão Prevista” +" Lead Time de Embarque (Dias)”.

**Data de embarque realizada:** nesse campo o usuário deve informar a data que a mercadoria embarcou no país de origem.

**Transtime (Dias):** nesse campo o usuário deve informar a quantidade de dias que o sistema deve considerar para calcular a “Data de Chegada Prevista”.

**Data de Chegada Prevista:** a data de chegada prevista se dá pelo seguinte cálculo: “Data de Embarque Previsto" + “Transtime”.

**Data de Chegada Realizada:** nesse campo o usuário deve informar a data de chegada da mercadoria no porto.

**LeadTime de Desembarque (Dias):** informar a quantidade de dias que o sistema deve considerar para calcular a “Data de Desembarque Prevista”.

**Data de Desembarque Prevista:** a data de desembarque prevista se dá pelo seguinte cálculo: “Data de Chegada Realizada” + “Lead Time de Desembarque (Dias).

**Lead Time de Desembaraço (Dias):** informar a quantidade de dias que o sistema deve considerar para calcular a “Data de Desembaraço Prevista”

**Data de Desembaraço Prevista:** a data de desembaraço prevista se dá pelo seguinte cálculo: “Data de Desembarque Prevista” + “Lead Time de Desembaraço (Dias).

**Data Desembaraço:** essa data é preenchida conforme a data informada no campo “Data Desembaraço”, na tela “Portal de Importação” na guia “Geral”.

**Lead Time de Emissão de NF-E (Dias):** informar a quantidade de dias que o sistema deve considerar para calcular a “Data de Emissão da NF-e Prevista”.

**Data de Emissão da NF-e Prevista:** a data de emissão de NF-e prevista se dá pelo seguinte cálculo: “Data Desembaraço Prevista” + “Lead Time de Emissão de NF-E (Dias)".

**Data de Emissão Nota Nacionalização:** essa data é preenchida conforme a data de emissão da nota de nacionalização vinculada ao processo de importação.

**Transtime de chegada na empresa (Dias):** informar a quantidade de dias que o sistema deve considerar para calcular a “Data de chegada em estoque Prevista”.

**Data de chegada em estoque Prevista:** a data de chegada em estoque prevista se dá pelo seguinte cálculo: “Data de Emissão da NF-e Prevista”  + “Transtime de chegada na empresa (Dias)”.

**Data de chegada no estoque Efetivo:** nesse campo o usuário deve informar a data de chegada no estoque efetivo.

![Imagem 2: Data de chegada no estoque Efetivo: nesse campo o usuário deve informar a data de chegada no estoque efetivo.](https://ajuda.sankhya.com.br/hc/article_attachments/26816160112535)

## 3. Status Follow Up

Os status do Follow Up são atualizados conforme a inserção de informações, segue abaixo como é atualizado cada status do processo no Follow Up:

**Pedido confirmado:** esse é o status atribuído automaticamente assim que o Follow Up é criado.

**Aguardando Produção:** o Status é atualizado a partir do preenchimento do campo “Data de Fabricação-Prevista”.

**Prontidão de Carga:** o Status é atualizado a partir do preenchimento do campo “Data de Prontidão Realizada”.

**Previsão de Embarque:** o Status é atualizado a partir do preenchimento do campo “Porto de origem”.

**Em Trânsito:** o Status é atualizado a partir do preenchimento do campo “Data de Embarque realizado”.

**Atracado (Aguardando registro):** o Status é atualizado a partir do preenchimento do campo “Data de chegada realizada”.

**Remoção:** o Status é atualizado a partir do preenchimento do campo “Data de chegada realizada” e do campo “Remoção”, escolhendo uma das seguintes opções: “DTA” ou “DTC".

**Aguardando Parametrização:** o Status é atualizado a partir do preenchimento dos campos “Nr. DI”, “Data de Registro da DI”, no cabeçalho do processo de importação (Portal de Importação).

**Aguardando desembaraço:** o Status é atualizado a partir do preenchimento dos campos “Nr.DI”, “Data de Registro da DI" e "Parametrização”, quando o mesmo estiver preenchido com a opção “Verde”. Pára **"Processo Desembaraçado".**

**Aguardando Conferência:** o Status é atualizado a partir do preenchimento dos campos “Nr.DI”, “Data de Registro da DI” e “Parametrização”, quando o mesmo estiver preenchido com a opção “Amarelo” ou “Vermelho”.

**DI Desembaraçada:** o Status é atualizado a partir do preenchimento dos campos “Nr.DI", “Data de Registro da DI, “Nota Fiscal” e a nota estiver com Status-NFe “Autorizada”, no Portal de Compras.

**Em Estoque:** o Status é atualizado a partir do preenchimento do campo “Data de Chegada no Estoque”.

![Imagem 3: Em Estoque: o Status é atualizado a partir do preenchimento do campo “Data de Chegada no Estoque”.](https://ajuda.sankhya.com.br/hc/article_attachments/26816556239255)

## 4. Dados da Importação

**Processo Importação:** nesse campo é indicado a qual processo de importação essas informações do follow-up pertencem.

**Status:** conforme o Item 3, nesse campo é apresentado em qual status está o follow-up.

**Parametrização:** nesse campo o usuário deve informar o canal de parametrização desse processo de importação. As opções são, “Verde”, “Amarelo”, “Vermelho” e “Cinza”.

**Remoção:** nesse campo é indicado se vai ter remoção ou não no processo de importação. As opções disponíveis são, “DTA”, “Sem Remoção” e “DTC”.

**Data Negociação Pedido:** nesse campo o usuário irá informar a data de negociação do pedido.

**Data de Confirmação Pedido:** nesse campo o sistema irá apresentar a data de confirmação do pedido de embarque vinculado ao processo de importação .

**Nro. Único Pedido Compra Origem:** nesse campo o sistema apresentará a data de confirmação do pedido de embarque, vinculado ao processo de importação.

**Data da Proforma:** nesse campo o sistema irá apresentar a data da proforma, indicada no pedido de embarque.

**Nr. Proforma:** o sistema irá apresentar o número da Proforma indicado no Pedido de Compra ou Embarque.

**Data Envio Swift:** nesse campo o usuário irá preencher a data que o swift foi enviado.

**Agente de carga/Cia Marítima:** nesse campo o usuário irá preencher o Agente de Carga ou a CIA Marítima do processo. Eles devem estar cadastrados como parceiro.

**Porto de Origem:** o usuário informará o porto de origem que a mercadoria irá ser embarcada.

**Data de Emissão Pedido:** nesse campo o sistema apresentará a data que o pedido de embarque foi emitido.

**Despachante:** o usuário indicará qual será o despachante do processo de importação. Eles devem estar cadastrados como parceiro.

**Fornecedor:** o sistema apresentará o Nome do Fornecedor vinculado ao Pedido de embarque.

**Local de Embarque:** nesse campo o sistema apresentará o local de embarque preenchido no cabeçalho do pedido de embarque.

**Navio:** o usuário informará o nome do Navio do processo de importação.

**Nr. Conhecimento de Embarque (BL/AWB/CRT):** onde o usuário informará o número do conhecimento de Embarque, conforme o documento gerado.

**Data de Registro DI:** nesse campo o Sistema apresentará a data de registro da DI, que foi informada no mesmo campo no “Portal de Importação”, na aba “Geral”.

**Nota fiscal:** nesse campo o sistema apresentará o número da nota fiscal eletrônica de nacionalização.

**Nr. Invoice:** o sistema apresentará o número da Invoice preenchido no cabeçalho do pedido de embarque.

**Número da DI:** nesse campo o Sistema apresentará a data de registro da DI, que foi informada no mesmo campo no “Portal de Importação”, na aba “Geral”.

**Valor Produto:** nesse campo o sistema irá apresentar o valor dos produtos na nota fiscal de nacionalização.

**Frete Importação:** nesse campo o sistema irá apresentar o valor de frete total de importação.

**Seguro Importação:** nesse campo o sistema irá apresentar o Valor de Seguro do processo de importação.

**Taxa Siscomex:** nesse campo o sistema irá apresentar o valor da Taxa Siscomex do processo de importação.

**II:** nesse campo o sistema irá apresentar o valor dos Impostos de Importação (1I) do processo de importação.

**IPI:** nesse campo o sistema irá apresentar o valor do IPI do processo de importação.

**PIS Importação:** nesse campo o sistema irá apresentar o valor do PIS, do processo de importação.

**COFINS Importação:** nesse campo o sistema irá apresentar o valor do COFINS do processo de importação.

**ICMS:** nesse campo o sistema irá apresentar o valor do ICMS do processo de importação.

**Outras importações:** nesse campo o sistema irá apresentar o valor de outras despesas de importação, do processo de importação.

**Valor Total:** neste campo o sistema irá apresentar o valor total da nota de nacionalização.

**Tipo de Carga:** o sistema apresentará o Tipo de Carga preenchido no Pedido de Embarque.

**Tipo De Volumes:** o sistema apresentará o Volume preenchido no Pedido de Embarque.

**Qtd. Volumes:** o sistema apresentará a quantidade de volumes preenchida no Pedido de embarque.

**Peso Líquido:** nesse campo o sistema apresenta o peso líquido total dos itens no processo de importação.

**Peso Bruto:** nesse campo o sistema apresenta o peso bruto total dos itens no processo de importação.

**Tipo Modal:** o sistema irá apresentar o tipo de modal escolhido no Pedido de embarque.

**Tipo Negociação:** o sistema irá apresentar o tipo de negociação indicado no pedido de embarque.

## 5. Aba Ocorrência Follow Up

Na Aba Ocorrência Follow Up, o usuário poderá registrar todas as ocorrências que aconteceram durante o processo de importação, para poderem ser consultadas posteriormente. Criando assim um dossiê de todo o processo de importação.

O usuário deverá clicar em "incluir", preencher o campo “Descrição”, detalhando o ocorrido, preencher a data que houve a ocorrência no campo “Data Ocorrência”. E se tratar de uma ocorrência assinalar o campo “Houve Ocorrência?”, e clicar em salvar. O usuário pode registrar várias ocorrências para o mesmo processo de importação. E o mesmo ficará registrado qual foi o último usuário que criou ou alterou aquela ocorrência.

### 5.1 Campos da aba Ocorrências

**Usuário:** nesse campo fica salvo o usuário que cadastrou a ocorrência.

**Data Alteração:** nesse campo fica salva a data da última alteração da ocorrência.

**Data Ocorrência:** nesse campo o usuário preenche a data da ocorrência.

**Descrição:**

**Houve Ocorrência:** nesse campo o usuário marca se é uma ocorrência ou apenas anotação.

![Imagem 4: Houve Ocorrência: nesse campo o usuário marca se é uma ocorrência ou apenas anotação.](https://ajuda.sankhya.com.br/hc/article_attachments/26817785553815)

## 6. Aba Container Follow Up

Na aba **“Container Follow Up”** serão apresentados os containers que foram cadastrados no “Pedido de Embarque”. Tornando possível que o usuário informe as seguintes informações por Container:

- Freetime de devolução do Container (Dias)
- Data Limite p/ para 1 Período Armazenagem
- Data Efetiva Dev. Container
- Data Remoção

![Imagem 5: Data Remoção](https://ajuda.sankhya.com.br/hc/article_attachments/26817817888151)

## 7. Liberação de Edição de Data Prevista

A funcionalidade permite que o usuário altere as datas previstas no Follow-up.

Para o usuário fazer a liberação foi criado no cadastro de usuários a opção "Permite Alterar Dt. Previstas FollowUp". Essa opção é responsável por permitir que o usuário altere ou não as datas previstas do Follow-Up.

![Imagem 6: Para o usuário fazer a liberação foi criado no cadastro de usuários a opção "Permite Alterar Dt. Previstas FollowUp".…](https://ajuda.sankhya.com.br/hc/article_attachments/26818412368663)

Caso o usuário esteja com essa opção desabilitada e o mesmo tentar alterar as datas previstas do Follow-Up, o sistema irá buscar as seguintes configurações para gerar a liberação:

**IMP\_USULIBFOL:** nesse parâmetro deverá colocar o código do usuário que receberá o evento de liberação, quando algum usuário que não tem permissão de alterar as datas previstas no Follow-Up tente fazer a alteração.

**IMP\_EVELIBFOL:** nesse parâmetro deverá colocar o código de evento de liberação que será gerado, quando algum usuário que não tem permissão de alterar as datas previstas no Follow-Up tente fazer a alteração.

Quando o usuário tentar alterar alguma data prevista, o sistema ira apresentar a seguinte mensagem. “Foi lançado uma liberação para permitir alterar os campos das datas previstas”

![Imagem 7: Quando o usuário tentar alterar alguma data prevista, o sistema ira apresentar a seguinte mensagem. “Foi lançado uma…](https://ajuda.sankhya.com.br/hc/article_attachments/26818412373015)

Após isso, deverá seguir com a liberação de limites conforme o seguinte artigo: [Liberação de Limites.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites)

Após o usuário liberador fazer a liberação, o usuário que solicitou a liberação deverá entrar no Follow-Up e alterar a data que deseja.

## 8. Notificações de Atraso do Follow Up

É possível configurar para o sistema emitir notificações, avisando que o processo de importação está com a próxima etapa a vencer ou vencido no sistema.

### 8.1 Preferências

Configurações > Avançado

**IMP\_NOTIAVENC:** nesse parâmetro o usuário deve informar quantos dias antes ele deseja que o sistema avise sobre quando a próxima data prevista vencerá.

![Imagem 8: IMP_NOTIAVENC: nesse parâmetro o usuário deve informar quantos dias antes ele deseja que o sistema avise sobre quando a…](https://ajuda.sankhya.com.br/hc/article_attachments/26818412374807)

**IMP\_NOTIVENC:** nesse parâmetro o usuário deve informar a quantidade de dias, após o vencimento da próxima etapa prevista, que o sistema deverá continuar avisando os usuários.

![Imagem 9: IMP_NOTIVENC: nesse parâmetro o usuário deve informar a quantidade de dias, após o vencimento da próxima etapa…](https://ajuda.sankhya.com.br/hc/article_attachments/26818412376983)

### 8.2 Configurando Usuário

Configurações > Controle de Acesso

No cadastro de usuário tem a opção “Recebe Notificação Follow-up”. Devem acessar os usuários que vão receber a notificação e que marcarem a opção a seguir:

![Imagem 10: No cadastro de usuário tem a opção “Recebe Notificação Follow-up”. Devem acessar os usuários que vão receber a…](https://ajuda.sankhya.com.br/hc/article_attachments/26818412379927)
