---
id: "360044603094"
titulo: "Edição do Número de Lote"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603094-Edi%C3%A7%C3%A3o-do-N%C3%BAmero-de-Lote"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:51:49Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Edição do Número de Lote manual", "Lote", "Ordem de Produção", "Produção", "Manufatura", "br.com.sankhya.producao.rotina.OrdemProducao", "Terceirização fabricação produtos", "Editar lote produção", "Restrições e configuração"]
---

# Edição do Número de Lote

É comum que algumas indústrias optem por terceirizar a fabricação integral de seus produtos. Como o processo produtivo é realizado em outra indústria, ocorre que algumas informações de manufatura são geradas/controladas pela fábrica terceira como, por exemplo, o número de lote, data de fabricação e data de validade dos produtos.

Com o objetivo de atender essa necessidade, o módulo Produção/W conta com uma funcionalidade denominada Editar Lote que permite a realização da edição tardia do lote, ou seja, a edição após o lançamento da ordem, do número de lote, data de fabricação e data de validade dos produtos produzidos na ordem de produção, conforme informação recebida da indústria terceira responsável pela fabricação.

Este recurso permite também, editar a ordem de produção de forma onde a mesma passe a englobar mais de um lote de produção do produto, pois a indústria terceira pode realizar várias produções e, consequentemente, várias entregas do produto para atender a quantidade solicitada.

[Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603094-Edi%C3%A7%C3%A3o-do-N%C3%BAmero-de-Lote#configuraes)                                                             [Editando um número de Lote](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603094-Edi%C3%A7%C3%A3o-do-N%C3%BAmero-de-Lote#editandoumnmerodelote)

[Restrições de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603094-Edi%C3%A7%C3%A3o-do-N%C3%BAmero-de-Lote#restriesdeuso)

## Configurações

A funcionalidade Editar Lote está disponível apenas nas [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o) cujo correspondente [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314) esteja configurado com tipo de numeração Manual e seja especificado um valor correspondente ao Lote Curinga; estes dados são configurados no Processo Produtivo, seção **"Nro. de lote"**, campos **"Tipo do Nro. Lote"** e **"Lote Curinga"**.

É importante informar que, o Lote Curinga será um valor fictício utilizado pelo sistema para lançamento da Ordem de Produção, e deverá ser substituído posteriormente por uma numeração de lote real.

![Imagem 1: É importante informar que, o Lote Curinga será um valor fictício utilizado pelo sistema para lançamento da Ordem de…](https://ajuda.sankhya.com.br/hc/article_attachments/4416676427287)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603094-Edi%C3%A7%C3%A3o-do-N%C3%BAmero-de-Lote#top)

## Editando um Número de Lote

Ao trabalhar com um Processo Produtivo, cujo Tipo de Numeração de lote seja Manual e que possua Lote Curinga, este lote curinga será carregado automaticamente na coluna **"Nro. Lote"** presente na aba Produtos Acabados (PA) no [Lançamento da Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP-) correspondente ao produto. Nesta etapa, você não poderá editar esta informação.

![Imagem 2: Ao trabalhar com um Processo Produtivo , cujo Tipo de Numeração de lote seja Manual e que possua Lote Curinga , este…](https://ajuda.sankhya.com.br/hc/article_attachments/4416754553623)

Uma vez lançada a Ordem de Produção com Lote Curinga, você poderá editar a numeração de lote dos produtos através da tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313), sendo que, na aba **"Produtos"**, temos o botão **"Editar Lote"**; o acionamento deste botão irá abrir um pop-up com esta mesma nomenclatura para que o Número do Lote Curinga seja substituído:

![Imagem 3: Uma vez lançada a Ordem de Produção com Lote Curinga , você poderá editar a numeração de lote dos produtos através da…](https://ajuda.sankhya.com.br/hc/article_attachments/4416739131159)

- No campo **"Nro. Lote"**, especifique o número de lote real que irá substituir o lote curinga.
- Obrigatoriamente, você também deve especificar a **"Quantidade"** do lote curinga que se deseja transformar em um lote real.
- Determine a **"Data de Fabricação"** do lote real que está substituindo o lote curinga. Este campo é habilitado apenas se o produto for controlado por Data de Fabricação.
- No campo **"Data de Validade"**, especifique a data de validade do lote real que está substituindo o lote curinga. Esta informação é habilitada para preenchimento, apenas se o produto for controlado por Data de Validade.

Ao **"Confirmar"** a ação de Editar Lote, o sistema realiza como consequência, a modificação da quantidade especificada do lote curinga em um lote real. Essa ação provoca dois resultados:

- Os apontamentos gerados até o momento para o lote curinga, são editados e irão representar o lote real agora incluído na ordem;
- As movimentações entre repositórios são editadas de forma a representar o lote real agora inserido na ordem.

Caso seja cometido algum erro durante a edição de um lote curinga em lote real, é possível proceder com a ação reversa, ou seja, voltar um lote real para o lote curinga, de modo a corrigir a modificação equivocada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603094-Edi%C3%A7%C3%A3o-do-N%C3%BAmero-de-Lote#top)

## Restrições de Uso

Existem algumas restrições quanto ao uso da funcionalidade de Editar Lote que visam manter a integridade dos dados gerados pelo sistema:

- Não é permitida a transferência parcial do lote curinga entre atividades;
- Não é permitido editar o lote curinga duas vezes para o mesmo lote real;
- Não é possível gerar uma nota de produção para um lote curinga;
- É permitida a volta do lote real para o lote curinga, apenas em relação a quantidade ainda não liberada por notas de produção;
- Os apontamentos que deram origem a nota de produção não nunca sofrem edição.

**Importante:** para que o sistema gerar a Data de Fabricação e/ou Validade dos produtos como mencionado durante a edição do lote, é preciso que a Base para cálculo da Dt.Validade do produto esteja definida como **"Data de inicialização da OP"**; esta definição é realizada no Processo Produtivo, aba Produtos (PA), sub-aba Geral, campo Base para cálculo da Dt. Validade:

![Imagem 4: Importante: para que o sistema gerar a Data de Fabricação e/ou Validade dos produtos como mencionado durante a edição…](https://ajuda.sankhya.com.br/hc/article_attachments/4416739262615)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603094-Edi%C3%A7%C3%A3o-do-N%C3%BAmero-de-Lote#top)
