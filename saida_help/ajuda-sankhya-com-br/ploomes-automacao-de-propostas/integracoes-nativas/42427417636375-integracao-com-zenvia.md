---
id: "42427417636375"
titulo: "Integração com Zenvia"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427417636375-Integra%C3%A7%C3%A3o-com-Zenvia"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:37Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452448", "sync_hash_837e45194b48"]
---

# Integração com Zenvia

## Por que integrar a solução ao Ploomes?

A integração permite realizar ligações diretamente pelo CRM, além de armazená-las como Registros de Interação para escutar depois.

![Imagem 1: A integração permite realizar ligações diretamente pelo CRM, além de armazená-las como Registros de Interação para…](https://downloads.intercomcdn.com/i/o/872283006/7c3b0c5520d34cf54f297353/image.png?expires=1786536000&signature=4bef42137272ef3ab1cbabf76233d90871b2c15f166f2b69d34a00a755fa2a6c&req=fCclFMF9nYFZFb4V1XW4ga7h2c4rEPI28Q%2B%2B%2Bo35u37Qo4V3RLsF%2Bswdxa%2FK%0AFVz5frSH7zINi8%2FVZ3OyM6wtgg%3D%3D%0A)

## Como realizar a integração?

Observação importante: para realizar a integração, você precisa ter uma conta ativa no Zenvia.

## Primeiro passo

Dentro do Ploomes, acesse o módulo de Administração e clique em "[Integrações Plug and Play](https://app10.ploomes.com/administration/integrations)":

![Imagem 2: Dentro do Ploomes, acesse o módulo de Administração e clique em " Integrações Plug and Play ":](https://downloads.intercomcdn.com/i/o/872271966/f426953c3c6703b1ee094a73/image.png?expires=1786536000&signature=8a779f8d5a6a1357bd368c814032594ed80962766db89f4e8c97f22cb3794282&req=fCclFM5%2FlIdZFb4V1XW4gYdxE1kfSP3R%2FvAilIlFTeLhpJHFM5UQJiC7n6hx%0AaqM9oE%2F2k3Z1fJrWXzjBfEG63Q%3D%3D%0A)

Agora, selecione a opção "Zenvia":

![Imagem 3: Agora, selecione a opção "Zenvia":](https://downloads.intercomcdn.com/i/o/872272895/099e7c810a28a37234d18b55/image.png?expires=1786536000&signature=fb1fc1475af199a1c10093a5f96e99333305337949901d1aaaf7a9b327fc07eb&req=fCclFM58lYhaFb4V1XW4gaOnklwFPUcD0Kt757yWFeARRpFaMs4tJkToPBW5%0A4rhWWQ2u02vUEQ8yn533g%2FtFIA%3D%3D%0A)

## Segundo passo

Abra uma nova guia em seu navegador e acesse sua conta no Zenvia e faça login. Você será direcionado ao Dashboard de sua conta e terá acesso ao **Access-Token:**

![Imagem 4: Abra uma nova guia em seu navegador e acesse sua conta no Zenvia e faça login. Você será direcionado ao Dashboard de…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369330657/0056d356e3c59395e0769899/mceclip0.png?expires=1786536000&signature=59b1adcac53595d3b274bffefab103345c93e7243bf88c290002dd1d996e7e9a&req=dyYuFcp%2Bm4RYFb4V1XW4gZmFbiZNUBKCvS8Az6rQ0HACNOZvV%2Fklyci0mWwY%0ATAeKsDJIcfuGv69d%2F5jCWAT2ew%3D%3D%0A)

Copie essa informação e retorne à página de integração do Ploomes.

## Terceiro passo

Cole o Access-Token no local indicado e informe o e-mail que você utiliza para **acessar o Zenvia**:

![Imagem 5: Cole o Access-Token no local indicado e informe o e-mail que você utiliza para acessar o Zenvia :](https://downloads.intercomcdn.com/i/o/872273614/0732bd90960ef2805e6e26d9/image.png?expires=1786536000&signature=c5d829cc66f46f58bce3925fb9b59ef77c9afe598f4b27c5a28db630e321c429&req=fCclFM59m4BbFb4V1XW4gcNZAQ3YjIMJoQgGZqEiE%2F71356e7jTKQxuu0dVu%0AwWt%2FfhY%2FpLxBUM8QLohwH%2FU86w%3D%3D%0A)

Agora, clique em "Ativar integração".

## Quarto passo

Vamos definir os ramais e os usuários de cada ramal. Para isso, acesse o TotalVoice > Central > Ramais:

[![Imagem 6: Vamos definir os ramais e os usuários de cada ramal. Para isso, acesse o TotalVoice > Central > Ramais:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330666/cdd7f24a619bbb5e322f0b36/image.png-expires%3D1619802000-signature%3D869b456b076e7ac67ee4faad9b2712af07b08de73bc0c9621ca36a3bb7d01f41?expires=1786536000&signature=da503078c00245c37cef86aff60ff47923a094b428a231762c31cd33437b231e&req=dyYuFcp%2Bm4dZFb4V1XW4gVZ0vnMFovtiS5HMJQUU%2Bs63vkaYVuop76y2kt4E%0AKmfJdMxyYdk3gln%2BmJzeGZeKQA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/122452094/f16d37fe23e362db0fcdb61c/image.png?expires=1619802000&signature=869b456b076e7ac67ee4faad9b2712af07b08de73bc0c9621ca36a3bb7d01f41)

Você verá todos os ID's, ramais e e-mails dos usuários do TotalVoice. Voltando ao Ploomes, clique em "Adicionar usuário":

Agora você deve definir qual é o usuário que terá o telefone habilitado e seu respectivo ID e Número do Ramal:

![Imagem 7: Agora você deve definir qual é o usuário que terá o telefone habilitado e seu respectivo ID e Número do Ramal:](https://downloads.intercomcdn.com/i/o/872274851/80725e2bdd359c5de2d8f14d/image.png?expires=1786536000&signature=7c7508480545d016ce26740c8148c8a69573a8c2837b006b2843d8697f4af1a9&req=fCclFM56lYReFb4V1XW4gbmZAYnfbDhV2COHV7XCYtBELSNY6%2FdSnDxHaryb%0Ai%2FCh9GcIav2t27pX7GZPLRFbmw%3D%3D%0A)

![Imagem 8: Agora você deve definir qual é o usuário que terá o telefone habilitado e seu respectivo ID e Número do Ramal:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1796033883/32331d436811e5d6a0a031da4775/image.png?expires=1786536000&signature=f1de1612fbef80212dd3729840b55ba1551b4865a406713daa1e215ab5624a6c&req=dScuEMl9nolXWvMW3nq%2BgRtgqlWC0l4VrggzlSm7EVOIuspjpmpBRtBl67ZO%0AkhhPbLXo2EHSVMdBbVPuhMfyxQQ%3D%0A)

Pronto, agora é só clicar em "Atualizar integração"! Para adicionar novos usuários, basta clicar no botão "Adicionar usuário" e repetir os passos anteriores.

## Como funciona a integração?

No canto superior direito de sua tela, você verá um telefone:

[![Imagem 9: No canto superior direito de sua tela, você verá um telefone:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330686/91b8fe7e4ac79fa221605f60/image.png-expires%3D1619802000-signature%3Dbd47e322ba00253580f169ce4b8aa07378d86598a06a88ca263802b079ee3569?expires=1786536000&signature=50d2de17c4124f915d81c95dba83f1fb350d093dbeb400c40eb44f6d2b0e0fb3&req=dyYuFcp%2Bm4lZFb4V1XW4gd%2Fwnu9OI5wi9hHiL4xSLPQ4TITRnD5iKr3QunSc%0ABGHoNSjUc1QjNwpXJAo1qRndMA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/122455058/888677ea3c3532b5172d0175/image.png?expires=1619802000&signature=bd47e322ba00253580f169ce4b8aa07378d86598a06a88ca263802b079ee3569)

Clique nele e você verá a seguinte janela:

[![Imagem 10: Clique nele e você verá a seguinte janela:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330693/764bbdc0673f99569b7db986/image.png-expires%3D1619802000-signature%3D6b50f7a9482d3a0720328995560703e5c58a9de0ef85af01b37c3ed76f88de84?expires=1786536000&signature=910725100e8029c98979a7c1d27b6017c454adef49df030a56d9104575046316&req=dyYuFcp%2Bm4hcFb4V1XW4gQ6WnnfdnV9Ecz6ikN0MtThWRrghcurvmJ6oLCOj%0AD%2BE1uyc4KJS8F%2BSoMFuvtJtD%2FQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/122455326/78febc5609a538efee1a57ce/image.png?expires=1619802000&signature=6b50f7a9482d3a0720328995560703e5c58a9de0ef85af01b37c3ed76f88de84)

Para ligar o telefone, clique em "Offline". Para realizar ligações, você pode digitar o número ou buscar pelo nome do cliente:

[![Imagem 11: Para ligar o telefone, clique em "Offline". Para realizar ligações, você pode digitar o número ou buscar pelo nome do…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330707/f69c86a028d5bcf01b16f8c2/image.png-expires%3D1619802000-signature%3D0a9a28debd5cec92a731058ae3e48a4df5cb11626777bd2ee0b375c14cadbd24?expires=1786536000&signature=1dd54b20a06dea85c22592b75e60af960d967dac764def01a6f6a89d42bb44f8&req=dyYuFcp%2BmoFYFb4V1XW4gSLlIVz9beNJl9vqy2TAHSE6mMqu5IFKgTFtH0lF%0AwQKX02Q2vFCeVer3zAa5FuuCLg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/122455810/28c8c5bad062d8080d8e60aa/image.png?expires=1619802000&signature=0a9a28debd5cec92a731058ae3e48a4df5cb11626777bd2ee0b375c14cadbd24)

Quando você digita o nome de um cliente, por exemplo, o Ploomes listará os telefones cadastrados nesses respectivos clientes:

[![Imagem 12: Quando você digita o nome de um cliente, por exemplo, o Ploomes listará os telefones cadastrados nesses respectivos…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330716/3ddab6eefae5d0f89afe4e42/image.png-expires%3D1619802000-signature%3Da8ea19143541a43fb87912ae66250b57843ff202348a97ef5c6f1bbecc84147d?expires=1786536000&signature=93396c9316be8dd689536042cde5ac8fc88a734296ecc9d48551056ff02ae113&req=dyYuFcp%2BmoBZFb4V1XW4gVpF1lmTRjG7DGQ2EfLr1kcUBvmoEkjP%2F%2FtSpecJ%0A3kMHJppurZXWVxjsxqetIEbCwA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/122456025/72f1a610ae33df2ab6c4fc64/image.png?expires=1619802000&signature=a8ea19143541a43fb87912ae66250b57843ff202348a97ef5c6f1bbecc84147d)

Depois de selecionado, basta clicar em "Ligar".

Quando a ligação for finalizada, um registro de interação do tipo "Telefone" será realizado de acordo com as informações preenchidas nesse formulário:

[![Imagem 13: Quando a ligação for finalizada, um registro de interação do tipo "Telefone" será realizado de acordo com as…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330721/9ef86a85df661e03ec5a5799/image.png-expires%3D1619802000-signature%3Df0cf2d3054bb963d1cc83e33f3c8bbe64a86ec8261b5ed91530949ac1301478b?expires=1786536000&signature=fb61c668df9879321d4be9af407d3f8172cfac71dd02f6b0d2ad6c3872ea906c&req=dyYuFcp%2BmoNeFb4V1XW4gcA1%2Fw4d5Al6WEf%2B527jl%2FyIU6JlYkNzUuuEj6gA%0ACqRxJq6lx9n4HdhFUDOwpCEjhA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/122456488/5f10015d8e435aae1f1c0828/image.png?expires=1619802000&signature=f0cf2d3054bb963d1cc83e33f3c8bbe64a86ec8261b5ed91530949ac1301478b)

Uma vez registrado, você poderá ouvir a ligação clicando no "Play" deste registro:

[![Imagem 14: Uma vez registrado, você poderá ouvir a ligação clicando no "Play" deste registro:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330725/137c42b4ec89dadfd0958a76/image.png-expires%3D1619802000-signature%3D64bff0fd4efe7c683d1dfd897ab487ac707120ed47f2211c93aec9713289b235?expires=1786536000&signature=269434487a01a5506f7e42a8b3f7bbd57d275d61d0f2185d03b432dd3753d403&req=dyYuFcp%2BmoNaFb4V1XW4gfspnZeGWUSlLy8FzB%2FmFVWxLvOo2fpNNlzIyiG5%0AgULNWcEdJpkBeSJ7E8LqNdGOxg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/122456872/b2956d4f6a11ac867a44b0fa/image.png?expires=1619802000&signature=64bff0fd4efe7c683d1dfd897ab487ac707120ed47f2211c93aec9713289b235)
