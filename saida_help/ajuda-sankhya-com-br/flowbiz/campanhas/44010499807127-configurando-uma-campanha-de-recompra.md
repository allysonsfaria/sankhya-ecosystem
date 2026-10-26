---
id: "44010499807127"
titulo: "Configurando uma campanha de Recompra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010499807127-Configurando-uma-campanha-de-Recompra"
trilha: "Flowbiz > Campanhas"
atualizado_em: "2026-10-05T18:39:18Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_16", "sync_hash_4d2eeda9d583"]
---

# Configurando uma campanha de Recompra

Neste artigo vamos ajudá-lo a implementar uma **estratégia de recompra para produtos que são consumidos em um determinado tempo.**

A ideia aqui é criar uma **campanha recorrente de lembrete** (possivelmente oferecendo um cupom de desconto para antecipar a próxima compra, reduzindo o tempo médio de recompra desse produto).

- Vamos utilizar como **exemplo uma loja de suplementos que vende Whey protein de 2Kg**, partindo do pressuposto que esse produto será **consumido em uma média de 3 meses**. Para isso, vamos configurar uma campanha para ser enviada a partir do segundo mês depois da compra desse produto, com a temática “**Seu whey protein está acabando**”, para impactá-lo todo mês enquanto não fizer uma nova compra.

Assim, a primeira coisa que precisamos é **criar o segmento que vamos utilizar.** Para isso, no **menu superior clique em > listas > clientes > vá em segmentos > “criar novo segmento”.**

![Imagem 1: Assim, a primeira coisa que precisamos é criar o segmento que vamos utilizar. Para isso, no menu superior clique em >…](https://ajuda.sankhya.com.br/hc/article_attachments/44010515988759)

Vamos utilizar a seguinte regra:

- **“Último pedido - STATUS”** é “pago”
- **“Último pedido - DATA”** é “há mais de 2 meses)
- **“Último pedido - PRODUTO”** contém “Whey Protein 2Kg”

![Imagem 2: “Último pedido - PRODUTO” contém “Whey Protein 2Kg”](https://ajuda.sankhya.com.br/hc/article_attachments/44010500367255)

**Observação**:

- Para a segmentação funcionar, é importante que o produto que estamos utilizando esteja cadastrado na sua plataforma de e-commerce com o nome correto. Caso precise de ajuda para ver o formato dos dados de cada campo, fale com o seu analista.
- Para este tipo de campanha, você pode utilizar tanto o campo Último pedido - PRODUTO quanto o campo Último pedido - CATEGORIA, dependendo do nível de abrangência da sua estratégia.

Com o segmento salvo, **agora você precisa criar a campanha.**

Para isso, vá no **menu superior em “campanhas” > "E-mail" > “Criar campanha de e-mail”** e selecione o segmento que acabou de criar como destinatário. Avance e siga o mesmo processo que você já conhece para criar o layout da sua campanha. Quando a campanha estiver criada e revisada, avance até a parte do agendamento e escolha a opção de **“agendar envio recorrente”.**

Para essa estratégia, o ideal é que você utilize a recorrência mensal. Para isso, **selecione a opção “personalizar dias do mês” e escolha o dia e hora em que ela será enviada.**

![Imagem 3: Para essa estratégia, o ideal é que você utilize a recorrência mensal. Para isso, selecione a opção “personalizar dias…](https://ajuda.sankhya.com.br/hc/article_attachments/44010509285143)

Feito isso é só clicar em “salvar” que sua campanha estará configurada.

Todas as suas recorrências vão aparecer no menu campanhas em “**agendadas**”.

## Observação

- Utilize um padrão de nomenclatura para as suas campanhas recorrentes para facilitar a gestão e análise dos resultados no menu Analytics posteriormente, diferenciando essas campanhas das campanhas pontuais. Exemplo: CRM / TEMÁTICA / SEGMENTO

\*Existem várias maneiras de se criar uma campanha de Recompra. Essa é apenas uma sugestão. Caso queira explorar outras maneiras, chame seu analista se precisar de ajuda.
