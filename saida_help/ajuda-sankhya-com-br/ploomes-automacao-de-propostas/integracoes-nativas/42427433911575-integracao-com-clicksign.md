---
id: "42427433911575"
titulo: "Integração com Clicksign"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427433911575-Integra%C3%A7%C3%A3o-com-Clicksign"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:40Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452445", "sync_hash_34db950a686e"]
---

# Integração com Clicksign

A integração entre o **Ploomes** e a **Clicksign** permite enviar documentos para assinatura digital diretamente da plataforma. É ideal para contratos, propostas e qualquer documento que exija validação formal de clientes ou parceiros.

Ao habilitar a integração, um novo botão será exibido no menu direito de cada documento, permitindo:

- disparo para assinatura;
- inclusão de signatários;
- acompanhamento do status de cada assinatura.

Para integrar, é necessário possuir um plano no Clicksign que permita conexões via API.

## Como realizar a integração?

## 1. Acessando o configurador no Ploomes

1. Acesse **Administração**.
2. Clique em **Integrações Plug and Play**.
3. Selecione **Clicksign**.
4. Clique em **Habilitar integração**.

![Imagem 1: Clique em Habilitar integração .](https://downloads.intercomcdn.com/i/o/872318419/ce00df73bdb582cb6e61d7aa/image.png?expires=1786536000&signature=ceb7b1ae5325275171b1361f1b56a6b81ac54adac4806965898f87c67d822302&req=fCclFch2mYBWFb4V1XW4gYDIpwTIN2nz2%2FpaBoBQlL9pZXoRXgBjZsYwHyAi%0ATWO%2FbIG5vNo9nWjreY%2B2Hoj81A%3D%3D%0A)

## 2. Gerando o Token no Clicksign

1. Entre na sua conta [Clicksign](https://www.clicksign.com/).
2. Acesse **Configurações > API**.

   [![Imagem 2: Acesse Configurações > API .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849534216/9d9b7a57d053f8c397b8a3f69745/image.png-expires-3D1619805600-signature-3Da0ed2b8bfc20190d1901daea49235a30cbc617faec452fb7aef8c0a8b6c0f5cc?expires=1786536000&signature=586c7a49655decb5491fa2662464ea973fce52b2a0fe19a31170ce22b5b48c56&req=dSgjH8x9mYNeX%2FMW3nq%2BgTjHNyaxl05mkYouYbXgjjHLI44hxXUZX41pxKop%0ANC2k0WSZ1WfIvQgPJB6k7g6fSzI%3D%0A)](https://downloads.intercomcdn.com/i/o/90506002/f7fcfd90ee60267d27dc0e12/image.png?expires=1619805600&signature=a0ed2b8bfc20190d1901daea49235a30cbc617faec452fb7aef8c0a8b6c0f5cc)
3. Role a página até o campo de configuração do e-mail do usuário da API.
4. Informe o e-mail, clique em **Salvar e-mail** e depois em **Gerar access token**.

   [![Imagem 3: Informe o e-mail, clique em Salvar e-mail e depois em Gerar access token .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849535424/81c3a953bc657be6655bb5ef804c/image.png-expires-3D1619805600-signature-3D5f93d1b1ea628ece351da9a521fc9f3596e3410118465ea17e65735729845793?expires=1786536000&signature=d8ed091bfc51a6147997745703228cb476a81f8d8567260c2c6efcc29429f2fc&req=dSgjH8x9mIVdXfMW3nq%2BgbBQzJc1CUjvBUc1LeWwEPvmzSpn3pGBRJPf0UZv%0ArcxY%2BOIpFzwpXnvt7NMCD2jBx6I%3D%0A)](https://downloads.intercomcdn.com/i/o/90506423/17a3aae987c4bc7e05267e3d/image.png?expires=1619805600&signature=5f93d1b1ea628ece351da9a521fc9f3596e3410118465ea17e65735729845793)
5. Adicione uma descrição e clique novamente em **Gerar access token**.

   [![Imagem 4: Adicione uma descrição e clique novamente em Gerar access token .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849535603/36d3174cf6b5f3e831ae4aa221b5/image.png-expires-3D1619805600-signature-3D144426a9ae142ea26a4c61e9fa8094809d98dbdd61a9ac9de85f8eb73feef4c6?expires=1786536000&signature=984f540cf8e69d5f591d0e416c8d474c45eabc52eff95e78a8873b4ba346706f&req=dSgjH8x9mIdfWvMW3nq%2Bgb7%2B9E64pQwpe2EY4npkOqMMZq%2FYdpRSlaEHmKQT%0AG1MPCzAdZFamXI%2FMahPxqFe3SjA%3D%0A)](https://downloads.intercomcdn.com/i/o/90506639/994a8fbfd9e791f99c280524/image.png?expires=1619805600&signature=144426a9ae142ea26a4c61e9fa8094809d98dbdd61a9ac9de85f8eb73feef4c6)
6. Copie o token criado.

   [![Imagem 5: Copie o token criado.](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330404/57b1bf01341ba62979739ea4/image.png-expires%3D1619805600-signature%3D4f75dc54b0aefdf7ea3f551b867028be5eb1df5f4c35623b8940a5ceb155c84a?expires=1786536000&signature=46d0fa1a14b7e4edf5d7d615fde55a48f8b80ac617edba1e5e6c7bf32e030ce3&req=dyYuFcp%2BmYFbFb4V1XW4gc%2Bu5zBiMZWIcLMdQUbLXa3aAnlg46CKZXePgEwD%0ARiZZzS%2B2ndkvfmBJb1KBV9U6tw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/90506797/4722005b886b861b6c716019/image.png?expires=1619805600&signature=4f75dc54b0aefdf7ea3f551b867028be5eb1df5f4c35623b8940a5ceb155c84a)

## 3. Autenticando o Token no Ploomes

1. Volte ao Ploomes.
2. Cole o token no campo **Token de autenticação**.

   ![Imagem 6: Cole o token no campo Token de autenticação .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849536875/3528cf123aa90921c96cf4fa5903/autorizarIntegracao.png?expires=1786536000&signature=a1052b717ff24f61ac8321e8692d80700a2c1a0ff478929b71145aff1109ba06&req=dSgjH8x9m4lYXPMW3nq%2Bgf1rEqW7J1R7AZA90cZALv1YxVgbcon3%2Bj%2FMgQ%2BM%0AD5DBY2THWDzsbS0%2BtolC495yXUE%3D%0A)

## 4. Customizando a integração

### Importar documentos assinados

Ative a opção "Deseja importar os documentos para o Ploomes após eles serem assinados?" para que, quando todas as assinaturas forem concluídas, o PDF do documento seja incluído na seção de "Anexos" do cliente.

![Imagem 7: Ative a opção "Deseja importar os documentos para o Ploomes após eles serem assinados?" para que, quando todas as…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849544835/d29bd8dda4dc6a8e9aaa24834d2b/unknown.png?expires=1786536000&signature=a0ac3fe6cfc2b579734891ff71d4fad45bd1f97ee8342c32e0965379113f401e&req=dSgjH8x6mYlcXPMW3nq%2BgT5vUPKsWQrHH%2BeIZkodbQAQWzkRAxiSKUqQ58fa%0AEW2dVJXLjiWgUlI4uT%2BGlqeCvVQ%3D%0A)

### Finalizar documento após última assinatura

Ative a opção "Finalizar documento após última assinatura" para que o documento seja automaticamente finalizado no Ploomes quando todos os signatários concluírem a assinatura.

![Imagem 8: Ative a opção "Finalizar documento após última assinatura" para que o documento seja automaticamente finalizado no…](https://downloads.intercomcdn.com/i/o/858449017/f717e605da77750c5a8a8fee/personalizarIntegracao.png?expires=1786536000&signature=45679ee5fb1dc95ff202ebc968db6bad9c954a52a72ece894f52fc0cfe8601a8&req=fCUvEs13nYBYFb4V1XW4gVtbOZTqYrKn4rdxEybGA1qy%2FcNMfoUR8SSrXJbS%0AjXxCGraKkS1Ak6VvR4l7VE0eaQ%3D%3D%0A)

### Mensagem enviada ao requisitar assinatura

Insira a mensagem que será enviada no e-mail para os assinantes.

Você pode digitar ou utilizar o recurso de fala.

![Imagem 9: Você pode digitar ou utilizar o recurso de fala.](https://downloads.intercomcdn.com/i/o/858449720/c6943eeaa66e0243c042a47a/mensagemIntegracao.png?expires=1786536000&signature=ebefd417cf0a494b78d4f70ff8850b2b6a9de0e330e59bb073dbc3ee94797263&req=fCUvEs13moNfFb4V1XW4gU9r0VAlR4sluzTRFFXaTRbDskK6qm3XNhjAbBlQ%0AzDIs8JVx3P8daX1UZQyq9n0%2FkQ%3D%3D%0A)

## 5. Configurando o Webhook no Clicksign

1. Clique em "Ativar integração".
2. Após ativar, copie a URL de Webhook exibida.

   ![Imagem 10: Após ativar, copie a URL de Webhook exibida.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849563421/e37cac12badc25f8e01389d92bb4/linkIntegracao.png?expires=1786536000&signature=94bed2296ab8527aca7620e9dfef9b8dab6865b08b53f2653b7119265d157358&req=dSgjH8x4noVdWPMW3nq%2Bgeb%2FUiMitWSujWikorma%2FYbXZwMt0h0pWrhw%2F7RJ%0AyWd2dH%2FlRa3XQZK0LzE%2Fy5zr4QU%3D%0A)
3. Volte ao Clicksign em **Configurações > API**.
4. Role a página até **Adicionar Webhook**.

   [![Imagem 11: Role a página até Adicionar Webhook .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849564134/8849d273ded0831b14fbd2b39281/image.png-expires-3D1619805600-signature-3D7adfdc503924dbf09b8e27dec56d464d655ef5a2d23dcbbb51a8aa31b4a56047?expires=1786536000&signature=304298dd3ba18d4125cd460569b092cf5c3fdd0970239c235ebc38042d6ccab2&req=dSgjH8x4mYBcXfMW3nq%2Bgdh54YqDbhD4FY85fwEPVbBb4XHhT2%2F4hdRmwgH9%0AxoYu%2BCAk%2BwsQ0M4%2Bd65c4dftgcA%3D%0A)](https://downloads.intercomcdn.com/i/o/90509050/bbcc589e67afbf5f0631e138/image.png?expires=1619805600&signature=7adfdc503924dbf09b8e27dec56d464d655ef5a2d23dcbbb51a8aa31b4a56047)
5. Cole a URL gerada.

   [![Imagem 12: Cole a URL gerada.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849564303/057e4925a7d718772954fa3ccacb/image.png-expires-3D1619805600-signature-3D6ca46f3efc3c6668ca387b8384f601267604beef9190137b614b975183ea1f78?expires=1786536000&signature=aac468377aee9264cf75453e6f31874b6dc8edbd7a61776e2704b207926b9dfc&req=dSgjH8x4mYJfWvMW3nq%2BgSyAdLicdMYG7jl5JHos62ARyDyjGsWdpbJYa6G6%0AYwjxtEA8xqfIXAuUrJ5OEuBdkSY%3D%0A)](https://downloads.intercomcdn.com/i/o/90509189/c2911186670aba1f725e68ac/image.png?expires=1619805600&signature=6ca46f3efc3c6668ca387b8384f601267604beef9190137b614b975183ea1f78)
6. Clique novamente em "Adicionar Webhook".

Pronto! A integração está finalizada.

## Como enviar o documento para assinatura?

1. Abra qualquer documento no Ploomes.
2. Clique em **Compartilhar** (canto superior direito).

   ![Imagem 13: Clique em Compartilhar (canto superior direito).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849566403/073b2bb34a1806b2baafb4054a3a/image.png?expires=1786536000&signature=f40282722e9da375ba5a7f393daf1c67c6342b2e27648b2289ef7f61030ee521&req=dSgjH8x4m4VfWvMW3nq%2BgS7a1mYk3g%2B%2FrSPMOO%2FXjtoEbo6hMuiUJPSPe%2B6J%0A8xsjoIn%2FMywbLthjUfgNjcDyYz4%3D%0A)
3. Escolha o método de compartilhamento **Clicksign**.
4. Em "Assinar" selecione o tipo de assinatura.
5. Em "Via Email" selecione o tipo de autenticação (via e-mail é o padrão).
6. Digite o e-mail do destinatário e clique em "Adicionar"

   ![Imagem 14: Digite o e-mail do destinatário e clique em "Adicionar"](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849566621/ea47a7c4e67444ac5b4443a7eae0/image.png?expires=1786536000&signature=fd73ed85f15d28609fc2313dcd98ff27e147f8cc9b62245cb2082c1372b1c7f9&req=dSgjH8x4m4ddWPMW3nq%2BgYZJaNX88iosMkXjRWdhFsb5H4mFjazRnH%2Bvly7u%0AXK%2BwIVjAI%2Bw6ZzSp4hZsnCBUg2o%3D%0A)
7. Após incluir todos os signatários, clique em **Enviar para assinatura**.

   ![Imagem 15: Após incluir todos os signatários, clique em Enviar para assinatura .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849590245/89887cab717b0dc1e1e92c56594c/image.png?expires=1786536000&signature=c3b09c4c8aca66e21087a458a7885875495ad5f21a584cf8ca26536313977e89&req=dSgjH8x3nYNbXPMW3nq%2BgZICN1pgCACNuT%2B6b%2FcsSgVcZAlxGoBXIJKxZOBS%0AMOaZ9BV8kCShl0gmXztiLzby7Ts%3D%0A)

Uma mensagem de sucesso aparecerá no canto inferior direito.

Quando todas as assinaturas forem concluídas, aparecerá "Assinatura por Clicksign realizada" na barra superior.

![Imagem 16: Quando todas as assinaturas forem concluídas, aparecerá "Assinatura por Clicksign realizada" na barra superior.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849600513/136bd3577399d01715c00a59f215/image.png?expires=1786536000&signature=6c77dbba6c24af8fb2ea839af39ba9726e2aaabf166782903ad1d9ec6fd39ae2&req=dSgjH89%2BnYReWvMW3nq%2BgdTu3kTDXB5aAQVaeH6cFiMU%2F97h4ucnX6h%2BAeDQ%0A2Lu0xhkQMMZNEhIegViYFzcSUbc%3D%0A)

## Tipos de autenticação de assinatura

Os tipos de autenticação disponíveis na integração são:

- Email
- Certificado Digital
- Pix
- SMS
- Whatsapp

![Imagem 17: Whatsapp](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849649864/dba497471c9c9b3ad16fc8f4be4f/unknown.png?expires=1786536000&signature=9324f2b3ad976c16d0f45a01bf29efc17a08ac946ab75fea6d36bbf443a7efab&req=dSgjH896lIlZXfMW3nq%2BgVcpf%2FyZPdKLHHOPLdnMjC%2FCqQJdP06yslhCJHtM%0AY%2FY1gVGq3w2eg7hf6U6XaSNSc%2BA%3D%0A)

## Como reenviar para assinatura?

Caso o documento ainda **não tenha sido assinado por todos**, é possível reenviar a solicitação de assinatura para todos os signatários envolvidos.

![Imagem 18: Caso o documento ainda não tenha sido assinado por todos , é possível reenviar a solicitação de assinatura para todos…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849649121/894d9721c79cfe4a0cf9fe873265/unknown.png?expires=1786536000&signature=bd84a43ba667613a226af1291c6b2e3142a845618dbd35ebbaf845a6ed21191e&req=dSgjH896lIBdWPMW3nq%2BgenzXNtVddKL4pogpkun3Dw8hkFqQHECbkKi%2B8Pm%0ANdhLUqfHINAd%2B03EFNFVnK3bWxQ%3D%0A)

## Como o signatário recebe e assina o documento?

1. O signatário receberá um e-mail com o botão **Assine agora**.

   [![Imagem 19: O signatário receberá um e-mail com o botão Assine agora .](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369330490/1f16358b1309716f69cb7720/image.png-expires%3D1619805600-signature%3D712209ce86736f4899971a9ab6b0e547b3646a55684c93ab35e5e84f5fbed2e3?expires=1786536000&signature=a14a866f5f832eae72613b98cf804d75ead07d4bfc602b143911d3ddbd92adbb&req=dyYuFcp%2BmYhfFb4V1XW4gZO%2FSzTtqfGAQfmy9cB9qJWzE7zcnxb4s8Xn1OU5%0AlYgF2YyWS0D%2BVHrwM7ML8c3Ueg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/90510605/a0efbfe18e6ddd9d32a286e6/image.png?expires=1619805600&signature=712209ce86736f4899971a9ab6b0e547b3646a55684c93ab35e5e84f5fbed2e3)
2. Ao abrir o link, poderá visualizar o documento.

   [![Imagem 20: Ao abrir o link, poderá visualizar o documento.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849598992/6977565ceb708f2361d149a52172/image.png-expires-3D1619805600-signature-3Df0a663d5c69073accc7d08e32ba10a9b8fda2c81c8d732dfc7b8099064d356da?expires=1786536000&signature=83209bbe292f9a215eac96fdfee97d55c3e6617553557c1b89ce16b6f6ca1647&req=dSgjH8x3lYhWW%2FMW3nq%2Bga%2FaIZm12BJ338EyAgTu1cLrDBbjqeoWJSuhIcB6%0APpLwl1%2Fn2hiP5qIhMpwrtyEI24w%3D%0A)](https://downloads.intercomcdn.com/i/o/90510873/16c754441dffe1802325c622/image.png?expires=1619805600&signature=f0a663d5c69073accc7d08e32ba10a9b8fda2c81c8d732dfc7b8099064d356da)
3. Em seguida, passará pelo processo de autenticação e receberá um token (via e-mail ou outro método configurado).

   [![Imagem 21: Em seguida, passará pelo processo de autenticação e receberá um token (via e-mail ou outro método configurado).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849599149/2b0be2a17073fb96d8bd086f2d3e/image.png-expires-3D1619805600-signature-3Dd78ab6097a7463b1b51ee8977cc3c027eb8e0560dae1295783fbc5b6f97d99d8?expires=1786536000&signature=915047dda027775152767153585a78638c7e5ae2cd7e82f4c743113284ad76df&req=dSgjH8x3lIBbUPMW3nq%2Bgc%2BL01CbZqHfrUqvevmtVQ86rTU5iGB0GpbSFe5H%0AXIYySLL%2FrI6wRts%2FeceTYiJnhaw%3D%0A)](https://downloads.intercomcdn.com/i/o/90511265/adad5d9fd2fe0b7b1a9e24e3/image.png?expires=1619805600&signature=d78ab6097a7463b1b51ee8977cc3c027eb8e0560dae1295783fbc5b6f97d99d8)
4. Após inserir o token, a assinatura será concluída.

   [![Imagem 22: Após inserir o token, a assinatura será concluída.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849632271/8404922ac42d9f9ce00f7deb8886/image.png-expires-3D1619805600-signature-3D43bae69616d690d860f838bc6bdf8900f2484b8105e16df8cd12473e919ee0bf?expires=1786536000&signature=d7edbc5139c8bfcef0b6d0a4a81d5ba89511b7c9277f698a7197b0204bf0753f&req=dSgjH899n4NYWPMW3nq%2BgYNZpO6bb7sW6cO49E5DG02RBWVUNU8qib2b21vX%0A%2BD1l5NkpPC9Uoi7j0W%2F5GNfApCA%3D%0A)](https://downloads.intercomcdn.com/i/o/90511449/4fc26f3daa933be7e76cebd8/image.png?expires=1619805600&signature=43bae69616d690d860f838bc6bdf8900f2484b8105e16df8cd12473e919ee0bf)

   [![Imagem 23: Após inserir o token, a assinatura será concluída.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1849632416/dbc6e0d1161e4999c7d65e9a8afc/image.png-expires-3D1619805600-signature-3D8f5da60565828170851bd3f6e92af7037ae14ea2c42452f18ed8537f30125ccf?expires=1786536000&signature=954a2ca53f9f6fea4c520d5ce8f1d3e0d4600c4eb78ee699fa4bf8728d43a6a8&req=dSgjH899n4VeX%2FMW3nq%2BgQZvQ4cNSvD6I9MxD1pMdaj96y3yPGyi44NXTfKY%0AIp3nhuikMtYNl7wVLXwzlkLuQ%2Fo%3D%0A)](https://downloads.intercomcdn.com/i/o/90511537/e6718a4817b8fbbf00bd0984/image.png?expires=1619805600&signature=8f5da60565828170851bd3f6e92af7037ae14ea2c42452f18ed8537f30125ccf)

Quando todos concluírem, o documento será finalizado no Ploomes (conforme a configuração definida durante a integração).

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
