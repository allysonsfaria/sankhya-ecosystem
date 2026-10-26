---
id: "44013341232151"
titulo: "[TMS] - Cadastro de Regiões"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013341232151--TMS-Cadastro-de-Regi%C3%B5es"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:54:12Z"
rotulos: ["sync_hc", "lincros", "lincros_13432697", "sync_hash_549491c3af33"]
---

# [TMS] - Cadastro de Regiões

**Menu**: Cadastros Gerais > Transportadoras > Negociações > Regiões

**Objetivo:** Realizar o cadastro de regiões dentro da Plataforma. As regiões são utilizadas para o cadastro de rotas e é um dos elementos necessários para a criação de uma tabela de frete.

## Considerações:

- É necessário ter a transportadora em questão cadastrada no sistema;

Abaixo segue os procedimentosNa tela de regiões, podemos encontrar o ID da localização, a transportadora, a descrição da região,  a latitude e longitude da região atendida.

Ainda é possível exportar uma região, importar via planilha, e exportar um modelo de planilha de regiões.

![Imagem 1: Ainda é possível exportar uma região, importar via planilha, e exportar um modelo de planilha de regiões.](https://ajuda.sankhya.com.br/hc/article_attachments/44013304918295)

Ao clicar em uma região da tela, é aberto a página de edição de região, onde é possível consultar quais localidades pertencem àquela região e alterar as informações da mesma conforme necessário. Na tela inicial é possível criar uma nova região.

Existem duas maneiras de criar uma região na Plataforma. O processo pode ser feito de forma unitária, ou em massa.

## Cadastro Unitário (Via Plataforma):

Selecionar o botão Novo:

![Imagem 2: Selecionar o botão Novo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013341481239)

- **ID Localização**: É preenchido automaticamente após a região ser salva;
- **Transportadora**: Transportadora à qual a região é válida;
- **Região**: Nome da região;
- **Latitude**: Latitude da região
- **Longitude**: Longitude da região
- **Localização**: É onde adicionam-se as localizações pertencentes àquela região. Podem ser faixas de CEP, cidades, estados ou outras regiões. Ao selecionar a localização, é possível clicar no ícone de + (mais) para adicionar a localização à região, ou clicar no ícone de - (menos) para restringir aquela localização na região. Essa opção de tornar restrita é útil para otimizar o processo de cadastro de regiões e pode ser utilizada onde há exceção de faixas de CEP ou em regiões do país. Um exemplo:

Para ilustrar, vamos imaginar que determinada transportadora divide seu atendimento no estado de São Paulo em duas regiões distintas: “SP Região Metropolitana” e “SP Interior”. Após cadastrar a região “SP Reg. Metropolitana” (que contempla 10 cidades, por exemplo), esta pode ser usada como restrição ao cadastrar a região “SP – Interior”, não sendo necessário informar uma a uma as demais cidades do estado.

- **Adicionar Cidades:** Permite adicionar todas as cidades de um determinado estado ou região. É uma opção útil para o caso de você precisar de muitas cidades desse estado, e preferir remover algumas, ao invés de adicionar uma grande quantidade, ou até o estado inteiro. Um exemplo:

Digamos que uma determinada transportadora atende apenas a região “SP Interior”, e que essa região não contempla apenas 10 cidades. Basta selecionar o estado de São Paulo, ativar a flag Adicionar Cidades, adicionar todas as cidades do estado de São Paulo e depois remover apenas as 10 cidades que não fazem parte da região.

Para utilizar, selecionar como localização o estado ou a localização desejada, e antes de clicar em mais ou menos, manter a flag ativa;

- **Ativo**: Informa se a região está ativa ou não.

## Cadastro das regiões Via Planilha de excel

É possível criar o cadastro em massa de regiões através da utilização de uma planilha. Para tanto, basta clicar em 'Modelo' na tela de Regiões. Um download irá iniciar automaticamente:

![Imagem 3: É possível criar o cadastro em massa de regiões através da utilização de uma planilha. Para tanto, basta clicar em…](https://ajuda.sankhya.com.br/hc/article_attachments/44013312373655)

Na tabela, as seguintes abas estarão disponíveis:

- **Regiões**: É onde você preenche o nome das regiões que deseja criar, informa o CNPJ da transportadora à qual aquela região se refere e informa se a região é ativa ou não;
- **Localizações Atendidas**: É onde será preenchida a localidade de cada região mencionada na aba anterior. Importante lembrar que  uma localidade pode ser um intervalo de CEPs (Para um bairro, por exemplo), uma cidade, um estado ou uma outra região. É necessário escolher apenas uma das opções de localidade por planilha;
- **Restrições**: Onde serão preenchidas as localidades não atendidas por determinada região;
- **Códigos IBGE**: É um glossário contendo o código de todas as cidades do Brasil. Pode ser utilizado como base para a inserção dos mesmos na tabela;
- **Siglas UF**: Siglas de todos os estados do Brasil;
- **Exemplo Regiões**: Exemplo de preenchimento da aba de Regiões;
- **Exemplo Localizações Atendidas**: Exemplo de preenchimento da aba de Localizações Atendidas;
- **Exemplo Restrições**: Exemplo de preenchimento da aba de Restrições.

## Exemplo de como realizar o cadastro das regiões via planilha utilizando 'Regiões':

- ## Aba 'Regiões'

![Imagem 4: Aba 'Regiões'](https://ajuda.sankhya.com.br/hc/article_attachments/44013312514711)

- ## Aba 'Localizacoes\_atendidas'

![Imagem 5: Aba 'Localizacoes_atendidas'](https://ajuda.sankhya.com.br/hc/article_attachments/44013312631063)

## Exemplo do Cadastro no sistema após a importação

![Imagem 6: Exemplo do Cadastro no sistema após a importação](https://ajuda.sankhya.com.br/hc/article_attachments/44013312760983)

## Exemplo de como realizar o cadastro das regiões via planilha utilizando 'Faixas de CEP', a aba 'Regiões' fica como o exemplo acima:

![Imagem 7: Exemplo de como realizar o cadastro das regiões via planilha utilizando 'Faixas de CEP', a aba 'Regiões' fica como o…](https://ajuda.sankhya.com.br/hc/article_attachments/44013305761431)

## Exemplo do Cadastro no sistema após a importação

![Imagem 8: Exemplo do Cadastro no sistema após a importação](https://ajuda.sankhya.com.br/hc/article_attachments/44013313014423)

Feito o preenchimento da planilha, basta importá-la clicando em Importar na tela inicial de Regiões:

![Imagem 9: Feito o preenchimento da planilha, basta importá-la clicando em Importar na tela inicial de Regiões:](https://ajuda.sankhya.com.br/hc/article_attachments/44013297437591)

Após adicionar o arquivo, basta clicar em upload e aguardar a importação. Por fim, o Resultado da importação será preenchido automaticamente, informando, dentre outras coisas, a quantidade de linhas com erro, caso hajam. Abaixo do Resultado de importação é possível visualizar a Relação de ocorrências, que tratam-se de uma descrição mais detalhada dos erros encontrados durante a importação da planilha.

## Alteração de Regiões em Massa (Via Planilha)

Da mesma forma que é possível importar para a Plataforma regiões completamente novas, é possível alterar via planilha as regiões já criadas. Para tanto, basta selecionar a opção exportar em excel. A Plataforma irá solicitar um e-mail e uma planilha contendo as regiões selecionadas será enviada para o e-mail informado. Basta fazer o download dessa planilha, realizar as alterações desejadas, salvar as modificações e em seguida importá-la novamente para a Plataforma.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
