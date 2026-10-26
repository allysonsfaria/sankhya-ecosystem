---
id: "44010063637783"
titulo: "[TMS] - Erro de importação de CT-e: transportadora do CT-e diferente da transportadora da ordem de coleta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010063637783--TMS-Erro-de-importa%C3%A7%C3%A3o-de-CT-e-transportadora-do-CT-e-diferente-da-transportadora-da-ordem-de-coleta"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:29:26Z"
rotulos: ["sync_hc", "lincros_17269534", "lincros", "sync_hash_03eb8f5aba8b"]
---

# [TMS] - Erro de importação de CT-e: transportadora do CT-e diferente da transportadora da ordem de coleta

**Menu**:

CT-e = Documentos eletrônicos > CT-es

Pré-conhecimento = Operacional > Operacional Cargas > Pré-conhecimentos
Importar/reimportar o CT-e = Operacional > Importação > CT-e > Importação

**Objetivo**: Explicar por que a importação do CT-e é bloqueada com a mensagem "Alterada a transportadora do conhecimento [número] com ordem de coleta vinculada de transportadora [código]" e como corrigir.

**Considerações**:

- Possuir um CT-e com erro de importação contendo a mensagem acima;
- O pré-conhecimento citado na mensagem possui uma Ordem de Coleta vinculada.

## Por que ocorre esta situação?

O sistema valida se a transportadora do conhecimento é a mesma transportadora da Ordem de Coleta vinculada a ele. Quando o CT-e importado traz uma transportadora diferente da que está na Ordem de Coleta, a importação é bloqueada para evitar inconsistência entre o conhecimento e a ordem de coleta.

## Como identificar o que diverge

1. Acesse Documentos eletrônicos > CT-es, abra o CT-e com erro e, na seção 'Mensagem de importação', copie o número do pré-conhecimento citado na mensagem;
2. Abra o pré-conhecimento e localize a Ordem de Coleta vinculada;
3. Compare a transportadora da Ordem de Coleta com a transportadora emitente do CT-e;
4. Defina qual das duas está correta para este embarque e siga um dos caminhos abaixo.

## Cenário 1 — A transportadora da Ordem de Coleta está correta

O CT-e veio com uma transportadora diferente da esperada. Na tela de importação de XML (Operacional > Importação > CT-e > Importação), desmarque a opção "Usar a transportadora definida na NFe, se disponível", informe manualmente a transportadora correta e importe o arquivo novamente.

## Cenário 2 — A transportadora do CT-e está correta

A Ordem de Coleta é que está com a transportadora errada. Altere a transportadora diretamente na Ordem de Coleta (ao trocar, o sistema limpa automaticamente os vínculos da transportadora anterior, como o veículo) e depois reimporte o CT-e.

Se não for possível identificar qual transportadora está correta ou a importação continuar bloqueada após o ajuste, abra um chamado informando o número/chave do CT-e, o número do pré-conhecimento e da Ordem de Coleta, e o print da mensagem de importação.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
