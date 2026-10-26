---
id: "360044609834"
titulo: "Liberação de Limites Orçamentários"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609834-Libera%C3%A7%C3%A3o-de-Limites-Or%C3%A7ament%C3%A1rios"
trilha: "Manual do Produto > Inteligência e Análise > Metas e Orçamentos > Aprovação e liberação"
atualizado_em: "2026-09-23T18:10:06Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "Liberação de Limites", "Limites", "Orçamento", "Liberação", "Orçamentários", "br.com.sankhya.liberacaolimitesorcamentario", "Liberação de Limites Orçamentários manual", "LIBATUALREAL", "Ajusta e confirma valores no Controle Orçamentário e Metas", "Personaliza exibições e atualiza metas para diferentes solicitações", "Permite aplicar filtros exportar dados e gerenciar solicitações", "VLRTOTNTLIBMET", "Metas e Orçamentos", "Controle Orçamentário"]
---

# Liberação de Limites Orçamentários

```
 Módulo: Metas e Orçamentos
```

---

Através desta tela, pode-se realizar a liberação dos limites orçamentários oriundos do módulo Controle Orçamentário e Metas e Jiva Metas e Controle Orçamentário.

**Observação:** **quando for realizada uma liberação de limite orçamentária, o sistema irá verificar se o valor de liberação solicitado é suficiente para que o lançamento correspondente seja** **confirmado. Caso não, antes que a liberação aconteça, tem-se o valor solicitado atualizado e as seguintes mensagens:**

**"O valor solicitado foi atualizado para R$X."**
**"O valor de R$Y não era suficiente para confirmação da nota."**

