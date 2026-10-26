---
id: "360044604454"
titulo: "Registro de Atendimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:03:51Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parceiro", "Contratos", "Anexos", "Ordem de Serviço", "Atendimento", "Registro", "GRUSERVREGATEND", "ORIGEMPADOS", "PERIOCONSULOS", "SERVICOPADRAO", "STATUSPADOS", "STATUSPADSUBOS", "br.com.sankhya.os.cad.registroatendimento", "Registro de Atendimento manual", "Registro de Atendimento: Agilidade e Controle"]
---

# Registro de Atendimento

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311189047191) Módulo: Contratos e Serviços > Ordem de Serviço
```

---

Nesta tela, você tem a possibilidade de registrar o atendimento inicial ao seu cliente de forma mais ágil, permitindo uma visualização mais rápida ao histórico de atendimentos para aquele Parceiro.

| [Aba Consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#abaconsulta) |  | [Aba Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#abalan%C3%A7amento) |
| --- | --- | --- |
| [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#par%C3%A2metrosqueinfluenciamestarotina) |  |  |

![Imagem 2: Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/9300688687383)

## Aba Consulta

Na aba **"Consulta"**, informe no campo **"Parceiro"** o nome ou razão social do Parceiro que você deseja buscar. Pode-se buscar o Parceiro através do ícone em formato de **"lupa"** localizado à frente do campo, ou ainda, digitando o início do nome do Parceiro, onde o sistema efetua uma busca rápida e apresenta na grade todos os Parceiros que possuem o nome ou razão social que contém o texto informado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#top)

## Aba Lançamento

Ao serem apresentados os registros na grade, você pode dar um duplo clique sobre o registro desejado, ou selecioná-lo e, pressionando o botão **"Selecionar"**, a aba **"Lançamento"** será habilitada e aberta.

![Imagem 3: Ao serem apresentados os registros na grade, você pode dar um duplo clique sobre o registro desejado, ou selecioná-lo…](https://ajuda.sankhya.com.br/hc/article_attachments/9300726736535)

No cabeçalho desta aba, visualizamos o nome do Parceiro, sua Cidade, a UF e seu Telefone. No canto superior direito da tela, são apresentados os botões **"Salvar"**, que realiza o salvamento do registro de atendimento, criando uma nova Ordem de Serviço, e o botão **"Limpar"**, que efetua a limpeza dos valores inseridos, redirecionando o foco da tela para a aba Consulta, desabilitando novamente a aba Lançamento.

A aba Lançamento, é composta por outras três sub-abas. São elas: [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#sub-abageral), [Anexos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#sub-abaanexos) e [Histórico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#sub-abahistrico).

**Sub-aba Geral**

Nesta aba, são apresentados os campos onde serão informados os dados padrão para o lançamento de uma OS. Além disto, alguns campos são carregados automaticamente, considerando os valores mais utilizados para o Parceiro selecionado, são eles, **"Contrato"**, **"Produto"** e **"Contato"**.

Para que o Contrato seja apresentado na aba Geral, este deverá conter **"Natureza"** informada ([Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abapropriedades)); nesta mesma tela, na aba [Produtos/Seviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaprodutosservios), inclua ao menos um produto Ativo; este não poderá estar configurado como Serviço. Porém, podem ser cadastrados serviços no contrato mas, para apresentação do contrato na tela de [Registro de Atendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454), você deve cadastrar pelo menos um Produto.

**Importante:** logo após informar o Contrato do Parceiro, o sistema efetua a validação se seu cliente possui alguma pendência financeira junto à Empresa; caso afirmativo, será apresentada a mensagem:

**"Parceiro em atraso desde o dia XX/XX/XXXX. Total atrasado: R$X,XX"**

O campo **"Serviço"** é alimentado da seguinte maneira: acesse a tela Contratos, informe o Código da Natureza na aba Propriedades; em seguida, acesse a tela [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774), selecione a natureza informada anteriormente, acesse a aba **"Serviços Autorizados"** e cadastre então os serviços que deverão ser apresentados no campo Serviço da rotina de Registro de Atendimento. Caso nenhum serviço esteja cadastrado, o sistema não permitirá que o atendimento seja registrado.

Se algum valor não puder ser utilizado em algum campo, o ícone ![não](https://ajuda.sankhya.com.br/hc/article_attachments/15470297306903) **"Não encontramos valores para este campo"** será apresentado logo à frente. Ao posicionar o mouse sobre o ícone, será exibida uma mensagem informando o motivo pelo qual aquele campo não pode ser utilizado. Se algum campo estiver com o ícone de inválido à frente e for feita a tentativa de salvamento do registro clicando no botão Salvar, o sistema exibirá a seguinte mensagem:

**"Existem campos com valores inválidos. Por favor, verifique-os antes de salvar."**

Para escolha dos **"Executantes"**, serão apresentados apenas aqueles que tiverem sido cadastrados na tela [Serviços por Executante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113153) para o Produto e o Serviço informados. Quando algum destes for modificado, a lista de Executantes será recarregada para os executantes que possuem permissão para execução do Serviço e Produto em questão. Caso não exista executante configurado, o campo será bloqueado e será exibida a mensagem:

**"Não é possível utilizar este executante para o produto e serviço selecionados"**

Localizado à frente do campo **"Problema"**, você identificará o ícone ![Imagem 5: Localizado à frente do campo "Problema" , você identificará o ícone que, ao ser acionado, apresentará a descrição…](https://ajuda.sankhya.com.br/hc/article_attachments/15470297316119) que, ao ser acionado, apresentará a descrição padrão para os problemas de OS, que é configurado através do parâmetro **"Texto padrão para problema da OS - SERVTEXTPROB"**.

O campo **"Origem"** é alimentado da seguinte maneira: se o parâmetro **"Códigos das Origens padrões da OS - ORIGEMPADOS"** estiver preenchido com os códigos das origens de atendimento padrão (Por exemplo: 300000,600000), o campo será preenchido com as descrições dos atendimentos padrão de código 300000 e 600000.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#abalan%C3%A7amento) 

**Sub-aba Anexos**

Nesta aba, você realiza a inclusão de anexos referentes ao atendimento. Estes arquivos serão anexados à OS que será criada quando clicar no botão Salvar.

![Imagem 6: Nesta aba, você realiza a inclusão de anexos referentes ao atendimento. Estes arquivos serão anexados à OS que será…](https://ajuda.sankhya.com.br/hc/article_attachments/9300790777879)

Na parte superior da aba, são exibidos três botões:

![Imagem 7: Adicionar um novo anexo;](https://ajuda.sankhya.com.br/hc/article_attachments/9300913590679) Adicionar um novo anexo;

![Imagem 8: Excluir um anexo;](https://ajuda.sankhya.com.br/hc/article_attachments/9300888999831) Excluir um anexo;

![Imagem 9: Editar um anexo já adicionado.](https://ajuda.sankhya.com.br/hc/article_attachments/9300889000727) Editar um anexo já adicionado.

Ao clicar no botão para Adicionar um Arquivo, será aberta a seguinte tela:

![Imagem 10: Ao clicar no botão para Adicionar um Arquivo , será aberta a seguinte tela:](https://ajuda.sankhya.com.br/hc/article_attachments/9300829642007)

Ao informar os dados básicos do anexo e clicar em Salvar, o registro será adicionado à grade.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#abalan%C3%A7amento) 

**Sub-aba Histórico**

Na aba Histórico, podem ser consultadas as Ordens de Serviço lançadas para o Parceiro selecionado na aba [Consulta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#abaconsulta). A Ordens de Serviço serão carregadas na grade e ordenadas pelo seu número de forma decrescente, ou seja, da mais recente, para a mais antiga. Você pode ainda, filtrar as Ordens de Serviço dentro de um determinado período, somente as que encontram-se pendentes, ou pelo problema da OS.

![Imagem 11: Na aba Histórico , podem ser consultadas as Ordens de Serviço lançadas para o Parceiro selecionado na aba Consulta . A…](https://ajuda.sankhya.com.br/hc/article_attachments/9301177220375)

O filtro inicial é alimentado considerando 30 (trinta) dias anteriores até o dia atual.

Caso sejam apresentadas nesta grade diversas Ordens de Serviço que contenham mais de um item, a marcação **"Agrupar por Ordem de Serviço"**, quando realizada, unirá estas OS's de numeração equivalente.

Clicando em uma das linhas da grade, será aberta a tela [Ordem de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603834-Ordem-de-Servi%C3%A7o), apresentando a Ordem de Serviço selecionada.

O botão **"Exibir histórico" ![Imagem 12: O botão "Exibir histórico" , quando acionado, permite a visualização do histórico da Ordem de Serviço selecionada na…](https://ajuda.sankhya.com.br/hc/article_attachments/9300932972951)**, quando acionado, permite a visualização do histórico da Ordem de Serviço selecionada na grade.

Ao clicar no botão **"Salvar"**, caso nenhum campo possua algum valor inválido, será gerada uma Ordem de Serviço para o atendimento, sendo apresentada a seguinte mensagem:

**"O atendimento foi registrado com sucesso. OS: X".**

Clicando no botão **"Abrir OS"**, a tela Ordem de Serviço será aberta apresentando a Ordem de Serviço gerada. Ao clicar no botão **"Fechar"**, a mensagem será fechada e será feito um reposicionamento para a aba Consulta, permitindo o registro de um novo atendimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#top)

## Parâmetros que influenciam esta rotina

No parâmetro **"Lista de grupos de serviços para lançamento no registro de atendimento - GRUSERVREGATEND"**, informe os grupos cujos serviços poderão ser apresentados na tela Registro de Atendimento. Estes grupos devem ser informados separando-os por vírgula (200100, 200200, 200300); caso nenhum grupo seja informado, todos os serviços que estão ligados à natureza do contrato serão apresentados, ou seja, o comportamento normal se mantém.

Informe no parâmetro **"Período para consulta de OS's - PERIOCONSULOS"** a quantidade de dias que serão respeitados pelo sistema para que este analise as ocorrências registradas e, assim, selecione o valor mais utilizado.

Preencha o parâmetro **"Serviço padrão para registro de atendimento - SERVICOPADRAO"** com o serviço padrão a ser utilizado nos Registros de Atendimento. Quando o serviço padrão informado não está disponível para o Parceiro da OS, será apresentado o primeiro serviço da lista.

Especifique no parâmetro **"Status padrão OS - STATUSPADOS"** o código do status da OS que será considerado como padrão para o Registro de Atendimento. Deverá ser preenchido com o código de um **"Status"** cadastrado na tela [Status OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604954).

Informe no parâmetro **"Status padrão Sub-OS - STATUSPADSUBOS"** o código de um Status Sub-OS cadastrado na tela [Status Sub-OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604894).

Em relação ao parâmetro **"Códigos das Origens padrões da OS - ORIGEMPADOS"**, este deverá ser preenchido com os códigos das origens que foram cadastrados previamente na tela [Origem de Atendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604294).

**Observações:**

- Se nenhum código de origem for informado no parâmetro, o sistema retornará todas as origens no campo **"Origem"** da tela Registro de Atendimento.
- Se for informado algum código, serão apresentadas apenas as origens cujos códigos foram informados no parâmetro.
- Caso seja informado algum código que não esteja cadastrado, o sistema não apresentará o código errado.

Habilitando o parâmetro **"Prioridade automática no Registro de Atendimento - REGATENDPRIAUTO"** e preenchendo os campos **"Impacto"** e **"Urgência"**, fará com que estes preencham, de maneira automática, o campo **"Prioridade"**.

Os campos adicionais inseridos no parâmetro **"Campos adicionais p/ Registro de Atendimento - REGATENDCAMPAD"** serão exibidos na grade do painel **"Campos disponíveis"** do pop-up **"Configuração do Formulário"** localizado no botão ![configuração](https://ajuda.sankhya.com.br/hc/article_attachments/15470297322391) da aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#abalanamento) desta tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604454-Registro-de-Atendimento#top)
