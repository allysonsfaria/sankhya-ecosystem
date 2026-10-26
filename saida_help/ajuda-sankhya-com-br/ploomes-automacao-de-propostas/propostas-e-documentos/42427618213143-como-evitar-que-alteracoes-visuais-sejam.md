---
id: "42427618213143"
titulo: "Como evitar que alterações visuais sejam perdidas após atualizar uma proposta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427618213143-Como-evitar-que-altera%C3%A7%C3%B5es-visuais-sejam-perdidas-ap%C3%B3s-atualizar-uma-proposta"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-10T18:05:49Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452385", "sync_hash_3c79be6fff89"]
---

# Como evitar que alterações visuais sejam perdidas após atualizar uma proposta

Às vezes algumas propostas exigem condições especiais e isso reflete em alterações nos textos do documento. Nestes casos, é importante que seu modelo de propostas esteja preparado para tal situação.

Geralmente as propostas possuem textos fixos, que são padrões para a maioria dos casos. Porém, sempre existe alguma situação que exige alguma adequação para um novo cenário. Nestes casos, intuitivamente os usuários tendem a fazer modificações visuais na proposta já gerada. Isso não está errado, porém alterando livremente o documento gerado, há um risco desta alteração ser perdida quando caso a proposta seja atualizada, clicando 'Editar > Atualizar dados e modelo'.

Isso acontece porque quando o Ploomes precisa recarregar os dados e modelo, entende-se que você está tentando restaurar o modelo padrão, então suas alterações manuais serão perdidas.

Abaixo está o exemplo de uma proposta que será editada visualmente:

[![Imagem 1: Abaixo está o exemplo de uma proposta que será editada visualmente:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328851/1e5525f2fd645ff8630d0248/ploomes_proposta_modificacao_visual.png-expires%3D1619791200-signature%3Ddf5a1f3cf1393a9e1d469f62132f06926be6e46df5e917daf6cf42b503b67a5b?expires=1786536000&signature=f10013cff636c6711f003f5dbf25c3ebe31bea5fc3d0448b9b5578c989818218&req=dyYuFct2lYReFb4V1XW4gR5B7qsE2E7CEJkP%2FdN7utkG171CBUNmOpUnWpau%0AOiSpVD3AUSioC3QSvnnQIUFI2A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/93870239/ff1da5837a27d85209f56477/ploomes_proposta_modificacao_visual.png?expires=1619791200&signature=df5a1f3cf1393a9e1d469f62132f06926be6e46df5e917daf6cf42b503b67a5b)

A seguir está o trecho após a alteração:

[![Imagem 2: A seguir está o trecho após a alteração:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328860/f2a69aff98a51317f1567552/ploomes_proposta_modificada.png-expires%3D1619791200-signature%3D0001048b984888185d3b35515b731f9c50752bb5f38fb4330c1b0dc01033b55c?expires=1786536000&signature=d6fa43cf0daf580e869439194e727d21e9fb4a133d02555c1ede0144553ef716&req=dyYuFct2lYdfFb4V1XW4gZJmITudlYQjOF0PPC77%2BHl0hN1DH3vu9Jhepip2%0Aq%2BsYlTHyNXU9bLKgeYIqWH2qUw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/93870325/59c019739bb20a6fd4c1de89/ploomes_proposta_modificada.png?expires=1619791200&signature=0001048b984888185d3b35515b731f9c50752bb5f38fb4330c1b0dc01033b55c)

O problema acontece caso o usuário clique em Atualizar Dados e Modelo, que serve para forçar que o Ploomes detecte um novo valor de produto ou fator, por exemplo. Neste caso o Ploomes vai puxar o modelo padrão, revertendo a modificação visual realizada acima.

## Como evitar o problema

Para evitar o problema é bem simples: basta criar um novo campo no editor de propostas, que servirá para armazenar seus textos editáveis. O campo pode ter um valor padrão que seja o texto que era fixo até então. Assim, sempre que você for gerar uma proposta, ele já estará preenchido com o texto mais frequente, mas poderá ser editado quando necessário. Desta forma, mesmo que o modelo precise ser recarregado, o texto estará seguro vinculado à variável, e não ao modelo em si.

[![Imagem 3: Para evitar o problema é bem simples: basta criar um novo campo no editor de propostas, que servirá para armazenar seus…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328863/9f274798f037ce59511d34c5/ploomes_proposta_criacao_campo.png-expires%3D1619791200-signature%3D6dd020c3e4f1427821a1640e4796e552428d85fef029245645d112646277b23b?expires=1786536000&signature=4f5e3e9f23ab08cdeee8fe57c01ada578643db3df2c862529cb2da48318d7dc8&req=dyYuFct2lYdcFb4V1XW4gRKYSk8SdCgDn%2FTb0Q71u0VkCFWRJx7Ia5SAYGLK%0Ag1S5qDFEyjvTcYgtp3d7ELRtJQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/93872317/53923ad405b2566d6803cc4a/ploomes_proposta_criacao_campo.png?expires=1619791200&signature=6dd020c3e4f1427821a1640e4796e552428d85fef029245645d112646277b23b)

[![Imagem 4: Para evitar o problema é bem simples: basta criar um novo campo no editor de propostas, que servirá para armazenar seus…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328871/bba51b885f6b782b9a6e9e60/image.png-expires%3D1619791200-signature%3D63b5092637854981990657add44b1059ccdfcd3b2ac572639cd3f620b396da02?expires=1786536000&signature=1d30beb7c0886c55c36974ddc012475fd6ab3ea500493415f56a1f6eba210530&req=dyYuFct2lYZeFb4V1XW4gcqRn7lc39%2BFAQmtr%2F%2Fzd8ln%2BzatoCZXGJ4TmYMA%0AV4WMc2ybmZa8JUH0ziJw5aV5TQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/93872459/e7fbd600b96892e35f7f7722/image.png?expires=1619791200&signature=63b5092637854981990657add44b1059ccdfcd3b2ac572639cd3f620b396da02)

A imagem acima mostra o campo criado posicionado onde antes estava o texto variável.

Por fim, ao gerar ou editar uma proposta, será possível ver que agora existe um campo novo que representa o texto em questão, como mostrado a seguir:

[![Imagem 5: Por fim, ao gerar ou editar uma proposta, será possível ver que agora existe um campo novo que representa o texto em…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328881/dfab775eab1370c9b03c99f9/ploomes_novo_campo_proposta.png-expires%3D1619791200-signature%3Db1f7e8c532213eecca7f94058e810868f5ea885bc3840895768de5371750287f?expires=1786536000&signature=100feac448a0246e868e3e0989671108e9d96efaf3d93e7f4fe9347a34c0c28e&req=dyYuFct2lYleFb4V1XW4gX%2FuQBXgEjIGfHZjut3LoPMMzqVAIYzCvJichvVI%0AXvdSoLg5oRgQYpmpXyy6umY%2Fbg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/93873159/b821f0e56003e76547970a34/ploomes_novo_campo_proposta.png?expires=1619791200&signature=b1f7e8c532213eecca7f94058e810868f5ea885bc3840895768de5371750287f)

Assim, todas as alterações às condições podem ser feitas no campo e recarregar o modelo não causará riscos de perda do conteúdo editado.
