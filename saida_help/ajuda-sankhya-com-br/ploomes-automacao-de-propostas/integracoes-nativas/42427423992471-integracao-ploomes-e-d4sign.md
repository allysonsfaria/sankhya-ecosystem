---
id: "42427423992471"
titulo: "Integração Ploomes e D4Sign"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427423992471-Integra%C3%A7%C3%A3o-Ploomes-e-D4Sign"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:00:11Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11636656", "sync_hash_51a7bd27a080"]
---

# Integração Ploomes e D4Sign

Este artigo detalha o processo de ativação e configuração da integração entre o Ploomes e a D4Sign para centralizar o envio de assinaturas pelo Ploomes.

## 1) Sobre a D4Sign

A **D4Sign** é uma plataforma de assinatura eletrônica e digital do Brasil. Ela permite a formalização de documentos com total segurança, integridade e validade jurídica, utilizando diversos pontos de autenticação para identificar os signatários.

## 2) Objetivos da Integração

A conexão com o D4sign permite que os usuários do Ploomes realizem assinaturas digitais diretamente pela plataforma, utilizando as funcionalidades da D4Sign para envio, autenticação, rastreamento e armazenamento de documentos assinados.

Essa funcionalidade atende clientes que já utilizam a D4Sign ou que desejam uma opção robusta de assinatura digital, proporcionando centralização dos processos, segurança e ganho de produtividade. A integração também fortalece o portfólio do Ploomes, contribuindo para atrair e manter clientes que demandam esse tipo de solução.

## 2) Pré-requisitos

- Ter uma conta ativa na D4Sign, em qualquer um dos planos disponíveis.
- O Ploomes não aceita contas do tipo Sandbox, pois os documentos assinados por esse tipo de conta não possuem validade jurídica.
- Acesso ao Token de acesso à API e da Chave de Criptografia fornecidos pela D4Sign.

## 3) Ativando a Integração com D4Sign

## 3.1) Ativação da Integração

Para ativar a integração:

1. Na tela inicial do Ploomes, vá em "**Administração" > "Integrações plug-and-play"**.

   ![Imagem 1: Na tela inicial do Ploomes, vá em " Administração" > "Integrações plug-and-play" .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581394664/89eb8bd2226ef6b2d3d94ae42bf2/image.png?expires=1786536000&signature=a024d92f955711cb693af41f55796a7a60959181d9bd2c0974964f91cb35fbab&req=dSUvF8p3mYdZXfMW3nq%2BgVdKMj8vxpT4QYibOjap73ZQlJhDV2cxJt0uu7s8%0A2QKSmlDLL22h5vzms8teMo%2B34%2B4%3D%0A)
2. Localize e clique sobre **“D4Sign”**.
3. Clique em **“Habilitar integração”**.
4. Em seguida, clique em **“Autorizar Integração”**.
5. Uma nova janela será aberta para realizar a autenticação com sua conta D4Sign.
6. Preencha com:

   - **Token da API**
   - **Chave de Criptografia**

![Imagem 2: Chave de Criptografia](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581395650/56cb4fbb3dbb577765c7e4904dc1/image+%281%29.png?expires=1786536000&signature=7c656b1e739f173a56657cb7101fb534b760ed0b998d5300167fe9dc16edcb24&req=dSUvF8p3mIdaWfMW3nq%2BgSDP6UXjx9hZjGGOiwKRmxvqB6Ig8m6g9v07bdji%0Ap3WrF%2BuGdoNTI86qxTPCqDnjS%2FI%3D%0A)

Esses dados podem ser obtidos na D4Sign acessando:

**"Configurações da Conta" > "</> Dev (API)" > "Meus dados da API"**

- Caso você não encontre essa opção na sua conta D4Sign, contatar o suporte da D4Sign para que eles possam direcionar a demanda e te ajudarem a acessar o seu **Token API** e sua chave criptografada