**Ao clicar em ![Imagem 1: Ao clicar em "Voltar" o pop-up será fechado, o grid será atualizado com os valores atualizados de liberação e a…](https://ajuda.sankhya.com.br/hc/article_attachments/23532030615319) "Voltar" o pop-up será fechado, o grid será atualizado com os valores atualizados de liberação e a liberação não é realizada.**

**Ao clicar em ![Imagem 2: Ao clicar em "Liberar" a liberação será executada, considerando os valores atualizados de liberação.](https://ajuda.sankhya.com.br/hc/article_attachments/23532092411415) "Liberar" a liberação será executada, considerando os valores atualizados de liberação.**

**Importante:** esta tela será apresentada para utilização no Sankhya Om, apenas se a empresa possuir em sua licença, o produto 30742 - CONTROLE ORÇAMENTÁRIO E METAS/W e para o Jiva Evo, o produto 20422 - JIVA - CONTROLE ORÇAMENTÁRIO E METAS.

| [Filtros e preenchimentos iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609834-Libera%C3%A7%C3%A3o-de-Limites-Or%C3%A7ament%C3%A1rios#filtrosepreenchimentosiniciais) |  | [Grade principal e botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609834-Libera%C3%A7%C3%A3o-de-Limites-Or%C3%A7ament%C3%A1rios#gradeprincipalebotesdatela) |
| --- | --- | --- |
| [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609834-Libera%C3%A7%C3%A3o-de-Limites-Or%C3%A7ament%C3%A1rios#Par%C3%A2metrosqueinfluenciamestarotina) |  |  |

![Imagem 3: Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360084887433)

## Filtros e preenchimentos iniciais

Ao acessar a tela, a primeira informação a ser incluída é o **"Usuário"** liberador, bem como sua respectiva **"Senha"** de acesso (senha de login no sistema). Caso o Usuário Liberador seja o mesmo logado no sistema, teremos a marcação **"Sou liberador"** que, ao ser realizada, inibe o preenchimento do Usuário e Senha, e credencia o usuário em questão à execução das devidas liberações; logicamente, caso você (usuário logado) não seja o Usuário Liberador, a marcação Sou liberador não deverá ser realizada.

![Imagem 4: Ao acessar a tela, a primeira informação a ser incluída é o "Usuário" liberador, bem como sua respectiva "Senha" de…](https://ajuda.sankhya.com.br/hc/article_attachments/360084887613)

**Observação:** para que o Usuário Liberador consiga executar, deferir ou indeferir as solicitações de liberação, é necessário que, em seu cadastro, possua os eventos 33 - Antecipação de Orçamento, 34 - Suplementação de Orçamento e 35 - Transferência de Orçamento disponibilizados ([Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), botão **"Outras Opções..."**, opção **"Limites para Liberação"**).

Além da possibilidade de criação de Filtros Personalizados, você pode definir um **"Período"** de abrangência das metas, bem como, através da marcação **"Apresentar apenas os pendentes?"** refinar a busca, exibindo somente as solicitações que ainda não receberam um parecer. Além disto, temos outros quatro campos de pesquisa, destinados à singularizar a alimentação da tela. São eles:

- **Empresa** **-** Empresa com a qual foi lançada a meta/orçamento;
- **Natureza** **-** [Natureza de Receita e Despesa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774) relacionada à meta/orçamento;
- **Centro de Resultado** **-** Você pode adicionar ao filtro o [Centro de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754) correspondente à meta/orçamento;
- **Solicitante** **-** É possível ainda, acrescentar/filtrar por Usuários que efetuaram a solicitação da liberação da meta/orçamento.

Em relação à marcação Apresentar apenas os pendentes?, quando esta for selecionada, serão apresentados apenas as solicitações pendentes com o campo NUNOTA = 0 e os que possuem NUNOTA <> 0 e que o registro exista na TGFCAB; caso o parâmetro **"Alterar rateio nota confirmada sem validar metas? - ALTRATSEMVALMET"** esteja desligado, a nota necessita estar confirmada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609834-Libera%C3%A7%C3%A3o-de-Limites-Or%C3%A7ament%C3%A1rios#top)

## Grade principal e botões da tela

Uma vez definidos o Usuário Liberador e os Filtros desejados, quando você clicar em Aplicar, serão carregadas na Grade principal as devidas solicitações de liberação. Serão exibidas as demandas de liberação de limite do tipo Suplementação, Transferência, Antecipação ou Indefinido; estas movimentações atualmente são geradas através da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) ou da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

![Imagem 5: Quando houver mais de uma liberação orçamentária para a mesma Nota/Meta no campo "Observação Solicitante" (por exemplo,…](https://ajuda.sankhya.com.br/hc/article_attachments/25365343811863) Quando houver mais de uma liberação orçamentária para a mesma Nota/Meta no campo **"Observação Solicitante"** (por exemplo, no processo de [Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/7092297445911-Rateios)), mesmo que sejam inseridas observações diferentes, a informação da última observação inserida prevalecerá.

![Imagem 6: Quando houver mais de uma liberação orçamentária para a mesma Nota/Meta no campo "Observação Solicitante" (por exemplo,…](https://ajuda.sankhya.com.br/hc/article_attachments/360084887813)

Observe as funcionalidades dos botões abaixo:

![Imagem 7: C onfigurar grade](https://ajuda.sankhya.com.br/hc/article_attachments/16368845570199) **Configurar grade**

Por meio deste botão, você escolhe as colunas que serão ou não exibidas na grade principal.

![Imagem 8: Anterior/Próximo](https://ajuda.sankhya.com.br/hc/article_attachments/16368845572631) **Anterior/Próximo**

Estes botões são responsáveis pela navegação entre os registros dispostos na grade.

![Imagem 9: Exportar grade para PDF](https://ajuda.sankhya.com.br/hc/article_attachments/22891353716375) **Exportar grade para PDF**

Este botão apresenta opções de exportação e visualização das informações da tela. Você poderá **"Exportar para PDF"**, **"Exportar para planilha"**, **"Exportar para cubo"**e o suporte para **"Relatórios Formatados"**.

![Imagem 10: Ações](https://ajuda.sankhya.com.br/hc/article_attachments/16369346668823) Ações

Serão apresentadas neste botão, ações que permitem a execução de tarefas específicas de forma rápida e descomplicada. No [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773) e no [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294) através da aba **"Ações"** é possível definir a execução de uma Rotina no Banco de dados (Stored Procedure), execução de uma Rotina Java, execução de um Script (JavaScript) ou o Lançamento de uma tela do sistema.

![Imagem 11: Detalhes](https://ajuda.sankhya.com.br/hc/article_attachments/16369346669719) **Detalhes**

Este botão, quando acionado, exibirá um pop-up de nome **"Detalhes do financeiro"**, onde temos informações a respeito do financeiro correspondente à linha selecionada na grade principal.

![Imagem 12: Liberar](https://ajuda.sankhya.com.br/hc/article_attachments/16369580855959) **Liberar**

Através deste botão, você permitirá a solicitação de liberação. Você pode realizar liberações para registros do tipo Antecipação, Suplementação ou Transferência. Trabalhando com solicitações do tipo Transferência, ao efetuar sua liberação, diferentemente dos outros tipos de solicitação, será aberto o pop-up **"Transferência de Recursos Orçamentários"**; neste pop-up, você delimita o valor a ser transferido, ou seja, poderá atender a solicitação de liberação de forma total ou parcial.

**Importante:** é preciso utilizar o botão acima para a transferência ser realizada corretamente, pois a meta precisar ser atualizada. Pode-se ainda atualizar essa meta automaticamente, para isso, basta acionar o parâmetro **"Atualizar Realizado da Meta na Liberação Orçamentária? - LIBATUALREAL"**.

A coluna **"Saldo disponível"** exibe o valor que se encontra liberado para transferência. Assim, no campo **"Valor solicitado"** será indicado qual o percentual do valor liberado será transferido.

**Nota:** os demais tipos de solicitação são diretamente liberados; não contam com a exibição de nenhum pop-up para ajustes de valores.

**Observação:** ao ligar o parâmetro **"Restringir CR na Trasf. Orçamentários - RESCRTRANORCA"**, o sistema irá exibir somente os Centros de Resultados em que o Liberador é responsável. Lembrando que, o usuário Liberador deve ser vinculado no campo **"Usuário Responsável"** da tela [Centros de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754).

![Imagem 13: Negar liberação](https://ajuda.sankhya.com.br/hc/article_attachments/16369526574231) **Negar liberação**

Ao contrário do botão anterior, por meio deste, o responsável pela liberação nega a solicitação de liberação. Sempre que ocorre a negação de uma solicitação, sua respectiva linha é retirada da grade principal.

**Importante – Renegociação de Títulos Liberados:** Se um título que excedeu o orçamento já foi liberado nesta rotina, mas passar por um processo de **Renegociação**, a liberação anterior será invalidada pelo sistema.

- **Comportamento:** O sistema zera o valor do campo **VLRDESDOB** (Valor Desdobrado) do título original e move o montante para o campo **VLRALIBERAR**.
- **Motivo:** A renegociação cria uma nova obrigação financeira que pode conter alterações de datas, naturezas ou centros de resultado, exigindo uma nova análise de impacto orçamentário.
- **Ação necessária:** O novo título gerado deverá passar por um novo processo de liberação nesta tela para que o valor volte a ser considerado como "desdobrado" no orçamento.

![Imagem 14: Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/16369557315095) **Outras Opções...**

O botão Outras Opções... conta com duas funcionalidades:

- **Exibir Acumulado:** Acionando esta opção, será aberto o pop-up denominado **"Resultados do Orçamento"**, onde teremos os dados no Período e no Ano correspondentes aos valores Orçados, Suplementados, Antecipados, Transferidos, Transferências de Saldo, Realizado, Compromissos, Saldos e Pendentes de Confirmação. Além disto, é possível recarregar os valores por meio do botão **"Atualizar Realizado"**.
- **Preferências:** Através desta opção, será aberto um pop-up com esta mesma nomenclatura, em que é disponibilizada a marcação **"Tentar confirmar a nota automaticamente?"** que, sendo realizada, ao efetuar a liberação da solicitação selecionada na grade, o sistema fará a tentativa de confirmação de seu título correspondente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609834-Libera%C3%A7%C3%A3o-de-Limites-Or%C3%A7ament%C3%A1rios#top)

## Parâmetros que influenciam esta rotina

**Considera o valor total da nota na liberação de limites da Meta? - VLRTOTNTLIBMET:** com este parâmetro ativado, a solicitação de liberação orçamentária sempre considerará o valor total da nota. Quando desativado, a solicitação orçamentária será feita com base no saldo disponível do orçamento correspondente. Em outras palavras, quando o parâmetro está ativo, o sistema apresentará no campo **"Valor Solicitado"**, o valor calculado com base no total da nota, porém internamente a solicitação ocorrerá com base no valor excedente.

[GIF animado: Imagem 15: Considera o valor total da nota na liberação de limites da Meta? - VLRTOTNTLIBMET: com este parâmetro ativado, a…](https://ajuda.sankhya.com.br/hc/article_attachments/34493118917271)

Em contrapartida, quando desligado, o sistema apresentará no campo "**Valor Solicitado"** o valor calculado com base no saldo disponível do orçamento correspondente, isto é, o valor excedente ao orçamento.

[GIF animado: Imagem 16: Em contrapartida, quando desligado, o sistema apresentará no campo " Valor Solicitado" o valor calculado com base no…](https://ajuda.sankhya.com.br/hc/article_attachments/34493118918807)

Os parâmetros a seguir também influenciam esta rotina quando a operação envolve vendas com cartão de crédito ou débito (evento 03). A configuração incorreta de qualquer um deles pode fazer com que o sistema solicite liberação mesmo em vendas à vista no débito.

**Validar Limite de Crédito por Tipo de Negociação – VALLIMCRETPV:** controla o consumo do limite de crédito com base no Subtipo definido na tela **Tipo de Negociação**, independentemente da origem do título.

- **Nenhum** — o sistema considera todos os títulos financeiros para o consumo do limite de crédito, independentemente do Subtipo configurado no Tipo de Negociação.
- **Apenas crédito** — o sistema desconsidera do consumo do limite de crédito os títulos cujo Subtipo, definido na tela **Tipo de Negociação**, seja "Cartão de Crédito".
- **Apenas débito** — o sistema desconsidera do consumo do limite de crédito os títulos cujo Subtipo, definido na tela **Tipo de Negociação**, seja "Cartão de Débito".
- **Ambos** — o sistema desconsidera do consumo do limite de crédito os títulos cujo Subtipo, definido na tela **Tipo de Negociação**, seja "Cartão de Crédito" ou "Cartão de Débito".

**Validar Limite de Crédito por Tipo de Título – VALLIMCRETIT:** define quais títulos financeiros serão considerados ou desconsiderados na validação do limite de crédito, com base no Subtipo configurado na tela **Tipo de Título**, desde que os títulos tenham origem no estoque (Central de Compras ou Central de Vendas).

- **Nenhum** — o sistema considera todos os títulos financeiros, independentemente do Subtipo configurado no Tipo de Título, para fins de validação do limite de crédito.
- **Apenas crédito** — o sistema desconsidera da validação do limite de crédito os títulos financeiros configurados com o Subtipo "Cartão de Crédito" na tela **Tipo de Título** e que tenham origem no estoque (Central de Compras/Vendas).
- **Apenas débito** — o sistema desconsidera da validação do limite de crédito os títulos financeiros configurados com o Subtipo "Cartão de Débito" na tela **Tipo de Título** e que tenham origem no estoque (Central de Compras/Vendas).
- **Ambos** — o sistema desconsidera da validação do limite de crédito todos os títulos financeiros configurados com os Subtipos "Cartão de Crédito" ou "Cartão de Débito", desde que tenham origem no estoque (Central de Compras/Vendas).

**ℹ️ Nota**

Os parâmetros `VALLIMCRETIT` e `VALLIMCRETPV` atuam de forma complementar, porém em níveis distintos: `VALLIMCRETIT` avalia o Tipo de Título e a origem no estoque; `VALLIMCRETPV` avalia o Tipo de Negociação, independentemente da origem. A configuração correta de ambos é essencial para garantir o comportamento esperado na validação e no consumo do limite de crédito.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609834-Libera%C3%A7%C3%A3o-de-Limites-Or%C3%A7ament%C3%A1rios#top)
