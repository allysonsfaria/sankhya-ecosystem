---
id: "44011090229399"
titulo: "[Routing] - Vale Pedágio Repom"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011090229399--Routing-Vale-Ped%C3%A1gio-Repom"
trilha: "Lincros > Roteirizador"
atualizado_em: "2026-10-05T18:55:23Z"
rotulos: ["sync_hc", "lincros", "lincros_13439506", "sync_hash_2d19317b6f87"]
---

# [Routing] - Vale Pedágio Repom

**Menu**: Roteirizador> Iniciar uma nova sessão> Vale Pedágio

**Objetivo**: Orientar como utilizar o vale pedágio Repom no Roteirizador

**Considerações**: 
              - A compra de vale pedágio deve ser efetuada somente quando a rota estiver exportada;
              - A Repom tem limitação de informar no máximo 23 pedágios em uma única rota;
              - Por padrão, a Repom permite o cancelamento da compra por TAG dentro de 15 minutos após confirmação da compra. Mais detalhes contactar o suporte da Repom.

**PARÂMETROS:**
Para utilização da compra do Vale Pedágio Repom os **parâmetros** abaixo são obrigatórios:
  1. Parâmetro integrador, **Caminho**: Cadastros > Depósitos> Parâmetros do depósito> Parâmetros Gerais> I**ntegrador vale-pedágio**. (Habilita as funcionalidades do integrador vale pedágio Repom).

  2. Parâmetro pedágio OSM (acesso Manager - para habilitar essa opção, solicitar ao suporte Lincros). Caminho: Cadastros> Depósitos> Parâmetros do depósito> Parâmetros de Geolocalização> **Usar pedágio do OSM**. (Habilitar o tráfego de pedágios OSM para a definição da viagem na plataforma Repom).

**CADASTROS:**
Além dos parâmetros informados, há alguns **cadastros** necessários para ocorrer a integração de vale pedágio. Confira os cadastros necessários:
  1. Cadastro do **CNPJ** no Depósito. Caminho: Cadastros> Depósito> Editar> Informar o **CNPJ Depósito**(Informar somente os números), esse dado é importante para a emissão da compra do vale pedágio. Esse CNPJ deve estar configurado no sistema da Repom para considerá-lo como válido.

  2. Cadastro do **integrador vale pedágio**. Caminho: Cadastros> Integrador Vale Pedágio> Novo / Editar. Todos os campos são obrigatórios. Os dados serão informados todos pela Repom. Esse cadastro garantirá a integração entre as plataformas Repom e Routing. Os dados de preenchimentos são:
 
Plataforma roteiro:
  \* URL autenticação;
  \* Usuário;
  \* Senha;
  \* Grant type;
  \* URL criar rota;
  \* URL consultar valor pedágio;
  
Plataforma viagem:
  \* URL autenticação;
  \* Usuário;
  \* Senha;
  \* URL comprar vale pedágio;
  \* URL cancelar compra.

  3. Cadastro de **tipo de veículo** através do caminho: Cadastros> Tipos de veículos> Editar / Novo. Para ocorrer a integração do pedágio é necessário selecionar a classificação do veículo **Caminhão** (outras classificações não devem integrar o vale pedágio).
Neste cadastro de tipo de veículo também se faz necessário informar corretamente a **Quantidade de Eixos** (o preenchimento desse campo é utilizado pela Repom para calcular o pedágio, o preenchimento incorreto acarretará falhas na emissão do vale pedágio).

  4. Cadastro de **veículo**, caminho: Cadastros> Veículos> Editar / Novo. No cadastro de veículo alguns ajustes são necessários também para compor o valor do pedágio.
Cadastro obrigatório:
  \* **Sair do depósito/ponto de apoio no início das entregas/coletas** - essa opção obrigatoriamente deve ser marcada, porque define se a origem da partida é do depósito ou ponto de apoio.
  \* **Transportadora**: campo obrigatório, associa a transportadora responsável pela entrega.
