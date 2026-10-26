---
id: "44012103980823"
titulo: "[Tracking] - Cross-Docking"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012103980823--Tracking-Cross-Docking"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T19:20:09Z"
rotulos: ["sync_hc", "lincros", "sync_hash_5e66a6642aec", "lincros_13434542"]
---

# [Tracking] - Cross-Docking

**Menu**: Tracking> Cross-Docking 

**Objetivo**: Explicar como utilizar a tela de Cross-Docking no Tracking.

**Considerações**: Para configurar o Cross-Docking, é necessário que o usuário tenha permissão de cadastro nos módulos: Unidade de Negócio, Transportadoras, Veículos, Motoristas e Usuários.

                            Para usar essa funcionalidade, é necessário importar uma rota de Cross-Docking no Tracking.

O que é uma Rota de Cross-Docking?

No Tracking, é possível enviar rotas de Cross-Docking, mas o que isso significa?

Uma rota de Cross-Docking é uma rota que inclui uma entrega (representada por um bolinha com a seta na parte superior) contendo vários documentos e/ou pedidos destinados a diferentes destinatários finais, que são entregues a uma transportadora. Essas rotas podem ter mais de uma parada, incluindo transportadores ou pontos de apoio, além de poder incluir entregas diretas aos clientes finais.

**Exemplo**: Uma rota pode incluir entregas diretas para clientes finais e entregas destinadas a uma transportadora para posterior distribuição.

![Imagem 1: Exemplo : Uma rota pode incluir entregas diretas para clientes finais e entregas destinadas a uma transportadora para…](https://ajuda.sankhya.com.br/hc/article_attachments/44012133526551)

**Configuração do Cross-Docking no Tracking**
Para que os transportadores utilizem a funcionalidade de Cross-Docking no Tracking, é necessário realizar os seguintes cadastros:

   º **Unidade de Negócio:** Cadastre a Unidade de Negócio com o mesmo código do campo "Código Negócio do Cliente" (O CNPJ é de preenchimento obrigatório).

![Imagem 2: º Unidade de Negócio: Cadastre a Unidade de Negócio com o mesmo código do campo "Código Negócio do Cliente" (O CNPJ é…](https://ajuda.sankhya.com.br/hc/article_attachments/44012087736727)

Caminho: Tracking > Cadastros > Unidades de Negócio.

   º **Depósito**: Após criar a Unidade de Negócio, é necessário cadastrar um depósito vinculado a ela.

Caminho: Tracking > Cadastros > Depósitos.

   º **Cadastrar uma Transportadora:** Registre a transportadora (O CNPJ é de preenchimento obrigatório).Caminho: Tracking > Cadastros > Transportadoras.

   º **Cadastrar um Usuário para o Transportador:** Para que o transportador acesse o Tracking, crie um usuário vinculado ao perfil 'Transportadora'.

Caminho: Tracking > Cadastros > Usuários.

   º **Cadastrar Veículos:** Associe os veículos à Unidade de Negócio e à Transportadora.

Caminho: Tracking > Cadastros > Veículos.

   º **Cadastrar Motoristas:** Associe os motoristas aos respectivos veículos, à Unidade de Negócio e à Transportadora..

Caminho: Tracking > Cadastros > Motoristas.

(**Nota:** O CNPJ informado no cadastro da Unidade de Negócio e da Transportadora deve ser o mesmo, obrigatoriamente.)

Após realizar esses cadastros, a funcionalidade de Cross-Docking estará disponível no menu lateral do Tracking.

![Imagem 3: Após realizar esses cadastros, a funcionalidade de Cross-Docking estará disponível no menu lateral do Tracking.](https://ajuda.sankhya.com.br/hc/article_attachments/44012151481751)

**Como Criar uma Rota de Cross-Docking**Na tela de Cross-Docking, serão exibidas todas as notas fiscais relacionadas às rotas de Cross-Docking destinadas à transportadora. Nessa tela, você pode filtrar as notas por Unidade de Negócio, Cliente e Cidade. Veja como criar uma rota:

1. Selecionar as notas desejadas;
2. Clique em 'Criar Rota';
3. Na janela que abrir, informe a Unidade de Negócio, Data da rota, Veículo e Motorista.
4. Ajuste a data e hora de previsão de entrega para cada entrega individualmente, se necessário, e altere a sequência das entregas. Após os ajustes, clique em 'Criar Rota'.

A rota será criada e exibida na tela de monitoramento, seguindo o fluxo do Tracking.

**Observação:**
O Cross-Docking no Tracking permite monitorar as duas etapas do processo:

**º Primeira etapa:** saída da carga fracionada destinada a vários clientes e entregue a uma transportadora.
   **º Segunda etapa:** a transportadora cria uma nova rota para entregar aos clientes finais.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
