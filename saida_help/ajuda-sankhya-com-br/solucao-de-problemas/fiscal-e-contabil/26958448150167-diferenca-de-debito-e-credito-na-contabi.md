---
id: "26958448150167"
titulo: "Diferença de Débito e Crédito na contabilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26958448150167-Diferen%C3%A7a-de-D%C3%A9bito-e-Cr%C3%A9dito-na-contabiliza%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:40:26Z"
rotulos: ["Fórmulas", "Crédito", "TOP", "Contabilização", "Financeiro", "Débito", "Diferença de Débito e Crédito na contabilização", "método das partidas dobradas", "Erro"]
---

# Diferença de Débito e Crédito na contabilização

O **método das partidas dobradas** é um princípio contábil que registra cada transação em pelo menos duas contas, garantindo que o total de **débitos** seja igual ao total de **créditos**.

Isso mantém o equilíbrio da contabilidade e reflete a equação básica:

**Ativo = Passivo + Patrimônio Líquido**.

Cada transação afeta pelo menos uma conta no débito e outra no crédito. O método assegura precisão, transparência e controle sobre as finanças, ajudando a identificar erros e fraudes.

Diante disso, sabemos o motivo pelo qual o sistema não pode permitir contabilizar com diferenças.

Posso ter vários débitos para um crédito e vice versa, ou vários débitos e créditos que no final vai fechar o valor de débito e crédito

**Exemplos:**

(1)** Um Débito para vários créditos**

D - 100,00

C-    50,00

C-    50,00

(1)** Um Crédito Para vários débitos**

C - 100,00

D -   50,00

D -   25,00

D -   25,00

(1)** Vários Créditos e Vários Débitos**

C-   75,00

   C-   25,00

   D-   75,00

   D-   25,00

Em todos os exemplos acima, o Total de Débito é 100,00 e o Total de Crédito é 100,00, obedecendo o método das partidas dobradas.

Foi usado como exemplo uma Nota de exemplo no valor de 420,00 + ICMS de 75,60

Na tela **"Agendamento"** (contabilização>> Rotinas): ao rodar a contabilização mostra a quantidade de lançamentos, a quantidade de contabilizados 0 e a qtde não contabilizados 1

- Esse cenário indica que houve um problema na contabilização. Mesmo a mensagem indicando Contabilização concluída com sucesso, a quantidade não contabilizada mostra que não gerou lote.

![Imagem 1: Esse cenário indica que houve um problema na contabilização. Mesmo a mensagem indicando Contabilização concluída com…](https://ajuda.sankhya.com.br/hc/article_attachments/27059341518103)

- Clique no botão **"Ver Não Contabilizados":** o sistema mostra detalhes do que precisa para analisar.
- Na coluna "**Descrição do Problema":** é possível ver que o sistema retornou a mensagem Divergência no documento: Tot. Débito: 420,00, Tot. Crédito: 0,00

![Imagem 2: Na coluna " Descrição do Problema": é possível ver que o sistema retornou a mensagem Divergência no documento: Tot.…](https://ajuda.sankhya.com.br/hc/article_attachments/27059341520791)

- **Dê um duplo clique na linha da nota que quer analisar:** o sistema irá direcionar para o documento que está tentando contabilizar.

[GIF animado: Imagem 3: Dê um duplo clique na linha da nota que quer analisar: o sistema irá direcionar para o documento que está tentando…](https://ajuda.sankhya.com.br/hc/article_attachments/27059341523351)

**![Imagem 4: Nessa etapa é necessário atenção em alguns pontos:](https://ajuda.sankhya.com.br/hc/article_attachments/27059040881943) Nessa etapa é necessário atenção em alguns pontos:**

- Verifique a  TOP de contabilização, o que tem de fórmulas para entender os valores que o sistema está buscando.

**Exemplo:** o valor da nota é 420,00, porém tem 75,60 de ICMS, valor total de débito e de crédito visualmente em uma contabilização seria 495,60.

D Estoque 420,00

C Caixa     420,00

D Caixa       75,60

C ICMS a Recolher 75,60

Por isso, é importante entender quais valores na nota estão tentando contabilizar. Se ele tivesse tentando contabilizar só o valor da nota por exemplo, seria somente os 420,00.

**Exemplo:**

D Estoque 420,00

C Caixa     420,00

Na tela do agendamento, clique no botão **"Ver Não Contabilizados novamente",** dê um duplo clique na TOP, ou pegue o número da TOP e pesquise na tela TOP de contabilização.

![Imagem 5: Na tela do agendamento, clique no botão "Ver Não Contabilizados novamente", dê um duplo clique na TOP, ou pegue o…](https://ajuda.sankhya.com.br/hc/article_attachments/27059341525911)

Em seguida, na tela **TOP Contabilização, comece verificando as linhas e as fórmulas** configuradas que irão buscar os valores que vão para o lançamento contábil.

Na TOP em questão (1401), vê-se que existe linha contabilizando somente o débito.

Não existe fórmula para contabilizar a linha do crédito.

![Imagem 6: Não existe fórmula para contabilizar a linha do crédito.](https://ajuda.sankhya.com.br/hc/article_attachments/27059363814039)

**Importante:** esse é um dos possíveis cenários.

- Posso ter as fórmulas configuradas com variáveis erradas;
- Posso ter fórmulas usando IF que condicionam a busca do valor e as condições não são atendidas para busca de tal valor.

Fórmulas permitem personalizar a busca de diversas formas, com isso é necessário entender da construção das mesmas.

Pode-se entender melhor nos seguintes manuais.

[TOP Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o)

[Ebook Gestão Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/6422445057943-Ebook-Gest%C3%A3o-Cont%C3%A1bil)
