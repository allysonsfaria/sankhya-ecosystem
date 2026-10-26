---
id: "4409305580439"
titulo: "Multiplicidade Sequencial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:10:52Z"
rotulos: ["Configuração", "Eventos", "Projeto", "sankhyaflow", "Multiplicidade Sequencial", "Define instâncias e scripts para etapas de aprovação", "Tarefas são executadas uma após a outra", "Aprovações em cascata para compras", "Multiplicidade"]
---

# Multiplicidade Sequencial

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313341564439) Versão disponível: a partir da 4.7
```

---

A multiplicidade é um recurso do SankhyaFlow que possibilita ao modelador configurar a abertura de uma determinada Tarefa de Usuário quantas vezes forem necessárias, de forma paralela ou sequencial.

A Multiplicidade Sequencial executa sequencialmente uma mesma Tarefa de Usuário diversas vezes dentro do fluxo, antes da próxima etapa do processo.

Esse recurso é utilizado quando uma mesma tarefa precisa ser executada por uma pessoa e, na sequência, existe a necessidade de outra(s) pessoa(s) também realizar(em) a mesma tarefa.

Como exemplo, podemos citar uma liberação em cascata. Em uma política de desconto nas vendas, pode ser que uma determinada faixa de valores de desconto seja aprovada de gestor a gestor, ou seja, uma mesma atividade seja aprovada sequencialmente porém, o segundo gestor somente aprova caso o primeiro tenha aprovado, o terceiro somente após o segundo e assim por diante.

Nessa documentação trataremos sobre nosso [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#casodeuso), a [Configuração de uma Tarefa de Usuário com Multiplicidade Sequencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#configura%C3%A7%C3%A3odeumatarefadeusu%C3%A1riocommultiplicidadesequencial), as [Demais configurações do Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#demaisconfigura%C3%A7%C3%B5esdocasodeuso), [Outras informações sobre Multiplicidade Sequencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#outrasinforma%C3%A7%C3%B5essobremultiplicidadesequencial) e os [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#resultados).

---

#### Caso de Uso

A empresa Beta Ltda utiliza o SankhyaFlow em seu processo de compras que está representado na imagem abaixo:

![Imagem 2: A empresa Beta Ltda utiliza o SankhyaFlow em seu processo de compras que está representado na imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/4409307432215)

| **Processo de Compras com Multiplicidade Sequencial** |
| --- |

Esse processo contempla as etapas de **"Solicitação de compras"**: Aprovação da Solicitação, Cotação dos produtos para garantir os melhores preços e Aprovação da compra utilizando a multiplicidade sequencial para realizar as alçadas de aprovações:

![Imagem 3: Esse processo contempla as etapas de "Solicitação de compras" : Aprovação da Solicitação , Cotação dos produtos para…](https://ajuda.sankhya.com.br/hc/article_attachments/4409299098903)

| **Tabela de alçadas de aprovação da empresa Beta Ltda** |
| --- |

Sendo assim, quando os itens aprovados das cotações forem de até R$10.000,00, o fluxo irá executar a multiplicidade e instanciar a primeira tarefa para o Coordenador de Suprimentos.

Na situação que a compra tiver um valor de R$15.000,00, será instanciada uma tarefa para o Coordenador de Suprimentos e, na sequência, será criada uma instância para o Gerente Administrativo Financeiro, pois a compra excede o valor de R$10.000,00.

Se a compra tiver um valor acima de R$50.000,00, haverá a criação da tarefa **"Aprovar compra"** por 4 vezes, respeitando a tabela acima, ou seja, será criada a primeira tarefa para o Coordenador de Suprimentos e quando finalizada essa atividade, serão criadas as tarefas até a última atividade, sendo ela do Diretor Presidente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#top)

#### Configuração de uma Tarefa de Usuário com Multiplicidade Sequencial

De acordo com a tabela acima, para que a aprovação da compra seja direcionada aos responsáveis por cada nível de aprovação, devemos configurar na Tarefa de Usuário **"Aprovar compra"**, a multiplicidade sequencial:

![Imagem 4: De acordo com a tabela acima, para que a aprovação da compra seja direcionada aos responsáveis por cada nível de…](https://ajuda.sankhya.com.br/hc/article_attachments/4409310103831)

| **Inserindo a Multiplicidade Sequencial** |
| --- |

Após definir que a Tarefa de Usuário terá a multiplicidade do tipo sequencial, precisamos definir a quantidade de instâncias que serão geradas. Nesse caso de uso, a quantidade vem em função do valor total das cotações aprovadas, ou seja, dependendo do valor de compra, será gerada de 1 a 4 tarefas sequencialmente; para isso, precisamos escrever um script que retornará um valor. Lembrando que esse script será dependente do script abordado no tópico [Demais configurações do Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#demaisconfigura%C3%A7%C3%B5esdocasodeuso).

O script será:

![Imagem 5: O script será:](https://ajuda.sankhya.com.br/hc/article_attachments/4409310127383)

| **Script quantidade de tarefas** |
| --- |

| ``` var resultado = getCampo("VALORTOTAL"); if (resultado == 1) {  return 1;  } else if (resultado == 2) {  return 2;  } else if (resultado == 3) {  return 3;  } else return 4; ``` |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#top)

#### Demais configurações do Caso de Uso

Em função do caso de uso, podemos ter vários usuários donos da tarefa **"Aprovar cotação"**; sendo assim, é necessário um script que abarque esse cenário:

| ``` var query = getQuery(); query.setParam("IDINSTPRN", getIdInstanceProcesso());  query.nativeSelect("SELECT CODUSUDONO FROM TWFITAR WHERE IDINSTTAR IN (SELECT MAX(IDINSTTAR) FROM TWFITAR WHERE IDELEMENTO = 'UserTask_0qlww1u' AND  IDINSTPRN = {IDINSTPRN} AND DHCONCLUSAO IS NOT NULL)"); if (query.next()) { var usuario= query.getInt("CODUSUDONO"); if (usuario == 17){ return "U=111"; } else if (usuario == 111){ return "U=16"; } else return "U=14"; }else{ return "U=17"; } ``` |
| --- |

**Observação:** para mais detalhes sobre as configurações de usuários candidatos dinâmicos acesse a documentação [Candidato executante dinâmico](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405488432663-Candidato-executante-din%C3%A2mico).

Para facilitar a escrita do script de Quantidade de Instâncias, conforme apresentamos no tópico [Configuração de uma Tarefa de Usuário com Multiplicidade Sequencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#configura%C3%A7%C3%A3odeumatarefadeusu%C3%A1riocommultiplicidadesequencial) , vamos configurar um outro script na Tarefa de Usuário **"Realizar cotação"**, para somar o valor total das cotações aprovadas e categorizar nas faixas de aprovação do Coordenador de Suprimentos ao Diretor. Para isso, utilizaremos o recurso de Eventos:

[GIF animado: Imagem 6: Para facilitar a escrita do script de Quantidade de Instâncias , conforme apresentamos no tópico Configuração de uma…](https://ajuda.sankhya.com.br/hc/article_attachments/4409300626199)

| **Configuração de Evento** |
| --- |

| ``` var query = getQuery(); query.setParam("IDINSTPRN", getIdInstanceProcesso()); query.nativeSelect("SELECT SUM (TOTAL) AS total FROM AD_COTACOESDEITENS WHERE IDINSTPRN = {IDINSTPRN} AND COTACAOAPROVADA = 'S'"); if (query.next()) { var total = query.getBigDecimal("total"); if (total  >= 50000) { setCampo ("VALORTOTAL", 4); //nivel presidente }else if (total  >=30000 && total < 50000) { setCampo ("VALORTOTAL", 3); //nivel diretor financeiro }else if (total  >=10000 && total < 30000) { setCampo ("VALORTOTAL", 2); //nivel gerente financeiro }else if (total <= 10000) { setCampo("VALORTOTAL", 1); //nivel coordenador } } ``` |
| --- |

**Nota:** para verificar mais informações sobre as configurações de eventos, acesse a documentação [Eventos de Processos e Eventos de Tarefa](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#top)

#### Outras informações sobre Multiplicidade Sequencial

Podemos definir uma expressão em JavaScript ou Groovy na **"Condição de Parada"**; caso essa expressão retorne verdadeiro, ao finalizar uma execução de uma tarefa com multiplicidade sequencial, a próxima execução que viria a ser criada não será mais, encerrando então a multiplicidade sequencial da tarefa:

![Imagem 7: Podemos definir uma expressão em JavaScript ou Groovy na "Condição de Parada" ; caso essa expressão retorne verdadeiro,…](https://ajuda.sankhya.com.br/hc/article_attachments/4409310226071)

| **Configuração Condição de Parada** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#top)

#### Resultados

Um responsável fará o lançamento de uma Solicitação de compras. Se ele for o mesmo responsável pelo Centro de Resultado, a próxima atividade já será a de Realizar Cotação.

![Imagem 8: Um responsável fará o lançamento de uma Solicitação de compras. Se ele for o mesmo responsável pelo Centro de Resultado…](https://ajuda.sankhya.com.br/hc/article_attachments/4409310337303)

| **Lançamento da Solicitação de compras** |
| --- |

Após lançada, a tarefa seguinte é a do responsável por fazer as cotações com os parceiros fornecedores:

![Imagem 9: Após lançada, a tarefa seguinte é a do responsável por fazer as cotações com os parceiros fornecedores:](https://ajuda.sankhya.com.br/hc/article_attachments/4409310719255)

| **Tarefa de Usuário "Realizar Cotação"** |
| --- |

Com a cotação feita, lançada e confirmada, ela seguirá para a Aprovação. Nesse faixa de valor, demandará a confirmação de todos os gestores conforme a tabela do caso de uso, ou seja, acima de R$50.000,00 todos precisam aprovar para a solicitação de compras ser concluída.

- **Primeiro usuário:** Carvalho, Coordenador de Suprimentos.

![Imagem 10: Primeiro usuário: Carvalho, Coordenador de Suprimentos .](https://ajuda.sankhya.com.br/hc/article_attachments/4409310977943)

| **Aprovação de Compra** |
| --- |

Após a aprovação da compra, é instanciada uma nova tarefa para o segundo aprovador.

- **Segundo usuário:** Amanda, Gerente Administrativo Financeiro.

![Imagem 11: Segundo usuário: Amanda, Gerente Administrativo Financeiro .](https://ajuda.sankhya.com.br/hc/article_attachments/4409311076887)

| **Aprovação de Compra** |
| --- |

Após a aprovação da compra, é instanciada uma nova tarefa para o terceiro aprovador.

- **Terceiro usuário:** Júlia, Diretor Administrativo Financeiro.

![Imagem 12: Terceiro usuário: Júlia, Diretor Administrativo Financeiro.](https://ajuda.sankhya.com.br/hc/article_attachments/4409311167511)

| **Aprovação de Compra** |
| --- |

Após a aprovação da compra, é instanciada uma nova tarefa para o quarto aprovador.

- **Quarto usuário:** Juliane, Diretor Presidente.

![Imagem 13: Quarto usuário: Juliane, Diretor Presidente.](https://ajuda.sankhya.com.br/hc/article_attachments/4409301274135)

| **Aprovação de Compra** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409305580439-Multiplicidade-Sequencial#top)
