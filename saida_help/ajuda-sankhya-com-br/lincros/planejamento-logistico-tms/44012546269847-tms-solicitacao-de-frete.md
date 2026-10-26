---
id: "44012546269847"
titulo: "[TMS] - Solicitação de Frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012546269847--TMS-Solicita%C3%A7%C3%A3o-de-Frete"
trilha: "Lincros > TMS > Planejamento Logístico - TMS"
atualizado_em: "2026-10-05T19:31:56Z"
rotulos: ["sync_hc", "lincros", "sync_hash_a7af075b04e3", "lincros_13433462"]
---

# [TMS] - Solicitação de Frete

**Menu**: Planejamento Logístico > Seleção de transportadora > Solicitação de Frete

**Objetivo**: A solicitação de frete é um canal de ligação entre um setor da empresa ao setor logístico. Ela possibilita que qualquer pessoa não pertencente ao setor logístico solicite um orçamento de custo de frete para determinado produto ou nota fiscal. Tendo a entrada da demanda por esta rotina, tem-se como resultado o custo do frete para efetuar o transporte desta demanda. Por exemplo, o usuário solicita um frete para transporte das notas fiscais X, Y e Z. Um outro usuário da logística, irá verificar esta solicitação de frete e para atendê-la, abrirá uma cotação spot a fim de realizar a escolha da melhor transportadora para realizar o transporte desta carga. Após a conclusão do processo de cotação, pode-se criar a ordem de coleta diretamente da cotação.

## Considerações:

- É necessário ter cadastrado no sistema Nota Fiscal, Pré-nota Fiscal ou Produtos;
- **Fluxo do Processo**: Solicitação de Frete > Cotação Spot > Ordem de Coleta;

## Solicitação de Frete

1. Para fazer uma solicitação de Frete deve clicar em 'Novo';
2. Selecionar o tipo de documento que deseja buscar (Nota fiscal ou Pré-nota fiscal) e, caso as notas fiscais em questão ainda não estejam no sistema, pode-se realizar a importação das mesmas na própria tela de solicitação de frete, adicionando os arquivos XML conforme imagem abaixo.
3. Solicitação de Frete pode também se feita pelo Produto, nesse caso não há necessidade de informar documento.

   ![Imagem 1: Solicitação de Frete pode também se feita pelo Produto, nesse caso não há necessidade de informar documento.](https://ajuda.sankhya.com.br/hc/article_attachments/44012555228183)
4. Pela lupa, pode-se realizar a busca dos documentos utilizando filtros. Também é possível selecionar mais de uma nota fiscal para inserir na solicitação. Após selecionar os documentos, clicar em Ok.
5. Caso os documentos importados não contenham produtos é possível adicioná-los manualmente, podendo buscar os mesmos na lookup: (campos que possuem lupa para buscas): preencher os campos conforme abaixo e clicar em Adicionar.
6. Se o produto em questão estiver vinculado a uma embalagem, ela pode ser selecionada através do campo Embalagem, que será adicionada na solicitação de fretes.

   ![Imagem 2: Se o produto em questão estiver vinculado a uma embalagem, ela pode ser selecionada através do campo Embalagem, que…](https://ajuda.sankhya.com.br/hc/article_attachments/44012533011735)
7. Pode-se clicar no lápis do produto ou da embalagem para realizar alterações, como quantidade, peso, valor, entre outros. A remoção do produto pode ser realizada clicando no X.

   ![Imagem 3: Pode-se clicar no lápis do produto ou da embalagem para realizar alterações, como quantidade, peso, valor, entre…](https://ajuda.sankhya.com.br/hc/article_attachments/44012541296919)

## Complementos da solicitação

- **Descrição**: este campo é obrigatório, nele pode-se informar o motivo desta demanda ou outras informações;

- **Pessoa de contato:** pode-se informar o(s) nome(s) e contato caso necessário;

- **Prioridade**: A prioridade é previamente cadastrada no Cadastros gerais > Configurações da empresa > Prioridades. Nela são informadas as horas/minutos para resolução. Desta forma, ao informar uma prioridade na solicitação, automaticamente é exibida uma data de vencimento fixa, definida conforme o cadastro da prioridade;

Pode-se informar a previsão de coleta e de entrega desejada. Se ela precisar ser previamente agendada, marcar a flag Entrega agendada para sinalizar.

**Obs.:** Ao selecionar os documentos na solicitação, automaticamente os campos de Endereço serão preenchidos! Caso sejam selecionadas diversas notas fiscais com endereços diferentes, será preenchido com os dados da primeira nota inserida na solicitação.

**Informações da carga**

- **Centro de custo**: Caso seja necessário vincular a solicitação a um centro de custo, ele pode ser cadastrado no menu Cadastros gerais > Regras de rateio > Centros de custo;
- **Natureza de operação**: Caso seja necessário informar a natureza de operação, ela pode ser cadastrada no caminho: Cadastros gerais > Regras de rateio > Operações;
- **Tipo da carga**: Campo utilizado para informar se a carga a ser transportada será fracionada ou fechada, ou seja, pré-conhecimento ou embarque;
- **Marcadores**: Caso seja necessário informar um marcador à solicitação, ele pode ser cadastrado no caminho: Cadastros gerais > Configurações da empresa > Marcadores;
- **Departamento**: Caso seja necessário vincular a solicitação a um departamento, ele pode ser cadastrado no caminho: Sistema > Acesso > Departamento;
- **Canal de distribuição**: Caso seja necessário informar um canal de distribuição, ele pode ser cadastrado no caminho: Cadastros gerais > Modelos de distribuição > Canais de distribuição;
- **Calculadora de frete para projeto:** Caso seja necessário vincular a um projeto de frete, é necessário a configuração cadastrada no caminho: Cadastros gerais > Configurações da empresa > Calculadora de fretes para projeto e um projeto de frete criado através do menu Planejamento logístico > Calculadora de fretes para projeto;
- **Observação**: Campo livre para preenchimento de outros dados desejados;
- Após salvar a solicitação de frete ela, a situação é gravada como Criado;
- É possível criar uma cotação spot a partir da tela de solicitação de frete. Assim que a cotação é aberta ela é alterada para Em andamento, e ao concluir, com a confirmação da escolha de transportadora para o transporte desta demanda, o status da solicitação de frete é alterado para Concluído;
- Caso seja necessário é possível também realizar o cancelamento da solicitação de frete através do botão Cancelar, alterando a situação para Cancelado. Para reabrir basta clicar no botão Reabrir. Ambos os procedimentos são registrados na aba Histórico;

## Importante

As alterações realizadas nas solicitações após a criação da cotação não serão transferidas para a cotação.

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
