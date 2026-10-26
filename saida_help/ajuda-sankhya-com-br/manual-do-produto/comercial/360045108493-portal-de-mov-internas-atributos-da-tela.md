---
id: "360045108493"
titulo: "Portal de Mov. Internas - Atributos da Tela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:28:22Z"
rotulos: ["Configuração", "Portal de Mov. Internas - Atributos da Tela manual", "WMS", "Requisições", "Parceiro", "Portal de Vendas", "TOP", "TEMMILHARNTDEC", "br.com.sankhya.mgecom.mov.PortalMovInternas", "Portal de Movimentação Interna", "Explorando o Portal de Movimentação Interna"]
---

# Portal de Mov. Internas - Atributos da Tela

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311988354839) Módulo: Comercial > Consulta
```

---

Aqui, analisaremos as particularidades que constituem a tela [Portal de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593); seus campos com seus respectivos preenchimentos, os botões e as situações que estes podem e/ou devem ser acionados.

**Observação:** O parâmetro **"Utilizar novo layout para portais - USANOVOSPORTAIS"** quando ativado, fará com que os Portais de [Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras), [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) ou [Movimentação Interna](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas) sejam carregados em novos layouts; remos-se a geração dos dados na tela de acordo com Tipo de movimento escolhido. Com o parâmetro desativado, os portais serão exibidos em seu layout habitual.

**Importante:** A partir da versão **3.24** do Sankhya-OM, a funcionalidade gerada pela ativação do parâmetro USANOVOSPORTAIS será um padrão no sistema, ou seja, mesmo que este se encontre desativado, os portais serão apresentados em novos layouts e não será possível utilizá-los na versão antiga.

| [Tipo de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#tipodemovimento) |  | [Filtro Personalizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#filtropersonalizado) |
| --- | --- | --- |
| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#filtros) |  | [Status Documentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#h_01EDSFWJDAET3GVJQ3GPJ8BQQ0) |
| [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#itens) |  | [Liberações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#liberaes) |
| [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#parceiros) |  | [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#wms) |
| [Grade - Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#grade-resultadodaseleo) |  | [Grade - Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#grade-itens) |
| [Painel de acesso rápido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#paineldeacessorpido) |  |  |

## Tipo de Movimento

![Imagem 2: Tipo de Movimento](https://ajuda.sankhya.com.br/hc/article_attachments/5922552922263)

Quando você acessa o Portal de Mov. Internas, a ação inicial a ser executada é a definição do **"Tipo de Movimento"** a ser trabalhado, sendo que você poderá escolher uma dentre as seguintes opções:

- [Pedido de Requisição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas#oqueumpedidoderequisio);
- [Requisição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas#oqueumarequisio);
- [Devolução de Requisição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas#oqueumadevoluoderequisio);
- [Transferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas#oqueumatransferncia);
- [Canceladas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas#oquecancelarumanotafiscal);
- Todos (exceto canceladas).

![Imagem 3: Embora o sistema permita duplicar um Tipo de Movimento do tipo Transferência para um de Venda , essa prática não é…](https://ajuda.sankhya.com.br/hc/article_attachments/33295813387031) Embora o sistema permita duplicar um **Tipo de Movimento** do tipo **Transferência** para um de **Venda**, essa prática não é recomendada diretamente, pois existem diferenças entre os tipos.

Nos movimentos de **Compra**, **Venda** ou **Devolução**, há campos obrigatórios que normalmente não são exigidos em uma **Transferência** ou **Requisição**. Por isso, ao duplicar, será necessário preencher manualmente todos os campos obrigatórios exigidos para o novo tipo de movimento, garantindo a integridade das informações.

Sempre que possível, recomendamos duplicar registros dentro do mesmo Tipo de Movimento, para evitar inconsistências ou retrabalho.

O botão ![Imagem 4: O botão localizado à frente da caixa de seleção de tipos de movimento, é denominado "Filtrar Top(s)" ; através dele,…](https://ajuda.sankhya.com.br/hc/article_attachments/5922622850839) localizado à frente da caixa de seleção de tipos de movimento, é denominado **"Filtrar Top(s)"**; através dele, você pode selecionar o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) desejado, de acordo com o tipo de movimento definido, por exemplo, sendo escolhido o tipo de movimento Requisição, serão exibidas para escolha, as TOP's cadastradas correspondentes ao tipo de movimento Requisição.

**Observação:** Quando o Tipo de Movimento estiver filtrando as Notas Canceladas, o Sankhya Om aplicará as regras por Empresa cadastradas na [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es) e vinculadas aos usuários ([Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes)), de forma a não permitir que estes visualizem informações da Empresa que foi associada à regra (campo **"Permissão"** = **"Proibido"**) ou visualize apenas desta Empresa (campo Permissão = **"Permitido"**).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Filtro Personalizado

![Imagem 5: Filtro Personalizado](https://ajuda.sankhya.com.br/hc/article_attachments/5922619200407)

A seção **"Filtro Personalizado"** é destinada à construção de filtros específicos de cada processo e/ou usuário.

O acionamento do botão ![Imagem 6: O acionamento do botão abre o pop-up "Assistente para a Criação de Filtros" ; por meio dele, é possível:](https://ajuda.sankhya.com.br/hc/article_attachments/5922654730775) abre o pop-up **"Assistente para a Criação de Filtros"**; por meio dele, é possível:

- **Criar um novo filtro;**
- **Editar um filtro existente;**
- **Deletar filtros existentes;**
- **Editar filtro padrão** **-** o filtro padrão é aplicado a todos que utilizam o sistema e somente o usuário SUP pode alterá-lo.

Uma vez um filtro criado e selecionado para uso, o botão ![Imagem 7: Uma vez um filtro criado e selecionado para uso, o botão que abre o Assistente para a criação de filtros, assume a…](https://ajuda.sankhya.com.br/hc/article_attachments/5922693538455) que abre o Assistente para a criação de filtros, assume a coloração vermelha, o que facilita a percepção de que existem filtros personalizados que foram elaborados e encontram-se ativos.

Quando você aciona o botão**"Limpar filtros"**, fará com que a seção **"Filtro Personalizado"** retorne para o estado inicial **"Sem filtro"**.

Já o botão **"Aplicar"** faz a junção de todos os filtros criados (personalizados ou não) e apresenta os resultados correspondentes na grade [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#grade-resultadodaseleo).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Filtros

![Imagem 8: Filtros](https://ajuda.sankhya.com.br/hc/article_attachments/5922722363543)

No quadrante **"Filtros"** temos os campos que irão auxiliar na localização de pedidos, notas etc, de maneira direcionada, rápida e singular.

Inicialmente, é possível que você determine a apresentação dos documentos considerando o período em que estes foram negociados ou movimentados, através dos campos **"Data da negociação"** ou **"Data do movimento"**, respectivamente. Além da possibilidade de configuração manual, estas duas datas podem ter sua definição previamente estabelecida por meio do botão **"Outras Opções..."**, opção [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601194-Portal-de-Mov-Internas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#preferncias).

Ao selecionar o Tipo de Movimento **"Canceladas"**, será possível trabalhar com o **"Período de Cancelamento"** das notas.

O **"Número do documento"** se refere ao número do pedido, nota etc; você poderá buscar por apenas um documento, informando o mesmo número em ambos os espaços, ou pesquisar por lançamentos efetuados dentro de um determinado intervalo de numerações.

Na tentativa de localizar apenas um documento, faça através do **"Número único"** da nota; esta é uma numeração gerada interna e exclusivamente para cada documento no sistema.

É possível filtrar os documentos desejados, informando aquele que gerou a nota e/ou aquele para o qual a nota foi gerada, ou seja, **"Empresa"** e **"Parceiro"**, respectivamente.

Caso sua empresa trabalhe com **"Ordem de Carga"**, você também poderá localizar os documentos que a compõem, informando sua devida numeração.

Visando refinar ainda mais a busca, a marcação **"Somente com carta de correção"** quando realizada, exibe com base também nos demais filtros, os documentos que possuem carta de correção a eles vinculada.

O quadrante **"Filtros"** conta com a marcação **"Notas com diferença na geração do Livro"** que leva em consideração o que é realizado na [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953), ou seja, as notas que apresentarem alguma divergência quanto a base de ICMS/IPI na execução da referida rotina, serão apresentadas na grade [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#grade-resultadodaseleo), com base também nos demais filtros.

Por fim, temos o **"Status conferência"** que está interligado às rotinas de [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073) e [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074); neste, são disponibilizadas as seguintes opções:

- Todos;
- Aguardando conferência;
- Em andamento;
- Finalizada divergente;
- Finalizada OK;
- Aguardando recontagem;
- Recontagem em andamento;
- Recontagem finalizada divergente;
- Recontagem finalizada OK.

Através do parâmetro **"Máximo de dias sem filtrar parceiro nos portais - MAXDIASPORTAIS"** você pode configurar no Portal de Vendas/Portal de Compras/Portal de Mov. Internas um intervalo em dias para se executar as pesquisas por **"Data da negociação"** e/ou **"Data do movimento"**. Caso não seja preenchido o filtro por Parceiro, Nº único ou Nº de documento, o prazo configurado neste parâmetro será respeitado. Valores menores que "0" não tem funcionalidade.

Ao executar uma consulta sem informar um prazo nos filtros de Data da negociação e/ou Data do movimento com o parâmetro configurado, a seguinte mensagem será exibida:

**"Informe um período de até X dia(s) para "Data da negociação" e/ou "Data do movimento" ou informe um filtro por Parceiro, Número único ou Nro. documento."**

É possível ainda que você configure essa mesma funcionalidade de forma específica para o [Portal de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593), através do parâmetro **"Máximo dias sem filtro no Portal de Mov. Internas - MAXDIASPORTMINT"**.

**Nota:** Quando o parâmetro MAXDIASPORTMINT estiver configurado, este terá preferência sobre o parâmetro MAXDIASPORTAIS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Status Documentos

![Imagem 9: Status Documentos](https://ajuda.sankhya.com.br/hc/article_attachments/5923138321303)

Este quadrante permite que você pesquise os documentos de acordo com o seu status; tem-se aqui, as seguintes opções:

- Status NF-e,
- Status NFS-e,
- Status CT-e.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Itens

![Imagem 10: Itens](https://ajuda.sankhya.com.br/hc/article_attachments/5923132310167)

Por meio do quadrante **"Itens"**, você poderá pesquisar pelos documentos desejados, considerando os **"Produtos"** que foram inseridos nos mesmos.

Além disso, na **"Situação do item"** é possível definir se serão apresentados os documentos que contenham itens **"Pendentes"**, **"Não Pendentes"** ou em **"Ambas"** as situações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Liberações

![Imagem 11: Liberações](https://ajuda.sankhya.com.br/hc/article_attachments/5923153784343)

O quadrante **"Liberações"** está diretamente ligado à rotina [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites) e a coluna **"Liberação"** apresentada na grade [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#grade-resultadodaseleo), pois esta última exibe a situação do documento em relação à rotina mencionada; observe as seguintes opções de marcação:

**Sem pendência:** Esta situação diz respeito a um documento que não possui liberações a serem feitas pra ele, ou seja, ele segue o fluxo de processos na empresa, sem a necessidade de nenhuma autorização vinda de outras pessoas (gestores);

**Reprovado:** Temos, neste caso, um documento que passou pela avaliação de um liberador e este não autorizou a solicitação realizada.

**Pendente:** Um documento se encontra nessa situação, quando alguma solicitação de liberação foi feita pra ele, porém o liberador ainda não avaliou sua concessão.

**Aprovado:** Ao solicitar alguma liberação para um documento qualquer e o liberador o concede, tem-se o documento com este status.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Parceiros

![Imagem 12: Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/5923215992471)

O quadrante **"Parceiros"** permite a escolha dos parceiros para os quais se efetuou o lançamento de documentos, de modo a serem filtrados na grade [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#grade-resultadodaseleo).

Ao clicar no botão ![Imagem 13: Ao clicar no botão "Adicionar" será aberto o pop-up "Pesquisando 'Parceiro'" onde você pode buscar os parceiros que…](https://ajuda.sankhya.com.br/hc/article_attachments/16417282728855) **"Adicionar"** será aberto o pop-up **"Pesquisando 'Parceiro'"** onde você pode buscar os parceiros que terão seus pedidos de requisição, requisições etc verificados.

O botão ![Imagem 14: O botão "Remover" retira o(s) parceiro(s) marcados na caixa da listagem construída.](https://ajuda.sankhya.com.br/hc/article_attachments/16417282733335)**"Remover"** retira o(s) parceiro(s) marcados na caixa ![Imagem 15: O botão "Remover" retira o(s) parceiro(s) marcados na caixa da listagem construída.](https://ajuda.sankhya.com.br/hc/article_attachments/5923401336215) da listagem construída.

Por fim, o botão ![Imagem 16: Por fim, o botão "Limpar" apaga todos os parceiros presentes na listagem, marcados ou não.](https://ajuda.sankhya.com.br/hc/article_attachments/16417282736279)**"Limpar"** apaga todos os parceiros presentes na listagem, marcados ou não.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## WMS

![Imagem 17: WMS](https://ajuda.sankhya.com.br/hc/article_attachments/5923438155415)

Último local disponível no Portal de Mov. Internas para ser utilizado como filtro, o quadrante **"WMS"** trabalha com opções ligadas às rotinas de Conferência e o módulo WMS.

O **"Status WMS"** possui vínculo com os processos de Expedição; você pode defini-lo para filtragem dos documentos, dentre as seguintes alternativas:

- Todos;
- Pedido parcialmente cortado;
- Enviado totalmente;
- Enviado parcialmente;
- Não enviado;
- Não controlado pelo WMS;
- Pedido totalmente cortado.

A **"Situação WMS"**, também relacionada aos processos de Expedição, possui as seguintes opções de definição:

- Todos;
- Prob./Erro confirmação nota;
- Aguardando recontagem;
- Em processo separação;
- Enviado para separação;
- Aguardando separação;
- Armazenado.
- Armazenado parcial;
- Aguardando conferência volumes;
- Conferência validada;
- Aguardando conferência (separação);
- Conferência com divergência;
- Parcialmente conferido;
- Aguardando armazenagem;
- Enviado para armazenagem;
- Pedido totalmente cortado;
- Não enviado;
- Cancelada;
- Pedido parcialmente cortado;
- Aguardando formação de volumes;
- Concluído;
- Em processo conferência;
- Aguardando conferência;

**Observação:** Para que o quadrante WMS seja apresentado, é necessário que a empresa possua em sua licença o Módulo WMS. Além disso, para sua correta utilização, é necessário que o filtro correspondente a este status esteja dentro das seguintes regras:

- No [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado para o lançamento, o campo **"Configuração p/ conferência"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) deve estar informado;
- No [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), a marcação **"Excluir do processo de conferência"** localizada na aba Geral, não deve estar assinalada; além disso, no lançamento efetuado, o item precisa estar Pendente;
- Se na [Configuração da Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073), a marcação **"Momento da conferência"** estiver definida como Antes de Faturar, será necessário que o lançamento na [Central de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154) esteja confirmado;
- Caso na Configuração da Conferência, a marcação **"Momento da conferência"** esteja definida como Antes da Confirmação, é necessário que o lançamento na Central de Mov. Internas esteja liberado para conferência;
- O status da conferência deve estar em concordância ao que for selecionado no Portal de Mov. Internas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Grade - Resultado da seleção

A grade **"Resultado da seleção"** é alimentada com os documentos resultantes da configuração previamente realizada nos [Filtros Personalizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#filtropersonalizado) ou dos [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#filtros). Um duplo clique sobre qualquer linha da grade, abre a [Central de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154) para visualização detalhada do documento.

![Imagem 18: A grade " Resultado da seleção " é alimentada com os documentos resultantes da configuração previamente realizada nos…](https://ajuda.sankhya.com.br/hc/article_attachments/5923550515863)

Podemos observar no alto da grade Resultado da seleção alguns botões que são essenciais para as rotinas possíveis de serem executadas no [Portal de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593). Trataremos abaixo sobre cada um deles:

**![Imagem 19: Configuração da Grade: Este botão quando acionado, abrirá um pop-up com este mesmo nome, onde você seleciona as colunas…](https://ajuda.sankhya.com.br/hc/article_attachments/16417282741655) Configuração da Grade:** Este botão quando acionado, abrirá um pop-up com este mesmo nome, onde você seleciona as colunas que irão compor a grade Resultado da seleção.

![Imagem 20: Exportar grade para PDF: Por meio deste botão, você pode realizar a visualização dos dados gerados na grade em…](https://ajuda.sankhya.com.br/hc/article_attachments/18798382036759) **Exportar grade para PDF:** Por meio deste botão, você pode realizar a visualização dos dados gerados na grade em relatório rápido, ou ainda, poderá **"Exportar como PDF"**, **"Exportar como planilha"** ou **"Visualizar em cubo..."**.

**Observação:** com o parâmetro **"Verifica se tem milhar e no tem decimal - TEMMILHARNTDEC"** ligado, ao exportar o relatório no formato planilha, os dados não serão apresentados com casa decimal, mas terão o ponto separador de milhar.

**![Imagem 21: Novo documento: Este botão abre a Central de Mov. Internas posicionando-a para inserção de um novo documento…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268427287) Novo documento:** Este botão abre a [Central de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154) posicionando-a para inserção de um novo documento correspondente ao [Tipo de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#tipodemovimento) que se encontra selecionado. Você pode também escolher previamente o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) que será utilizado, ou ainda o [Layout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634) que servirá de base para o novo lançamento.

**![Imagem 22: Duplicar: Através deste botão, você pode efetuar a duplicação (cópia) de um documento selecionado na grade. Ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268427287) Duplicar:** Através deste botão, você pode efetuar a duplicação (cópia) de um documento selecionado na grade. Ao acioná-lo, será aberto o pop-up **"Duplicar/Copiar Documento"**, onde informa-se a TOP, Série, Data de saída, determina-se se o documento em questão irá atualizar preço, além de ser possível Selecionar Itens que irão compor o futuro documento.

**Importante:** Para que a opção Duplicar se encontre disponível para utilização, o parâmetro **"Permite duplicar pedidos/notas? - PODEDUPNF"** necessita estar habilitado.

**Observação:** Habilitando-se o parâmetro **"Copiar séries de produtos ao duplicar transferências? - DUPSERIEPROD"**, ao duplicar uma nota de transferência os números de série de cada item do produto serão copiados para o novo documento.

**Nota:** O parâmetro **"Atualizar Preço na Duplicação de Pedido - ATUALPRECOPVEN"** quando ligado, realiza a marcação automática da opção **"Atualiza Preço"**, sendo possível desmarcá-la manualmente.

Ao duplicar um pedido/nota com a marcação **"Recalcular preço prod. ao faturar"** ([Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)) realizada, o sistema atualizará o preço mesmo que a opção Atualiza Preço se encontre marcada; quando o campo Recalcular preço prod. ao faturar estiver desmarcado, o preço será atualizado somente se a opção Atualiza Preço estiver selecionada.

Não há relação entre o comportamento descrito acima e as configurações do campo **"Digitação da Nota"** localizado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abavenda).

**![Imagem 23: Remover: Este botão procede com a exclusão do documento selecionado na grade, porém, atente-se para as condições de…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268429975) Remover:** Este botão procede com a exclusão do documento selecionado na grade, porém, atente-se para as condições de remoção de um documento do sistema, por exemplo, após realizar a confirmação de um documento pode-se excluí-lo somente se o Tipo de Operação - TOP utilizado no lançamento possuir em sua aba Geral, a marcação **"Permitir Alteração após confirmar"** acionada.

**![Imagem 24: Imprimir: Por meio deste botão, você pode imprimir os dados apresentados na grade, ou definir a opção de impressão de…](https://ajuda.sankhya.com.br/hc/article_attachments/16417282751383) Imprimir:** Por meio deste botão, você pode imprimir os dados apresentados na grade, ou definir a opção de impressão de acordo com o documento e/ou processo que está sendo executado. Temos as seguintes opções:

- Imprimir Nota;
- Imprimir Boleto;
- Imprimir Expedição;
- Imprimir Nota Adicional;
- Desvincular Impressoras Substitutas;
- Visualizar Boleto.

![Imagem 25: Cancelar Nota: O acionamento deste botão invalida o documento. Você pode obter mais informações acerca deste processo…](https://ajuda.sankhya.com.br/hc/article_attachments/16417282753431) **Cancelar Nota:** O acionamento deste botão invalida o documento. Você pode obter mais informações acerca deste processo nos link's [O que é Cancelar uma Nota Fiscal?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas#oquecancelarumanotafiscal) e [Como realizar o Cancelamento de uma Nota Fiscal?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas#comorealizarocancelamentodeumanotafiscal).

**![Imagem 26: Opções para Nota Fiscal Eletrônica: Temos através deste botão, todas as opções acerca das Notas Fiscais Eletrônicas .…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268440343) Opções para Nota Fiscal Eletrônica:** Temos através deste botão, todas as opções acerca das [Notas Fiscais Eletrônicas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633). No uso do Tipo de Movimento **"Canceladas"**, este botão é habilitado caso algum documento seja selecionado na grade Resultado da seleção.

**Observação:** Ao selecionar uma nota que esteja com o **"Status NF-e" = "Aguardando Correção"** e clicando na opção **"Gerar lote"** disponível neste botão, caso a data e/ou hora estejam diferentes da data e/ou hora do servidor, o parâmetro **"Obriga Dt.Negoc. ser igual a do servidor? - DTNEGSERV"** terá o seguinte comportamento:

- Encontrando-se habilitado, será realizada a alteração da data e/ou hora do documento de forma automática.
- Caso encontre-se desabilitado, será apresentado um pop-up te questionando se você deseja manter a data e/ou hora do documento ou se deseja ajustar estas informações para que estejam de acordo com as informações do servidor.

Desta forma, será possível alterar as datas de negociação, faturamento e entrada/saída de acordo com o mesmo comportamento da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) ao realizar a confirmação de uma nota com data diferente do servidor.

**Importante:** Realize a atualização destas datas e horas pois, se um boleto estiver vinculado à estas datas e for efetuado a correção do cadastro dias depois, a nota e o boleto serão recebidos com datas de saídas incorretas, ocasionando a perda do prazo negociado.

Ao clicar na opção **"Pendente de Retorno"** será apresentada a opção **"Marcar como Pendente de Retorno"**, que ao ser acionada, fará com que as informações da NF-e sejam encaminhadas para outro registro, e esta precisará ser Cancelada após sua aprovação. Dessa forma, uma nova NF-e poderá ser gerada para este lançamento.

Na opção **"DANFE de segurança"** a alternativa **"Marcar como DANFE de segurança"** deve ser utilizada apenas em contingência. Ao selecionar esta opção, o DANFE precisará ser impresso em Formulário de Segurança (FS-DA).

Em relação à opção **"Enviar XML da NF-e/CC-e e Danfe por e-mail"** disponível neste botão, quando esta for selecionada, será enviado ao e-mail cadastrado o XML da NF-e e CC-e, o PDF da NF-e (DANFe) e, também, o PDF da **"Carta de Correção"**, caso exista alguma gerada.

**Nota:** Se você utilizar esta rotina sem um modelo de impressão de Carta de Correção inserido na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abanf-enfc-e), campo **"Relatório Carta de Correção"**, o sistema não encaminhará o PDF no e-mail e não emitirá qualquer mensagem de aviso.

**![Imagem 27: Opções para Nota Fiscal Eletrônica de Serviços: Por meio deste botão, teremos acesso às opções que podem ser utilizadas…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268445463)Opções para Nota Fiscal Eletrônica de Serviços:** Por meio deste botão, teremos acesso às opções que podem ser utilizadas quando realizado o lançamento de uma [Nota Fiscal Eletrônica de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434).

**![Imagem 28: Opções para Conhecimento de Transporte Eletrônico: Este botão exibe as alternativas relacionadas ao CT-e - Conhecimento…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268447895) Opções para Conhecimento de Transporte Eletrônico:** Este botão exibe as alternativas relacionadas ao [CT-e - Conhecimento de Transporte Eletrônico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834).

**![Imagem 29: Entregar - Devolv./Estor.: Este botão será modificado à medida em que os diferentes Tipos de Movimento forem…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268453271) ![Imagem 30: Entregar - Devolv./Estor.: Este botão será modificado à medida em que os diferentes Tipos de Movimento forem…](https://ajuda.sankhya.com.br/hc/article_attachments/5923822790807) Entregar - Devolv./Estor.:** Este botão será modificado à medida em que os diferentes [Tipos de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#tipodemovimento) forem selecionados. Você pode acessar os detalhes sobre cada um dos comportamentos destes botões nos link's [Entregar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601194-Portal-de-Mov-Internas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#entregar) e [Devolver/Estornar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601194-Portal-de-Mov-Internas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#devolv.estor.), respectivamente.

**![Imagem 31: Ações: Através deste botão, tem-se a escolha das ações configuradas previamente na tela Dicionário de Dados .](https://ajuda.sankhya.com.br/hc/article_attachments/16417268454935) Ações:** Através deste botão, tem-se a escolha das ações configuradas previamente na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

**![Imagem 32: Outras Opções: Todas as alternativas de uso apresentadas ao acionar este botão, podem ser acessadas no link Portal de…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268462871) Outras Opções:** Todas as alternativas de uso apresentadas ao acionar este botão, podem ser acessadas no link [Portal de Mov. Internas - Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601194-Portal-de-Mov-Internas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es).

**![Imagem 33: Sankhya Place: Este botão abre a tela " Sankhya Place " , onde podemos visualizar o conteúdo ligado à área Comercial…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268466967) Sankhya Place:** Este botão abre a tela **"Sankhya Place"**, onde podemos visualizar o conteúdo ligado à área Comercial Sankhya. O Sankhya Place também pode ser acessado por meio do link <https://place.sankhya.com.br/#login>.

**![Imagem 34: Mostrar lista de painéis: Localizada no lado superior direito da tela, esta opção exibe a listagem dos painéis que…](https://ajuda.sankhya.com.br/hc/article_attachments/5923896264087) Mostrar lista de painéis:** Localizada no lado superior direito da tela, esta opção exibe a listagem dos painéis que compõem a tela Portal de Mov. Internas. Clicando-se na opção desejada, o sistema direciona o foco para a mesma.

**![Imagem 35: Mapa de atalhos: Além das opções até aqui citadas, que podem ser acessadas via botões, você também poderá fazê-los via…](https://ajuda.sankhya.com.br/hc/article_attachments/5923892335127) Mapa de atalhos:** Além das opções até aqui citadas, que podem ser acessadas via botões, você também poderá fazê-los via atalhos do teclado. Esta opção, assim como a anterior, se encontra no lado superior direito do Portal de Mov. Internas.

**Observação:** Através da coluna **"Ambiente NFS-e (Nota/Pedido)"** presente na grade Resultado da seleção, podemos visualizar em qual ambiente NFS-e a nota foi gerada. Essa coluna é alimentada através da configuração efetuada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abanfs-e) no campo **"Ambiente NFS-e"**. Esta informação será utilizada apenas na emissão própria de notas fiscais de serviço eletrônica.

**Observação:** Ao ligar o parâmetro **"Mostrar parceiros inativos nos portais - MOSTRARPARCINAT"**, o sistema irá exibir as notas de parceiros inativos no layout flex, sem a necessidade de criar filtros personalizados para tal ação.

**Nota:** Para que os valores dos principais campos (listados abaixo) sejam exibidos como totalizadores na grade Resultado de Seleção, é necessário que a marcação **"Habilitar totalizador na grade Resultados de seleção?"** do pop-up [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601194-Portal-de-Mov-Internas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#preferncias) (botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601194-Portal-de-Mov-Internas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)) esteja habilitado.

- Vlr. Nota
- Base da Substituição
- Base do ICMS
- Base do IPI
- Base Substituição Sem Redução
- Comissão
- Comissão Gerente
- Custo Total do Produto
- Desc. Total dos itens em Moeda
- Desconto total por item
- Metro Cúbico
- Peso
- Peso Bruto
- Peso liq. dos itens
- Qtd. volumes
- Total Líq. Itens em Moeda
- Valor DIFAL UF Destino
- Valor DIFAL UF Remet.
- Vlr. da Substituição
- Vlr. Destaque
- Vlr. do Frete
- Vlr. do ICMS
- Vlr. do IPI
- Vlr. do Juro
- Vlr. Moeda
- Vlr. ST FCP Interno

**Observação:** A alteração da marcação acima será aplicada na próxima vez que você entrar no Portal ou na seleção de outro Tipo de Movimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Grade - Itens

Na grade **"Itens"** serão apresentados os itens correspondentes ao documento selecionado na grade [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#grade-resultadodaseleo).

![Imagem 36: Na grade "Itens" serão apresentados os itens correspondentes ao documento selecionado na grade Resultado da seleção .](https://ajuda.sankhya.com.br/hc/article_attachments/5923947114007)

No alto da grade Itens, tem-se o botão ![Imagem 37: No alto da grade Itens , tem-se o botão " Ações" que permite a escolha das ações configuradas previamente na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16417268454935) **"Ações"** que permite a escolha das ações configuradas previamente na tela Dicionário de Dados.

**Observação:** o campo **"Qtd. pendente"** será preenchido em uma próxima ação, por exemplo, quando um pedido se transformar em nota ou uma nota for convertida em devolução. Lembrando que, neste caso o movimento de transferência não será considerado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

## Painel de acesso rápido

O **"Painel de acesso rápido"** localiza-se no canto direito da tela e é caracterizado pela variedade de botões que podem ser disponibilizados para uso.

![Imagem 38: O " Painel de acesso rápido " localiza-se no canto direito da tela e é caracterizado pela variedade de botões que podem…](https://ajuda.sankhya.com.br/hc/article_attachments/5923973206423)

A configuração do painel é acessada através do botão ![Imagem 39: A configuração do painel é acessada através do botão também localizado na região direita da tela, porém na parte…](https://ajuda.sankhya.com.br/hc/article_attachments/5923983646999) também localizado na região direita da tela, porém na parte superior. Ao pressionar o referido botão, é aberto o pop-up **"Configuração do painel de acesso rápido",** onde terá disponibilizadas as opções correspondentes ao botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601194-Portal-de-Mov-Internas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es):

![Imagem 40: A configuração do painel é acessada através do botão também localizado na região direita da tela, porém na parte…](https://ajuda.sankhya.com.br/hc/article_attachments/5924037320727)

A intenção do **"Painel de acesso rápido"** é agilizar o acesso às funcionalidades mais utilizadas pelos usuários referentes ao botão **"Outras Opções..."**. É importante mencionar que todas as opções estão disponibilizadas para todos os [Tipos de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#tipodemovimento), porém, o sistema internamente controla a apresentação de cada opção em seu Tipo de Movimento correspondente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#top)

Acesse também:

[Central de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154)

[Portal de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593)

[Portal de Mov. Internas - Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601194-Portal-de-Mov-Internas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)