![Imagem 3: Caso você não encontre essa opção na sua conta D4Sign, contatar o suporte da D4Sign para que eles possam direcionar a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581398340/d628db52ef4ea7ca0ba1da49045d/image+%283%29.png?expires=1786536000&signature=8d2601ab38ef20ab9b7fd69ff10df17a30c842e0e80d88eceb0f8cea93ae314d&req=dSUvF8p3lYJbWfMW3nq%2BgQFhOVOE7I3NqJc85oroDwyZ5tR2fjlvbQ93VwaP%0A8efflhKM1fqk%2BB%2FIzpAOXXT05bc%3D%0A)

Após autenticar a integração com a D4Sign, você poderá definir os comportamentos padrão que serão aplicados sempre que um documento for enviado para assinatura. Essas configurações ajudam a garantir organização e praticidade no uso da ferramenta.

## 3.2) Configuração de cofres e pastas

- **Cofre padrão**: obrigatório para o funcionamento da integração. É o local onde os documentos assinados serão armazenados dentro da D4Sign.
  Você pode escolher entre os cofres existentes em sua conta da D4Sign, que são sincronizados automaticamente após a autenticação.
- **Pasta padrão** (opcional): caso queira, você pode vincular uma pasta específica dentro do cofre selecionado. Isso permite manter os documentos organizados por categoria, tipo ou cliente, por exemplo.

## 3.3) Outras configurações disponíveis

- **Mensagem personalizada para os signatários**:
  Defina um texto que será exibido no corpo do e-mail enviado pela D4Sign ao signatário. Essa mensagem pode incluir orientações sobre o conteúdo do documento ou instruções específicas sobre a assinatura.

  **Importante**: atualmente **não** é possível personalizar o assunto do e-mail enviado pela D4Sign.

- **Importação automática para o Ploomes**:
  Você pode ativar a opção **“Deseja importar os documentos para o Ploomes após eles serem assinados?”**

  - Se ativado, o documento assinado será anexado automaticamente no cliente, no card ou em ambos, conforme o tipo de documento:

    - **Propostas**: anexo no card e no cliente (se houver).
    - **Vendas**: anexo no cliente e no card (se houver).
    - **Documentos de cliente**: anexo na página do cliente.
    - **Documentos de card**: anexo no card e no cliente (se houver).

![Imagem 4: Documentos de card : anexo no card e no cliente (se houver).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581400518/a2eaad2196fcbff826d016c9fb9b/image+%285%29.png?expires=1786536000&signature=a71f565a2e5d82c5f19c50ae61e9e6a3e8b6e3c0b9aec6b9621045f09c300e68&req=dSUvF81%2BnYReUfMW3nq%2BgZT%2BCyRRBleAiT2H8OBP1z4pGM%2FJFaQGYzG8Ksvx%0AL1FEaX53b9qn7qK2uLXgw8R1Gqw%3D%0A)

## 4) Utilizando a Integração com D4Sign

## 4.1) Configuração do Modelo de Documento

### Como configurar âncoras de assinatura digital com D4Sign no Ploomes

Após ativar a integração com a D4Sign no Ploomes, é possível configurar os modelos de documento para definir o posicionamento da assinatura digital. Essa etapa **não é obrigatória para o funcionamento da integração,** ou seja, a assinatura digital tem validade jurídica mesmo sem o posicionamento no documento, mas pode ser feita caso você deseje controlar visualmente onde a assinatura será aplicada.

#### Passo a passo para configurar:

1. **Acesse seus modelos de documento**

   No menu **Administração**, clique em **Modelos de documento** e abra o modelo que deseja configurar (proposta, documento de venda ou qualquer outro tipo criado no Ploomes).
