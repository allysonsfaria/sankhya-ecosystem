---
id: "42427577526167"
titulo: "Atualizações de Dezembro de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427577526167-Atualiza%C3%A7%C3%B5es-de-Dezembro-de-2024"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:05Z"
rotulos: ["sync_hc", "ploomes", "ploomes_10231243", "sync_hash_e6a82a588fd0"]
---

# Atualizações de Dezembro de 2024

## [04/12/2024] [Correção]

- Em negócios, ao atualizar um campo do contato, o valor atualizado aparecia temporariamente na checklist como se tivesse sido alterado no cliente, caso esse campo estivesse listado. No entanto, essa mudança era apenas visual, ao atualizar a página, o valor original do cliente era restaurado. Agora, ao atualizar o campo do contato, apenas o campo correspondente do contato na checklist será modificado.
- Ao usar as setas de voltar e avançar do navegador nos relatórios beta, apesar de mudar a url para o painel anterior, a visualização não mudava. O erro foi corrigido e agora a navegação pelas setas funciona corretamente.
- Ao aplicar um filtro complexo em uma tabela dinâmica que excede a profundidade máxima permitida na requisição (MaxAnyAllExpressionDepth), agora será exibida uma mensagem mais clara: 'Filtro inválido devido à quantidade excessiva de etapas.'
- Nos relatórios, o gráfico de Análise Histórica agora será exibido sempre no tamanho "Grande". Além disso, o seletor de tamanho do widget foi desativado para este tipo de gráfico.
- O tooltip do botão para 'Relatórios beta' no menu lateral não estava exibindo a descrição correta. Agora, ele exibe corretamente a mensagem 'Relatórios beta', como esperado.
- Com o TinyMCE não era possível editar os valores dos campos substituídos no modelo de e-mail. Agora, os valores substituídos vão se comportar como texto.

## [06/12/2024] [Correção]

- Ao clicar em "Enviar proposta para aprovação", o modal exibia uma mensagem informando que a proposta entraria no fluxo de aprovação pelo CPQ Beta. No entanto, havia um atraso no fechamento do modal e nenhuma indicação visual de que a proposta estava sendo salva, o que poderia levar o usuário a pensar que o sistema estava travado. Foi implementado um loader que informa ao usuário que a proposta está sendo processada e enviada para aprovação, garantindo uma experiência mais clara e intuitiva.

## [10/12/2024] [Correção]

- Os botões do menu horizontal estavam despadronizados. Alguns possuíam tooltip e outros não. Foram adicionadas tooltips em todos os botões que possam aparecer no menu.
- Quando o filtro de uma automação retornava um erro, mesmo editando a automação com um filtro válido, a mensagem de erro continuava aparecendo. Os desenvolvedores subiram uma correção, e agora, quando editado para um filtro válido, salva normalmente.
- Quando era feita uma busca por produto do cliente, levava em conta apenas o nome do produto, e não o nome do produto do cliente. Agora retorna os dois casos.

## [11/12/2024] [Correção]

- Ao clicar na aba "Enviar e-mail" dentro da tela de um negócio, não estava exibindo a opção para colocar link e não exibe o botão "..." do editor TinyMCE. O problema identificado foi causado por um conflito no pacote da ferramenta TinyMCE, utilizado para gerenciar campos de texto multilinha na aplicação. A correção foi realizada por meio da atualização do pacote responsável pela funcionalidade de campos multilinha no front-end, garantindo a compatibilidade e o funcionamento adequado do TinyMCE.

## [12/12/2024] [Correção]

- Ao atualizar a integração do RD Station, fazemos uma verificação das flags ativas para remover e criar webhooks. Fazemos uma busca de webhook pelo nome, e não eram ignoradas letras maiúsculas e minúsculas, o que causava algumas confusões nesse processo. Sendo assim, os desenvolvedores adicionaram uma propriedade para ignorar mudanças de letras maiúsculas e minúsculas na busca dos webhooks.

## [13/12/2024] [Correção]

- Ao abrir um e-mail com filtro, ele não considera a pasta dos e-mails, o que gerava um erro no código, fazendo com que os botões de 'Marcar como não lido' e 'Mover para' não aparecessem na tela. Os desenvolvedores implementaram uma correção e o problema não ocorre mais.

## [17/12/2024] [Correção]

- Em alguns casos o evento de registro do Zenvia estava vindo com o mesmo valor do anterior, sendo assim, os desenvolvedores implementaram uma correção para prevenir que isso aconteça.
- Ao baixar um anexo de e-mail que o nome continha caracteres especiais o nome era modificado. Corrigimos e agora o anexo é baixado com o nome correto, mesmo tendo caracteres especiais.
- Em anexos de e-mail, adicionamos um ícone de download que é exibido ao passar o mouse sobre o item para simplificar a operação do usuário.

## [19/12/2024] [Correção]

- Anteriormente, o contador de e-mails não lidos não era exibido. Os desenvolvedores implementaram uma correção, e agora o ícone de e-mails exibe corretamente a quantidade de e-mails não lidos.
- A lógica de detecção de duplicidade de empresas na integração do RD Station foi ajustada. Anteriormente, a verificação consistia em identificar se havia uma empresa no Ploomes cujo nome correspondia ao campo name do RD Station. Com a correção, a busca foi ajustada para ser realizada com base no campo company do RD Station.

## [26/12/2024] [Correção]

- A integração entre Omie e Ploomes estava removendo todas as tags de clientes ao editar informações, devido a uma limitação na API do Omie. Antes, o processo apagava todas as tags e as recriava, causando conflitos durante atualizações simultâneas. Com a correção, apenas as tags especificadas são alteradas ou removidas, resolvendo o problema.

## [27/12/2024] [Correção]

- Os desenvolvedores corrigiram um problema relacionado ao uso de dois estados no frontend ao criar filtros em um painel no relatório beta: um para o painel atual e outro para o campo do filtro. A função responsável por enviar os filtros ao backend foi ajustada para ser atualizada não apenas quando o campo do filtro era alterado, mas também quando o painel fosse alterado, garantindo que os dados fossem enviados corretamente para o painel correto.
