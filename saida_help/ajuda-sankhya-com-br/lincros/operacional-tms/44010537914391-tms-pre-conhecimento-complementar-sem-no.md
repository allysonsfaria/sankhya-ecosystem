---
id: "44010537914391"
titulo: "[TMS] - Pré-conhecimento Complementar sem Normal vinculado: dois erros na importação de CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010537914391--TMS-Pr%C3%A9-conhecimento-Complementar-sem-Normal-vinculado-dois-erros-na-importa%C3%A7%C3%A3o-de-CT-e"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:40:33Z"
rotulos: ["sync_hc", "lincros", "lincros_16796188", "sync_hash_0629c1f92a62"]
---

# [TMS] - Pré-conhecimento Complementar sem Normal vinculado: dois erros na importação de CT-e

**Menu**: Para verificar/corrigir o pré-conhecimento > Operacional > Operacional Cargas > Pré-conhecimentos
Para verificar o CT-e > Operacional > Conhecimentos de frete
Para importar/reprocessar um CT-e > Operacional > Importação > CT-e > Importação
Para o contorno preventivo > Cadastros Gerais > Cadastros Gerais Configurações da Empresa > Tipos de frete

**Objetivo**: Explicar a causa comum por trás de dois erros distintos de importação de CT-e, mostrar como eles se relacionam entre si, e orientar sobre o ajuste necessário e o contorno preventivo (cadastro de Tipos de Frete).

**Considerações**:

- Os dois erros abaixo têm a mesma causa raiz: um pré-conhecimento que foi criado como do tipo **Complementar**, sem um pré-conhecimento do tipo **Normal** vinculado a ele;
- Isso normalmente acontece quando a NF-e vinculada ao CT-e é uma **nota filha** (ou seja, referencia uma nota pai) — nesse cenário, o sistema já classifica o pré-conhecimento gerado como Complementar automaticamente;
- **Isso não é uma falha do sistema**: a criação do pré-conhecimento como Complementar está correta para esse tipo de nota. O que falta, nesses casos, é o pré-conhecimento do tipo Normal correspondente, que o sistema exige para concluir a validação/importação.

## Os dois erros

**Erro 1** — aparece na importação do próprio CT-e original, quando o sistema não encontra o pré-conhecimento Normal correspondente:

"Nenhum conhecimento do tipo [Normal, Redespacho] localizado para o CT-e informado"

**Erro 2** — aparece na importação de um CT-e de Complemento de Valores (um documento diferente, emitido posteriormente), quando ele tenta se referenciar ao CT-e original pela chave de acesso e não o encontra:

"Não foi possível encontrar o CT-e referenciado [chave/Caminho XML=//CTe/infCte/infCteComp/chCTe/text()] (CT-e vem do SEFAZ com tipo: CT-e de Complemento de Valores)"

## Por que ocorrem e como se relacionam

Um CT-e do tipo Complemento de Valores só existe para complementar o valor de um CT-e original já emitido. Por isso, todo CT-e desse tipo traz, no XML, a chave de acesso do CT-e "pai" ao qual se refere (campo infCteComp/chCTe).

Quando o CT-e original correspondente a essa chave está com o Erro 1 ainda não corrigido — ou seja, seu pré-conhecimento continua registrado como Complementar em vez de Normal —, ele não é reconhecido como um CT-e válido na base. Qualquer complemento de valores que tente referenciá-lo, então, dispara o Erro 2.

**Efeito cascata**: em uma sequência de documentos com esse problema, o Erro 2 tende a se repetir enquanto o(s) CT-e(s) original(is) mais antigos da cadeia não forem corrigidos — mesmo que o XML do complemento mais recente esteja perfeitamente correto.

## O que precisa ser ajustado

Para cada CT-e afetado pelo Erro 1:

1. Localizar o pré-conhecimento vinculado à NF-e do CT-e com erro (em Pré-conhecimentos, ou diretamente pela tela do CT-e);
2. Alterar o tipo do pré-conhecimento de Complementar para Normal;
3. Reprocessar/reimportar o CT-e.

Quando houver mais de um CT-e afetado em sequência, o ajuste deve seguir a ordem cronológica, do mais antigo para o mais recente — já que os complementos mais novos (Erro 2) dependem dos CT-es originais mais antigos estarem corrigidos primeiro. Corrigir fora de ordem pode dar a falsa impressão de que o ajuste "não resolveu", quando na prática ainda falta corrigir um CT-e anterior na cadeia.

Os CT-es que já são genuinamente do tipo Complemento de Valores não precisam ter o tipo alterado — eles voltam a importar normalmente assim que o CT-e original que referenciam estiver corrigido.

## Como contornar (cadastro de Tipos de Frete)

A classificação do pré-conhecimento (Normal, Complementar, etc.) é derivada automaticamente a partir do CFOP da nota fiscal, consultado no cadastro de Tipos de Frete (Cadastros Gerais > Cadastros Gerais Configurações da Empresa > Tipos de frete):

- Ao importar, o sistema busca nesse cadastro um registro para o CFOP informado na NF-e;
- Se encontra, cria o pré-conhecimento já com o tipo configurado ali;
- Se não encontra, assume o tipo Normal por padrão.

**Contorno recomendado**: identificar o CFOP das NF-es que vêm gerando pré-conhecimento Complementar sem par Normal, e cadastrá-lo em Tipos de Frete, definindo ali o "Tipo do conhecimento" desejado (Normal) antes de salvar. Assim, ao receber futuramente uma NF-e com esse CFOP, o sistema já cria o pré-conhecimento no tipo correto automaticamente, sem necessidade de ajuste manual depois.

Esse cadastro não corrige os documentos que já falharam — apenas evita que novos CT-es caiam no mesmo problema.

**Como solicitar suporte**: Caso haja dificuldade em localizar ou ajustar o pré-conhecimento, ou o CT-e original referenciado realmente não exista na base, abra um chamado com o suporte Lincros informando:

- Número/chave de acesso do CT-e com erro;
- Se for o Erro 2, a chave de acesso do CT-e original referenciado (infCteComp/chCTe);
- Print da mensagem de erro na importação;
- Se houver mais de um documento afetado, a lista completa para avaliação do efeito cascata.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
