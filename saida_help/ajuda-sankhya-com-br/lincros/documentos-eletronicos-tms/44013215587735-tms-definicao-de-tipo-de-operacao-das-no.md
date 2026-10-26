---
id: "44013215587735"
titulo: "[TMS] - Definição de Tipo de Operação das Notas Fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013215587735--TMS-Defini%C3%A7%C3%A3o-de-Tipo-de-Opera%C3%A7%C3%A3o-das-Notas-Fiscais"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T19:51:19Z"
rotulos: ["sync_hc", "lincros", "lincros_13432813", "sync_hash_d8abd57fa104"]
---

# [TMS] - Definição de Tipo de Operação das Notas Fiscais

**Menu**: Documentos eletrônicos > NF-es

**Objetivo**: Entender a forma que o sistema analisa as notas fiscais e como ele define se corresponde a uma nota de Entrada ou Saída.

**Considerações**:

- O sistema possui algumas regras internas (não alteráveis) que são consideradas para que seja então definido o tipo de operação de uma nota fiscal (Entrada ou Saída)

## Etapa 1

O sistema verifica a modalidade do frete, se for uma das modalidades abaixo então será mantido o tipo de operação que está constando no arquivo XML, caso contrário o sistema segue com as próximas verificações.

- Por conta de Terceiros
- Sem Frete
- Não Preenchido (nula)

**Observação:**No arquivo XML da NF-e existe o campo **tpNF** - Tipo de Operação da NF-e.

Esse campo pode ser preenchido com os seguintes valores:

0 = Entrada.
1 = Saída.

![Imagem 1: 0 = Entrada. 1 = Saída.](https://ajuda.sankhya.com.br/hc/article_attachments/44013196521111)

## Etapa 2

O sistema verifica se a unidade é a tomadora do frete, caso não seja, o sistema segue para a próxima etapa.

**2.1** Se a modalidade do frete for uma das modalidades abaixo,  operação é definida como ENTRADA.

- Frete por Conta do Destinatário
- Frete c/ frota própria por conta do Destinatário

**2.2** Se a modalidade do frete for uma das modalidades abaixo ou outra modalidade diferente das citadas acima, será mantido o tipo de operação que consta no XML.

- Frete por Conta do Emitente
- Frete c/ frota própria por conta do Emitente

## Etapa 3

O sistema verifica se a unidade é a emitente do documento, caso seja a emitente então é definido como saída, caso não seja, o sistema segue para a próxima etapa.

## Etapa 4

Apenas define o tipo de operação como Entrada.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
