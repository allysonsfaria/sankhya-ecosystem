---
id: "360044598674"
titulo: "Parcelar com Vários Tipos de Títulos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598674-Parcelar-com-V%C3%A1rios-Tipos-de-T%C3%ADtulos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:47:57Z"
rotulos: ["Configuração", "Movimentação Financeira", "CAMPODISPPARC", "Parcelar com Vários Tipos de Títulos", "Parcelar com Vários Tipos de Títulos manual", "Preferências", "Financeiro", "Parcelamento Flexível com Vários Tipos de Títulos", "PDVWEB"]
---

# Parcelar com Vários Tipos de Títulos

Nosso sistema dispõe de uma opção para gerar parcelas para o financeiro do pedido/nota direto da [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) na grade de itens permitindo que você configure a quantidade de parcelas necessárias para compor a negociação junto ao cliente.

![Imagem 1: Nosso sistema dispõe de uma opção para gerar parcelas para o financeiro do pedido/nota direto da Central - Compras |…](https://ajuda.sankhya.com.br/hc/article_attachments/8420445065495)

Para isso temos que verificar as seguintes regras:

- O [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) utilizado deve estar configurado na aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas), campo Opção de digitação como **"Digita Data e Valor"**;
- A movimentação deve atualizar financeiro e possuir financeiros na aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abafinanceiro);
- O sistema irá permitir um parcelamento onde o valor pode ser menor ou maior que o valor total da nota; somente será emitida uma mensagem de aviso;
- Mediante a forma que for feito o parcelamento, pode haver mais de uma parcela com o mesmo vencimento e valor;
- A geração das parcelas seguirá a ordem informada no parcelamento, ou seja, se informado primeiro o parcelamento, por exemplo, de 10 parcelas e depois inserida uma parcela à vista, será gerada primeiro as 10 parcelas e depois a parcela à vista;
- Se forem alterados valores ou optar-se por refazer o financeiro, o sistema irá gerar as parcelas com base na configuração do [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) e não do parcelamento efetuado;

