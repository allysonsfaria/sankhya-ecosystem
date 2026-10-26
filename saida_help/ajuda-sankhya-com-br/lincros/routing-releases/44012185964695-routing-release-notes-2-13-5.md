---
id: "44012185964695"
titulo: "[Routing] - Release Notes 2.13.5"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012185964695--Routing-Release-Notes-2-13-5"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:22:41Z"
rotulos: ["sync_hc", "lincros", "lincros_13434096", "sync_hash_b02664f90f46"]
---

# [Routing] - Release Notes 2.13.5

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012196413719)

## Melhorias

---

## Alteração no texto de seleção de veículos, na tela de iniciar uma nova sessão.

Foi retirada a nomenclatura da obrigatoriedade de selecionar um veículo para criar uma sessão. **[Link do Artigo](https://lincros.movidesk.com/kb/article/210140/routing-iniciar-uma-nova-sessao-de-roteirizacao?preview=true&revisionId=686678)**.

---

## Integração de pedidos devolvidos no Tracking com o Routing.

Com a melhoria os pedidos devolvidos no Tracking serão integrados com o Routing como pedido de Reentrega.

![Imagem 2: Com a melhoria os pedidos devolvidos no Tracking serão integrados com o Routing como pedido de Reentrega.](https://ajuda.sankhya.com.br/hc/article_attachments/44012186368535)

---

## Validação no cadastro de motorista.

Ao realizar um cadastro de motorista com um CPF, será validado a quantidade de caracteres, não podendo concluir caso tenha um valor menor que 11 dígitos. **[Link do artigo](https://lincros.movidesk.com/kb/article/146650/cadastro-de-motorista?preview=true&revisionId=676768)**.

---

## Criação da sessão com clientes de coordenada inválida.

Com a melhoria será possível cadastrar clientes onde não será possível obter a latitude e longitude na importação. **[Link do artigo](https://lincros.movidesk.com/kb/article/220082/router-sessao-com-clientes-de-coordenada-invalidas?preview=true&revisionId=724025)**.

---

## Alterar o nome da rota em lote.

Com a melhoria será possível cadastrar clientes onde não será possível obter a latitude e longitude na importação. **[Link do artigo](https://lincros.movidesk.com/kb/article/220134/alteracao-do-nome-da-rota-em-lote?preview=true&revisionId=724089).**

---

## Adicionada a quantidade de total de itens na sessão.

Quando selecionado um pedido na tela da sessão será apresentada a quantidade total de itens.

![Imagem 3: Quando selecionado um pedido na tela da sessão será apresentada a quantidade total de itens.](https://ajuda.sankhya.com.br/hc/article_attachments/44012211565207)

![Imagem 4: Quando selecionado um pedido na tela da sessão será apresentada a quantidade total de itens.](https://ajuda.sankhya.com.br/hc/article_attachments/44012196807703)

---

## Consulta de pedidos pela data de importação.

Com a melhoria será possível consultar os pedidos pela importação. **[Link do artigo](https://lincros.movidesk.com/kb/article/209661/routing-pedidos?preview=true&revisionId=724245).**

![Imagem 5: Com a melhoria será possível consultar os pedidos pela importação. Link do artigo .](https://ajuda.sankhya.com.br/hc/article_attachments/44012196890263)

---

## Validação na importação de cadastro de clientes.

Com a melhoria aplicada será realizada análises nos registros com intuito de retirar inconsistências no endereço.

Exemplo:

- **Campo 'Endereço'** ;

  - Normalizar o tipo de logradouro: “Av.” = “Avenida”
  - Tratar tipos de logradouro repetidos: “R RUA” = “RUA”
  - Inserção de virgula antes do número de casa: “R. Xyz 123” = “Rua Xyz, 123”
- ## Campo 'Cidade';

  - Tratar algarismos árabes e romanos: “XV de Novembro” = “Quinze de Novembro”
  - Transfere a sigla de estado para o campo dedicado: “Blumenau/SC” = “Blumenau”
- ## Campo 'Cidade';

  - Tratamento de nomes para siglas: “Santa Catarina” = ”SC”
- ## Campo 'CEP';

  - Permite uma componente com 8 ou duas de 5 e 3 números e junta eles:

- - - “01234-567” = ”01234567”

- - Preenche os componentes com zeros na esquerda:

    - “1234-56” = “01234056”
    - “1234567” = “01234567”
    - “123” = “00123”

---

## Adicionado no relatório de clientes a coluna de grade de atendimento.

Adicionado uma nova coluna no relatório de clientes para visualizar a grade de atendimento. **[Link do artigo](https://lincros.movidesk.com/kb/article/208426/routing-relatorios-de-clientes?preview=true&revisionId=684259).**

---

## Nova funcionalidade (íman) para desenhar os setores.

O íman ao desenhar um novo setor ou desenhando em um setor já cadastrado, será alinhado próximo ao setor cadastrado. **[Link do artigo](https://lincros.movidesk.com/kb/article/197471/routing-cadastro-de-setor?preview=true&revisionId=724295).**

![Imagem 6: O íman ao desenhar um novo setor ou desenhando em um setor já cadastrado, será alinhado próximo ao setor cadastrado.…](https://ajuda.sankhya.com.br/hc/article_attachments/44012201577239)

---

## Possibilidade de informar o complemento na importação de clientes via arquivo.

Foi adicionado o complemento para importação de clientes via arquivo, para esta funcionalidade é necessário a alteração no layout de importação via arquivo.

---

## Adicionado botão para inativar o motorista.

Foi adicionado um novo botão para inativar o cadastro de motorista. **[Link do artigo](https://lincros.movidesk.com/kb/article/146650/cadastro-de-motorista?preview=true&revisionId=723788).**

---

## Nova funcionalidade para consultar os pedidos pelo número.

Com essa funcionalidade, será possível, consultar os pedidos cujo valor se inicia ou finaliza com um determinado valor. **[Link do artigo.](https://lincros.movidesk.com/kb/article/209661/routing-pedidos?preview=true&revisionId=724245)**

---

## Integração do valor do pedágio como taxa adicional entre o Routing com o TMS Lincros.

Com essa integração os valores do pedágio serão integrados ao TMS quando criado ao embarque. **[Link do artigo.](https://lincros.movidesk.com/kb/article/217438/router-integracao-do-valor-do-pedagio-ao-tms-como-taxa-adicional?preview=true&revisionId=716352)**

---

## Melhoria no cadastro dos setores.

Com a melhoria será possível realizar o desenho dos setores de forma automática obtendo o desenho através do nível de Estado, Munícipio e Bairro ou manual. **[Link do artigo.](https://lincros.movidesk.com/kb/article/197471/routing-cadastro-de-setor?preview=true&revisionId=724295)**

---

## Integração do mapa da Rota entre o Routing com o TMS Lincros.

Com esta melhoria ao criar o Embarque no TMS Lincros, será integrado o mapa com as entregas da rota.

---

## Envio no número da sessão ao integrar a rota entre o Routring com o TMS Lincros.

Com a melhoria o número da sessão será enviada na integração da rota para o TMS Lincros ao criar o embarque.

---

## Melhoria na visualização dos setores.

Foi adicionado bordas nos setores para facilitar a visualização.

![Imagem 7: Foi adicionado bordas nos setores para facilitar a visualização.](https://ajuda.sankhya.com.br/hc/article_attachments/44012219791255)

---

## Melhoria na exibição dos menus.

Com a melhoria os menus serão apresentados em ordem alfabética.

---

## Adicionado nova ação para finalizar uma rota.

Ao clicar em uma rota com o botão direito, será possível utilizar a ação para finalizar a rota.

![Imagem 8: Ao clicar em uma rota com o botão direito, será possível utilizar a ação para finalizar a rota.](https://ajuda.sankhya.com.br/hc/article_attachments/44012212753815)

---
