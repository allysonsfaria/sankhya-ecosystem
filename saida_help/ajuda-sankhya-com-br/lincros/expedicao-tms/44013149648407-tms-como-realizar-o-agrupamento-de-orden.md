---
id: "44013149648407"
titulo: "[TMS] - Como realizar o agrupamento de ordens de coleta no arquivo EDI (NOTIFIS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013149648407--TMS-Como-realizar-o-agrupamento-de-ordens-de-coleta-no-arquivo-EDI-NOTIFIS"
trilha: "Lincros > TMS > Expedição - TMS"
atualizado_em: "2026-10-05T19:49:13Z"
rotulos: ["sync_hc", "lincros", "sync_hash_045aa0c1c207", "lincros_13432917"]
---

# [TMS] - Como realizar o agrupamento de ordens de coleta no arquivo EDI (NOTIFIS)

**Menu**: Expedição > Coletas > Ordem de Coleta

**Objetivo**: Como realizar o agrupamento de ordens de coleta no arquivo EDI (NOTIFIS)

## Considerações:

- Possuir notas fiscais importadas no sistema;
- Possuir ordens de coletas cadastradas no sistema;

Abaixo segue os procedimentos:

1. Na ordem de coleta existe a opção 'Agrupar conhecimentos',o qual possui a mesma funcionalidade do botão 'Forçar união' na tela de pré-conhecimentos;
2. Para que o agrupamento ocorra, é necessário que a origem, destino, remetente e destinatário dos conhecimentos existentes na ordem de coleta sejam iguais, caso contrário não irá agrupá-los.;
3. No NOTIFIS, quando não há agrupamento, é gerada a linha 312, que se refere ao destinatário, e logo em seguida a linha 313, que se refere aos dados da nota fiscal, e em seguida novamente linha 312 e 313, a assim por diante, conforme layout do NOTIFIS padrão proceda que consta em anexo;
4. Já quando houver agrupamento, irá ter a linha 312, e logo abaixo poderá ter diversas linhas 313 (até 40 de acordo com o layout), que se referem a nota fiscal do mesmo destinatário informado na linha 312;
5. Dessa forma a transportadora irá entender que todas as notas abaixo da linha 312, irão se referir apenas a um destinatário, e consequentemente a transportadora poderá emitir apenas um CT-e vinculando todas essas notas juntas, sem necessidade de separação.

Abaixo segue um exemplo:

-> Arquivo NOTIFIS (EDI) sem o agrupamento:

![Imagem 1: -> Arquivo NOTIFIS (EDI) sem o agrupamento:](https://ajuda.sankhya.com.br/hc/article_attachments/44013166826519)

-> Arquivo NOTIFIS (EDI) com o agrupamento:

![Imagem 2: -> Arquivo NOTIFIS (EDI) com o agrupamento:](https://ajuda.sankhya.com.br/hc/article_attachments/44013158755479)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
