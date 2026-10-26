---
id: "4405488432663"
titulo: "Candidato executante dinâmico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405488432663-Candidato-executante-din%C3%A2mico"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-08-12T15:44:05Z"
rotulos: ["Configuração", "Workflow", "Centro de Resultado", "Candidato executante dinâmico", "Sankhyaflow", "Usuários candidatos dinâmicos via scripts", "Aprovador varia conforme valor adiantamento", "Scripts configuram candidatos conforme contexto", "JavaScript", "Groovy"]
---

# Candidato executante dinâmico

A definição de usuários candidatos dinâmicos é determinada através de expressões (scripts) na linguagem JavaScript ou Groovy, de acordo com o contexto do processo, sendo possível utilizar todas as funções de consulta para definir o candidato executante dinâmico, como por exemplo, **"getUsuarioInclusao"**, que irá retornar o usuário solicitante do processo.

![Imagem 1: Todas as funções de consulta estão disponíveis o botão de "Ajuda" do campo onde é digitado o script.](https://ajuda.sankhya.com.br/hc/article_attachments/16092145499415) Todas as funções de consulta estão disponíveis o botão de **"Ajuda"** do campo onde é digitado o script.

Ao definir uma expressão em uma determinada tarefa, no momento em que a instância dela for criada, será executada a expressão, definindo assim a lista de seus usuários candidatos.

Esse recurso deve ser utilizado em processo que os candidatos executantes de uma tarefa são desconhecidos, até o momento em que um determinado fluxo de trabalho ou tarefas anteriores sejam executadas.

Existe uma rotina no SankhyaFlow que mantém a lista de usuários candidatos sempre atualizada, ou seja, caso uma tarefa esteja sem um responsável (dono) e ocorra uma alteração, como exemplo, a inserção de um novo usuário em um grupo de usuário, ou a alteração do usuário responsável por um determinado Centro de Resultado, no dia seguinte os usuários candidatos dessa tarefa estarão atualizados.

Para demonstrar essa funcionalidade, iremos utilizar como caso de uso o processo de **"Adiantamento de viagens"**, o qual os candidatos de algumas tarefas irão variar em função de um dado preenchimento em um campo do processo e em relação ao usuário que realizou a solicitação:

![Imagem 2: Para demonstrar essa funcionalidade, iremos utilizar como caso de uso o processo de "Adiantamento de viagens" , o qual…](https://ajuda.sankhya.com.br/hc/article_attachments/15499504149527)

| **Processo de Adiantamento de viagens** |
| --- |

Esse processo permite que qualquer colaborador solicite um adiantamento de viagem para seu líder imediato (responsável pelo Centro de Resultado) ou gerente, sendo que o líder aprova valores de até R$1000,00 e acima desse valor, apenas um determinado grupo de gerentes poderá aprovar. Sendo assim, os usuários candidatos da tarefa **"Aprovar adiantamento de viagem"** irão variar em função do valor informado em um determinado campo de um formulário formatado do processo.

Após aprovação do líder/gerente, a solicitação é direcionada ao solicitante (colaborador), para que ele detalhe todos os gastos ocasionados durante a viagem; dessa forma, o candidato da tarefa **"Apontar despesa de viagem"** estará sempre em função do usuário solicitante.

Enfim, a solicitação é direcionada ao departamento financeiro para realizar a análise das despesas e execução da compensação financeira.

---

Abaixo, demonstraremos as configurações necessárias para atender o processo descrito acima, em relação aos usuários candidatos das tarefas mencionadas.

---

Na tela Processos de Negócio, na tarefa **"Aprovar adiantamento de viagem"**, aba **"Usuários Candidatos"**, sub-aba **"Expressão"**, vamos configurar os candidatos dinâmicos dessa tarefa:

![Imagem 3: Na tela Processos de Negócio, na tarefa "Aprovar adiantamento de viagem" , aba "Usuários Candidatos" , sub-aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4405489619095)

| **Configuração de usuários candidatos dinâmicos** |
| --- |

Conforme o cenário descrito, os usuários candidatos dessa tarefa irão variar conforme o contexto abaixo:

1. Se o valor do adiantamento solicitado for menor ou igual à R$1.000,00, deve ser encaminhado para o responsável do Centro de Resultado do solicitante realizar a aprovação do adiantamento;
2. Caso o valor do adiantamento solicitado for maior do que R$1.000,00, deve ser encaminhado para o grupo de usuário Gerência realizar essa aprovação.

As informações serão obtidas através do campo de um formulário formatado que permite único registro:

**Campo:** VALORADIANTAMENTO
**Formulário:** AD\_SOLICITACAOADIANTAMENTO

Portanto, para que esse cenário ocorra, é necessário escrever o script abaixo contemplando as seguintes informações:

| ``` // Obter dados do formulários var formulario = getLinhasFormulario("AD_SOLICITACAOADIANTAMENTO"); // Validar existência de conteúdo  if (formulario.length > 0) { var valorAdiantamento = formulario[0].getCampo("VALORADIANTAMENTO"); var usuario = getUsuarioInclusao();                // Valor do adiantamento menor ou igual a R$1000,00              if (valorAdiantamento <= "1000"){         // Identificação do usuário responsável pelo centro de resultado do solicitante         var query = [];         var params = [usuario];         query.push(" SELECT ");         query.push("    CODUSURESP AS COLUNA, ");         query.push("    'U' AS TIPO ");        query.push(" FROM ");        query.push("    TSICUS ");        query.push(" WHERE CODCENCUS = (SELECT CODCENCUSPAD FROM TSIUSU WHERE CODUSU = :usuario)");         return getLista(query.join(''), params);     } } // Caso a condição acima não for verdadeira, os usuário candidatos será o grupo de usuário = 9 return "G = 9"; ``` |
| --- |

**Observação:** existem várias formas de concatenar uma string. Nesse exemplo, estamos utilizando um arranjo de dados. Para identificar o usuário responsável pelo centro de resultado do solicitante, a função **getLista** transforma em uma lista de usuários baseados na query escrita e o **query.join** junta todos os elementos da **query.push** retornando em uma linha.

Será possível retornar mais de um grupo, usuário ou equipe, informando sempre o **"Tipo"** (G, U, E) e **"Valor"** em sequência, conforme o exemplo: return 'G=9,U=10,E=11,U=7'

![Imagem 4: Na imagem abaixo apresentamos o script configurado na tarefa:](https://ajuda.sankhya.com.br/hc/article_attachments/4405499562135)Na imagem abaixo apresentamos o script configurado na tarefa:

| **Script usuários candidatos dinâmicos na tarefa** |
| --- |

Após descrever o script, devemos clicar em **"OK"** e salvar as informações.

Agora iremos configurar o usuário candidato dinâmico na tarefa **"Apontar despesas de viagem"**:

![Imagem 5: Agora iremos configurar o usuário candidato dinâmico na tarefa "Apontar despesas de viagem" :](https://ajuda.sankhya.com.br/hc/article_attachments/4405499757335)

| **Configuração de usuários candidatos dinâmicos** |
| --- |

Conforme o contexto do processo, essa tarefa deve ser direcionada sempre ao usuário solicitante; para isso, utilizaremos no script o método abaixo:

| ``` return getUsuarioInclusao() ``` |
| --- |

O método acima sempre irá retornar o usuário que realizou a solicitação:

![Imagem 6: O método acima sempre irá retornar o usuário que realizou a solicitação:](https://ajuda.sankhya.com.br/hc/article_attachments/4405499859863)

| **Script usuários candidatos dinâmicos na tarefa** |
| --- |

Abaixo, no primeiro exemplo, a colaboradora Juliane realizou uma solicitação de adiantamento no valor de R$2.000,00 (tela [Lista de Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595434-Lista-de-Tarefas)):

[GIF animado: Imagem 7: Abaixo, no primeiro exemplo, a colaboradora Juliane realizou uma solicitação de adiantamento no valor de R$2.000,00…](https://ajuda.sankhya.com.br/hc/article_attachments/4405501732375)

| **Solicitação de Adiantamento de viagem** |
| --- |

Como o valor do adiantamento foi maior do que R$1.000,00, os usuários candidatos da tarefa **"Aprovar adiantamento de viagem"** será o grupo de usuários com o código 9. Alice é uma das candidatas desse grupo para realizar a tarefa; sendo assim, ela é quem realizará a aprovação desse adiantamento:

![Imagem 8: Como o valor do adiantamento foi maior do que R$1.000,00, os usuários candidatos da tarefa "Aprovar adiantamento de…](https://ajuda.sankhya.com.br/hc/article_attachments/4405491090711)

| **Usuário candidato da tarefa de Aprovar adiantamento de viagem** |
| --- |

Após a aprovação do adiantamento e a baixa do título, a tarefa **"Apontar despesas de viagem"** irá para a colaboradora Juliane realizar as prestações de contas.

Agora, no segundo exemplo o colaborador Luiz realizou uma solicitação de adiantamento de viagem no valor de R$950,00:

[GIF animado: Imagem 9: Agora, no segundo exemplo o colaborador Luiz realizou uma solicitação de adiantamento de viagem no valor de R$950,00 :](https://ajuda.sankhya.com.br/hc/article_attachments/4405491245335)

| **Solicitação de Adiantamento de viagem** |
| --- |

Como o valor do adiantamento foi menor do que R$1.000,00, o usuário candidato da tarefa de **"Aprovar adiantamento de viagem"** é o responsável pelo Centro de Resultado do solicitante. Nesse caso, o colaborador Luiz faz parte do CR do Comercial, o qual o usuário responsável é a Laura.

Sendo assim, Laura realizará a aprovação desse adiantamento:

![Imagem 10: Sendo assim, Laura realizará a aprovação desse adiantamento:](https://ajuda.sankhya.com.br/hc/article_attachments/4405502380311)

| **Usuário candidato da tarefa de Aprovar adiantamento de viagem** |
| --- |

Após a aprovação do adiantamento e a baixa do título, a tarefa **"Apontar despesas de viagem"** irá para o colaborador Luiz realizar as prestações de contas.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405488432663-Candidato-executante-din%C3%A2mico#top)
