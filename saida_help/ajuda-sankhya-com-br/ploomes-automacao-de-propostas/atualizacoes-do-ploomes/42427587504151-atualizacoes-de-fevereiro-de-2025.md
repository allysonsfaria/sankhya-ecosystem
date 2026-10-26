---
id: "42427587504151"
titulo: "Atualizações de Fevereiro de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427587504151-Atualiza%C3%A7%C3%B5es-de-Fevereiro-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:03Z"
rotulos: ["sync_hc", "ploomes", "ploomes_10531933", "sync_hash_e18a608b58b9"]
---

# Atualizações de Fevereiro de 2025

## [04/02/2025] [Correção]

- Foi adicionado um atributo responsável por fazer uma validação da query e checar se essa query contem expand=\* sem o preload=true, caindo nisso retornar um BadRequest.
- Corrigimos um comportamento em e-mails que adicionava <br> indevidamente ao lidar com quebras de linha em conteúdos contendo HTML. Agora tratamos corretamente tanto casos de texto puro quanto de conteúdo com tags HTML, garantindo a renderização adequada em ambos os cenários.

## [07/02/2025] [Correção]

- Em funis que não tinham o módulo de proposta ou não existia proposta criada, o App pedia para selecionar uma proposta ao tentar criar uma nova venda ou documento, impossibilitando a criação dos mesmos.
- No aplicativo, corrigimos o comportamento dos marcadores do registro de interação que não eram passados para o registro de visita (check-in).

## [10/02/2025] [Correção]

- Na integração com o RD Station, o campo "Última conversão - Fonte" não era preenchido devido a uma verificação aplicada antes do mapeamento dos dados. Agora, o código foi ajustado para que essa verificação ocorra corretamente, garantindo o preenchimento adequado do campo.

## [11/02/2025] [Correção]

- A validação que impede que uma fórmula rode novamente caso possua as mesmas variáveis não estavam funcionando. Foi corrigido e agora prevenimos diversos loops de ocorrer.
- Ao tentar integrar um cliente com Id (Omie) preenchido com espaços vazios não era informado o erro e o cliente não integrava. Agora, exibimos no cliente um registro de interação informando que o Id (Omie) está preenchido incorretamente.

## [12/02/2025] [Correção]

- Corrigimos a análise da fórmula condicional na montagem de sua estrutura de condições. Agora, caso o campo possua colchetes, o comportamento será o mesmo da fórmula simples: remove-se os colchetes mas ainda exibe o campo com o nome normal
- No app, ao usar um campo como variável de uma formula interna e como valor padrão, ao alterar a formula interna, o calculo do valor padrão zerava o valor da variável na formula interna. Os desenvolvedores corrigiram esse comportamento e o problema não ocorre mais.
- Correção na experiência de busca de e-mails na tela "Novo E-mail". Melhora a experiência ao preencher os campos "Para", "CC" e "CCO", especialmente em situações de compartilhamento de proposta, venda ou documento.

  Alterações realizadas: Padronização e organização dos resultados exibidos na caixa de seleção dos campos "Para", "CC" e "CCO", excluídos os já selecionados para eles.

  Aplicação da seguinte ordem de exibição para os resultados: 1- Caso o documento tenha uma pessoa vinculada, esta será exibida primeiro. 2- Em seguida, as pessoas da empresa vinculada ao documento, organizadas em ordem alfabética (limite de 15). 3- Por fim, os usuários da conta, também organizados em ordem alfabética (limite de 15).

## [13/02/2025] [Correção]

- APP - Corrigimos fórmulas de filtro em campos de seleção (que usam campos da Proposta como valor padrão) que não estavam calculando corretamente ao criar Venda e Documento.
- APP - Corrigimos fórmulas de campos da Proposta que utilizavam variáveis de Campos de Produto não estavam sendo calculados corretamente quando não existia nenhum Campo de Bloco.
- APP - Existia uma regra no redirecionamento de notificações onde se um cliente está vinculado a entidade automaticamente redirecionamos para o cliente, essa regra é antiga e não precisamos mais dela. Por isso adicionei uma nova verificação para descobrir se a notificação é relacionado a um registro de interação ou tarefa e com isso redirecionar apropriadamente.
- APP - Fórmulas de filtro em campos de seleção (que usam campos da Proposta como valor padrão) não estavam calculando corretamente ao criar Venda e Documento
- APP - Campo de seleção múltipla estava com um erro impedindo a fila de fórmulas ser finalizada

## [17/02/2025] [Correção]

- O app não estava realizando o redirect para a visualização do cliente ao pressionar um campo do tipo contato dinâmico. Foi ajustada a lógica para permitir esse redirect, além dos campos nativos, para campos dinâmicos também.
- No aplicativo, de forma intermitente, os valores dos campos de produto não apareciam na visualização do html da proposta. Adicionamos uma verificação ao salvar a proposta para impedir que isso aconteça

## [18/02/2025] [Correção]

- Não ocorria a limitação de modelos ao duplicar uma venda. Por isso, os desenvolvedores corrigiram a requisição que traz os modelos de venda permitidos na edição, duplicação e revisão em modal. Antes eram filtrados os modelos de documentos, mesmo a entidade sendo de venda.

## [20/02/2025] [Correção]

- A API possui um limite de 100 caracteres para o campo de texto simples. Por esse motivo, os desenvolvedores implementaram esse mesmo limite no campo de texto simples do aplicativo.
- Foi corrigido um problema onde, ao editar o campo de telefone sem alterar o valor e salvar, a máscara de formatação era removida. Agora, a máscara é mantida corretamente, mesmo quando o valor do campo não é alterado.
- Ao gerar nova venda, o aplicativo não estava salvando qual era o ID da proposta de origem, agora salva corretamente.
- Agora filtramos os tipos de assinatura disponíveis antes de carregar o modal de compartilhamento de documento. Evitando, assim, que a opção padrão carregada seja alguma indisponível.
- O campo situação podia ser adicionado no formulário de negócio, porém o preenchimento desse campo não mudava a situação do card. Para resolver esse problema, mantivemos o campo no formulário, porém bloqueado para edição e sem bloqueio de campo obrigatório, além de adicionar um tooltip avisando que o campo é apenas para visualização e não pode ser editado.

## [25/02/2025] [Correção]

- Corrigido um problema onde documentos derivados de propostas não salvavam corretamente devido a um valor errado em seus produtos no CPQ Beta.
