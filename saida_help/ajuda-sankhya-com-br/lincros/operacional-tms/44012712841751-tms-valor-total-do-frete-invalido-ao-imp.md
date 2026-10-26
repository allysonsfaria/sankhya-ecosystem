---
id: "44012712841751"
titulo: "[TMS] - Valor total do frete inválido ao importar Ct-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012712841751--TMS-Valor-total-do-frete-inv%C3%A1lido-ao-importar-Ct-e"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:36:44Z"
rotulos: ["sync_hc", "lincros", "sync_hash_29fe22c4c689", "lincros_13433339"]
---

# [TMS] - Valor total do frete inválido ao importar Ct-e

**Menu**: Operacional > Importação > CT-e > Importação

**Objetivo**: Como corrigir o erro com a mensagem 'Valor do frete inválido' ao importar Ct-e

**Considerações**:

- Possuir  um XML para realizar a importação do CT-e e que apresenta a mensagem com o problema

Abaixo segue os procedimentos:
1. Realizar a importação  do CT-e através do menu: Operacional > Importação > CT-e > Importação;

![Imagem 1: Abaixo segue os procedimentos: 1. Realizar a importação do CT-e através do menu: Operacional > Importação > CT-e >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012738082327)

2. Caso seja apresentado a mensagem 'Valor total do frete inválido' no log da importação, verificar no arquivo XML do Ct-e a tag 'VTPRES', se a mesma possui valor:

![Imagem 2: 2. Caso seja apresentado a mensagem 'Valor total do frete inválido' no log da importação, verificar no arquivo XML do…](https://ajuda.sankhya.com.br/hc/article_attachments/44012698178711)

3. Caso o valor da tag 'VTPres' estiver zerado não será possível efetuar a importação do arquivo ocorrendo a mensagem de erro informada acima;

4. Neste caso, deve ser solicitado à transportadora um novo arquivo XML com este campo preenchido;

5. Após o envio do novo arquivo realizar a importação novamente.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
