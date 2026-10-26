---
id: "42427671328791"
titulo: "Codifique as URL de suas requisições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427671328791-Codifique-as-URL-de-suas-requisi%C3%A7%C3%B5es"
trilha: "PLOOMES: Automação de propostas  > API & Webhooks"
atualizado_em: "2026-08-03T13:05:33Z"
rotulos: ["sync_hc", "ploomes", "sync_hash_0b488e2062b2", "ploomes_5452434"]
---

# Codifique as URL de suas requisições

Este artigo tem por finalidade prevenir alguns problemas que podem ocorrer ao realizar requisições à API que contenham caracteres especiais. O principal deles é o '&', que pode ser interpretado como um parâmetro.

Por exemplo: imagine que seja necessário fazer uma busca por uma empresa chamada 'R&B Soluções' que esteja 'Ativa' no Endpoint de contatos. A pesquisa seria da seguinte maneira (sem codificação):

[https://public-api2.ploomes.com/Contacts?$filter=Name+eq+'R**&**B Soluções'**&**StatusId+eq+1863](https://public-api2.ploomes.com/Contacts?$filter=Name+eq+'R&B%20Solu%C3%A7%C3%B5es'&StatusId+eq+1863)

Nome que no endereço acima, existem 2 '&'s. Um no nome do cliente em questão e outro para identificar o parâmetro 'StatusId'. O problema é que sem a codificação, não há como distinguir ambas as ocorrências. Com isso, resultados inesperados podem acontecer e o dado provavelmente não será buscado.

A URL codificada ficaria da seguinte maneira:
[https%3A%2F%2Fapi2.ploomes.com%2FContacts%3F%24filter%3DName%2Beq%2B%27R%26B%20Solu%C3%A7%C3%B5es%27%26StatusId%2Beq%2B1863](http://https:%2F%2Fapi2.ploomes.com%2Fcontacts%3F%24filter%3Dname+eq+%27r%26b%20solu%C3%A7%C3%B5es%27%26statusid+eq+1863/)

É possível notar que todos os caracteres especiais ':', '/', '&' foram codificados.

A maioria das linguagens de programação tem classes nativas para codificar URLs. Em C#, por exemplo, basta utilizar o método EscapeDataString, que retorna uma **string**, do pacote System.Uri, assim:
Uri.EscapeDataString(sua\_url)

Utilizando este método simples, muitos problemas de busca de dados podem ser evitados. Outras linguagens podem ter métodos equivalentes, basta realizar uma busca rápida na Internet :)
