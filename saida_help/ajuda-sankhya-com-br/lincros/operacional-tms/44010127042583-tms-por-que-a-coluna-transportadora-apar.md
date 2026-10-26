---
id: "44010127042583"
titulo: "[TMS] - Por que a coluna Transportadora aparece em branco na tela de Notas Fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010127042583--TMS-Por-que-a-coluna-Transportadora-aparece-em-branco-na-tela-de-Notas-Fiscais"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:31:01Z"
rotulos: ["sync_hc", "lincros", "lincros_17153887", "sync_hash_17ac60e89544"]
---

# [TMS] - Por que a coluna Transportadora aparece em branco na tela de Notas Fiscais

**Menu**: Operacional > Documentos de despacho > Notas Fiscais

**Objetivo**: Entender por que a coluna "Transportadora" pode aparecer em branco na listagem de Notas Fiscais, mesmo quando a informação está preenchida dentro da nota individualmente.

## Por que isso acontece

A coluna "Transportadora" na tela de listagem de Notas Fiscais não lê o dado diretamente da nota fiscal. Ela é preenchida a partir da transportadora cadastrada no **pré-conhecimento (conhecimento) vinculado** à nota — e não a partir de um campo próprio da NF.

Por isso, quando o pré-conhecimento é gerado automaticamente na importação da nota fiscal mas não retorna automaticamente a transportadora, a coluna fica em branco na listagem — mesmo que a informação apareça normalmente ao abrir a nota fiscal individualmente ou ao consultar o PDF/DANFE.

Esse comportamento é consistente em todos os usuários e telas de listagem: se todos os usuários enxergam o campo em branco para as mesmas notas, não se trata de uma questão de permissão de usuário, e sim da ausência da transportadora no pré-conhecimento vinculado.

## Como corrigir

Para que a coluna passe a exibir corretamente, é necessário preencher a transportadora diretamente no **pré-conhecimento** vinculado à nota fiscal em questão, e não na nota fiscal em si.

## Como o CT-e/pré-conhecimento chega ao sistema

O documento de transporte (CT-e) não é gerado automaticamente pelo Lincros a partir das notas fiscais — ele precisa ser recebido de alguma forma para que o vínculo aconteça:

1. **Integração automática (EDI/API)**: a transportadora envia os arquivos XML do CT-e diretamente para o sistema. É configurado no cadastro de cada transportadora dentro do Lincros, que precisa estar habilitada para receber documentos. Quando configurado, o CT-e chega, é processado e já fica vinculado às notas automaticamente.
2. **Importação manual**: caso a transportadora não tenha integração ativa, é possível importar os arquivos XML dos CT-es manualmente pelo caminho: Operacional > Importação — nessa tela também é possível consultar o histórico e o resultado de cada importação.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
