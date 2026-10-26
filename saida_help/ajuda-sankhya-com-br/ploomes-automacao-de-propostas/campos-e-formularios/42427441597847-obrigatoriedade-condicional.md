---
id: "42427441597847"
titulo: "Obrigatoriedade Condicional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427441597847-Obrigatoriedade-Condicional"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-10T18:02:53Z"
rotulos: ["sync_hc", "ploomes", "ploomes_8913576", "sync_hash_801b475d9972"]
---

# Obrigatoriedade Condicional

## Sobre a funcionalidade

Agora, além de definir o comportamento padrão da obrigatoriedade de um campo, também é possível configurar em quais situações específicas o campo deve ou não ser obrigatório, podendo variar por usuários, perfis de usuários, equipes ou por fórmulas, da mesma forma como é feito na edição e visualização condicionais.

## Objetivos da funcionalidade

Permitir a configuração de regras específicas de obrigatoriedade de campos para atender a uma necessidade maior de fluxos de trabalho e regras de formulários, que muitas vezes são preenchidos de forma parcial por equipes diferentes e em momentos diferentes da jornada de atendimento aos seus clientes.

## Requisitos para uso da funcionalidade

Não há pré-requisitos.

## Utilizando a funcionalidade

### Configurando a obrigatoriedade dos campos

#### 1) Usuários que serão afetados pelas regras de obrigatoriedade

A primeira opção a ser configurada na obrigatoriedade do campo é a seleção de quais usuários serão afetados pelas regras de "campo obrigatório" de "obrigatoriedade por fórmula" que serão definidas, podendo escolher entre: todos da empresa, perfis de usuários, equipes ou usuários individualmente.

Ou seja, **apenas os usuários contemplados nesta seleção é que serão impactados pelas regras.** Os usuários não contemplados na seleção não serão obrigados a preencher o campo e nunca serão afetadas pela definição de "campo obrigatório" e nem pela "obrigatoriedade por fórmula".

![Imagem 1: Ou seja, apenas os usuários contemplados nesta seleção é que serão impactados pelas regras. Os usuários não…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173506115/7e08bef1e99023e6a6c713075692/image.png?expires=1786536000&signature=fe46bfc17daebe19b04310f49071d8d708fd60ee443fd0d8c72cb968e4f99c9d&req=diEgFcx%2Bm4BeXPMW3nq%2Bgbrwq693kpe0xRuJCIHJbpi4skW04jseeGQJIcw%2F%0AlwEofBthpMEwaVRAWEdJ5wsSpwk%3D%0A)

#### 2) Estado padrão de obrigatoriedade do campo

A segunda opção a ser configurada é a definição do estado padrão do campo (obrigatório ou não obrigatório) em formulários, abas e cadastros, aplicável somente aos usuários contemplados na seleção feita.

Ou seja, **quando os usuários contemplados na seleção visualizarem esse campo em formulários, abas e cadastros, o mesmo aparecerá como obrigatório para eles,** a menos que alguma fórmula configurada no item a seguir altere esse comportamento nos formulários.

![Imagem 2: Ou seja, quando os usuários contemplados na seleção visualizarem esse campo em formulários, abas e cadastros, o mesmo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173507027/9fcdd1e584d474732648ca965999/image.png?expires=1786536000&signature=2423169d106a3a1d851fc4c2167b9e7cef17ada13f4f135e95e8f3213b2225bd&req=diEgFcx%2BmoFdXvMW3nq%2BgXl%2BEHJD5EypUkBvWKHqD2zDFnQnzckMRbn%2FlqnT%0AN3z0naFb8t8xRqOk7X8i95DaQVk%3D%0A)

#### 3) Obrigatoriedade por fórmula

A terceira e última opção a ser configurada é a definição de variação de comportamento da obrigatoriedade do campo, valida apenas em formulários, em função de alguma fórmula configurada.

Ou seja, **quando os usuários contemplados na seleção visualizarem esse campo em formulários, dependendo da fórmula configurada, a obrigatoriedade de preenchimento do campo poderá ser alterada**, podendo modificar inclusive o estado padrão de obrigatoriedade do campo configurado anteriormente.

![Imagem 3: Ou seja, quando os usuários contemplados na seleção visualizarem esse campo em formulários, dependendo da fórmula…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173507838/7b11831bc82a5e0437d334c3b972/image.png?expires=1786536000&signature=8004ce45920c1c785f50ce4eaa7ed60982f20b13c82be56084e1ccb0637c2e68&req=diEgFcx%2BmolcUfMW3nq%2BgVEkAauar3IOhgfJ1ZXLIBdAuhcumstfB8jix1A%2F%0Attzc0sa9sfPFS9RMJ8Fyp%2FAMqk8%3D%0A)

### Combinando as opções de configuração

No quadro a seguir, está um resumo do resultado obtido em formulários, abas e telas de clientes e negócio quando as regras de "campo obrigatório" e de "obrigatoriedade por fórmula" se combinam, **dado que o "campo obrigatório" afeta formulários, abas e telas de clientes/negócios e que a "obrigatoriedade por fórmula" afeta apenas formulários e pode alterar a definição do "campo obrigatório".**

| **"Campo obrigatório"** | **"Obrigatoriedade por fórmula"** | **Resultado em formulários** | **Resultado em abas e telas de clientes e negócios** |
| --- | --- | --- | --- |
| Obrigatório | Obrigatório | Obrigatório | Obrigatório |
| Obrigatório | Não obrigatório | Não obrigatório | Obrigatório |
| Obrigatório | Vazia | Obrigatório | Obrigatório |
| Não obrigatório | Obrigatório | Obrigatório | Não obrigatório |
| Não obrigatório | Não obrigatório | Não obrigatório | Não obrigatório |
| Não obrigatório | Vazia | Não obrigatório | Não obrigatório |

### Migrando as configurações dos campos já existentes

Os campos configurados como obrigatório no padrão anterior serão migrados para o novo padrão, mantendo o mesmo efeito, e com a seguinte combinação de campos, que indica que a definição de "campo obrigatório" é válida para "todos os usuários da empresa".

![Imagem 4: Os campos configurados como obrigatório no padrão anterior serão migrados para o novo padrão, mantendo o mesmo efeito,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173510441/84c46d1224cb09115a1b7231607b/image.png?expires=1786536000&signature=1027ed45926be97bb39498c062029cfe29d22be77c0bca6a94c97c00495bdbeb&req=diEgFcx%2FnYVbWPMW3nq%2BgcvHyVMDPuLvyGrz64UaX%2BvYgpqxWqG%2FIlc%2F2Abm%0AaMKml5cTiElBhjids%2FARtAtjqLU%3D%0A)

Da mesma forma, os campos não obrigatórios no padrão anterior, serão migrados para o novo padrão com a definição de "campo obrigatório" desativada e válida para "todos os usuários da empresa".

![Imagem 5: Da mesma forma, os campos não obrigatórios no padrão anterior, serão migrados para o novo padrão com a definição de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173511204/dededf7068be7bec43ff1edb5298/image.png?expires=1786536000&signature=b00a91cc8fa929b71a684d12467144224db2a077b541659ebe283f2ec5771797&req=diEgFcx%2FnINfXfMW3nq%2Bgf4vzWxdMnD7s3BUg%2F93Nwo8ziQr6lsMAjj8%2B2dU%0AO6dCKj2UVg9FHTUJZ7epclDVlCQ%3D%0A)

## Limitações da funcionalidade

A configuração de obrigatoriedade está disponível para a maioria dos tipos de campo, com exceção dos campos do tipo: Assinatura Docusign e Desenvolvedor.
