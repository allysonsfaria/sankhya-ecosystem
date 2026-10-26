---
id: "44010530587543"
titulo: "Configurando uma campanha de Cross sell"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010530587543-Configurando-uma-campanha-de-Cross-sell"
trilha: "Flowbiz > Campanhas"
atualizado_em: "2026-10-05T18:39:33Z"
rotulos: ["sync_hc", "flowbiz", "sync_hash_79b0a2d9bbc0", "flowbiz_17"]
---

# Configurando uma campanha de Cross sell

Neste artigo vamos ajudá-lo a implementar uma **estratégia de cross sell para usuários que não compraram um determinado produto ou categoria no último pedido.**

A ideia da campanha é apresentar o produto/categoria para o cliente, seus benefícios e/ou diferenciais, podendo trazer um cupom de desconto para incentivar a compra.

Para isso, vamos utilizar **como exemplo uma loja de moda que quer incentivar a compra da categoria de “Jaquetas”.**

A primeira coisa que vamos precisar é **criar o segmento de quem no último pedido não comprou jaquetas**.

- No menu superior acesse sua **lista de clientes**, vá em **segmentos** e clique em **“criar novo segmento”**.

![Imagem 1: No menu superior acesse sua lista de clientes , vá em segmentos e clique em “criar novo segmento” .](https://ajuda.sankhya.com.br/hc/article_attachments/44010517674263)

Para isso, vamos utilizar a seguinte regra:

**“Último pedido - STATUS”** é **“pago”**

**“Último pedido - PRODUTO”** não contém **“Jaqueta”**

![Imagem 2: “Último pedido - PRODUTO” não contém “Jaqueta”](https://ajuda.sankhya.com.br/hc/article_attachments/44010486060695)

## Observações:

- Para a segmentação funcionar, é importante que o produto que estamos utilizando esteja cadastrado na sua plataforma de e-commerce com o nome correto. Caso precise de ajuda para ver o formato dos dados de cada campo, fale com o seu analista.
- Para este tipo de campanha, você pode utilizar tanto o campo Último pedido - PRODUTO quanto o campo Último pedido - CATEGORIA, dependendo de como estão gravados os dados na sua plataforma de e-commerce ou da abrangência da sua estratégia.

Com o segmento salvo, agora **precisamos criar a campanha.**

Para isso, **vá no menu superior em “campanhas” > "E-mail" > “Criar campanha de e-mail”** e selecione o segmento que acabou de criar como destinatário. Avance e siga o mesmo processo que você já conhece para criar o layout da sua campanha. Quando a campanha estiver criada e revisada, avance até a parte do agendamento e escolha a opção **“agendar envio recorrente”.**

Para essa estratégia, o ideal é que você utilize a recorrência mensal. Para isso, selecione a opção **"Personalizar dia do mês”** e escolha o dia e hora em que ela será enviada.

![Imagem 3: Para essa estratégia, o ideal é que você utilize a recorrência mensal. Para isso, selecione a opção "Personalizar dia…](https://ajuda.sankhya.com.br/hc/article_attachments/44010486278551)

Feito isso é só clicar em “salvar” que sua campanha estará configurada.

Todas as suas recorrências vão aparecer no menu campanhas em “**agendadas**”.

**Observação**: utilize um padrão de nomenclatura para as suas campanhas recorrentes para facilitar a gestão e análise dos resultados no menu Analytics posteriormente, diferenciando essas campanhas das campanhas pontuais. Exemplo: CRM / TEMÁTICA / SEGMENTO

\*Existem várias maneiras de se criar uma campanha de cross sell. Essa é apenas uma sugestão. Caso queira explorar outras maneiras, chame seu analista se precisar de ajuda.
