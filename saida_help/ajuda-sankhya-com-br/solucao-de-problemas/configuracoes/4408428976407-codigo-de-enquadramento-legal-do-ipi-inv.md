---
id: "4408428976407"
titulo: "Código de Enquadramento Legal do IPI inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4408428976407-C%C3%B3digo-de-Enquadramento-Legal-do-IPI-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-15T19:18:09Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "#validadoRaiane", "Correção de Enquadramento Legal do IPI"]
---

# Código de Enquadramento Legal do IPI inválido

**![Mensagem](https://ajuda.sankhya.com.br/hc/article_attachments/15977010164119)  MENSAGEM**:

387 - Código de Enquadramento Legal do IPI inválido.

**![Causa](https://ajuda.sankhya.com.br/hc/article_attachments/15977010166295) CAUSA:**

Quando for emitida uma NF-e com Código de Enquadramento Legal do IPI (cEnq) preenchido com valor que não existe no [Anexo XIV](http://www.oobj.com.br/bc/assets/cEnq.pdf), será retornado a rejeição "387 - Código de Enquadramento Legal do IPI inválido".

**![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/15977010167959) SOLUÇÃO:**

Um erro muito comum dos usuários é informar códigos que ainda não foram publicados pela Sefaz em decorrência das regras de validação abaixo:

Se CST = "02" ou "52", informar cEnq com um valor entre "301" e "399";

Se CST = "04" ou "54", informar cEnq com um valor entre "001" e "099";

Se CST = "05" ou "55", informar cEnq com um valor entre "101" e "199";

Para os demais casos, informar cEnq com um valor entre "601" e "608" ou "999".

Para corrigir, informe o código que esteja dentro do intervalo aceito para cada CST

Corrigido o Código de Enquadramento Legal do IPI, reenvie a NF-e para processamento.

**Exemplo:**

Foi emitida uma NF-e com CST de IPI igual a 52 e com o Código de Enquadramento Legal do IPI (cEnq) igual a 399. Como o Código de Enquadramento informado não existe na tabela disponibilizada pela Sefaz, a NF-e será rejeitada pelo motivo 387.

No XML:

| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30 | `<``imposto``>`  `<``ICMS``>`  `<``ICMS40``>`  `<``orig``>0</``orig``>`  `<``CST``>50</``CST``>`  `</``ICMS40``>`  `</``ICMS``>`  `<``IPI``>`  `<``cEnq``>399</``cEnq``>`  `<``IPINT``>`  `<``CST``>52</``CST``>`  `</``IPINT``>`  `</``IPI``>`  `<``PIS``>`  `<``PISAliq``>`  `<``CST``>01</``CST``>`  `<``vBC``>221.44</``vBC``>`  `<``pPIS``>1.65</``pPIS``>`  `<``vPIS``>3.65</``vPIS``>`  `</``PISAliq``>`  `</``PIS``>`  `<``COFINS``>`  `<``COFINSAliq``>`  `<``CST``>01</``CST``>`  `<``vBC``>221.44</``vBC``>`  `<``pCOFINS``>7.60</``pCOFINS``>`  `<``vCOFINS``>16.82</``vCOFINS``>`  `</``COFINSAliq``>`  `</``COFINS``>`  `</``imposto``>` |
| --- | --- |

No TXP-SP:

N|
N06|0|50|||
O||||| **399**|
O08| **52**|
Q|
Q02|01|221.44|1.65|3.65|
S|
S02|01|221.44|7.60|16.82|

Veja regra de validação da Sefaz:

![Imagem 4: Veja regra de validação da Sefaz:](http://www.oobj.com.br/bc/assets/Articles/359/Rej387_NFE.png)
