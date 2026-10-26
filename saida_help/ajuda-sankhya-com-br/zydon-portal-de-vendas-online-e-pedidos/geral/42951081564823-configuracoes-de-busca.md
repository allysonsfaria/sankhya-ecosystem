---
id: "42951081564823"
titulo: "Configurações de Busca"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951081564823-Configura%C3%A7%C3%B5es-de-Busca"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T13:54:14Z"
rotulos: ["zydon", "sync_hc", "zydon_213266014760", "sync_hash_35b43822ea55"]
---

# Configurações de Busca

## A funcionalidade de Busca de Produtos permite configurar a forma como os resultados são exibidos no portal B2B, otimizando a navegação e tornando a experiência do usuário mais eficiente e direcionada. Com os ajustes certos, é possível garantir que os produtos mais relevantes apareçam primeiro, de acordo com o comportamento de pesquisa e os objetivos do seu negócio.

**Acesso**

1. No menu lateral esquerdo, localize e clique em **Loja Virtual**.
2. Acesse **Minha loja B2B**.
3. Escolha a jornada que deseja configurar:

   - Cliente
   - Vendedor
4. Na pré-visualização do portal, localize o campo **Busca de produtos**, logo no início da tela.

[![Imagem 1: Na pré-visualização do portal, localize o campo Busca de produtos , logo no início da tela.](https://ajuda.sankhya.com.br/hc/article_attachments/42951081867287)](https://downloads.intercomcdn.com/i/o/jgm6ml00/1759310295/c1c4698b7c250dd9f81bfad5c3dc/image.png?expires=1779296400&signature=8458aba2069f38b40e5551578d5a6c195ee030511ec4aaa83c22fb84a3ac3988&req=dSciH8p%2FnYNWXPMW1HO4zT7%2B%2B9F74FJx3WmT9lard9zbjrrKSUhJ5wSz7tHz%0ACiMX%0A)

Funcionalidades disponíveis

**Placeholder do Campo**

- Texto exibido dentro do campo de busca antes do usuário digitar algo.
- Serve como **orientação** sobre o que pode ser pesquisado (ex: “Digite o nome do produto, marca ou código”).

**Habilitar "Mais Buscados"**

- Exibe uma **lista lateral** com os termos mais pesquisados, relacionados ao que foi digitado.
- Auxilia o usuário com sugestões automáticas.

**Habilitar Busca por Marca**

- Exibe uma **lista lateral de marcas** relacionadas ao termo pesquisado.
- Ideal para destacar marcas populares ou estratégicas.

**Habilitar Busca por Categoria**

- Mostra uma **lista de categorias** relacionadas aos termos digitados.
- Ajuda o usuário a refinar a busca por segmento de produto.

**Prioridade para Palavras à Esquerda**

- Quando ativada, a busca considera com **maior relevância os termos digitados primeiro** (da esquerda para a direita).
- Exemplo: ao buscar "camisa polo", os resultados que contêm "camisa" no início do nome terão prioridade sobre aqueles que contêm "polo" primeiro.

**Exemplo:**

Se a busca for **"JOELHO SOLDÁVEL 45mm"**, os resultados serão exibidos na seguinte ordem:

1. Produtos com o nome exato **"JOELHO SOLDÁVEL 45mm"** aparecem primeiro.
2. Em seguida, produtos que contêm **"JOELHO SOLDÁVEL"** no nome.
3. Depois, produtos com **"JOELHO 45mm"**.
4. Em seguida, produtos com apenas **"JOELHO"**.
5. Depois, produtos com **"SOLDÁVEL 45mm"**.
6. Em seguida, produtos com apenas **"SOLDÁVEL"**.
7. Por fim, produtos que contêm apenas **"45mm"** no nome.

Essa lógica garante uma busca mais direcionada e relevante para o usuário, respeitando a sequência das palavras digitadas.

## Defina os campos de busca

1. **Campo**

   - Selecione o campo chave que será utilizado como base para as buscas.
2. **Peso**

   - Defina o peso do campo em uma escala de **0,5 a 5**, sendo **5** o de maior relevância.
   - Essa configuração influencia a prioridade que o sistema dará a esse campo ao listar os resultados.
3. **Nível de Correção**

   O **Nível de Correção** é uma funcionalidade que define o grau de tolerância para erros de digitação ou ortografia nos termos de busca inseridos pelos usuários. Essa configuração é especialmente útil para garantir resultados mais relevantes, mesmo em casos de erros simples.

   **Opções Disponíveis**

   1. **Automática**

      - A correção ocorre de forma automática, com maior tolerância a erros.
      - Para palavras com até **três caracteres**, será aplicada **uma correção automática**.
      - Para palavras com até **seis caracteres**, serão aplicadas **duas correções automáticas**.
   2. **Alta**

      - Permite uma margem de até **dois erros ortográficos entre o** termo digitado e a palavra buscada.
   3. **Baixa**

      - Permite uma margem de até **um erro ortográfico entre o** termo digitado e a palavra buscada.
   4. **Nenhum**

      - Não aplica correções. Caso a palavra seja digitada incorretamente, a busca não retornará resultados.

   Essa funcionalidade oferece maior flexibilidade para os usuários, tornando o processo de busca mais eficiente, mesmo em situações onde há pequenos erros de digitação.
4. **Nível de Similaridade**

   - Configure como o sistema interpretará os termos de busca, ajustando o grau de flexibilidade e precisão.

   **Opções de Similaridade**:

   - **Palavra-chave**

     - Realiza buscas parciais e flexíveis.
     - Retorna resultados que contenham qualquer uma das palavras digitadas, independentemente da ordem.
     - Ideal para usuários que possuem apenas informações gerais ou fragmentadas.

       **Exemplo**:

       Na configuração de busca como "Palavra Chave", o sistema realiza buscas parciais, identificando registros que contenham qualquer uma das palavras inseridas, independentemente da ordem. Isso torna a busca mais flexível, especialmente para usuários que não possuem o nome completo do produto.

       1. **Busca por "geração"**: Quando o termo "geração" é inserido, o sistema retorna resultados que contenham essa palavra em qualquer parte do nome do produto. Assim, os produtos **"Kindle 11ª Geração"** e **"Alexa Echo Dot 5ª Geração"** aparecem na lista de resultados, pois ambos possuem o termo "geração" em seus nomes.

       Essa configuração é útil para cenários em que o usuário conhece apenas uma parte do nome do produto ou está buscando por categorias mais amplas, aumentando a probabilidade de encontrar resultados relevantes.

       [![Imagem 2: Essa configuração é útil para cenários em que o usuário conhece apenas uma parte do nome do produto ou está buscando…](https://ajuda.sankhya.com.br/hc/article_attachments/42951111713687)](https://ajuda.sankhya.com.br/hc/article_attachments/42951111713687)
   - **Palavra exata**

     - Busca baseada na correspondência exata dos termos inseridos.
     - Retorna apenas registros que reproduzem exatamente o texto digitado.
     - Útil para usuários que sabem exatamente o que estão procurando.

       **Exemplo:**

       Quando o tipo de busca é configurado como "Palavra Exata", o sistema só retorna resultados que correspondem exatamente ao termo digitado, sem considerar variações ou aproximações.

       1. **Busca de "cadeira"**: No primeiro exemplo, ao pesquisar por "cadeira", o sistema não encontra nenhum resultado porque não há registros exatos para a palavra "cadeira". Como a busca de "Palavra Exata" requer uma correspondência exata, se o produto não estiver registrado com esse nome exato, ele não será retornado, como demonstrado na segunda imagem. A mensagem "Nenhum resultado encontrado para: cadeira" é exibida.

          [![Imagem 3: Busca de "cadeira" : No primeiro exemplo, ao pesquisar por "cadeira", o sistema não encontra nenhum resultado porque…](https://ajuda.sankhya.com.br/hc/article_attachments/42951126588183)](https://ajuda.sankhya.com.br/hc/article_attachments/42951126588183)
       2. **Busca de "Cadeira Gamer Husky Max"**: No segundo exemplo, ao digitar o nome completo de um produto, o sistema encontra e exibe o "Cadeira Gamer Husky Max", pois a busca encontrou uma correspondência exata.

       Portanto, a busca por "Palavra Exata" restringe os resultados apenas aos termos que coincidam perfeitamente com o que o usuário digita, tornando a busca mais precisa, mas também mais restritiva.

       [![Imagem 4: Portanto, a busca por "Palavra Exata" restringe os resultados apenas aos termos que coincidam perfeitamente com o que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951132996631)](https://ajuda.sankhya.com.br/hc/article_attachments/42951132996631)

       c. **Busca por 'Marca':** Aplicando o campo como **Marca**, o sistema retorna apenas resultados que correspondam exatamente ao termo pesquisado, garantindo maior precisão.

       - **Busca por "Husky" no campo Marca**: Quando o termo "Husky" é inserido, o sistema retorna apenas os produtos cuja marca seja exatamente "Husky". Nesse caso, o único resultado apresentado é a **Cadeira Gamer Husky Max**, pois ela está registrada com a marca "Husky".
       - Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o resultado corresponda exatamente à marca inserida no campo de busca.

       [![Imagem 5: Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951127041303)](https://ajuda.sankhya.com.br/hc/article_attachments/42951127041303)

       [![Imagem 6: Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951133396503)](https://ajuda.sankhya.com.br/hc/article_attachments/42951133396503)
   - **Regular**

     - Combina flexibilidade e precisão.
     - Aplica critérios de correspondência parcial com foco em relevância.
     - Inclui resultados próximos à expressão digitada, mas que não correspondam exatamente.
     - Ideal para situações em que é necessário encontrar informações relacionadas, mesmo com pequenas variações nos termos.

       **Exemplo:**

       1. **Palavra Parcial**

          - O usuário digitou "cadeir".
          - O sistema identificou sugestões próximas, como "cadeira", baseando-se nos dados disponíveis no banco de dados. Isso ocorre graças à configuração de similaridade, que permite encontrar itens com fragmentos de palavras.
       2. **Categorias e Produtos Relacionados**

          - A busca regular trás as categorias relacionadas em que os produtos listados estão relacionados.
          - Essa funcionalidade melhora a experiência do usuário ao trazer resultados contextuais, que podem incluir itens similares ou complementares ao que está sendo buscado.
       3. **Peso e Relevância**

          - Campos configurados com maior peso na busca garantem que produtos mais relevantes sejam exibidos primeiro (neste caso, a "Cadeira Gamer Husky Max" aparece destacada).
       4. **Correção e Sugestão de Termos**

          - O sistema sugere palavras como "cadeira", indicando que a busca regular consegue interpretar variações e pequenos erros, oferecendo resultados que correspondem ao que o usuário provavelmente procura.

       [![Imagem 7: O sistema sugere palavras como "cadeira", indicando que a busca regular consegue interpretar variações e pequenos…](https://ajuda.sankhya.com.br/hc/article_attachments/42951127720087)](https://ajuda.sankhya.com.br/hc/article_attachments/42951127720087)

   ---

   Para obter mais informações sobre o uso das configurações de busca ou qualquer outra dúvida, entre em contato com nossa equipe de suporte.

**Campo**

- Selecione o campo chave que será utilizado como base para as buscas.

**Peso**

- Defina o peso do campo em uma escala de **0,5 a 5**, sendo **5** o de maior relevância.
- Essa configuração influencia a prioridade que o sistema dará a esse campo ao listar os resultados.

**Nível de Correção**

O **Nível de Correção** é uma funcionalidade que define o grau de tolerância para erros de digitação ou ortografia nos termos de busca inseridos pelos usuários. Essa configuração é especialmente útil para garantir resultados mais relevantes, mesmo em casos de erros simples.

**Opções Disponíveis**

1. **Automática**

   - A correção ocorre de forma automática, com maior tolerância a erros.
   - Para palavras com até **três caracteres**, será aplicada **uma correção automática**.
   - Para palavras com até **seis caracteres**, serão aplicadas **duas correções automáticas**.

**Automática**

- A correção ocorre de forma automática, com maior tolerância a erros.
- Para palavras com até **três caracteres**, será aplicada **uma correção automática**.
- Para palavras com até **seis caracteres**, serão aplicadas **duas correções automáticas**.
- **Alta**

  - Permite uma margem de até **dois erros ortográficos entre o** termo digitado e a palavra buscada.

- **Baixa**

  - Permite uma margem de até **um erro ortográfico entre o** termo digitado e a palavra buscada.

- **Nenhum**

  - Não aplica correções. Caso a palavra seja digitada incorretamente, a busca não retornará resultados.

Essa funcionalidade oferece maior flexibilidade para os usuários, tornando o processo de busca mais eficiente, mesmo em situações onde há pequenos erros de digitação.

**Nível de Similaridade**

- Configure como o sistema interpretará os termos de busca, ajustando o grau de flexibilidade e precisão.

**Opções de Similaridade**:

- **Palavra-chave**

  - Realiza buscas parciais e flexíveis.
  - Retorna resultados que contenham qualquer uma das palavras digitadas, independentemente da ordem.
  - Ideal para usuários que possuem apenas informações gerais ou fragmentadas.

    **Exemplo**:

    Na configuração de busca como "Palavra Chave", o sistema realiza buscas parciais, identificando registros que contenham qualquer uma das palavras inseridas, independentemente da ordem. Isso torna a busca mais flexível, especialmente para usuários que não possuem o nome completo do produto.

    1. **Busca por "geração"**: Quando o termo "geração" é inserido, o sistema retorna resultados que contenham essa palavra em qualquer parte do nome do produto. Assim, os produtos **"Kindle 11ª Geração"** e **"Alexa Echo Dot 5ª Geração"** aparecem na lista de resultados, pois ambos possuem o termo "geração" em seus nomes.

    Essa configuração é útil para cenários em que o usuário conhece apenas uma parte do nome do produto ou está buscando por categorias mais amplas, aumentando a probabilidade de encontrar resultados relevantes.

    [![Imagem 8: Essa configuração é útil para cenários em que o usuário conhece apenas uma parte do nome do produto ou está buscando…](https://ajuda.sankhya.com.br/hc/article_attachments/42951111713687)](https://ajuda.sankhya.com.br/hc/article_attachments/42951111713687)

**Palavra-chave**

- Realiza buscas parciais e flexíveis.
- Retorna resultados que contenham qualquer uma das palavras digitadas, independentemente da ordem.
- Ideal para usuários que possuem apenas informações gerais ou fragmentadas.

  **Exemplo**:

  Na configuração de busca como "Palavra Chave", o sistema realiza buscas parciais, identificando registros que contenham qualquer uma das palavras inseridas, independentemente da ordem. Isso torna a busca mais flexível, especialmente para usuários que não possuem o nome completo do produto.

  1. **Busca por "geração"**: Quando o termo "geração" é inserido, o sistema retorna resultados que contenham essa palavra em qualquer parte do nome do produto. Assim, os produtos **"Kindle 11ª Geração"** e **"Alexa Echo Dot 5ª Geração"** aparecem na lista de resultados, pois ambos possuem o termo "geração" em seus nomes.

  Essa configuração é útil para cenários em que o usuário conhece apenas uma parte do nome do produto ou está buscando por categorias mais amplas, aumentando a probabilidade de encontrar resultados relevantes.

[![Imagem 9: Essa configuração é útil para cenários em que o usuário conhece apenas uma parte do nome do produto ou está buscando…](https://ajuda.sankhya.com.br/hc/article_attachments/42951142016535)](https://ajuda.sankhya.com.br/hc/article_attachments/42951111713687)

- **Palavra exata**

  - Busca baseada na correspondência exata dos termos inseridos.
  - Retorna apenas registros que reproduzem exatamente o texto digitado.
  - Útil para usuários que sabem exatamente o que estão procurando.

    **Exemplo:**

    Quando o tipo de busca é configurado como "Palavra Exata", o sistema só retorna resultados que correspondem exatamente ao termo digitado, sem considerar variações ou aproximações.

    1. **Busca de "cadeira"**: No primeiro exemplo, ao pesquisar por "cadeira", o sistema não encontra nenhum resultado porque não há registros exatos para a palavra "cadeira". Como a busca de "Palavra Exata" requer uma correspondência exata, se o produto não estiver registrado com esse nome exato, ele não será retornado, como demonstrado na segunda imagem. A mensagem "Nenhum resultado encontrado para: cadeira" é exibida.

       [![Imagem 10: Busca de "cadeira" : No primeiro exemplo, ao pesquisar por "cadeira", o sistema não encontra nenhum resultado porque…](https://ajuda.sankhya.com.br/hc/article_attachments/42951126588183)](https://ajuda.sankhya.com.br/hc/article_attachments/42951126588183)
    2. **Busca de "Cadeira Gamer Husky Max"**: No segundo exemplo, ao digitar o nome completo de um produto, o sistema encontra e exibe o "Cadeira Gamer Husky Max", pois a busca encontrou uma correspondência exata.

    Portanto, a busca por "Palavra Exata" restringe os resultados apenas aos termos que coincidam perfeitamente com o que o usuário digita, tornando a busca mais precisa, mas também mais restritiva.

    [![Imagem 11: Portanto, a busca por "Palavra Exata" restringe os resultados apenas aos termos que coincidam perfeitamente com o que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951132996631)](https://ajuda.sankhya.com.br/hc/article_attachments/42951132996631)

    c. **Busca por 'Marca':** Aplicando o campo como **Marca**, o sistema retorna apenas resultados que correspondam exatamente ao termo pesquisado, garantindo maior precisão.

    - **Busca por "Husky" no campo Marca**: Quando o termo "Husky" é inserido, o sistema retorna apenas os produtos cuja marca seja exatamente "Husky". Nesse caso, o único resultado apresentado é a **Cadeira Gamer Husky Max**, pois ela está registrada com a marca "Husky".
    - Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o resultado corresponda exatamente à marca inserida no campo de busca.

    [![Imagem 12: Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951127041303)](https://ajuda.sankhya.com.br/hc/article_attachments/42951127041303)

    [![Imagem 13: Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951133396503)](https://ajuda.sankhya.com.br/hc/article_attachments/42951133396503)

**Palavra exata**

- Busca baseada na correspondência exata dos termos inseridos.
- Retorna apenas registros que reproduzem exatamente o texto digitado.
- Útil para usuários que sabem exatamente o que estão procurando.

  **Exemplo:**

  Quando o tipo de busca é configurado como "Palavra Exata", o sistema só retorna resultados que correspondem exatamente ao termo digitado, sem considerar variações ou aproximações.

  1. **Busca de "cadeira"**: No primeiro exemplo, ao pesquisar por "cadeira", o sistema não encontra nenhum resultado porque não há registros exatos para a palavra "cadeira". Como a busca de "Palavra Exata" requer uma correspondência exata, se o produto não estiver registrado com esse nome exato, ele não será retornado, como demonstrado na segunda imagem. A mensagem "Nenhum resultado encontrado para: cadeira" é exibida.

     [![Imagem 14: Busca de "cadeira" : No primeiro exemplo, ao pesquisar por "cadeira", o sistema não encontra nenhum resultado porque…](https://ajuda.sankhya.com.br/hc/article_attachments/42951126588183)](https://ajuda.sankhya.com.br/hc/article_attachments/42951126588183)
  2. **Busca de "Cadeira Gamer Husky Max"**: No segundo exemplo, ao digitar o nome completo de um produto, o sistema encontra e exibe o "Cadeira Gamer Husky Max", pois a busca encontrou uma correspondência exata.

  Portanto, a busca por "Palavra Exata" restringe os resultados apenas aos termos que coincidam perfeitamente com o que o usuário digita, tornando a busca mais precisa, mas também mais restritiva.

  [![Imagem 15: Portanto, a busca por "Palavra Exata" restringe os resultados apenas aos termos que coincidam perfeitamente com o que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951132996631)](https://ajuda.sankhya.com.br/hc/article_attachments/42951132996631)

  c. **Busca por 'Marca':** Aplicando o campo como **Marca**, o sistema retorna apenas resultados que correspondam exatamente ao termo pesquisado, garantindo maior precisão.

  - **Busca por "Husky" no campo Marca**: Quando o termo "Husky" é inserido, o sistema retorna apenas os produtos cuja marca seja exatamente "Husky". Nesse caso, o único resultado apresentado é a **Cadeira Gamer Husky Max**, pois ela está registrada com a marca "Husky".
  - Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o resultado corresponda exatamente à marca inserida no campo de busca.

  [![Imagem 16: Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951127041303)](https://ajuda.sankhya.com.br/hc/article_attachments/42951127041303)

  [![Imagem 17: Essa configuração é ideal para usuários que desejam buscar produtos de uma marca específica, assegurando que o…](https://ajuda.sankhya.com.br/hc/article_attachments/42951133396503)](https://ajuda.sankhya.com.br/hc/article_attachments/42951133396503)

Útil para usuários que sabem exatamente o que estão procurando.

**Regular**

- Combina flexibilidade e precisão.
- Aplica critérios de correspondência parcial com foco em relevância.
- Inclui resultados próximos à expressão digitada, mas que não correspondam exatamente.
- Ideal para situações em que é necessário encontrar informações relacionadas, mesmo com pequenas variações nos termos.

  **Exemplo:**

  1. **Palavra Parcial**

     - O usuário digitou "cadeir".
     - O sistema identificou sugestões próximas, como "cadeira", baseando-se nos dados disponíveis no banco de dados. Isso ocorre graças à configuração de similaridade, que permite encontrar itens com fragmentos de palavras.
  2. **Categorias e Produtos Relacionados**

     - A busca regular trás as categorias relacionadas em que os produtos listados estão relacionados.
     - Essa funcionalidade melhora a experiência do usuário ao trazer resultados contextuais, que podem incluir itens similares ou complementares ao que está sendo buscado.
  3. **Peso e Relevância**

     - Campos configurados com maior peso na busca garantem que produtos mais relevantes sejam exibidos primeiro (neste caso, a "Cadeira Gamer Husky Max" aparece destacada).
  4. **Correção e Sugestão de Termos**

     - O sistema sugere palavras como "cadeira", indicando que a busca regular consegue interpretar variações e pequenos erros, oferecendo resultados que correspondem ao que o usuário provavelmente procura.

  [![Imagem 18: O sistema sugere palavras como "cadeira", indicando que a busca regular consegue interpretar variações e pequenos…](https://ajuda.sankhya.com.br/hc/article_attachments/42951127720087)](https://ajuda.sankhya.com.br/hc/article_attachments/42951127720087)
