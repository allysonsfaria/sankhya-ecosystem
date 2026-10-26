---
id: "360044598774"
titulo: "Natureza de Receitas e Despesas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:11Z"
rotulos: ["manual", "Sintético", "Configuração", "Contas", "Receitas", "Relatórios Gerenciais", "Analítico", "Estrutura", "QTDMAXREGEXPORT", "Cadastro de Natureza", "Contas Contábeis", "Natureza de Receitas e Despesas", "Níveis", "Usado em OS no Portal", "Visualização de Serviços Específicos nos Portais", "br.com.sankhya.core.cad.naturezarecdesp", "Natureza de Receitas e Despesas manual", "Despesas", "Financeiro", "Natureza", "Como criar nova natureza", "Natureza de Receitas e Despesas: Configuração e Utilização"]
---

# Natureza de Receitas e Despesas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310715438359) Módulo: Configurações > Cadastros > Gerencial 
```

---

A classificação dos lançamentos financeiros de uma empresa em uma estrutura de Naturezas é uma forma de agrupar Receitas e Despesas para análise de desempenho e tomada de decisões. Conhecida também como Plano de Contas Gerencial, pois normalmente essas naturezas têm uma ligação direta com as Contas Contábeis e através delas serão feitas as interpretações de desempenho financeiro da empresa.

| [Considerações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#considera%C3%A7%C3%B5esiniciais) |  | [Realizando um novo cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#realizandoumnovocadastro) |
| --- | --- | --- |
| [Orientações para um cadastro eficaz](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#orienta%C3%A7%C3%B5esparaumcadastroeficaz) |  | [Campos para Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#camposparacontabiliza%C3%A7%C3%A3o) |
| [Visualização de serviços específicos nos P...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#visualiza%C3%A7%C3%A3odeservi%C3%A7osespec%C3%ADficosnosportais) |  | [Campos adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#camposadicionais) |
| [Aba PIS/COFINS Todas Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#Abapis/cofinstodasempresas) |  | [Aba Natureza x PIS/COFINS x Em...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#abanaturezapiscofinsempresa) |
| [Ferramentas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#ferramentas) |  | [Parâmetros que influenciam...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#par%C3%A2metrosqueinfluenciamnocadastro...) |
| [Exemplo de aplicabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#exemplodeaplicabilidade) |  |  |

## Considerações Iniciais

Esta é uma das telas do sistema composta por árvore hierárquica; algumas informações sobre esta particularidade, podem ser visualizadas por meio do link [Telas com Hierarquia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600814-Telas-com-Hierarquia).

![Imagem 2: Esta é uma das telas do sistema composta por árvore hierárquica; algumas informações sobre esta particularidade, podem…](https://ajuda.sankhya.com.br/hc/article_attachments/9778762229527)

A definição das naturezas deve ter como objetivos:

- Tornar fácil a classificação dos lançamentos;
- Atender às exigências de informação da gerência;
- Apresentar os resultados de forma clara;
- Dar sentidos aos valores e percentuais apurados;
- Ser operacionalmente viável.

A configuração de **"Naturezas"** é precedida pela definição da máscara ou estrutura dos níveis. Esta será cadastrada na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias). Através do parâmetro **"Máscara para natureza - MASCNATUREZA"** é aplicada uma padronização para a hierarquia dos diferentes níveis de Natureza de Receitas e Despesas. Os níveis são separados por pontos que identificam os **"pais"**, **"filhos"**, **"netos"**, **"bisnetos"**. Já, a máscara padrão é 9\.99\.99\.99;0, sendo obrigatório o uso das barras e do ";0". Lembrando que, esta não pode conter mais de 9 dígitos.

Caso contrário poderá ocasionar erros em todas as rotinas que utilizam Naturezas de Receitas e Despesas.

Exemplo: estruturação em quatro níveis, com um dígito no primeiro nível, dois dígitos no segundo e terceiro níveis e três dígitos no quarto nível: 9\.99\.99\.99;0.

**Nota:** mesmo que a Empresa possua Naturezas cadastradas, este parâmetro sobrescreverá a configuração realizada na tela [Máscara para Natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597174).

O parâmetro **"Máscara para o Centro de Resultados - MASCCENCUS"** influencia na tela de pesquisa do campo **"Centro de Resultado"** da aba "C.R. X Conta Contábil". Com este parâmetro, as informações da tela de pesquisa são apresentadas em forma de hierarquia, seguindo o padrão especificado neste parâmetro. Inicialmente, deve-se definir quantos níveis terá a estrutura e quantos dígitos haverá em cada nível.

Com o parâmetro **"Usar máscara MASCCENCUS na geração do arquivo ECD - CTBUSAMASCCECD"** ligado, o código de centro de custo será apresentado conforme a máscara definida no parâmetro MASCCENCUS, porém sem pontuação, exibindo apenas números.

**Observação:** caso o usuário tenha gerado o ECD do ano anterior sem a máscara (apenas utilizando os números), pode ocorrer erros de validação ao importar o ECD atual, utilizando a função de importação do ECD anterior disponível no PVA.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Realizando um novo cadastro

Ao utilizar o botão ![Imagem 3: Ao utilizar o botão "Novo" e efetuar a inserção de um novo "Cód. Natureza" e sua respectiva "Descrição" para a Natureza.](https://ajuda.sankhya.com.br/hc/article_attachments/16647446176279) **"Novo"** e efetuar a inserção de um novo **"Cód. Natureza"** e sua respectiva **"Descrição"** para a Natureza.

Caso necessário realizar algum tipo de consulta em relação a nomenclatura das Naturezas já cadastradas, à frente do campo Cód. Natureza, ao clicar na lupa para pesquisa de uma Natureza, será aberta a tela para pesquisa em modo hierarquia, onde pode-se alterne sua apresentação para o modo grade através do botão ![Imagem 4: Caso necessário realizar algum tipo de consulta em relação a nomenclatura das Naturezas já cadastradas, à frente do…](https://ajuda.sankhya.com.br/hc/article_attachments/16647446184599) **"Configurar Grade"**; além disso, tanto em modo grade, quanto em modo hierárquico, podemos digitar o início do nome de um cadastro, que ao solicitar a pesquisa, serão apresentados todos os registros que contêm o nome informado, facilitando assim a localização de naturezas já configuradas no sistema.

![Imagem 5: Caso necessário realizar algum tipo de consulta em relação a nomenclatura das Naturezas já cadastradas, à frente do…](https://ajuda.sankhya.com.br/hc/article_attachments/9778968274071)

Se a marcação **"Ativa"** estiver desabilitada, a Natureza não poderá ser visualizada nos demais cadastros do sistema.

Caso você deseje cadastrar uma **"Natureza Sintética"**, deverá desmarcar a opção **"Analítica"**.

**Nota:** as opções Ativa e Analítica virão automaticamente marcadas pelo sistema na inclusão de uma nova Natureza. Nas demais rotinas do sistema apenas serão aceitas as linhas **"Analíticas"**.

Por exemplo: estruturação em quatro níveis, com um dígito no primeiro nível, dois dígitos no segundo e terceiro níveis e três dígitos no quarto nível: 9.99.99.999.

A marcação **"Incide no resultado"** é utilizada como facilitadora na criação de filtros personalizados. Sua ativação não irá influenciar nos valores gerados/exibidos nos Relatórios Gerenciais (Sintético por Natureza, Analítico por Natureza).

O campo **"Serviço Único Faturamento"**, está ligado ao processo de [Agrupamento de Serviços no Faturamento de Contratos e Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599994-Agrupamento-de-Servi%C3%A7os-no-Faturamento-de-Contratos-e-Servi%C3%A7os).

O campo **"Tipo de natureza"** é apresentado quando na árvore hierárquica um registro **"Analítico"** é selecionado. Por meio deste campo, será determinado se a Natureza que está sendo cadastrada será do tipo **"Receita"** ou **"Despesa"**. O tipo definido neste campo, deve estar relacionado ao campo **"Tipo de Natureza"** informado para o Grupo de Naturezas ao qual a natureza em questão pertence. Além disso, a informação inserida neste campo é utilizada na rotina acessada pela tela [Planejamento Orçamentário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609874-Planejamento-Or%C3%A7ament%C3%A1rio).

A marcação **"Gera informações para o Livro Caixa Digital Produtor Rural"** tem o objetivo de determinar quais financeiros irão compor o Livro Caixa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Orientações para um cadastro eficaz

Estas são algumas dicas para obter o máximo retorno dos recursos que o sistema oferece no cadastro de Naturezas.

**1 - Evitar redundâncias**

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

Acesse o link para mais informações referente ao [Cadastro de Centro de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado).

**2 - Evitar misturar os conceitos de "Natureza" e "Grupos de Produtos"**

Este tipo de cadastro dificulta a operacionalização, pois seria necessário fazer um rateio da **"Nota"** para identificar o valor por grupo de produtos da nota. Esta é uma análise facilmente retirada nas análises de venda. Esta classificação somente seria operacionalizável se existisse um **"Tipo de Negociação"** ou **"TOP"** para a venda de cada **"Grupo de Produto"**, o que é absurdo.

```
01 Vendas

 01.01 Cimento

 01.02 Tijolos

 01.03 Areia

 01.04 Brita

 01.05 Telhas
