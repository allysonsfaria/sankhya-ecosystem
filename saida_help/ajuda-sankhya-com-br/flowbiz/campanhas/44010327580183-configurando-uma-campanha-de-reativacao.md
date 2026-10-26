---
id: "44010327580183"
titulo: "Configurando uma campanha de Reativação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010327580183-Configurando-uma-campanha-de-Reativa%C3%A7%C3%A3o"
trilha: "Flowbiz > Campanhas"
atualizado_em: "2026-10-05T18:36:09Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_10", "sync_hash_1f91dd00a506"]
---

# Configurando uma campanha de Reativação

Neste artigo vamos ajudá-lo a implementar uma **estratégia Reativação para clientes que não compram há muito tempo**.

Nesta estratégia vamos **configurar duas campanhas recorrentes**:

1. Uma para clientes cujo último pedido foi há mais de 1 ano;
2. Outra para clientes cujo último pedido foi entre 6 e 12 meses;

A ideia aqui é oferecer um cupom de desconto mais agressivo para usuários que não compram há mais de 12 meses e um cupom de desconto menos agressivo para usuários que não compram há mais de 6 meses, utilizando em ambas as campanhas a temática **“Estamos com saudades”.**

A primeira coisa que precisamos para isso é criar esses **dois segmentos na lista de clientes**. Para isso, siga o caminho abaixo:

## Listas > Clientes > Segmentos > Criar Segmento

![Imagem 1: Utilize as seguintes regras:](https://ajuda.sankhya.com.br/hc/article_attachments/44010374736023)Utilize as seguintes regras:

“**Último pedido - STATUS”** é pago

“**Último pedido - DATA**” é há mais de 6 meses

“**Último pedido - DATA**” é nos últimos 12 meses

![Imagem 2: “ Último pedido - DATA ” é nos últimos 12 meses](https://ajuda.sankhya.com.br/hc/article_attachments/44010375096599)

O segmento de usuários cujo último pedido foi há mais de 1 ano já está criado por padrão na sua lista com o nome [REATIVAÇÃO] Mais de 1 ano sem pedidos pagos.

Com os segmentos escolhidos, **agora você precisa criar a campanha.**

Para isso, vá no **menu superior em “campanhas” > E-mail** **> “Criar campanha de e-mail”** e **selecione o segmento que acabou de criar como destinatário**.

Avance e siga o mesmo processo que você já conhece para criar o layout da sua campanha. Quando a campanha estiver criada e revisada, avance até a parte do **agendamento e escolha a opção de “agendar envio recorrente”.**

Para essa estratégia, o ideal é que você **utilize a recorrência mensal.** Para isso, **selecione a opção “personalizar dias do mês”** e escolha o dia e hora em que ela será enviada.

![Imagem 3: Para essa estratégia, o ideal é que você utilize a recorrência mensal. Para isso, selecione a opção “personalizar dias…](https://ajuda.sankhya.com.br/hc/article_attachments/44010375381143)

**Sugestão:** Você pode configurar a campanha com o maior desconto para ser enviada todo dia 20 para os clientes que não compram há mais de 12 meses e a campanha com menor desconto todo dia 5 para clientes que não compram entre 6 e 12 meses.
Você também pode incluir o segmento de [REATIVAÇÃO] Sem pedidos cadastrados em ambas as campanhas.

Feito isso é só clicar em “salvar” que sua campanha estará configurada.
Todas as suas recorrências vão aparecer no menu campanhas em “agendadas".
**Observação**: utilize um padrão de nomenclatura para as suas campanhas recorrentes para facilitar a gestão e análise dos resultados no menu Analytics posteriormente, diferenciando essas campanhas das campanhas pontuais.

## Exemplo: CRM / TEMÁTICA / SEGMENTO

Existem várias maneiras de se criar uma campanha de Reativação. Essa é apenas uma sugestão. Caso queira explorar outras maneiras, chame seu analista se precisar de ajuda via WhatsApp 51 9790-9718\*
