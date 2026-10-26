---
id: "42427484628887"
titulo: "Caso de uso - Limpeza de clientes duplicados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427484628887-Caso-de-uso-Limpeza-de-clientes-duplicados"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-11T16:14:46Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7950340", "sync_hash_9ad036b76699"]
---

# Caso de uso - Limpeza de clientes duplicados

Quando houver duplicidade de cadastros, eles podem ser identificados exportando os dados e utilizando uma planilha do Excel para buscar informações repetidas com base em um campo específico do formulário.

## Como exportar os dados?

- Acesse a tela de **Clientes**;
- Clique na **engrenagem** no lado direito da listagem e mantenha visíveis apenas as colunas **Nome**, **CNPJ** e **ID**;
- Em seguida, clique em **Ações da aba > Exportar aba**.

![Imagem 1: Em seguida, clique em Ações da aba > Exportar aba .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2071684629/a52950d540a37fcce10b8c54cabc/image.png?expires=1786536000&signature=a92333bb8f36381a199c0a7a9057039286d1af8cb07cfbb19bd2e33a73df5897&req=diAgF892mYddUPMW3nq%2BgbadnClYw5KpY6OXMlb5g7EQnBPz%2FxMeihkoGlKP%0AK89y3uylAeov274Km077NSySFXw%3D%0A)

Após exportar a aba, acesse a planilha. À direita da planilha, crie uma nova coluna chamada **Marcadores** e preencha com **“Duplicado”** todas as linhas que correspondam a registros identificados como duplicados.

⚠️ **Importante:** mantenha um dos cadastros **sem** o marcador. Esse será o registro que permanecerá na base e **não deverá ser excluído**.

![Imagem 2: ⚠️ Importante: mantenha um dos cadastros sem o marcador. Esse será o registro que permanecerá na base e não deverá ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2071766230/e6c8c4f61d2f58676abc8f4b2ab6/image.png?expires=1786536000&signature=ff5a3c5811c3ba3a3aa448c709c15951d0d84a17cc8a9acfcdd84592e01cdf13&req=diAgF854m4NcWfMW3nq%2BgT0blPxjbiyHD5H%2B1spysoBnHm0KS0%2FHGo0JGF%2BA%0AnmnBA%2BJJpoKsTVzCioALmDpQuaA%3D%0A)

## Como importar os dados?

Após salvar a planilha, realize a importação dos registros, mapeando os campos **Nome**, **CNPJ**, **Marcadores** e **ID**.

Durante o processo, configure a **detecção de duplicidade pelo campo ID**, garantindo que os marcadores sejam atualizados corretamente nos registros já existentes.

[GIF animado: Imagem 3: Durante o processo, configure a detecção de duplicidade pelo campo ID , garantindo que os marcadores sejam atualizados…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2071771715/186faf1acbef6c22a1f1bcdca51d/importar.gif?expires=1786536000&signature=38b293b92e1f75e0811d3443c5bc1e4ccae0861cbba804615c4d275098e63371&req=diAgF855nIZeXPMW3nq%2BgY2OXpB9Hopf00gVjfPLColDVibx965NyJR6y%2FpK%0AK2r6QIWW1%2B4wvyRjJ9FC%2FZk6j5o%3D%0A)

## Como realizar a limpeza?

Após concluir a importação, crie uma aba para visualizar apenas os clientes marcados como duplicados:

- Acesse a tela de **Clientes** e clique em **Nova aba**;
- Defina o **título** da aba e quem poderá visualizá-la;
- Configure o filtro:

  - **Marcadores** > **Igual a** > **Duplicado**;
- Clique em **Salvar**.

![Imagem 4: Clique em Salvar .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2071787415/b0d827b3353b0c211d4e20b0d17d/image.png?expires=1786536000&signature=d8a3257f161d9c2b7d177049027b0cb51a9b7b7431e8f32fcd14fb0f21124532&req=diAgF852moVeXPMW3nq%2BgbtbOuYqzJamt1DjlnixQsm6IPjBMwUAePLd5q4X%0AH8OlD9s%2FTFpSwqQuhwcN9U3Gh7g%3D%0A)

Caso os registros duplicados estejam **sem movimentação** (sem negócios, atividades ou vínculos), você pode utilizar a **edição em massa** nessa aba para realizar a exclusão dos clientes duplicados.

⚠️ **Atenção:** A edição em massa é **irreversível**. Antes de confirmar a ação, verifique cuidadosamente se realmente deseja excluir todos os itens da aba.

- Clique em **Ações da aba > Edição em massa**;
- Selecione a opção **Excluir itens**;
- Digite a palavra solicitada para confirmação e finalize a exclusão.

