---
id: "7092297445911"
titulo: "Rateios da Folha de Pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7092297445911-Rateios-da-Folha-de-Pagamento"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Eventos e Regras de Cálculo"
atualizado_em: "2026-10-07T15:39:36Z"
rotulos: ["Rateio", "Projeto", "Centro de Resultado", "br.com.sankhya.core.cad.projetos", "Financeiro", "Pessoal", "Folha de Pagamento", "br.com.sankhya.fin.cad.centroResultado", "ID: br.com.sankhya.rh.Rateios", "Estrutura de Rateio na Folha de Pagamento", "FPRATEIOUNICO"]
---

# Rateios da Folha de Pagamento

```
 Módulo: Pessoal + > Cadastros
```

---

Os Centros de Resultados ou Projetos são subdivisões da empresa responsáveis não apenas por custos, mas também por receitas e, consequentemente, por resultados. A gestão focada em Centros de Resultados e Projetos facilita a constatação de desempenho em relação ao alcance de objetivos, pois demonstra as atividades e/ou os segmentos que não estão agregando valor de forma satisfatória à empresa, auxiliando os gestores no processo decisório de resultados ou necessidades de investimento. Além disso, visa subdividir uma empresa apontando quem é o responsável pelo gasto ou pela receita.

É uma definição elaborada no início da implantação do sistema e que não é realizada somente pelo setor de Departamento Pessoal, uma vez que precisa atender a todas as áreas, como o setor contábil, financeiro, pessoal e outros.

Para consultar essa estrutura, acesse a tela [Centros de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado) que está disponível no módulo Configurações da nossa solução.

