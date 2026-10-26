---
id: "44012674253463"
titulo: "[TMS] - Previsão de entrega a partir da ordem de coleta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012674253463--TMS-Previs%C3%A3o-de-entrega-a-partir-da-ordem-de-coleta"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:36:04Z"
rotulos: ["sync_hc", "lincros", "lincros_13433369", "sync_hash_8e8146c879cd"]
---

# [TMS] - Previsão de entrega a partir da ordem de coleta

**Menu:** Operacional > Cargas > Pré-conhecimentos

**Objetivo**: Como configurar o sistema para que a previsão de entrega comece a contar a partir da data mínima/máxima da ordem de coleta.

## Considerações:

- Possuir ordem de coleta vinculada ao pré-conhecimento;
- Ordem de coleta precisa estar com a situação ‘Enviado à transportadora’ ou ‘Confirmada’ para que o sistema pegue a data base para calcular a previsão de entrega;
- Possuir configuração de empresa como ‘true’ conforme será apresentado abaixo.

## Configurações de empresa

Para que a previsão de entrega pegue como 'data base' a 'data mínima/máxima da ordem de colet'a, é necessário possuir o parâmetro ‘considerarDataMinimaColetaPrevisao’ ou ‘considerarDataMaximaColetaPrevisao’ como ‘true’.

No momento que o parâmetro mínimo estiver como ‘true’, será desconsiderado o parâmetro máximo, e vice-versa.

![Imagem 1: No momento que o parâmetro mínimo estiver como ‘true’, será desconsiderado o parâmetro máximo, e vice-versa.](https://ajuda.sankhya.com.br/hc/article_attachments/44012667771543)

![Imagem 2: No momento que o parâmetro mínimo estiver como ‘true’, será desconsiderado o parâmetro máximo, e vice-versa.](https://ajuda.sankhya.com.br/hc/article_attachments/44012704588695)

É necessário também que o parâmetro ‘considerarDataCtePrevisaoEntrega’ esteja como ‘false’ para que o sistema considere um dos parâmetros informados acima.

## Regras para o parâmetro ser utilizado

Para que a data base para cálculo do prazo seja de acordo com a data mínima/máxima da ordem de coleta, é necessário primeiro que o pré-conhecimento esteja vinculado a uma ordem de coleta.

![Imagem 3: Para que a data base para cálculo do prazo seja de acordo com a data mínima/máxima da ordem de coleta, é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/44012674811287)

Se o parâmetro ‘considerarDataMinimaColetaPrevisao’ estiver como ‘true’, a data base para o cálculo será a data mínima da ordem de coleta. Já se o parâmetro ‘considerarDataMaximaColetaPrevisao’ estiver como ‘true’, a data base para o cálculo será a data máxima da ordem de coleta.

![Imagem 4: Se o parâmetro ‘considerarDataMinimaColetaPrevisao’ estiver como ‘true’, a data base para o cálculo será a data mínima…](https://ajuda.sankhya.com.br/hc/article_attachments/44012689676951)

A situação da ordem de coleta precisa seguir a regra de estar com a situação ‘Enviada à transportadora’, quando o usuário da empresa realiza o envio por e-mail da ordem de coleta, ou com a situação ‘Confirmada’, quando o usuário de transportadora confirma a ordem de coleta pelo portal do transportador.

![Imagem 5: A situação da ordem de coleta precisa seguir a regra de estar com a situação ‘Enviada à transportadora’, quando o…](https://ajuda.sankhya.com.br/hc/article_attachments/44012694424855)

No exemplo apresentado, o parâmetro que está como ‘true’ é o ‘considerarDataMinimaColetaPrevisao’, portanto a data base para calcular o prazo de entrega seria 23/02.

Ao entrarmos no pré-conhecimento, no campo ‘Previsão entrega transportadora’, se passarmos o mouse por cima do mesmo, irá mostrar esta data base para cálculo.

Os dias da previsão irão contar de acordo com o prazo cadastrado no menu Cadastros gerais > Transportadoras > Negociações > Prazos de entrega > Transportadora.

![Imagem 6: Os dias da previsão irão contar de acordo com o prazo cadastrado no menu Cadastros gerais > Transportadoras >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012705101463)

**Obs.:** A partir do momento que o campo ‘Data de coleta’ estiver preenchido, a base da previsão passa a contar a partir da data que estiver neste campo.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
