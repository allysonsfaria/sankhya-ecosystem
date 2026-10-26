---
id: "26952551759895"
titulo: "Regras sistêmicas para alimentação do Campo Chave CT-e de Referência (tela Cadastro Livro ICMS IPI)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26952551759895-Regras-sist%C3%AAmicas-para-alimenta%C3%A7%C3%A3o-do-Campo-Chave-CT-e-de-Refer%C3%AAncia-tela-Cadastro-Livro-ICMS-IPI"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:40:29Z"
rotulos: ["CT-e", "Configuração", "Livros Fiscais", "ICMS", "TOP", "regras sistêmicas para a alimentação do campo \"Chave CT-e de Referência\"", "validações Chave CT-e de Referência", "Chave CT-e de Referência", "Documentos Eletrônicos"]
---

# Regras sistêmicas para alimentação do Campo Chave CT-e de Referência (tela Cadastro Livro ICMS IPI)

Durante a geração dos livros fiscais (Processo da tela **"Geração ICMS IPI"**), o sistema avalia se o documento que está sendo gerado foi lançado com os seguintes modelos: **57, 63 ou 67**, pois esses modelos de documentos são as validações que iniciam a construção da informação do campo **"Chave CT-e de Referência".**

#### **(1)** Item 1°

A próxima validação, que o sistema realiza, é se o documento em questão foi lançado com uma TOP do **tipo de movimento "Venda"** e, também, se uma determinada rotina que existia apenas no MGE **não** está em uso na base. Pois, hoje na aplicação SankhyaOm não temos o campo que acionava essa rotina. Diante disso, existe uma consulta na tela DBExplorer que verifica se a empresa da geração em questão está ou não com essa rotina ativada:

SELECT INTEGCTE
FROM TGFEMP EMP
WHERE EMP.CODEMP = ???

OBS: Substituir os pontos de interrogação pelo código da empresa.

Rotina em questão, que não pode estar em uso:

![Imagem 1: Rotina em questão, que não pode estar em uso:](https://ajuda.sankhya.com.br/hc/article_attachments/27109374592919)

Se o retorno da consulta for o valor zero, então a empresa não usa essa determinada rotina e o sistema segue para as próximas análises de validações.

A próxima validação que o sistema faz é se a TOP do documento em questão, estava com o campo **"Tipo de emissão CT-e"** com uma das seguintes opções: **anulação ou complementar**.

![Imagem 2: A próxima validação que o sistema faz é se a TOP do documento em questão, estava com o campo "Tipo de emissão CT-e" com…](https://ajuda.sankhya.com.br/hc/article_attachments/27109374594711)

Se todas as validações forem atendidas, o valor do campo Chave CT-e (TGFCAB.CHAVECTE) da **nota origem** do CT-e complementar/anulação será gerado.

A nota origem deverá ser obtida através da ligação realizada na tabela TGFVAR (rotina de **"Documentos relacionados"**).

#### **(1)** Item 2°

Caso as validações do **Item 1°** falhem, o sistema verificará se nos financeiros do documento em questão, e/ou se o documento em questão, tem origem direta na tela **"Movimentação Financeira".** Assim, tem-se o campo  Chave CT-e de Referência preenchido e essa informação será levada para os livros fiscais.
