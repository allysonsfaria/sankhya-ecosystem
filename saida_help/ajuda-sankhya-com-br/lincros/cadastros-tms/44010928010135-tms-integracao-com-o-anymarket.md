---
id: "44010928010135"
titulo: "[TMS] Integração com o Anymarket"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010928010135--TMS-Integra%C3%A7%C3%A3o-com-o-Anymarket"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:50:02Z"
rotulos: ["sync_hc", "lincros", "lincros_13438893", "sync_hash_ecf563c432c3"]
---

# [TMS] Integração com o Anymarket

**Contexto:**
O Anymarket é um HUB de integração que permite integrações como: ERP, plataformas de venda online, marketplaces, soluções logísticas, soluções de precificação, conciliação, entre tantas outras integrações.

Por ser um integrador o Anymarket possibilita aos nossos clientes realizarem vendas em mais de 60 marketplaces, como por exemplo, Mercado Livre, Amazon, Shopee.

Esta integração permite que o cálculo de frete seja solicitado diretamente no site de compras online, na sequência, esta solicitação chega ao TMS e ele retorna a plataforma oferecendo as melhores opções de preço e prazo ao cliente que está realizando a compra. Além disso, após o fechamento da venda, o pedido faturado é enviado ao TMS fazendo uso desta integração, e a partir disso o TMS realiza a ordem de coleta para o transportador responsável pela entrega. Para completar, através de um link aberto o TMS alimenta a plataforma de vendas online contendo cada ocorrência relacionada a entrega, até que a encomenda chegue no destinatário que realizou a compra.

---

## Como configurar:

Basta executar alguns passos, para que os pedidos faturados através das plataformas de e-commerce e marketplace disponíveis no Anymarket, sejam enviados ao Lincros TMS.

## Passo 1

- O primeiro passo é solicitar sua licença Anymarket junto a um consultor Lincros. Na sequência, nosso consultor fará a configuração inicial junto ao seu consultor Anymarket inserindo algumas informações importantes para a integração funcionar. Para isso, tenha o contato de seu consultor Anymarket.

## Passo 2

- Cadastrar dois marcadores para o Anymarket, um para o tipo de negociação normal, e um para o tipo expressa. Para saber mais sobre marcadores [acesse este artigo](https://intercom.help/ajudalincros/pt-BR/articles/13438934-tms-como-cadastrar-marcadores).

  - O Anymarket apresenta ao cliente que está realizando a compra online, dois tipos de frete, um deles é o tipo normal e o outro é o tipo expresso, para que essas opções de frete sejam exibidas na plataforma, é obrigatório que você configure os marcadores e então vincule os marcadores às tabelas de frete.

## Passo 3

- Adicionar os respectivos marcadores nas tabelas de frete correspondentes. Saiba mais sobre o cadastro de tabelas de frete [clique aqui](https://intercom.help/ajudalincros/pt-BR/articles/13432703-tms-cadastro-de-tabela-de-fretes-via-tela-do-sistema).

  - Para que a busca funcione corretamente, a tabela precisa possuir apenas UM dos marcadores, conforme negociação com a transportadora, NORMAL ou EXPRESSA.
- O marcador deve ser colocado em todas as tabelas que podem atender a negociação do Anymarket.

## Passo 4

- Possuir o cadastro de CEP de origem da unidade utilizada pelo Anymarket para realizar a consulta. Para saber como cadastrar o CEP de origem [clique aqui](https://intercom.help/ajudalincros/pt-BR/articles/13432599-tms-cadastro-de-parametros-de-unidade).

  - Para que o valor do frete calculado no TMS seja enviado à loja virtual através do Anymarket, são necessárias as informações de: faixas de peso, origem e destino condizente com o frete. Para isso é necessário cadastrar o CEP do Centro de Distribuição de onde o produto será despachado como sendo a origem do frete. O destino será o endereço com CEP cadastrado pelo comprador da loja online no momento da compra.

**Importante:** É fundamental que o ambiente Anymarket integrado às plataformas de e-commerce e marketplace esteja ativo e funcionando, com todos os produtos devidamente cadastrados. Todo este processo é feito com o auxílio da equipe de suporte da Anymarket.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