2. **Defina o local da assinatura**

   Escolha o ponto do documento onde deseja que a assinatura apareça. Uma boa prática é criar um espaço sublinhado e adicionar uma indicação do assinante, como neste exemplo:

   ![Imagem 5: Escolha o ponto do documento onde deseja que a assinatura apareça. Uma boa prática é criar um espaço sublinhado e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581401493/32e52215600dc11ce7deb05db9fb/image+%286%29.png?expires=1786536000&signature=63ed865595848f8c13a7ef940d400ca759c03ac3ddd777bdc5abe039df4960b1&req=dSUvF81%2BnIVWWvMW3nq%2BgUAjtmC5xL1lnIXhr0xfOFKyvFLrx8WZOfZzraUl%0ASofDbtTOIfzpYi%2B%2BZN%2BBv7jtpCY%3D%0A)
3. **Crie os campos de assinatura digital:**

   Vá até o menu **Campos >** Clique em **Proposta** (ou outro tipo correspondente ao modelo) > Selecione **Criar Campo**

   ![Imagem 6: Vá até o menu Campos > Clique em Proposta (ou outro tipo correspondente ao modelo) > Selecione Criar Campo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581401905/648868ff0c613199874ca6ed8193/image+%287%29.png?expires=1786536000&signature=2a9c8e72d9b62cfdc9889e8ce35142f5e46866e7786a0f7202294cdccd1353b4&req=dSUvF81%2BnIhfXPMW3nq%2BgfOGeaTbF8UzGf7VvkQDGQ%2BlVjM2y%2BNIpvSSbNUU%0AjaxsrdYLivEmb84GGLWdN1gWiDU%3D%0A)

   No menu lateral, escolha o tipo de campo **Assinatura D4Sign e** preencha o campo **Título do Campo** com um nome identificável, sem espaços (ex: `Contratante1`, `Contratada1`).

   O campo “**Valor padrão**” será preenchido automaticamente e após isso clique em **Salvar**

   ![Imagem 7: O campo “ Valor padrão ” será preenchido automaticamente e após isso clique em Salvar](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581402303/ac87c6539416e99aa7d9eeffed64/image+%288%29.png?expires=1786536000&signature=a93a8d51ae27bbb31587c1b1aaf06f5ba88772d557513a568ae848e5a708681d&req=dSUvF81%2Bn4JfWvMW3nq%2Bgcx6IdBJKMeRHTT9mFX1iGmWeDQICVNttRngxj%2FQ%0Aa0kCFWY1XjCHjgHUr1J2vNHwkeI%3D%0A)
4. **Crie campos para todas as assinaturas necessárias**

   Caso o documento precise de mais de uma assinatura, repita o processo criando novos campos com nomes diferentes (ex: `Contratante2`, `Contratada2`).
5. **Insira os campos no documento**

   Posicione cada campo criado no local correspondente da assinatura.

   ![Imagem 8: Posicione cada campo criado no local correspondente da assinatura.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581402774/efa610b49150f583d9c9d52ac43c/image+%289%29.png?expires=1786536000&signature=7e9ae4066be0a15472d28c64ed67fde586efec093c64ab2fc4f4885fca4502fb&req=dSUvF81%2Bn4ZYXfMW3nq%2Bgcwk9Bf8LEP0ysxNNv4w%2FOi7K%2Fh%2BMEr2JK%2FNwB9i%0AEjgdvexMmN41Ljg8p0w%2BOQzLxPQ%3D%0A)

   Em seguida, altere a **cor da fonte do campo** para a mesma cor do fundo do documento. Isso evita que o nome do campo fique visível na versão final assinada.

   **Importante:** Na integração com a D4Sign, a opção **“esconder campo**” ou marcar o campo como “**ocultar por padrão**” não funciona. Por isso, é essencial mudar a cor da fonte para ocultar o texto visualmente.

   ![Imagem 9: Importante: Na integração com a D4Sign, a opção “esconder campo ” ou marcar o campo como “ ocultar por padrão ” não…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581403280/fe289e3857454c00d25982d41983/image+%2810%29.png?expires=1786536000&signature=3c96ad5f46a0ca141b7d6ff322ee85f37810c14a4dd6cead81306875082a6df1&req=dSUvF81%2BnoNXWfMW3nq%2BgQKX2Gton1%2B3WIplvX1O%2BTip8U1eI%2FEl6DvUknz4%0AlW69MYpnimP8FyBtKx%2FXQsmkr98%3D%0A)
