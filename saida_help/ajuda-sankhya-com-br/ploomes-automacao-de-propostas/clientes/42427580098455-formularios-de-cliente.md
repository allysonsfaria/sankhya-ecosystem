---
id: "42427580098455"
titulo: "Formulários de cliente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427580098455-Formul%C3%A1rios-de-cliente"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T18:05:22Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5780195", "sync_hash_0ef879365d4a"]
---

# Formulários de cliente

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=s4_bjffPLVk)

Os formulários de cliente podem ser editados em Administração - Campos e formulários.

## Diferença entre Empresa, Empresa Mini, Pessoa e Pessoa Mini.

Ao acessar a tela de formulários, clicando em "Clientes", vê-se opções de Empresas, Empresas mini, Pessoas, e Pessoas mini.

Os formulários comuns são utilizados ao cadastrar um novo cliente pelo botão "Novo +", ou apertando "Shift+C" para empresas e "Shift+P" para pessoas.

![Imagem 1: Os formulários comuns são utilizados ao cadastrar um novo cliente pelo botão "Novo +", ou apertando "Shift+C" para…](https://downloads.intercomcdn.com/i/o/427664134/b427caa9defe380db288d9a8/Pasted+image+20211201162045.png?expires=1786536000&signature=0bed1e47dbde1bf22ec37c0d82cb8a75c3c45f45dadd256650b4b56c527ce431&req=cCIgEM96nIJbFb4V1XW4gRGgBBoNyuxU4eqdl1bPZX5spAJKrKts5zQ0sm7l%0Awu%2BrFqCHHA3d8361layYCshp8g%3D%3D%0A)

Também definem quais campos aparecem na página do cliente à esquerda.

![Imagem 2: Também definem quais campos aparecem na página do cliente à esquerda.](https://downloads.intercomcdn.com/i/o/427664278/fb32d39050aa027064e7447f/Pasted+image+20211201162422.png?expires=1786536000&signature=1bb23ab13602ed7e16fab4c91734a6cf6cea0a52ec3a173ac96302a16931ad6d&req=cCIgEM96n4ZXFb4V1XW4gXF8swjZ8ZnVXsVhPxIAcrm3eBhr7WMLLv%2BkiS%2FJ%0AgIxka9qwl1x4r6j56eiN2xzBiw%3D%3D%0A)

Formulários mini aparecem na hora de cadastrar um cliente ainda não cadastrado dentro de um formulário de outra entidade, como no de negócios.

![Imagem 3: Formulários mini aparecem na hora de cadastrar um cliente ainda não cadastrado dentro de um formulário de outra…](https://downloads.intercomcdn.com/i/o/427664479/9764ef1310c5338198cc0a91/Pasted+image+20211201162630.png?expires=1786536000&signature=2b64b14a24b6954fdfb5ab8516c2d01ef44fe8e0662c6baec208d5ccde895931&req=cCIgEM96mYZWFb4V1XW4gR0CO9xb9S1%2BdnkZtxFHl7d3VNWuHBs5%2BlhsseHW%0ADvZgHsD%2F0K75O%2FA9EGxNP%2FDMjw%3D%3D%0A)

Também definem quais campos de cliente aparecem à esquerda da página de um negócio.

![Imagem 4: Também definem quais campos de cliente aparecem à esquerda da página de um negócio.](https://downloads.intercomcdn.com/i/o/427664596/fbd13aab5001fc7eeab3f5ea/Pasted+image+20211201162745.png?expires=1786536000&signature=f0e48141307a5ec0e29957b806272fb6db9fd39356e56be0b784c02868f01c5a&req=cCIgEM96mIhZFb4V1XW4gV6T3Mfiw1%2FrsNlyubcsL4peIfpZ0RclvJNaoFfS%0AFeK8DNnCZvftxYBIYqlXANmeog%3D%3D%0A)

## Criação e inclusão de campos

Campos podem ser adicionados ao formulário em "Adicionar campo", no canto superior direito do formulário. Caso o campo desejado não exista, clique em "Criar campo" para inserir um novo campo.

**Tipos de campo**

À esquerda, seleciona-se o tipo do campo que será criado.
Os campos disponíveis são:

- Texto simples
  Texto limitado a 250 caracteres
- Texto multilinha
  Texto de caracteres ilimitados
- Número inteiro
  Integer
- Moeda
  Número limitado a 2 casas decimais
- Número com casas decimais ilimitadas
  Float
- Opções pré-cadastradas
  Lista de opções cadastráveis
- Data
  Campo de preenchimento de data
- Horário
  Campo de preenchimento de horário
- Checkbox
  Campo de 'sim' ou 'não'
- CPF
  Campo com máscara de CPF
- CNPJ
  Campo com máscara de CNPJ
- Porcentagem
  Campo com indicador de porcentagem (age como casas decimais em fórmula; para usar como porcentagem, é necessário dividi-lo por 100)
- Endereço
  Campo integrado ao Google Maps
- Imagem
  Campo para subir imagens
- Anexo
  Campo para subir arquivos, limitado a 25mb
- Cor
  Paleta de cores
- Desenvolvedor
  Personalize o campo com injeção de HTML, CSS e JavaScript
- Usuário
  Lista de usuários da conta
- Produto
  Lista de produtos da conta
- Cliente
  Lista de clientes da conta
- Símbolo de moeda
  Cria um símbolo de moeda, geralmente utilizado antes de um campo de valor
- Assinatura
  Recebe assinaturas pelo APP

É importante que o tipo do campo seja escolhido durante a criação do campo, pois não poderá ser alterado posteriormente.

**Valor padrão**

O valor padrão determina como o campo vem preenchido ao se abrir um formulário. Não tem 'gatilho', portanto só aparece na criação da entidade.
Pode ser configurado para que puxe valor de outro campo - mas só vai ser puxado um valor caso o mesmo já esteja preenchido no momento da criação.

**Obrigatoriedade**

A chave "Preenchimento obrigatório" impede o usuário de salvar o formulário caso o campo não esteja preenchido.

**Campo chave**

A chave "Campo chave" impede o usuário de salvar o formulário caso o campo esteja preenchido com um valor já cadastrado no sistema, impedindo duplicidade.

**Campo de duas colunas**

A chave "Campo de duas colunas" aumenta a largura do campo no formulário.

**Máscaras**

Alguns campos, como Telefones, CNPJ, e CPF, vêm com máscaras pré-cadastradas.
No caso do CNPJ, por exemplo, é validado o número do CNPJ e o Dígito verificador, impedindo o usuário de cadastrar um formulário caso o CNPJ não exista ou esteja preenchido incorretamente.
Não é possível remover a máscara de um campo ou criar máscaras customizadas.

**Campos múltiplos**

Em campos de Opções pré-cadastradas, é possível marcar a chave "Campo múltiplo" para que o usuário possa selecionar mais de uma opção no campo.

**Fórmulas**

Em "Configurações avançadas", é possível criar uma fórmula para o campo.
As fórmulas rodam apenas no formulário, e seguem a lógica do JavaScript.
é possível criar uma fórmula de JavaScript simples, uma fórmula integrada de JSON, uma fórmula condicional (Condicional simples em JavaScript, mas de preenchimento sem programação), ou uma fórmula Excel.
As fórmulas aceitam campos dinâmicos, clicando em "Campos", e em "Códigos JS" é possível selecionar uma das fórmulas padrão para preenchimento automático.

**Dados de pessoa física**

Em "Configurações avançadas", a chave Marcar como dado de pessoa física garante que o campo será completamente apagado de nosso banco de dados caso o cliente seja excluído. Isso garante conformidade da sua empresa com a LGPD.

**Filtro de lista**

Em "Configurações Avançadas" nos campos de Opções pré-cadastradas, Usuário, Produto e Cliente, é possível limitar quais itens aparecem na lista dependendo de uma fórmula criada.

**Configurações de edição e bloqueio do campo**

Podemos limitar quais usuários editam o campo em "Edição restrita";
Também é possível bloquear a edição por padrão para todos os usuários;
As "Regras de edição" podem liberar ou bloquear a edição dependendo de uma fórmula criada, semelhante ao filtro de lista.

Se configurado para bloquear a edição para usuários selecionados, os administradores também poderão editar mesmo que não estejam selecionados.

**Configurações de visualização do campo**

As mesmas configurações de edição existem para a visualização do campo, podendo ocultar condicionalmente um campo do formulário.
Administradores podem revelar um campo oculto manualmente apertando "Shift+F"

## Seções e ordenação de campo

Na configuração do formulário, é possível adicionar uma seção em "Nova seção" e remanejar campos ao arrastá-los.
As seções têm sua própria limitação de visualização por usuário.

Um formulário organizado diminui o atrito do usuário no uso do sistema! Garanta que todo campo seja necessário nesse momento, e que a edição e criação seja fácil e fluida.
