---
id: "17123178705815"
titulo: "Erro Geração ICMS/IPI  apresenta erro:  By zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17123178705815-Erro-Gera%C3%A7%C3%A3o-ICMS-IPI-apresenta-erro-By-zero"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:53:50Z"
rotulos: ["Fiscal", "NF-e", "IPI", "ICMS", "Impostos", "Divisão por zero", "Zerar BASE DE ICMS ou incluir VLR ICMS nas notas", "BASE DE ICMS maior que zero sem VLR ICMS", "Erro"]
---

# Erro Geração ICMS/IPI  apresenta erro:  By zero

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17123238643607) **MENSAGEM:**

Ao executar a rotina **Geração ICMS/IPI** apresenta seguinte erro:  / by zero.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17123208294551)CAUSA:**

Ocorre quando o valor da BASE DE ICMS tem algum valor e o ICMS em questão não foi incluído.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17123223547799)SOLUÇÃO:**

Não deve existir o cenário onde, nas notas lançadas no sistema, que serão levadas aos livros fiscais de ICMS/IPI, tenham BASE DE ICMS maior que zero e, não tenham VLR ICMS, pois durante os processamentos, há o calculo de divisão do valor do ICMS pela BASE ICMS, e isso causa a mensagem apresentada e citada nesse artigo, então se não há valores de ICMS na nota, a base deve estar zerada também.
