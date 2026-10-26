---
id: "42427633105047"
titulo: "Otimização de código para buscar dados em vários níveis (expands)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427633105047-Otimiza%C3%A7%C3%A3o-de-c%C3%B3digo-para-buscar-dados-em-v%C3%A1rios-n%C3%ADveis-expands"
trilha: "PLOOMES: Automação de propostas  > API & Webhooks"
atualizado_em: "2026-08-03T13:05:32Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452435", "sync_hash_b219f11fc707"]
---

# Otimização de código para buscar dados em vários níveis (expands)

**INTRODUÇÃO**
Muitas vezes é necessário buscar dados de várias entidades distintas em uma mesma consulta para tratá-los para trabalhar com automações e integrações, o problema é que trazer dados de diferentes fontes pode ser uma operação pesada e causar Timeout em sua requisição.

Vamos pegar como exemplo o seguinte cenário: queremos buscar a última revisão de uma proposta cujo negócio foi Ganho e queremos trazer dados detalhados de:

1. Proposta, incluindo os Campos customizados
2. Cliente relacionado, incluindo seus Marcadores e Campos customizados.
3. Negócio incluindo os Marcadores
4. Responsável pelo Negócio
5. Produtos incluindo oc Campos customizados e os Opcionais (e também seus Campos customizados)

A consulta padrão seria parecida com a seguinte:
[https://public-api2.ploomes.com/Quotes?$filter=LastReview+eq+true+and+Deal/StatusId+eq+2&$select=Id,Amount,QuoteNumber,Date,ExpirationDate,DeliveryTime&$expand=Contact($select=Id;$expand=Tags($select=Tag;$expand=Tag($select=Name)),OtherProperties),Deal($select=Id;$expand=Owner($select=Name,Email),Tags($select=Tag;$expand=Tag($select=Name))),Products($select=Product,Quantity;$expand=Parts($expand=Product($select=Code),OtherProperties),Product($select=Code),OtherProperties),OtherProperties($expand=ObjectValue)&$orderby=Id](https://app.intercom.com/)

**DESAFIO**O problema é que para que esta consulta seja executada, a API do Ploomes tem que percorrer entidades em vários níveis para encontrar todos os dados necessários, e esta operação será realizada para cada resultado que corresponda aos parâmetros da busca. Imagine que o filtro desta consulta encontre 15 resultados em uma base de 1.000 Negócios, para cada um dos resultados seria necessário percorrer os diferentes níveis e muito provavelmente a operação sofreria um Timeout (estouro de tempo de requisição) antes de ser completa e os dados desejados não serão retornados.

**SOLUÇÃO**A solução para este caso é bastante simples: fazer o filtro buscando todos os selecionando apenas o ID da entidade, e depois iterar sobre os resultados buscando informações complementares. Então a mesma operação seria dividida em duas etapas. Na primeira, seria feito somente o seguinte:

[https://public-api2.ploomes.com/Quotes$filter=LastReview+eq+true+and+Deal/StatusId+eq+2&$select=Id&$orderby=Id](https://app.intercom.com/)

Uma vez encontrado a listagem (Array de JSON) que correspondem à pesquisa, percorrer cada um deles (**loop**) expandindo a hierarquia e selecionando então todos os dados necessários, como mostrado a seguir:
[https://public-api2.ploomes.com/Quotes?$filter=Id+eq+](https://app.intercom.com/)" + **quote["Id"]** + "[&$select=Id,Amount,QuoteNumber,Date,ExpirationDate,DeliveryTime&$expand=Contact($select=Id;$expand=Tags($select=Tag;$expand=Tag($select=Name)),OtherProperties),Deal($select=Id;$expand=Owner($select=Name,Email),Tags($select=Tag;$expand=Tag($select=Name))),Products($select=Product,Quantity;$expand=Parts($expand=Product($select=Code),OtherProperties),Product($select=Code),OtherProperties),OtherProperties($expand=ObjectValue)&$orderby=Id](https://app.intercom.com/)

O **quote["Id"]** destacado acima representa o ID da proposta da vez dentro do Loop. Embora ainda estejamos fazendo vários **Expands** e trazendo as mesmas informações da consulta não otimizada, iterando assim a busca fica extremamente mais rápida porque estamos dizendo para a API que queremos um ID específico.
