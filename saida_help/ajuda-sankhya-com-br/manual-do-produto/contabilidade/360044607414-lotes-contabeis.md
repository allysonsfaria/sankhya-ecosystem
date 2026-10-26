---
id: "360044607414"
titulo: "Lotes Contábeis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-08-17T19:33:38Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Situação", "Relatórios", "Contabilidade", "Financeiro", "Aberto", "Contábeis", "Fechado", "Fechar", "Reabrir", "br.com.sankhya.mgecontab.lotes.contabeis", "Lotes Contábeis manual", "Lotes", "Gestão Eficiente de Lotes Contábeis"]
---

# Lotes Contábeis

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42314952452503) Módulo: Contabilidade> Arquivos
```

---

Nesta tela, você realizará a manutenção de Lotes Contábeis. Nela podem ser realizados os cadastros, exclusões, edições, fechamentos e reaberturas de lotes. Sendo assim teremos:

| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis#filtros) | [Cadastros, Edição e Exclusão de lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis#cadastro,edi%C3%A7%C3%A3oeexclus%C3%A3odelotes) |
| --- | --- |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) | [Considerações acerca da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis#considera%C3%A7%C3%B5esacercadatela) |

                       

![Imagem 2: Considerações acerca da tela](https://ajuda.sankhya.com.br/hc/article_attachments/1500000203042)

Filtros

Na parte superior esquerda da tela, você poderá realizar a configuração de filtros personalizados por meio do ícone , de modo que sejam apresentados os lotes conforme a necessidade e a configuração realizada.

Na **"Referência"** defina o período que será utilizado para efetuar a busca do mês e o ano de referência dos lotes. São disponibilizadas as seguintes opções de escolha:

- Todos (serão considerados todos os meses do ano corrente);
- Janeiro;
- Fevereiro;
- Março;
- Abril;
- Maio;
- Junho;
- Julho;
- Agosto;
- Setembro;
- Outubro;
- Novembro;
- Dezembro.

No **"Intervalo de Lotes"**, depois de definido o período de referência, informe neste campo um intervalo de numeração dos lotes que estejam dentro do período estabelecido anteriormente.

O campo **"Período de movimento"** é preenchido automaticamente ao definir o campo Referência, ou você também poderá preenchê-lo manualmente, informando um período que se encaixe no período contábil, e no que foi estabelecido anteriormente no campo Referência. Caso informe um período em desacordo com estas configurações, será apresentada a seguinte mensagem:

**"O período de movimentação está fora do período contábil. Deve estar dentro de xx/xx/xxxx a xx/xx/xxxx."**

O campo **"Exibir Lotes"** é destinado a definição da exibição dos lotes de acordo com sua situação. Pode-se escolher dentre as seguintes opções:

- Todos;
- Abertos;
- Fechados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis#top)

Cadastro, Edição e Exclusão de Lotes

Ao cadastrar um lote contábil, o sistema respeita a configuração realizada na tela **"Contabilidade > Preferências > Empresa"**, onde são utilizados os seguintes campos:

- **"Referência"** (aba Exercício): Para cálculo do ano contábil;
- **"Numeração dos Mestres de Lote"** (aba Lançamentos): Para controle de numeração do lote;
- **"Início do número do lote manual"** e **"Fim do número do lote manual"** (aba Lançamentos): Para controle de numeração manual.

Na realização do cadastro de um lote, os seguintes campos são de preenchimento obrigatório:

- Nro. Lote;
- Referência;
- Dt. Movimento;
- Total do lote;

O campo **"Situação"** é definido automaticamente de acordo com o status do lote, que pode ser **"Aberto"** ou **"Fechado"**.

Os demais campos são preenchidos automaticamente de acordo com os lançamentos contábeis realizados.

O campo **"Observação"** é destinado a preencher alguma característica ou particularidade relevante para o lote que está sendo cadastrado.

Ao cadastrar o lote, este é registrado com a situação **"Aberto"**.

**Nota:** Os campos **"Referência"** e **"Total do lote"** depois que o registro é incluído e salvo, se tornam inabilitados para edição.

Os procedimentos descritos abaixo de **"Fechamento"** e **"Reabertura"** de lotes, são realizados através do acionamento do botão **"Outras Opções..."** presente na parte superior direita da tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis#top)

## Botões Outras Opções...

Neste botão teremos as opções abaixo:

![Imagem 3: Neste botão teremos as opções abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/1500000206901)

Ao realizar o fechamento de um lote, é feita a validação da diferença entre os lançamentos de crédito e de débito, caso esta diferença seja diferente de "0" (zero), o lote não poderá ser fechado e a seguinte mensagem será apresentada:

**"O Lote não foi fechado, pois existe diferença dos Débitos em relação aos Créditos, verifique a coluna "Diferença" e faça a correção."**

Caso a diferença entre os créditos e débitos esteja correta, mas o total informado no lote e o lançamento do lote estejam diferentes, será exibida uma nova mensagem questionando sobre a correção do lote. Para fechamento do lote, esta diferença não pode existir.

Referente à opção Reabrir Lotes, tem-se que procedimento de reabertura de lotes é realizado, para que seja possível efetuar algum eventual ajuste nos lançamentos, e consequente recomposição de seus saldos.

O Fechamento mês é uma rotina que tem como objetivo, verificar se todos os lotes no mês que está sendo fechado, estão apresentando a situação igual a **"Fechado"**, realizar a atualização os saldos das contas contábeis no período de referência, fazer a alteração da data do mês de referência da contabilidade para o mês seguinte e apresentar o relatório de **"Validação de Débito/Crédito"** por data de lançamento.

Ao acionar esta opção, será aberta uma pequena tela apresentando o mês atual, que neste caso consiste no mês de referência informado no campo **"Referência"** presente na tela **"Contabilidade > Preferências > Empresa > aba Exercício"**.

![Imagem 4: Ao acionar esta opção, será aberta uma pequena tela apresentando o mês atual, que neste caso consiste no mês de…](https://ajuda.sankhya.com.br/hc/article_attachments/360099073634)

Ao clicar em **"Confirmar"**, o sistema verifica se todos os lotes do mês apresentado estão fechados. Caso existam lotes abertos, o fechamento não será permitido, e a seguinte mensagem será apresentada:

**"O mês atual não poderá ser fechado, pois contém Lote(s) Aberto(s)"**

Com todos os lotes fechados, ao confirmar o fechamento do mês, o sistema apresentará uma mensagem para informá-lo que o fechamento foi realizado.

Ao realizar o fechamento do último mês do período contábil (Dezembro), será apresentada uma mensagem sobre o procedimento:

**"Atenção, O mês atual é o último mês do exercício. Confirma fechamento do mês e do exercício?"**

Ao clicar em **"Sim"**, o sistema irá efetuar o fechamento do mês e a alteração do exercício contábil para o exercício seguinte, modificando a data de referência para o primeiro mês (Janeiro) do período contábil seguinte.

Se você clicar na opção **"Cópia de Lote entre empresas"**, o pop up de mesma nomenclatura será aberto:

![Imagem 5: Se você clicar na opção "Cópia de Lote entre empresas" , o pop up de mesma nomenclatura será aberto:](https://ajuda.sankhya.com.br/hc/article_attachments/360101305873)

Ao acionar essa opção, você poderá realizar a cópia de quantos e quais lotes forem necessários para as empresas. Para que seja possível efetuar tal procedimento, duas premissas devem ser satisfeitas:

1)Ambas as empresas (origem e destino), devem possuir o mesmo Plano de Contas;

2)Para o lote a ser criado, o número do lote no mês de referência não pode existir.

Pode-se perceber que a tela é dividida em dois quadrantes, sendo o primeiro deles referente a empresa de origem, ou seja, a empresa da qual os lotes serão copiados.

- O campo **"Empresa"** será apresentado preenchido com a empresa já selecionada na abertura da tela Lotes Contábeis. Caso seja necessário utilizar outra empresa como base para cópia, selecione-a por meio de um clique no nome da empresa em destaque no lado superior direito da tela.
- Logo abaixo, informe o **"Lote"** de origem, que será copiado para a empresa de destino.
- O campo **"Referência"** será preenchido automaticamente ao informar a numeração do Lote.

Já no quadrante inferior, teremos os dados da empresa de destino, ou seja, a empresa para a qual os lotes serão copiados.

Selecione primeiramente, a **"Empresa"** de destino e informe diretamente seu código ou buscando o mesmo pelo ícone de pesquisa. Serão apresentadas para escolha, apenas as empresas que tiverem seu plano de contas compatível com a empresa de origem.

Em seguida, informe o **"Lote"** de destino que será criado.

Por fim, preencha a data de **"Referência"** do lote que está sendo elaborado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis#top)

## Considerações acerca da tela

- Os campos de destino, **"Lote"** e **"Referência"** não poderão existir para que seja efetuada a cópia.
- Caso informe um lote para ser copiado cujo número já exista naquela referência, o sistema irá exibir a seguinte mensagem:

**"Lote (número) já existente na empresa destinatária, altere o número do lote para que o mesmo possa ser copiado."**

- A opção Fechar todos os lotes é responsável por realizar o fechamento de todos os lotes que se encontram em aberto. Poderão ser fechados apenas os lotes cuja referência tenha sido informada nos filtros. Ao clicar nesta opção, todos os lotes correspondentes à referência informada serão fechados.
- Referente à opção Visualizar Lançamentos (Ctrl + L), ao selecionar um determinado lote contábil e clicar nessa opção, a tela [Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173) será aberta automaticamente, selecionando os lançamentos contábeis que se referem àquele lote.

**Nota:** Caso você selecione esta opção sem posicionar nenhum registro, será exibida a mensagem seguinte:

**"É necessário um lote selecionado para que seus lançamentos possam ser visualizados".**

**Observação:** Para esta opção, apenas um registro poderá ser selecionado pois, ao selecionar mais de um lote, será informado que não é possível visualizar os lançamentos para mais de um lote e solicitará a seleção de apenas um lote.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607414-Lotes-Cont%C3%A1beis#top)
