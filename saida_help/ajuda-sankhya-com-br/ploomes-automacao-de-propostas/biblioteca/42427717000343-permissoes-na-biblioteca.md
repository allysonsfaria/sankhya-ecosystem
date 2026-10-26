---
id: "42427717000343"
titulo: "Permissões na biblioteca"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427717000343-Permiss%C3%B5es-na-biblioteca"
trilha: "PLOOMES: Automação de propostas  > Biblioteca"
atualizado_em: "2026-08-10T18:08:16Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452268", "sync_hash_173cf8c8fe69"]
---

# Permissões na biblioteca

## Permissões em Administração

Ao ativar o módulo, a opção de “Biblioteca” vai aparecer nas regras de perfil. Se o nome do módulo foi alterado, então a nova opção de regras terá este nome personalizado. As regras para o módulo de biblioteca em Administração afetam as ações do usuário no módulo como um todo. As regras existentes são:

- “Tem acesso ao módulo de arquivos?” - Os perfis que tiverem a opção “Não” marcada perderão a possibilidade de acessar o módulo de biblioteca porque não constará o botão do módulo no menu.
- “Pode criar pastas-mãe?” - Os perfis que tiverem a opção “Não” marcada não perderão criar pastas-mães, isto é, as primeiras pastas das hierarquias de pastas. Se o administrador assim o desejar, também conseguirá impedir que os usuários criem subpastas através das permissões das pastas.

  ![Imagem 1: “Pode criar pastas-mãe?” - Os perfis que tiverem a opção “Não” marcada não perderão criar pastas-mães, isto é, as…](https://downloads.intercomcdn.com/i/o/564946125/419ab6ea68d153ff1561704d/image.png?expires=1786536000&signature=d6ec11082bba85ab38f5a23c8fe291e2eb0eaac2b2cc7a0fbcc2c88f9464d655&req=cSYjH814nINaFb4V1XW4gRcelFJKb8wuiRln7FgL85ze6ELmu2hAMu2zBI%2Fu%0AMXoshNYKD65mXd1gS1bUFuFYnw%3D%3D%0A)

## Permissões das pastas

As permissões existentes para as pastas e seus arquivos são: **visualização, edição** e **exclusão.** Os usuários que puderem ver uma pasta, também têm permissão para **visualizar e baixar** os arquivos contidos naquela pasta. A permissão de edição permite a **criação e a movimentação** da pasta e de seus arquivos. Por fim, a permissão de exclusão permite que o usuário **exclua** a pasta e seus arquivos.

![Imagem 2: As permissões existentes para as pastas e seus arquivos são: visualização, edição e exclusão. Os usuários que puderem…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326115/353c18c61f94c38cf8650fec/mceclip2.png?expires=1786536000&signature=ef349e034becf5976be28f381714dcc6018a38dbd85a8f0c966f9619e5bb1bdc&req=dyYuFct4nIBaFb4V1XW4gZekw1c%2FD0hjvlkbFWBJjpiTeAr%2BnkJnYS%2BXGOs0%0AHn%2FU2lhNhS5BYy%2Fzqj4YUD9%2BSw%3D%3D%0A)

- **Hierarquia das permissões -** Cada pasta tem sua própria permissão, que é

limitada sempre pelas regras de permissão da pasta anterior. Isso quer dizer que a pasta anterior à pasta que está sendo configurada sempre vai limitar as possibilidades de regras que poderá receber, mas as pasta-mãe, por serem as primeiras da hierarquia, têm mais flexibilidade de permissões e ditam o comportamento das demais pastas abaixo delas.

Observe o exemplo da imagem abaixo. As subpastas B, C e E respeitam as permissões, já que a pasta anterior, a pasta A, possui a permissão mais ampla de todas. No entanto, a pasta F está configurada incorretamente. Sua pasta anterior, a pasta E, permite apenas o acesso do Carlos. Portanto, por mais que esteja configurado para todos acessarem a pasta F, somente o Carlos poderá ver e acessar a pasta F.

![Imagem 3: Observe o exemplo da imagem abaixo. As subpastas B, C e E respeitam as permissões, já que a pasta anterior, a pasta A,…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326118/702bd32605833aacd1369626/mceclip3.png?expires=1786536000&signature=e80d8a55c94ef1d12a11878857e67745c42a8c5e26ceedae885b2a895d15cf8e&req=dyYuFct4nIBXFb4V1XW4gYYv2S%2BNXhZCcfNBTF0OGAsz5ioqZ4PARdIVaV%2B4%0AMIl5G%2BdQVxa0XhhJpZXYzBFnqQ%3D%3D%0A)

- **Hierarquia dos tipos de permissões -** Além disso, a pasta-mãe também

tem o papel de ditar o **tipo de permissão** das suas subpastas; se é **por usuário, por perfil** ou **por equipe**. O tipo de permissão deve se manter o mesmo em toda árvore da pasta-mãe e o próprio sistema não vai permitir a mudança para outro tipo senão o definido como padrão.

No exemplo abaixo o tipo de permissão configurado na pasta-mãe A foi o tipo de usuário, que permite o acesso de Bento e João. As subpastas B, C e D estão com permissões corretas porque também têm permissões por usuário, incluindo as combinações possíveis entre Bento e João. A pasta E está incorreta porque Carlos não pertence à permissão da pasta-mãe A. As pastas F e G também estão com permissões erradas porque possuem tipos de permissão diferentes da pasta-mãe A.

Este comportamento é causado por uma limitação técnica que originou-se da necessidade de restringir as permissões das subpastas para grupos de usuários menores do que o grupo da pasta-mãe.

![Imagem 4: Este comportamento é causado por uma limitação técnica que originou-se da necessidade de restringir as permissões das…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326123/bfe4cc7e4d2e10799357d81f/mceclip4.png?expires=1786536000&signature=9ab017a29f4e9435486d50df2fd6c47cc727860e0bdb7cb91a9f73abd60277e2&req=dyYuFct4nINcFb4V1XW4gb8Oq%2FNC9GSL0NxYoBSvtkeM8A0acNONxz8fEemQ%0A20FgRFjJ8lLCSFo1QLIrswt9lQ%3D%3D%0A)

## Mudanças nas permissões

É possível que alguns usuários queiram editar as permissões de pastas uma vez que as permissões de uma árvore de pastas já tenham sido criadas. O usuário deve proceder com cautela porque o tipo de modificação pode acarretar em propagações equivalentes nas subpastas da pasta editada. Confira os cenários e suas consequências.

- **Edição do tipo de permissão -** A alteração do tipo de permissão para outro propaga nas subpastas a mesma permissão nova. Exemplo: se uma árvore está estruturada com um tipo de permissão de perfil de usuário e o tipo for trocado para equipe, todas as subpastas terão a mesma alteração de permissão da pasta-mãe.

![Imagem 5: Edição do tipo de permissão - A alteração do tipo de permissão para outro propaga nas subpastas a mesma permissão nova.…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326132/9048bb0d455dfc86ee12c545/mceclip5.png?expires=1786536000&signature=0b8a2d8eafa6e68863d089090693b09459a56de241f36c55c35c3dd9bde72376&req=dyYuFct4nIJdFb4V1XW4gdHRwz6l7DSMky5cfaIe6hIwoMSgi8%2BXozafYawM%0AvM2iSGzywCTpa2qscCFoaClW0A%3D%3D%0A)

- **Edição de uma pasta pública para se tornar restrita -** Se uma estrutura de pastas estiver totalmente irrestrita e o usuário trocar a permissão da pasta-mãe para uma configuração restritiva, todas as suas subpasta herdarão a mesma restrição.

![Imagem 6: Edição de uma pasta pública para se tornar restrita - Se uma estrutura de pastas estiver totalmente irrestrita e o…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326135/1182703a7682e0b54fbc71fa/mceclip6.png?expires=1786536000&signature=c4525619bfe95a58591b75180204130399abc5954f818da3031c535fab8bfb15&req=dyYuFct4nIJaFb4V1XW4gXJc3WuS%2BtkKseiRLJK80oYSl3B268vLlo%2FooJWS%0AnupQw6Ekh7lnItyeXlJAZCK8Sg%3D%3D%0A)

- **Edição de uma pasta restrita para se tornar pública -** Em uma árvore de pastas restritas, a liberação da permissão para todos da pasta-mãe não afeta as suas subpastas. Elas vão continuar com as mesmas restrições anteriores e se o usuário quiser, vai precisar liberar uma a uma.

![Imagem 7: Edição de uma pasta restrita para se tornar pública - Em uma árvore de pastas restritas, a liberação da permissão para…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326141/14ffa2d36e3f240aaf9f672f/mceclip7.png?expires=1786536000&signature=c13ed0d78e882b0ab4d44decdc5c4d022ec02e9a16784d2a2a81328b3241d846&req=dyYuFct4nIVeFb4V1XW4gdrotTDFYA5o%2FJJ97uSLmvSO4wVT9Bex4o%2Bqee9K%0ASI80YTEuj0jN529DivHwDkmOXA%3D%3D%0A)

- **Inserção de permissões -** Se uma nova alternativa for incluída na pasta-mãe, ela vai ser propagada e incluída em todas as subpastas.

![Imagem 8: Inserção de permissões - Se uma nova alternativa for incluída na pasta-mãe, ela vai ser propagada e incluída em todas…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326149/f0aa59502b2b229cb56612ed/mceclip8.png?expires=1786536000&signature=4d948e944a0438dab0076113f486919bbc2be653475db8165f0e973cbae29158&req=dyYuFct4nIVWFb4V1XW4gVqq7BFdmaNabyAburqVmt1jnHKsrlQngW2FCJ6k%0AgGo8wZLBcloZMsidZd2zZClleg%3D%3D%0A)

- **Remoção de permissões -** Se uma alternativa existente for removida da pasta-mãe, ela vai ser removida em todas as subpastas.

  ![Imagem 9: Remoção de permissões - Se uma alternativa existente for removida da pasta-mãe, ela vai ser removida em todas as…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326157/5a51829f88e9eb169c7f92be/mceclip9.png?expires=1786536000&signature=90d7dfce3f3fc53ede9d86407b236b847733976a88e12b2ee1b1f3e075b862c6&req=dyYuFct4nIRYFb4V1XW4gehmOWZiwrQCZo4kAi1kxSGXOO29tAVvKDsbIUeJ%0AVCCDZX8UlsbcfBKicemLA6%2Ffwg%3D%3D%0A)

## Movimentar pastas e arquivos

Os usuários do sistema têm a possibilidade de movimentar pastas, itens e coleções para outras localidades dentro do módulo, porém seguindo as suas permissões de visualização e edição. Os comportamentos esperados das movimentações são os seguintes.

- **Manutenção das permissões -** As permissões das pastas movidas se manterão as mesmas quando:

a. As pastas possuem o mesmo tipo de permissão.

![Imagem 10: a. As pastas possuem o mesmo tipo de permissão.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326163/242b08f5b7c3ae1b2b3b6569/mceclip10.png?expires=1786536000&signature=fd8fc36e678cdb94261cbd3d5859fadd8cf76b5e67ff2414d39d9fbd983c13f3&req=dyYuFct4nIdcFb4V1XW4gc6w12jVugfdbY%2BU1vc5n2RV7GWy7SphA2tj3%2BnM%0ASVcSalWWP7qIm50oneY72k2xgg%3D%3D%0A)

b. A pasta de origem possui uma restrição mas a pasta de destino está com visualização para todos da empresa.

![Imagem 11: b. A pasta de origem possui uma restrição mas a pasta de destino está com visualização para todos da empresa.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326165/7978380178aee5e25d4e96d6/mceclip11.png?expires=1786536000&signature=17996fde650982f0d9cb267caaff511843b46bb19a105643f4881f1e7bed40b3&req=dyYuFct4nIdaFb4V1XW4gaFzeNdzs2%2FNHzq4FS9jGD%2B1TQv8UVh4zqgWme17%0A3r3ZQbvexkTLEW1oJNh7SWyzjg%3D%3D%0A)

c. A pasta origem possui restrições que estão contidas nas restrições da pasta destino.

![Imagem 12: c. A pasta origem possui restrições que estão contidas nas restrições da pasta destino.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326171/7f8c82d81b08b7f8617e4453/mceclip12.png?expires=1786536000&signature=386767edd2e31378fa21c7f6a4053e5c3c43a31bfca87b05ed1564fd31c6b05f&req=dyYuFct4nIZeFb4V1XW4gdUUQ8dIm2Gawz2Fr58q2%2BAT5muap5Ne8y4JijBC%0AT3q5iH7bxNIPRrrhdCoEbFqHKg%3D%3D%0A)

- **Perda de parte das permissões -** Há perda de parte das permissões quando:

a. Pasta de origem for mais restrita do que a pasta de destino, sendo que a pasta de origem contém as permissões da pasta destino.

![Imagem 13: a. Pasta de origem for mais restrita do que a pasta de destino, sendo que a pasta de origem contém as permissões da…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326181/414e8947d53f09ba64096f23/mceclip13.png?expires=1786536000&signature=511d5596495a5cbeebe9d34916a2bb7450cf9387152c72aafa9f845dc1d9543d&req=dyYuFct4nIleFb4V1XW4geI891%2BeyMPBMGc3vf5NxRQi1O%2FlTszKLOX1bKlv%0AL8cKRO%2By86wQ%2FaG6DgFl06t8FQ%3D%3D%0A)

- **Perda das permissões -** A situação em que todas as permissões são perdidas e somente o administrador da conta terá acesso é:

a. Uma pasta e suas subpastas são movidas para dentro de uma pasta restrita.

![Imagem 14: a. Uma pasta e suas subpastas são movidas para dentro de uma pasta restrita.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326183/b0f28cb3142e9795747181f5/mceclip14.png?expires=1786536000&signature=6971728f6c63b15895c3d4e7a33c4cf7ca9fa0a0e0745a8fc95f85e8831d618a&req=dyYuFct4nIlcFb4V1XW4gWOuh4L6UNWgfhP%2FlAOWaaWim0zee16VLcggMA1c%0AKdLBmoN9YlSpUl6AzPbw%2B7TUiw%3D%3D%0A)

- **Utiliza as permissões da pasta superior -** As situações em que a pasta movida replica as permissões da nova pasta superior são:

a. As pastas possuem o mesmo tipo de configuração de permissões, porém contém permissões não compatíveis.

![Imagem 15: a. As pastas possuem o mesmo tipo de configuração de permissões, porém contém permissões não compatíveis.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326189/25a360d52e006f46fb9511c3/mceclip15.png?expires=1786536000&signature=da321464d83a244d8dd68af9912c8e1ebde303f41071b9ae511cc46e20534aa0&req=dyYuFct4nIlWFb4V1XW4gfdd1kbqU%2BCV7NC6iPoHr95WkOYOTirtr%2FcR1rY8%0A5T52aLy4MwfRuMxh2Jig0yoQWw%3D%3D%0A)

b. As pastas possuem configurações de tipos de permissões diferentes.

![Imagem 16: b. As pastas possuem configurações de tipos de permissões diferentes.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369326194/586108acc3a598cb14b380d7/mceclip16.png?expires=1786536000&signature=603b14e7c3837fb1c831adb15b64beb7e60d9c745d79bd2b8ada4c91edc6f2f9&req=dyYuFct4nIhbFb4V1XW4gXvZmhIZaRkglDGFl47ZxEiX9IFz1PpCgmHJE7a0%0AWegI765TDUqUSSQfKos6FbvlFQ%3D%3D%0A)
