---
id: "28148339768599"
titulo: "Não foi possível carregar a lista de funcionários. Motivo: A subconsulta retornou mais de 1 valor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28148339768599-N%C3%A3o-foi-poss%C3%ADvel-carregar-a-lista-de-funcion%C3%A1rios-Motivo-A-subconsulta-retornou-mais-de-1-valor"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:00Z"
rotulos: ["Configuração", "DBExplorer", "Aviso Prévio", "Reajuste Salarial", "Isso não é permitido quando a subconsulta segue um", "Não foi possível carregar a lista de funcionários. Motivo: A subconsulta retornou mais de 1 valor", "ou quando ela é usada como uma expressão", "Pessoal+", "Erro"]
---

# Não foi possível carregar a lista de funcionários. Motivo: A subconsulta retornou mais de 1 valor

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/28150146281623) MENSAGEM:**

Não foi possível carregar a lista de funcionários. 

Motivo: A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, <, <= , >, >= ou quando ela é usada como uma expressão.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28150150873623) SITUAÇÃO:**

Ao realizar o Reajuste Salarial por meio do caminho:

**Pessoal+ » Rotinas Folha » Reajuste Salarial**, após preencher todos os campos necessários, ocorre um erro ao tentar carregar a lista de funcionários.

![Imagem 3: Pessoal+ » Rotinas Folha » Reajuste Salarial , após preencher todos os campos necessários, ocorre um erro ao tentar…](https://ajuda.sankhya.com.br/hc/article_attachments/28148339753623)

![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28150146290711) **SOLUÇÃO:**

**![Imagem 5: Identifique os funcionários com aviso prévio duplicado, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/28150146293271) Identifique os funcionários com aviso prévio duplicado, siga os passos abaixo:**

1. Acesse a tela Configurações » Avançado » DBExplorer.
2. Execute a seguinte consulta:

SELECT CODFUNC, COUNT(\*) FROM TFPAVI

WHERE CODEMP = ‘xx’

GROUP BY CODFUNC

HAVING COUNT(\*) > 1

**\*\* Trocar o 'xx' pelo código da empresa.**

**![Imagem 6: Realize o cancelamento do aviso incoerente.](https://ajuda.sankhya.com.br/hc/article_attachments/28150150883223) Realize o cancelamento do aviso incoerente.**

1. Acesse a tela Pessoal+ » Cadastros » Aviso Prévio;
2. Faça a busca pelo funcionários encontrado;
3. Preencha os campos de cancelamento do aviso.

![Imagem 7: Preencha os campos de cancelamento do aviso.](https://ajuda.sankhya.com.br/hc/article_attachments/28148339760535)

![Imagem 8: Realize o procedimento de reajuste salarial selecionando os funcionários. Agora, o processo deve ser concluído sem que…](https://ajuda.sankhya.com.br/guide-media/01HY3RKFT1NYRAS4YDHR5QPXNE) **Realize o procedimento de reajuste salarial selecionando os funcionários. Agora, o processo deve ser concluído sem que a mensagem de erro seja exibida.**

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/28150146288663) CAUSA:**

Foi identificado um registro duplicado de aviso prévio para o funcionário com sequência 2, sem que o aviso prévio da sequência anterior tenha sido cancelado.