![Imagem 1: Para consultar essa estrutura, acesse a tela Centros de Resultado que está disponível no módulo Configurações da nossa…](https://ajuda.sankhya.com.br/hc/article_attachments/7092399570455)

Já um Projeto pode ser definido como uma decisão empresarial cujos resultados devem ser apurados separadamente do restante do negócio, de modo a avaliar se aquela iniciativa está gerando os resultados financeiros esperados. É mais uma forma de agrupar ou classificar as receitas e despesas para apuração de resultados, porém não é obrigatória.

Da mesma maneira que os Centros de Resultado, os Projetos também serão definidos, de modo geral, para todas as áreas e eles podem ser consultados na tela [Projetos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109073).

![Imagem 2: Da mesma maneira que os Centros de Resultado , os Projetos também serão definidos, de modo geral, para todas as áreas e…](https://ajuda.sankhya.com.br/hc/article_attachments/7092484356631)

**Observação:** no sistema, os lançamentos atribuídos a determinado Projeto podem ser analisados em conjunto com outras informações possibilitando um controle gerencial completo e abrangente.

---

Vistos os conceitos, as funções e as rotinas responsáveis pelo cadastro e consulta dos Centros de Resultado e Projetos, agora trataremos da estrutura de Rateio na Folha de Pagamento.

No sistema, a estrutura do rateio se dá por uma ordem de prioridade apresentada a seguir:

**(1)** **Prioridade 1 - Rateio de Movimento**

Ao existir um tipo de rateio associado a algum evento registrado na tela Lançamento de Movimento, o sistema irá segui-lo e o restante da folha será rateado conforme ordem de prioridade na configuração.

**(1)** **Prioridade 2 - Rateio de Funcionário**

Caso não haja rateio relacionado em eventos de Movimento e exista lançado por Funcionário, o sistema irá ratear os eventos dos funcionários pelo Centro de Resultado ou Projeto que estiver configurado e a respectiva Natureza.

**(1)** **Prioridade 3 - Rateio no Evento**

Havendo um Centro de Resultado associado em algum evento que esteja no cálculo e não tenha critério de rateio por Movimento ou por Funcionário, esse evento será rateado pelo Centro de Resultado e Natureza ligados a ele e o restante dos eventos seguem a configuração de rateio do Departamento ou da Empresa.

**(1)** **Prioridade 4 - Rateio no Departamento**

Se não existir critério de rateio por Movimento, Funcionário ou Evento, e tenha somente no Departamento, o sistema irá ratear os eventos da folha pelo Centro de Resultado associado ao Departamento do funcionário e respectiva Natureza.

**(1)** **Prioridade 5 - Rateio na Empresa**

Caso não tenha critério de rateio no Movimento, Funcionário, Evento ou Departamento, e tenha somente na Empresa, os eventos da folha serão rateados pelo Centro de Resultado associado a Empresa do funcionário e respectiva Natureza.

---

Agora veremos como é configurado o rateio nas cinco telas citadas acima: Lançamentos de Movimento, Rateios, [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610434), [Departamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610254) e [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293).

### Imagem 3: Lançamento de Movimento Lançamento de Movimento

Na tela de Lançamento de Movimento, o sistema valida primeiramente se haverá uma forma de rateio por **"Funcionário"** ou **"Evento"**, portanto, aqui é possível informar para qual Centro de Resultado e/ou Projeto devem ser transferidos os custos de um determinado evento.

![Imagem 4: Na tela de Lançamento de Movimento , o sistema valida primeiramente se haverá uma forma de rateio por "Funcionário" ou…](https://ajuda.sankhya.com.br/hc/article_attachments/7093013642647)

### Imagem 5: Rateios Rateios

Outra forma de realizar um rateio para funcionário será por meio dessa tela.

![Imagem 6: Outra forma de realizar um rateio para funcionário será por meio dessa tela.](https://ajuda.sankhya.com.br/hc/article_attachments/7093008516375)

Aqui, é possível lançar o rateio por Empresa ou por Departamento. A diferença entre os dois é que, no primeiro, serão apresentados todos os funcionários da empresa, enquanto no segundo pode-se fazer o filtro por departamento.

- **Seleção por empresa**

Primeiramente, clique no card Seleção por empresa, faça o filtro da(s) empresa(s) para as quais deseja fazer o lançamento e acione o botão **"Próximo"**.

![Imagem 7: Primeiramente, clique no card Seleção por empresa , faça o filtro da(s) empresa(s) para as quais deseja fazer o…](https://ajuda.sankhya.com.br/hc/article_attachments/7093084333463)

Em seguida, serão exibidos todos os funcionários ativos. Aqui também é possível visualizar quem possui rateio já registrado e para qual referência. Caso deseje visualizar, editar ou excluir o lançamento, clique no botão **"Cadastrar Rateio"**.

![Imagem 8: Em seguida, serão exibidos todos os funcionários ativos. Aqui também é possível visualizar quem possui rateio já…](https://ajuda.sankhya.com.br/hc/article_attachments/7093105547671)

Ao abrir a tela para o funcionário que já possui registro, será apresentado um gráfico com os percentuais e centro de resultados ali configurados, sendo possível também a visualização em lista. Caso deseje editar ou excluir um rateio lançado, clique no Centro de Resultado para que os botões **"Editar"** e **"Excluir"** sejam habilitados.

Se desejar, também é possível cadastrar um novo rateio para a referência atual. Para isso, acione o botão ![Imagem 9: Se desejar, também é possível cadastrar um novo rateio para a referência atual. Para isso, acione o botão "Adicionar…](https://ajuda.sankhya.com.br/hc/article_attachments/7093141955223) **"Adicionar Rateio"**, preencha as informações e salve o rateio por meio do botão  ![Finalizar](https://ajuda.sankhya.com.br/hc/article_attachments/15496821316631) **"Salvar rateio"**.

![Imagem 11: Se desejar, também é possível cadastrar um novo rateio para a referência atual. Para isso, acione o botão "Adicionar…](https://ajuda.sankhya.com.br/hc/article_attachments/7093211072663)

Se houver a necessidade de inclusão de um rateio para um ou mais funcionários que ainda não possuem essa configuração, retorne à tela principal, selecione o(s) card(s) dos funcionários e clique no botão Cadastrar rateio.

Informe o Centro de Resultado ou Projeto, e o percentual do Rateio, que pode ser inserido manualmente ou arrastando a linha **"% do Rateio"**, clique em **"Incluir novo rateio"** e salve as informações.

![Imagem 12: Informe o Centro de Resultado ou Projeto , e o percentual do Rateio, que pode ser inserido manualmente ou arrastando a…](https://ajuda.sankhya.com.br/hc/article_attachments/7093244289687)

Após a inclusão dos rateios, você poderá visualizá-los em gráfico ou lista e fazer os ajustes necessários.

- **Seleção por departamento**

Acione o card correspondente a Seleção por departamento, filtre a empresa e clique em Próximo. Em seguida, você irá filtrar os departamentos que receberão os lançamentos do rateio e logo após, selecionar os funcionários que estão lotados nos departamentos selecionados. Clique em Cadastrar Rateio.

![Imagem 13: Acione o card correspondente a Seleção por departamento , filtre a empresa e clique em Próximo . Em seguida, você irá…](https://ajuda.sankhya.com.br/hc/article_attachments/7093289317143)

Faça a inclusão dos Centros de Resultados ou Projetos com seus devidos percentuais e ao salvar o rateio, o mesmo estará disponível para ser usado na integração com o financeiro.

| ℹ️**Rateio para um único Centro de Resultado ou Projeto**  Quando o rateio de um funcionário é configurado com um único **Centro de Resultado** ou **Projeto** (100% do rateio concentrado em um só CR), habilite o parâmetro **Permite rateio para único CR/Projeto - FPRATEIOUNICO** na tela **Preferências** (Configurações > Avançado).  Sem esse parâmetro habilitado, o sistema pode não gerar corretamente o rateio por Centro de Resultado nesses casos, e a Integração Financeira pode herdar um Centro de Resultado incorreto para o funcionário.  Esse parâmetro não interfere em rateios com mais de um Centro de Resultado ou Projeto, nesses casos, o sistema já considera o centro de resultado do próprio rateio, como descrito em [Como fazer a integração financeira da folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610374). |
| --- |

### Imagem 14: Eventos Eventos

Outra forma de realizar o lançamento de rateio é por meio da tela [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767), sendo possível definir qual será o **"Centro de Resultado"** que receberá o custo de um determinado evento e no campo **"Natureza para Integração a Financeiro"** será classificado o tipo de gasto ou receita referente ao evento.

![Imagem 15: Outra forma de realizar o lançamento de rateio é por meio da tela Eventos , sendo possível definir qual será o "Centro…](https://ajuda.sankhya.com.br/hc/article_attachments/7093322609431)

### Imagem 16: Departamentos Departamentos

Na tela [Departamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610254) também é possível realizar o rateio da folha de pagamento, sendo essa a quarta prioridade de validação. Caso faça a opção por esta forma de rateio, o Centro de Resultado correspondente deve ser informado no cadastro do departamento.

![Imagem 17: Na tela Departamentos também é possível realizar o rateio da folha de pagamento, sendo essa a quarta prioridade de…](https://ajuda.sankhya.com.br/hc/article_attachments/7093383066391)

### Imagem 18: Empresas Empresas

No cadastro de Empresas é possível identificar qual Centro de Resultado receberá os valores calculados, caso o mesmo não tenha sido identificado nos cadastros anteriormente citados. Nessa tela, selecione a aba [Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas#contabiliza%C3%A7%C3%A3o) e preencha o campo **"Cód. Centro Resultado"**.

![Imagem 19: No cadastro de Empresas é possível identificar qual Centro de Resultado receberá os valores calculados, caso o mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/7093408874647)

---

**Cálculos**

Feitos os lançamentos do rateio e após o cálculo da folha de pagamento, será possível visualizar os rateios lançados.

Para isso faça o cálculo da folha do funcionário individual ou coletivo e a confirmação da folha. Posteriormente, acione o botão ![integrar](https://ajuda.sankhya.com.br/hc/article_attachments/15496821317911) **"Integração Financeira"**. Preenchidas as informações da configuração de integração financeira, como datas de **"Negociação"**, **"Vencimento"**, **"Entrada/Saída"** e **"Histórico"**, clique em **"Confirma Integração"**.

![Imagem 21: Para isso faça o cálculo da folha do funcionário individual ou coletivo e a confirmação da folha. Posteriormente,…](https://ajuda.sankhya.com.br/hc/article_attachments/7093444516247)

Ao confirmar a integração financeira, será apresentado o resumo da mesma e o botão **"Rateios"**, onde poderá visualizar os valores distribuídos por Centros de Resultados.

![Imagem 22: Ao confirmar a integração financeira, será apresentado o resumo da mesma e o botão "Rateios" , onde poderá visualizar…](https://ajuda.sankhya.com.br/hc/article_attachments/7093504483351)

**Importante:** se o cálculo da folha de uma referência estiver confirmada, o sistema não permitirá excluir o rateio dessa referência na tela de Rateios.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7092297445911-Rateios-da-Folha-de-Pagamento#top)
