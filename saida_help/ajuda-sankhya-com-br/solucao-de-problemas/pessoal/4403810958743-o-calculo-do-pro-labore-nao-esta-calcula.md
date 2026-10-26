---
id: "4403810958743"
titulo: "O cálculo do Pró-labore não está calculando o desconto INSS na folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403810958743-O-c%C3%A1lculo-do-Pr%C3%B3-labore-n%C3%A3o-est%C3%A1-calculando-o-desconto-INSS-na-folha"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:42Z"
rotulos: ["Configuração", "Impostos", "Folha", "INSS", "não apagar", "#validadoRayssa", "Cálculo do Pró-Labore Sem Desconto de INSS", "Pró-labore"]
---

# O cálculo do Pró-labore não está calculando o desconto INSS na folha

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16345466800791) MENSAGEM:**

O cálculo do Pró-labore não está calculando INSS.

**![Imagem 2: SOLUÇÃO: Verifique se a fórmula utilizada está de acordo com a padrão:](https://ajuda.sankhya.com.br/hc/article_attachments/16345466803991) SOLUÇÃO:**
Verifique se a fórmula utilizada está de acordo com a padrão:

**INSS - PRO LABORE**

| TruncFol(IF((QueFuncionario.VINCULO = 80), IF((&E1912 + &E505) <= FTF(5, 3, (&E1912 + &E505), &Refere, QueFuncionario.TIPTAB), (((&E1912 + &E505) \* 0.11) - &E506), (FTF(5, 2, (&E1912 + &E505), &Refere, QueFuncionario.TIPTAB) - &E506)), 0), 2) |
| --- |

Observe o tipo de tabela de **INSS/IRRF/SAL FAM** no cadastro do Pró-labore se está como **tipo A - Empresas Privadas.** Logo após, veja a tabela de Faixa de Salário Mínimo, se a mesma está cadastrada de acordo com formato de modelo abaixo. Pois, o campo limite da faixa precisa estar cadastrado com sequência de sete números 9 (9999999), na qual os pontos e a virgula é carregada automaticamente pelo sistema.

Valor 1 - Valor do salário mínimo.

Valor 2 - Valor máximo de desconto.

Valor 3 - Teto máximo de contribuição.

Como o Pró-labore não segue a nova regra de desconto de INSS, a verificação do teto de contribuição é feita através da tabela de faixa de código 5 - SALÁRIO MÍNIMO:

![Imagem 3: Como o Pró-labore não segue a nova regra de desconto de INSS, a verificação do teto de contribuição é feita através da…](https://ajuda.sankhya.com.br/hc/article_attachments/4403811663383)

**![Imagem 4: CAUSA: A tabela de Faixa de Salário Mínimo estava cadastrada com campo limite da faixa = 1.](https://ajuda.sankhya.com.br/hc/article_attachments/16345466805783) CAUSA:**
A tabela de Faixa de Salário Mínimo estava cadastrada com campo limite da faixa = 1.
