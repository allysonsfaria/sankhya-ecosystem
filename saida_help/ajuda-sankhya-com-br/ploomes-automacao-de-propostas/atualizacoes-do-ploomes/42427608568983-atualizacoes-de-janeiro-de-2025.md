---
id: "42427608568983"
titulo: "Atualizações de Janeiro de 2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427608568983-Atualiza%C3%A7%C3%B5es-de-Janeiro-de-2025"
trilha: "PLOOMES: Automação de propostas  > Atualizações do Ploomes"
atualizado_em: "2026-08-03T13:03:00Z"
rotulos: ["sync_hc", "ploomes", "ploomes_10375212", "sync_hash_30e3db34d98e"]
---

# Atualizações de Janeiro de 2025

## [09/01/2025] [Correção]

- Anteriormente, era possível excluir um signatário após a assinatura com a integração do Clicksign, o que causava confusão de informações, já que no Clicksign não atualiza. Os desenvolvedores implementaram uma correção que impede a remoção de signatários que já assinaram, alinhando-se ao padrão do Clicksign.
- Os desenvolvedores corrigiram um erro no frontend que impedia o processo de exibir o botão de "Integração Autorizada" do Outlook 365 e bloqueava a ativação, mesmo que a autorização já tivesse sido realizada no backend.

## [14/01/2025] [Correção]

- No gerador de HTML, quando o usuário utilizava um idioma diferente de pt-BR, os campos do tipo Checkbox exibiam no formulário corretamente as opções traduzidas no idioma selecionado. No entanto, ao gerar a venda, proposta ou documento, o valor correspondente à opção selecionada era sempre preenchido em português, independentemente do idioma configurado pelo usuário. Os desenvolvedores ajustaram isso e agora será exibido de acordo com o idioma do usuário.
- Quando um documento tinha mais do que 20 produtos e algum deles era removido pelo filtro do bloco, o carregamento dos produtos travava. Os desenvolvedores implementaram uma correção para esse problema.

## [15/01/2025] [Correção]

- No aplicativo, o comportamento do campo de checkbox obrigatório estava divergente do comportamento na versão web. Na web, o switch desligado era recusado devido à obrigatoriedade, enquanto no aplicativo o switch desligado era tratado como 'Não', permitindo que passasse pela validação de obrigatoriedade. Os desenvolvedores corrigiram o comportamento no aplicativo.

## [16/01/2025] [Correção]

- No aplicativo, havia um problema ao adicionar um responsável para um cliente do tipo "Pessoa" vinculado a uma empresa: a alteração não era salva corretamente, e o responsável era removido ao retornar à tela do cliente. Antes, era possível editar diretamente o campo de responsável nos contatos de empresas, mas as alterações não eram aplicadas. Agora, o sistema exibe um aviso informando que alterações no responsável devem ser feitas na empresa-mãe, evitando edições diretas no contato.

## [20/01/2025] [Correção]

- Identificamos uma inconsistência no comportamento dos campos nativos [Cliente.Telefones] e [Contato.Telefones] no mapeamento de valores padrão em formulários externos. Embora esses campos não permitam a definição de valores padrão, eles estavam disponíveis para seleção no mapeamento. Para resolver essa questão, realizamos uma atualização na configuração de formulários externos. Agora, os campos de telefone foram removidos da lista de opções disponíveis para o mapeamento de valores padrão, garantindo maior consistência no uso da funcionalidade.
- Campos com opções pré-cadastradas não estavam sendo preenchidos corretamente pelas fórmulas integradas no CPQ Beta. A correção foi aplicada, garantindo que os campos de opções pré-cadastradas sejam processados e preenchidos de maneira adequada.
- Ao acessar o Ploomes, foi identificado que a requisição "iframe" era carregada com o link do vídeo do YouTube, originalmente destinada ao primeiro acesso do usuário. No entanto, essa requisição continuava sendo realizada mesmo após o primeiro acesso, o que causava lentidão, especialmente em contas que possuem restrição de acesso ao YouTube em sua rede. Como parte da atualização, a biblioteca angular-youtube-embed foi removida e o script <https://www.youtube.com/iframe_api> deixou de ser utilizado.

## [22/01/2025] [Correção]

- Na integração com o Zapier, ao testar um dos triggers, os itens retornados eram os mais antigos, foi corrigido para serem devidamente os itens mais recentes no momento do teste.

## [21/01/2025] [Correção]

- Na integração com o Clicksign, o campo "Assinado Clicksign" não era atualizado devido a timeout em uma requisição pesada ao banco de dados. O problema foi resolvido com a otimização da integração, dividindo as requisições e implementando cache.
- Em relatórios, filtros do tipo último ano não considerava o dia 31/12 como pertencente ao último ano. Agora considera corretamente.

## [24/01/2025] [Correção]

- Ao importar clientes com números de telefone iniciados por +55, o sistema apresentava um problema na formatação ao editar o telefone no front-end. Implementamos uma melhoria para corrigir essa situação, garantindo que os números sejam exibidos e tratados corretamente.
- No CPQ-Beta, corrigimos um problema na utilização de marcador de produto como variável em fórmulas
- Anteriormente, ao criar ou editar uma proposta em um negócio, o Valor do negócio era atualizado automaticamente para refletir o Valor da última proposta ou revisão criada/editada. No entanto, ao excluir a última proposta ou revisão, o Valor do negócio permanecia inalterado, refletindo o valor da proposta/revisão excluída. Agora, estabelecemos um vínculo entre o negócio e a proposta que originou o valor do negócio. Assim, quando essa proposta é excluída, o Valor do negócio será automaticamente zerado.
- No menu horizontal, há um ícone de alerta para o fluxo de aprovação. Ao passar o mouse sobre ele, é exibido um tooltip, e, ao clicar no ícone, um dropdown é aberto com uma lista de fluxos a serem aprovados. No entanto, o tooltip permanecia visível na tela mesmo após clicar em um dos elementos do dropdown. Os desenvolvedores implementaram uma correção e o problema não ocorre mais.
