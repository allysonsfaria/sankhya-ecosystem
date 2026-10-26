---
id: "44012725211287"
titulo: "[TMS] - Valor total do percentual de rateio excedeu 100%"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012725211287--TMS-Valor-total-do-percentual-de-rateio-excedeu-100"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:37:11Z"
rotulos: ["sync_hc", "lincros", "sync_hash_ea30ecc5f490", "lincros_13433308"]
---

# [TMS] - Valor total do percentual de rateio excedeu 100%

**Menu**: Operacional > Cargas > Embarque

**Objetivo:** Entender o motivo da mensagem "Valor total do percentual de rateio excedeu 100%" ser apresentada e o que fazer para corrigir a situação.

**Considerações:**

- Possuir embarque criado no TMS;

Abaixo segue os procedimentos:

No menu: Operacional > Cargas > Embarques, é possível que ao tentar recalcular o mesmo seja apresentada a seguinte mensagem: 'Valor total do percentual de rateio excedeu 100%', conforme imagem abaixo:

![Imagem 1: No menu: Operacional > Cargas > Embarques, é possível que ao tentar recalcular o mesmo seja apresentada a seguinte…](https://ajuda.sankhya.com.br/hc/article_attachments/44012700202391)

Essa mesma mensagem pode ocorrer também durante a importação de XML de NF-e, alterações em pré-conhecimentos, resolução de pendências, etc. A questão é que normalmente envolve embarques com pré-conhecimentos vinculados onde está ocorrendo rateio;

A correção, contudo, é bem simples e pra isso deve-se:

1. Acessar o menu: Operacional > Cargas > Embarques e selecionar o embarque vinculado ao documento que está sofrendo alteração;

2. Na aba 'pré-conhecimentos' deverá acessar cada um dos pré-conhecimentos vinculados ao embarque, e encontrar o pré-conhecimento que esteja sem vínculo com uma NF-e;

![Imagem 2: 2. Na aba 'pré-conhecimentos' deverá acessar cada um dos pré-conhecimentos vinculados ao embarque, e encontrar o…](https://ajuda.sankhya.com.br/hc/article_attachments/44012745412503)

![Imagem 3: 2. Na aba 'pré-conhecimentos' deverá acessar cada um dos pré-conhecimentos vinculados ao embarque, e encontrar o…](https://ajuda.sankhya.com.br/hc/article_attachments/44012715646871)

3. Tendo encontrado o pré-conhecimento sem vínculo com NF-e, deve-se realizar este vínculo ou remover o pré-conhecimento do embarque;

![Imagem 4: 3. Tendo encontrado o pré-conhecimento sem vínculo com NF-e, deve-se realizar este vínculo ou remover o…](https://ajuda.sankhya.com.br/hc/article_attachments/44012740789527)

-

![Imagem 5: -](https://ajuda.sankhya.com.br/hc/article_attachments/44012725871895)

Pelo fato do pré-conhecimento não ter nota fiscal e o mesmo estar em um embarque, o sistema não tem como calcular corretamente o rateio, visto que o mesmo é feito sobre o valor da nota fiscal, e por conta disso é apresentada a mensagem excedendo o limite do rateio.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
