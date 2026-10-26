---
id: "360045110053"
titulo: "Central de Certificações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:29:45Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Empresa", "WMS", "Contrato", "Controle de Acessos", "Contabilidade", "Central de Certificações", "Limitações", "Permissão", "Proibição", "Regra", "br.com.sankhya.com.avan.cert.centraldecertificacoes", "Central de Certificações manual", "Contabilização", "Financeiro", "CERTIFCASCATA", "USACERTCOMISS", "Configuração de Permissões", "Restrições de Visualização", "SUBSTCONTA substitui se ligado", "Central de Projetos"]
---

# Central de Certificações

```
 Módulo: Comercial > Avançado > Certificações
```

---

Limite lançamentos e visualizações no sistema por meio da configuração de permissões ou proibições na **Central de Certificações**. Para usar esta rotina, você precisa ter o opcional **"Central de Certificação"** liberado.

> **Importante: Restrições de Aplicabilidade**
>
> As regras definidas na Central de Certificações **não são aplicadas** nas seguintes situações:
>
> - **Agendadores:** Processos executados de forma automática via agendamento não sofrem as restrições de permissão ou proibição configuradas nesta rotina.
> - **Venda Assistida:** Esta rotina não possui as permissões/restrições cadastradas na Central de Certificações.
> - **Módulo de Metas/Orçamentário:** As regras não são consideradas neste módulo, incluindo as rotinas de **Transferência Orçamentária** e **Liberação de Limites Orçamentários**. Nessas telas, as instâncias (como Centro de Resultado, Empresa, entre outras) não interferem na visualização ou operação dos dados.

Acesse os links abaixo para entender as funcionalidades da tela:

