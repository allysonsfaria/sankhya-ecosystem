---
id: "42427410956695"
titulo: "O valor dos negócios ganhos está diferente do valor das vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427410956695-O-valor-dos-neg%C3%B3cios-ganhos-est%C3%A1-diferente-do-valor-das-vendas"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-03T12:57:06Z"
rotulos: ["sync_hc", "ploomes_5452189", "sync_hash_302ff5187966", "ploomes"]
---

# O valor dos negócios ganhos está diferente do valor das vendas

Se os seus relatórios de **negócios ganhos** e de **vendas** estão apresentando valores diferentes, não se preocupe: isso é um comportamento comum do sistema e, na maioria das vezes, está ligado à forma como as datas são contabilizadas.

Para identificar e corrigir essa divergência, siga o método de verificação abaixo:

## 1. Entenda a diferença entre os campos de Data

O principal motivo da diferença nos relatórios é o "gatilho temporal" que cada módulo utiliza:

- **No módulo de Vendas:** O sistema utiliza o campo nativo chamado **Data**. Geralmente, esse campo registra o momento exato em que a venda foi faturada ou concluída.
- **No módulo de Negócios:** O relatório pode estar configurado para olhar para a **Data de Criação** ou **Data de Início** do negócio.

## 2. O cenário do "Negócio de um mês que virou Venda no outro"

A divergência acontece quando um processo comercial atravessa a virada do mês. Veja este exemplo prático:

- **Mês 1 (Janeiro):** O vendedor inicia um atendimento e cria um **Negócio**.
- **Mês 2 (Fevereiro):** O cliente decide fechar, o negócio é marcado como **Ganho** e o sistema gera a **Venda**.

**O que acontece com os relatórios se eles estiverem olhando o mês de Janeiro?**

- O relatório de **Negócios** (por data de criação) vai somar o valor desse contrato em **Janeiro**.
- O relatório de **Vendas** só vai contabilizar esse valor em **Fevereiro** (quando a venda de fato aconteceu).

## Como resolver?

Para que os dois relatórios batam perfeitamente, certifique-se de que ambos estão olhando para o mesmo momento do funil:

- Altere o critério de data do seu relatório de **Negócios** para filtrar pelo campo **Término do negócio**, em vez da Data de Criação.

Dessa forma, tanto o negócio ganho quanto a venda serão contabilizados exatamente no mesmo mês, eliminando a diferença nos gráficos!
