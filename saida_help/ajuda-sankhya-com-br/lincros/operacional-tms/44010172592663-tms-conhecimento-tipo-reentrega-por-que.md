---
id: "44010172592663"
titulo: "[TMS] - Conhecimento tipo Reentrega: por que a data de entrega não é preenchida automaticamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010172592663--TMS-Conhecimento-tipo-Reentrega-por-que-a-data-de-entrega-n%C3%A3o-%C3%A9-preenchida-automaticamente"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:31:03Z"
rotulos: ["sync_hc", "lincros", "lincros_17153886", "sync_hash_2566a8f494dd"]
---

# [TMS] - Conhecimento tipo Reentrega: por que a data de entrega não é preenchida automaticamente

**Menu**: Entregas e Ocorrências > Acompanhamento de entregas

**Objetivo**: Entender por que um conhecimento do tipo Reentrega não tem a data de entrega preenchida automaticamente, mesmo após uma nova tentativa de entrega.

## Comportamento do sistema

Conhecimentos do tipo **Reentrega** e **Complementar** possuem um comportamento em comum: ambos são criados já com o status "Transportado" — diferente de um conhecimento Normal, que segue o fluxo padrão de baixa de entrega.

A diferença está em quando a data de entrega é populada:

- **Complementar**: é gerado no momento da importação da nota fiscal, quando a data de entrega já existe e é associada a ele naquele instante — por isso normalmente já exibe a data.
- **Reentrega**: é criado fora do fluxo de importação, em um momento posterior. O ponto "reentrega" na régua de eventos usa a **data de emissão do conhecimento** como referência, e não dispara o ponto de "entrega normal" — por isso a coluna de entrega fica sem preenchimento automático, mesmo que a mercadoria já tenha sido reentregue fisicamente.

Esse é o comportamento esperado do sistema, não um erro ou falha de configuração.

## Como fazer a data de entrega aparecer

Para que a data de entrega apareça no conhecimento de reentrega, é necessário que uma ocorrência de entrega seja lançada e vinculada a esse conhecimento especificamente. Isso pode ser feito de três formas:

- Via integração da transportadora (EDI/API);
- Por arquivo/EDI enviado manualmente;
- Registrada manualmente na tela do conhecimento.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
