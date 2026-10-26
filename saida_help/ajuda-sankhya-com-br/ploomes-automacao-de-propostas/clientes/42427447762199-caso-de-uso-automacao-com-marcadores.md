---
id: "42427447762199"
titulo: "Caso de uso: Automação com marcadores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427447762199-Caso-de-uso-Automa%C3%A7%C3%A3o-com-marcadores"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T18:04:19Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7925201", "sync_hash_588156314c2e"]
---

# Caso de uso: Automação com marcadores

No Ploomes, é possível utilizar marcadores nas automações para otimizar e organizar seus processos.

Neste exemplo, vamos configurar uma automação que preenche automaticamente o campo de marcador com **“Caso urgente”** sempre que um cliente criado pertencer à região Sul.

## Como criar marcadores?

- Acesse a tela de **Clientes**;
- Clique em **Menu**, no canto superior direito;
- Selecione a opção **Configurar marcadores de cliente**;
- Defina o **nome** e a **cor** do marcador desejado.

[GIF animado: Imagem 1: Defina o nome e a cor do marcador desejado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2070582953/ee15f178c3442eb746ae19138f1b/marcador.gif?expires=1786536000&signature=55f13441a4baec8f99a261782ca30f13417f74f3800124b2df56b0a86bfb13cd&req=diAgFsx2n4haWvMW3nq%2BgVcggxQQlXJCj7ISj3yp0%2BO%2F%2FwABqcBEtngxIOBz%0A0VoYaaM6wWPuezi8cjiiM6B6EPA%3D%0A)

## Como criar a automação?

- Acesse **Administração > Automações**;
- Selecione a entidade **Cliente** e clique em **Nova automação**;
- Defina o gatilho como **Quando o item for criado**;
- Configure o filtro:

  - **Região** > **Igual a** > **Sul;**
- Configure a ação:

  - **Editar dados** > **Marcadores** > **Valor estático** > **Caso urgente;**
- Clique em **Salvar**.

[GIF animado: Imagem 2: Clique em Salvar .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2070748719/e6d51c93f09f5210d00784f663d2/automacao.gif?expires=1786536000&signature=da98bf506779c276bd44ec664ede80dadf2e7e00cbd722cfb1be62fb1477b85a&req=diAgFs56lYZeUPMW3nq%2BgUKKPuPYi3up1qZn8H1dTXJAcjHbrHdVOJPNV62y%0Ajh8Q13u84zz1QJGQh6GQh0vlC0k%3D%0A)

## Como limpar marcadores?

O campo de **Marcadores** é do tipo múltiplo, ou seja, permite a associação de mais de um marcador ao mesmo registro.

No entanto, quando os marcadores são utilizados para segmentação de clientes ou negócios, pode ser mais estratégico manter apenas **um marcador por vez**, facilitando filtros e análises.

## Como limpar por automação?

Neste exemplo, quando o cliente tiver o campo **“Status”** alterado para **Ativo** e pertencer à **região Sul**, a automação irá remover o marcador **“Caso urgente”** e adicionar o marcador **“Fora da prioridade”**.

- Acesse **Administração > Automações**;
- Selecione a entidade **Cliente** e clique em **Nova automação**;
- Defina o gatilho como **Quando o item for editado**;
- Configure o filtro:

  - **Região** > **Igual a** > **Sul**
  - **Status** > **Igual a** > **Ativo**
- Configure a ação:

  - **Editar dados** > **Marcadores** > **Valor estático** > **Vazio;**
  - **Editar dados** > **Marcadores** > **Valor estático** > **Fora da prioridade;**
- Clique em **Salvar**.

[GIF animado: Imagem 3: Clique em Salvar .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2070861782/afc6a4e0a3010b0f7f01c623e7c1/automacao2.gif?expires=1786536000&signature=ffe5fcaba2f6e39852efe07b723a2a82300b61b8922fdf6927a1a1edf67bc8e6&req=diAgFsF4nIZXW%2FMW3nq%2BgXoh1T1ZumCNgGT26GeEF7mXJfbC7DW053IULpX%2F%0AwTyjky0CHkRudvSHul2SQtM0jlQ%3D%0A)

## Como limpar por edição em massa?

Também é possível realizar a limpeza de marcadores por meio da **edição em massa**.

Para isso, é necessário criar uma aba aplicando um filtro pelo marcador que deseja remover.

⚠️ **Atenção:** A edição em massa é **irreversível**. Antes de confirmar a alteração, verifique cuidadosamente se os dados exibidos correspondem exatamente aos registros que você deseja modificar.

- Acesse a tela de **Clientes**;
- Clique em **Nova aba**;
- Defina o **nome** da aba e quem poderá visualizá-la;
- Configure o filtro:

  - **Marcadores** > **Igual a** > **Caso urgente;**
- Clique em **Criar aba**.

![Imagem 4: Clique em Criar aba .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2070925262/482100fe638aedbcdc8d4c141cf8/image.png?expires=1786536000&signature=c07c7af9524cc1f2390e47f6e23e67e249f0da78016cecf52458b0dd2179550e&req=diAgFsB8mINZW%2FMW3nq%2Bgco9olBbKiPLPElg%2FXGH4j00OqH2HamKeAww3OKZ%0AgzP2rZXtPO0ARfj0iFaRiDHSDzk%3D%0A)

Após a criação da aba, siga os passos abaixo para realizar a limpeza dos marcadores:

- Clique em **Ações da aba**;
- Selecione **Edição em massa**;
- Configure:

  - **Marcadores** > **Substituir por** > **Vazio** (ou selecione outro marcador, se desejar);
- Clique em **Confirmar alterações**.

[GIF animado: Imagem 5: Clique em Confirmar alterações .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2071284122/ab4a15f63c687cb2a3a0bdd91e80/ABA.gif?expires=1786536000&signature=d7ead360bda9415a72286d1ddeae44e497b7c2ed5bf1f00b987fe8f087c9f0cb&req=diAgF8t2mYBdW%2FMW3nq%2BgVwhvLUoPi235UYSjia1G6zKmolmSzfQ5t7mE52U%0AkBMZR3d0JdJcgCv%2BQLP2ABPQn8c%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
