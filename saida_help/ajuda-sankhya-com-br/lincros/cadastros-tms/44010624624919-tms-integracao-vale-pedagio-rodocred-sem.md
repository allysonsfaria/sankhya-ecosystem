---
id: "44010624624919"
titulo: "[TMS] Integração Vale-Pedágio Rodocred/Sem Parar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010624624919--TMS-Integra%C3%A7%C3%A3o-Vale-Ped%C3%A1gio-Rodocred-Sem-Parar"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:42:24Z"
rotulos: ["sync_hc", "lincros", "lincros_13438889", "sync_hash_33bcfe40f0e6"]
---

# [TMS] Integração Vale-Pedágio Rodocred/Sem Parar

## Contexto:

Essa funcionalidade permite realizar a cotação de todos os pedágios presentes em uma determinada rota melhorando a previsibilidade dos custos ao cliente e permitindo o pagamento antecipado do pedágio. Na prática, será liberado um novo botão na tela de embarque, o "Calcular pedágio".

Este botão fará a cotação de todos os pedágios presentes na rota determinada, inclusive sequenciado, levando em conta até mesmo a quantidade de eixos do veículo, trazendo mais assertividade sobre os valores a serem pagos ao transportador.

Ela é destinada a empresas que se enquadrem na lei nº 10.209, de 23 de março de 2001, que institui o Vale Pedágio Obrigatório (VPO).

---

## Pré-requisitos:

- Utilizar o serviço Rodocred/Sem Parar

---

## Instruções:

## 1º Passo:

- O primeiro passo é solicitar sua licença de pedágio junto a um consultor Lincros.
- Na sequência, nosso consultor fará a configuração inicial junto ao seu consultor Rodocred inserindo algumas informações importantes para a integração funcionar. Tenha o contato de seu consultor Rodocred e informe a forma de pagamento à transportadora, se é via Cupom ou Via TAG.

## 2º Passo:

- Verificar e/ou cadastrar os grupos de veículo e [veículos](https://intercom.help/ajudalincros/pt-BR/articles/13432717-tms-cadastro-de-veiculo) que serão utilizados para o transporte.
- O cadastro do grupo de veículos é feito através do menu: Cadastros Gerais > Transportadoras > Veículos > Grupos
- Para que o cálculo ocorra corretamente é obrigatório o preenchimento dos eixos e da rodagem.

![Imagem 1: Para que o cálculo ocorra corretamente é obrigatório o preenchimento dos eixos e da rodagem.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1964976706/4583659ebe0bc07937a45d7a9ad7/566F8DA6FE7CF2DE350B66E4885A74E0?expires=1791331200&signature=80892806c50e4ab7ce4d86cbb9ef54aa024e39608735f5635d68e988d55175e4&req=dSkhEsB5m4ZfX%2FMW3nq%2BgVTYaLbmnb681zOe87KgrVanZfmn97TzcU51qqns%0ADd%2BvkgGdejQl6pEOy8fpmhV89ds%3D%0A)

![Imagem 2: Para que o cálculo ocorra corretamente é obrigatório o preenchimento dos eixos e da rodagem.](https://ajuda.sankhya.com.br/hc/article_attachments/44010625033367)

![Imagem 3: Para que o cálculo ocorra corretamente é obrigatório o preenchimento dos eixos e da rodagem.](https://ajuda.sankhya.com.br/hc/article_attachments/44010649995415)

- Rodagem simples: tem um pneu em cada ponta do eixo e pode suportar até 6 toneladas de carga.
- Rodagem dupla: possuem dois pneus em cada ponta, sendo que esse tipo de eixo pode aguentar até 10 toneladas.

## 3º Passo:

- Possuir o [embarque](https://intercom.help/ajudalincros/pt-BR/articles/13439330-tms-como-funciona-o-embarque-no-tms-tabela-de-frete) criado. O cálculo do pedágio é o último passo da criação do embarque, portanto ele deve estar já com todos os documentos, definição de transportadora, definição do veículo, etc. Com o embarque criado, basta clicar em "Calcular pedágio"

- O **Valor pedágio** e o **ID Rota** serão exibidos na área de **Pedágio** da tela de Edição de embarque.
- O valor do pedágio será apresentado como um componente de cálculo da tabela de frete, nas movimentações do embarque com nome 'VPO' e descrição 'Vale pedágio obrigatório'. O valor não será somado ao valor cálculo do frete.

![Imagem 4: O valor do pedágio será apresentado como um componente de cálculo da tabela de frete, nas movimentações do embarque com…](https://ajuda.sankhya.com.br/hc/article_attachments/44010639297815)

- **IMPORTANTE:** O cálculo do pedágio **não é o mesmo** que a compra do vale pedágio. A compra só será efetuada ao confirmar o embarque.

## 4º Passo:

- Para **efetivar a compra**, é necessário realizar a confirmação do Embarque. Após todos os trâmites realizados e definidos para o transportador sair com mercadoria, é necessário confirmar o embarque para realizar a compra do pedágio. Para isso o usuário deve possuir permissão de confirmação de pedágio.
- **IMPORTANTE:** A partir do momento que o usuário clicar sobre botão 'Confirmar', não será possível retirar documentos, ou alterar dados de origem e destino, placa e motorista do embarque.
- Para garantir que a compra foi feita com sucesso, o campo "Comprovante pedágio" deve estar preenchido.

![Imagem 5: Para garantir que a compra foi feita com sucesso, o campo "Comprovante pedágio" deve estar preenchido.](https://ajuda.sankhya.com.br/hc/article_attachments/44010650429207)

- Caso o embarque tenha sido confirmado, mas o campo de comprovante de pedágio estiver em branco, a opção de "Reprocessar" será apresentada. O usuário precisa reprocessar o pedágio para que o campo de comprovante seja preenchido e a compra efetivamente seja realizada.

![Imagem 6: Caso o embarque tenha sido confirmado, mas o campo de comprovante de pedágio estiver em branco, a opção de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010650561431)

- Como não é possível editar um embarque já confirmado, em caso de necessidade de alteração, o embarque precisa ser cancelado para realizar o estorno da compra, e é necessário criar um novo embarque. A Rodocred tem um prazo de 3hrs para cancelar o pedágio.
- A Rodocred pode rejeitar o cancelamento da compra. Se o cancelamento for rejeitado, será criada uma [pendência](https://intercom.help/ajudalincros/pt-BR/articles/13433311-tms-painel-de-aprovacoes) do tipo "Rejeição da compra de pedágio". A pendência poderá ser resolvida pelo [usuário com permissão](https://intercom.help/ajudalincros/pt-BR/articles/13439012-tms-como-configurar-a-alcada-de-aprovacao).

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
