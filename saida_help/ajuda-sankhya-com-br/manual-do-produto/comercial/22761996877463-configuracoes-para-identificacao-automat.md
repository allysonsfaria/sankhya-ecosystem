---
id: "22761996877463"
titulo: "Configurações para Identificação Automática de Bandeira de Cartão nos Recebimentos em TEF e POS no PDV Web"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:18:04Z"
rotulos: ["Configuração", "TEF", "Financeiro", "Tipos de Título", "Tipos de Negociação", "PDV Web", "POS", "REcebimento com cartão", "Cartão"]
---

# Configurações para Identificação Automática de Bandeira de Cartão nos Recebimentos em TEF e POS no PDV Web

A partir da versão 4.21, no [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047) será possível realizar a identificação automática de bandeira de cartão nos recebimentos em TEF e POS. Essa funcionalidade permite que, na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753), a Taxa administradora seja aplicada corretamente, além de simplificar a quantidade de tipos de títulos exibidos na tela do PDV Web. 

**Observação:** atualmente, a identificação automática de bandeira de cartões só está habilitada para uso com a PayGo e Sitef.

Acesse os links abaixo para realizar as configurações dessa funcionalidade no **Sankhya Om** para uso no PDV Web:

| Configurações | |
| --- | --- |
| [Configuração do Tipo de Título Principal ("Título pai")](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#Configura%C3%A7%C3%A3odoTipodeT%C3%ADtuloPrincipal) | |
| [Configuração de Tipo de Títulos Secundários ("Títulos filhos")](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#Configura%C3%A7%C3%A3odeTipodeT%C3%ADtulosSecund%C3%A1rios) | |
| [Configuração do Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#Configura%C3%A7%C3%A3odoTipodeNegocia%C3%A7%C3%A3o) | |
| Recebimentos no PDV Web | |
| [Recebimento no PDV Web utilizando identificação de bandeira automática por Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#RecebimentonoPDVWebutilizandoidentifica%C3%A7%C3%A3odebandeiraautom%C3%A1ticaporTipodeT%C3%ADtulo) | |
| [Recebimento no PDV Web utilizando identificação de bandeira automática por Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#RecebimentonoPDVWebutilizandoidentifica%C3%A7%C3%A3odebandeiraautom%C3%A1ticaporTipodeNegocia%C3%A7%C3%A3o) | |

### Configuração do Tipo de Título Principal ("Título pai")

Acesse a tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494) e configure as seguintes abas:

#### Aba Geral

Para que o sistema identifique corretamente a bandeira e a rede, siga as configurações abaixo conforme a integração utilizada:

(1)** PayGo**:

- **Rede**: no campo **"Parc. Administradora"**, insira a administradora responsável pelos recebimentos em TEF (adquirente).
- **Bandeira**: preencha o campo **"Forma Pagamento TEF"** com a bandeira do cartão.

(1)** Sitef**: **{disponível na versão 4.30b95}**

O sistema utiliza as informações configuradas nas telas [Bandeiras Tef](https://ajuda.sankhya.com.br/hc/pt-br/articles/28204786714647-Bandeiras-Tef) e [Redes Tef](https://ajuda.sankhya.com.br/hc/pt-br/articles/28206343290135-Redes-Tef). Para garantir o correto funcionamento:

- **Rede**: na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao) da tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), insira o código da Rede Tef no campo **"Nome da Rede na operação TEF"**. Depois, vincule o código do Cadastro de Parceiros ao campo **"Parc. Administradora"**, na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) do [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top), assim, o sistema reconhecerá a integração com o TEF SITEF.
- **Bandeira**: no campo **"Forma de Pagamento TEF"**, informe o nome da bandeira conforme registrado na tela Bandeiras Tef.

**Observação:** por se tratar do Tipo de Título Principal, no campo Forma Pagamento TEF poderá ser informado qualquer bandeira, pois esse Tipo de Título funcionará no PDV Web como base para iniciar o recebimento em TEF.

Caso o Tipo de Título seja para operações em POS, habilite a marcação **"Utiliza POS"**. 

![Imagem 1: Só é permitida a configuração de um Tipo de Título Principal para TEF e um para POS.](https://ajuda.sankhya.com.br/hc/article_attachments/22762635719319) Só é permitida a configuração de um Tipo de Título Principal para TEF e um para POS.

![Imagem 2: Só é permitida a configuração de um Tipo de Título Principal para TEF e um para POS.](https://ajuda.sankhya.com.br/hc/article_attachments/22762760660503)

#### Aba Fast Service

Nesta aba, ative obrigatoriamente a marcação **"Utiliza no Fast Service?"** para uso do PDV Web.

![Imagem 3: Nesta aba, ative obrigatoriamente a marcação "Utiliza no Fast Service?" para uso do PDV Web .](https://ajuda.sankhya.com.br/hc/article_attachments/22762969269015)

#### Aba Preferências de Cartão

Habilite nesta aba, a marcação **"Tip. título cartão principal PDV Web"**.

![Imagem 4: Habilite nesta aba, a marcação "Tip. título cartão principal PDV Web" .](https://ajuda.sankhya.com.br/hc/article_attachments/22763014926359)

**Observação:** a próxima etapa de configuração será o cadastro dos Tipos de Títulos Secundários ("Títulos filhos"). Esses Tipos de Títulos serão utilizados pelo PDV Web no momento da identificação da bandeira do cartão, retornada pelo gateway de pagamento (Sitef e PayGo), onde, de forma automática, será trocado por esse título no momento da efetivação do pagamento. Assim, na tela Movimentação Financeira, no campo **"Tipo de Título"** da guia [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Lan%C3%A7amento), será inserido a informação do "título filho". Quando o sistema não identificar o título filho cadastrado, na Movimentação Financeira esse campo será preenchido com o "título pai" e, no campo **"Histórico"** será inserido um texto informativo, onde não foi possível identificar o "tipo de título filho" devido à falta do cadastro.

Observe abaixo um título na Movimentação Financeira em que não foi possível identificar a bandeira do cartão:

![Imagem 5: Observe abaixo um título na Movimentação Financeira em que não foi possível identificar a bandeira do cartão:](https://ajuda.sankhya.com.br/hc/article_attachments/22764501532183)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#top)

### Configuração de Tipo de Títulos Secundários ("Títulos filhos")

A configuração dos Tipos de Títulos Secundários também é realizada nas seguintes abas da tela Tipos de Título:

#### Aba Geral

Nesta aba, indique no campo Forma Pagamento TEF a bandeira do cartão e o Parc. Administradora, que é a administradora dos recebimentos em TEF (adquirente). Preencha no campo **"% Taxa Administradora"**, a taxa que é aplicada conforme contrato firmado junto à administradora (adquirente).

**Nota:** por se tratar do Tipo de Título Secundário, todos os campos citados acima deverão ter a informação correta, pois estas são essenciais para a identificação da bandeira e aplicação da taxa na Movimentação Financeira.

Caso o Tipo de Título seja para operações em POS, ative a marcação Utiliza POS.

![Imagem 6: Caso o Tipo de Título seja para operações em POS, ative a marcação Utiliza POS .](https://ajuda.sankhya.com.br/hc/article_attachments/22764851213463)

#### Aba Fast Service

Nesta aba, ative obrigatoriamente a marcação Utiliza no Fast Service? para uso do PDV Web.

![Imagem 7: Nesta aba, ative obrigatoriamente a marcação Utiliza no Fast Service? para uso do PDV Web .](https://ajuda.sankhya.com.br/hc/article_attachments/22762969269015)

#### Aba Geral Preferências de Cartão

Determine, obrigatoriamente a quantidades de parcelas no campo **"Qtd. parcelas"**.

![Imagem 8: Determine, obrigatoriamente a quantidades de parcelas no campo "Qtd. parcelas" .](https://ajuda.sankhya.com.br/hc/article_attachments/22764880885399)

**Observação:** é recomendável cadastrar a quantidade de Tipos de Títulos Secundários que a Empresa permite parcelar por bandeira e administradora. Por exemplo, se a Empresa trabalhar com parcelamento por cartão de crédito em até 8 (oito) vezes na bandeira MASTERCARD para a administradora REDECARD, deverão ter 8 (oito) Tipos de Títulos Secundários cadastrados, além do Tipo de Título Principal.

Após a realização dessas configurações, o PDV Web passará a trabalhar com a identificação automática de bandeira de cartão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#top)

### Configuração do Tipo de Negociação

Para cadastrar os [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) nos quais se deseja ter recebimento com cartão TEF ou POS, recomenda-se utilizar o Tipo de Título Principal em uma das parcelas do cadastro, onde deverá ser configurado um registro (TEF ou POS), vinculando esse Tipo de Título cadastrado.

Abaixo, tem-se um exemplo de configuração do Tipo de Negociação, onde a forma de pagamento foi configurada como à vista + cartão de crédito TEF (auto).

![Imagem 9: Abaixo, tem-se um exemplo de configuração do Tipo de Negociação , onde a forma de pagamento foi configurada como à…](https://ajuda.sankhya.com.br/hc/article_attachments/22765924452119)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#top)

### Recebimento no PDV Web utilizando identificação de bandeira automática por Tipo de Título

Realizadas as configurações nos passos anteriores, ao efetuar uma venda no PDV Web serão exibidos apenas os Tipos de Títulos configurados como Tipo de Título Principal, quando o recebimento for feito por Tipo de Título.

Abaixo, segue um exemplo de recebimento por Tipo de Título com dois Tipos de Títulos Principais, sendo um para TEF e outro para POS.

![Imagem 10: Após informar o "Valor à Receber" e selecionar o "Tipo de título" , o pop-up de "Recebimento com cartão" TEF e POS será…](https://ajuda.sankhya.com.br/hc/article_attachments/22765927707159)Após informar o **"Valor à Receber"** e selecionar o **"Tipo de título"**, o pop-up de **"Recebimento com cartão"** TEF e POS será exibido na tela para prosseguir com o preenchimento da **"Qtd. parcelas"** que o cliente deseja realizar o pagamento e o acionamento do cliente modular do gateway de pagamento:

![Imagem 11: Após informar o "Valor à Receber" e selecionar o "Tipo de título" , o pop-up de "Recebimento com cartão" TEF e POS será…](https://ajuda.sankhya.com.br/hc/article_attachments/22766108897047)

Após concluir o recebimento e a nota, na Movimentação Financeira, o campo Tipo de Título terá a informação referente ao Tipo de Título Secundário, de acordo com a bandeira, administradora e quantidade de parcelas retornadas durante o recebimento no PDV Web.

Nos casos em que não for possível identificar o Tipo de Título Secundário, na Movimentação Financeira será mantido o Tipo de Título Principal e no campo Histórico será informado o motivo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#top)

### Recebimento no PDV Web utilizando identificação de bandeira automática por Tipo de Negociação

Ao realizar uma venda no PDV Web por Tipo de Negociação serão exibidos apenas os Tipos de Títulos configurados como Tipo de Título Principal, quando o recebimento for feito por Tipo de Título.

Abaixo tem-se um exemplo de recebimento por Tipo de Negociação com dois Tipos de Títulos Principais, sendo um para TEF e outro para POS.

![Imagem 12: Abaixo tem-se um exemplo de recebimento por Tipo de Negociação com dois Tipos de Títulos Principais , sendo um para TEF…](https://ajuda.sankhya.com.br/hc/article_attachments/22768015872407)

Ao efetuar o recebimento no pop-up Recebimento com cartão, as parcelas serão decompostas na tela, de acordo com a quantidade de parcelas informadas no campo Qtde parcelas, e consequentemente, transacionadas na operadora do TEF:

![Imagem 13: Ao efetuar o recebimento no pop-up Recebimento com cartão , as parcelas serão decompostas na tela, de acordo com a…](https://ajuda.sankhya.com.br/hc/article_attachments/22768015881239)

Após concluir todos os recebimentos previstos no Tipo de Negociação, ao finalizar a venda clicando no botão **"[F7] Concluir"**, as parcelas serão exibidas na Movimentação Financeira da mesma forma que ocorre no Recebimento por Tipo de Título.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22761996877463-Configura%C3%A7%C3%B5es-para-Identifica%C3%A7%C3%A3o-Autom%C3%A1tica-de-Bandeira-de-Cart%C3%A3o-nos-Recebimentos-em-TEF-e-POS-no-PDV-Web#top)
