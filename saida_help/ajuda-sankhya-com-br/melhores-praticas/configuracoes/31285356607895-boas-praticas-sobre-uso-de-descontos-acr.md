---
id: "31285356607895"
titulo: "Boas práticas sobre uso de Descontos/Acréscimo em JSON de integração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31285356607895-Boas-pr%C3%A1ticas-sobre-uso-de-Descontos-Acr%C3%A9scimo-em-JSON-de-integra%C3%A7%C3%A3o"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T14:33:24Z"
rotulos: ["Parceiro", "Descontos", "Integração", "API", "JSON", "JSON da API de integração com o Sankhya", "playload", "Descontos/Acréscimo", "integrações", "API integração Sankhya", "Acréscimos"]
---

# Boas práticas sobre uso de Descontos/Acréscimo em JSON de integração

A partir das **versões 4.32b60, 4.33b18 e 4.34b3**, os **parceiros integradores** possuem maior **flexibilidade** para **enviar descontos e acréscimos na integração de pedidos ou notas.**

**Anteriormente, o cálculo era restrito ao campo PERCDESC**, limitando-se a percentuais e impossibilitando o uso de valores fixos. **Com a atualização, é possível optar por diferentes abordagens para o cálculo de descontos e acréscimos.**

#### Conheça os cenários que podem ser adotados pelos parceiros integradores na criação do JSON da API de integração com o Sankhya:

**(1)** **Cenário 1:** **Valor de Desconto no Total da Nota como Base**

- Informe o atributo **"VLRDESCTOT"** no **cabeçalho** da nota no payload;
- No **Item**, informe o campo **“PERCDESC”** com valor 0.
- O sistema **calculará** o **percentual total de desconto** e o **valor total** com **base no Valor de Desconto** informado no cabeçalho.

**(1)** **Cenário 2:** **Valor de Desconto por Item como Base**

- Informe o atributo **"VLRDESC"** em cada **Item** do payload;
- No **Item**, informe o campo **“PERCDESC”** com valor 0;
- O sistema **calculará** o **percentual** e o **valor de desconto total por item** com **base no valor informado**.

**(1)** **Cenário 3:** **Percentual de Desconto como Base no cabeçalho**

- Informe o atributo **"PERCDESC"** no **cabeçalho** da nota no payload;
- No **Item**, informe o campo **“PERCDESC”** com valor 0;
- O sistema **calculará** o **valor de desconto total** da nota com **base no percentual informado.**

**(1)** **Cenário 4:** **Percentual de Desconto como Base no item**

- Informe o atributo **"PERCDESC"** com o percentual desejado no **Item** no payload;
- O sistema **calculará** o **valor de desconto total por item** com **base no percentual informado**.

(1)** Comportamento para Acréscimos:**

No Sankhya, não existe um campo exclusivo para o registro de valores de acréscimo. Dessa forma, para adicionar um acréscimo, informe um sinal negativo no atributo em questão. Assim, o sistema interpreta automaticamente como um acréscimo:

- **Exemplo:** “-10.00” será considerado 10% de acréscimo.

No **Item** ou **cabeçalho**, só será considerado o acréscimo caso seja enviado no **PERCDESC**. Não será considerado o envio de acréscimo no **VLRDESC**.

(1)** Observações Importantes:**

- Evite informar descontos no cabeçalho e descontos por item no mesmo payload.
- Quando se trata de uma **alteração de itens** já **existentes** no **pedido/nota**, **passe** tanto o **PERCDESC** quanto o **VLRDESC.** Pois, quando se trata de alterações, passando apenas um dos campos o outro ficará em branco.
