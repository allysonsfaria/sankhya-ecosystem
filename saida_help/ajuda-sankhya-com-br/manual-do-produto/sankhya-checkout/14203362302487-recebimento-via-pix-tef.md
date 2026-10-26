---
id: "14203362302487"
titulo: "Recebimento via Pix TEF "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14203362302487-Recebimento-via-Pix-TEF"
trilha: "Manual do Produto > Comercial e Vendas > Vendas > Sankhya Checkout"
atualizado_em: "2026-07-29T16:02:50Z"
rotulos: ["Configuração", "TEF", "Financeiro", "Sankhya Checkout", "PIX", "TEFGATEWAY", "Perfis e integração com SiTef", "Parâmetros no Sankhya e credenciais no TEF Nuvem", "Cancelamento parcial via NSU no SITEF", "Sitef"]
---

# Recebimento via Pix TEF 

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42314996837143) Módulo: Configurações > Sankhya Checkout    ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42314996839831) Versão disponível: a partir da 4.19
```

---

**Importante:** Para o correto funcionamento do Pix TEF e o registro adequado das informações de autorização, é fundamental que a **versão do client SiTef (SiTef PDV CliSitef) instalada na máquina seja compatível com o Sankhya**. A versão **V1.2.0.53** é a recomendada para garantir a integração completa e o preenchimento correto dos dados de transação. Versões anteriores, como a **V1.2.0.52**, podem causar problemas no registro do código de autorização.

---

Para realizar o recebimento Pix TEF no Checkout, primeiramente, é preciso configurar os Tipos de Títulos no **Sankhya Om**.

Assim, realize as seguintes configurações:

- Configure o parâmetro **"Gateway de recebimento com cartão (TEF) - TEFGATEWAY"** com a opção **"SiTef"**;
- Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba **"PIX"**, defina o campo **"Tipo de PIX"** com a opção **"TEF"**;
- Por fim, ainda na tela menciona, acesse a aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageral) e configure no campo **"Tipo de pgto para NFC-e / NF-e / CF-e"** a opção **"17 - Pagamento Instantâneo (PIX)"**.

![Imagem 3: É necessário cadastrar as credenciais do banco (PSP Recebedor) no Portal do TEF Nuvem; e após esse cadastro, deve-se…](https://ajuda.sankhya.com.br/hc/article_attachments/18786147624599) É necessário cadastrar as credenciais do banco (PSP Recebedor) no Portal do TEF Nuvem; e após esse cadastro, deve-se entrar em contato com o Suporte SKYTEF para habilitar o PIX na licença do TEF do estabelecimento.

Desse modo, o sistema estará apto para realizar o recebimento com Pix TEF no **Sankhya Checkout**.

[GIF animado: Imagem 4: Desse modo, o sistema estará apto para realizar o recebimento com Pix TEF no Sankhya Checkout .](https://ajuda.sankhya.com.br/hc/article_attachments/14768014953239)

Na aba [Integrações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abaintegra%C3%A7%C3%A3o) das [Preferências do Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout), informe o **"Tipo de Título para recebimento em PIX TEF"** conforme os Tipos de Títulos criados anteriormente no **Sankhya Om**.

Posteriormente, no [Cadastro de Perfis](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001985901-Menu-do-Checkout#perfis) do **Checkout**, habilite a marcação **"Receber em PIX TEF"** (aba **"Venda"**) ao cadastrar/configurar um perfil Caixa; lembre-se ainda que essa marcação ficará disponível apenas quando o campo **"Gateway de recebimento com cartão (TEF)"** do Cadastro de Checkouts (aba **"TEF"**) for definido com a opção **"SiTeF"**.

[GIF animado: Imagem 5: Posteriormente, no Cadastro de Perfis do Checkout , habilite a marcação "Receber em PIX TEF" (aba "Venda" ) ao…](https://ajuda.sankhya.com.br/hc/article_attachments/14384943477399)

**Nota:** ao ativar as marcações Receber em PIX POS e Receber em PIX TEF juntas, ou a marcação **"Marcar todos"** o sistema exibirá uma mensagem o informando que as marcações Receber em PIX POS e Receber em PIX TEF são exclusivas, isto é, deve-se acionar somente uma delas.

Dessa forma, ao realizar o recebimento de uma nota, o QRCode será gerado e ao efetuar o pagamento, o comprovante da transação será impresso.

[GIF animado: Imagem 6: Dessa forma, ao realizar o recebimento de uma nota, o QRCode será gerado e ao efetuar o pagamento, o comprovante da…](https://ajuda.sankhya.com.br/hc/article_attachments/14766314668823)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14203362302487-Recebimento-via-Pix-TEF#top)

---

#### Cancelamento de recebimento em PIX TEF

Ao realizar uma venda com recebimento parcial no Pix TEF, é possível efetuar o cancelamento do pagamento, caso o recebimento ainda não esteja finalizado. Considere o seguinte exemplo desse processo:

Na tela Vendas do Sankhya Checkout foi incluído um produto que terá uma parte do seu valor pago via PIX TEF.

Assim, após o [Recebimento via Pix TEF](https://ajuda.sankhya.com.br/hc/pt-br/articles/14203362302487-Recebimento-via-Pix-TEF#in%C3%ADciodasconfigura%C3%A7%C3%B5es) (conforme etapas demonstradas no início do artigo), caso seja necessário efetuar o cancelamento desse valor, acione o atalho -N, desse modo, será apresentado um pop-up com o Número Sequencial Único - NSU, copie o valor informado.

Depois, no **"Módulo SITEF"** selecione a carteira digital **"Pix"** e clique em **"Confirmar"**. Em seguida, em informações adicionais selecione a opção **"QR code do Estabelecimento"** e clique em **"Confirmar"**. Agora, informe o **"Valor"** que deseja cancelar, a **"Data da Transação"** e no campo "**Número do documento"** informe o NSU copiado anteriormente. Clique em **"Confirmar"**, para que o cancelamento seja efetivado.

[GIF animado: Imagem 7: Depois, no "Módulo SITEF" selecione a carteira digital "Pix" e clique em "Confirmar" . Em seguida, em informações…](https://ajuda.sankhya.com.br/hc/article_attachments/14878894597655)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/14203362302487-Recebimento-via-Pix-TEF#top)
