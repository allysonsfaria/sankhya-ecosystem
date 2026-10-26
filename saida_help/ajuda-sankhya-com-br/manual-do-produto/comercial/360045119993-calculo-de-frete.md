---
id: "360045119993"
titulo: "Cálculo de Frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119993-C%C3%A1lculo-de-Frete"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:33:40Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parceiro", "Cidades", "Fórmulas", "Cálculo de Frete", "Cálculo Automático de Frete", "br.com.sankhya.mgecom.cad.calculofrete", "Cálculo de Frete manual", "Transporte", "Fretes", "Assistente de Filtros", "Comercial"]
---

# Cálculo de Frete

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312120006551) Módulo: Comercial > Rotinas > Ordem de Carga
```

---

Esta rotina tem o objetivo de facilitar o cálculo de frete para todas as notas de uma [Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga) ou várias Ordens de Carga. Para isso, é necessário que o tipo de cálculo do frete esteja configurado corretamente no cadastro da ordem de carga.

Ao efetuar o cálculo, se alguma ordem de carga estiver sem o tipo de cálculo cadastrado, o sistema emite a seguinte mensagem:

**"O tipo de cálculo do frete deve ser informado na ordem de carga"**.

![Imagem 2: "O tipo de cálculo do frete deve ser informado na ordem de carga" .](https://ajuda.sankhya.com.br/hc/article_attachments/21978181626519)

Inicialmente, por meio do **"Assistente de filtros"** pode-se realizar a criação de filtros personalizados para apresentação das Ordens de Carga que servirão como base para o cálculo do frete.

Tem-se também, os botões ![Imagem 3: Tem-se também, os botões "Remover selecionados" e "Remover NÃO selecionados" para retirar as OC's selecionadas da grade.](https://ajuda.sankhya.com.br/hc/article_attachments/21978307254935) **"Remover selecionados"** e ![Imagem 4: Tem-se também, os botões "Remover selecionados" e "Remover NÃO selecionados" para retirar as OC's selecionadas da grade.](https://ajuda.sankhya.com.br/hc/article_attachments/21978324520087) **"Remover NÃO selecionados"** para retirar as OC's selecionadas da grade.

É possível realizar a filtragem das Ordens de Carga através do **"Tipo de Movimento"** utilizado; por exemplo, pode-se filtrar pelas Ordens de Carga relacionadas apenas às Compras, Requisições, entre outras possibilidades.

Quando se trabalha com várias empresas cadastradas no sistema, é possível solicitar a exibição das Ordens de Carga relacionadas a cada uma delas separadamente, ao preencher o campo **"Empresas"** com seu respectivo código.

Se a marcação **"Calcular fretes por rota usando o valor atual?"** for efetuada, o sistema utiliza para cálculo o valor atual e, se desmarcada, o valor histórico.

Apresentadas as Ordens de Carga desejadas, acione o botão ![Imagem 5: Apresentadas as Ordens de Carga desejadas, acione o botão "Calcular Frete" , para que o cálculo seja realizado. Abaixo,…](https://ajuda.sankhya.com.br/hc/article_attachments/22317572309143) **"Calcular Frete"**, para que o cálculo seja realizado. Abaixo, têm-se as configurações para que o cálculo seja corretamente efetuado.

### Configurações necessárias para cálculo de Frete

Na tela [Fórmulas para Cálculo de Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600334) são realizados os cadastros das fórmulas para realização do cálculo dos diversos tipos de frete. O código destas fórmulas deve ser informado no cadastro do [Veículo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109693-Ve%C3%ADculos) que será registrado na ordem de carga.

Na tela mencionada acima, informe os seguintes campos:

- O **"Código da Fórmula"** com o código da fórmula que é cadastrada aleatoriamente e progressivamente.
- A **"Descrição"** do que se trata a fórmula que está sendo cadastrada.
- No campo **"Tipo de Distância"** se seleciona a distância a ser considerada nos cálculos do frete, entre as seguintes opções:
  - **Entre Parceiros:** se a fórmula for definida para calcular por **"Parceiro"** e não houver distância cadastrada entre dois parceiros em uma ordem de carga, é necessário que se realize o cadastro da distância entre parceiros; nesta opção, despreza-se a distância entre cidades. Caso não seja cadastrada a distância entre parceiros, o sistema emite uma mensagem informando que o frete não será calculado por falta do cadastro de distância entre parceiros daquela ordem de carga;
  - **Entre Cidades:** analogicamente, sendo a fórmula por **"Cidade"**, considera-se apenas à distância por cidade, se fazendo necessário o cadastro da distância entre as cidades. Despreza-se a distância entre parceiros e emite-se uma mensagem caso não esteja cadastrada a distância entre as cidades;
  - **Entre Parceiros ou Cidades:** se a fórmula for por **"Parceiro/Cidade"**, o sistema verifica se há distância por parceiro e, não havendo, considera a distância por cidade; se também não houver distância por cidades, será solicitado pelo sistema o cadastro de distância entre os parceiros ou entre as cidades.
- No campo **"Fórmula"** cadastre a fórmula propriamente dita. Pode-se também utilizar o botão **"F(x) Construtor"**, localizado no lado direito superior da tela para auxílio na construção da fórmula.
- No [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos#h_5f714e1e-fcee-4e29-86aa-87de3a8a4c1c), deve-se inserir no campo **"Fórmula p/cálculo de Frete"** a fórmula criada no passo anterior.
- Na tela [Ordens de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga#h_01ECQYS6QH937X57WSMH9GSH58), preencha os campos **"Veículo"**, **"Região"**, **"Parceiro Transportadora"** e **"Parceiro Origem da Rota"**. Ainda nesta tela, na aba [Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga#h_01ECQYSGSBRZKRY1H2FH3FGG6D), preencha os campos **"Tipo de Cálculo de Frete"** e **"Tipo de Distância p/ Valor Manual/Tabela"**.

**Nota:** se a distância for Entre Parceiros, preencha os campos **"Cód. Parceiro Origem"** (parceiro configurado na Ordem de Carga - Parceiro Origem da Rota) e **"Cód. Parceiro Destino"** (Parceiro da Nota). Por outro lado, sendo a distância Entre Cidades, preencha os campos **"Cód. Cidade Origem"** e **"Cód. Cidade Destino"**. 

- Realize o Pedido/Nota de Venda;

- Na tela [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga), informe a Ordem de Carga e atualize a sequência da Ordem de Carga da Nota.

- Após as configurações acima, basta clicar no botão Calcular Frete da rotina Cálculo de Frete.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119993-C%C3%A1lculo-de-Frete#top)