**![Imagem 2: Comportamento do Parcelamento no PDVWEB](https://ajuda.sankhya.com.br/hc/article_attachments/33715898122775) Comportamento do Parcelamento no PDVWEB**

Ao utilizar a opção **"Parcelamento com vários títulos"** em seus Pedidos de Venda e faturá-los através do PDVWEB, é crucial entender como o sistema gerencia as parcelas.

**O que você precisa saber:**

Se o parâmetro `VALAPRRECPDV` estiver ativado em suas **Preferências do Sistema**, o **PDVWEB** pode reprocessar o financeiro do seu pedido. Isso significa que as parcelas originalmente definidas no **Pedido de Venda** podem ser desconsideradas, e o sistema criará novos títulos com base nas configurações de parcelamento do **Tipo de Negociação** utilizado no momento do faturamento no **PDVWEB**. Por exemplo, se seu pedido tinha 10 parcelas no cartão, mas o **Tipo de Negociação** no **PDVWEB** está configurado para 3 parcelas de boleto, o **PDVWEB** irá gerar 3 parcelas de boleto, ignorando suas 10 parcelas originais.

**A Solução:**

Para garantir que o **PDVWEB** sempre **respeite as parcelas definidas previamente no seu Pedido de Venda**, independentemente do **Tipo de Negociação** utilizado no faturamento, é necessário que o parâmetro **`VALAPRRECPDV`** esteja **desativado** (desabilitado) nas **Preferências do Sistema**. Recentemente, também foi desabilitado o parâmetro **`HABTIPALTDTVENC`** para otimizar essa consistência.

Com essas configurações, suas parcelas serão mantidas exatamente como você as definiu no momento da criação do **Pedido de Venda**, assegurando a fidelidade do seu financeiro.

- [Conta bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), [Natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas) e [Centro de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado) serão copiados para as parcelas criadas;
- O sistema leva em consideração os parâmetros **"Transfere vencimento quando fim de semana/feriado - TRANSFVENC"**, **"Contrato para software? - CONTSOFT"** e **"Data Base p/ Cálculo do Vencimento no Faturamento - DTCALCVENC"**;
- Se for efetuado o parcelamento de um pedido de venda parcial ou totalmente faturado, o sistema emitirá a seguinte mensagem:

**"Existem lançamentos baixados que não podem ser excluídos."**

Ao clicar no botão **"Parcelar com vários Tip. Títulos"**, será apresentado o pop- abaixo:

[GIF animado: Imagem 3: Ao clicar no botão "Parcelar com vários Tip. Títulos" , será apresentado o pop- abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/8419790652567)

Neste pop-up temos os seguintes campos: 

**Tipo de Título:** informe-se qual será o Tipo de Título utilizado para geração das parcelas.

**Nro. Parcelas:** informe-se o número de parcelas que deverão compor o parcelamento em questão.

**Prazo entre parcelas:** este campo influenciará na composição do vencimento das parcelas; se o prazo for zero, será apresentado logo à frente do campo em vermelho, a expressão **(Á vista)**.

**Vlr do Desdobramento:** informe-se o valor que será composto no parcelamento configurado.

**Dt. Vencimento:** será apresentada preenchida a data em conformidade com o parâmetro DTCALCVENC; suponhamos que o parâmetro em questão esteja configurado com a Data de Faturamento e esta seja 12/02/2018, com isso, o primeiro vencimento será esta data. Caso necessário, podemos modificá-la.

**Total da nota:** o parcelamento é calculado com base no valor total da nota e este campo exibe esse valor para facilitar a visualização.

Ao clicar no botão Confirmar os financeiros serão gerados conforme configurado e se Cancelar, manterá a que já está criada.

**Importante:** a funcionalidade de Parcelar com vários tipos de títulos não atua corretamente caso a marcação **"Baixa na confirmação"** ([Cadastro de Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), [aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)) esteja realizada; isso porque, uma vez que será refeito o parcelamento de forma manual, o sistema não será capaz de identificar qual das partes deverá ser baixada na confirmação.

---

#### Parâmetros

Pode-se trabalhar com a configuração do parâmetro **"Campos disponíveis no parcelamento - CAMPODISPPARC"**, onde cria-se uma lista de campos que se deseja visualizar no pop-up de **"Parcelamento com vários tipos de títulos"**.

Observemos que no parâmetro mencionado, foram inseridos os campos **"NOSSONUM"** e **"CARTA"**.

![Imagem 4: Observemos que no parâmetro mencionado, foram inseridos os campos "NOSSONUM" e "CARTA" .](https://ajuda.sankhya.com.br/hc/article_attachments/8419388977175)

Uma vez informados os campos desejados no parâmetro, podemos observá-los disponíveis para escolha na configuração da grade do pop-up **"Parcelamento com vários tipos de títulos"**, conforme imagem abaixo:

![Imagem 5: Uma vez informados os campos desejados no parâmetro, podemos observá-los disponíveis para escolha na configuração da…](https://ajuda.sankhya.com.br/hc/article_attachments/8421417830295)

Passando-se os dois campos do nosso exemplo, para a parte de Colunas selecionadas, podemos notá-los agora na grade para configuração do parcelamento:

![Imagem 6: Passando-se os dois campos do nosso exemplo, para a parte de Colunas selecionadas , podemos notá-los agora na grade…](https://ajuda.sankhya.com.br/hc/article_attachments/8421450288151)

Ao clicar-se no sinal de inclusão para acrescentar um parcelamento, notaremos os campos disponíveis para preenchimento.

![Imagem 7: Ao clicar-se no sinal de inclusão para acrescentar um parcelamento, notaremos os campos disponíveis para preenchimento.](https://ajuda.sankhya.com.br/hc/article_attachments/8421453174551)

**Observação:** os campos NOSSONUM e CARTA aqui utilizados, são apenas exemplos para entendimento da configuração. Esta rotina possibilita a utilização dos campos que melhor se adequarem ao dia-a-dia e processo da empresa; pode-se também utilizar **"campos adicionais"** nesta configuração. Caso você queira que os campos adicionados sejam apresentados na aba **"Financeiro"** da [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), estes devem ser configurados na aba correspondente a esta tela em [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598674-Parcelar-com-V%C3%A1rios-Tipos-de-T%C3%ADtulos#top)
