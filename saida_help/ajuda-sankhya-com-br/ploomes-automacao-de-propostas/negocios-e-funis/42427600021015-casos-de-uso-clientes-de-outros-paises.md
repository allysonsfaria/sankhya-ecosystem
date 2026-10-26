---
id: "42427600021015"
titulo: "Casos de uso - Clientes de outros países"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427600021015-Casos-de-uso-Clientes-de-outros-pa%C3%ADses"
trilha: "PLOOMES: Automação de propostas  > Negócios e funis"
atualizado_em: "2026-08-11T16:14:27Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7951300", "sync_hash_6ed0c5171f23"]
---

# Casos de uso - Clientes de outros países

Para classificação de clientes estrangeiros, podemos realizar algumas configurações:

## Criação de campo

Para facilitar o manuseio dos clientes estrangeiros no Ploomes, podemos criar um campo do tipo "texto simples", para utilizar como um campo de identificador.

**Por que não usar o nativo?** Por que o nativo possui máscara e vai impedir a criação, pois somente aceita o formato de CNPJ brasileiro.

Para saber como criar campo, [clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/42427655359767).

![Imagem 1: Para saber como criar campo, clique aqui .](https://downloads.intercomcdn.com/i/o/752048608/2825fbd3bfb185f7e36f24e0/image.png?expires=1786536000&signature=4cd1d6a951398558b46816740ea1e5bf55b44760ad9513cf2cba76e3dd44025d&req=cyUlFs12m4FXFb4V1XW4gdHylVOfh%2BA%2BjOj3%2BoBAagDY9ftc6DwoVByXg%2By2%0AoXDcCww2I7TNJdnpYSujXoMh1g%3D%3D%0A)

Este campo será usado para preencher com número de identificação do seu cliente, sendo um "substituto" do CNPJ.

## Checklist Condicional

A utilização de checklist condicional em negócios é útil para situações em que uma informação é obrigatória para um tipo de negócio e não para outro. Um bom exemplo é o campo de CNPJ para clientes internacionais.

Para criar um checklist, vamos entrar nas configurações do funil:

![Imagem 2: Para criar um checklist, vamos entrar nas configurações do funil:](https://downloads.intercomcdn.com/i/o/751951475/f66c77bb953daddc8de54b87/image.png?expires=1786536000&signature=6d07abc831bc35369504ed34162619f6a0039be6529198b50edcc8dfa669ec43&req=cyUmH8x%2FmYZaFb4V1XW4gcMB0o6AyK0dxLYZPDRdztPhQoS4gONICZLFGIM3%0A94F5%2BozONZTFzdFhISiOElVE7g%3D%3D%0A)

Ao acessar a página de configurações, vamos entrar no checklis do estágio desejado:

![Imagem 3: Ao acessar a página de configurações, vamos entrar no checklis do estágio desejado:](https://downloads.intercomcdn.com/i/o/751953406/e876778f8db86ae5c64dc075/image.png?expires=1786536000&signature=4226020977eeb9380cfe7faea89f4b6cbb08b6c9d55e771be2437f56f148f374&req=cyUmH8x9mYFZFb4V1XW4gcThOrLDWdyWde3XdtG1uv16Hne8kNw4Z44CqO9o%0AXcQ9OxeoyUHee%2FwMo4SwyLHg0w%3D%3D%0A)

![Imagem 4: Ao acessar a página de configurações, vamos entrar no checklis do estágio desejado:](https://downloads.intercomcdn.com/i/o/751957768/6735e01466362f20b138e628/image.png?expires=1786536000&signature=45a8f7f690877e61182a4146b168ed1f7afb0e3f003fd78110799aff64ffa9ad&req=cyUmH8x5modXFb4V1XW4gZ2%2BEjBo1xu3beNZLBTzf694HmNzQTiVYVc4Xylq%0AecUEKIQbDXxAm6wg0RwT7lBufg%3D%3D%0A)

Vamos criar 2 checklist's para realizar essa diferenciação de negócios.

O 1° será com os seguintes filtros:

![Imagem 5: O 1° será com os seguintes filtros:](https://downloads.intercomcdn.com/i/o/752033832/b87ecf59bfd7851dc0319677/image.png?expires=1786536000&signature=0ad310810b65393e002bf67ecc78728365e22d95e773c4deb45b556094791db9&req=cyUlFsp9lYJdFb4V1XW4gWLg2kiQo8kms%2FPE1zJ8uF2pZ36QOIAxIdnb6M7k%0AkTbMMUJuS391di56QN45gCeEkA%3D%3D%0A)

![Imagem 6: O 1° será com os seguintes filtros:](https://downloads.intercomcdn.com/i/o/752034050/f9310540478961b569d5df4a/image.png?expires=1786536000&signature=f6889691c171f89b33c597290b8beed1adce9e12b13148eb4d2a204e00305f60&req=cyUlFsp6nYRfFb4V1XW4gYD6XE7oF6Uk7ZeS5EMJQn5dW3V9GvTBTYlKZtBl%0AQRmIdkkv7PAw1NwUpCfVv8rrEA%3D%3D%0A)

Para configurar o 2° passo do checklist vamos fazer:

[GIF animado: Imagem 7: Para configurar o 2° passo do checklist vamos fazer:](https://downloads.intercomcdn.com/i/o/752041737/4b4abfdffa8dd92bd9f3fb11/NewGIF+%289%29.gif?expires=1786536000&signature=e49e75ee50b955c0dc59db059face833b808a10cce3d573c208bff2ab5d99048&req=cyUlFs1%2FmoJYFb4V1XW4gT%2BusMqiAXy8da5FcrFgvk82nN%2FvLfDQaobmxwP6%0AIOO6oGUAyUxwZghmiGSWwClYow%3D%3D%0A)

Logo, na prática ficará assim:

Para clientes do Brasil, precisam preencher CNPJ

![Imagem 8: Para clientes do Brasil, precisam preencher CNPJ](https://downloads.intercomcdn.com/i/o/752049121/dd37860d6ab219ee29cb85fd/image.png?expires=1786536000&signature=c6f788bc4157bc5dac548366e2579ba3a7b7284e2b478de5ee05480dfbe4a3a5&req=cyUlFs13nINeFb4V1XW4gak4YLUqvCm8ptzBYqXHTXBMRRMC%2F6vfvfPPxr87%0AXQfZSHSyOlOoYLqI5WQhRJOAow%3D%3D%0A)

Para o 2° , vamos seguir o mesmo raciocínio, mas a condição será diferente.

![Imagem 9: Para o 2° , vamos seguir o mesmo raciocínio, mas a condição será diferente.](https://downloads.intercomcdn.com/i/o/753447613/944a57d552155868f3676dd5/image.png?expires=1786536000&signature=e95bb12d6331c7f6f384b1fe600412e71d9b1f340b5f1b65b9a4af1d2a6a2e8d&req=cyUkEs15m4BcFb4V1XW4gZl6QHuqOtbRRKURva519WgMq9t0CMqmJrTXUMaO%0ASFppcO3GOLdvYbr%2BheZA9fZtMQ%3D%3D%0A)

![Imagem 10: Para o 2° , vamos seguir o mesmo raciocínio, mas a condição será diferente.](https://downloads.intercomcdn.com/i/o/752060465/8ca7507411b7458b9ab461bf/image.png?expires=1786536000&signature=e124dd55ef8403c11325fec2a7eacf705b59a158d80b2f775d7b3cdbd47c1802&req=cyUlFs9%2BmYdaFb4V1XW4gRNZCBRdRJgbnl6cMXtDwZIkJey9CAi5ndMZszvu%0AoPTDDl1hGwqCIxJ2mFAcv8wY1A%3D%3D%0A)

Logo, na prática ficará assim:

Para clientes estrangeiros, precisam preencher o campo Identificador que criamos

![Imagem 11: Para clientes estrangeiros, precisam preencher o campo Identificador que criamos](https://downloads.intercomcdn.com/i/o/752060710/3d9679d5d6487678d5530164/image.png?expires=1786536000&signature=91e13ad901fe70f04e4ad9faa9bc1944571a451cc725897021bf687a13a2d351&req=cyUlFs9%2BmoBfFb4V1XW4gWuMEolnqo6%2FJ0gLuQvW%2BZ4GCfiDf5rYtE%2B%2Fx3VV%0A%2FIiQFkWlmFZn9SE1DkcuPj8m%2BQ%3D%3D%0A)

---

Esse artigo te ajudou? Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

Ficou com alguma dúvida? Não hesite em chamar o Suporte pelo chat.
