---
id: "44010589842711"
titulo: "[TMS] - Erro na importação do CT-e - ORDEM DE COLETA: \"Transportadora diferente da transportadora do conhecimento\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010589842711--TMS-Erro-na-importa%C3%A7%C3%A3o-do-CT-e-ORDEM-DE-COLETA-Transportadora-diferente-da-transportadora-do-conhecimento"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T18:40:49Z"
rotulos: ["sync_hc", "lincros", "lincros_16497580", "sync_hash_001662072fcf"]
---

# [TMS] - Erro na importação do CT-e - ORDEM DE COLETA: "Transportadora diferente da transportadora do conhecimento"

## 1 - Problema Relatado pelo Cliente

Ao importar um arquivo XML de CT-e, o sistema recusa a importação e a coluna "Situação" exibe **"Importado com erros"**, com a seguinte mensagem na coluna "Mensagem":

"A transportadora [Nome da Transportadora do CT-e] da ordem de coleta[Número] é diferente da transportadora [Nome da Transportadora do Conhecimento] do conhecimento[Número]"

O cliente não consegue tratar o erro pela tela, pois a opção "Tratar erro" não fica disponível para esse tipo de bloqueio, e o CT-e permanece sem vínculo.

## 2 - Por que esse erro acontece

Esse bloqueio é um comportamento esperado do sistema, e não uma falha de integração. Ele existe para proteger a integridade dos seus dados fiscais.

Quando uma ordem de coleta é criada, ela já fica vinculada a uma transportadora específica (o "conhecimento"). Se chega um CT-e cujo emissor é uma transportadora diferente daquela já vinculada a essa mesma ordem de coleta, o sistema entende que há uma divergência entre o que foi planejado (ordem de coleta) e o que foi efetivamente executado ou emitido (CT-e), e bloqueia a importação automática para evitar que dois documentos fiscais de transportadoras diferentes fiquem associados ao mesmo processo por engano.

Na prática, esse erro costuma acontecer por um destes dois motivos:

- **Cenário 1 - Redespacho:** a carga foi transferida para uma segunda transportadora no meio do trajeto (transbordo), e o CT-e dessa segunda etapa está sendo importado como se fosse o mesmo conhecimento da primeira transportadora.
- **Cenário 2 - Divergência de cadastro:** a ordem de coleta foi criada, ou o conhecimento foi vinculado, com uma transportadora diferente daquela que realmente emitiu o CT-e (por exemplo, por erro de digitação, troca de transportadora de última hora sem atualizar o sistema, ou necessidade de uma carta de correção).

## 3 - Como identificar qual cenário se aplica ao seu caso

Antes de aplicar a solução, confirme com sua equipe de logística/roteirização:

- A carga realmente passou por mais de uma transportadora até chegar ao destino (baldeação/transbordo)? Se sim, é o **Cenário 1 (Redespacho)**.
- A transportadora que emitiu o CT-e é a única responsável pelo transporte, e o cadastro da ordem de coleta é que está errado? Se sim, é o **Cenário 2 (Divergência de cadastro)**.

## 4 - Cenário 1: Redespacho (mais de uma transportadora na mesma carga)

Nesse caso, o CT-e da segunda transportadora não deve ser forçado dentro do conhecimento já existente. Ele precisa ser reconhecido pelo sistema como uma **nova etapa de transporte (redespacho)**.

**Como resolver:**

1. Confirme com o setor de logística que houve de fato uma transferência de carga entre transportadoras.
2. Verifique se o XML da nota fiscal contém a informação de redespacho. Sem essa informação, o sistema não consegue gerar o conhecimento de redespacho automaticamente.
3. Configure ou solicite ao emissor da nota fiscal que inclua a informação de redespacho no XML, seguindo o passo a passo do artigo: [Gerar conhecimento de redespacho de forma automática](https://sankhya.zendesk.com/hc/pt-br/articles/44010117758487).
4. Caso precise criar esse conhecimento de redespacho manualmente para destravar o caso pontual, siga: [Como criar um pré-conhecimento de redespacho manualmente](https://sankhya.zendesk.com/hc/pt-br/articles/44010498527127).
5. Após o ajuste, reimporte o CT-e ou utilize a ação "Reprocessar" na tela de CT-e.

## 5 - Cenário 2: Divergência de cadastro (transportadora errada na ordem de coleta)

Nesse caso, o transporte foi feito por apenas uma transportadora, mas o sistema tem cadastrada uma transportadora diferente da que emitiu o CT-e. É preciso corrigir manualmente o vínculo no pré-conhecimento.

**Como resolver:**

1. Acesse: **Operacional > Cargas > Pré-conhecimento > Edição de pré-conhecimento**.
2. Localize o pré-conhecimento indicado na mensagem de erro.
3. Acesse a aba **Transporte** e, dentro dela, a aba **Transportadora**.
4. Corrija o campo **Transportadora** (e a **Filial**, se aplicável) para a transportadora correta, ou seja, a mesma que emitiu o CT-e.
5. Clique em **Salvar**.
6. **Atenção:** se esse pré-conhecimento já estiver vinculado a um embarque, o sistema valida se a transportadora do pré-conhecimento é a mesma do embarque. Se for necessário trocar a transportadora, pode ser preciso remover o pré-conhecimento do embarque antes, já que ele deixa de compor aquele frete.
7. Após corrigir, reimporte o CT-e ou utilize a ação "Reprocessar" na tela de CT-e.

Passo a passo detalhado com imagens: [Como alterar Transportadora do Pré-conhecimento após importar a Carta de Correção](https://suporte.lincros.com/pt-BR/articles/13433410-tms-como-alterar-transportadora-do-pre-conhecimento-apos-importar-a-carta-de-correcao).

## 6 - Pontos importantes

- Esse bloqueio não tem opção de "forçar" pela tela porque envolve dois documentos fiscais de transportadoras diferentes. A correção precisa ser feita na origem (cadastro do pré-conhecimento) antes da reimportação.
- Se o CT-e já vinculado ao conhecimento estiver **cancelado**, o sistema trata esse caso de forma um pouco diferente. Se você receber uma mensagem mencionando CT-e cancelado, entre em contato com o suporte para orientação específica.
- Em casos com grande volume de CT-es afetados pelo mesmo motivo (por exemplo, dezenas ou centenas de documentos), entre em contato com o suporte antes de fazer correções manuais em massa. Pode haver uma causa comum (parametrização ou padrão de emissão) que, corrigida uma vez, evita que o erro se repita nos próximos documentos.

## 7 - Artigos Relacionados

- [Entendendo o CT-e no TMS: Como Criar, Importar, Validar e Gerenciar CT-e](https://suporte.lincros.com/pt-BR/articles/13433249-tms-entendendo-o-ct-e-no-tms-como-criar-importar-validar-e-gerenciar-ct-e)
- [Gerar conhecimento de redespacho de forma automática](https://sankhya.zendesk.com/hc/pt-br/articles/44010117758487)
- [Como criar um pré-conhecimento de redespacho manualmente](https://sankhya.zendesk.com/hc/pt-br/articles/44010498527127)
- [Como alterar Transportadora do Pré-conhecimento após importar a Carta de Correção](https://suporte.lincros.com/pt-BR/articles/13433410-tms-como-alterar-transportadora-do-pre-conhecimento-apos-importar-a-carta-de-correcao)
