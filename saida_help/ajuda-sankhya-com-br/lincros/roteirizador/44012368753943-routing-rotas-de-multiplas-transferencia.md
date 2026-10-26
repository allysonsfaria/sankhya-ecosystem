---
id: "44012368753943"
titulo: "[Routing] - Rotas de Múltiplas Transferências entre Depósitos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012368753943--Routing-Rotas-de-M%C3%BAltiplas-Transfer%C3%AAncias-entre-Dep%C3%B3sitos"
trilha: "Lincros > Roteirizador"
atualizado_em: "2026-10-05T19:26:17Z"
rotulos: ["sync_hc", "lincros", "sync_hash_64e5cd2fe5f3", "lincros_13433783"]
---

# [Routing] - Rotas de Múltiplas Transferências entre Depósitos

**Menu:
1. Parametrização:**Cadastros > Depósitos > Parâmetros**2. Cadastro:** Cadastros > Ponto de apoio > Novo/Editar**3. Roteirização:**Roteirizador > Roteirizar > Iniciar Uma Nova Sessão

## Objetivo

Criar rotas de transferência de pedidos entre depósitos, através da criação de rotas dentro de uma sessão de roteirização, de forma simples.

## Considerações:

- Possuir um ponto de apoio cadastrado, com as mesmas informações do deposito que receberá as transferências;
- Ter permissão de Manager/Administrador para ativação de parâmetros (parâmetros informados logo abaixo);
- Possuir integração com o TMS, para importação de Notas / Pré-Notas Fiscais.
- O uso de um token de autenticação é indispensável. Caso ainda não possua um, solicite ao suporte da Lincros para gerar o token.

**Observação:** Antes de seguirmos com as configurações de múltiplas transferências, é importante ressaltar que esse processo abrange apenas depósitos que possuem integração entre as plataformas TMS e Routing, para a roteirização de Notas/Pré-Notas Fiscais.

**1. Parâmetros para habilitar**

Deposito:

- Programação de múltiplas transferências (Cadastros> Depósito> Parâmetros (engrenagem)> Parâmetros Gerais.

![Imagem 1: Programação de múltiplas transferências (Cadastros> Depósito> Parâmetros (engrenagem)> Parâmetros Gerais.](https://ajuda.sankhya.com.br/hc/article_attachments/44012339039255)

(**Nota:** Este parâmetro precisa estar habilitado no depósitos de origem e destino da transferência, para que seja possível visualizar os campos Unidade e Depósito de Redespacho no cadastro de Ponto de Apoio.)

**Quem possui acesso aos parâmetros?**

Para ativar os parâmetros dentro do cadastro de deposito, é importante certificar-se de que seu usuário possui o perfil Administrador/Manager.

**2. Cadastro:**Primeiramente, é necessário cadastrar um ponto de apoio no depósito de origem, com as mesmas informações de endereço do depósito de destino das transferências. Esse ponto de apoio representará o local para onde os pedidos serão transferidos.

**Caminho:**Cadastros > Ponto de apoio > Novo/Editar

![Imagem 2: 2. Cadastro: Primeiramente, é necessário cadastrar um ponto de apoio no depósito de origem, com as mesmas informações…](https://ajuda.sankhya.com.br/hc/article_attachments/44012339179671)

- **Unidade :** No campo 'Unidade', deve-se informar a unidade do depósito de destino.
- **Depósito de Redespacho :** Neste campo, é importante selecionar o depósito de destino das transferências, lembrando que apenas os depósitos com o parâmetro 'Programação de Múltiplas Transferências' habilitado serão listados.

## 3. Roteirização:

Com os parâmetros devidamente ativos e atribuídos à Unidade e ao Depósito de Redespacho no ponto de apoio, vamos prosseguir com a consolidação do processo dentro da sessão de roteirização. Para isso, é necessário iniciar uma nova sessão de roteirização (para saber como iniciar uma nova sessão, [clique aqui](https://lincros.movidesk.com/kb/pt-br/article/210140/routing-iniciar-uma-nova-sessao-de-roteirizacao?ticketId=&q=)) com os pedidos que serão transferidos para outro depósito. Após a criação da sessão, seguimos para a etapa de criação da rota.

**Como criar a rota de transferência entre depósitos:**

O processo de criação das rotas consiste em três passos. Antes de iniciar, para acessar a tela de Programação de Transferências, é necessário selecionar o ícone cinza localizado na lateral esquerda da tela da sessão.
 

![Imagem 3: O processo de criação das rotas consiste em três passos. Antes de iniciar, para acessar a tela de Programação de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012351093911)

1. Ao selecionar essa nova opção, a tela de Programação de Múltiplas Transferências será aberta, inicialmente exibindo os pedidos da sessão que você deseja transferir.

   ![Imagem 4: Ao selecionar essa nova opção, a tela de Programação de Múltiplas Transferências será aberta, inicialmente exibindo os…](https://ajuda.sankhya.com.br/hc/article_attachments/44012339453207)

   (**Nota:** É possível visualizar na parte inferior desta tela uma 'linha do tempo' com as etapas a serem seguidas.)
2. Com os pedidos selecionados, clique em ‘Avançar’, na parte inferior da tela;
3. Neste passo, é necessário selecionar um ou mais pontos de apoio, que serão utilizados para as coletas e para onde os pedidos serão destinados.;

   **( Nota:** No sequenciamento, o depósito de saída será sempre o primeiro na ordem, seguido pelas unidades onde as coletas serão realizadas, e o último ponto de apoio será o destino dos pedidos.)

   ![Imagem 5: Neste passo, é necessário selecionar um ou mais pontos de apoio, que serão utilizados para as coletas e para onde os…](https://ajuda.sankhya.com.br/hc/article_attachments/44012327534103)
4. Após selecionar os pontos de apoio, é hora de definir o veículo que será utilizado para transportar os pedidos até o destino.

   ![Imagem 6: Após selecionar os pontos de apoio, é hora de definir o veículo que será utilizado para transportar os pedidos até o…](https://ajuda.sankhya.com.br/hc/article_attachments/44012339651223)
5. Selecione a opção 'Confirmar' para que, com base nas informações selecionadas, a rota seja criada.

Deste modo a rota é criada na sessão:

![Imagem 7: Deste modo a rota é criada na sessão:](https://ajuda.sankhya.com.br/hc/article_attachments/44012369916439)

**Exportar Sessão**

Para consolidar a transferência de pedidos para o depósito de destino, é necessário exportar a sessão. Abaixo seguem os passos a serem seguidos:

1. Na lateral esquerda da tela da sessão de roteirização, é importante selecionar a opção 'Exportar Sessão';

   ![Imagem 8: Na lateral esquerda da tela da sessão de roteirização, é importante selecionar a opção 'Exportar Sessão';](https://ajuda.sankhya.com.br/hc/article_attachments/44012339975575)
2. A tela exibirá a aba para seleção do sistema 'Routing – Rotas de Transferência', sendo esta a única opção a ser utilizada para transferências de pedidos entre depósitos;

   ![Imagem 9: A tela exibirá a aba para seleção do sistema 'Routing – Rotas de Transferência', sendo esta a única opção a ser…](https://ajuda.sankhya.com.br/hc/article_attachments/44012322706071)

**Para confirmar se a transferência foi realizada, siga os passos abaixo:**

1. Na tela inicial do Roteirizador, acessar a aba 'Pedidos'.
2. Selecionar o depósito de destino, e informe o número de pedido (se houver mais de um, separe-os por vírgula) ou utilize a data dos pedidos.
3. Em seguida, selecione a opção 'Filtrar'.

 'Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos'
