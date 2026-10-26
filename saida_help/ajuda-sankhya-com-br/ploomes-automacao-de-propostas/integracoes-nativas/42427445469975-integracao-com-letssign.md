---
id: "42427445469975"
titulo: "Integração com LetsSign"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427445469975-Integra%C3%A7%C3%A3o-com-LetsSign"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:03:51Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6121612", "sync_hash_e95ded469472"]
---

# Integração com LetsSign

## Sobre o LetsSign

O LetsSign é uma ferramenta de assinatura digital, automação e gestão de documentos, ela ajuda a tornar o processo de vendas mais ágil ao encurtar o tradicional e burocrático processo de assinaturas físicas.

A integração entre LetsSign e Ploomes permite colher assinaturas de contratos, propostas e outros documentos diretamente no Ploomes, otimizando o processo de assinatura digital.

## Configurando a integração

## 1. Acessando a integração no Ploomes

- Com um usuário Administrador, acesse Administração > [Integrações Plug & Play](https://app10.ploomes.com/administration/integrations) > LetsSign
- Clique em "Habilitar integração":

![Imagem 1: Clique em "Habilitar integração":](https://downloads.intercomcdn.com/i/o/961927539/d7bbae7f076953fe748a003f/image10.png?expires=1786536000&signature=0ec90d912be715dd97d8bf8a0b95e1841f392725725aa7f6a70d8e079439fcce&req=fSYmH8t5mIJWFb4V1XW4gWocx6xaxFMlg8jLhgp2O0PdXX0dcdBlPceKz3ud%0Av30h3QQeFquQD166iSwnpFgddw%3D%3D%0A)

## 2. Obtendo o ID da conta no LetsSign

- No LetsSign, acesse o menu de “[Integrações](https://app.letssign.com.br/app/integrations)” e clique na parte de configurações para integração:

![Imagem 2: No LetsSign, acesse o menu de “ Integrações ” e clique na parte de configurações para integração:](https://downloads.intercomcdn.com/i/o/961930182/e5efb133220eda31093d3a70/image15.png?expires=1786536000&signature=d204d72a448480a32344d70e72cc5890537dc635b18b6c226f839ba87bbe65ff&req=fSYmH8p%2BnIldFb4V1XW4gZahpMCMZCr%2Br%2Ff%2FVzCX57Ja3MihSUni9rhN2QO6%0A%2F7R96SLwyGktfx1SRG5T%2Fhr9YQ%3D%3D%0A)

- Selecione o usuário padrão da integração;

- Clique em "Salvar";

- Em "Parceiros de Integração", selecione o parceiro ‘Ploomes’ e copie o ID da conta - vamos utilizar ele na configuração dentro do Ploomes.

![Imagem 3: Em "Parceiros de Integração", selecione o parceiro ‘Ploomes’ e copie o ID da conta - vamos utilizar ele na configuração…](https://downloads.intercomcdn.com/i/o/961931736/a210b72cc45bb67b68c88e6e/Untitled.png?expires=1786536000&signature=1c102a46f230de5ecb5e7b77506261c306941f46ca0a43a4b699b2434b5ff742&req=fSYmH8p%2FmoJZFb4V1XW4gTdCdtgNZmTtKfnACMKcbHBHubWCC73YcD6WVmSd%0ATnsuHP6gGH41jPl6ZmrF2E3u%2Bw%3D%3D%0A)

## 3. Ativando a integração no Ploomes

- Cole o ID da conta no Ploomes, adicione a mensagem para o e-mail de assinatura e clique em "Ativar integração".

![Imagem 4: Cole o ID da conta no Ploomes, adicione a mensagem para o e-mail de assinatura e clique em "Ativar integração".](https://downloads.intercomcdn.com/i/o/961934000/f1b897f98708125821a0ed5c/Untitled+%281%29.png?expires=1786536000&signature=d3cc9ae79f0522a9a919753d54b5847fa25f4eaa3fcdaf86546143e13e219ca4&req=fSYmH8p6nYFfFb4V1XW4gbVngZAKrxQdxStR0kEAy40YSSXHj0PvmHLp%2BPra%0AI7NxzNCLvW0q4Unp9lW9Fx8LSg%3D%3D%0A)

- Ao ativar a integração, uma URL será exibida. Copie a URL para a próxima etapa.

![Imagem 5: Ao ativar a integração, uma URL será exibida. Copie a URL para a próxima etapa.](https://downloads.intercomcdn.com/i/o/961934636/85f6486993e13292d8c6faac/image16.png?expires=1786536000&signature=e4d06b9b867eddaa70ab01fe32ef96229f2d70620e5012dfc5b5567b7a6f6701&req=fSYmH8p6m4JZFb4V1XW4gfmOBvGcqWcU2mg%2Fi2Pl3aP1B2z3kBpxnVYz433I%0AbJWTg5KRgIrDVBXvHyrL2Sy28w%3D%3D%0A)

## 4. Habilitando o Webhook no LetsSign

- No LetsSign, vá para "Integrações" > "[Webhooks](https://app.letssign.com.br/app/integrations/webhooks)".

![Imagem 6: No LetsSign, vá para "Integrações" > " Webhooks ".](https://downloads.intercomcdn.com/i/o/961936697/19e340637f5979f5a60899d8/image19.png?expires=1786536000&signature=79e98abba570da66237a34f003399a3af66201a9f97d766060cb8b330d526b30&req=fSYmH8p4m4hYFb4V1XW4gdg327CIfiCxZtU1joWVpsNmgHEdsi31iQmS7JiZ%0Aqt%2BnMkEoQVzwRJAd7kWeRCpM0w%3D%3D%0A)

- Adicione a URL copiada do Ploomes em "Adicionar URL" e clique em "Salvar URLs".

![Imagem 7: Adicione a URL copiada do Ploomes em "Adicionar URL" e clique em "Salvar URLs".](https://downloads.intercomcdn.com/i/o/961936941/76ab7e711f4c51cf3ad22c62/image7.png?expires=1786536000&signature=4cd49243a808364b4a7e70d0c9a3e015868ca82cd2a26bc640cb68fc5ff3b5cb&req=fSYmH8p4lIVeFb4V1XW4gZMe9v%2BxsLeFklO0w7B0gyhjdP87pLT0RQb1iKQJ%0ACijsIn58%2FNiNmbV6VHka9Lo8BA%3D%3D%0A)

**Pronto! Os sistemas estão integrados.**

---

## A integração na prática

## 1. Como o envio é feito

- Dentro do documento, clique em "Compartilhar" e selecione LetsSign.

- Escolha o tipo de assinatura, o formato de envio e adicione o e-mail do signatário. Adicione mais signatários se desejar.

![Imagem 8: Escolha o tipo de assinatura, o formato de envio e adicione o e-mail do signatário. Adicione mais signatários se…](https://downloads.intercomcdn.com/i/o/961955323/70c1b10d5aaa67ae95b7e95f/image9.png?expires=1786536000&signature=3006c6b50eeeaee2310ac66cebb7761aae8305127b03b7d4f5d724cb792059fe&req=fSYmH8x7noNcFb4V1XW4gSquVs8ihmdZ2sIny4mu7iOniF0PlkH9hb%2Bbu88z%0ADn3Nsc3YOM32T2RFVQiLHeDVUw%3D%3D%0A)

Independente do método de entrega escolhido, é obrigatório fornecer o endereço de e-mail do destinatário.

- Clique em "Enviar para assinatura".

É possível acompanhar o status da assinatura no topo da tela do documento.

![Imagem 9: É possível acompanhar o status da assinatura no topo da tela do documento.](https://downloads.intercomcdn.com/i/o/961956477/d197f3379b16741ad505e090/image4.png?expires=1786536000&signature=4b3d98a823f9a89a446de84a270220642eaee4d67977ae839ad07460a7d05f99&req=fSYmH8x4mYZYFb4V1XW4gREssT6Hvh7FaAV2y1WquDvT%2F0o0e1ibkE3vYQxM%0AqvemKZ9Vz4Jax7OtAC77nTGfRQ%3D%3D%0A)

## 2. Como o signatário recebe

- O signatário recebe um e-mail para visualizar o documento e proceder à assinatura.

Veja como a solicitação chega na caixa de entrada do e-mail do signatário:

![Imagem 10: Veja como a solicitação chega na caixa de entrada do e-mail do signatário:](https://downloads.intercomcdn.com/i/o/961957101/01fd17869d17ed6c650a5c92/image11.png?expires=1786536000&signature=149e33f2a37cc9111d7026cd56199b541bd2d45ff84cc8159e3b7e13ef3d8db2&req=fSYmH8x5nIFeFb4V1XW4gV5w2uIi0SzjZkE9wUaW7C5mk9A6%2Fl3eQ8pRla8b%0A8sFPZy74t4%2B9s%2F45mHltGy2suw%3D%3D%0A)

A "Mensagem do solicitante" é configurada na tela da integração.

O signatário, ao clicar em "Visualizar para assinar", irá visualizar o modelo e poderá assiná-lo:

![Imagem 11: O signatário, ao clicar em "Visualizar para assinar", irá visualizar o modelo e poderá assiná-lo:](https://downloads.intercomcdn.com/i/o/961958123/9f8017a47e18b5c60fdb7dec/image5.png?expires=1786536000&signature=b3b63b6ad3479cbc2f7dc86716f14ddbffc2da93bef091032a7cdd08c4809590&req=fSYmH8x2nINcFb4V1XW4gdC1tGulxfKmAznYKA6kP9uRkIxY1IA8LjA%2B%2Fmy0%0AATHTv22VPJZYymYBuFFUl%2BqzqQ%3D%3D%0A)

Ao clicar em Assinar ele irá preencher com seus dados pessoais para prosseguir:

![Imagem 12: Ao clicar em Assinar ele irá preencher com seus dados pessoais para prosseguir:](https://downloads.intercomcdn.com/i/o/961959629/07c9f38a590e512b0dfc8ed9/image26.png?expires=1786536000&signature=f391bbfdace57f444eed02f9b1615a06c0510978e8c59f42e2ed064dcc56aa94&req=fSYmH8x3m4NWFb4V1XW4gRqnfCXiAXD9l5SJoqRSWB5CxYmfOjgEpBrg8rNy%0Ai8uf5tWhVAudrbw%2FKMcKWfWBdQ%3D%3D%0A)

E passará por uma fase de autenticação, receberá um novo token em sua caixa de entrada:

![Imagem 13: E passará por uma fase de autenticação, receberá um novo token em sua caixa de entrada:](https://downloads.intercomcdn.com/i/o/961960471/145e10f5782fec0d628c9390/image18.png?expires=1786536000&signature=0733f5c654685414e358668fbd4d79e81a67fa5841c4070513e20eb0c9450416&req=fSYmH89%2BmYZeFb4V1XW4geqALwqa8nlw3BiMGZBXgwW5LcDG34lt%2FXyDQMPs%0AnLJgGPRHjSdsVJuK7RK%2FikgWKA%3D%3D%0A)

![Imagem 14: E passará por uma fase de autenticação, receberá um novo token em sua caixa de entrada:](https://downloads.intercomcdn.com/i/o/961960820/3c539eb2855d79b832b3bf5e/image24.png?expires=1786536000&signature=c435184fb92a14d8e9bf8ea4fbe31e2c0029388fd67323cf05cfbc794d976ccc&req=fSYmH89%2BlYNfFb4V1XW4gTK60421LgLSgZ2JNAeDAzdK7vK8wABGJqVP10Tu%0AbIF86G6WDAhoodPKxo4bXCjtjg%3D%3D%0A)

- Após autenticação, o documento é assinado.

![Imagem 15: Após autenticação, o documento é assinado.](https://downloads.intercomcdn.com/i/o/961961032/73835bf95c83c2d21b784948/image23.png?expires=1786536000&signature=3da0b2d13b5f374a928050e4be0e2cb1975760d539b5da91db7f29789c8648b1&req=fSYmH89%2FnYJdFb4V1XW4gRt4p1b1B%2Fjqp1xj%2BtFL2gdS0vOEMRTwLQTJ%2FSZZ%0AVMXOLXWLypo1qgsFdWLYRi9bBw%3D%3D%0A)

## 3. Como fica no Ploomes

Ao retornar ao Ploomes, verifique no topo da tela do documento que a assinatura foi concluída.

![Imagem 16: Ao retornar ao Ploomes, verifique no topo da tela do documento que a assinatura foi concluída.](https://downloads.intercomcdn.com/i/o/961961277/e0b753cc3db59e2acbea26fd/image14.png?expires=1786536000&signature=96921d82d891746cbeca7a5fcc42b027e97724ea100d128be075a31d31c92598&req=fSYmH89%2Fn4ZYFb4V1XW4gVi%2BL%2B8PyKpmmpHDglaIWSKwWwA2eDEm%2BUSxcpvE%0AM9TV%2Fy8Bk%2BbmxvF0NMezQC9OMg%3D%3D%0A)

Após a assinatura, não é possível remover o signatário.

---

## Solução de problemas

## Por que meus e-mails não chegam na caixa de entrada dos clientes após ativar a integração?

Certifique-se de definir um usuário padrão para envio de e-mails no LetsSign, através do campo "Usuário padrão para integração" na tela "Integrações".

---

Este guia visa proporcionar uma compreensão geral da integração entre LetsSign e Ploomes. **Caso necessite de informações adicionais ou suporte, estamos à disposição para ajudar!**