Cadastro facultativo:
  \* **Volta para o depósito/ponto de apoio no término das entregas/coletas** - define se o destino de retorno é o depósito ou ponto de apoio, não marcando essa opção, a rota encerra após a última atividade.

  5. Cadastro de **motorista**. Caminho: Cadastros> Motoristas> Editar / Novo. Os dados a serem preenchidos nesse cadastro são:
  \* Documento: Informar o número do documento do motorista (cadastro facultativo);
  \* Número do cartão - essa opção só aparece se os parâmetros informados anteriormente estiverem ativos (cadastro facultativo).
**Observação:** Caso o motorista use somente TAG não é necessário informar no sistema, pois essa informação deve estar cadastrada diretamente no sistema de vale pedágio Repom. Caso o motorista possua cartão e TAG, será priorizado a TAG para a efetivação da compra do vale pedágio Repom (Este comportamento é padrão da Repom).

  6. Cadastro de **transportadora**, caminho: Cadastros> Transportadoras> Editar / Novo. Se faz necessário o cadastro da transportadora com o Nome e CNPJ correto da transportadora, esses dados são obrigatórios para integração com o sistema Repom.

Aqui finalizamos toda a parte de parametrização e cadastros. Com todos os passos anteriores devidamente preenchidos, é hora de realizar a compra de vale pedágio. Vamos ao que interessa então, a compra de vale pedágio ocorre quando é finalizado uma rota e ou sessão, então sem mais delongas vamos ao passo-a-passo.

  1. Iniciar uma nova sessão (Dúvidas de como proceder? Segue artigo, [clique aqui](https://lincros.movidesk.com/kb/pt-br/article/210140/routing-iniciar-uma-nova-sessao-de-roteirizacao?ticketId=&q=));
  2. Após criar as rotas é possível consultar, comprar ou cancelar o vale pedágio, para isso é necessário localizar na lateral esquerda o símbolo do vale-pedágio:

![Imagem 1: Considerações : - A compra de vale pedágio deve ser efetuada somente quando a rota estiver exportada; - A Repom tem…](https://ajuda.sankhya.com.br/hc/article_attachments/44011094990743)

  3. Clicando no vale-pedágio uma janela é exibida, nessa janela haverá algumas informações e opções, sendo elas:
  \* As rotas criadas, é possível selecionar uma ou mais rotas;
  \* Na parte inferior da janela há a opção "**Consultar valor vale pedágio**", essa opção pode ser consultada a qualquer momento durante o processo de roteirização, é necessário selecionar ao menos uma rota para realizar a consulta do valor de vale pedágio. Quando é feito a consulta é retornado o valor caso seja calculado com sucesso, ou a crítica no campo "**Mensagem integrador"** em caso de não ocorrer a consulta;

![Imagem 2: 3. Clicando no vale-pedágio uma janela é exibida, nessa janela haverá algumas informações e opções, sendo elas: * As…](https://ajuda.sankhya.com.br/hc/article_attachments/44011095113623)

  \* Na mesma janela há a opção "**Comprar vale pedágio**", a compra de vale pedágio só pode ocorrer quando a rota e/ou sessão estiver com status de exportada, antes disso, é possível clicar na opção, mas o retorno gerado em tela será: **Rota ainda não exportada**.

Com a rota exportada, ao clicar na opção "**Comprar vale pedágio**" é feito a comunicação com a Repom, o vale pedágio é comprado e disponibilizado ao motorista informado na rota:

![Imagem 3: * Na mesma janela há a opção " Comprar vale pedágio ", a compra de vale pedágio só pode ocorrer quando a rota e/ou…](https://ajuda.sankhya.com.br/hc/article_attachments/44011113722391)

  \* A opção "**Cancelar vale pedágio**" deve ser usada somente após a compra do vale pedágio, e há um prazo de 15 minutos para cancelamento junto à Repom (mais informações contactar a Repom).

![Imagem 4: * A opção " Cancelar vale pedágio " deve ser usada somente após a compra do vale pedágio, e há um prazo de 15 minutos…](https://ajuda.sankhya.com.br/hc/article_attachments/44011090881943)

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
