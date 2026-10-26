---
id: "14971681963031"
titulo: "Natureza de Receitas e Despesas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Tributação da folha"
atualizado_em: "2026-09-25T18:16:39Z"
rotulos: ["Configuração", "Contas", "Centro de Resultado", "Relatórios Gerenciais", "USANATCTA", "USANATXEMP", "QTDMAXREGEXPORT", "Financeiro", "ID: br.com.sankhya.rh.Natureza", "MASCNATUREZA", "MASCCENCUS", "UTILABAPARCNAT", "Cadastro e Gestão de Naturezas de Receitas e Despesas"]
---

# Natureza de Receitas e Despesas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42315095353879) Módulo: Pessoal + > Cadastros
```

---

A classificação dos lançamentos financeiros de uma empresa em uma estrutura de Naturezas é uma forma de agrupar Receitas e Despesas para análise de desempenho e tomada de decisões. Conhecida também como Plano de Contas Gerencial, pois normalmente essas naturezas têm uma ligação direta com as Contas Contábeis e através delas serão feitas as interpretações de desempenho financeiro da empresa.

As contas podem ser Sintéticas, que servem apenas para hierarquizar as naturezas, ou Analíticas, que servem para receber lançamentos na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) e nos Portais.

Navegue nos links abaixo para conhecer as funcionalidades dessa tela:

| Funcionalidades da tela | |
| --- | --- |
| [Considerações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#considera%C3%A7%C3%B5esiniciais) | [Orientações para um cadastro eficaz](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#orienta%C3%A7%C3%B5esparaumcadastroeficaz) |
| [Realizando um novo cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#realizandoumnovocadastro) | [Visualização serviços específicos nos Portais](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#visualiza%C3%A7%C3%A3odeservi%C3%A7osespec%C3%ADficosnosportais) |
| [Campos adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#camposadicionais) | [Ferramentas](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#ferramentas) |
| [Parâmetros influentes no cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#par%C3%A2metrosqueinfluenciamnocadastro...) |  |

---

### Considerações Iniciais

Esta é uma das telas do sistema composta por árvore hierárquica; algumas informações sobre esta particularidade podem ser visualizadas por meio do link [Telas com Hierarquia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600814-Telas-com-Hierarquia).

![Imagem 2: Esta é uma das telas do sistema composta por árvore hierárquica; algumas informações sobre esta particularidade podem…](https://ajuda.sankhya.com.br/hc/article_attachments/15471168755735)

A definição das Naturezas deve ter como objetivos:

- Tornar fácil a classificação dos lançamentos;
- Atender às exigências de informação da gerência;
- Apresentar os resultados de forma clara;
- Dar sentidos aos valores e percentuais apurados;
- Ser operacionalmente viável.

A configuração de Naturezas é precedida pela definição da máscara ou estrutura dos níveis. Esta será cadastrada na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).

Através do parâmetro **"Máscara para natureza - MASCNATUREZA"** é aplicada uma padronização para a hierarquia dos diferentes níveis de Natureza de Receitas e Despesas. Os níveis são separados por pontos que identificam os **"pais"**, **"filhos"**, **"netos"** e **"bisnetos"**. Já, a máscara padrão é 9\.99\.99\.99;0, sendo obrigatório o uso das barras e do ";0". Lembrando que, esta não pode conter mais de 9 dígitos.

Caso contrário poderá ocasionar erros em todas as rotinas que utilizam Naturezas de Receitas e Despesas.

Exemplo: estruturação em quatro níveis, com um dígito no primeiro nível, dois dígitos no segundo e terceiro níveis e três dígitos no quarto nível: 9\.99\.99\.99;0.

**Nota:** mesmo que a Empresa possua Naturezas cadastradas, este parâmetro sobrescreverá a configuração realizada na tela [Máscara para Natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597174).

O parâmetro **"Máscara para o Centro de Resultados - MASCCENCUS"** influencia na tela de pesquisa do campo **"Cód. Centro Resultado"** da aba C.R. X Conta Contábil. Com este parâmetro, as informações da tela de pesquisa são apresentadas em forma de hierarquia, seguindo o padrão especificado neste parâmetro. Inicialmente, deve-se definir quantos níveis terá a estrutura e quantos dígitos haverá em cada nível.

Com o parâmetro **"Usar máscara MASCCENCUS na geração do arquivo ECD - CTBUSAMASCCECD"** ligado, ele impactará na apresentação do código de centro de custo, aplicando a máscara definida no parâmetro MASCCENCUS, porém sem pontuação, exibindo apenas números.

**Observação:** caso o usuário tenha gerado o ECD do ano anterior sem a máscara (apenas utilizando os números), pode ocorrer erros de validação ao importar o ECD atual, utilizando a função de importação do ECD anterior disponível no PVA.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#top)

### Orientações para um cadastro eficaz

Estas são algumas dicas para obter o máximo retorno dos recursos que o sistema oferece no cadastro de Naturezas.

#### ![Imagem 3: Evitar redundâncias](https://ajuda.sankhya.com.br/hc/article_attachments/42315105738391) Evitar redundâncias

Exemplo:

```
01 Departamento Financeiro (Sintético)
 01.01 Salários e encargos (Analítico)
 01.02 Energia elétrica (Analítico)
 01.03 Telefone (Analítico)

