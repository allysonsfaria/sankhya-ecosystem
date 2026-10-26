---
id: "42427467945495"
titulo: "Como usar os campos de aniversário do cliente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427467945495-Como-usar-os-campos-de-anivers%C3%A1rio-do-cliente"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T18:01:59Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7959791", "sync_hash_be167d5b1c04"]
---

# Como usar os campos de aniversário do cliente?

Os campos de aniversário são recursos estratégicos que permitem identificar oportunidades de relacionamento com clientes em datas importantes, facilitando ações como envio de mensagens comemorativas.

## Como filtrar clientes por aniversário?

Antes de configurar o filtro, é necessário adicionar o campo **Data de nascimento** ao formulário de cliente.

## Como adicionar o campo ao formulário?

⚠️ Somente usuários com o perfil "Administrador" têm acesso a essa tela e configuração.

- Acesse **Administração > Campos e formulários > Cliente > Pessoas**;
- Clique em **Adicionar campo**;
- Busque pelo campo **Data de nascimento** e adicione-o ao formulário;
- Clique em **Salvar formulário** para concluir a alteração.

[GIF animado: como adicionar o campo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2053108771/5273b4f71cf7ad2cdf95608f9cd0/dataNascimento.gif?expires=1786536000&signature=0552bc1a68f84b04ecaa43e376cdd9bbf79cabdd05065904e36f92ac40897efc&req=diAiFch%2BlYZYWPMW3nq%2BgaeZAQVK23KwQm0VsifTQP5Ig9YlkSozvkTllqWf%0Adi5NRLAJkaJWsmAj7WffYxH7yns%3D%0A)

Dessa forma, ao criar ou editar um cliente, será possível preencher o campo **Data de Nascimento**.

Com essa informação registrada, os campos de **Último aniversário** e **Próximo aniversário** serão calculados automaticamente pelo sistema, permitindo sua utilização em filtros e abas.

## Como fazer o filtro?

- Acesse a tela de **Clientes**;
- Clique em **Filtros** > **Novo filtro** > **Filtro avançado;**
- Defina o nome do filtro e quem poderá visualizá-lo;
- Adicione a seguinte condição:

  - **Próximo aniversário** > **Igual a** > **Data Relativa** > **Hoje;**
- Clique em **Aplicar** ou em **Salvar**, caso deseje reutilizar esse filtro no futuro.

![filtro próximo aniversario](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2053520495/f2ecab16fa33c018fdcdfbd12223/image.png?expires=1786536000&signature=ec6bf92eca427a31b50213c81094b5263013cc1824e296c8d856d74d33c9f6ee&req=diAiFcx8nYVWXPMW3nq%2BgWkY%2Bhr4ofjYjZI8o%2F32JJsrruLYLdxhys%2B11Os5%0Acftpmn%2FUw5fY72gFRGr7cdaDaOs%3D%0A)

Também é possível criar uma **aba** utilizando essa mesma condição. Para isso, acesse a tela de **Clientes**, clique em **Nova aba** e configure os mesmos critérios utilizados no filtro.

## Como utilizar em uma automação?

Você pode configurar uma automação que será executada de forma periódica para enviar um e-mail de felicitação aos seus clientes na data de aniversário.

**⚠️ Importante:** para realizar esse passo, é necessário ter contratado o **Módulo de Automações**. Caso ainda não tenha, entre em contato com o **Suporte** ou com a sua **Gerente de Contas** para obter mais informações.

- Acesse **Administração** > **Automações;**
- Selecione **Cliente** > **Nova automação;**
- Defina o nome da automação;
- Em **Gatilho**, selecione **Periodicamente**;
- Configure para executar **todos os dias**, no horário de sua preferência;

[GIF animado: Imagem 3: Configure para executar todos os dias , no horário de sua preferência;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2053630006/0cf20266a5979bd34c53c3c1ea3b/enviarEmail.gif?expires=1786536000&signature=85c65f11a65b427e6e8358c93c0acff66bb499555d6fecf9445ad26938496410&req=diAiFc99nYFfX%2FMW3nq%2BgegMG9qeX6bHLqYQCrgKgnAQ0JCohtlNXmHnqltW%0A5%2FKzWgIV5r7jWjR87WnzN3EkHV8%3D%0A)

- Adicione o seguinte filtro:

  - **Próximo aniversário** > **Igual a** > **Data Relativa** > **Hoje;**
- Na ação da automação, selecione **Enviar e-mail;**
- Como destinatário, escolha o campo **E-mail** do Cliente;
- Defina o **Assunto** e o **conteúdo** da mensagem;
- Clique em **Salvar** para finalizar a configuração.

[GIF animado: Imagem 4: Clique em Salvar para finalizar a configuração.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2053730820/62701f7f3973629e8f63951ce415/enviarEmail2.gif?expires=1786536000&signature=e827f27375971e321e594878bc5be8e681a0ebb52e4e878eab6404e77550147a&req=diAiFc59nYldWfMW3nq%2BgeWCQnsLrKB1HUkG%2Fm9%2F7IQmDJV%2FeCkoT%2B%2BWylid%0AodbA6Tb4fQrf1q2Hs6ejxuUCLx4%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
