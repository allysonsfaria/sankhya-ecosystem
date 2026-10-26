---
id: "42427490728855"
titulo: "Caso de uso: Troca de responsável em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427490728855-Caso-de-uso-Troca-de-respons%C3%A1vel-em-massa"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T18:03:31Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7942870", "sync_hash_f9f029cfbc98"]
---

# Caso de uso: Troca de responsável em massa

Em situações como a saída de um vendedor da empresa, pode ser necessário transferir todos os clientes sob sua responsabilidade para outro usuário.

Esse processo pode ser realizado de forma rápida e prática utilizando a **edição em massa**, permitindo atualizar diversos registros ao mesmo tempo.

⚠️ **Atenção:** A edição em massa é **irreversível**. Antes de confirmar a alteração, verifique cuidadosamente se os dados exibidos correspondem exatamente aos registros que você deseja modificar.

## Como realizar?

## Criar uma aba com os clientes do responsável atual

No módulo **Clientes**, crie uma **Nova aba** para reunir todos os clientes do usuário que terá o responsável alterado:

- Clique em **Nova aba**;
- Defina um nome para a aba e escolha quem poderá visualizá-la;
- Adicione o filtro com a condição: **Responsável > Igual a > [usuário atual]**;
- Clique em **Criar aba**.

![Imagem 1: Clique em Criar aba .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2056765530/905e24ae10dccd18b046f6377a65/image.png?expires=1786536000&signature=60328898df02d3d649f16ef9736b643ebe5eaa0dbdb600028093f83b92926c6f&req=diAiEM54mIRcWfMW3nq%2Bgb37zeI4eq%2FfThK5IBuXi277JHfmGqck8cPKowWC%0AsB3Y%2BA21jzN22vL2HySsMF0nJ9s%3D%0A)

Caso o usuário já esteja **inativo**, utilize a seguinte condição no filtro:
**Responsável** > **Nome** > **Igual a** > **[nome exatamente igual ao do usuário inativo]**

![Imagem 2: Caso o usuário já esteja inativo , utilize a seguinte condição no filtro: Responsável > Nome > Igual a > (nome…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2056773487/2acac14c52f295de8ed083245be8/image.png?expires=1786536000&signature=00c2f5a9596eea1916304eb12347c481a0997f1f8e181d39d78637313f7b79e6&req=diAiEM55noVXXvMW3nq%2BgbKdYSIpHCzpNX2TYSsvjiCmNUer9SMDiwMxi545%0AWCDSzndXw%2F3%2F6XDUowdnRZSh1zk%3D%0A)

## Conferir os itens listados

Após criar a aba, revise atentamente a listagem para garantir que **todos os clientes exibidos** pertencem de fato ao responsável que será alterado:

- Clique no ícone de engrenagem ao lado das colunas e adicione a coluna **Responsável**;
- Confira a **quantidade de itens** exibidos na aba;
- Verifique se a coluna **Responsável** corresponde exatamente ao usuário que terá os registros alterados.

[GIF animado: Imagem 3: Verifique se a coluna Responsável corresponde exatamente ao usuário que terá os registros alterados.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2061918324/e9e0ef07d6ca36a705342b9b7ac5/responsavel.gif?expires=1786536000&signature=8218ec35c17f872dbd3989030ff927caa50b9371cc6cc178ee67422c6c185915&req=diAhF8B%2FlYJdXfMW3nq%2BgWpy9sN6nFLgyN80YxEcLRUilHs0eRDXAbtcfXzo%0Ay%2BU%2BXZjFonsMqUfpCtqoWsBi3Uw%3D%0A)

## Realizar a edição em massa

Quando tiver certeza de que a aba está configurada corretamente, clique no ícone de engrenagem ao lado do nome da aba:

- Clique em **Edição em massa**;
- Escolha o campo **Responsável**;
- Selecione a operação **Substituir por**;
- Defina e adicione o novo usuário responsável;
- Clique em **Confirmar alterações**.

[GIF animado: Imagem 4: Clique em Confirmar alterações .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2061944821/c0508c9bf9437307d880731c372e/edicao.gif?expires=1786536000&signature=e538cced4a3018507d1872e22099ab0624c76dc6012d32fc8daf6eb086279cb3&req=diAhF8B6mYldWPMW3nq%2BgWYkuEFLXZtF8j93dsUDhGCj4qv7uNwzqbQjcguA%0AXDEs1ogLJ%2Baw34QNeuEqTtWXVcM%3D%0A)

## O que acontece depois?

Após a conclusão da alteração, a aba ficará vazia. Isso ocorre porque o filtro permanece configurado com o responsável anterior. Para visualizar novamente os clientes, basta editar o filtro e substituir pelo novo responsável.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