02 Departamento Comercial (Sintético)
 02.01 Salários e encargos (Analítico)
 02.02 Energia elétrica (Analítico)
 02.03 Telefone (Analítico)
```

Neste tipo de cadastro somente estarão visíveis para o Lançamento as Naturezas Analíticas, assim, haverá uma redundância de cadastros, dificultando o lançamento e organização das informações. O melhor a fazer é cadastrar da seguinte forma:

```
Natureza

01 Despesas Gerais (Sintético)
 01.01 Salários e encargos (Analítico)
 01.02 Energia elétrica (Analítico)
 01.03 Telefone (Analítico)

Centro de Resultado

01 Departamento Financeiro (Analítico)
02 Departamento Comercial (Analítico)
```

No lançamento do título ou da classificação do mesmo, a Natureza e o Centro de Resultado serão informados, possibilitando a análise de gastos por departamento.

#### ![Imagem 4: Evitar misturar os conceitos de "Natureza" e "Grupos de Produtos"](https://ajuda.sankhya.com.br/hc/article_attachments/42315095359511) Evitar misturar os conceitos de "Natureza" e "Grupos de Produtos"

Este tipo de cadastro dificulta a operacionalização, pois seria necessário fazer um rateio da Nota para identificar o valor por grupo de produtos da nota. Esta é uma análise facilmente retirada nas análises de venda. Esta classificação somente seria operacionalizável se existisse um [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) ou [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) para a venda de cada Grupo de Produto, o que é inviável.

```
01 Vendas
 01.01 Cimento
 01.02 Tijolos
 01.03 Areia
 01.04 Brita
 01.05 Telhas
```

#### ![Imagem 5: Evitar um grande número de níveis](https://ajuda.sankhya.com.br/hc/article_attachments/42315095361175) Evitar um grande número de níveis

Um cadastro com grande número de níveis torna os lançamentos muito complicados e os relatórios gerenciais apresentam muitas quebras, tornando-se difíceis de interpretar.

```
01 Receitas
 01.01 Receitas operacionais
         01.01.01 Receitas de vendas
                 01.01.01.01 Vendas de balcão
