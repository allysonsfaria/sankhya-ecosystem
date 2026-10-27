---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/boas-praticas-usabilidade-ds"
titulo: "Boas praticas de usabilidade"
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/boas-praticas-usabilidade-ds"
trilha: "Blog > Boas Praticas Usabilidade Ds"
---

# Boas praticas de usabilidade

21 de maio de 2023 · 4 min para ler

![Lara Minasian Esparta](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/LaraEsparta.jpg)

Lara Minasian Esparta

Product Manager

![Ana Flavia Fernandes](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/AnaFernandes.jpg)

Ana Flavia Fernandes

Associate Product Owner

## Objetivo

Esse artigo visa apresentar algumas boas práticas definidas entre times de UX e desenvolvimento, para a implementação de jornadas no design system, sejam elas de componentes, migração de telas, ou implementação de novas aplicações.

## Guidelines

Antes de tudo é importante que fique evidente quais são os guias para desenvolvimento de produtos dentro do contexto Sankhya:

![Guidelines](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/guidelines-6357d55feb5c154adfe640e2d58dd929.png)

Essas regras devem ser levadas em conta durante TODO o processo de desenvolvimento (Definição de features, prototipação, arquitetura, desenvolvimento e testes).

### Objetivo do design system

- Um dos principais objetivos do Design System é agilizar as operações do dia a dia dos nossos usuários: otimizar
- Por conta disso, o foco em atalhos de navegação, evitar o uso do mouse ou a interação com pop ups para seleção de valores no preenchimento de campos se torna um ponto de atenção

### Elementos que o usuário não pode ter interação

Usuários sem permissão a alguma ação não deverão ter acesso aos recursos em botões, ícones clicáveis e opções em dropdown apresentados para seleção.

- A ideia é barrarmos a ação a partir de sua raíz, não permitir ao usuário que toda a jornada seja realizada até que um Dialog seja apresentado quando houver uma tentativa de save, avanço, etc

#### Exemplo:

- Um usuário sem permissão para a impressão não deverá poder selecionar ícones de impressora, opção de imprimir nos botões de ação e em mais opções. Tudo isso deverá estar OU desabilitado OU não apresentado.

## Pop-up ou stack view?

Quando o local possuir mais de uma grade ou uma grade editável, o espaço dos pop ups é muito pequeno para garantir uma boa interação. Por isso, nestes casos a migração/implementação deverá considerar uma stack view.

### Uso de stack views

A Stackview é usada para suplantar Popups que possuem um médio/alto esforço cognitivo de tarefas como:

- CRUDs;
- Forms com múltiplos campos;
- Grades complexas com muito scroll ou grades duplas (primária + secundária);
- Abas

![StackView](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/stackView-fb72526e4dd644a8c12f321dd4d2bb47.png)

### Uso de pop-ups

Popups geralmente são usados para apresentar itens básicos de mera visualização ou consulta. Pode, ainda, apresentar formulários que tenham poucos campos (em média, até 5 campos).

![PopUp](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/popUp-21269f5e84cd106439f7f287fa1c4bd3.png)

informação

Possíveis exceções, devido inviabilidades técnicas: quando o usuário clica em uma opção de menu ou botão e vai para uma segunda tela onde informará dados para executar um processamento, essa regra até se aplica e poderia ser um padrão. Mas temos exceções, por exemplo as telas que abrem de clientEvent, normalmente são popups pois são disparados por serviços do backend. Nestes casos, mais raros, o arquiteto do time deve sinalizar o impedimento e a pessoa designer deve utilizar a variação X-large do popup: [Link da documentação](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popup/#varia%C3%A7%C3%B5es-de-largura).

![Exceções](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/Excecoes-d3457b051dbee920977376842542278a.png)

### Múltipla seleção de registros

Ao migrar uma tela para o Design System, o drive sobre o comportamento do sistema em cenários de múltipla seleção de registros (quando em telas com grade), deve ser evidenciado para tratativa correta.

- Ações que são aplicadas somente a registros isolados deverão obedecer o mesmo comportamento do item [Elementos que o usuário não pode ter interação](https://gilded-nasturtium-6b64dd.netlify.app/blog/boas-praticas-usabilidade-ds#elementos-que-o-usu%C3%A1rio-n%C3%A3o-pode-ter-intera%C3%A7%C3%A3o), permissão de realização das ações, ícones clicáveis, opções, etc não deverão ser apresentados nessas condições.

### Dialogs

Dialogs deverão conter textos que sejam claros, objetivos e entendidos por todos os usuários, não somente os com conhecimento técnico.

- Em alertas, o usuário deverá saber qual é o ‘risco’ que está correndo ao prosseguir.
- Em erros, o usuário deverá saber qual é o problema, a ponto de entender o que precisa ser feito para ter sucesso no que tentou realizar anteriormente:
  - É um problema de validação? Direcionar que um campo obrigatório precisa ser preenchido, que a ação desejada não pode ser realizada em registros com uma característica x e etc.
  - É um problema de permissão? Rever a jornada pois o usuário nem deveria ter conseguido iniciar a interação com a funcionalidade.

### Atenção aos casos de insucesso

Assim como o sucesso na realização de uma rotina, eles devem ser evidenciados em wireflows para o direcionamento correto ao desenvolvimento.

- o feedback ao usuário será apresentado em formato de toast, dialog ou caixa de avisos?
- o sistema processa a rotina em varredura de informações (para geração de uma lista de erros) ou pausa seu trabalho no primeiro impedimento encontrado?