[GIF animado: Imagem 5: Digite a palavra solicitada para confirmação e finalize a exclusão.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2078151671/0acd81eaed721bac06f7acae4c27/exlcuir.gif?expires=1786536000&signature=5a785b2c8587c4b0d65817b530d8991a713c60049421592df803196509b6ebff&req=diAgHsh7nIdYWPMW3nq%2BgYt%2BjD4yVXJPrMdbJbWNMOnrc8RTU1A5mvoiqUxW%0AAfD9mqYfwN3r%2FXVStb6RhwRG0jI%3D%0A)

## Como transferir dados de duplicatas?

Na aba de **Duplicados**, acesse cada cliente identificado para verificar se há **negócios** ou **pessoas** vinculados que precisam ser transferidos antes da exclusão.

Para transferir negócios**:**

- Acesse a tela do cliente duplicado;
- Clique na aba **Negócios**;
- Na coluna **Cliente**, altere para o cliente correto que deverá manter o vínculo.

[GIF animado: Imagem 6: Na coluna Cliente , altere para o cliente correto que deverá manter o vínculo.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323420/0c9a9489a4f7d079e356095b/limpar_clientes_negocios.gif?expires=1786536000&signature=46418a38eb1c7690824df8cbdf85795caa34cbceb51ca3f2ed9fabfa09262a88&req=dyYuFct9mYNfFb4V1XW4gUals2QJA%2BksSmx1WVGjbxfVZ3yP%2BuLJ1sFL%2FK48%0AZ8LcZZsKHzfOdMumpcdYCkEy8Q%3D%3D%0A)

Para transferir pessoas:

- Acesse a tela do cliente duplicado;
- Clique na aba **Pessoas**;
- Na coluna **Empresa**, altere para a empresa correta que deverá manter o vínculo.

[GIF animado: Imagem 7: Na coluna Empresa , altere para a empresa correta que deverá manter o vínculo.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323429/463ce5ab67337c7eff528a8c/limpar_clientes_pessoas_xx.gif?expires=1786536000&signature=e616a582f4810bf33e6064cfcf15eb60434cc7a85d0c8e1bede959dd3779c01b&req=dyYuFct9mYNWFb4V1XW4gceMirHychohHbT9jiaAB4lJiE2idkKetuYimKkU%0ALH8XfXhfkrEpbBiCYfATMQhoMg%3D%3D%0A)

Caso alguma coluna não esteja visível, clique no ícone de **engrenagem** ao final da listagem de colunas e adicione a coluna desejada.

Após concluir a transferência dos vínculos, acesse **Opções** e selecione **Excluir cliente** para remover o cadastro duplicado.

[GIF animado: Imagem 8: Após concluir a transferência dos vínculos, acesse Opções e selecione Excluir cliente para remover o cadastro duplicado.](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369323436/5059bc6fdf76ac51777eef8a/limpar_clientes_xx.gif?expires=1786536000&signature=952bdf5c085d4118b0c8b22e2a31d8214d54a75441cb69f86e6dd3430854986e&req=dyYuFct9mYJZFb4V1XW4gTn4rzlm3xLxSSqnOkd2r3UFdd7TK2aJYa3uOdwx%0AfckXrK3zAE%2FRUsU6klRKsW%2Brfg%3D%3D%0A)

## Como evitar duplicidade nos cadastros?

Para evitar duplicidade de cadastros, é possível definir determinados campos como **Campo chave**. A função do **Campo chave** é identificar informações já existentes na base.

Assim, ao tentar cadastrar um cliente com um dado que já esteja registrado nesse campo, o sistema exibirá um erro no formulário, impedindo a criação de um cadastro duplicado.

💡 **Dica**: para entender sobre erros no formulário, [acesse este artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427634719255).

Siga os passos abaixo para definir um campo como **Campo chave**:

- Acesse **Administração > Campos e formulários**;
- Selecione a entidade **Cliente** e escolha o formulário desejado (**Empresas** ou **Pessoas**);
- Edite o campo que deseja definir como chave;
- Ative a opção **Campo chave**;
- Clique em **Salvar** e **Salvar formulário**.

[GIF animado: Imagem 9: Clique em Salvar e Salvar formulário .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2071395364/e0b46045c6998b6d542ceca2f750/campo.gif?expires=1786536000&signature=1eff5a85a4a5272a7471be7901159449e79bc27497c2bc84d31a26dcd725e86d&req=diAgF8p3mIJZXfMW3nq%2BgRua5mX9gFS%2FgSAhSpfbY9NuAVGmBDsnTJ0gSIo9%0AM8fSkvzMrkItvroxjqq3q%2FpCFYQ%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
