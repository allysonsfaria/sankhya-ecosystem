---
id: "360055751594"
titulo: "Não pode incluir uma tabela com data VIGOR anterior ou igual a última data da tabela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360055751594-N%C3%A3o-pode-incluir-uma-tabela-com-data-VIGOR-anterior-ou-igual-a-%C3%BAltima-data-da-tabela"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:27:28Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "Atualização", "ORA-06512", "Inserir data de vigor maior", "Data de vigor anterior à última", "Data de vigor não atualizada", "Erro"]
---

# Não pode incluir uma tabela com data VIGOR anterior ou igual a última data da tabela

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17282542053527) MENSAGEM:**

Não pode incluir uma tabela com data VIGOR anterior ou igual a última data da tabela
(Nutab: XXX DtVigor: XX/YY/ZZZZ)
[ORA-06512]: em "SANKHYA.TRG\_INC\_TGFTAB\_AFTER" line 101

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17282498808855) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela "Atualização de preço de venda" em: Comercial>>Rotinas>>Atualização de Preço de Venda](https://ajuda.sankhya.com.br/hc/article_attachments/17282498814487) Acesse a tela **"Atualização de preço de venda"** em: Comercial>>Rotinas>>Atualização de Preço de Venda

Faça um filtro, para buscar a tabela desejada para alteração de preço de produto.
No resultado, é possível identificar o código da tabela e a data de vigor, podendo ordenar por ordem crescente.

Utilize a opção de reajuste por índice ou pelo botão (+), para inserir um novo preço com Data de Vigor, maior que a data do último preço da referida tabela, ou seja:
Se estiver atualizando preço da tabela 9, na qual data de vigor é 13/01/2021, informe uma data de vigor maior que 13/01/2021, pois já existe uma atualização de preço para a tabela superior a 13/01/2021

- A aplicação não permite excluir uma atualização de preço antiga, caso já tenha sido vendido itens daquela tabela;
- A aplicação não permite incluir preço de venda inferior à última data de vigor da tabela.

(1)** Artigos relacionados:** [Atualização de Preço de Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612094)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17282498820759) CAUSA:**

Ocorre quando estiver tentando uma atualização de preço para entrar em vigor dia 12/07/2012, porém na Tabela de preços já existe uma atualização para a data 15/07/2012, então ao tentar inserir acusa o erro acima.