6. **Salve o modelo**

   Após finalizar as configurações, clique em **Salvar** no canto superior direito da tela.

Pronto! O modelo estará configurado para exibir as assinaturas digitais nos locais definidos ao ser enviado via D4Sign.

## 4.2) Envio de Documentos

Após gerar uma proposta, documento ou venda pelo Ploomes, clique em **Compartilhar** > selecione **D4Sign**.

Os campos de **cofre** e **pasta** são preenchidos automaticamente com os valores definidos na configuração e **não podem ser alterados** pela tela de envio (apenas pela tela de configuração).

Com o documento gerado, ao clicar no botão **“Compartilhar”** no canto superior direito da tela, será exibida a opção de compartilhamento via D4Sign.

[GIF animado: Imagem 10: Com o documento gerado, ao clicar no botão “Compartilhar” no canto superior direito da tela, será exibida a opção de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581404690/b22182c36f1cb12ed6d9c3fd62ee/compartilharproposta+%281%29.gif?expires=1786536000&signature=533216ac745c81f6cf252ba69f4ce52a9d2c119606c89bf21f7ba4dcf0151fef&req=dSUvF81%2BmYdWWfMW3nq%2BgUoqLsy9Em96Ex7Cd4U6g6eQAJ8rT6d1lsVZXLWI%0ARbLOCwA0H9I0yl5mpuccqb19xNs%3D%0A)

Nessa etapa, você poderá configurar suas preferências e necessidades no envio de assinatura. No primeiro campo, selecione o **Tipo de Assinatura** (consulte a lista completa de tipos de assinatura).

Em seguida, defina a **Via de Envio** (veja as opções disponíveis na lista de vias), o **Tipo de Autenticação** (veja as opções na lista de tipos de autenticação) e, se configurado, a **Âncora,** o campo de assinatura que cada destinatário deverá preencher.

Finalize adicionando o contato do signatário e clicando em “Adicionar”.

![Imagem 11: Finalize adicionando o contato do signatário e clicando em “Adicionar”.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581405043/8583d86bf7ff38f5cb5c483afc89/image+%2811%29.png?expires=1786536000&signature=876d7825df719383f47289e2ff4017c7fa4484e927d5482fb916ba8fa27d935e&req=dSUvF81%2BmIFbWvMW3nq%2BgUXjizGVecGfvoP9JuYYJLMJcR6EFEyMm5MTqt0w%0ApZE0ELtNMKzqAynnuoZtXNe0O5Y%3D%0A)

### Campos disponíveis no envio:

- **Tipo de assinatura**

  **Lista completa de assinaturas disponíveis no campo**

  - Assinar
  - Aprovar
  - Reconhecer
  - Assinar como parte
  - Assinar como testemunha
  - Assinar como interveniente
  - Acusar recebimento
  - Assinar como Emissor, Endossante e Avalista
  - Assinar como Emissor, Endossante, Avalista e Fiador
  - Assinar como fiador
  - Assinar como parte e fiador
  - Assinar como responsável solidário
  - Assinar como parte e responsável solidário
  - Assinar como fiel depositário
  - Assinar como avalista
  - Assinar como Anuente
  - Assinar como Interveniente Garantidor
  - Assinar como Parte e Avalista
  - Assinar como Parte, Avalista e Interveniente Garantidor
  - Assinar como Parte e Fiador
  - Assinar como Parte e Fiel Depositário
  - Assinar como Parte e Interveniente Garantidor
  - Assinar como Fiduciante
  - Assinar como parte e fiduciante
  - Assinar como devedor da cédula de crédito bancário
  - Assinar como Credor de Cédula de crédito bancário

