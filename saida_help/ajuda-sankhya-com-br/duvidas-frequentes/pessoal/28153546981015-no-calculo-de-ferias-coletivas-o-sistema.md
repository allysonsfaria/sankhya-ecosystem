---
id: "28153546981015"
titulo: "No cálculo de férias coletivas, o sistema está considerando mais dias de férias do que está sendo solicitado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28153546981015-No-c%C3%A1lculo-de-f%C3%A9rias-coletivas-o-sistema-est%C3%A1-considerando-mais-dias-de-f%C3%A9rias-do-que-est%C3%A1-sendo-solicitado"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:26:17Z"
rotulos: ["Configuração", "Folha de Pagamento", "Férias", "No cálculo de férias coletivas o sistema está considerando mais dias de férias", "Regras de Cálculo", "Recursos Humanos"]
---

# No cálculo de férias coletivas, o sistema está considerando mais dias de férias do que está sendo solicitado

**SITUAÇÃO:**

Calculando 19 dias de férias coletivas para alguns funcionários com menos de 1 ano de admissão, o sistema está considerando mais dias de férias do que está sendo informado no cálculo.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28154692370199)SOLUÇÃO:**

Acesse a tela Pessoal+ » Cadastros » Regras de Cálculo e na aba **"Férias"** verifique o campo **"Quita resíduos menores ou iguais a",** relacionado às férias coletivas.

Se, por exemplo, o valor configurado nesse campo for **10** e o funcionário em questão tiver direito a **25 dias** de férias no período aquisitivo, o sistema utilizará automaticamente no cálculo os **25 dias** para quitar os dias restantes. Dessa forma, não haverá 5 dias residuais, já que ele é inferior ao valor definido no campo.

Caso a empresa opte por calcular apenas os dias estabelecidos no cálculo, o campo **"Quita resíduos menores ou iguais a"** deverá ficar com o numeral **‘0’**, e consequentemente se o funcionário tiver direito a **25 dias** de férias, o período aquisitivo dele irá permanecer com um saldo de **5 dias**.

![Imagem 2: Caso a empresa opte por calcular apenas os dias estabelecidos no cálculo, o campo "Quita resíduos menores ou iguais a"…](https://ajuda.sankhya.com.br/hc/article_attachments/28153546975127)

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/28154710958743) **CAUSA:**

Na regra de calculo »  aba férias » férias coletivas, o campo Quita resíduos menores ou iguais que: Dias  está configurado com um valor diferente de ‘0’.
