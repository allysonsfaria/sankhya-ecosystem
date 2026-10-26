---
id: "360044600314"
titulo: "Fórmulas para Desconto Máximo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:22:46Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Fórmulas", "Liberação de Limites", "Fórmulas para Desconto Máximo", "br.com.sankhya.formulas.desconto.maximo", "Fórmulas para Desconto Máximo manual", "Tipos de Negociação", "Desconto Máximo Fórmulas Configuração", "Comercial"]
---

# Fórmulas para Desconto Máximo

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311792278679) Módulo: Comercial > avançado
```

---

Através desta tela, você poderá criar fórmulas para o cálculo do **"Desconto Máximo"**, considerando campos dos cadastros de [Região](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074), [Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), [Vendedor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133), [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) e [Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874). As fórmulas serão informadas na tela de cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) para a validação dos eventos [21 - Fórmula Desc.Máx.Tipo Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#21-frmuladesc.mx.tiponegociao) e [27 - Fórmula Desc.Máx.Tipo Negoc. por Item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#27frmuladesc.mx.tiponegoc.poritem).

**Importante:** para validação dos eventos de Desconto máximo pela Fórmula, os parâmetros abaixo precisam estar configurados:

- Ligue o parâmetro **"Usar liberação de limites por alçada?- USALIBLIM"**, para habilitar o controle de Liberação de Limites.
- O parâmetro **"Valida desconto máximo-VALDESCMAX"** não pode estar configurado com as opções **"Não valida"** ou **"Valida e aceita"** para que a liberação seja exigida.

[Preenchimentos iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#preenchimentosiniciais)                                                             [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#construtordeexpress%C3%B5es) 

[Vincular a fórmula ao Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#vincularaf%C3%B3rmulaaotipodenegocia%C3%A7%C3%A3o)                           [Definir limites para liberação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#definirlimitesparalibera%C3%A7%C3%A3o)  

[Configurar Desconto máximo por produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#configurardescontom%C3%A1ximoporproduto)

![Imagem 2: Configurar Desconto máximo por produto](https://ajuda.sankhya.com.br/hc/article_attachments/360099255554)

## Preenchimentos iniciais

Temos os seguintes campos para preenchimento:

O campo **"Código"** é de preenchimento manual e obrigatório, e se refere a um código de identificação da fórmula.

Informe no campo **"Descrição da Fórmula"**, uma descrição para identificar a fórmula de forma mais fácil.

O campo **"Fórmula"** é destinado à construção da fórmula propriamente dita, e pode ser feita com o auxílio do componente **"Construtor de Expressão"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#top)

## Construtor de Expressões

![Imagem 3: Construtor de Expressões](https://ajuda.sankhya.com.br/hc/article_attachments/1500000390021)

Temos através do botão em destaque, o componente Construtor de Expressões. Você pode obter mais detalhes do funcionamento deste componente acessando o link [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109213).

A seguir, apresentaremos alguns exemplos de expressões:

**1.** Para validação do evento 27 - Fórmula Desc.Máx.Tipo Negoc. por Item, a fórmula deve ser feita de forma que ela estabeleça um limite, em valor, para o desconto que cada item poderá receber. Para isso, normalmente é levado em consideração os dados da negociação, como Parceiro, Região, Empresa, dentre outros. Abaixo, trouxemos um exemplo da fórmula:

queItens.VLRTOT\* IF(queParcDM.CODREG=10100,0.1,0.05)

Nesta fórmula, para encontrar o valor do desconto máximo o **"Valor Total do Item"** está sendo multiplicado por 10% ou 5%, dependendo da região do [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610034).

**2.** Para validação do evento 21 - Fórmula Desc.Máx.Tipo Negociação, são observados os valores totais da nota, ou seja, a soma dos descontos oferecidos para todos os itens não pode ser acima do valor resultante da resolução da sua expressão matemática. Considere o exemplo:

(queCab.VLRNOTA+queCab.VLRDESCTOT+queCab.VLRDESCTOTITEM)\*IF(queParcDM.CODREG=10100,0.1,0.05)

Nesta expressão, o valor total da negociação será obtido pela soma do **"Valor da Nota"** com os descontos totais da nota e do item, e este valor da negociação, da mesma forma que o exemplo do item anterior, será multiplicado também por 10% ou 5%, dependendo da região do Parceiro.

**Observação:** As fórmulas precisam ser configuradas para retornar o valor do Desconto Máximo, e não o percentual.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#top)

## Vincular a fórmula ao Tipo de Negociação

Depois que você cadastrar as fórmulas necessárias nesta tela, é preciso vinculá-las aos cadastros dos [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173), aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas).

O campo **"Fórmula desc. máximo"**, faz com que o sistema passe a validar o evento [21 - Fórmula Desc.Máx.Tipo Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#21-frmuladesc.mx.tiponegociao), observando se o desconto total da negociação supera o valor obtido pela resolução da fórmula.

Já o campo **"Fórmula desc. máximo itens"** determina que o sistema valide o evento [27 - Fórmula Desc.Máx.Tipo Negoc. por Item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#27frmuladesc.mx.tiponegoc.poritem), observando para cada item da nota ou pedido, se o valor do desconto oferecido é maior que o estabelecido pela fórmula.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#top)

## Definir limites para liberação

No Cadastro de [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), botão [Outras opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es), opção **"Limites para Liberação"**, devem ser calculados os limites, em valor ou percentual, que o usuário terá para liberação dos eventos 21 e/ou 27, conforme as configurações realizadas anteriormente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#top)

## Configurar Desconto máximo por produto

No Cadastro de Produtos é onde se inicia a Liberação de Limites de Desconto. Assim, se o produto estiver com o campo **"% Desconto Máximo"** (aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abavenda)) vazio, a liberação não será exigida.

Desta forma, para que o sistema observe apenas o Desconto Máximo obtido pelas fórmulas dos Tipos de Negociação, é recomendado que, neste campo, seja definido um % Desconto máximo de 100%.

**Observação:** Se for informado neste campo, um percentual menor que 100%, o sistema validará, além dos eventos da fórmula do Tipo de Negociação, os eventos [25 - Desconto por item da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#25-descontoporitemdanota), e [2 -](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#2-descontoproduto) [Desconto Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#2-descontoproduto)[.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#2-descontoproduto)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314-F%C3%B3rmulas-para-Desconto-M%C3%A1ximo#top)
