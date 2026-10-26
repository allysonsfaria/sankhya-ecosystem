---
id: "44011068523543"
titulo: "[TMS] Recalcular Pré Conhecimento - Tipo de Movimento Não Localizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011068523543--TMS-Recalcular-Pr%C3%A9-Conhecimento-Tipo-de-Movimento-N%C3%A3o-Localizado"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T18:54:28Z"
rotulos: ["sync_hc", "lincros", "sync_hash_bebbb12b2260", "lincros_13439652"]
---

# [TMS] Recalcular Pré Conhecimento - Tipo de Movimento Não Localizado

**Menu:** Operacional > Cargas > Pré-conhecimentos;**Objetivo**: resolver a mensagem "Tipo de Movimento não localizado" ao recalcular um Pré-Conhecimento;
**Considerações:** isso ocorrerá apenas com componentes customizados;
**Resolvendo a mensagem:**

Quando um Pré-Conhecimento não está trazendo informações na aba "**Movimentos**", é natural ser acionado o botão "**Recalcular**". Porém, caso seja retornado a mensagem  "**Tipos de Movimento não localizado**", o Pré-Conhecimento não será recalculado:

![Imagem 1: Quando um Pré-Conhecimento não está trazendo informações na aba " Movimentos " , é natural ser acionado o botão "…](https://ajuda.sankhya.com.br/hc/article_attachments/44011056867479)

Isso ocorre, por conta de algum componente que consta no CT-e, não possuir preenchimento ou possuir um preenchimento inválido em seu cadastro, no campo "**Código Movimento**":

![Imagem 2: Isso ocorre, por conta de algum componente que consta no CT-e, não possuir preenchimento ou possuir um preenchimento…](https://ajuda.sankhya.com.br/hc/article_attachments/44011085133207)

![Imagem 3: Isso ocorre, por conta de algum componente que consta no CT-e, não possuir preenchimento ou possuir um preenchimento…](https://ajuda.sankhya.com.br/hc/article_attachments/44011101139863)

![Imagem 4: Isso ocorre, por conta de algum componente que consta no CT-e, não possuir preenchimento ou possuir um preenchimento…](https://ajuda.sankhya.com.br/hc/article_attachments/44011082131991)

**Cadastros gerais > Configurações da empresa > Componentes de frete**
Para resolver a mensagem, basta ajustar o cadastro informando um código existente/válido ou criar um novo código. Sobre a criação de novos **Tipos de Movimento** e de vinculá-los a componentes de frete, temos o artigo a baixo que demonstra o processo:

[https://lincros.movidesk.com/kb/article/292812/tms-tipos-de-movimento-no-cadastro-de-componente-de-frete?preview=true&revisionId=1169783a](https://lincros.movidesk.com/kb/article/292812/tms-tipos-de-movimento-no-cadastro-de-componente-de-frete?preview=true&revisionId=1169783)**Conclusão:** se faz necessário identificar todos os componentes que comportam o Pré-Conhecimento com o erro e validar cada cadastro, quanto ao **Tipo de Movimento**.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
