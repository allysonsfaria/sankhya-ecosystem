---
id: "42427604894359"
titulo: "Como arredondar campos para duas casas decimais?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427604894359-Como-arredondar-campos-para-duas-casas-decimais"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-11T16:14:18Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452384", "sync_hash_8b48adaf17f9"]
---

# Como arredondar campos para duas casas decimais?

No dia-a-dia ao serem geradas propostas pode ser que você se depare com uma variação no valor total da sua ordem de venda.

Nesses casos, é preciso inserir uma fórmula de JavaScript bem simples nas configurações desses campos que apresentam erros como os que mencionei.

No cenário abaixo a soma total dos produtos não estava correta e foi preciso alterar a fórmula do "**[Bloco.Total]**". Veja o exemplo de como foi inserida a fórmula:

[![Imagem 1: No cenário abaixo a soma total dos produtos não estava correta e foi preciso alterar a fórmula do " (Bloco.Total) ".…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328837/4e01e6cf61728eb8c8373067/image.png-expires%3D1619463600-signature%3D471603cdcfe144eb50a5dd07584a5aca839a018dc5f28e310049c3344c294e94?expires=1786536000&signature=3ef37ff09b4881f3f215e06d8fd3fe039e99f1ade6ec1323fb1f91aa16b23506&req=dyYuFct2lYJYFb4V1XW4gdK2WTURiprV%2FaF2ZuTe1pZCHo8Ax%2BdBoDuQAXZm%0Avz4ylBzOVMmU4ERGhC0aWfRe8g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/232017415/439690b391b7aeb02c58b9a3/image.png?expires=1619463600&signature=471603cdcfe144eb50a5dd07584a5aca839a018dc5f28e310049c3344c294e94)

A fórmula padrão a ser utilizada é **parseFloat .toFixed ()**.

Dentro dos parenteses você precisa inserir a quantidade de casas que deseja, por exemplo: (2)

Além disso, é importante lembrar que ao "**Salvar a Fórmula**", é preciso ir no documento gerado para o seu cliente e revisar os números de quantidade ou os valores na **Proposta**/**Venda**.

Veja [aqui](https://sankhya.zendesk.com/hc/pt-br/articles/42427485369111) como ajustar as casas decimais de um campo de porcentagem.
