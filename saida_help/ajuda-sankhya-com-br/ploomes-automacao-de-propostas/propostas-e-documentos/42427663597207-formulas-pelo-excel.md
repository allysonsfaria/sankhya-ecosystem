---
id: "42427663597207"
titulo: "Fórmulas pelo Excel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427663597207-F%C3%B3rmulas-pelo-Excel"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-10T18:07:55Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452298", "sync_hash_6c8fedee4f5b"]
---

# Fórmulas pelo Excel

Primeiro vamos configurar a fórmula do nosso campo:

[![Imagem 1: Primeiro vamos configurar a fórmula do nosso campo:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328397/3e748d3d3a551972d5ae1c2e/image.png-expires%3D1619384400-signature%3Da73b5cabef673ee8b23bdc6ce887947cebd77f9bde8d420b3d3d389bbe896c50?expires=1786536000&signature=7c7ad61b8ec11a58bef017683c0a94090457f2bf161136d8d6b901cc46f06fce&req=dyYuFct2nohYFb4V1XW4gd8eKsGgHCTbl%2Bi96scMmR84VbgimmXoVD2F70GS%0AbNwk%2FlFelgGdedDTHbFgpZRqTg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/149986138/0c75a4a37579bc452599478b/image.png?expires=1619384400&signature=a73b5cabef673ee8b23bdc6ce887947cebd77f9bde8d420b3d3d389bbe896c50)

Nesse exemplo estou montando um simulador de preço. O exemplo que vou usar pode ser feito direto pela fórmula simples (inclusive já é padrão do campo "Total" dos produtos da proposta)
Selecione "Fórmula do Excel"

[![Imagem 2: Nesse exemplo estou montando um simulador de preço. O exemplo que vou usar pode ser feito direto pela fórmula simples…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328404/9315b45122c0dafb246ab3ff/image.png-expires%3D1619384400-signature%3Db29d98046cbcec6b2e72a8e904a66a9e0285235b982ad80eb73de229f28697bb?expires=1786536000&signature=2ac80570093848df4972e7ec8e02a87ef96b6b2091d51f820a378cd25edca8b0&req=dyYuFct2mYFbFb4V1XW4gfshKJ8lrZ6IC5szTrkJhNyEot1xCVnmpzTbmIvE%0AS5XE2j3IlqeK4TL30mgjjatWBw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/149986313/3fca49cfa8aa3f1928b34f2c/image.png?expires=1619384400&signature=b29d98046cbcec6b2e72a8e904a66a9e0285235b982ad80eb73de229f28697bb)

Vamos começar pelo upload da planilha; Minha planilha é simples para fins de exemplo, mas podem ser configuradas planilhas complexas com procv e campos dinâmicos normalmente. (⚠️Podem existir limitações)

[![Imagem 3: Vamos começar pelo upload da planilha; Minha planilha é simples para fins de exemplo, mas podem ser configuradas…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328412/e26b387f91414600f40b7869/image.png-expires%3D1619384400-signature%3D384f04f9a1dd9af959472aa5a075e21e33d516bd521eba3ddb760e9b44bd878e?expires=1786536000&signature=c0174573b00e45ef9900753523e62efdfef2c856580e38b159e40172283350ea&req=dyYuFct2mYBdFb4V1XW4gQpwrxUfX1Qg%2Bh3W4aN4mnBwWUhuwDYdFr0Q6a%2Fc%0AW6lZDZnS%2FFhXYxTzD06DiiycAw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/150069316/c0f08f3fb70a4ed7639f0a6f/image.png?expires=1619384400&signature=384f04f9a1dd9af959472aa5a075e21e33d516bd521eba3ddb760e9b44bd878e)

Faço o upload de uma planilha pelo meu computador:

[![Imagem 4: Faço o upload de uma planilha pelo meu computador:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328426/716b27ba37b798bb9c861a1c/image.png-expires%3D1619384400-signature%3D3411c5e1601672376cfe93d4144a0bab75593871f3d4bd3bdbc060efa53e4229?expires=1786536000&signature=9f2e0f97d213fe216f8db5e9657c888f17f50bdc156dc94b2e243046e6833174&req=dyYuFct2mYNZFb4V1XW4gRF65uiuNbMe44gGGrHdHRuq6v8AztjuTEUNVl82%0AiRUtIdgw%2Bxu1EBxhdrzidsNNIw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/150071078/611614d5b6a37087b2221258/image.png?expires=1619384400&signature=3411c5e1601672376cfe93d4144a0bab75593871f3d4bd3bdbc060efa53e4229)

Agora quero retornar o valor da célula B4, que usa B1, B2 e B3 para fazer o cálculo:

[![Imagem 5: Agora quero retornar o valor da célula B4, que usa B1, B2 e B3 para fazer o cálculo:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328437/6a174e76035537d92e62f3da/b4.gif-expires%3D1619384400-signature%3D031fac28a45b6275ecea4977795f4c61a567683abd822b0b89153e55ce058f6a?expires=1786536000&signature=096842ab853b31fdfacd62e4287db6ba64f79da1a76e50e011d4922ed4b0f826&req=dyYuFct2mYJYFb4V1XW4gTINtOxpB1D1etjMdLRH6ah1SJpWdXFkjpSSi0fN%0AIbWFz32KPvrSQDidORCNh0jNbA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/150071942/0ceca10ebe96e74fd162b9df/b4.gif?expires=1619384400&signature=031fac28a45b6275ecea4977795f4c61a567683abd822b0b89153e55ce058f6a)

Exemplo da fórmula funcionando:

[![Imagem 6: Exemplo da fórmula funcionando:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328446/33b489177f17a981b50440f0/exce.gif-expires%3D1619384400-signature%3Dbff229305fd7ae7e66c2977c3627228f6ff74ea2f64e9e89c39630fe71c90ff3?expires=1786536000&signature=d764f076e063c01bfa76388ea9d535a364750b2ecf5b9a89e358ba101d2b482d&req=dyYuFct2mYVZFb4V1XW4gfIun27amzprLccJ%2B1S1j886EnKyfMQHaSGvfc%2Bg%0AzQpafgaV5yNSIeU71eG%2FCSjcfg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/150072555/f0545843034d1b4aedf0c057/exce.gif?expires=1619384400&signature=bff229305fd7ae7e66c2977c3627228f6ff74ea2f64e9e89c39630fe71c90ff3)
