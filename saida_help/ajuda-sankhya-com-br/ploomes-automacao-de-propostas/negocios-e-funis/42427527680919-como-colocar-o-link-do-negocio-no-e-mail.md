---
id: "42427527680919"
titulo: "Como colocar o link do negócio no e-mail?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427527680919-Como-colocar-o-link-do-neg%C3%B3cio-no-e-mail"
trilha: "PLOOMES: Automação de propostas  > Negócios e funis"
atualizado_em: "2026-08-10T18:04:54Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5616866", "sync_hash_ed569c64a9e8"]
---

# Como colocar o link do negócio no e-mail?

## Criação do Campo

Primeiro vamos criar um campo do tipo: Texto Simples no Funil desejado (Menu > Configurar Funil > Formulário de Novo Negócio > Adicionar Campo > Criar Campo) chamado **Link do Negócio**:

![Imagem 1: Primeiro vamos criar um campo do tipo: Texto Simples no Funil desejado (Menu > Configurar Funil > Formulário de Novo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1884337801/af07882f9b69498af54753a66123/1.png?expires=1786536000&signature=956256f7aec994d5a7f61c9382a9741393729b61f41b8ab89d5df2c5a64e7368&req=dSgvEsp9molfWPMW3nq%2Bgb0bCRbN13w7hCNgHfRndfebUPwFPS0JLhS5rTOd%0AQTdnoGwjYji2Yl2kkKu4MS0BvAA%3D%0A)

Nesse momento vamos em Configurações Avançadas > Fórmula > Configurar e inserir a fórmula:

"app10.ploomes.com/deal/"+"**[Negócio.Id]**"

**Lembrando:** o campo Negócio.ID precisa ser inserido clicando em Campos > ID.

![Imagem 2: Nesse momento vamos em Configurações Avançadas > Fórmula > Configurar e inserir a fórmula: "app10.ploomes.com/deal/"+"…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1884337993/f44e311dbf379f375547be45250e/2.png?expires=1786536000&signature=9b5ff36129a2bb50cff1ed87249b4baa72c23c5226f7d8bad04b3013fab3b243&req=dSgvEsp9mohWWvMW3nq%2BgXNMxOB5DoQSvkR2DWSE%2B4XrLCLeFg8hNrja5k5m%0A%2B4rrM2S4MF6A61bdaxVMSBEE1LI%3D%0A)

**Dica:** manter o campo no formulário é opcional.

## Criação da Automação

Indo em Administração > Automações > Negócio > Nova Automação, vamos configurar dessa forma:

![Imagem 3: Indo em Administração > Automações > Negócio > Nova Automação, vamos configurar dessa forma:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1884339026/227c7e242f078b6b127ff87db048/Captura+de+tela+2025-12-14+190105.png?expires=1786536000&signature=0c0bd76150ec69f388b5595000de75a19cc8f75fa14c39d92513093b6d65455b&req=dSgvEsp9lIFdX%2FMW3nq%2BgXi12Eiz3Eiz3uzwH8MkpqzMiLWezKSUJOK2SA3J%0AxxzIKpq5aCckBg%2Bo04vqaanluWA%3D%0A)

O filtro dependerá do funil/estágio que você deseja que a automação rode. Nesse caso, a mesma irá funcionar somente quando o negócio for criado no funil de Vendas, mas você pode inserir outros Funis ou se desejar Todos, basta colocar: Negócio > Funil > Diferente de > Vazio.

Para essa automação vamos utilizar duas ações, a primeira irá editar o campo de **Link do Negócio** (campo que criamos anteriormente) com a fórmula que inserimos nele:

![Imagem 4: Para essa automação vamos utilizar duas ações, a primeira irá editar o campo de Link do Negócio (campo que criamos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1884339197/f313d51b3db80c15b1e9d0c2d571/3.png?expires=1786536000&signature=53497eed7c37199b1679be35d2bcaaa8231dafe14b3db0d7a4a01c65b98cd9b0&req=dSgvEsp9lIBWXvMW3nq%2BgZ%2FzMf7AlVojS%2BUq5uxsULB3okgl8h8Aavs8OE2J%0AGxxp2ucCYmyEYQoCTQ8kk0AMZcs%3D%0A)

![Imagem 5: Para essa automação vamos utilizar duas ações, a primeira irá editar o campo de Link do Negócio (campo que criamos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1884339382/526956a2e6dc3b74d023d7166ab3/2.png?expires=1786536000&signature=5423b92b09c5ce143e81aa86258b92a04fbe8041a9a2a714340c45cf9409cbd4&req=dSgvEsp9lIJXW%2FMW3nq%2BgSLKtd%2B%2B3Hg2CbErIeQv5pyV08ANv6GXS62Q5gSf%0A0xRH1yMhZq3FffLAmRruLu10%2BJM%3D%0A)

A segunda automação iremos enviar o e-mail e inserirmos o campo de: **Link do Negócio** em seu conteúdo:

![Imagem 6: A segunda automação iremos enviar o e-mail e inserirmos o campo de: Link do Negócio em seu conteúdo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1884340289/be1fdaea9d3efec5c161df2a0026/Captura+de+tela+2025-12-14+190309.png?expires=1786536000&signature=892e50323bd36b941f246026de8c52ff035fe6730d1a7d394a5d34794a1f9abc&req=dSgvEsp6nYNXUPMW3nq%2BgaMyUWGbARV64PkkOSAw6nhnMndQy%2Fz%2FwUithI2f%0ABIiz4TjkIgleiQDggCKa8sv%2BfNI%3D%0A)

## Demonstração

O e-mail chegará dessa forma:

![Imagem 7: O e-mail chegará dessa forma:](https://downloads.intercomcdn.com/i/o/397607761/81038b2653f2d56a2b32ce5a/image.png?expires=1786536000&signature=ffd3de7d800321633852a4c20c93525129ba4d916d7312cf397c086c95c00db0&req=dykgEMl5modeFb4V1XW4gaIslEzilfkh0UHO7ABQoh%2Fw72pfVAAh%2FMPdKctb%0AmFlXVyeIX%2FgTkYpV2lvSx26i8w%3D%3D%0A)

**Atenção:** esse artigo é válido para outras entidades (como: clientes, vendas, propostas) você apenas terá que reproduzir o passo a passo na entidade desejada.

---

Esse artigo te ajudou? Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

Ficou com alguma dúvida? Não hesite em chamar o Suporte pelo chat.
