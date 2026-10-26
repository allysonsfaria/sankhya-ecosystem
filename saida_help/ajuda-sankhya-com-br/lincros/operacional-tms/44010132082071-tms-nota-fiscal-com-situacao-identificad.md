---
id: "44010132082071"
titulo: "[TMS] - Nota fiscal com situação \"Identificada\": como resolver a pendência que bloqueia a fatura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010132082071--TMS-Nota-fiscal-com-situa%C3%A7%C3%A3o-Identificada-como-resolver-a-pend%C3%AAncia-que-bloqueia-a-fatura"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:30:32Z"
rotulos: ["sync_hc", "lincros", "lincros_17153888", "sync_hash_00f2497be5b9"]
---

# [TMS] - Nota fiscal com situação "Identificada": como resolver a pendência que bloqueia a fatura

**Menu**: Operacional > Documentos de despacho > Notas Fiscais

**Objetivo**: Entender por que uma nota fiscal com situação "Identificada" bloqueia a aceitação da fatura, e como resolver a pendência gerada por essa situação.

## Por que a pendência é criada

A situação **"Identificada"** ocorre quando a nota fiscal é criada automaticamente durante a correção de erros de importação de CT-e — normalmente quando o documento é importado via SEFAZ com Certificado Digital, antes de a NF-e completa estar disponível.

Enquanto a nota fiscal estiver com essa situação, o sistema cria automaticamente uma pendência de classificação "Situação Identificada" vinculada ao pré-conhecimento — e essa pendência **impede a aceitação da fatura** enquanto não for resolvida.

## Quando a pendência se resolve sozinha

A pendência é resolvida **automaticamente** assim que a nota fiscal deixa de estar com situação "Identificada" (por exemplo, após a importação correta da NF-e completa), desde que pelo menos uma destas condições seja atendida:

- O pré-conhecimento (conhecimento) possui apenas 1 documento fiscal vinculado; ou
- A descrição da pendência está vazia; ou
- A descrição da pendência contém a chave de acesso da nota fiscal.

Nesses casos, o sistema resolve a pendência sozinho e cria automaticamente uma providência registrando que a NF foi importada pelo sistema — nenhuma ação manual é necessária.

## Quando é preciso agir manualmente

Fora das condições acima — por exemplo, quando o conhecimento tem mais de um documento fiscal vinculado e a descrição da pendência não referencia a chave da nota — a resolução automática não ocorre. Nesse caso:

1. Vincule novamente uma providência à pendência;
2. Realize a resolução da pendência manualmente.

**Atenção:** a cada nova tentativa de importação da mesma NF, a pendência é reaberta e retorna para o status "Não Resolvida" — mesmo que já tenha sido resolvida manualmente antes. Se providências associadas a tentativas anteriores tiverem sido excluídas, será necessário vincular novas providências antes de resolver novamente.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
