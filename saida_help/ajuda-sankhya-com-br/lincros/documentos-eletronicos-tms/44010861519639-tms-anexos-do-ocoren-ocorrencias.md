---
id: "44010861519639"
titulo: "[TMS] - Anexos do OCOREN (ocorrências)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010861519639--TMS-Anexos-do-OCOREN-ocorr%C3%AAncias"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T18:48:24Z"
rotulos: ["sync_hc", "lincros", "lincros_13432820", "sync_hash_d06fe88c6a02"]
---

# [TMS] - Anexos do OCOREN (ocorrências)

**Menu**: Documentos eletrônicos > NF-es > Edição de nota fiscal > Aba 'Ocorrências'

**Objetivo**: Como realizar a importação de um anexo a uma ocorrência através do e-mail ou FTP

**Considerações**:

- Se o envio dos anexos for feito pelo FTP, é necessário realizar a configuração de acordo com a documentação ['[TMS] - Cadastro de FTP das transportadoras'](https://sankhya.zendesk.com/hc/pt-br/articles/44010861519639).

## Configurando o anexo

É possível enviar anexos aos eventos de ocorrência através da importação de arquivos via e-mail ou FTP. Os anexos devem seguir a nomenclatura a seguir:

![Imagem 1: É possível enviar anexos aos eventos de ocorrência através da importação de arquivos via e-mail ou FTP. Os anexos devem…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963155080/9a17d85c1d66659dfaffe02c9ec5/6B35DF4D70B30A612C61241005239BD6?expires=1791331200&signature=93aae70e9d5bd74e6f1d49977289159af69ab1404e972dcafbc6642cd68c0393&req=dSkhFch7mIFXWfMW3nq%2Bgc42TZYSE2Q2T7dn7pmI9KGS%2F%2FVPJr2A6MDnZ33y%0AusG9NapkTL0AbW2DA1re%2Bv7bTEI%3D%0A)

Devem ser informados todos os zeros para preenchimento dos campos, exemplo: 1/5/2020 na data deverá ser 01052020.

O nome dos arquivos deverá obedecer ao padrão da expressão regular abaixo:

![Imagem 2: O nome dos arquivos deverá obedecer ao padrão da expressão regular abaixo:](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963155084/f3d77995f18266b1e4e30695d0cb/9C7BC84269883F93E0AF0318EABC4F0C?expires=1791331200&signature=49ddf74eaf3dc4ecb559cb6d92dcd834885f768f78e23d0bbceb0b3c3c5f5ef3&req=dSkhFch7mIFXXfMW3nq%2BgUSUKGJy%2BLASzd8mwtakJ%2BmOIpEcopLCtT5xXBuw%0AqjRcM3nL8%2BXNfYnXbDTgU7%2B%2F2V0%3D%0A)

O anexo é importado de forma assíncrona por e-mail ou FTP e vinculado na ocorrência.

![Imagem 3: O anexo é importado de forma assíncrona por e-mail ou FTP e vinculado na ocorrência.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963155092/0beaf998805d4b299486b85eecce/9FF45448663CDBD371C406D9C88764CE?expires=1791331200&signature=2973c8ccee33b6491569309587906b28ccda0dd97fee721d66b3930c611b9ed4&req=dSkhFch7mIFWW%2FMW3nq%2BgcIZoYjbKRmvNkPbZV1vW%2BFmr77tvJrSCyswM1sl%0AVF%2B048o9X84EjZB7JVJLAMDxgJ0%3D%0A)

**Obs.:** Caso não seja encontrado uma Nota Fiscal, ou não seja encontrado uma ocorrência, será criado uma pendência de arquivo. Esta pendência é resolvida e o anexo reprocessado no momento que a ocorrência e a NF-e são importados no sistema.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