![Imagem 12: Assinar como Credor de Cédula de crédito bancário](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581406776/45e5faf49a372efe2170228ef35b/image+%2815%29.png?expires=1786536000&signature=a8675a56fa4baeaaf3d0a74e5b16efcec9674a41526470b3ffb63f5aeb2d4b70&req=dSUvF81%2Bm4ZYX%2FMW3nq%2Bga8UhU7dsvb9ggHej3AYgaph4tBPyMRo%2FimvwfmD%0AdOU2FKxlJ491lxkRmlUMb14F3CA%3D%0A)

- **Via de envio**:

  - **E-mail**: preenchimento manual com sugestões automáticas baseadas nos contatos do Ploomes.
  - **WhatsApp**: exige telefone do contato (preenchido automaticamente, se disponível).

![Imagem 13: WhatsApp : exige telefone do contato (preenchido automaticamente, se disponível).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581407877/10edcad0becd4c6f04de4dedefa5/image+%2816%29.png?expires=1786536000&signature=3756a956fae7503f70c054df84aa2af50d4f76076e70570f25d0a214324fafec&req=dSUvF81%2BmolYXvMW3nq%2BgdvOwJl%2FYCDClzB1CErD7px7RrbMSOenYbcN7ujb%0AomsnGOYncdhdaF%2BUgKrh2go6bMQ%3D%0A)

- **Tipo de autenticação**:

  - Sem autenticação (padrão)
  - Exigir código
  - Exigir token SMS
  - Exigir token whatsapp
  - Exigir autenticação PIX
  - Exigir documento com foto
  - Exigir documento com foto + selfie
  - Exigir autenticação por vídeo selfie
  - Exigir certificado digital ICP-Brasil

**Observação:** Os recursos de autenticação via **token SMS** e **token WhatsApp** são oferecidos pela D4Sign e **devem ser contratados separadamente**.

Para utilizá-los no processo de assinatura, é necessário:

- Entrar em contato diretamente com a equipe da D4Sign
- Solicitar a contratação dos pacotes específicos de envio de token por SMS e/ou WhatsApp

![Imagem 14: Solicitar a contratação dos pacotes específicos de envio de token por SMS e/ou WhatsApp](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581407936/f2d9c95ac8734f4bb883797709e0/image+%2817%29.png?expires=1786536000&signature=65d5729e4607bc0e28bf5dc2439166c66d6baed85ce290a9a67ed7be2059c29d&req=dSUvF81%2BmohcX%2FMW3nq%2BgaHUO7TTXkLRSBtU4j19MmCfqUDmgcK2pLbTTrja%0AAiWKbKo%2BZqf63wsV3Nv6sajmVRo%3D%0A)

