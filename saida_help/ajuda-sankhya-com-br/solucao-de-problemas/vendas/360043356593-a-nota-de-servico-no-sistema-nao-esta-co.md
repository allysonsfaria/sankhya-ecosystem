---
id: "360043356593"
titulo: "A nota de serviço no sistema não está com o mesmo número de RPS da prefeitura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043356593-A-nota-de-servi%C3%A7o-no-sistema-n%C3%A3o-est%C3%A1-com-o-mesmo-n%C3%BAmero-de-RPS-da-prefeitura"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:44Z"
rotulos: ["#RevisadoGui", "Fiscal", "Prefeituras", "NFS-e", "Números divergentes", "Não é um problema", "Processo normal", "Erro"]
---

# A nota de serviço no sistema não está com o mesmo número de RPS da prefeitura

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16109398268439) SITUAÇÃO:**

A nota de serviço no sistema não está com o mesmo número de RPS da prefeitura.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16109398270871) SOLUÇÃO:**

Esta situação pode sim ocorrer e neste caso não há o que resolver. Nem sempre irá coincidir, pois a aplicação envia o **"Número do RPS"** para a Prefeitura, que após o processamento e autorização gera um "Número de NFS-e", que é retornado para o sistema e é gravado no campo **"Nro. NFS-e"** (TGFCAB.NUMNFSE) e não necessariamente deverá ser igual ao Número do RPS"(TGFCAB.NUMNOTA).

Não há como "acertar" para que ambos os campos sejam iguais novamente, pois a gravação de "Número de NFS-e" é sequencial e controlado pela Prefeitura.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16109561375511) CAUSA:**

Isso ocorre em casos em que é gerado uma nota diretamente pelo Portal da Prefeitura, e posteriormente é gerado uma nota pelo sistema, neste caso, o Número do RPS será diferente, exemplo:

| **Núm. RPS** | **Núm. NFSe** | **Emitido onde?** |
| --- | --- | --- |
| 1 | 1 | Sistema |
| 2 | 2 | Sistema |
|  | 3 | Portal da Prefeitura |
| 3 | 4 | Sistema |
| 4 | 5 | Sistema |
