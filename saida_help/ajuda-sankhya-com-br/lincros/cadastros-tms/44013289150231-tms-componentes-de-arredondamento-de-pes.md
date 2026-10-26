---
id: "44013289150231"
titulo: "[TMS] - Componentes de Arredondamento de Peso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013289150231--TMS-Componentes-de-Arredondamento-de-Peso"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:53:40Z"
rotulos: ["sync_hc", "lincros", "lincros_13432713", "sync_hash_f6cab38315c7"]
---

# [TMS] - Componentes de Arredondamento de Peso

**Menu**: Cadastros gerais > Configurações de empresa > Componentes de frete

**Objetivo**: Como realizar a configuração do arredondamento de peso

**Considerações**:

- Os componentes formatoArredondamento e mascaraArredondamento foram criados para atender as negociações das transportadoras que utilizam o cálculo do frete peso por fração de Kg inteira, arredondando para cima ou para baixo o peso nominal/cubado, para atribuir a tarifa;
- Este cadastro deve ser solicitado para o time de Suporte da Lincros, pois somente o Suporte tem acesso ao cadastro de Componentes de Frete;

## Abaixo segue um exemplo:

O peso da nota é 12,36 kg , e o valor por Kg é R$ 1,00;

O cálculo padrão do sistema multiplica o valor por Kg pelo peso, desta forma o valor fica R$ 12,36;

Caso a transportadora utilize o arredondamento de peso para cima, o Frete peso de uma nota de 12,36 kg custará R$ 13,00;

Caso a transportadora utilize o arredondamento de peso para baixo, o Frete peso de uma nota de 12,36 kg custará R$ 12,00;

1. Cadastrar os componentes mencionados, conforme as imagens abaixo.

## mascaraArredondamento:

## formatoArredondamento:

2. Após ter os componentes cadastrados e configurados pelo time de Suporte da Lincros;

3. Acessar a Tabela de fretes cuja a negociação inclui arredondamento de peso, e inserir os seguintes componentes nas Generalidades da tabela:

O componente '**mascaraArredondamento**', selecionando a máscara cadastrada;

O componente '**formatoArredondamento**', selecionando o formato de arredondamento para o frete peso ( para cima ou para baixo);

O componente Formato do peso, selecionando o formato 'KILO\_FRACAO';

Exemplo de Pré-conhecimento com o formato de arredondamento de Frete peso para baixo:

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