- **Âncoras de assinatura** (caso estejam configuradas no modelo de documento):

  - Serão aplicadas conforme a estrutura definida no modelo. Para saber como configurar, [consulte o Item 2 "**Configuração do Modelo de Documento**"](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427423992471-Integra%C3%A7%C3%A3o-Ploomes-e-D4Sign#h_e1c9ae72a7) desse artigo.

![Imagem 15: Serão aplicadas conforme a estrutura definida no modelo. Para saber como configurar, consulte o Item 2 " Configuração…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581413214/f04b21d8ca7e1d9fc89fd77733c7/image+%2818%29.png?expires=1786536000&signature=b5b9023d4fc4b656bb12a51c85a8b330d294a53b2bbdd674d275c6eadbc78008&req=dSUvF81%2FnoNeXfMW3nq%2Bgc7nFzm5%2Bgfd%2FueId87fsIKZm359OVX2o9wUKXKF%0AGW%2BD29hezJC1pi3bKz0wX6bFnNQ%3D%0A)

## 4.3) Ordenação de Assinaturas

Por padrão, os signatários recebem o documento ao mesmo tempo, em um fluxo de **envio paralelo**. Isso significa que todos podem assinar assim que o documento for enviado.

Se for necessário que o documento seja assinado em uma ordem específica — por exemplo, primeiro pela contratante, depois pela contratada — você pode configurar o **envio sequencial**. Para isso:

- Ative a opção **"Quero que as assinaturas sejam realizadas na ordem configurada acima"** na tela de envio do documento.
- Em seguida, organize a ordem dos signatários clicando e arrastando cada um deles para a posição desejada na lista.
- A numeração da ordem de assinatura será ajustada automaticamente conforme a posição definida.

Essa funcionalidade garante que o próximo signatário só receba o documento depois que o anterior tiver finalizado sua assinatura, respeitando a sequência definida.

[GIF animado: Imagem 16: Essa funcionalidade garante que o próximo signatário só receba o documento depois que o anterior tiver finalizado sua…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581413576/d52da3f7a0a6305e7361f78f854b/gifd4signsuporte+%281%29.gif?expires=1786536000&signature=ffd12efb9bdf17d86a316205d3c81daeb2a416cc21dc860246fb56ddd5dcb038&req=dSUvF81%2FnoRYX%2FMW3nq%2BgcMPIzmBck9ReZ4xyJ5MzytLSL4dVetpVp1GmlNf%0AGIcYY0JZQoV4SPWgCAeC%2BcydPvw%3D%0A)

**Importante:**

- Não é possível editar a ordem digitando manualmente os números. A posição de cada signatário deve ser ajustada com o movimento de arrastar para cima ou para baixo.
- Após o início do processo de assinatura, a ordem configurada não pode mais ser alterada.
- Caso um novo signatário seja adicionado após o envio, ele será posicionado automaticamente **após o último da lista atual**, respeitando a sequência já definida.

---

## 4.4) Acompanhamento da Assinatura

- Após o envio do documento para assinatura pela D4Sign, o acompanhamento do status pode ser feito de duas formas:

  #### Visualização rápida no documento

  A indicação **“Assinatura por D4Sign ligada”** será exibida no canto superior direito do documento compartilhado.

  Ao clicar nesse botão, será aberta uma tela com o **painel de acompanhamento da D4Sign**, que mostra:

  - A lista dos signatários configurados;
  - Um **check verde** ao lado do nome de cada pessoa que já concluiu sua parte do processo;
  - Usuários **sem o check verde** ao lado do nome que estão com pendências para a finalização do documento.

[GIF animado: Imagem 17: Usuários sem o check verde ao lado do nome que estão com pendências para a finalização do documento.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581418607/e52a64ad154d81a7a57ccdfb94bc/gifassinado.gif?expires=1786536000&signature=1c98d32a9dccb2e2c94fc22119e385f46654ae19a99a0a0a8b6492a0a2b6cbc4&req=dSUvF81%2FlYdfXvMW3nq%2BgV9FVEyItCRZ7QXhib8riMRIx9NcoWR0Jbo4tam5%0AqvWFdH%2F15KDJmQslWp46H5vO6%2Bc%3D%0A)

## 4.5) Ações Pós-Envio

- Após o envio de um documento para assinatura pela D4Sign, algumas ações continuam disponíveis enquanto o fluxo de assinatura estiver em andamento:

  - **Adicionar signatários** – Permitido enquanto houver signatários pendentes.
  - **Editar ou remover signatários** – Permitido apenas para os signatários que ainda não assinaram.
  - **Reenviar documento** – Possível para signatários que ainda não concluíram a assinatura.
  - **Cancelar assinatura** – Permitido enquanto o fluxo de assinatura ainda não tiver sido finalizado.

## 4.6) Quando a assinatura é concluída

- O botão de acompanhamento muda para **“Assinatura D4Sign realizada”**.
- Todos os nomes dos signatários aparecem com **check verde**, e o status geral indica que o documento foi **finalizado** com sucesso.

  ![Imagem 18: Todos os nomes dos signatários aparecem com check verde , e o status geral indica que o documento foi finalizado com…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581422346/b4e54c57d024d2144617294fb2b0/image+%2819%29.png?expires=1786536000&signature=6c0768d076023ecda89e3a9cb7e9fc665101e9a130c14024a1855b6ea6edac71&req=dSUvF818n4JbX%2FMW3nq%2BgQ8lJXwUuTndHQXQNdXQdxfR83yu0CdgxU5%2F%2BsyQ%0AQCgctFUwNmF7R4aXZFrl5wAMsoo%3D%0A)
- Se, na configuração da integração, estiver marcada a opção para **importar os documentos assinados**, o PDF assinado será automaticamente salvo nos **Anexos**:

  - Do **cliente vinculado** à proposta, venda ou documento;
  - E do **negócio vinculado**.

![Imagem 19: E do negócio vinculado .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1581428436/f96a13eaf357d59b0335f3c10230/image+%2820%29.png?expires=1786536000&signature=ae93c45e9a2870eb565ec6bdbc2f9120e5ac3355bfa89fd1634c021efc704b00&req=dSUvF818lYVcX%2FMW3nq%2BgWZdmLqwWmz2AdO5u4PbIIbW4wQOWlCL71T6JWvv%0ARH5825iahryKCPCKaSoNQP7995c%3D%0A)

#### Campo de "Assinado (D4Sign) no Ploomes

- Um campo chamado **“Assinado (D4Sign)”** é criado automaticamente no Ploomes.
- Ele será preenchido com **“Sim”** assim que todas as assinaturas forem finalizadas.
- Esse campo pode ser usado em **filtros**, **automações** e **relatórios** para facilitar o acompanhamento e a execução de ações pós-assinatura.

## 4.7) Campos da Integração

Ao habilitar a integração com a D4Sign, alguns campos personalizados são criados automaticamente no Ploomes. Esses campos permitem acompanhar o status de envio e assinatura dos documentos, além de registrar as configurações utilizadas.

#### Campos de envio e rastreamento

#### Esses campos indicam se o item foi enviado para a D4Sign e armazenam os respectivos identificadores gerados pela plataforma:

- **Venda enviada (D4Sign)** – Indica se a venda foi enviada para assinatura via D4Sign.
- **Proposta enviada (D4Sign)** – Indica se a proposta foi enviada para assinatura via D4Sign.
- **Documento enviado (D4Sign)** – Indica se o documento foi enviado para assinatura via D4Sign.
- **ID de venda (D4Sign)** – Armazena o identificador da venda na D4Sign.
- **ID de proposta (D4Sign)** – Armazena o identificador da proposta na D4Sign.
- **ID do documento (D4Sign)** – Armazena o identificador do documento na D4Sign.

#### Campos de configuração

#### Esses campos registram as opções configuradas no momento do envio do documento:

- **ID do Cofre (D4Sign)** – Indica o cofre utilizado no envio do documento.
- **ID da Pasta (D4Sign)** – Indica a pasta utilizada no envio do documento.
- **Enviado em ordem de assinatura (D4Sign)** – Campo do tipo "Sim/Não" que informa se o documento foi enviado com a opção de ordem de assinatura ativada.
- **Assinado (D4Sign)** – Campo do tipo "Sim/Não" que será preenchido automaticamente com "Sim" quando todas as assinaturas forem concluídas.

Esses campos podem ser utilizados em filtros, automações e relatórios para facilitar o controle e o acompanhamento do processo de assinatura eletrônica.

## 5) Limitações da Integração com D4Sign

#### Funcionalidades não disponíveis nesta versão

Alguns recursos oferecidos pela D4Sign não estão disponíveis nessa versão da integração com o Ploomes.

- #### Grupos de assinatura

  - Não é possível configurar grupos de assinatura, onde mais de uma pessoa é elegível para assinar, mas apenas uma precisa concluir a assinatura.
    Esse tipo de configuração pode ser útil para equipes maiores, mas no momento a integração trabalha com signatários definidos individualmente.
- #### Reordenação alterada pelo número na ordem de assinatura

  - A ordenação dos signatários pode ser feita diretamente pela interface, por meio da funcionalidade de **arrastar e soltar**.
    A edição da ordem por número manual (por exemplo, digitar “2” para mover um signatário para a segunda posição) não está disponível nesta versão.
- #### Observadores e destinatários em cópia

  - A opção de adicionar pessoas para receberem uma cópia do documento após a assinatura, sem necessidade de assiná-lo, não está habilitada nessa versão da integração.
- #### Múltiplas autenticações combinadas

  - A D4Sign permite configurar mais de um método de autenticação ao mesmo tempo (como token SMS + código por e-mail).
    Na integração atual, é possível escolher apenas **um tipo de autenticação por signatário**.
- #### Navegação por subpastas

  - Todas as pastas, junto das subpastas da conta D4Sign são exibidas como uma lista simples durante a configuração.
    A navegação por níveis hierárquicos das subpastas não está disponível.

---

## F.A.Q (Perguntas Frequentes)

- #### Como ativo a integração?

  Acesse **Administração > Integrações plug-and-play**, clique em **D4Sign** e siga as etapas de autenticação com os dados fornecidos pela D4Sign.

- #### Posso alterar o cofre ou a pasta no momento do envio?

  Não. O cofre e a pasta são definidos na tela de configuração da integração e utilizados automaticamente nos envios.

- #### É possível reordenar os signatários?

  Sim. A reordenação pode ser feita apenas por **arraste** (drag & drop) na interface. Não é possível editar a ordem digitando números manualmente.
- #### Como posiciono a assinatura no documento?

  Utilize o campo **“Assinatura D4Sign”** no modelo de proposta ou documento. Posicione o campo onde desejar e defina a cor da fonte como branca para que o texto não apareça visualmente.

- #### Quais tipos de autenticação estão disponíveis?

  Todos os métodos oferecidos pela D4Sign estão disponíveis. Autenticação por **Pix, SMS ou WhatsApp** exige contratação adicional diretamente com a D4Sign.

- #### O que acontece se o cofre configurado for excluído na D4Sign?

  A integração será desabilitada na primeira tentativa de envio após a exclusão. O usuário verá um **toaster de erro**, e o primeiro usuário que ativou a integração receberá uma **notificação por e-mail** informando a desativação.
- #### O que acontece se a pasta configurada for excluída na D4Sign?

  A pasta será removida da tela de integração, e os documentos passarão a ser enviados apenas para o cofre configurado.
  ⚠️ **Atenção**: a pasta excluída **não** será automaticamente removida do campo salvo na configuração.
- #### Posso adicionar o mesmo signatário mais de uma vez?

  Não. O sistema impede a duplicação de signatários para garantir a integridade do fluxo de assinatura.
- #### É possível definir signatários por padrão e em ordem fixa, como existe na D4Sign?

  Não. O processo de disparo de assinaturas com vinculação ao D4Sign é feito exclusivamente aqui no Ploomes e é preciso incluir os signatários manualmente e ajustar a ordem conforme desejado, mesmo quando há uma configuração de signatários e ordem no cofre do lado da D4.

---

## Glossário:

- **Token API / Chave de Criptografia**

  Credenciais fornecidas pela D4Sign para autenticação da integração.
- **Cofre (D4Sign)**

  Estrutura principal de armazenamento de documentos.
- **Pasta (D4Sign)**

  Subdivisão dentro do cofre para organização dos arquivos.
- **Assinatura D4Sign**

  Campo utilizado no modelo de documento para indicar o local da assinatura.
- **Via de envio**

  Meio pelo qual o signatário recebe o link de assinatura (e-mail ou WhatsApp).
- **Tipo de autenticação**

  Mecanismo de verificação utilizado antes da assinatura.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
