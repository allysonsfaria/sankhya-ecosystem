---
id: "44012242862103"
titulo: "[Routing] - Release Notes 2.20"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012242862103--Routing-Release-Notes-2-20"
trilha: "Lincros > Releases (Atualizações) > Routing (Releases)"
atualizado_em: "2026-10-05T19:23:52Z"
rotulos: ["sync_hc", "lincros", "sync_hash_b3e2cbef4b47", "lincros_13433999"]
---

# [Routing] - Release Notes 2.20

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44012243060759)

## Melhorias

---

## Saneamento de Endereços

Adicionamos novas palavras na base de saneamento de endereço, como:

ED
POSTO
PST
MERCADO
MERCADINHO
SUP
SUPERMERCADO
SUPER
DEPOSITO
BAR
FARMACIA

---

## Estratégias de Roteirização

Adicionamos a melhoria de permitir a cópia de parâmetros de depósitos para a criação de estratégias de roteirização, possibilitando que um depósito tenha uma ou mais estratégias, e possa selecionar elas no momento de gerar a sessão.

— Tela de cadastro

![Imagem 2: — Tela de cadastro](https://ajuda.sankhya.com.br/hc/article_attachments/44012243189399)

— Selecionar estratégia

![Imagem 3: — Selecionar estratégia](https://ajuda.sankhya.com.br/hc/article_attachments/44012270089879)

---

## Definir tipo de conhecimento/embarque ao exportar a sessão para o TMS

Adicionado novo campo na exportação de rotas, ao exportar a sessão para o TMS o usuário poderá escolher o tipo de conhecimento/embarque, permitindo que ao término do processo de roteirização, o usuário possa selecionar o tipo de conhecimento necessário para a etapa do processo logístico (1ª perna ou 2ª perna).
Isso permitirá que o roteirizador gere os embarques no TMS contemplando os tipos de conhecimento necessários.
Resultado esperado: gerar os embarques no TMS com os tipos de conhecimentos selecionados no Routing.

![Imagem 4: Adicionado novo campo na exportação de rotas, ao exportar a sessão para o TMS o usuário poderá escolher o tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012258377367)

---

**Exibir os tipos de produtos e sua ocupação, apenas como informativo, sem restringir a ocupação do carro**
Foi adicionado um novo parâmetro de depósito para permitir exibir os tipos de produto, mesmo que não há definição de percentual de ocupação no tipo de veículo.

Para habilitar este parâmetro, basta seguir o caminho: Cadastros >> Depósito >> Parâmetros do depósito >> Marcar a opção "Mostrar ocupação do veículo por tipo de produto na sessão" (conforme imagem abaixo).
Resultado esperado com o parâmetro habilitado: mesmo não havendo tipos de veículos com limitações, deve exibir as capacidades por tipo de produto.
Resultado esperado com o parâmetro desabilitado: mostrar capacidades por tipo de veículo somente de tipos com limitação.

![Imagem 5: Para habilitar este parâmetro, basta seguir o caminho: Cadastros >> Depósito >> Parâmetros do depósito >> Marcar a…](https://ajuda.sankhya.com.br/hc/article_attachments/44012228503703)

![Imagem 6: Para habilitar este parâmetro, basta seguir o caminho: Cadastros >> Depósito >> Parâmetros do depósito >> Marcar a…](https://ajuda.sankhya.com.br/hc/article_attachments/44012243788951)
