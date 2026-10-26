---
id: "44010117758487"
titulo: "[TMS] - Gerar conhecimento de redespacho de forma automática"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010117758487--TMS-Gerar-conhecimento-de-redespacho-de-forma-autom%C3%A1tica"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:30:30Z"
rotulos: ["sync_hc", "lincros", "lincros_13433349", "sync_hash_53667ccf05a9"]
---

# [TMS] - Gerar conhecimento de redespacho de forma automática

**Menu:** Operacional > Importação > Ct-e > Importação

**Objetivo**: Como gerar conhecimento de redespacho de forma automática

## Considerações:

- O Lincros possui **dois caminhos** para gerar o redespacho automaticamente: (1) via roteiro, sem depender de informações no XML da NF-e; e (2) via tags informadas no XML da NF-e;
- Em ambos os casos, o pré-conhecimento do primeiro trecho permanece como **Normal** e os trechos seguintes são gerados como **Redespacho**;
- Em ambos os casos, a transportadora do redespacho **deve ser diferente** da transportadora do pré-conhecimento Normal de origem;

## Caminho 1 - Redespacho automático via roteiro (não depende de tags no XML)

- Ao incluir a NF-e em uma carga, o Lincros simula as opções de frete a partir da origem e do destino da nota fiscal;
- Quando a simulação resulta em um roteiro com mais de um trecho, o primeiro trecho gera o pré-conhecimento **Normal** e os demais trechos são marcados automaticamente como **Redespacho**;
- O destino do primeiro trecho precisa ter interseção de faixa de CEP com a origem do segundo trecho;
- As transportadoras do primeiro e do segundo trecho não podem ser a mesma;
- Quando há mais de um redespacho, o Lincros encadeia os trechos em múltiplos níveis;
- Neste caminho, o único requisito da NF-e é ter origem e destino identificáveis, não sendo necessário nenhum campo específico no XML.

## Caminho 2 - Redespacho automático via tags no XML da NF-e

- Ao importar a NF-e no Lincros, automaticamente o sistema irá gerar tanto o pré-conhecimento Normal quanto o de Redespacho;
- Inclusive o pré-conhecimento de redespacho que será gerado automaticamente, já irá ficar com o CEP de Origem correto, e calculará corretamente de acordo com a tabela do fracionado também;

Para que isso seja possível, é necessário implementar na NF-e as TAG´s abaixo:

- **TF\_CNPJ\_REDESPACHO**: Deve ser informado o CNPJ da transportadora que fará o 'Redespacho' (devem ser informados os 14 números sem pontos e sem barras e traços);
- **TF\_CEP\_REDESPACHO:** Deve ser informado o CEP que determinará o destino do pré-conhecimento 'Normal' e a origem do pré-conhecimento de 'Redespacho' (devem ser informados 8 números sem pontuação e sem traço);

Abaixo, um exemplo de XML de NF-e com essas tags informadas nas 'infAdic':

![Imagem 1: Abaixo, um exemplo de XML de NF-e com essas tags informadas nas 'infAdic':](https://ajuda.sankhya.com.br/hc/article_attachments/44010101018007)

**Obs:** Estas tag´s são parametrizadas pela TI do cliente.

**Obs²:** O Lincros não aceita hoje mais de uma tag do mesmo tipo, por exemplo, cliente que redespacha 2 trajetos na mesma nota.

**Obs³:** Se a NF-e não tiver as tags e o roteiro não indicar mais de um trecho, o redespacho não é gerado automaticamente. Nesse caso, ele pode ser criado manualmente a partir do pré-conhecimento Normal.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