```

#### ![Imagem 6: Evitar uma estrutura muito simplificada](https://ajuda.sankhya.com.br/hc/article_attachments/42315095363223) Evitar uma estrutura muito simplificada

Em uma estrutura muito simplificada o resultado pode tornar-se muito simples podendo não atender às necessidades de informação dos gestores da empresa.

```
03 Energia elétrica
04 Telefones
05 Água
```

#### ![Imagem 7: Evitar misturar o conceito de Natureza com o conceito de Centro de Resultado](https://ajuda.sankhya.com.br/hc/article_attachments/42315095365527) Evitar misturar o conceito de Natureza com o conceito de Centro de Resultado

**Natureza** - Com o quê estou gastando ou recebendo?

**Centro de Resultado** - Quem está gastando ou recebendo?

Exemplo: ao pagar uma despesa de viagem, a Natureza é o motivo do gasto - Despesa de Viagens. A despesa de viagem deve ser apropriada para um Centro de Resultado, por exemplo, Departamento de Vendas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#top)

### Realizando um novo cadastro

Acione o botão ![Imagem 8: Acione o botão "Cadastrar Natureza" e preencha os campos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16591955231639) **"Cadastrar Natureza"** e preencha os campos abaixo:

| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#PainelPrincipal) | [Aba PIS/COFINS Todas Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#AbaPIS/COFINSTodasEmpresas) |
| --- | --- |
| [Aba Descrição da Natureza por Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#AbaDescri%C3%A7%C3%A3odaNaturezaporParceiro) | [Aba Projeto x Conta Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#AbaProjetoxContaCont%C3%A1bil) |
| [Aba Natureza x PIS/COFINS x Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#AbaNaturezaxPIS/COFINSxEmpresa) |  |

---

#### Painel Principal

Insira um novo **"Cód. Natureza"** e sua respectiva **"Descrição"**.

Caso necessário realizar algum tipo de consulta em relação a nomenclatura das Naturezas já cadastradas, à frente do campo Cód. Natureza, ao clicar na lupa para pesquisa de uma Natureza será aberta a tela para pesquisa em modo hierarquia, onde pode-se alternar sua apresentação para o modo grade através do botão ![Imagem 9: Caso necessário realizar algum tipo de consulta em relação a nomenclatura das Naturezas já cadastradas, à frente do…](https://ajuda.sankhya.com.br/hc/article_attachments/20592908286999) **"Configurar Grade"**; além disso, tanto em modo grade, quanto em modo hierárquico, pode-se digitar o início do nome de um cadastro, que ao solicitar a pesquisa serão apresentados todos os registros que contêm o nome informado, facilitando assim a localização de naturezas já configuradas no sistema.

![Imagem 10: Caso necessário realizar algum tipo de consulta em relação a nomenclatura das Naturezas já cadastradas, à frente do…](https://ajuda.sankhya.com.br/hc/article_attachments/14973132811927)

Habilite a marcação **"Ativa"** para que a Natureza possa ser visualizada nos demais cadastros do sistema.

Caso deseje cadastrar uma Natureza Sintética deverá efetuar a marcação **"Analítica"**.

A marcação **"Incide no resultado"** é utilizada como facilitadora na criação de filtros personalizados. Sua ativação não irá influenciar nos valores gerados/exibidos nos Relatórios Gerenciais (Sintético por Natureza, Analítico por Natureza).

Os campos **"Conta contábil"** e **"Conta contábil 2"** tornarão a contabilização mais simples e eficaz, criando uma ligação das Naturezas com o [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054) relacionando as informações gerenciais às análises Contábeis.

Os campos **"Cód. Histórico 1"** e **"Cód. Histórico 2"** serão utilizados para a contabilização.

**Observação:** se a contabilização utilizar as Contas da Natureza e não houver **"Histórico"** nem **"Histórico Padrão"** informado, o sistema busca o Cód. Histórico correspondente a Natureza que for informada no lançamento. Se contabilizando na Conta 1 da Natureza, o sistema busca o Cód. Histórico 1; se contabilizando na Conta 2 da Natureza, o sistema busca o Cód. Histórico 2.

No caso de títulos rateados, se a Contabilização estiver parametrizada para buscar a **"Conta Contábil do Rateio"** e não existir histórico informado, o sistema irá buscar o Cód. Histórico 1 da Natureza usada na tela de [Rateio dos custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113793).

O campo **"Serviço único faturamento"** está ligado ao processo de [Agrupamento de Serviços no Faturamento de Contratos e Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599994-Agrupamento-de-Servi%C3%A7os-no-Faturamento-de-Contratos-e-Servi%C3%A7os).

O campo **"Tipo de natureza"** é apresentado quando na árvore hierárquica um registro Analítico é selecionado. Por meio deste campo será determinado se a Natureza que está sendo cadastrada será do tipo **"Receita"** ou **"Despesa"** que, deve estar relacionado ao campo **"Tipo de Natureza"** informado para o [Grupo de Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598514) ao qual a Natureza em questão pertence. Além disso, a informação inserida nesse campo é utilizada na rotina acessada pela tela [Planejamento Orçamentário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio).

As marcações **"Gera informações para o Livro Caixa Digital Produtor Rural"** e **"Receita de Adiantamentos para o Livro Caixa Digital Produtor Rural"** tem o objetivo de determinar quais financeiros irão compor o Livro Caixa.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#realizandoumnovocadastro)

#### Aba PIS/COFINS Todas Empresas

![Imagem 11: Aba PIS/COFINS Todas Empresas](https://ajuda.sankhya.com.br/hc/article_attachments/28134560537367)

Os campos **"Cód. Sit. Tribut. PIS"** e **"Cód. Sit. Tribut. COFINS"** determinarão o código da situação tributária de PIS  e COFINS.

Os campos **"Conta Contábil para EFD"** e **"Cód. Natureza (PIS/COFINS M410/M810)"** serão preenchidos com valores que irão compor o arquivo [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674).

A **"Natureza da Base de Cálculo do Crédito de PIS/COFINS"** e o **"Regime (EFD PIS/COFINS)"** também serão apresentados conforme a definição das [Preferências da Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893).

Na geração do relatório PIS/COFINS, o sistema irá validar se os campos **"Alíquota de PIS"** e **"Alíquota de COFINS"** da aba [Natureza x PIS/COFINS x Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#abanaturezapiscofinsempresa) estão preenchidos e, caso não, os campos **"Alíquota de PIS"** e **"Alíquota de COFINS"** dessa aba que serão verificados.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#realizandoumnovocadastro)

#### Aba Descrição da Natureza por Parceiro

Esta aba será visualizada quando o parâmetro **"Habilita a aba Descrição da Natureza por Parceiro? - UTILABAPARCNAT"** estiver habilitado.

![Imagem 12: Esta aba será visualizada quando o parâmetro " Habilita a aba Descrição da Natureza por Parceiro? - UTILABAPARCNAT"…](https://ajuda.sankhya.com.br/hc/article_attachments/24135678931991)

Informe o **"Código do Parceiro"** e a **"Descrição da Natureza"** que deseja vincular ao Parceiro da NFS-e.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#realizandoumnovocadastro)

#### Aba Projeto x Conta Contábil

Esta aba será apresentada respeitando a combinação dos parâmetros abaixo:

- Usar relação Natureza X Projeto? - USANATPROJ: ativado;
- Usar relação Natureza X Cta Bancária? - USANATCTA: desativado.

Através dessa aba, pode-se vincular uma determinada Natureza a um ou mais Projetos e Contas Contábeis. Esta configuração irá refletir no uso das [TOP Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o), no que tange a informação do campo Conta contábil, que poderá ser definido com a opção Natureza por Projeto.

![Imagem 13: Através dessa aba, pode-se vincular uma determinada Natureza a um ou mais Projetos e Contas Contábeis . Esta…](https://ajuda.sankhya.com.br/hc/article_attachments/24136491343127)

Por meio da marcação **"Considerar rateio como prioridade?"** pode-se utilizar o rateio como critério primário para os lançamentos que se referem à projetos. Entretanto, caso não exista o rateio, o sistema manterá o comportamento padrão.

Ao realizar o cadastro de um Projeto, considerando que a marcação Considerar rateio como prioridade? esteja habilitada, e em seguida realizar o lançamento de uma nota utilizando o rateio e considerando que o campo **"Cód. Projeto"** esteja buscando a opção **"R - Rateio"**, tem-se que o sistema utilizará a conta contábil cadastrada no campo **"Conta Reduzida"** buscando assim, o Projeto Natureza do Rateio.

**Observação:** em outra perspectiva, caso o sistema não localize a conta contábil, este seguirá a rotina já criada, utilizando, portanto, a opção **"Natureza por Projeto"** (tela TOP Contabilização, [Campos a serem configurados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#camposaseremconfigurados), campo **"Conta Contábil"**).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#realizandoumnovocadastro)

#### Aba Natureza x PIS/COFINS x Empresa

Esta aba possibilita o cadastro das informações de PIS/COFINS por Empresa.

![Imagem 14: Esta aba possibilita o cadastro das informações de PIS/COFINS por Empresa .](https://ajuda.sankhya.com.br/hc/article_attachments/15471168762903)

O campo **"Nro Único"** será gerado automaticamente.

É obrigatório informar a **"Data Início Validade"**; já o campo **"Data Fim Validade"** poderá ficar vazio, a fim de evitar a repetição de cadastros para o próximo período subsequente, caso a empresa permaneça com as mesmas informações de PIS/COFINS.

**Observação:** os períodos não poderão ficar intercalados uns com os outros para a mesma combinação Natureza x Período x Empresa.

**Importante:** considere os comportamentos do sistema na busca das informações de PIS/COFINS para cada Natureza:

- O período que está sendo gerado para o EFD será a referência para procurar o período de validade cadastrado para cada natureza. Exemplo: se estiver gerando o EFD para o período 01/06/2020 a 30/06/2020, ele será encontrado no período de validade cadastrado como 01/01/2020 a 31/12/2020.
- Para cada natureza, primeiro o sistema busca as informações pela chave **"Natureza/Período/Empresa"**; se existir esse cadastro, o sistema utiliza os dados encontrados; caso contrário, utilizará os dados da aba PIS/COFINS Todas as empresas.

Na geração do relatório PIS/COFINS, o sistema irá validar se os campos **"Alíquota de PIS"** e **"Alíquota de COFINS"** dessa aba estão preenchidos e, caso não, os campos **"Alíquota de PIS"** e **"Alíquota de COFINS"** da aba PIS/COFINS Todas Empresas que serão verificados. 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#realizandoumnovocadastro) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#top)

### Visualização de Serviços específicos nos Portais

O sistema permite filtrar os itens que aparecem nas OS externas, fazendo com que alguns serviços específicos não sejam mostrados no portal da Sankhya.

Para isso, deve-se utilizar a marcação da aba Serviços Autorizados, chamada **"Usado em OS no portal"**, que virá marcada por padrão.

Caso não queira que um serviço específico para aquela natureza não apareça no portal, basta desativar essa marcação, fazendo com que itens que tenham esse serviço fiquem invisíveis.  

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#top)

### Campos adicionais

Essa tela tem suporte para campos adicionais criados pelo usuário conforme lhe for conveniente. Para maiores informações sobre essa funcionalidade acesse o link: [Conhecendo o Sankhya-Om - Dicas e Facilitadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#top)

### Ferramentas

Por meio do botão Configurar Grade é possível visualizar a árvore em modo grade e ainda configurar quais colunas estarão visíveis.

O botão ![Imagem 15: O botão "Exportar grade para PDF" possibilitará a impressão dos registros da grade em formato PDF e XLS ou Visualizar…](https://ajuda.sankhya.com.br/hc/article_attachments/20592982521751) **"Exportar grade para PDF"** possibilitará a impressão dos registros da grade em formato PDF e XLS ou Visualizar em Cubo.

**Nota:** por meio da configuração do parâmetro **"Qtd. máx. de reg. para export. de PDF, XLS e Cubo - QTDMAXREGEXPORT"**, tem-se a possibilidade de limitar a quantidade máxima de registros que serão exportados na utilização das funcionalidades **"Exportar como PDF"**, **"Exportar como planilha"** e **"Visualizar em cubo"**. Informe um número inteiro, que representa o limite de registro que serão exportados, por exemplo 50 registros, 100 registros; dependendo da necessidade da empresa/usuário.

Esta tela dispõe ainda do botão para a criação de filtros personalizados. Contudo, os filtros feitos, somente serão aplicados nos registros filhos.

**Importante:** independente do critério de filtro criado o sistema adicionará um critério com a condição **AND (Perfil.ANALITICO = N)**. Dessa forma o sistema filtrará os registros que satisfaçam o filtro do usuário e também filtrará todos os registros que não são analíticos.

Por meio da opção **"Substituir Natureza"**, poderá realizar a substituição de determinada natureza. Para isso, informe a **"Natureza a ser substituída"** e a **"Natureza Nova"**. Caso deseje excluir a natureza substituída, ative a marcação **"Excluir Natureza Substituída"**. Com as configurações efetuadas, acione o botão **"Atualizar"**.

**Observação:** o usuário deve conter permissão de acesso para realizar esta rotina (tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), menu **"Configurações > Cadastros > Gerencial > Natureza de Receitas e Despesas"** marcação **"Substituir Natureza"**).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#top)

### Parâmetros que influenciam no cadastro

**Usar relação Natureza X Cta Bancária? - USANATCTA**: quando habilitado faz com que o sistema gere o **"Nosso Número"** dos boletos pela sequência informada no cadastro da Natureza, onde será informada a conta bancária. Caso contrário, o sistema irá gerar o Nosso Número pela regra básica de cada banco, de acordo com o cadastro da conta bancária informada na tela [Geração do Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/6145491647383).

**Usar relação Natureza X Empresa - USANATXEMP**: este parâmetro influencia na aba [Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#contasflexveisnacontabilizao) do cadastro da [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174), no que se refere à apresentação ou não da opção **"Natureza por Empresa"** na lista da coluna **"Conta contábil"**. Para esta opção aparecer na lista, o **"Tipo de conta"** tem que ser **"Variável"**.

Se este parâmetro estiver habilitado, a aba Natureza X Empresa será apresentada uma aba para informar a conta contábil e a empresa na qual será feita a contabilização. Ao inserir uma nova linha na contabilização, pode-se escolher na lista de opções **"Empresa por Natureza"**.

**Conteúdo a ser enviado na descrição de NFS-e - NFSEOBSITERPS**: quando este estiver com a opção **"Observação - Natureza da nota"** selecionada, e o parâmetro UTILABAPARCNAT habilitado, o sistema verificará se no cadastro de Naturezas de Receitas e Despesas, aba Descrição da Natureza por Parceiro há alguma Descrição da Natureza para o Parceiro da NFS-e; se houver, o sistema enviará essa descrição para a NFS-e, se não, levará a descrição da natureza.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14971681963031-Natureza-de-Receitas-e-Despesas#top)