```

**3 - Evitar um grande número de níveis**

Um cadastro com grande número de níveis torna os lançamentos muito complicados e os relatórios gerenciais apresentam muitas quebras, tornando-se difíceis de interpretar.

```
01 Receitas

 01.01 Receitas operacionais

         01.01.01 Receitas de vendas

                 01.01.01.01 Vendas de balcão
```

**4 - Evitar uma estrutura muito simplificada**

Em uma estrutura muito simplificada o resultado pode tornar-se muito "pobre" podendo não atender às necessidades de informação dos gestores da empresa.

```
03 Energia elétrica

04 Telefones

05 Água
```

**5 - Evitar misturar o conceito de Natureza com o conceito de Centro de Resultado**

**Natureza** - Com o quê estou gastando ou recebendo?

**Centro de Resultado** - Quem está gastando ou recebendo?

Exemplo: Ao pagar uma despesa de viagem, a Natureza é o motivo do gasto - Despesa de Viagens. A despesa de viagem deve ser apropriada para um Centro de Resultado, por exemplo, Departamento de Vendas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Campos para Contabilização

**Contas Contábeis:** A vinculação da Natureza com as contas contábeis informadas nestes campos, tornará a contabilização mais simples e eficaz, criando uma ligação das Naturezas com o Plano de Contas (Contabilidade), relacionando as informações gerenciais às análises Contábeis.

Os campos Histórico 1 e Histórico 2 serão utilizados para a contabilização.

**Observação:** se a contabilização utilizar as **"Contas da Natureza"** e não houver **"Histórico"** nem **"Histórico Padrão"** informado, o sistema busca o Histórico correspondente da Natureza que for informada no lançamento. Se contabilizando na **"Conta 1 da Natureza"**, o sistema busca o **"Histórico 1"**; se contabilizando na **"Conta 2 da Natureza"**, o sistema busca o **"Histórico 2"**.

No caso de títulos rateados, se a Contabilização estiver parametrizada para buscar a **"Conta Contábil do Rateio"** e não existir histórico informado, o sistema irá buscar o Histórico 1 da Natureza usada na tela de Rateio.

**Observação:** caso não haja uma conta informada no campo acima, a contabilização será realizada conforme o campo **"Natureza"** do cabeçalho da nota.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Visualização de Serviços específicos nos Portais

O sistema permite filtrar os itens que aparecem nas OS externas, fazendo com que alguns serviços específicos não sejam mostrados no portal da Sankhya.

Para isso, deve-se utilizar a marcação na tela de Natureza de Receitas e Despesas, na aba Serviços Autorizados, chamada **"Usado em OS no Portal"**, que virá marcada por padrão.

Caso o usuário não queira que um serviço específico para aquela natureza não apareça no portal, basta desmarcar esta opção, fazendo com que itens que tenham esse serviço fiquem invisíveis.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Campos adicionais

A tela de cadastro de naturezas de receitas e despesas tem suporte para campos adicionais criados pelo usuário conforme lhe for conveniente. Para maiores informações sobre essa funcionalidade em [Conhecendo o Sankhya-W/Campos Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934-Conhecendo-o-Sankhya-W).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Aba PIS/COFINS Todas Empresas

![Imagem 6: Aba PIS/COFINS Todas Empresas](https://ajuda.sankhya.com.br/hc/article_attachments/4411273453335)

O campo **"Cód. Natureza (PIS/COFINS M410/M810)"** é alimentado com valores que irão compor o arquivo [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674).

Na geração do relatório PIS/COFINS o sistema irá validar se os campos **"Alíquota de PIS"** e **"Alíquota de COFINS"** da aba [Natureza x PIS/COFINS x Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#abanaturezapiscofinsempresa) estão preenchidos e, caso não, os campos **"Alíquota de PIS"** e **"Alíquota de COFINS"** dessa aba que serão verificados.

Nos campos **"Cód. Sit. Tribut. PIS"** e **"Cód. Sit. Tribut. COFINS"** pode-se definir os códigos dos CST's de PIS e COFINS conforme o Manual do EFD Contribuições.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Aba Natureza x PIS/COFINS x Empresa

Esta aba possibilita que você cadastre as informações de PIS/COFINS por Empresa.

![Imagem 7: Esta aba possibilita que você cadastre as informações de PIS/COFINS por Empresa .](https://ajuda.sankhya.com.br/hc/article_attachments/9779359243799)

O campo **"Nro Único"** será gerado automaticamente.

É obrigatório informar a **"Data Início Validade"**; já o campo **"Data Fim Validade"** poderá ficar vazio, a fim de evitar a repetição de cadastros para o próximo período subsequente, caso a empresa permaneça com as mesmas informações de PIS/COFINS.

**Observação:** os períodos não poderão ficar intercalados uns com os outros para a mesma combinação Natureza x Período x Empresa.

Abaixo, temos os comportamentos do sistema na busca das informações de PIS/COFINS para cada natureza:

- O período que está sendo gerado para o EFD, será a referência para procurar o período de validade cadastrado para cada natureza. Exemplo: se estiver gerando o EFD para o período 01/06/2020 a 30/06/2020, ele será encontrado no período de validade cadastrado como 01/01/2020 a 31/12/2020.
- Para cada natureza, primeiro o sistema busca as informações pela chave **"Natureza/Período/Empresa"**; se existir esse cadastro, o sistema utiliza os dados encontrados; caso contrário, utilizará os dados da aba **"PIS/COFINS Todas as empresas"**.

Na geração do relatório PIS/COFINS o sistema irá validar se os campos **"Alíquota de PIS"** e **"Alíquota de COFINS"** dessa aba estão preenchidos e, caso não, os campos **"Alíquota de PIS"** e **"Alíquota de COFINS"** da aba [PIS/COFINS Todas Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#Abapis/cofinstodasempresas) que serão verificados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Ferramentas

Por meio do botão Configurar Grade é possível visualizar a árvore em modo grade e ainda configurar quais colunas estarão visíveis.

O botão ![Imagem 8: O botão "Exportar grade para PDF" possibilitará a impressão dos registros da grade em formato PDF e XLS ou Visualizar…](https://ajuda.sankhya.com.br/hc/article_attachments/16647472503831) **"Exportar grade para PDF"** possibilitará a impressão dos registros da grade em formato PDF e XLS ou Visualizar em Cubo.

**Nota:** por meio da configuração do parâmetro **"Qtd. máx. de reg. para export. de PDF, XLS e Cubo - QTDMAXREGEXPORT"**, tem-se a possibilidade de limitar a quantidade máxima de registros que serão exportados na utilização das funcionalidades **"Exportar como PDF"**, **"Exportar como planilha"** e **"Visualizar em cubo"**. Informe um número inteiro, que representa o limite de registro que serão exportados, por exemplo 50 registros, 100 registros; dependendo da necessidade da empresa/usuário.

Esta tela dispõe ainda do botão para a criação de filtros personalizados. Contudo, os filtros feitos, somente serão aplicados nos registros filhos.

Independente do critério de filtro criado o sistema adicionará um critério com a condição **AND (Perfil.ANALITICO = N)**. Dessa forma o sistema filtrará os registros que satisfaçam o filtro do usuário e também filtrará todos os registros que não são analíticos.

**Botão Outras opções**

No botão**"Outras Opções"**, temos a opção **"Substituir Natureza"**, por meio dela, você poderá realizar a substituição de determinada natureza. Para isso, siga os passos abaixo:

1. Informe a **"Natureza a ser substituída"** e a **"Natureza Nova"**.
2. Caso deseje excluir a natureza substituída, ative a marcação **"Excluir Natureza Substituída"**.
3. Com as configurações efetuadas, acione o botão **"Atualizar"**.

**![Imagem 9: Informações importantes sobre a rotina de Substituição de Natureza:](https://ajuda.sankhya.com.br/hc/article_attachments/29903201158167) Informações importantes sobre a rotina de Substituição de Natureza:**

- O usuário deve conter permissão de acesso para realizar esta rotina (tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), menu **"Configurações > Cadastros > Gerencial > Natureza de Receitas e Despesas"** marcação **"Substituir Natureza"**).
- A funcionalidade de substituição irá atualizar apenas as tabelas que possuem vínculo direto com a tabela da Natureza por meio da chave estrangeira (TGFNAT).
- A rotina de substituição de natureza foi criada para facilitar a troca de cadastros antigos por novos cadastros. Esta rotina só pode ser utilizada no momento da criação do novo cadastro, ou seja, antes da nova natureza ser usada em qualquer lançamento. Se a nova natureza já tiver sido aplicada, a substituição não será possível. Neste caso, recomenda-se inativar o registro que não será mais utilizado, garantindo que ele não seja empregado em novos lançamentos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Exemplo de aplicabilidade

Veja as vantagens da adoção de uma estrutura eficiente de Naturezas:

- Melhoria no acesso às informações, através do acompanhamento das Receitas e Despesas por grupos pré-determinados facilmente visualizados nos relatórios gerenciais. A partir de uma classificação fundamentada e com os dados devidamente registrados e organizados, pode-se obter informações seguras analisando os vários relatórios gerenciais. Relacionando as informações com os Projetos e Centros de Resultados torna-se possível uma visão abrangente de cada particularidade dos negócios da empresa.
- Possibilita a classificação contábil e torna o processo de contabilização mais simples e eficaz, criando uma ligação das Naturezas com o Plano de Contas do Módulo de Contabilidade, relacionando as informações gerenciais às análises Contábeis. Uma das maiores facilidades oferecidas por esta ligação é a redução da estrutura de Contas Contábeis.
- Permite a criação e o acompanhamento de metas orçamentárias, integrando com o Módulo de Controle Orçamentário e Metas do MGE.

Exemplo de Naturezas:

**01** Despesas Gerais (Sintético)

**01.01** Viagens (Sintético)

**01.01.01** Hospedagem (Analítico)

**01.01.02** Alimentação (Analítico)

**01.01.03** Transporte (Analítico)

As contas podem ser Sintéticas, que servem apenas para hierarquizar as naturezas, ou Analíticas que servem para receber lançamentos na Movimentação Financeira e nos Portais.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)

## Parâmetros que influenciam no cadastro de natureza de receitas e despesas

O parâmetro **"Usar relação Natureza X Cta Bancária? - USANATCTA"**, quando habilitado faz com que o sistema gere o **"Nosso Número"** dos boletos pela sequência informada no cadastro da natureza, onde será informada a conta bancária. Caso contrário, o sistema irá gerar o nosso número pela regra básica de cada banco, de acordo com o cadastro da conta bancária informada na tela de geração do arquivo de remessa.

Já o parâmetro **"Usar relação Natureza X Empresa - USANATXEMP"**  influencia na aba de contabilização do cadastro de TOP, no que se refere à apresentação ou não da opção **"Natureza por Empresa"**, na lista da coluna **"Conta contábil"**. Para esta opção aparecer na lista, o **"Tipo de conta"** tem que ser **"Variável"**.

Este parâmetro afeta também a exibição ou não da aba **"Natureza X Empresa"** no cadastro de Natureza. Nesta aba o usuário irá informar a conta contábil e a empresa na qual estará sendo feita a contabilização e ao inserir uma nova linha na contabilização poderá escolher na lista a opção **"Natureza por Empresa"**.

Se este parâmetro estiver habilitado, a Aba **"Natureza X Empresa"** será apresentada uma aba para informar a conta contábil e a empresa na qual será feita a contabilização. Ao inserir uma nova linha na contabilização, pode-se escolher na lista de opções **"Empresa por Natureza"**.

**Importante:** respeitando a seguinte combinação de parâmetros, será apresentada no cadastro de Natureza de Receitas e Despesas, a aba **"Projeto X Conta Contábil"**:

- Usar relação Natureza X Projeto? - USANATPROJ, ativado;
- Usar relação Natureza X Cta Bancária? - USANATCTA, desativado;
- Usar relação Natureza X Empresa - USANATXEMP, desativado.

Através da aba Projeto X Conta Contábil, você poderá vincular uma determinada Natureza a um ou mais Projetos e Contas Contábeis. Esta configuração irá refletir no uso das [TOP's Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o), no que tange a informação do campo Conta contábil, que poderá ser definido com a opção Natureza por Projeto.

Ainda neste contexto, tem-se localizado na aba Projeto X Conta Contábil, a marcação **"Considerar rateio como prioridade?"**. Posto isto, será necessário atentar-se as seguintes informações:

- Por meio da marcação mencionada acima, o usuário poderá utilizar o rateio como critério primário para os lançamentos que se referem à projetos. Entretanto, caso não exista o rateio, o sistema deverá manter o comportamento padrão.
- Ao realizar o cadastro de um projeto, considerando que a marcação Considerar rateio como prioridade? esteja habilitada, e em seguida realizar-se o lançamento de uma nota utilizando o rateio e considerando que a [TOP Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o) (campo **"Cód. Projeto"**) esteja buscando a opção **"R - Rateio"**, tem-se que o sistema utilizará a conta contábil cadastrada no campo **"Conta Reduzida"** (aba Projeto X Conta Contábil), buscando assim, o Projeto Natureza do Rateio.

**Observação:** em outra perspectiva, caso o sistema não localize a conta contábil, este seguirá a rotina já criada, utilizando, portanto, a opção **"Natureza por Projeto"** (tela TOP Contabilização, [Campos a serem configurados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#camposaseremconfigurados), campo **"Conta Contábil"**).

Quando o parâmetro **"Habilita a aba Descrição da Natureza por Parceiro? - UTILABAPARCNAT"** estiver ligado, exibirá a aba **"Descrição da Natureza por Parceiro"**, presente na tela Natureza de Receitas e Despesas.

Se o parâmetro **"Conteúdo a ser enviado na descrição de NFS-e - NFSEOBSITERPS"** estiver com a opção **"Observação - Natureza da nota"** selecionada, e o parâmetro de chave UTILABAPARCNAT habilitado, o sistema verificará se no Cadastro de Naturezas de Receitas e Despesas, aba Descrição da Natureza por Parceiro há alguma Descrição da Natureza para o Parceiro da NFS-e; se houver, o sistema enviará essa descrição para a NFS-e, se não, levará a descrição da natureza.

Quando o parâmetro **"Valida tipo de natureza (Receita / Despesa) na movimentação financeira - VALIDATIPONAT"** for habilitado, será permitido lançar naturezas apenas do Tipo Receita para os títulos de Receitas e naturezas do Tipo Despesa, para aquelas que são Despesas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas#top)
