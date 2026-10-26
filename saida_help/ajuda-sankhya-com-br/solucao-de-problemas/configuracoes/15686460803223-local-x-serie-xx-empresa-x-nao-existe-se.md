---
id: "15686460803223"
titulo: "Local: x Série: xx Empresa: x, não existe série para esta empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15686460803223-Local-x-S%C3%A9rie-xx-Empresa-x-n%C3%A3o-existe-s%C3%A9rie-para-esta-empresa"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:56:24Z"
rotulos: ["Produtos", "Configuração", "Importação", "Estoque", "Importação de Dados por Coletor: Requisitos e Contagem", "Erro"]
---

# Local: x Série: xx Empresa: x, não existe série para esta empresa

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16968137738007) MENSAGEM:**

Local: x Série: xx Empresa: x, não existe série para esta empresa.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16968137744151) CAUSA:**

Ocorre ao tentar fazer a contagem de inventário por série sem que a mesma tenha registro na tabela TGFSER.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16968137739287) SOLUÇÃO:**

![Imagem 4: Para que consiga utilizar a importação de dados por coletor, é necessário que tenha registro na TGFSER.](https://ajuda.sankhya.com.br/hc/article_attachments/16968121562903) Para que consiga utilizar a importação de dados por coletor, é necessário que tenha registro na TGFSER.

**Modelo:**

Layout: 999999999999

Exemplo: 120000006664

            120000006748

            120000014825

Onde cada linha do arquivo é um número de série e a quantidade contada é um. Para que o número de série indicado seja contado, será necessário que o número de série inserido no arquivo esteja no cadastro de séries (TGFSER), com a máxima nota e na empresa indicada no campo **"Empresa"** desta tela.

![Imagem 5: Será gerada a contagem na TGFCTS da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/16968137740951) Será gerada a contagem na TGFCTS da seguinte forma:

- DTCONTAGEM – Data da contagem indicada na tela
- TIPCONTAGEM – Tipo "C" - contagem
- CODPROD – Encontrada na tabela de série (TGFSER)
- CODEMP – Código da empresa da tela
- CODLOCAL - Código do local da tela
- ESTOQUE – Quantidade um se for contagem nova.

Se já existir uma contagem com a mesma data, tipo, produto, empresa, local será somada a existente.

Ou seja, na implantação de saldo não é possível, pois ainda não existe registro na TGFSER, somente quando a serie já foi movimentada.

**(1)** Para mais informações consulte o manual da [Importação de Dados Coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609574-Importa%C3%A7%C3%A3o-de-Dados-Coletor?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjoxMDYwMjAyMzEyNzgzMSwidGlja2V0X2lkIjoyOTQxNzYsImNoYW5uZWxfaWQiOjYzLCJ0eXBlIjoiU0VBUkNIIiwiZXhwIjoxNjkwNjMzNTUwfQ.2qVPvd1R7fADzbsZ7rXwg7Z62U5eyCQLTS1EriKLjE4).
