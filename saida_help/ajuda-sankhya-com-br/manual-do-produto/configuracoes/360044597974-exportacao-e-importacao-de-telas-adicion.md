---
id: "360044597974"
titulo: "Exportação e Importação de Telas Adicionais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:58Z"
rotulos: ["Exportação e Importação de Telas Adicionais", "Exportação e Importação de Telas Adicionais manual", "Importação", "Personalização", "Exportação e Importação de Funcionalidades no Sankhya Om", "Plataforma", "Exportacao", "Módulo"]
---

# Exportação e Importação de Telas Adicionais

O Sankhya Om dispõe do recurso que possibilita compartilhar funcionalidades adicionais entre ambientes diferentes, como telas e os menus/pastas necessários para lançá-las, criados diretamente no sistema através das telas [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas) e [Menu do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112053-Menu-do-Sistema-).

Dentre o conjunto de funcionalidades delas, temos o Módulo Adicional onde você pode, por exemplo, criar os cadastros na base de produção em uma base alternativa e aprimorá-los conforme testes e ao final, exportar tudo no formato de um módulo e importar diretamente no servidor. Ou ainda, compartilhar esse módulo entre vários clientes, sem a necessidade de criar tudo novamente.

---

![Imagem 1: A documentação a seguir, trata somente os processos de importação e exportação de módulo, a criação das telas e menus…](https://ajuda.sankhya.com.br/hc/article_attachments/16245336146967) A documentação a seguir, trata somente os processos de importação e exportação de módulo, a criação das telas e menus devem ser visualizados na documentação das telas [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773) e [Menu do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112053).

---

Dessa forma, nesse artigo trataremos da [Exportação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#exporta%C3%A7%C3%A3o) e [Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#importa%C3%A7%C3%A3o) de uma tela adicional, a [Exportação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#exporta%C3%A7%C3%A3odem%C3%B3dulo) e [Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#importa%C3%A7%C3%A3odem%C3%B3dulo) de um módulo, além do [Merge de Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#mergedeimporta%C3%A7%C3%A3o) de módulos.

## Exportação de um tela adicional

Em [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas), a opção **"Exportar Metadados"** estará disponível no botão ![Imagem 2: Em Construtor de Telas , a opção " Exportar Metadados" estará disponível no botão "Outras Opções..." , somente se…](https://ajuda.sankhya.com.br/hc/article_attachments/16245336149655) **"Outras Opções..."**, somente se houver uma tabela selecionada na grade. Assim, ao ser acionada, um arquivo será gerado com todas as informações necessárias para criar essa tabela.

**Observação:** outras tabelas adicionais que tenham relacionamento com a tabela em questão, também serão automaticamente incorporadas.

Todas as ações da tabela selecionada e de outras que possuem relacionamento com ela, serão exportadas. Além disso, caso haja alguma ação do tipo Rotina Java, o arquivo **.zip** gerado terá uma pasta para cada módulo cadastrado na tela Módulo Java e os arquivos **.jar** estarão dentro destas pastas. Na sequência, informe um local onde esse arquivo será gravado.

**Nota:** quando comprar uma solução pelo Place e esta for protegida, não será possível efetuar a exportação dos metadados. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#top)

## Importação de uma tela adicional

Ainda no Construtor de Telas, por meio da opção **"Importar Metadados"**, também do botão Outras Opções..., o sistema interpretará o arquivo de exportação, e dessa forma, criará todas as tabelas, ações e módulos java presentes nele.

Ao selecionar essa opção, uma tela será aberta para definição do arquivo **.zip** previamente exportado.

---

Pode ser que, ocorram determinados conflitos, mas o sistema possui uma maneira de trata-los, e com seu auxílio é possível definir o que o sistema deverá realizar nesses casos. Observe:

- **Conflito de módulo Java**

Esse conflito ocorrerá caso já exista o módulo Java cadastrado na base, o sistema dará 3 opções a você: **"Adicionar arquivos ausentes"**, **"Não alterar o Módulo Java"** e **"Trocar os arquivos do módulo"**, de forma que, ao selecionar determinada opção, o sistema mostrará abaixo e em vermelho a descrição do que esta opção fará. Observe:

- **Conflito de Rotina de banco de dados**

Esse conflito ocorrerá caso exista alguma rotina de banco de dados que utilize uma procedure já existente no banco de dados. Logo, você terá duas opções, sendo elas a de **"Não alterar a procedure"** e **"Atualizar a procedure"**. Ao selecionar uma delas, é possível ver, em vermelho, a sua descrição.

**Observação:** no caso de re-importação, diferentemente dos Módulos Java e das Rotinas de Banco de dados, o sistema não gera conflito e não atualiza automaticamente as ações em JavaScript. Para atualizá-las, será necessário que você realize a exclusão manual das ações para que quando houver a re-importação, o sistema inclua as ações em JavaScript atualizadas.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#top)

## Exportação do módulo

Um Módulo adicional nada mais é do que uma ou mais telas adicionais, menus, e pastas que podem ser abertas no sistema. A exportação dos módulos é efetuada na tela [Menu do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112053-Menu-do-Sistema-).

Dessa forma, inicialmente, escolha um menu que esteja no painel **"Menu Ativo"**, e em seguida, clique no botão ![Imagem 3: Dessa forma, inicialmente, escolha um menu que esteja no painel "Menu Ativo" , e em seguida, clique no botão "Exportar…](https://ajuda.sankhya.com.br/hc/article_attachments/4411445393943) **"Exportar módulo"**.

**Nota:** para exportar ou importar um módulo, o sistema necessita estar rodando com uma licença que contenha o opcional Plataforma de Personalização/W.

O sistema analisa todas as subpastas do item selecionado para buscar menus que abram telas adicionais. Todas as telas encontradas serão exportadas inclusive com a estrutura de menu necessária para lançar essas telas, e ao final, é exibido um resumo do que foi exportado.

Você poderá notar que foi exportada inclusive uma Trigger vinculada à tabela **"AD\_FILME"**. Isso porque durante a exportação, o sistema encontrou essa trigger definida diretamente no Banco de dados. Ao clicar no botão **"Baixar arquivo"** e em seguida escolher o local apropriado para salvar o mesmo, o processo de exportação é finalizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#top)

## Importação de módulo

O processo de importação do módulo é tão simples quanto os demais. De forma que, ao clicar no botão ![Imagem 4: O processo de importação do módulo é tão simples quanto os demais. De forma que, ao clicar no botão "Importar módulo" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4411455632279) **"Importar módulo"**, serão solicitadas duas informações: o **"sufixo"** para as tabelas, sendo ele opcional, e o local onde deve ser incluída a estrutura de menus. 

![Imagem 5: O processo de importação do módulo é tão simples quanto os demais. De forma que, ao clicar no botão "Importar módulo" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4411447546135)

Assim, ao optar pela opção **"Importar diretamente na raiz"**, a estrutura será colocada no primeiro nível dos módulos exibidos. Se houver uma pasta selecionada dentre os módulos.

É possível ainda, anexar a nova estrutura a partir desse ponto, usando a opção **"Importar na pasta selecionada"**.

Quando o botão **"Selecionar arquivo"** for acionado, o arquivo previamente exportado deve ser selecionado, de modo a enviar essas informações para a criação do módulo. Depois desse processo, um resumo da importação é exibido.

**Nota:** existe uma trigger para a tabela AD\_FILME, o arquivo usado nessa importação foi obtido em um ambiente SQLServer e estamos importando esse módulo em um ambiente Oracle.  Como esse tipo de recurso é incompatível de um Banco de dados para outro, a trigger foi ignorada na importação e o aviso no topo da janela deixa essa informação explícita, além da linha aparecer na cor vermelha. Nesse caso, a conversão da trigger deve ser feita manualmente e incorporada ao Banco de dados, caso contrário, o funcionamento do módulo ficará comprometido ou incompleto. Isso também acontecerá para as Procedures, se houver alguma Ação do tipo Rotina de Banco de Dados. Neste caso, a ação será criada, mas a procedure não será criada no banco, o cadastro da ação ficará conforme figura abaixo, sendo necessário clicar no botão destacado para criar o template da procedure, ou cadastrá-la diretamente no banco. Todo o restante dos recursos importados funcionará perfeitamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#top)

## Merge de Importação de Módulos

Pode-se ainda, realizar alterações no módulo adicional existente, ou exportá-lo e importá-lo novamente. Quando isso ocorrer, o sistema irá manter o que não foi alterado e apenas irá atualizar aquilo que estiver diferente. Dessa forma, observe os exemplos a seguir:

**Exemplo 1:**

Temos em uma base, um módulo chamado CINEMA, e esse módulo possui vários itens, os quais estão com descrições incorretas ou que precisam de alteração. Sendo assim, você poderá alterar todas as descrições, exportar o módulo normalmente e importá-lo, por exemplo, em outra base que já tenha o módulo Cinema. Quando este for importado, nada do que não foi alterado sofrerá modificações e o que estiver diferente será modificado.

**Exemplo 2:**

Isso também é válido para alterações realizadas via trigger's, por exemplo: no módulo CINEMA, temos uma tela adicional chamada **"**Cadastro de Filmes**"** e você, como usuário do sistema deseja bloquear inclusões nessa tela. Para isso, foi criada a seguinte trigger no banco ORCL:

| ```  CREATE OR REPLACE TRIGGER TESTEJAVA.TRG_AD_FILMES  BEFORE INSERT ON AD_FILMES FOR EACH ROW  BEGIN    RAISE_APPLICATION_ERROR(-20101, 'Inclusão bloqueada pela trigger');   END;  / ``` |
| --- |

Porém, se você desejar exportar esse novo bloqueio para outras bases às quais também possuem o módulo de CINEMA, basta exportar o módulo alterado e importá-lo nas demais bases. Quando fizer a importação do módulo novamente, a trigger será criada, e consequentemente o bloqueio às inclusões na tela ocorrerá, e as demais funcionalidades/telas/campos que o módulo já possuía e não foram alteradas, serão mantidas.

Teremos ainda, determinadas validações, sendo estas:

Na tela Menu do Sistema, caso solicite a importação de um módulo já existente (idêntico ao que existe/sem alterações), o sistema o importará normalmente, mas não realizará nenhuma alteração e nem apresentará a mensagem que ele já existe no sistema.

Se a importação for solicitada de um módulo já existente (idêntico ao que existe/sem alterações), em alguma outra pasta diferente da que ele existe, o sistema não permitirá sua inclusão e irá emitir a mensagem:

**"Este módulo já foi importado na pasta raiz. Para atualizá-lo selecione o mesmo local ou remova os menus anteriores."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais#top)
