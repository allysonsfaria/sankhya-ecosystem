---
id: "360044606754"
titulo: "Centros de Resultado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-18T14:03:59Z"
rotulos: ["manual", "Sintético", "Configuração", "Máscara", "Contas", "Centro de Resultado", "Relatórios Gerenciais", "Centros de resultado", "Plano de contas", "br.com.sankhya.fin.cad.centroresultado", "Centros de Resultado manual", "Analítico", "Estrutura", "Financeiro", "Centros de Resultado: Análise e Configuração"]
---

# Centros de Resultado

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310861090967) Módulo: Configurações > Cadastros > Gerencial
```

---

Um Centro de Resultado pode ser definido como um subconjunto ou parte de uma empresa que pode ter suas receitas e despesas analisadas separadamente, possibilitando avaliar seu desempenho e compará-lo ao da empresa como um todo. Esses subconjuntos podem ser, por exemplo, departamentos, obras, unidades de negócio, agências, filiais, entre outros.

Essa é uma das telas do sistema composta por árvore hierárquica. Você pode saber mais sobre, por meio do artigo [Telas com Hierarquia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600814).

A configuração do Centro de Resultado é precedida pela definição da máscara ou estrutura dos níveis, esse procedimento é realizado através do parâmetro **"Máscara para o Centro de Resultado - MASCCENCUS"**.

Quando o parâmetro **"Usar máscara MASCCENCUS na geração do arquivo ECD - CTBUSAMASCCECD"** estiver ligado, ele impactará na apresentação do código de centro de custo, aplicando a máscara definida no parâmetro MASCCENCUS, porém sem pontuação, exibindo apenas números.

**Observação:** caso o usuário tenha gerado o ECD do ano anterior sem a máscara (apenas utilizando os números), pode ocorrer erros de validação ao importar o ECD atual, utilizando a função de importação do ECD anterior disponível no PVA.

| ![Imagem 2: Observação: caso o usuário tenha gerado o ECD do ano anterior sem a máscara (apenas utilizando os números), pode…](https://ajuda.sankhya.com.br/hc/article_attachments/42310861091607) | Tem-se nesta tela suporte para campos adicionais. Para maiores informações sobre essa funcionalidade acesse [Campos Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934-Conhecendo-o-Sankhya-W#camposadicionais "clique aqui"). |
| --- | --- |

Para saber mais sobre a tela, consulte os links a seguir:

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#abageral)                                                                   [Aba Quadro de Área](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#abaquadroderea)

[Aba Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#abanaturezas)                                                          [Aba Limites Orçamentário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#abalimitesor%C3%A7ament%C3%A1rio)

[Aba Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#abausurios)                                                             [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#botooutrasopes...)

![Imagem 3: Aba Usuários Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/6921931140887)

## Aba Geral

Ao habilitar a marcação **"CR para calculo e-LALUR (Parte A)"**, os centros de resultados **"CR"** que serão utilizados no processo de apuração realizado na tela [Apuração Regime Normal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607314) serão filtrados; sendo ainda que, apenas os saldos das Contas Contábeis e CR's serão considerados nos filtros.

Caso o campo **"Ativo"** se encontre desabilitado, o Centro de Resultado não poderá ser visualizado nos demais cadastros e rotinas do sistema.

Para realizar o cadastro de um Centro de Resultado Sintético, é necessário que você desmarque a opção **"Analítico"**.

**Observação:** as opções Ativo e Analítico virão automaticamente acionadas pelo sistema na inclusão de um novo Centro de Resultado. Nas demais rotinas do sistema serão aceitas apenas as linhas Analíticas.

O campo **"Veículo Obrigatório"** será apresentado para utilização, apenas se o parâmetro **"Usar rateio por veículo? - RATEIOPORVEICU"** estiver habilitado. Através de sua marcação, determine os rateios por veículo serão realizados no Centro de Resultado.

O campo **"Parceiro Responsável"** será preenchido com o [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) responsável pelo Centro de Resultado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#top)

## Aba Quadro de Área

![Imagem 4: Aba Quadro de Área](https://ajuda.sankhya.com.br/hc/article_attachments/4424713186583)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#top)

## Aba Naturezas

Nesta aba você irá relacionar as Naturezas com o Centro de Resultado, informando quais serão utilizadas nos lançamentos realizados com este Centro de Resultado. O cadastro das Naturezas só é possível para os Níveis Analíticos dos Centros de Resultado. Esta informação é utilizada a princípio apenas como instrumento para formatação de relatórios para este tipo de análise, não sendo validada esta combinação nos lançamentos realizados pelos Portais, Movimentação Financeira ou Rateio.

![Imagem 5: Nesta aba você irá relacionar as Naturezas com o Centro de Resultado, informando quais serão utilizadas nos lançamentos…](https://ajuda.sankhya.com.br/hc/article_attachments/4424740115863)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#top)

## Aba Limites Orçamentário

Essa aba será habilitada quando o parâmetro **"Usa lib. orçamentária por CR e valor excedente? - HABLIBORCEXCCR"** estiver ligado.

![Imagem 6: Essa aba será habilitada quando o parâmetro "Usa lib. orçamentária por CR e valor excedente? - HABLIBORCEXCCR" estiver…](https://ajuda.sankhya.com.br/hc/article_attachments/4424735919127)

Assim, ao habilitá-lo, o sistema deixará de considerar a configuração dos eventos **"33 - Antecipação de Orçamento"**, **"34 - Suplementação de Orçamento"** e **"35 - Transferência de Orçamento"**, da opção **"Limites para Liberação"** do [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874) e irá considerar os cadastros desta aba dos Centros de Resultado.

Ao confirmar uma nota nas Centrais e utilizar a configuração de liberação orçamentária por centro de resultado e valor excedente, esta será direcionada automaticamente para o responsável que tiver a alçada para liberação. Caso não seja associado nenhum usuário para liberação, será emitido um alerta nas Centrais de Notas informando que não foi encontrado nenhum usuário responsável com alçada para liberação do orçamento excedido.

```
                                         ![Imagem 7: Ao confirmar uma nota nas Centrais e utilizar a configuração de liberação orçamentária por centro de resultado e valor…](https://ajuda.sankhya.com.br/hc/article_attachments/16106826526999)
       Ao disparar os eventos acima, o sistema observará o período de suplência,
       configurado no Cadastro de Usuários, aba "Suplentes". Dessa maneira, caso
       um determinado usuário encontre-se ausente no período configurado na aba
       Suplentes, todo evento que for disparado para o mesmo, será direcionado
       ao usuário suplente.
```

De outra forma, caso não exista configuração nesta aba, será disparado o evento para o usuário responsável configurado no Centro de Resultado.

O valor do limite será verificado pelo campo **"Valor excedido"**, que atende todas as possibilidades através do Centro de Resultado que encontra-se cadastrado:

- Permite Suplementação;
- Permite Antecipação;
- Permite Transferência.

Configure o campo **"Tipo limite"** dentre as opções **"Evento"** ou **"Mensal"**. Para analisar um exemplo da solicitação de liberação do tipo [Mensal,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045226793) acesse o link.

**Observação:** na tela de [Liberação de Limites Orçamentários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609834), caso um usuário tente executar uma ação em que ele não possui alçada, será exibido um pop-up para que o mesmo transfira o evento para o próximo usuário liberador que tenha permissão para executar a ação.

```
                                           ![Imagem 8: Observação: na tela de Liberação de Limites Orçamentários , caso um usuário tente executar uma ação em que ele não…](https://ajuda.sankhya.com.br/hc/article_attachments/16106826526999)
     Os parâmetros "Nível p/Aprov.Antecipação de Orçamento - NIVAPROVANTECIP",
            "Nível p/Aprov.Suplementação de Orçamento - NIVAPROVSUPL" e "Nível p/Aprov.
           Transferência de Orçamento - NIVAPROVTRANSF" devem estar configurados com
     qualquer valor acima de 0 para que liberação orçamentária por CR e valor
     excedente seja executada.
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#top)

## Aba Usuários

Esta aba apresenta o usuário responsável ligado ao Centro de Resultado padrão configurado no campo **"Cód.Centro Resultado Padrão"**, aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao), no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios).

