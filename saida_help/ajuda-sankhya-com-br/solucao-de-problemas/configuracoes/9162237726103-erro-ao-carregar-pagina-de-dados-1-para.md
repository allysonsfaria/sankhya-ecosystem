---
id: "9162237726103"
titulo: "Erro ao carregar página de dados 1 para ViewFinanceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9162237726103-Erro-ao-carregar-p%C3%A1gina-de-dados-1-para-ViewFinanceiro"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-03T14:15:15Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "CORE_E00358", "Correção de Filtro em View Financeiro", "Erro"]
---

# Erro ao carregar página de dados 1 para ViewFinanceiro

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19033134286743) MENSAGEM:**

[CORE\_E00358] Erro ao carregar página de dados 1 para ViewFinanceiro.
A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, <, <= , >, >= ou quando ela é usada como uma expressão.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033149365911) SITUAÇÃO:**

Ao tentar acessar as telas Movimentação financeira ou Compensação financeira a mensagem abaixo é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19033134313367) CAUSA:**

Quando o filtro possui alguma condição incorreta ou incompleta.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033149386135) SOLUÇÃO:**

- Necessário verificar se a tela possui algum filtro, sendo o padrão ou algum criado. Caso possua algum filtro, faça o teste retirando o filtro. Se o erro deixar de ocorrer verifique a expressão utilizada nesse filtro;
- Para visualizar o filtro padrão é necessário acessar o sistema com o usuário SUP;

![Imagem 5: Para visualizar o filtro padrão é necessário acessar o sistema com o usuário SUP;](https://ajuda.sankhya.com.br/hc/article_attachments/19033149394327)

- Identificado o filtro é necessário revisar o mesmo, pois alguma condição do filtro ficou incorreta ou incompleta causando o erro apresentado na tela. Se o erro persistir, verificar se existe campo adicional calculado na tabela.

![Imagem 6: Identificado o filtro é necessário revisar o mesmo, pois alguma condição do filtro ficou incorreta ou incompleta…](https://ajuda.sankhya.com.br/hc/article_attachments/19033134335511)
