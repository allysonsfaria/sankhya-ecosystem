---
id: "360044603214"
titulo: "Parâmetros Personalizáveis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603214-Par%C3%A2metros-Personaliz%C3%A1veis"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:53:20Z"
rotulos: ["Configuração", "Pesquisa", "Veículos", "Apresentação", "Busca", "Nome da Tabela", "Parâmetros Personalizáveis", "Parâmetros Personalizáveis manual", "Dicionário de Dados", "Parâmetros", "Preferências", "Parametrização de Senhas de Acesso ao Sistema", "Comercial"]
---

# Parâmetros Personalizáveis

O Sankhya Om dispõe de recursos através dos quais você poderá configurar os botões de pesquisa, para facilitar a busca e o preenchimento dos campos. São parâmetros personalizáveis, os apresentados a seguir:

#### Busca Personalizada nos Botões de Pesquisa

Você deverá criar um parâmetro na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), formado pelo prefixo **"BUSCA"**.**"NOME DA TABELA"**, onde em Nome da Tabela você deverá informar o nome da tabela desejada, ou seja, indique uma personalização da busca por qualquer tabela, por exemplo: **"BUSCA.TGFVEI"**, indica a preferência na tabela Veículos.

Trouxemos um exemplo:

Nos Portais e nas Centrais, a busca padrão de Veículos é fixa, pré-determinada por Marca Modelo.

Ao digitar um caractere na descrição do botão de pesquisa do campo "Veículos", como por exemplo **"P"**, e clicar na lupa, o sistema apresentará todos os veículos com a Marca Modelo iniciados por P.

Suponhamos que para você, seja mais interessante pesquisar o veículo não pela Marca e Modelo e sim pela Placa; você deverá, portanto, acessar a tela de Preferências e cadastrar o novo parâmetro da seguinte forma:

Após clicar no botão![Imagem 1: Após clicar no botão :](https://ajuda.sankhya.com.br/hc/article_attachments/16695122140183):

- Informe no campo **"Chave"** a expressão BUSCA.TGFVEI;
- Preencha o campo **"Descrição"** com **"Campo de Busca Automática de Veículo"**(sem as aspas);
- No campo **"Módulos do Sistema"** escolha a opção **"Comercial"**;
- Em **"Menu"** selecione a opção **"Diversas"**;
- No campo **"Aba"** informe **"Diversas"**;
- No campo **"Tipo"** selecione a opção **"Texto"** e, por fim;
- No campo **"Texto"**, informe o nome do campo que fará parte da pesquisa, ou seja, **"PLACA"**, conforme demostramos na imagem abaixo:

![Imagem 2: No campo "Texto" , informe o nome do campo que fará parte da pesquisa, ou seja, " PLACA" , conforme demostramos na…](https://ajuda.sankhya.com.br/hc/article_attachments/360087062633)

Após a configuração do parâmetro, o resultado da busca apresenta as placas dos veículos.

#### Apresentação Personalizada Nos Botões de Pesquisa

O parâmetro **"APRES"."NOME DA TABELA"** permite a apresentação de campos adicionais criados em qualquer tabela.

Na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados), é possível a criação de campos a partir da soma de dois ou mais campos.

Trouxemos um exemplo:

Suponhamos que você deseja preencher no campo Veículo, além da Marca e Modelo, também a Placa do Veículo. No Dicionário de Dados, você deve selecionar a tabela TGFVEI, criar o campo **"Descrição"** (o nome do campo não deve existir na tabela), efetuar as marcações **"Visível no grid de pesquisa"** e **"Campo Calculado"** (esta última devido à não existência do campo DESCRICAO no banco de dados), inserir a expressão: return com.sankhya.util.StringUtils.getNullAsEmpty($col\_MARCAMODELO) + " [" + com.sankhya.util.StringUtils.getNullAsEmpty($col\_PLACA) + "]"; e salvar.

Após isto, no botão **"Outras Opções"**, reinicie os dados desta unidade para que o campo seja reconhecido pelo Sankhya Om:

[GIF animado: Imagem 3: Após isto, no botão "Outras Opções" , reinicie os dados desta unidade para que o campo seja reconhecido pelo Sankhya Om…](https://ajuda.sankhya.com.br/hc/article_attachments/360087064313)

Logo em seguida, na tela de Preferências, realize a seguinte configuração:

Adicione o parâmetro com a Chave APRES.TGFVEI;

No campo **"Descrição"**, informe **"Campo de Apresentação do Veículo"**;

Em **"Módulos do Sistema"** escolha o módulo **"Comercial"**;

Nos campos **"Menu"** e **"Aba"** informe **"Diversas"**;

No campo **"Tipo"** escolha a opção **"Texto"** e, por fim, informe no campo **"Texto"** o nome do campo que, no caso, é **"DESCRICAO"**:

![Imagem 4: No campo "Tipo" escolha a opção "Texto" e, por fim, informe no campo "Texto" o nome do campo que, no caso, é…](https://ajuda.sankhya.com.br/hc/article_attachments/360085871174)

Após isto, nas Centrais de Notas, além da Marca, também será exibido no campo **"Veículo"**, a Placa do mesmo.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603214-Par%C3%A2metros-Personaliz%C3%A1veis#top)