![Imagem 9: Esta aba apresenta o usuário responsável ligado ao Centro de Resultado padrão configurado no campo "Cód.Centro…](https://ajuda.sankhya.com.br/hc/article_attachments/4424713492631)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#top)

## Botão Outras Opções...

#### Gerar registros filhos

Quando o botão **"Outras Opções..."** é acionado na tela, tem-se a exibição da opção **"Gerar registros** **filhos"**, que o permitirá realizar um processo muito útil quando existe um padrão repetitivo na criação dos Centros de resultados.

Para esta geração ocorrer, o cadastro já deve possuir uma máscara para Centro de Resultado que contenha um Centro de Resultado Sintético da hierarquia Pai.

Ao acionar a opção Gerar registros filhos, será apresentado um pop-up de mesma nomenclatura com os seguintes campos para configuração:

![Imagem 10: Ao acionar a opção Gerar registros filhos , será apresentado um pop-up de mesma nomenclatura com os seguintes campos…](https://ajuda.sankhya.com.br/hc/article_attachments/4424736023959)

O campo **"Adicionar nome registro pai"** permite que você configure no nome do CR filho o nome do CR do Pai. Este, possui as seguintes opções:

- **Não adicionar:** Não será incluso o nome do CR Pai;
- **Adicionar no início:** Será incluso o nome do CR Pai no início do nome do CR Filho a ser gerado;
- **Adicionar no final:** O nome do CR Pai será adicionado no final do nome do CR Filho a ser gerado.

Ao acionar a marcação **"Registros analíticos?"**, a marcação **"Analítico"** será habilitada. Caso esteja desmarcada, o CR filho será sintético.

**Seção Nome dos registros**

O campo **"Parte fixa"** deve ser preenchido com o nome do CR Filho. Este será obrigatório caso o campo Adicionar nome registro pai esteja configurado com a opção Não Adicionar.

Os campos **"Número inicial"** e **"Número final"** serão preenchidos com o intervalo da quantidade de CR filhos que serão criados, visto que, farão parte da descrição do CR Filho.

#### Substituir Centro de Resultado

No botão Outras Opções, temos também a opção **"Substituir Centro de Resultado"**, por meio dela, você poderá realizar a substituição de determinado centro de resultado. Para isso,

1. Informe o **"Centro de Resultado a ser Substituído"** e o **"Centro de Resultado Novo"**.
2. Caso deseje excluir o centro de resultado substituído, ative a marcação **"Excluir Centro de Resultado Substituído"**.
3. Com as configurações efetuadas, acione o botão **"Atualizar"**.

![Imagem 11: Informações importantes sobre a rotina de Substituição de Centro de Resultado:](https://ajuda.sankhya.com.br/hc/article_attachments/16106826526999) **Informações importantes sobre a rotina de Substituição de Centro de Resultado:**

- O usuário deve conter permissão de acesso para realizar esta rotina (tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), menu **"Configurações > Cadastros > Gerencial > Centros de Resultado"** marcação **"Substituir Centro Resultado"**).
- A funcionalidade de substituição irá atualizar apenas as tabelas que possuem vínculo direto com a tabela do Centro de Resultado por meio da chave estrangeira (TSICUS).
- A rotina de substituição de centro de resultado foi criada para facilitar a troca de cadastros antigos por novos cadastros. Esta rotina só pode ser utilizada no momento da criação do novo cadastro, ou seja, antes do novo centro de resultado ser usado em qualquer lançamento. Se o novo centro de resultado já tiver sido aplicado, a substituição não será possível. Neste caso, recomenda-se inativar o registro que não será mais utilizado, garantindo que ele não seja empregado em novos lançamentos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado#top)
