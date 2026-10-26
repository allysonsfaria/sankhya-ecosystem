---
id: "44010729274775"
titulo: "[Routing] - Release Notes 2.12.0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010729274775--Routing-Release-Notes-2-12-0"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T18:45:20Z"
rotulos: ["sync_hc", "lincros", "lincros_13434125", "sync_hash_0ba5126ff399"]
---

# [Routing] - Release Notes 2.12.0

## Consulta de pedidos pela data de importação.

Com a melhoria será possível consultar os pedidos pela importação. [Link do artigo](https://intercom.help/ajudalincros/pt-BR/articles/13439353-routing-pedidos).

---

## Validação na importação de cadastro de clientes.

Com a melhoria aplicada será realizada análises nos registros com intuito de retirar inconsistências no endereço. Exemplo:

- ## Campo 'Endereço':

  - Normalizar o tipo de logradouro: "Av." = "Avenida"
  - Tratar tipos de logradouro repetidos: "R RUA" = "RUA"
  - Inserção de virgula antes do número de casa: "R. Xyz 123" = "Rua Xyz, 123"
- ## Campo 'Cidade':

  - Tratar algarismos árabes e romanos: "XV de Novembro" = "Quinze de Novembro"
  - Transfere a sigla de estado para o campo dedicado: "Blumenau/SC" = "Blumenau"
- ## Campo 'Estado':

  - Tratamento de nomes para siglas: "Santa Catarina" = "SC"
- ## Campo 'CEP':

  - "01234-567" = "01234567"
  - "1234-56" = "01234056"
  - "1234567" = "01234567"

---

## Adicionado no relatório de clientes a coluna de grade de atendimento.

Adicionado uma nova coluna no relatório de clientes para visualizar a grade de atendimento. [Link do artigo](https://intercom.help/ajudalincros/pt-BR/articles/13439400-routing-relatorios-de-clientes).

---

## Nova funcionalidade (íman) para desenhar os setores.

Ao desenhar um novo setor, desenhando em um setor já cadastrado, este será alinhando próximo ao cadastrado. [Link do artigo](https://intercom.help/ajudalincros/pt-BR/articles/13432298-routing-cadastro-de-setor).

![Imagem 1: Ao desenhar um novo setor, desenhando em um setor já cadastrado, este será alinhando próximo ao cadastrado. Link do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010737566999)

---

## Possibilidade de informar o complemento na importação de clientes via arquivo.

Foi adicionado o complemento para importação de clientes via arquivo, para esta funcionalidade é necessário a alteração no layout de importação via arquivo.

---

## Adicionado botão para inativar o motorista.

Foi adicionado um novo botão para inativar o cadastro de motorista. [Link do artigo](https://intercom.help/ajudalincros/pt-BR/articles/13438712-routing-cadastro-de-motorista).

---

## Nova funcionalidade para consultar os pedidos pelo número.

Com essa funcionalidade, será possível consultar os pedidos cujo valor se inicia ou finaliza com um determinado valor. [Link do artigo.](https://intercom.help/ajudalincros/pt-BR/articles/13439353-routing-pedidos)

---

## Integração do valor do pedágio como taxa adicional entre o Routing com o TMS Lincros.

Com essa integração os valores do pedágio serão integrado ao TMS quando criado ao embarque. [Link do artigo.](https://intercom.help/ajudalincros/pt-BR/articles/13438599-routing-integracao-do-valor-do-pedagio-ao-tms-como-taxa-adicional)
