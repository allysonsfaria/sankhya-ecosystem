---
id: "42430271612183"
titulo: "Componente JavaScript"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430271612183-Componente-JavaScript"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:02:50Z"
rotulos: ["sync_hc", "neppo", "neppo_857997540", "sync_hash_4265577c3f6a"]
---

# Componente JavaScript

## Visão Geral

Este documento tem como finalidade orientar a utilização do componente JavaScript para fins de criação de bot no construtor de bot.

## Usabilidade

No novo componente de JS, o usuário poderá realizar seleção do tema pré-definido de sua preferência para codificar tornando a experiência agradável, além de ter uma estrutura funcional para desenvolver parametrizações diretamente em javascript, permitindo salvar os parâmetros desenvolvidos em uma variavel e utilizar durante todo o fluxo do bot.

Observações:

- Valores booleanos não podem ser retornados como `true` e `false`.
- O vars contém todas as variáveis do fluxo, tanto locais quanto globais.

  - Ex: para obter a origem do usuário, utilizando a variável glabal `firstMessage`, pelo componente de JavaScript, basta acessar via `vars.firstMessage.originUser`.

![Imagem 1: Ex: para obter a origem do usuário, utilizando a variável glabal firstMessage , pelo componente de JavaScript, basta…](https://ajuda.sankhya.com.br/hc/article_attachments/42637658447639)