| Funcionalidades da tela Central de Certificações | |
| --- | --- |
| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#painelprincipal) | [Configuração de Limitação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#configuraodelimitao) |
| [Restrição por empresa no WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#restrioporempresanowms) | [Restrição por empresa na Contabilidade...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#Restri%C3%A7%C3%A3oporempresanaContabilidade) |
| [Restrição por Dashboard](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#restriopordashboard) | [Parâmetros que atuam na Central...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#parmetrosqueatuamnacentraldecertificaes) |

###

### Painel Principal

O campo **"Regra"** pode ser preenchido de forma manual ou automática; esta definição é feita pelo botão ![Imagem 1: O campo "Regra" pode ser preenchido de forma manual ou automática; esta definição é feita pelo botão "Outras Opções..."…](https://ajuda.sankhya.com.br/hc/article_attachments/22045860432023) **"Outras Opções..."**. Indique neste campo, a chave da regra que está sendo criada, ou seja, esta numeração será responsável por identificá-la em todas as rotinas em que ela estiver presente.

![Imagem 2: As regras configuradas se aplicam somente ao campo Centro de resultados na tela de Contratos .](https://ajuda.sankhya.com.br/hc/article_attachments/35817315178519) As regras configuradas se aplicam somente ao campo **Centro de resultados** na tela de [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774).

![Imagem 3: As regras configuradas se aplicam somente ao campo Centro de resultados na tela de Contratos .](https://ajuda.sankhya.com.br/hc/article_attachments/22041292738967)

Informe o nome da regra a ser cadastrada através do campo **"Descrição".**

Informe no campo **"Instância Principal"** a instância central a ser utilizada na regra, ou seja, a tabela principal que será considerada.

No campo **"Instância Secundária"** selecione uma instância para associar com a instância principal. É importante ressaltar que, quando uma regra for configurada com Instância Secundária, não será permitido utilizar a marcação **"Não Visualizar"** presente na aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes) do cadastro do [Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), pois nesse caso, essa regra não irá acatar a configuração da marcação.

Por meio do campo **"Permissão"** realiza-se uma das principais configurações da regra; é o fator determinante para o resultado final, pois traz as opções **"Permitido"** ou **"Proibido"**, ou seja, irá permitir ou proibir a visualização de tal configuração, por exemplo.

Quando a instância estiver dupla, por exemplo, **"Empresa"** e **"Centro de Resultado"**, o sistema filtrará os registros nas grades das telas [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)/[Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953)/[Movimentações Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593), [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) e [Faturamento de Pedidos/OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694), além de outras telas que utilizam a Central de Certificações, com base na marcação Não Visualizar, da aba Validações, da tela Usuários.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#top)

### Configuração de Limitação

As limitações de lançamentos serão configuradas por instâncias, como por exemplo: Centro de Resultado, Conta bancária, Empresa, Grupo de Produto, Local, Natureza, Parceiro, Produto, Projeto e Tipo de Operação - TOP ou pares pré-programados de instâncias, Natureza x Projeto, Natureza x Centro de Resultado entre outros que podem ser associados à Empresa, Usuário, Funcionário ou Vendedor.

Poderão também ser configuradas por regras gerais, que são válidas para o sistema todo através da rotina [Regras Gerais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112893-Regras-Gerais). Assim como, as referidas limitações podem ser configuradas por ordem de sequência, a qual o sistema fará as validações.

Ao efetuar a inserção de uma Nota, Rateio ou Financeiro, o sistema verifica se existe alguma restrição/permissão com o tipo geral, senão existir, irá procurar por outras regras.

A regra é um conjunto de combinações do mesmo par de Instâncias Principal e Secundária. Quando for inserido mais de uma regra de Permissão, com o mesmo par de Instâncias Primária e Secundária, as duas permitindo, as duas negando ou uma permitindo e outra negando, o sistema proibirá tudo devido à combinação matemática. Sendo que as Regras de Instâncias diferentes podem ser de Permissão ou Proibição.

No caso de intervalos, como no exemplo apresentado na tela abaixo, o sistema fará a validação do local começando no 7100 e terminando no 8099, ou seja, qualquer local utilizado neste intervalo também será validado junto com o Centro de resultado 50600.

**Nota:** as validações são feitas nas inserções e nas alterações.

![Imagem 4: Nota: as validações são feitas nas inserções e nas alterações.](https://ajuda.sankhya.com.br/hc/article_attachments/22042158826391)

Quando a regra possui Instância Secundária, pode ser uma Proibição/Permissão apenas para a combinação, por isso não se pode Filtrar regras combinadas.

**Importante:** as regras aqui definidas cuja **"Instância Principal"** seja a Empresa, serão consideradas na geração dos relatórios do sistema; relatório de **"Entradas e Saídas"**, **"Produtos"**, **"Financeiros"** e **"Movimento Bancário"**. Para que isso ocorra, é necessário que na tela [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes), a regra em questão seja informada para o usuário em questão. Considere o exemplo a seguir sobre esta definição:

Ao cadastrar uma regra na Central de Certificações, definiu-se a instância principal como Empresa, o campo **"Permissão"** foi definido com a opção **"Permitido"**; no cadastro do usuário, marcou-se os campos **"Ativo"** e **"Não Visualizar"**. Ao acessar o relatório Entradas e Saídas, serão visualizadas apenas as empresas cadastradas na regra da Central de Certificações inicialmente criada.

Ainda em uma situação cuja Instância Principal seja a **"Empresa"**, suas validações também são consideradas no [Cadastro de Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores). Um segundo exemplo, cadastrando-se uma regra na Central de Certificações, definiu-se a instância principal como Empresa, o campo **"Permissão"** foi definido como **"Proibido"**; no cadastro do usuários, aba Validações, marcou-se o campo **"Ativo"** e desmarcou-se o campo **"Não Visualizar"**. Ao informar o campo **"Empresa"** presente na tela de Cadastro de Vendedores/Compradores, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores#abageral), não será permitido vincular ao vendedor/comprador a empresa cadastrada na regra da Central de Certificações inicialmente criada.

---

![Imagem 5: A partir da versão 4.35:](https://ajuda.sankhya.com.br/hc/article_attachments/31870492456343) **A partir da versão 4.35:**

Quando o parâmetro **"Apl. Reg. Visual. Central de Certificação Inst. Dupla - APCERTINSTDUP"** for ativado, o sistema não aplicará o uso de instâncias duplas nos lançamentos — ou seja, a visibilidade de registros nas telas não será restrita durante a digitação, mas sim validada apenas no momento da gravação do lançamento.

#### Exemplo prático:

Considere a seguinte configuração na Central de Certificações:

- **Centro de Resultado permitido:** Logística
- **Natureza de operação permitida:** Produtos para revenda

Ao acessar o **Portal de Vendas** para lançar uma venda:

- Os campos de pesquisa para **Centro de Resultado** e **Natureza** exibirão **todos os registros disponíveis**, sem filtrar com base nas permissões definidas.
- No entanto, ao tentar **salvar o lançamento**, o sistema fará a verificação:
  - Se algum dos dados informados **não estiver permitido** na configuração da Central de Certificações, o sistema **bloqueará o salvamento** e apresentará uma mensagem de erro.

Além disso, o usuário, ao acessar telas que possuem grade, como, por exemplo, **Portal de Vendas**, **Portal de Compras**, **Portal de Movimentações Internas**, **Liberação de Limites**, entre outras, não verá na grade os dados quando a marcação **“Não Visualizar”** na aba [Validação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes) do Cadastro do [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) estiver habilitada.

---

O sistema observará as regras da Central de Certificações mas seguintes rotinas:

- [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o);
- [Planejamento de Produção (MRP I)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174);
- Apontamentos ([Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274), [Apontamento de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118973), [Apontamento de Produções Conjuntas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118753));
- [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314).

> **Importante:**
> As regras da Central de Certificações **não são consideradas em execuções realizadas por Agendadores**, independentemente das instâncias configuradas.

Lembrando que, nas rotinas acima, serão contempladas as instâncias de Empresa, Parceiro, Produto e Grupo de Produtos, ou seja, com base nas regras, o usuário será permitido ou proibido de acessar, conforme certificação.

**Nota:** quando o sistema é acessado por um usuário sem restrições e a tela Apontamento de Produção é acessada por um usuário com restrições referentes à OP, a OP não será apresentada para o mesmo; porém, quando o sistema é acessado por um usuário com restrições referentes à OP e a tela Apontamento de Produção é acessada por um usuário sem restrições, a OP não será apresentada ao usuário, devido às restrições do usuário que realizou o login no sistema.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#top)

### Restrição por empresa no WMS

Ao realizar as movimentações de **"Recebimento"**, **"Expedição"**, **"Transferência"** entre endereços e **"Inventário"**, as tarefas só poderão ser executas pelo usuário configurado para empresa, na qual estão sendo realizadas as movimentações.

Ao realizar o login no coletor, com um usuário que não tenha permissão na execução da tarefa, o sistema não permitirá a realização desta, e exibirá ao usuário uma mensagem de alerta.

As validações serão executadas de acordo com a Central de Certificações. As atividades e informações das telas serão apresentadas por empresa, de acordo com o usuário que estiver logado e a empresa que estiver configurada para o referido usuário. Tem-se abaixo um exemplo destas validações:

Inicialmente configure o acesso apenas a empresa **"3"**:

![Imagem 6: Inicialmente configure o acesso apenas a empresa "3" :](https://ajuda.sankhya.com.br/hc/article_attachments/22042603376663)

Em seguida, restringe-se a empresa **"40"**:

![Imagem 7: Em seguida, restringe-se a empresa "40" :](https://ajuda.sankhya.com.br/hc/article_attachments/22042647529879)

Na tela Usuários, aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes), insira as regras cadastradas anteriormente:

![Imagem 8: Na tela Usuários , aba Validações , insira as regras cadastradas anteriormente:](https://ajuda.sankhya.com.br/hc/article_attachments/22068908570519)

Ao efetuar as configurações descritas acima, tem-se as validações criadas para as seguintes telas:

- [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento) - Quando logado com um usuário configurado para uma determinada empresa, só será possível visualizar e gerar as tarefas de armazenamento, para as notas lançadas para esta empresa.
- [Geração de Tarefas de Contagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Gera%C3%A7%C3%A3o-de-Tarefas-de-Contagem) - Na geração das tarefas ao vincular um usuário, só serão exibidos os usuário que tiverem permissão para a empresa e os usuários que não tiverem nenhuma validação.

**Observação:** se o seu objetivo for realizar a restrição da empresa 3 para utilização de um usuário, é necessário criar a regra de permissão das empresas 1 e 2, por exemplo. Porém, se a única regra vinculada for de proibir a empresa 3, o sistema entenderá que as demais empresas não possuem vínculo de permissão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#top)

### Restrição por empresa na Contabilidade e Contabilização

Nos módulos Contabilidade e Contabilização, ao criar uma restrição por empresa (assim como feito no exemplo do tópico acima), o sistema irá **"permitir"** ou **"proibir"** a visualização e utilização das empresas para lançamentos, criação ou geração de relatórios.

As empresas as quais o usuário não tiver permissão para visualização não serão apresentadas na tela de seleção de empresa. Considere um exemplo de regra, onde foi feita a configuração de **"proibição"** de visualização à empresa **"3"**.

![Imagem 9: As empresas as quais o usuário não tiver permissão para visualização não serão apresentadas na tela de seleção de…](https://ajuda.sankhya.com.br/hc/article_attachments/22069203403287)

Observe que ao acessar a rotina de [Contabilidade da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa), com o usuário que possui a regra acima a ele vinculada, a empresa **"3"** não é apresentada para configuração:

![Imagem 10: Observe que ao acessar a rotina de Contabilidade da Empresa , com o usuário que possui a regra acima a ele vinculada, a…](https://ajuda.sankhya.com.br/hc/article_attachments/22069376840087)

Na tela de [Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento), quando o usuário possuir vinculada a ele uma regra que proíbe a visualização de determinada empresa, esta não será apresentada na tela de escolha da empresa que terá sua contabilização gerada. Serão apresentadas apenas as empresas as quais ele tenha permissão para visualizar e utilizar. Note que na imagem abaixo, ao procurar por empresa **"3"**, baseada na regra criada na primeira imagem deste tópico (permissão = proibido), também não é apresentada.

![Imagem 11: Na tela de Agendamento , quando o usuário possuir vinculada a ele uma regra que proíbe a visualização de determinada…](https://ajuda.sankhya.com.br/hc/article_attachments/22075280673175)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#top)

### Restrição por Dashboard

De forma semelhante ao que foi elencado nos tópicos acima, na [Construção de um Dashboard](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605574-Construtor-de-Dashboards) será possível levar em consideração as regras pertinentes à Central de Certificações. Ou seja, o sistema irá **"permitir"** ou **"proibir"** a visualização dos dados contidos no dashboard de acordo com a(s) restrição(ões) aqui criadas, sendo estas por Empresa, Tipo de Operação - TOP, Natureza, Centro de Resultado, entre outros.

Para realizar a ativação desta funcionalidade, basta inserir no comentário da query o seguinte trecho **"/CC NOMEDATABELA CC\*/"**. Deste modo, o sistema validará as restrições de cada usuário ao acessar este dashboard. Considere um exemplo básico destes dados:

Na inserção de uma regra para o usuário "João", onde o mesmo não está permitido à visualização das informações relacionadas a uma determinada empresa, quando este acessar um dashboard que demonstre a relação de notas emitidas com a query abaixo, visualizará no dashboard as notas de acordo com a regra em questão:

SELECT EMP.CODEMP, CAB.NUNOTA

FROM

TSIEMP /\*CC TSIEMP CC\*/ EMP

INNER JOIN TGFCAB  /\*CC TGFCAB CC\*/ CAB ON CAB.CODEMP=EMP.CODEMP

WHERE CAB.DTNEG >= XXXX AND CAB.DTNEG<= XXXX

Sendo assim, o sistema irá validar a Central de Certificações na construção do Dashboard. Tem-se abaixo a relação das tabelas que podem ser inseridas no trecho elencado acima:

| VGFFINRAT | TGFCAB | VGFCAB | TGFNAT | TSIEMP |
| --- | --- | --- | --- | --- |
| TGFTOP | TGFMBC | TSICUS | TGFEMP | TGFECF |
| TGFEST | TGFLOC | TCSPRJ | TGFMAQ | TGFOIR |
| TGFLIV | TGFAJA | TGFGUI | TGFIAA | TGMTRA |
| TGFLIT | TGFE340 | TGFE350 | TCSCON | TGFITE |
| TGFCTT | TSICTA | TGFPAR | VGFFIN | TGFPRO |
| TGFMGC | TGFSBC | TGFFIN | TGFGRU |  |
| TGFLOU | TGFLIS | TGMMET | TGFORD |  |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#top)

### Parâmetros que atuam na Central de Certificações

**Priorizar conta informada no faturamento? - PRIORIZACTAFAT:** quando este parâmetro estiver ligado, o sistema irá primeiro validar a conta bancária informada no lançamento e, em seguida, realizará a validação na Central de Certificação, se aplicável.

**Usar regras da Central de Certificação em cascata? - CERTIFCASCATA:** quando na Central de Certificações houver uma restrição para a empresa "x" e esta restrição se encontrar associada ao usuário "Y", o sistema automaticamente permite que este usuário tenha acesso apenas as contas dessa mesma empresa. Nessa situação, o usuário "Y" não conseguirá imprimir um boleto de outra empresa.

Em certos casos, existem usuários que apesar de não conterem acesso a determinadas empresas para lançamentos e movimentações por exemplo, ainda sim precisam imprimir boletos dessas outras empresas. Deste modo, para realizar a referida impressão se faz necessário habilitar este parâmetro. Veja abaixo um exemplo:

Usuário João  -> central de certificação empresa 1

Usuário Maria -> central de certificação empresa 2

- Quando o parâmetro estiver habilitado, João só conseguirá imprimir boletos cuja conta seja da empresa 1 e Maria só conseguirá imprimir boletos que a conta seja da empresa 2;
- Caso esteja desligado, João e Maria conseguirão imprimir boletos tanto da empresa 1 como da empresa 2.

**Usa certific. na tela de comissão por OS Form/Fecha - USACERTCOMISS:** este parâmetro quando habilitado, faz com que as regras de certificações por Centro de Resultados criadas na Central de Certificações, seja proibindo ou permitindo, sejam aplicadas para vendedores e/ou executantes nas telas:

- [Cálculo de Comissão por Fórmula](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603954-C%C3%A1lculo-de-Comiss%C3%A3o-por-F%C3%B3rmula) - No lançamento de nota de venda, cujo vendedor tenha configurado o Centro de Resultado não permitido para visualização para o usuário, a nota não será incluída no Cálculo de Comissão.
- [Cálculo de Comissão por OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604674-C%C3%A1lculo-de-Comiss%C3%A3o-por-OS) - Para o cálculo de comissão por OS, é conferido o Centro de Resultado configurado no usuário Executante da OS. Por exemplo, para um determinado usuário, o sistema irá apresentar as Ordens de Serviço dos executantes cujo Centro de Resultado configurado seja o que lhe é permitido.
- [Fechamento de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034-Fechamento-de-Comiss%C3%A3o) - Possui a mesma condição da tela de Comissão por fórmula, ou seja, irá validar se o Centro de Resultado vinculado ao Vendedor pode ou não ser visto pelo usuário.
- [Comissão de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594894) - Esta tela irá considerar as regras configuradas pela Central de Certificações através do Centro de Resultado do Vendedor.

**Importante:** a regra criada deve ser vinculada ao [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes).

**Substitui Conta do Financeiro com Conta Baixa - SUBSTCONTA:** quando este parâmetro está ligado, a conta informada no campo **"Conta"** no momento da [baixa de títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos#top) substituirá a conta registrada no campo **"Conta Baixa"** localizada no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Principal) da tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). Se o parâmetro estiver desligado, mesmo que uma conta diferente seja informada na baixa de títulos, o sistema manterá a conta registrada originalmente no campo Conta Baixa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es#top)
