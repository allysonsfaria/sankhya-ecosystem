---
id: "42429595634199"
titulo: "Integração Ploomes - Dicas de uso"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429595634199-Integra%C3%A7%C3%A3o-Ploomes-Dicas-de-uso"
trilha: "NEPPO: Personalização de atendimento > Neppo Omnichannel > Projetos Neppo"
atualizado_em: "2026-08-06T17:43:10Z"
rotulos: ["sync_hc", "neppo", "neppo_289472521", "sync_hash_710de0d6731c"]
---

# Integração Ploomes - Dicas de uso

**Ploomes**

🔴 Filtrar contatos através do número de telefone telefone:

```
https://api2.ploomes.com/Contacts?$expand=Phones&$filter=Phones/any(p:p/SearchPhoneNumber+eq+3197832186)
```

parte 1: **?$expand=Phones** → espandir as propriedades “Phones”, se não inserir essa informação, não é mostrado no retorno.

parte 2: **$filter=Phones** → utiliza a propriedade Phones dos contatos

```
propriedades padrões...
"Phones": [
                {
                    "Id": 6378094,
                    "ContactId": 401629984,
                    "PhoneNumber": "3197832186",
                    "SearchPhoneNumber": 3197832186,
                    "TypeId": 1,
                    "CountryId": 76
                }
            ]
```

parte 3: **/any(p:p/SearchPhoneNumber+eq+3197832186)** → query ODATA, entra na propriedade Phones e utiliza a propriedade **SearchPhoneNumber** para busca, utilizando o eq para ser igual ao número desejado.

---

🔴 Criar um registro de interação em um deal (negócio)

O registro de interação é como uma anotação em um negócio, um texto livre

utilizar POST

```
https://api2.ploomes.com/InteractionRecords
```

corpo:

```
{
    "DealId": 415290818, //id do DEAL
    "Content": "tipo 7 Comentário aleatório 16/09",
    "TypeId": 7 // é um tipo para informar que partiu de whatsapp
}
```

caso queira deixar apenas como texto simples, utilize o **TypeId** como 1

Exemplo na plataforma, com a logo do whats em verde foi o type 7, em cinza o type 1

![Imagem 1: Exemplo na plataforma, com a logo do whats em verde foi o type 7, em cinza o type 1](https://ajuda.sankhya.com.br/hc/article_attachments/42526699349399)

---

🔴 Buscar os deals de um contato

GET

```
https://api2.ploomes.com/Deals?$filter=ContactId+eq+602729422
```

filter → ContactId (contato desejado)

utilizar a expressão odata “+eq+123345”

---
