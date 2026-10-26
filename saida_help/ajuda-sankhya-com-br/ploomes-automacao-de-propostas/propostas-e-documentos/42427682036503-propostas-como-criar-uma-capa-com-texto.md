---
id: "42427682036503"
titulo: "Propostas - como criar uma capa com texto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427682036503-Propostas-como-criar-uma-capa-com-texto"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-11T16:13:55Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452277", "sync_hash_e00851404d07"]
---

# Propostas - como criar uma capa com texto

Como criar uma capa com campos inteligentes, como nome de cliente e data da proposta

Para editar os modelos de proposta, vamos em administração - [modelos de documentos](https://app.ploomes.com/templates/quotes)

Nesse caso, vou criar um novo modelo de propostas, mas isso pode ser feito com qualquer modelo existente!

Vou inserir minha capa em uma Seção separada:

[![Imagem 1: Vou inserir minha capa em uma Seção separada:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327055/ddd937003aacc458e127660d/image.png-expires%3D1619359200-signature%3Db5cf616ca2c6e5ef39d04212fe80b943fd309da0a1d62d54813055a9160e6d84?expires=1786536000&signature=877e4776eb8c52aac4768e555b8a9e0bc252022e25e31e4ce54b0f244dbbc320&req=dyYuFct5nYRaFb4V1XW4gdOBizdj1y3ZDiKbYonz2e9yctWU0xjjoQ1y4TY6%0AB5NZxKDJZBeUdahr%2BwdOi2ygPA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135970531/8a099e31667646a2bbfde229/image.png?expires=1619359200&signature=b5cf616ca2c6e5ef39d04212fe80b943fd309da0a1d62d54813055a9160e6d84)

[![Imagem 2: Vou inserir minha capa em uma Seção separada:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327061/66a5b30349619b2386074058/image.png-expires%3D1619359200-signature%3D1b88da9ae97d4837e7c9e044fde9f28f8995fc94be70a5e5cea38cbccf2a56ac?expires=1786536000&signature=14bd74ca7f56c2a0507fe372dbf352ceb83c0bd33c17924d864cc3df4e50aa3d&req=dyYuFct5nYdeFb4V1XW4gZ7qZXV4EYSL0p4flrfnNc2TDl9rbE0oREYoDhyw%0AxZuYXPb9PKAHJZ0St9KfuaiU3w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135970604/22e9a07f1099b8b8944d89c4/image.png?expires=1619359200&signature=1b88da9ae97d4837e7c9e044fde9f28f8995fc94be70a5e5cea38cbccf2a56ac)

Para facilitar sua edição, disponibilizamos um código que vai te auxiliar na edição da capa. Vamos abrir o código fonte e colá-lo lá.

[![Imagem 3: Para facilitar sua edição, disponibilizamos um código que vai te auxiliar na edição da capa. Vamos abrir o código fonte…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327068/ed1266a8bc989413e7e4e995/image.png-expires%3D1619359200-signature%3D3d9fc0f5fb1fe3ff048a2b652465066d7907f0fa6c1a13497f16e46f792bf83d?expires=1786536000&signature=3211028dab038a54d792a6f5518ca4da68ff1a4b0632bda9cd8ca823f405caff&req=dyYuFct5nYdXFb4V1XW4gRjOYgaTpo57V8dXiLk%2F%2Bik8NCPl2KjhglebQ8j3%0ABTg9uQr94lIg5t%2FX%2FgFvmHyyeg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135970865/aa76867deba4062c0e05a463/image.png?expires=1619359200&signature=3d9fc0f5fb1fe3ff048a2b652465066d7907f0fa6c1a13497f16e46f792bf83d)

[![Imagem 4: Para facilitar sua edição, disponibilizamos um código que vai te auxiliar na edição da capa. Vamos abrir o código fonte…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327081/c8aae6e2b875613595370fa9/image.png-expires%3D1619359200-signature%3D921f0085f27e7003e25a772667579f1aab290db250044a8d1e59c204d411341b?expires=1786536000&signature=1c03129d0cae9a2a88e6abbc94acc3a1ef7ccce6913323ef7eff1725910c4ac4&req=dyYuFct5nYleFb4V1XW4gepSKGmFuiQmduHmpr1YtjCTv8on6CrFDUiX7VC1%0ADR83Jc8p7t3zImH9Oxq4BR6oCQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135971020/c8ab980fe6b08436aa058adc/image.png?expires=1619359200&signature=921f0085f27e7003e25a772667579f1aab290db250044a8d1e59c204d411341b)

O código é o seguinte:

<div ><img alt="" src="https://ploomescrm.s3-sa-east-1.amazonaws.com/E9B11508301A/Images/3cc7f9d029384594a2f6f69f9838e748.png" />
 <div >
 <table >
 <tbody>
 <tr>
 <td >&nbsp;</td>
 <td >
 <p><span ><span ><strong><field key="contact\_name" path-id="1">[Cliente.Nome]</field></strong></span></span></p>

<p><span ><field format="d" formattable="date" key="quote\_date" path-id="56">[Proposta.Data]</field></span></p>

<p>&nbsp;</p>
 </td>
 <td >&nbsp;</td>
</tr>
</tbody>
</table>
</div>
</div>

Colado o código, vamos sair da janela do código-fonte e editar a imagem!
Clique duas vezes na imagem para escolher uma nova;

[![Imagem 5: Colado o código, vamos sair da janela do código-fonte e editar a imagem! Clique duas vezes na imagem para escolher uma…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327089/f6c652c8b2767db5a6521e23/image.png-expires%3D1619359200-signature%3D63acb5f74f0d25b257c3a570b8553733936c645553b4e00f66e732a7dae823c5?expires=1786536000&signature=79de65026a628458c216d939713a5472d2a647c8b28a0977e388f9ba7d2b3267&req=dyYuFct5nYlWFb4V1XW4geOlNdtx1vXASYWfz264vrfVRiJ16ZdH6EC9Kxbc%0Ac4br83%2Ba3gWjS%2B8gvEyha%2FxXYA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135973648/6ae68bb9bd3eb8807939d33e/image.png?expires=1619359200&signature=63acb5f74f0d25b257c3a570b8553733936c645553b4e00f66e732a7dae823c5)

Você pode escolher uma nova de seu computador ou uma que já tenha sido upada ao ploomes. Nesse caso já inseri a minha, então vou escolher direto do menu:

[![Imagem 6: Você pode escolher uma nova de seu computador ou uma que já tenha sido upada ao ploomes. Nesse caso já inseri a minha,…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327092/bfa76f4e6694799ec4f2c714/image.png-expires%3D1619359200-signature%3D76f907d3eaf09cd17ad781e1bb83df1b4da66932f5cf9a8e1dc9b1a5691dc8c0?expires=1786536000&signature=6e59f2d0c700cd43c7ece0085d0e9a02d3c215ec1f2fb634727e49c8ba1c7609&req=dyYuFct5nYhdFb4V1XW4gX3CVprmB2y8JdGOg1bd%2F060IPaJEyf8lgsLxSPK%0AEUNDGkeLw8ThbZm1gHbh6xlxVw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135974013/97bd5a334a9ac3301c67d67b/image.png?expires=1619359200&signature=76f907d3eaf09cd17ad781e1bb83df1b4da66932f5cf9a8e1dc9b1a5691dc8c0)

Agora, sem dar atenção à largura na tela de formatação, vamos dar o "ok"

[![Imagem 7: Agora, sem dar atenção à largura na tela de formatação, vamos dar o "ok"](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327098/92c5aa5f5aa014737c44388d/image.png-expires%3D1619359200-signature%3D45fb0647e83916ef4edfa769a570d24a770f341faba8265533a88ba0e2e53e2b?expires=1786536000&signature=4e01f61af546ed85a3a420b20c724ada6103a17527847f8fa33717dc350e79d1&req=dyYuFct5nYhXFb4V1XW4ge7FLxkRrdmFm8TXuQwdWdJLte6E7hQ38WV7kLz%2F%0AU3pAup2Dss935aSu1fgvufVe8w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135974194/dc4fc1473bd7ce097ae9ed0d/image.png?expires=1619359200&signature=45fb0647e83916ef4edfa769a570d24a770f341faba8265533a88ba0e2e53e2b)

Em "estilos", removo as bordas:

[![Imagem 8: Em "estilos", removo as bordas:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327106/2c221d2e5c5a8b91e1e3220d/image.png-expires%3D1619359200-signature%3D90c20911921017ff1bdc5c2d42fa2cb0936e9030a7582bf269a70af00efaca60?expires=1786536000&signature=5a6081efe751cd2c37a6ffcb13614e08d5f0b66dd625edf0f17cdf30447a5b4a&req=dyYuFct5nIFZFb4V1XW4gRkrIEE4Ie8vf9VZG5SM4iwu0JM%2FoFQ0wup3sIUI%0AIilPOtmojP18HLlJr7JImm%2FjGQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135974368/236cbff78076716ad3c50fbf/image.png?expires=1619359200&signature=90c20911921017ff1bdc5c2d42fa2cb0936e9030a7582bf269a70af00efaca60)

Agora, para formatar a imagem: Abro novamente o código-fonte e edito a altura para 1122.5 e a largura para 800 (ambos se situam na primeira linha)

[![Imagem 9: Agora, para formatar a imagem: Abro novamente o código-fonte e edito a altura para 1122.5 e a largura para 800 (ambos…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327111/0ab56d075ef5dbeaa9f7a019/image.png-expires%3D1619359200-signature%3D98d2f64b82b04722a362ffaa2ac11ec77251cead7207b2c69467f3f07a490719?expires=1786536000&signature=bcf54ff27a6a2dc616075a7b81c7a1cc512c34e141339e0f40ad0ea4fe5fec49&req=dyYuFct5nIBeFb4V1XW4gaHn%2F2joi72TG546U%2BQ6LLWgPIKIr3gzdu9Hd3vN%0A%2FrOBph%2B76y1Vupa6VllJE%2FpE9A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135974642/e6b8f8595ce9f507176d7c0f/image.png?expires=1619359200&signature=98d2f64b82b04722a362ffaa2ac11ec77251cead7207b2c69467f3f07a490719)

[![Imagem 10: Agora, para formatar a imagem: Abro novamente o código-fonte e edito a altura para 1122.5 e a largura para 800 (ambos…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327119/06668be90b50d3d435851fc5/image.png-expires%3D1619359200-signature%3D3b14c9abf1ae1da9a810b83847d8e1f8d3112dc23fff28a97876fc4fcf8746a1?expires=1786536000&signature=1e4f0aaa9746befa7d843f7127773fd824d6c95f6a8eddf1f70ade8c3df3c5ad&req=dyYuFct5nIBWFb4V1XW4gd91dzoz8Tb3UV%2BGrh1KAf0efXHefhhUJA730dj7%0A%2B8GridsusLujyWNm%2BTfcm1LGzg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135974709/7fb0a3ce34e4733ee9695199/image.png?expires=1619359200&signature=3b14c9abf1ae1da9a810b83847d8e1f8d3112dc23fff28a97876fc4fcf8746a1)

Está feita a capa!

Agora, para configurar onde ficam os campos inteligentes, editamos o "top" na segunda linha:

[![Imagem 11: Agora, para configurar onde ficam os campos inteligentes, editamos o "top" na segunda linha:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327132/8fce0cc5e5b32e56f5f8e40a/image.png-expires%3D1619359200-signature%3D84952b443f5fdbcdbb5aa8af3b86f69690c8d765a43cb7f375d071c38509e66b?expires=1786536000&signature=547d362a46cfff5ab161d5b458da8e9bcbd3a49d14a1ce7b83ec82de079e892c&req=dyYuFct5nIJdFb4V1XW4gUnNXn5nhM3Aod9fj73sPqJ1jjJb2GQKmLsoyTeq%0A8W8cC7U73dEa5GBGMfE8%2FfHGYA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/135976161/ee74d07dda5edad3a6b140df/image.png?expires=1619359200&signature=84952b443f5fdbcdbb5aa8af3b86f69690c8d765a43cb7f375d071c38509e66b)

Esse valor é o número de pixels entre o topo da tabela e o começo da capa. quanto maior esse valor, mais para baixo vão estar os campos.
