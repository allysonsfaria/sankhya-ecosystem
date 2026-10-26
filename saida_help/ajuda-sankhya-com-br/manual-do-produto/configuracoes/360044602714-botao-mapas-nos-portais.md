---
id: "360044602714"
titulo: "Botão 'Mapas' nos portais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:52:48Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Parceiro", "Rota", "Botão 'Mapas' nos portais", "Distância", "LIBERAMAPGOOGLE", "Rota para endereço de entrega", "Rota para endereço do parceiro", "Visualizador de mapas", "Botão 'Mapas' nos portais manual", "Endereço de Entrega", "Mapas", "Endereços", "Botão ‘Mapas’ nos Portais: Explorando Localizações e Rotas", "Google Maps"]
---

# Botão 'Mapas' nos portais

O Sankhya-Om dispõe de um recurso de Mapas para análise da localização do endereço do parceiro, ou seja, o endereço principal e o endereço de entrega, como também as rotas do endereço da empresa referente ao endereço principal/entrega do parceiro.

Assim, trataremos nesse artigo sobre os seguintes tópicos:

[Opções do Botão Mapas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#opesdobotomapas)                           

[Como configurar o Botão Mapas ao Google Maps](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#comoconfigurarobotomapasaogooglemaps)

[Múltiplos Endereços de Entrega para o mesmo Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#mltiplosendereosdeentregaparaomesmoparceiro)    

### Opções do Botão Mapas

O botão **"Mapas"** poderá apresentar opções de acordo com a necessidade e finalidade da tela em que o mesmo estiver presente. As telas onde o botão está presente são as seguintes:

- Nas [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), serão exibidas todas as opções;
- Na tela de [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), estarão disponíveis apenas as opções **"Endereço de entrega"** e **"Endereço"**;
- Na tela de [Formação de carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga), não será apresentada nenhuma opção, porém ao clicar no botão Mapas é aberto o Google Maps exibindo os endereços dos Parceiros que constituírem a Ordem de carga.

Abaixo trataremos da descrição das opções mencionadas acima:

**Endereço de entrega:** Esta opção abrirá a tela **"Mapa Visualizador de Endereços"** e trará em um ponto o endereço de entrega do parceiro. Este endereço é visualizado no mapa por um marcador **"P"** com a cor **vermelha**.

**Endereço do parceiro:** Através desta opção será aberta a tela Mapa Visualizador de Endereços e trará em um ponto o endereço principal do parceiro. Este endereço é visualizado no mapa por um marcador **"P"** com a cor **vermelha**.

**Rota para endereço de entrega:** A tela Mapa Visualizador de Endereços será aberta e trará dois pontos no mapa, um com o endereço de entrega do parceiro, e outro com o endereço da empresa (também selecionado na nota), o endereço da empresa é representado por um marcador maior, na cor **azul** e que contem uma estrela. O sistema gerará uma rota de um endereço para o outro, na barra lateral é possível visualizar o endereço dos dois pontos, e também a distância entre os pontos. A origem é o endereço da empresa e destino é o endereço de entrega do parceiro.

**Rota para endereço do parceiro:** Esta opção abrirá a tela Mapa Visualizador de Endereços e trará dois pontos no mapa, um com o endereço do parceiro, e outro com o endereço da empresa (também selecionado na nota). O endereço da empresa é representado por um marcador maior, na cor **azul** e que contem uma estrela. O sistema gerará uma rota de um endereço para o outro, na barra lateral é possível visualizar o endereço dos dois pontos, e também a distância entre os pontos. A origem se refere ao endereço da empresa e destino corresponde ao endereço do parceiro.

**Importante:** a tela só é populada após o mapa ser carregado. Isso só ocorre se houver conexão com a internet. Caso você tente visualizar o endereço/rota e não tenha acesso a internet o sistema não conseguirá localizar o endereço e poderá ficar apresentando um pop-up com a mensagem **"...Carregando"** até que a conexão com a internet seja estabelecida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#top)

### Como configurar o Botão Mapas ao Google Maps

Para o funcionamento do Mapa integrado com a ferramenta [Google Maps](https://www.google.com.br/maps), é fundamental seguir os seguintes passos:

- Efetue o preenchimento do parâmetro **"Chave para mapas do sistema - CHAVEGOOGLEMAP"** com a API KEY (chave de acesso) que o Google fornece;
- Para gerar a API KEY é necessário acessar o link [Geração da API KEY](https://developers.google.com/maps/documentation/javascript/get-api-key);
- Depois, realize o login com uma conta Google;
- Após esses passos, clique na opção **"Obter uma chave"**;
- Informe um nome para o projeto e clique em **"Create and Enable API"**, para que a chave gerada seja exibida na tela.

Ao finalizar esses procedimentos, copie a chave e insira no parâmetro. Depois, refaça o login no sistema e abra novamente a tela, dessa forma, ela estará pronta para uso.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#top)

### Múltiplos Endereços de Entrega para o mesmo Parceiro

Para utilizar outros endereços de entrega além do endereço de entrega do parceiro, existe o parâmetro **"Usa endereço de entrega dos contatos - USENDENTREGA"**, que quando habilitado mostrará na aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaendereo) da tela de **"Cadastro de Parceiros"** a marcação **"Utiliza endereço de entrega do contato"**.

Ao lançar um pedido ou nota de venda e informar um parceiro que esteja com a marcação Utiliza endereço de entrega do contato assinalada, o sistema irá validar para que seja informado um contato com endereço preenchido no cabeçalho da nota.

- Se o parceiro tiver um contato cadastrado, mas o mesmo não tiver endereço preenchido, o sistema não irá aceitar e emitirá a seguinte mensagem:

**"Contato não tem endereço preenchido"**.

- Se o campo Utiliza endereço de entrega do contato estiver marcado, mas o parceiro não possuir um contato cadastrado, o sistema não aceitará salvar o pedido/nota e emitirá a seguinte mensagem:

**"É obrigatório informar o contato do parceiro para entrega"**.

**Observação:** mesmo com o parâmetro USENDENTREGA ligado, ao utilizar o botão Mapas, o endereço exibido para o Parceiro continuará sendo o endereço principal.

Para que os campos de endereço de contato possam ser utilizados, foram criadas as variáveis abaixo. As mesmas serão utilizadas no modelo txt do campo **"Observação"** da NF-e, que é onde o endereço do contato será impresso.

- **enderecont:** retorna o endereço do contato;
- **baicont:** retorna o bairro do contato;
- **cidadecont:** retorna a cidade do contato;
- **estadocont:** retorna o estado do contato;
- **cepcont:** retorna o CEP do contato.

Na tela de [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga), o botão **"Outras opções"** apresenta a opção **Visualizar endereços/Endereços/Contato**, que se habilitada mostrará o endereço do contato das notas (da mesma forma que ocorre para as outras opções deste mesmo menu).

Sendo assim, será impresso na nota no campo Observação, o endereço de entrega do contato e na tela de Formação de Carga você poderá montar as suas cargas baseadas no endereço do contato.

**Importante:** não é possível alterar o endereço principal na nota porque o governo não permite que um parceiro tenha mais de um endereço. Por isso, o endereço do contato será apresentado nos dados adicionais da nota.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#top)
