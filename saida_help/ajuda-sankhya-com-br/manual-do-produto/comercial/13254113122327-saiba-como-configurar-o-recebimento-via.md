---
id: "13254113122327"
titulo: "Saiba como configurar o recebimento via Pix"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:17:45Z"
rotulos: ["Configuração", "Contas", "Financeiro", "Sankhya Checkout", "PIX", "recebimento via PIX", "PDV Web", "recebimento via PIX no PDV Web", "PEREXCFINPOS", "Configurações PDV Web", "Recebimento via Pix"]
---

# Saiba como configurar o recebimento via Pix

Neste artigo, trataremos das etapas para a configuração do recebimento via Pix por meio do [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047) e [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394-Vis%C3%A3o-geral-do-Sankhya-Checkout).

| Recebimento via Pix |
| --- |
| [Configuração das Credenciais Pix](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#Configura%C3%A7%C3%A3odasCredenciaisPix) |
| [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#PDVWeb)   - [Configurações para o Recebimento via Pix](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#Configura%C3%A7%C3%B5esparaoRecebimentoviaPix)   - [Cadastro do Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#CadastrodoTipodeT%C3%ADtulo)   - [Tipo de Título para o Pix POS](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#TipodeT%C3%ADtuloparaoPixPOS)   - [Cadastro do Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#CadastrodoTipodeNegocia%C3%A7%C3%A3o)        - [Configurações adicionais para o Recebimento no PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#Configura%C3%A7%C3%B5esadicionaisparaoRecebimentonoPDVWeb)   - [Recebimento com Pix no PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#RecebimentocomPixnoPDVWeb)   - [Recebimento com Pix POS no PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#RecebimentocomPixPOSnoPDVWeb)   - [Recebimento com Pix TEF no PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#RecebimentocomPixTEFnoPDVWeb)   - [Cancelamento de recebimento via Pix TEF](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#CancelamentoderecebimentoviaPixTEF) |
| [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#SankhyaCheckout)   - [Configurações para o recebimento Pix TEF](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#Configura%C3%A7%C3%B5esparaorecebimentoPixTEF)   - [Cancelamento do recebimento Pix TEF](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#CancelamentodorecebimentoPixTEF)  - [Configurações para o recebimento PIX QRcode](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#Configura%C3%A7%C3%B5esparaorecebimentoPIXQRcode) |

---

## Configuração das Credenciais Pix

Com as informações de credenciais Pix recebidas da instituição bancária, o primeiro passo é configurá-las no Sankhya Om. Acesse a tela **Contas**, aba **Pix**, e configure os campos de acordo com a sua instituição bancária.

**(1)Banco do Brasil**

O recebimento via Pix para o Banco do Brasil é realizado exclusivamente pelo modelo Pix Imediato, disponível na Fintech Sankhya. As configurações de credenciais descritas abaixo não se aplicam a esta instituição.

**Para configurar, acesse:** [**Pix Imediato**](https://ajuda.sankhya.com.br/hc/pt-br/articles/36268652893591-PIX-imediato)**.**

---

**(1)** **Banco Itaú**

Preencha na aba Pix, os campos:

- Chave da API PIX,
- Client ID PIX,
- Chave PIX.

Em seguida, acione na mesma aba a marcação **"Utiliza PIX PDV"**, para poder gerar a credencial.

Com as informações preenchidas, clique no botão ![Imagem 1: Com as informações preenchidas, clique no botão "Outras Opções" e selecione "Gerar certificado Pix" . No pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/28757106572567) **"Outras Opções"** e selecione **"Gerar certificado Pix"**. No pop-up **"Geração de certificado Pix"** informe os campos **"Site da empresa"**, **"E-mail de contato"** e **"Token Temporário"**, e clique em **"OK"**.

![Imagem 2: Com as informações preenchidas, clique no botão "Outras Opções" e selecione "Gerar certificado Pix" . No pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/28757106573719)

**Nota:** caso a empresa não possua um site, preencha o campo Site da empresa com a mesma informação do campo E-mail de contato.

Ao concluir corretamente será apresentada a seguinte mensagem:

**"Credenciamento realizado com sucesso"**

Após o credenciamento, o campo **"Client Secret Pix"** será automaticamente preenchido com a informação gerada.

![Imagem 3: Após o credenciamento, o campo "Client Secret Pix" será automaticamente preenchido com a informação gerada.](https://ajuda.sankhya.com.br/hc/article_attachments/28757087699735)

Depois, em [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), selecione a empresa em que os recebimentos serão creditados e informe na aba [PIX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893#abapix), o **"Tipo de PIX"**. Essa configuração deve ser efetuada para as duas instituições bancárias (Itaú e Banco do Brasil).

**Observação:** após salvar a alteração do campo "Tipo de PIX", o campo **"Conta Fintech"** deverá ser preenchido com a conta cadastrada na Fintech. Caso isso não ocorra automaticamente, revise as etapas anteriores de configuração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

## PDV Web

### Configurações para o Recebimento via Pix

#### Cadastro do Tipo de Título

Na tela Tipos de Título cadastre um novo Tipo de Título para as operações de Pix POS. Para isso, clique no botão ![Imagem 4: Na tela Tipos de Título cadastre um novo Tipo de Título para as operações de Pix POS. Para isso, clique no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16454855220375) **"Cadastrar Tipo de Título"**informe a **"Descrição"** do registro e selecione no campo **"Subtipo"**, a opção **"PIX POS"**.

Ainda nessa tela, acione na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) a marcação **"Utiliza POS"**.

![Imagem 5: Ainda nessa tela, acione na aba Geral a marcação "Utiliza POS" .](https://ajuda.sankhya.com.br/hc/article_attachments/17733851957527)

![Imagem 6: As configurações da aba Preferências de Cartão da tela Tipos de Título também possuem influência nas operações de Pix…](https://ajuda.sankhya.com.br/hc/article_attachments/17846078144151) As configurações da aba [Preferências de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto) da tela Tipos de Título também possuem influência nas operações de Pix POS.

Ainda na aba Geral, selecione no campo **"Tipo de pgto para NFC-e / NF-e / CF-e"** a opção **"17-Pagamento Instantâneo (PIX)"**.

![Imagem 7: Ainda na aba Geral , selecione no campo "Tipo de pgto para NFC-e / NF-e / CF-e" a opção "17-Pagamento Instantâneo…](https://ajuda.sankhya.com.br/hc/article_attachments/17733836054807)

Na aba [Fast Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abafastservice), ative a marcação **"Utiliza no Fast Service?"**.

![Imagem 8: Na aba Fast Service , ative a marcação "Utiliza no Fast Service?" .](https://ajuda.sankhya.com.br/hc/article_attachments/17733836055319)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

#### Tipo de Título para o Pix POS

Para o Pix POS, além dos passos de cadastro de Pix mencionados anteriormente, será necessário configurar as seguintes informações:

Na tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494) cadastre um novo tipo de título para operações em Pix POS. Para isso, clique no botão ![Imagem 9: Na tela Tipos de Título cadastre um novo tipo de título para operações em Pix POS. Para isso, clique no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16454855220375) **"Cadastrar Tipo de Título"**, informe a **"Descrição"** do registro e selecione no campo **"Subtipo"** a opção **"PIX POS"**.

Ainda nessa tela, acione na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494#abageral) a marcação **"Utiliza POS"**.

![Imagem 10: Ainda nessa tela, acione na aba Geral a marcação "Utiliza POS" .](https://ajuda.sankhya.com.br/hc/article_attachments/17733836061207)

E em seguida, informe na aba [Preferências do Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494#abaprefernciasdecarto) o campo **"Operação CTF"** com a opção **"Débito"**, uma ves que também poderão ser utilizadas em operações PIX POS.

![Imagem 11: E em seguida, informe na aba Preferências do Cartão o campo "Operação CTF" com a opção "Débito" , uma ves que também…](https://ajuda.sankhya.com.br/hc/article_attachments/17733851969047)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

#### Cadastro do Tipo de Negociação

Acesse a tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) e vincule no campo **"Tipo de Título"** o tipo de título cadastrado anteriormente.

![Imagem 12: Acesse a tela Tipos de Negociação , aba Parcelas e vincule no campo "Tipo de Título" o tipo de título cadastrado…](https://ajuda.sankhya.com.br/hc/article_attachments/17733836065559)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

#### Configurações adicionais para o Recebimento no PDV Web

O recebimento dos valores das mercadorias será realizado com o acionamento do botão **"Receber"**, no entanto, algumas configurações serão necessárias para que esse processo ocorra de forma correta. Iremos abordar cada um delas:

![Imagem 13: Nas Preferências da Empresa , sub-aba NFC-e (sub-aba NF-e/NFC-e da aba Documentos Fiscais Eletrônicos ) , "Seção NFC-e"…](https://ajuda.sankhya.com.br/hc/article_attachments/17733851926551) Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), sub-aba [NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abanf-enfc-e) (sub-aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNF-e/NFC-e) da aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)), **"Seção NFC-e"**, habilite a marcação **"Utiliza troco no PDV Web"**;

**Observação:** ao ser realizada uma venda por Tipo de Negociação que contenha troco, será apresentado um pop-up **"Recebimento em dinheiro"**, não havendo possibilidade de receber por meio de outras opções como ocorre no recebimento por Tipo de Título.

![Imagem 14: As formas de pagamento do PDV Web , sendo elas Dinheiro , Cheque , Cartão de Crédito e Cartão de Débito , devem estar…](https://ajuda.sankhya.com.br/hc/article_attachments/17733836030743) As formas de pagamento do PDV Web, sendo elas Dinheiro, Cheque, Cartão de Crédito e Cartão de Débito, devem estar devidamente configuradas e associadas a um tipo de título. Esta associação é feita no cadastro de [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494), por meio dos campos **"Tipo de pgto para NFC-e/NF-e/CF-e"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)) e **"Operação CTF"** (aba [Preferências de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto)).

![Imagem 15: Além disso, habilite o parâmetro "Usa recebimento com carto (CTFClient)? - USARECEBCARTCTF" .](https://ajuda.sankhya.com.br/hc/article_attachments/17733836035095) Além disso, habilite o parâmetro **"Usa recebimento com carto (CTFClient)? - USARECEBCARTCTF"**. 

![Imagem 16: Na tela Configurador de Layout da Nota , indique através do campo "Tipo Recebimento" qual será a forma de recebimento a…](https://ajuda.sankhya.com.br/hc/article_attachments/17733836035991) Na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634), indique através do campo **"Tipo Recebimento"** qual será a forma de recebimento a ser utilizada.

Desse modo, ao solicitar o recebimento, o sistema estará pronto e levará em consideração o Tipo de Recebimento selecionado. Sendo que, ao optar pela opção Ambos será necessário indicar um dos tipos para dar continuidade no processo:

![Imagem 17: Desse modo, ao solicitar o recebimento, o sistema estará pronto e levará em consideração o Tipo de Recebimento…](https://ajuda.sankhya.com.br/hc/article_attachments/17846258310295)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

### Recebimento com Pix no PDV Web

Na tela [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047), após a efetuar uma venda, na tela de recebimento, pode-se receber por Pix o tipo de título e o tipo de negociação configurado nas etapas anteriores. 

No recebimento com Tipo de Título, o tipo de título configurado estará disponível na opção **"E - Pix"**. Assim, ao informar o **"Valor à Receber"** e clicar no tipo de título da opção E - Pix, o QR Code será exibido na tela para leitura no aplicativo do banco do cliente pagador.

[GIF animado: Imagem 18: No recebimento com Tipo de Título , o tipo de título configurado estará disponível na opção "E - Pix" . Assim, ao…](https://ajuda.sankhya.com.br/hc/article_attachments/13257811653527)

No recebimento com Tipo de Negociação, o tipo de negociação configurado deverá ser informado no pop-up **"[F2] Identificar"**. Depois, na tela de recebimento, clique no botão **"Receber"**, assim, o QR Code será exibido na tela para leitura no aplicativo do banco do cliente pagador.

[GIF animado: Imagem 19: No recebimento com Tipo de Negociação , o tipo de negociação configurado deverá ser informado no pop-up "(F2)…](https://ajuda.sankhya.com.br/hc/article_attachments/13258151691287)

**Observações:**

- No **Sankhya Om**, os recebimentos realizados por Pix irão constar na Conta Caixa PDV do usuário logado. Os valores recebidos serão creditados diretamente na conta Pix configurada para a Empresa. Além disso, as transferências entre as contas no **Sankhya Om** não serão feitas de forma automática, devendo o usuário realizar essa operação para futura conciliação bancária.
- O pagamento realizado por **"PIX"** no PDV Web, não será registrado na tabela TGFPIX. De forma que, quando o financeiro da transação for aprovado, a marcação **"Recebido"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abageral) da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) será automaticamente habilitada.
- Ao gerar o Qr Code para pagamento via PIX, o sistema ficará validando de tempo em tempo, o retorno de confirmação de pagamento retornado pela API. Quando o pagamento for confirmado, a marcação Recebido do financeiro vinculado ao ID da transação será habilitada. Lembrando que, a baixa ocorrerá após a confirmação da nota, ao finalizar a venda no Pdv Web. Para conferir, basta filtrar a Empresa vinculada à nota, o código do Usuário logado no sistema e a Conta selecionada no processo de baixa por tipo de título. Importante ressaltar, que essa conta deve estar parametrizada no campo **"Número da conta padrão na baixa"** das [Configurações do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es) na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/6505454717591).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

### Recebimento com Pix POS no PDV Web

No recebimento com Tipo de Título, o tipo de título configurado estará disponível na opção **"E - Pix"**. Assim, ao informar o **"Valor à Receber"** e clicar no tipo de título da opção E - Pix, na modalidade Pix POS, o pop-up de recebimento em Pix POS será exibido para que seja informado os seguintes dados da transação:

No campo **"NSU"** informe o número sequencial único.

Depois, indique a quantidade de parcelas no campo **"Qtd. Parcelas"**. Em seguida, defina a data da transação no campo **"Dt. Transação"**. Por fim, no campo **"Vlr Transação"** informe o valor da transação. 

Feito isso, clique em **"Confirmar"**.

![Imagem 20: Feito isso, clique em "Confirmar" .](https://ajuda.sankhya.com.br/hc/article_attachments/16454306647319)

Já no recebimento com Tipo de Negociação, o tipo de negociação configurado deverá ser informado no pop-up **"[F2] Identificar"**. Depois, na tela de recebimento, clique no botão **"Receber"**, assim o pop-up de recebimento em Pix POS será exibido para que seja informado o Número Sequencial Único-NSU identificador da transação realizada.

**Nota:** para realizar a exclusão de notas com recebimento no cartão POS, basta ligar o parâmetro **"Permite excluir financeiros POS - PEREXCFINPOS"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

### Recebimento com Pix TEF no PDV Web

![Imagem 21: O uso dessa funcionalidade é exclusivo para a integração com a Sitef (SkyTEF).](https://ajuda.sankhya.com.br/hc/article_attachments/17846078144151) O uso dessa funcionalidade é exclusivo para a integração com a Sitef (SkyTEF).

Para receber um Tipo de Negociação ou um Tipo de Título com o Pix do tipo **"TEF"**, realize as configurações de acordo com o tópico [Configurações para o Recebimento via Pix](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#Configura%C3%A7%C3%B5esparaoRecebimentoviaPix).

Com as configurações acima previamente realizadas, na tela [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047), inclua um [Novo documento no Portal](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web#novodocumentonoportal), assim, na tela de recebimento, ao acionar o botão **"Concluir"** será apresentado um pop-up para confirmar o recebimento com Pix. 

**Observação:** a conta da baixa ultilizada para o recebimento com Pix TEF será a informada na aba [PIX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapix) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#top).

**Nota:** no Portal do TEF Nuvem, é necessário cadastrar as credenciais do banco (PSP Recebedor). Após o cadastro, entre em contato com o Suporte SKYTEF para que seja habilitado o Pix na licença do TEF do estabelecimento.

Canais de Atendimento Suporte SKYTEF:

- 11-2175-9501 /2175- 9500 / 11- 4550-1450 / 0800-9797-625;
- E-mail [suporte.tef@skytef.com.br](mailto:suporte.tef@skytef.com.br);
- Para obter o suporte pelo chat, acesse o site [www.skytef.com.br](http://www.skytef.com.br).

**Observação:** caso a comunicação seja realizada através do Clientmodular, será necessário incluir a configuração abaixo no arquivo "Clientetrn.ini.", localizado na pasta "c:/Client": 

[BOTOES\_HABILITADOS]
btCarteirasDigitais=1

Ressaltamos que antes de efetuar este procedimento, é necessário pausar o "clientSitef" e, em seguida, reiniciar para validação da configuração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

### Cancelamento de recebimento via Pix TEF

Ao realizar uma venda com recebimento via Pix TEF, é possível efetuar o cancelamento do pagamento, caso o recebimento ainda não esteja finalizado.

Para isso, acione o botão ![Imagem 22: Para isso, acione o botão "Cancelar" e no pop-up "Estornar Recebimento PIX TEF" clique no botão "Estornar".](https://ajuda.sankhya.com.br/hc/article_attachments/17733836069399) **"Cancelar"** e no pop-up **"Estornar Recebimento PIX TEF"** clique no botão **"Estornar".**

![Imagem 23: Para isso, acione o botão "Cancelar" e no pop-up "Estornar Recebimento PIX TEF" clique no botão "Estornar".](https://ajuda.sankhya.com.br/hc/article_attachments/17733836076695)

Ao clicar no botão Estornar, o sistema fará o chamado ao client SITEF. Nele, selecione a carteira digital **"Pix"** e clique em **"Confirmar"**. Em seguida, informe a **"Data da Transação"** e o **"Número do documento"**. Clique em **"Confirmar"**, para que o cancelamento seja efetivado. 

**Observação:** após a confirmação do cancelamento pela SITEF, na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) será criado um movimento de Receita e outro de Despesa e o primeiro lançamento financeiro gerado no recebimento será excluído automaticamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

## Sankhya Checkout

### Configurações para o recebimento Pix TEF

![Imagem 24: O uso dessa funcionalidade é exclusivo para a integração com a Sitef (SkyTEF).](https://ajuda.sankhya.com.br/hc/article_attachments/17846078144151) O uso dessa funcionalidade é exclusivo para a integração com a Sitef (SkyTEF).

Para realizar o recebimento Pix TEF no [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394-Vis%C3%A3o-geral-do-Sankhya-Checkout), primeiramente, é preciso configurar os [Tipos de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) no **Sankhya Om**.

Depois, na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), acesse a aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageral) e selecione no campo **"Tipo de pgto para NFC-e / NF-e / CF-e"** a opção **"17 - Pagamento Instantâneo (PIX)"**.

Desse modo, o sistema estará apto para realizar o recebimento com Pix TEF no Sankhya Checkout. 

Agora, acesse o Sankhya Checkout e informe no menu [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout), aba [Integrações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abaintegra%C3%A7%C3%A3o) o **"Tipo de Título para recebimento em PIX TEF"** conforme os Tipos de Títulos criados anteriormente no **Sankhya Om**.

Depois, no [Cadastro de Perfis](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001985901-Menu-do-Checkout#perfis) do Sankhya Checkout, habilite a marcação **"Receber em PIX TEF"** (aba **"Venda"**) ao cadastrar/configurar um perfil Caixa.

![Imagem 25: Essa marcação ficará disponível apenas quando o campo "Gateway de recebimento com cartão (TEF)" do "Cadastro de…](https://ajuda.sankhya.com.br/hc/article_attachments/17846078144151) Essa marcação ficará disponível apenas quando o campo **"Gateway de recebimento com cartão (TEF)"** do **"Cadastro de Checkouts"** (aba **"TEF"**) for definido com a opção **"SiTeF"**.

[GIF animado: Imagem 26: Essa marcação ficará disponível apenas quando o campo "Gateway de recebimento com cartão (TEF)" do "Cadastro de…](https://ajuda.sankhya.com.br/hc/article_attachments/17733851924887)

**Nota:** ao ativar as marcações Receber em PIX POS e Receber em PIX TEF juntas, ou a marcação **"Marcar todos"** o sistema exibirá uma mensagem o informando que as marcações Receber em PIX POS e Receber em PIX TEF são exclusivas, isto é, deve-se acionar somente uma delas.

Dessa forma, ao realizar o recebimento de uma nota, o QRCode será gerado e ao efetuar o pagamento, o comprovante da transação será impresso.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

### Cancelamento de recebimento em Pix TEF

Ao realizar uma venda com recebimento parcial no Pix TEF, é possível efetuar o cancelamento do pagamento, caso o recebimento ainda não esteja finalizado. Considere o seguinte exemplo desse processo:

Na tela **"Vendas"** do [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394-Vis%C3%A3o-geral-do-Sankhya-Checkout) foi incluído um produto que terá uma parte do seu valor pago via Pix TEF.

Assim, após o Recebimento via Pix TEF, caso seja necessário efetuar o cancelamento desse valor, acione o atalho -N, desse modo, será apresentado um pop-up com o Número Sequencial Único-NSU, copie o valor informado. 

Depois, no **"Módulo SITEF"** selecione a carteira digital **"Pix"** e clique em **"Confirmar"**. Em seguida, em informações adicionais, selecione a opção **"QR code do Estabelecimento"** e clique em **"Confirmar"**. Agora, informe o **"Valor"** que deseja cancelar, a **"Data da Transação"** e no campo **"Número do documento"** informe o NSU copiado anteriormente. Clique em **"Confirmar"**, para que o cancelamento seja efetivado. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)

### Configurações para o recebimento PIX QRcode

Para realizar o recebimento Pix QRcode no [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394-Vis%C3%A3o-geral-do-Sankhya-Checkout), primeiramente, no **Sankhya Om** configure no cadastro de [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Pix](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abapix), os campos:

- Chave da API Pix;
- Client Secret Pix;
- Client ID Pix;
- Chave pix;

E acione a marcação **"Utiliza PIX PDV"**.

![Imagem 27: E acione a marcação "Utiliza PIX PDV" .](https://ajuda.sankhya.com.br/hc/article_attachments/28384532830487)

Em seguida, na tela de [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [PIX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapix), selecione no campo **"Tipo de PIX"** a opção **"API(BB e Itaú)"**. Desse modo, os demais campos desta aba serão preenchidos automaticamente com base no cadastro de Contas.

![Imagem 28: Em seguida, na tela de Preferências da Empresa , aba PIX , selecione no campo "Tipo de PIX" a opção "API(BB e Itaú)" .…](https://ajuda.sankhya.com.br/hc/article_attachments/28384548228375)

Acesse a tela os [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), e configure o campo **"Subtipo"** com a opção **"PIX"**. Depois, na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral), selecione no campo **"Tipo de pgto para NFC-e / NF-e / CF-e"** a opção **"17-Pagamento Instantâneo (PIX)"**. 

![Imagem 29: Acesse a tela os Tipos de Título , e configure o campo "Subtipo" com a opção "PIX" . Depois, na aba Geral , selecione…](https://ajuda.sankhya.com.br/hc/article_attachments/17733836054807)

![Imagem 30: A guarde alguns minutos para a sincronização dos dados entre o Sankhya Om e o Sankhya Checkout .](https://ajuda.sankhya.com.br/hc/article_attachments/28383726857879) Aguarde alguns minutos para a sincronização dos dados entre o **Sankhya Om** e o **Sankhya Checkout**.

Agora, acesse o **Sankhya Checkout** e na página principal clique no ![Imagem 31: Agora, acesse o Sankhya Checkout e na página principal clique no "Menu" > "Cadastros" .](https://ajuda.sankhya.com.br/hc/article_attachments/28383754693911) **"Menu"** > **"Cadastros"**.

![Imagem 32: Agora, acesse o Sankhya Checkout e na página principal clique no "Menu" > "Cadastros" .](https://ajuda.sankhya.com.br/hc/article_attachments/28383726864535)

Em seguida, clique em **"Perfis"** > **"Perfis e acesso"**. Clique duas vezes sobre o perfil desejado para abrir o pop-up de configuração do perfil. Na aba **"Venda"**, conceda a permissão **"Receber com Pix"**.

[GIF animado: Imagem 33: Em seguida, clique em "Perfis" > "Perfis e acesso" . Clique duas vezes sobre o perfil desejado para abrir o pop-up de…](https://ajuda.sankhya.com.br/hc/article_attachments/28383726866071)

**Importante:** não é possível configurar as marcações Receber com Pix e Receber em PIX TEF simultaneamente.

Volte para o Menu e selecione a opção **"Preferências"**. Na aba **Integração**, no campo **"Tipo de título para recebimento em PIX"**, informe o código do cadastro do Tipo de Título realizado no **Sankhya Om**.

![Imagem 34: Volte para o Menu e selecione a opção "Preferências" . Na aba Integração , no campo "Tipo de título para recebimento em…](https://ajuda.sankhya.com.br/hc/article_attachments/28383726869015)

Após as configurações, acesse o **"Menu"** > **"Venda"** no **Sankhya Checkout**. Ao realizar uma venda, a opção de recebimento **"Pix"** ficará disponível:

![Imagem 35: Após as configurações, acesse o "Menu" > "Venda" no Sankhya Checkout . Ao realizar uma venda, a opção de recebimento…](https://ajuda.sankhya.com.br/hc/article_attachments/28383726870807)

Ao acioná-la será exibido o QR Code para pagamento:

![Imagem 36: Ao acioná-la será exibido o QR Code para pagamento:](https://ajuda.sankhya.com.br/hc/article_attachments/28383754702359)

**Nota:** certifique-se de que, ao utilizar apenas uma das opções, PIX QRcode ou PIX TEF, a outra opção não seja configurada para evitar problemas operacionais. Por exemplo:

Quando PIX TEF não é utilizado, mas a conta de recebimento do PIX TEF está configurada nas Preferências da empresa ou o Tipo de título para recebimento via PIX TEF está configurado no Checkout.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/13254113122327-Saiba-como-configurar-o-recebimento-via-Pix#top)
