---
id: "4408440807831"
titulo: "Prazos de vencimento nas tarefas de usuário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4408440807831-Prazos-de-vencimento-nas-tarefas-de-usu%C3%A1rio"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:10:24Z"
rotulos: ["Configuração", "Prazos", "Fluxo de Processos", "Financeiro", "Sankhyaflow", "Prazos de vencimento nas tarefas de usuário", "Definir prazos para tarefas", "Notificações e status configurados", "Adiantamento de viagens aprovado", "Tarefas de Usuário"]
---

# Prazos de vencimento nas tarefas de usuário

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313355776279) Versão disponível: a partir da 4.9
```

---

Esse é um recurso que permite definir prazos de execução para as Tarefas de Usuário e geralmente é utilizando quando a empresa identifica a necessidade de estabelecer um prazo para as pessoas executarem uma determinada tarefa.

Em um processo de compras, por exemplo, podemos definir um prazo para os usuários que realizam a tarefa **"Realizar cotação"** (cotar preço/valor de algo) concluírem essa atividade.

Em nosso caso de uso, apresentaremos o processo de **"Adiantamento de viagens**":

![Imagem 2: Em nosso caso de uso, apresentaremos o processo de "Adiantamento de viagens ":](https://ajuda.sankhya.com.br/hc/article_attachments/4408438283927)

| **Processo de Adiantamento de viagens** |
| --- |

Esse processo permite que qualquer colaborador solicite um adiantamento de viagem para seu líder imediato aprovar ou não essa solicitação. Essa análise tem o prazo de vencimento de 1 dia; conforme esse prazo for vencendo, o líder é alertado na tarefa e caso ele não analise dentro desse período, também será notificado sobre o status dessa tarefa via e-mail/sistema.

Aprovando a solicitação, ela é direcionada ao solicitante (colaborador), para que o mesmo detalhe todos os gastos ocasionados durante a viagem. Por fim, a solicitação é direcionada ao departamento financeiro realizar a análise das despesas e executar a compensação financeira.

Para que a tarefa **"Aprovar adiantamento de viagem"** tenha um prazo estabelecido, devemos habilitar a marcação **"Utilizar prazo?"**:

![Imagem 3: Para que a tarefa "Aprovar adiantamento de viagem" tenha um prazo estabelecido, devemos habilitar a marcação "Utilizar…](https://ajuda.sankhya.com.br/hc/article_attachments/4408438559639)

| **Utilizar prazo na tarefa** |
| --- |

Agora, o próximo passo é realizar as configurações necessárias para que o prazo de vencimento seja de 1 dia. Para isso, acessamos o botão **"Abrir configuração de Prazos de vencimento"** e na aba **"Prazo"** definimos o seguinte:

- **Tipo de Prazo:** Fixo, pois sempre será o mesmo prazo.
- **Prazo em:** Dia(s).
- **Dias ou Horas:** 1

![Imagem 4: Dias ou Horas: 1](https://ajuda.sankhya.com.br/hc/article_attachments/4408438667287)

| **Configurando prazo na tarefa** |
| --- |

---

| ![Imagem 5: Configurando prazo na tarefa](https://ajuda.sankhya.com.br/hc/article_attachments/42313295204631) | Caso seja necessário definir um prazo dinâmico para uma mesma Tarefa de Usuário, em função de um critério informado em um formulário, deve ser utilizado o Tipo de Prazo Variável, para que seja possível escrever uma expressão em JavaScript ou Groovy e determinar a data de vencimento da tarefa. Nessa expressão poderão ser utilizadas todas as funções de consulta (disponível no help do script) para buscar os dados que foram preenchidos no processo. |
| --- | --- |

---

Status é a situação de uma tarefa em relação ao seu prazo de vencimento. Por padrão, cada status (No prazo, A vencer, Vencido, Muito Vencido) tem um tempo decorrido já definido e, caso seja necessário, o modelador poderá alterá-lo. No status **"A vencer"**, por exemplo, o tempo decorrido padrão é de 70%, ou seja, quando atingir 70% do prazo estabelecido, a tarefa entrará no status A vencer.

**Observação:** na aba **"Status"**, o campo **"Contagem"** determina se o tempo decorrido será contado em **"Percentual"**, **"Dia(s)"** ou **"Hora(s)"**; por padrão ele já vem preenchido com a opção Percentual.

![Imagem 6: Observação: na aba "Status" , o campo "Contagem" determina se o tempo decorrido será contado em "Percentual" , "Dia(s)"…](https://ajuda.sankhya.com.br/hc/article_attachments/4408525137303)

| **Configurando status** |
| --- |

Para que o responsável pela tarefa Aprovar adiantamento de viagem visualize na Lista de Tarefas os status, conforme o prazo estabelecido for vencendo, manteremos ativo todos os status e para todos eles iremos configurar para que o dono/candidato da tarefa receba as notificações via e-mail e por sistema; para isso, selecionamos no **"Tipo"** a opção **"Ambas"** e informamos uma **"Conta SMTP"**. Também será possível inserir mais destinatários através de Scripts SQL porém não faremos nesse caso de uso.

Por fim, ao acessar a aba Prazo de vencimento, teremos o resumo de todas as configurações realizadas de prazo para essa tarefa:

![Imagem 7: Por fim, ao acessar a aba Prazo de vencimento , teremos o resumo de todas as configurações realizadas de prazo para…](https://ajuda.sankhya.com.br/hc/article_attachments/4408526237975)

| **Resumo do prazo configurado** |
| --- |

Conforme as configurações realizadas, apresentaremos agora a visualização do prazo de vencimento e do status na tarefa (Lista de Tarefas).

Ao realizar a solicitação de um Adiantamento de viagem, a mesma foi direcionada para seu líder aprovar. Nesse exemplo, a solicitação foi feita no dia 21/09/2021 às 14:07:50 e, sendo assim, o prazo de vencimento é em 22/09/2021 às 14:07:50 e o status é **"No prazo"**, como apresentado no card e no cabeçalho da tarefa:

![Imagem 8: Ao realizar a solicitação de um Adiantamento de viagem , a mesma foi direcionada para seu líder aprovar. Nesse exemplo,…](https://ajuda.sankhya.com.br/hc/article_attachments/4409138814871)

| **Prazo e status na tarefa** |
| --- |

Assim como configurado nos status, o dono/candidato da tarefa receberá uma notificação via sistema e e-mail o informando sobre o status do prazo de vencimento da tarefa:

![Imagem 9: Assim como configurado nos status, o dono/candidato da tarefa receberá uma notificação via sistema e e-mail o…](https://ajuda.sankhya.com.br/hc/article_attachments/4409134198679)

| **Notificação via sistema do status do prazo de vencimento da tarefa** |
| --- |

![Imagem 10: Notificação via sistema do status do prazo de vencimento da tarefa](https://ajuda.sankhya.com.br/hc/article_attachments/4409134307479)

| **Notificação via e-mail do status do prazo de vencimento da tarefa** |
| --- |

**Nota:** conforme for atingido o tempo decorrido que foi configurado em cada status, no card e no cabeçalho da tarefa o status será atualizado; por exemplo, ao atingir 70% do prazo decorrido de 1 dia, o status será atualizado para A vencer.

Outra funcionalidade com o prazo de vencimento no card da tarefa, é utilizar ele como critério na **"Ordenação das Tarefas"** de acordo com o seu vencimento, podendo ser **"Mais próximos primeiro"** ou **"Mais distantes primeiro"**:

![Imagem 11: Outra funcionalidade com o prazo de vencimento no card da tarefa, é utilizar ele como critério na "Ordenação das…](https://ajuda.sankhya.com.br/hc/article_attachments/4408532928023)

| **Ordenação das tarefas de acordo com o vencimento** |
| --- |

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4408440807831-Prazos-de-vencimento-nas-tarefas-de-usu%C3%A1rio#top)
