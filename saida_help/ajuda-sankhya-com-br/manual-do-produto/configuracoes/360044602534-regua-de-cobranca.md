---
id: "360044602534"
titulo: "Régua de Cobrança"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-10-22T18:20:08Z"
rotulos: ["manual", "SMS", "Configuração", "Eventos", "Parceiro", "TIPTITCREDCLI", "br.com.sankhya.reguacobranca", "Régua de Cobrança manual", "Cobrança", "DIASHISTREGUA", "Financeiro", "FOLGASAB", "FOLGADOM", "Gerenciando a Régua de Cobrança", "USAWHATSREGUA", "Neppo", "Envio de whatsapp", "DIASDESATRÉGUA", "Whatsapp", "Automação"]
---

# Régua de Cobrança

```
 Módulo: Financeiro > Cobrança
```

---

A **Régua de Cobrança** é uma ferramenta de automação que gerencia todos os procedimentos de cobrança de uma empresa. Deste modo, tem-se a garantia de um nível elevado de comodidade e apoio na redução do índice de inadimplência.

Este recurso se resume na definição de diversos eventos de cobrança na **"Timeline"** (linha do tempo) dos títulos que serão executados de forma automática a medida em que a data de vencimento se aproxima ou se distancia (vence).

Os eventos disponíveis na funcionalidade são:

- Envio de mensagens por SMS, E-mail ou Whatsapp;
- Registro de eventos na agenda da equipe de cobrança (Agenda de recurso ou Gerência de cobrança);
- Bloqueio de novas vendas à prazo;
- Geração de arquivos para transmissão FTP ou disponibilidade em diretório;
- Ações personalizadas.

**Observações:**

- A **Régua de Cobrança** é executada somente uma vez por dia, apenas quando tratar-se da baixa do título é que ocorrerá a sua execução imediata. Além, disso o sistema só considera dias corridos na execução.
- Ao utilizar uma base diferente de Produção (Teste, Treinamento) e o parâmetro **"Dias para desativar régua em base diferente de produção - DIASDESATRÉGUA"** estiver configurado com um número diferente de zero, caso exista qualquer **Régua de Cobrança** **"Ativa"** com data de ativação igual ou superior ao valor informado no parâmetro, será desativada automaticamente no horário de execução.

| Funcionalidades da tela | |
| --- | --- |
| [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#configuraes) | [Aba Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos) |
| [Aba Seleção de títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#sele%C3%A7ao) | [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#botooutrasopes...) |

---

![Imagem 1: Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/4412669736855)

### Configurações

Inicialmente, são fundamentais algumas configurações no sistema para começar a construção da **Régua de Cobrança.**

#### Conta SMS

Na tela [Conta SMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109313-Conta-SMS) será definida a plataforma de comunicação que será aplicada no envio de SMS.

![Imagem 2: Na tela Conta SMS será definida a plataforma de comunicação que será aplicada no envio de SMS.](https://ajuda.sankhya.com.br/hc/article_attachments/4412669795479)

#### Grupo Cobrança

A tela [Grupo Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108313-Grupo-Cobran%C3%A7a) possibilitará a criação de Grupos de Cobrança a fim de realizar a segmentação dos Parceiros de acordo com o seu nível de inadimplência.

![Imagem 3: A tela Grupo Cobrança possibilitará a criação de Grupos de Cobrança a fim de realizar a segmentação dos Parceiros de…](https://ajuda.sankhya.com.br/hc/article_attachments/4412669817367)

#### Modelo de E-mail

Através da tela [Modelo de E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133-Modelo-de-E-mail), configure os modelos de e-mail que serão utilizados.

![Imagem 4: Através da tela Modelo de E-mail , configure os modelos de e-mail que serão utilizados.](https://ajuda.sankhya.com.br/hc/article_attachments/4412669862039)

No Modelo de E-mail, insira a tag IMGLINK que pretende encaminhar como anexo. Para enviar a imagem nesse formato, será necessário acrescentar o link da imagem na seguinte estrutura de tag:

${IMGLINK[link da imagem]} (cifão; abre chave; tag IMGLINK, abre colchete, link da imagem, fecha colchete, fecha chave).

Observe abaixo o exemplo de uma imagem com a seguinte URL: [https://portalerp.com/images/2021/02/10/logo-sankhya-novopng.png](https://portalerp.com/images/2021/02/10/logo-sankhya-novopng.png "https://portalerp.com/images/2021/02/10/logo-sankhya-novopng.png").

Ao enviar esta imagem será necessário ser informada a tag ${IMGLINK[link da imagem]} no **"Conteúdo"** do Modelo de E-mail da seguinte forma:

${IMGLINK[[https://portalerp.com/images/2021/02/10/logo-sankhya-novopng.png]}](https://portalerp.com/images/2021/02/10/logo-sankhya-novopng.png%5D%7D%E2%80%9D "https://portalerp.com/images/2021/02/10/logo-sankhya-novopng.png%5D%7D%E2%80%9D").

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#top)

### Aba Eventos

Esta aba permite a criação/configuração e duplicar os eventos conforme o processo de cobrança adotado pela empresa.

![Imagem 5: Esta aba permite a criação/configuração e duplicar os eventos conforme o processo de cobrança adotado pela empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/35946011624727)

Clique em **"+ Adicionar evento"** para seleção do evento desejado:

| [Envio de E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#enviodee-mail) | [Envio de SMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#enviodesms) |
| --- | --- |
| [Transferência de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#transfernciadedados) | [Envio de WhatsApp](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#01JRZ6VWAM1WHYNZHHFFRATWG6) |
| [Alerta/Bloqueio de venda à prazo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#alertabloqueiodevendaprazo) | [Registro de Contato p/ cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#registrodecontatopcobrana) |
| [Ação Programada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#aoprogramada) | [Agenda de recursos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#agendaderecursos) |

---

Quando a opção **"Duplicar"** for utilizada, as informações do evento existente serão copiadas para o novo evento, e a descrição **"Cópia de"** será adicionada no campo **"Descrição"** do pop-up do evento.

#### Envio de E-mail

O e-mail é enviado ao Contato do Parceiro que possui a marcação "Responsável pela cobrança" habilitada na sub-aba Geral, aba **Contatos** do **Cadastro de Parceiros**.

![Imagem 6: O e-mail é enviado ao Contato do Parceiro que possui a marcação "Responsável pela cobrança" habilitada na sub-aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4412927769111)

O campo **"Descrição"** será preenchido com o nome do evento. Esse nome será apresentado na Régua de Cobrança quando o mouse estiver posicionado em cima do evento.

Por meio do campo **"Acontece"**, determine em qual momento o evento será disparado. Temos as seguintes opções:

- Antes do vencimento: Informa-se o número de dias antes do vencimento;
- **No vencimento**;
- **Após o vencimento:** Será indicado o número de dias após o vencimento;
- **Ao baixar**;
- **Filtro Personalizado**.

**Nota:** com a opção Ao baixar selecionada, assim que o título for baixado tem-se a execução do evento configurado. Sendo que, ao baixar um título que possui uma baixa com data futura; o envio do evento será realizado no ato da baixa antecipada.

**Observação:** se a opção **"Filtro Personalizado"** estiver selecionada, a aba **"Filtro"** se torna de preenchimento obrigatório, ou seja, o sistema não permitirá que você acione o botão **"Concluir"** do Evento de E-mail sem configurar um filtro, sendo ele que determinará a data de quando acontecerá o evento.

Quando a marcação **"Executar apenas em dias úteis"** for habilitada, o sistema irá disparar o evento apenas em dias úteis, ou seja, o evento será executado apenas nos dias que não são feriados e finais de semana. De outro modo, quando esta for desmarcada, o sistema enviará o e-mail em qualquer dia da semana.

**Nota:** se tratando de feriados, estes deverão ser cadastrados conforme orientação do artigo [Feriados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603274-Feriados). Já no caso dos finais de semana será necessário que os parâmetros **"Folga no Sábado? - FOLGASAB"** e **"Folga no Domingo? - FOLGADOM"** estejam ligados na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).

Nesta etapa serão configurados os dados pertinentes aos destinatários deste evento:

![Imagem 7: Nesta etapa serão configurados os dados pertinentes aos destinatários deste evento:](https://ajuda.sankhya.com.br/hc/article_attachments/4412669989271)

Essa aba permite indicar se o evento enviará o e-mail para o Parceiro, Contato do Parceiro ou para o Vendedor. Além disso, a aba **"Outros e-mails"** possibilitará a inclusão de outros e-mails para recebimento.

Esse e-mail será enviado considerando a seguinte regra:

Será enviado para o **Contato** do **Parceiro** que possuir a marcação **"Responsável pela cobrança"** habilitada na sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#sub-abageral), aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacontatos) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494).

**⚠️ Atenção**

Valide se o contato principal de cobrança possui a marcação **Responsável pela cobrança**. Sem essa marcação, o e-mail não é enviado, mesmo que o contato tenha a marcação **Recebe boleto/Pix p/ email**.

Se nenhum contato atender à condição acima, **nenhuma mensagem será enviada.**

Na próxima etapa tem-se os dados relacionados ao conteúdo do e-mail:

![Imagem 8: Na próxima etapa tem-se os dados relacionados ao conteúdo do e-mail:](https://ajuda.sankhya.com.br/hc/article_attachments/4412669997207)

É necessário apontar qual será o **"Modelo do corpo do e-mail"**, previamente cadastrado na tela [Modelo de E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133-Modelo-de-E-mail).

Preencha o campo **"Responder para"** para realizar o envio do e-mail para uma só pessoa quando o remetente responder ao e-mail enviado.

**Observação:** caso você faça a marcação **"Usar modelo"** ao lado do campo Responder para, será utilizado o e-mail informado no campo **"Responder para"** do [Modelo de E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133-Modelo-de-E-mail) (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110133-Modelo-de-E-mail#abageral)) para que o destinatário possa responder.

O campo **"Assunto"** irá comportar o objetivo do e-mail. Sendo que, é possível utilizar variáveis para construí-lo.

No campo **"Conta SMTP"**, obtém-se a conta que será responsável pelo envio do e-mail, sendo que a mesma deve estar previamente configurada na tela [Contas SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP). Além disso, é possível utilizar a conta SMTP configurada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa).

**Nota:** pode-se utilizar os dados Responder para, Assunto e Conta SMTP configurados no Modelo de E-mail.

Essa etapa auxiliará na utilização/inclusão de anexos no envio do e-mail:

![Imagem 9: Essa etapa auxiliará na utilização/inclusão de anexos no envio do e-mail:](https://ajuda.sankhya.com.br/hc/article_attachments/4412670002071)

A marcação **"Anexar boleto"** será acionada quando for necessário que os boletos sejam enviados anexados ao e-mail.

O campo **"Anexar notas fiscais relacionadas"** permite determinar se será enviado no anexo do e-mail o PDF do DANFE, o XML da NF-e ou Ambos; quando o título for originado de uma nota venda.

Ao efetuar a marcação **"Um relatório para todos os títulos"** tem-se que o relatório formatado será gerado e enviado apenas uma vez, com todos os anexos em um único arquivo.

Ao indicar um **"Relatório formatado"**, o mesmo será enviado como um anexo do e-mail.

**Importante:** atenção Consultores e Implantadores: Tratando-se do Relatório formatado, a régua passa como filtro os campos CODREGUA, CODEVENTO, DIAEXEC e os campos da TGFFIN que estiverem sendo solicitados no relatório.

Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento, podendo ainda utilizar filtros específicos nesta pesquisa:

![Imagem 10: Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento,…](https://ajuda.sankhya.com.br/hc/article_attachments/4412670006039)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos)

#### \*\*\*\*Envio de SMS

Este evento possibilita o envio de um SMS contendo uma mensagem em relação ao(s) título(s) em aberto ou aqueles que foram baixados. Para a utilização deste evento, as configurações de integração com a plataforma [Infobip](https://www.infobip.com/pt?utm_source=google&utm_medium=cpc&utm_term=infobip&utm_network=g&utm_matchtype=e&utm_campaign=act%20--%20gsn%20--%20latam%20south%20--%20brazil%20--%20lead%20generation%20-%20brand&utm_adgroup=brand%20--%20native%20--%20e&gclid=EAIaIQobChMIpc-mmenF4gIVBw2RCh0_dAneEAAYASAAEgIhSvD_BwE) ou as definições do Modem nativo necessitam ser previamente realizadas.

![Imagem 11: Este evento possibilita o envio de um SMS contendo uma mensagem em relação ao(s) título(s) em aberto ou aqueles que…](https://ajuda.sankhya.com.br/hc/article_attachments/4412662668695)

O campo **"Descrição"** será preenchido com o nome do evento. Este nome será apresentado na Régua de Cobrança quando o mouse estiver posicionado em cima do evento.

Através do campo **"Acontece"**, determina-se em qual momento o evento será disparado. Tem-se as seguintes opções:

- **Antes do vencimento:** Informa-se o número de dias antes do vencimento;
- **No vencimento**;
- **Após o vencimento:** Será indicado o número de dias após o vencimento;
- **Ao baixar**.

**Nota:** optando-se pela opção Ao baixar, assim que o título for baixado tem-se a execução do evento configurado. Sendo que, ao baixar um título que possui uma baixa com data futura; o envio do evento será realizado no ato da baixa antecipada.

Através desta etapa, determina-se qual será a plataforma de envio de SMS a ser utilizada. Pode-se optar pela integração com a **"Infobip"** ou a utilização do **"MODEM"**.

![Imagem 12: Através desta etapa, determina-se qual será a plataforma de envio de SMS a ser utilizada. Pode-se optar pela integração…](https://ajuda.sankhya.com.br/hc/article_attachments/4412662758679)

Nesta etapa serão configurados os dados pertinentes aos destinatários deste evento:

![Imagem 13: Nesta etapa serão configurados os dados pertinentes aos destinatários deste evento:](https://ajuda.sankhya.com.br/hc/article_attachments/4412662768023)

Esta aba permite indicar se o evento enviará o e-mail para o Parceiro, Contato do parceiro ou para o Vendedor. Além disso, a aba **"Outros e-mails"** possibilitará a inclusão de outros e-mails para recebimento deste e-mail.

Tem-se nesta etapa as informações a respeito do conteúdo da mensagem:

![Imagem 14: Tem-se nesta etapa as informações a respeito do conteúdo da mensagem:](https://ajuda.sankhya.com.br/hc/article_attachments/4412670165143)

O campo **"Mensagem"** contém algumas variáveis que podem ser utilizadas na formatação do texto. Sendo elas:

- **Títulos:** &{LISTA\_TITULOS};

**Nota:** por padrão, a váriavel acima exibe os campos **"Data de Vencimento"**, **"Valor Líquido"**, **"Linha Digítavel"** e **"Número Único do Financeiro"**. Porém, é possível editá-la colocando à sua frente determinados campos da tabela TGFFIN. Desse modo, observe o exemplo:

&{LISTA\_TITULOS:NUMNOTA=Nro da Nota,DTNEG=Data da Emissão,DESDOBRAMENTO=Parcela,  DTVENC=Vencimento,VLRDESDOB=Valor}

Dados do título:

| **Nro da Nota** | **Data da Emissão** | **Parcela** | **Vencimento** | **Valor** |
| --- | --- | --- | --- | --- |
| 100 | 10/08/2023 | 1 | 17/08/2023 | 100,00 |

- **Email empresa:** &{EMAIL\_EMPRESA};
- **Nome empresa:** &{NOME\_EMPRESA};
- **Razão social empresa:** &{RAZAO\_SOCIAL\_EMPRESA};
- **Nome parceiro:** &{NOME\_PARCEIRO};
- **Total de débito:** &{TOTAL\_DEBITO};
- **CNPJ do parceiro:** &{CPFCNPJ\_PARCEIRO};
- **CNPJ da empresa:** &{CNPJ\_EMPRESA};
- **Quantidade de títulos:** &{QTD\_TITULOS};
- **Linha digitável:** &{LINHA\_DIGITAVEL}.

Ao final, tem-se a etapa onde será possível simular e verificar quais serão os títulos que se encaixarão neste evento. Podendo também utilizar filtros específicos nessa pesquisa.

![Imagem 15: Ao final, tem-se a etapa onde será possível simular e verificar quais serão os títulos que se encaixarão neste evento.…](https://ajuda.sankhya.com.br/hc/article_attachments/4412653252631)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos)

#### \*\*\*\*Envio de WhatsApp

Envie mensagens de cobrança de forma automática, usando o WhatsApp integrado à **Régua de Cobrança** com o evento **Envio de WhatsApp**.

#### Pré-requisitos

- Ter acesso à Régua de Cobrança no Sankhya Om.
- Contratar o serviço de envio de WhatsApp via [Neppo.](https://www.sankhya.com.br/software-de-gestao-erp/erp-para-gestao-de-vendas/produtos/neppo/)
- Possuir as credenciais de integração fornecidas pela [Neppo](https://www.sankhya.com.br/software-de-gestao-erp/erp-para-gestao-de-vendas/produtos/neppo/) após a ativação.
- ![Imagem 16: Ter o produto WhatsApp na sua licença (conforme imagem).](https://ajuda.sankhya.com.br/hc/article_attachments/36549093285911) Ter o produto WhatsApp na sua licença (conforme imagem).

![Imagem 17: Ter o produto WhatsApp na sua licença (conforme imagem).](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEWv8GSH3d3fw2y7KHj7fIOCM8lruEo8KyjBQMM753S9YOIdrlPMznI1OODOa%2BD6sgrsStKmZS8RgIr%2FPtyxzbvpU2a4kBtTgIAv2ZxpNrMEcYGS%2BbDZvCkNpbcrR8kXPLqv%2Fv60iexCO%2BUI6%2B0XTtWSBROtTr%2BUDM1X%2FC76etVmcoZtA1XgevRQ%2Fx8i%2FpGLrqBX1ZSIHyBQn8vuenVq1sLCxex8rdvcx0nxmo4qxtPe7F9X23GgBe8a2RigES2AmYU%2BpazjDr6AFbRz2bRXRBGmhT7BEyOl%2BGVx5c0kti7D3CAv6uiTEGAgR53ILDgGfgJGZvMzY%2BALhrffcOiUHZo4WjggQy%2BfVnVN2Zong1yX%2BDIxWapQVf4fMH1IKnpJp%2FlavSzoNlcNqTrRmzWs%2Bm6Xk7%2BtaC99DSPPR9Zk6yeyl67WHTv2ShwtSeGX6VchdbgvoYS7WZnZT5XVg70Md8ku9ct2ClGXAQQTq8RoG7G5%2FbxHK9XhZPr6%2Fk1fH62W%2FF1oE6VKjBxH8hVQYxSpClF889JHjP8TlL4QRO73qQ2091dGhOhK45cambx6mvIbQgzUUgWA71dBXyIZ%2Bw%3D%3D&allow_caching=true&sz=w1559-h923-rw)

Se não tiver o produto na licença, esta configuração não é aberta:

![Imagem 18: Se não tiver o produto na licença, esta configuração não é aberta:](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEVcT5xORH%2BAY%2BkVvDlipU3Wz9sRuX3ef%2B3DL0t1cBrZJ7q7Qoi7wMzsqtOgBhqaeLUj8nF4EqfXHmpOT%2B4BB%2FMvorbbY2s3R6TS4hmxAnTq%2B%2B7hhLfASVT3jnanahh74fbjlgMgSt5tEyxFLRomljwa8bjV6ykgzlcCE5uBnFWjvRWn8CUNCLSkVtLu%2FfgkHP7E8zSFUVoh%2FpHZGsTzql9suXTkFcJqvp0%2BL%2BPkUeIg%2FoyKxmeySA3hv9IXy%2BkXQlg1eemo9YRExPnRd00iHpeO3%2FdyZJ19kKnDOc4w5SkU%2B6uPr6FQcF%2FSlOtQmo3SPGAvU5XOkqOGxYvd1huAsXB%2BP%2BFGASi43lz3suAU4s3RkzzaETyp01IV8NKGHwD%2FFncYokDBbmJ%2B8agi3HmRY6QKj7pkK5NKTU3fEMZPTxG6EklH2OTe98LAD4wRAIaf2HqRqk7b6I2d5Gl7Gc91gXHnw8%2Fv7nOl2swvIPb%2FUyclUTTdXyMCVFqNBS46%2Fwng9RQ6QterikytsE0bqYwvLkww%2FUPDwHzCs0pVZmXtwM8NI9u55oN0WkOdjyqw6pTB60yJkOHRzwSljP7rYznjstE%3D&allow_caching=true&sz=w1559-h923-rw)

#### Contratação do serviço WhatsApp na régua de cobrança

1. Acesse a **Régua de Cobrança**
2. Clique em **Eventos** > **Adicionar Evento**
3. Selecione o evento **Envio de WhatsApp**
4. Clique em **Avançar** na janela de apresentação do serviço
5. Preencha os campos do formulário
6. Aguarde o contato da equipe comercial para finalizar a contratação

![Imagem 19: Aguarde o contato da equipe comercial para finalizar a contratação](https://ajuda.sankhya.com.br/hc/article_attachments/35946011626135)

#### Configuração do evento Envio por WhatsApp

1. Acesse o menu **Régua de Cobrança**
2. Selecione o evento **Envio de WhatsApp**
3. Insira as credenciais de integração
4. Informe os dados fornecidos pela [Neppo](https://www.sankhya.com.br/software-de-gestao-erp/erp-para-gestao-de-vendas/produtos/neppo/)
5. Clique em **Salvar Credenciais** para concluir e deixar o evento disponível na **Régua de Cobrança**

![Imagem 20: Clique em Salvar Credenciais para concluir e deixar o evento disponível na Régua de Cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/35946011628311)

#### Obter credenciais da Neppo

1. Acesse no ambiente Neppo **Integrações > Neppo Token API > Gerar credenciais**
2. Insira as credenciais: Chave do Consumidor, Senha do Consumidor, Usuário, Senha.
3. Copie e cole as informações no ERP.
4. Prossiga para configurar o envio das cobranças via Whatsapp.

[GIF animado: Imagem 21: Prossiga para configurar o envio das cobranças via Whatsapp.](https://ajuda.sankhya.com.br/hc/article_attachments/31462260400535)

#### Templates

![Imagem 22: Entre em contato com o time da Neppo para obter suporte na configuração dos templates e campanhas.](https://ajuda.sankhya.com.br/hc/article_attachments/27769807334423) Entre em contato com o time da Neppo para obter suporte na configuração dos templates e campanhas.

Para que o serviço funcione corretamente, certifique-se que os templates:

- Estejam corretamente cadastrados no broker de whatsapp.
- Sejam validados junto à Meta (WhatsApp).
- Estejam cadastrados na Neppo. Para acessar, siga: Home > Template de campanha

**(2)**Todos os templates de envio devem ser previamente parametrizados na plataforma Neppo de acordo com a campanha criada. Para acessar a tela, siga: **Home > Campanha**.

São necessários:

- Templates para envio com **anexos** (como boleto ou PDF);
- Templates para envio **sem anexos**, sendo que **um deles deve conter o ID 999999999**.

![Imagem 23: Templates para envio sem anexos , sendo que um deles deve conter o ID 999999999 .](https://ajuda.sankhya.com.br/hc/article_attachments/31463284320919)

**Exemplo de template:**

| Prezado cliente &{NOME\_PARCEIRO},  Sua(s) fatura(s) está(ão) se aproximando do vencimento.  Dados do título(s):  &Número\_Nota  Qualquer dúvida, entre em contato conosco respondendo esta mensagem. |
| --- |

#### Etapas da configuração do envio

Após a autenticação, ao configurar o evento **Envio de WhatsApp**, siga as etapas abaixo:

#### Evento

- Informe a **Descrição do evento** (texto que será exibido ao passar o mouse sobre o ícone na régua).
- Defina se deseja **enviar anexo**:
  - Não Enviar;
  - PDF do DANFE;
  - Anexar Boleto.

**Observação**: a Meta não permite mais de um anexo por mensagem. Portanto, **não é permitido enviar boleto e PDF no mesmo evento**.

- No campo **Mensagem para envio de WhatsApp (Template de mensagens Neppo)**, será exibida a lista de templates cadastrados na Neppo para o parceiro. Selecione o template desejado.

![Imagem 24: A lista de templates é carregada automaticamente da Neppo. Ao criar novos templates, utilize o botão "Atualizar" .](https://ajuda.sankhya.com.br/hc/article_attachments/27769807334423) A lista de templates é carregada automaticamente da Neppo. Ao criar novos templates, utilize o botão **"Atualizar"**.

A seleção do template depende do tipo de anexo:

- **PDF do DANFE** ou **Anexar Boleto** → exige templates com variáveis de anexo;
- **Não Enviar** → permite apenas templates sem variáveis de anexo.
- No campo **Acontece**, defina o momento do disparo:
  - Antes do vencimento (informe o número de dias);
  - No vencimento;
  - Após o vencimento (informe o número de dias);
  - Ao baixar (quando o título for baixado).
- Marque a opção **Executar apenas em dias úteis**, se necessário.
- Avance clicando em **"Próximo"**.

**Destinatários**

Selecione o(s) destinatário(s) da cobrança:

- **Parceiro**: utiliza o número do campo **Celular/Fax** da aba **Endereço** do **Cadastro de Parceiros**;
- **Contato do parceiro**: utiliza o número do campo **Celular** da aba **Contatos**, sub-aba **Geral**, conforme as regras para envio.

![Etapa Destinatários do evento Envio de WhatsApp com as opções Parceiro e Contato do parceiro](https://ajuda.sankhya.com.br/hc/article_attachments/31452560316951)

Na opção **Parceiro**, preencha o campo **Celular/Fax** com DDD e número, sem o código do país. No evento **Envio de WhatsApp**, o campo **Telefone** não é usado.

![Aba Endereço do Cadastro de Parceiros com o campo Celular/Fax](https://ajuda.sankhya.com.br/hc/article_attachments/44450540901015)

**Regras para envio**

Na opção **Contato do parceiro**, a mensagem segue esta ordem:

1. Envia para todos os contatos **ativos** com número de celular preenchido e com a marcação **Responsável pela cobrança**.
2. Se não houver, envia para o primeiro contato **ativo** com celular preenchido e marcação **Recebe boleto/Pix p/ email**.
3. Se nenhum contato atender às condições acima, nenhuma mensagem é enviada.

![Sub-aba Geral da aba Contatos do Cadastro de Parceiros com a marcação Responsável pela cobrança destacada](https://ajuda.sankhya.com.br/hc/article_attachments/44412200627479)

**⚠️ Atenção**

Sem o número preenchido no parceiro ou no contato, a mensagem não é enviada, e a tela **Histórico da Régua de Cobrança** registra o erro "Erro ao enviar whatsapp. Não foram encontrados dados de destinatário para o respectivo título". Antes de abrir um chamado, confira o Histórico e o cadastro do parceiro e dos contatos. Para saber mais, acesse [Erro ao enviar whatsapp. Não foram encontrados dados de destinatário para o respectivo título](https://ajuda.sankhya.com.br/hc/pt-br/articles/36594355994007).

**Teste de conexão**

Essa etapa verifica se as credenciais estão corretas e permite validar a conexão com a API da Neppo.

![Imagem 28: Essa etapa verifica se as credenciais estão corretas e permite validar a conexão com a API da Neppo.](https://ajuda.sankhya.com.br/hc/article_attachments/31452513709207)

Para realizar o teste:

1. Preencha o campo **Destinatário** com um número de telefone (com DDD);
2. Informe um **Número Único Financeiro** válido (utilizado para buscar variáveis da mensagem);
3. Clique no botão **"Testar conexão"**.

Se a conexão com a API for bem-sucedida, será exibida a mensagem:

**"Sucesso: Conexão da API bem-sucedida"**

\_![Imagem 29: _ _Este teste valida apenas a entrega da mensagem para a Neppo, não garante a entrega final via WhatsApp (Meta).](https://ajuda.sankhya.com.br/hc/article_attachments/27769807334423)\_Este teste valida apenas a entrega da mensagem para a Neppo, não garante a entrega final via WhatsApp (Meta).

**Filtro**

Nesta etapa, você pode aplicar **filtros específicos** conforme as regras de cobrança da empresa.

![Imagem 30: Nesta etapa, você pode aplicar filtros específicos conforme as regras de cobrança da empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/31452513711255)

Ao clicar em  **"Testar resultado"**, será exibido um pop-up para informar a **Data de execução**. Após aplicar, o sistema listará os títulos que seriam considerados para envio de cobrança naquela data.

Finalize clicando em **"Concluir"**, e o evento será incluído na régua de cobrança.

**Como editar suas credenciais**

1. Acesse o menu **Régua de Cobrança**
2. Selecione o evento **Envio de WhatsApp**
3. Clique em **Alterar Credenciais**
4. Atualize as informações
5. Clique em **Salvar Credenciais** para concluir

![Imagem 31: Clique em Salvar Credenciais para concluir](https://ajuda.sankhya.com.br/hc/article_attachments/35945967590935)

#### **(1)** Exemplo prático

Imagine uma régua com os seguintes eventos configurados:

- **Envio de WhatsApp:** 3 dias antes do vencimento;
- **Envio de e-mail:** no vencimento;
- **Envio de SMS:** 3 dias após o vencimento.

![Imagem 32: Envio de SMS: 3 dias após o vencimento.](https://ajuda.sankhya.com.br/hc/article_attachments/31452560323223)

Na execução do evento, serão enviados à Neppo os seguintes dados para cada cobrança:

- Número Único Financeiro
- Telefone do destinatário
- Número da nota
- Data de vencimento
- Valor líquido
- Linha digitável
- E-mail da empresa
- Nome da empresa
- CNPJ da empresa
- Razão Social da empresa
- Nome do parceiro
- CNPJ do parceiro
- Template selecionado

A Neppo processará essas informações, substituirá as variáveis no template e enviará a mensagem ao cliente.

**Observação:** o envio ocorre por **número financeiro/destinatário**. Por exemplo:

- Nota 10 → financeiro 112425 → parceiro Joseph → telefone (34) 99999-9999
- Nota 11 → financeiro 112427 → parceiro Joseph → telefone (34) 99999-9999
  Resultado: **duas mensagens serão enviadas**, contabilizando **dois disparos ativos**.

![Imagem 33: Nota 11 → financeiro 112427 → parceiro Joseph → telefone (34) 99999-9999 Resultado: duas mensagens serão enviadas ,…](https://ajuda.sankhya.com.br/hc/article_attachments/31452513712919)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos)

#### \*\*\*\*Transferência de Dados

Este evento permite efetuar a transferência de arquivos diretamente para um FTP, Diretório ou Envio por e-mail.

![Imagem 34: Este evento permite efetuar a transferência de arquivos diretamente para um FTP, Diretório ou Envio por e-mail.](https://ajuda.sankhya.com.br/hc/article_attachments/4412653261079)

O campo **"Descrição"** será preenchido com o nome do evento. Este nome será apresentado na Régua de Cobrança quando o mouse estiver posicionado em cima do evento.

Através do campo **"Acontece"**, determina-se em qual momento o evento será disparado. Tem-se as seguintes opções:

- **Antes do vencimento:** Informa-se o número de dias antes do vencimento;
- **No vencimento**;
- **Após o vencimento:** Será indicado o número de dias após o vencimento;
- **Ao baixar**.

**Observação:** optando-se pela opção Ao baixar, assim que o título for baixado tem-se a execução do evento configurado. Sendo que, ao baixar um título que possui uma baixa com data futura; o envio do evento será realizado no ato da baixa antecipada.

Nesta etapa serão apontados os dados relacionados ao layout de transferência dos dados:

![Imagem 35: Nesta etapa serão apontados os dados relacionados ao layout de transferência dos dados:](https://ajuda.sankhya.com.br/hc/article_attachments/4412670193175)

No campo **"Layout"** será informado o layout utilizado para geração do arquivo. Sendo que, o mesmo necessita estar previamente cadastrado na tela [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054-Layout-de-Processamento-de-Arquivo).

Tem-se no campo **"Nome do arquivo"** a descrição que identifica o arquivo, sendo possível utilizar variáveis para compor a mesma. Pode-se ainda, utilizar o nome definido no layout do arquivo.

Esta etapa contém as configurações pertinentes ao destino de geração do arquivo:

![Imagem 36: Esta etapa contém as configurações pertinentes ao destino de geração do arquivo:](https://ajuda.sankhya.com.br/hc/article_attachments/4412653269399)

![Imagem 37: Envio por E-mail: Este botão permite o envio do arquivo por e-mail, utilizando as mesmas opções de configuração do…](https://ajuda.sankhya.com.br/hc/article_attachments/15411362322327) **Envio por E-mail:** Este botão permite o envio do arquivo por e-mail, utilizando as mesmas opções de configuração do evento [Envio de E-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#enviodee-mail).

![Imagem 38: Endereço FTP: Utiliza-se este botão para executar a configuração de um FTP, neste caso é necessário informar os dados…](https://ajuda.sankhya.com.br/hc/article_attachments/15411319214743) **Endereço FTP:** Utiliza-se este botão para executar a configuração de um FTP, neste caso é necessário informar os dados obrigatórios para conexão com o FTP.

![Imagem 39: Diretório de destino: O arquivo será gerado no diretório do repositório de arquivos, que pode ser acessado através da…](https://ajuda.sankhya.com.br/hc/article_attachments/15411362325015) **Diretório de destino:** O arquivo será gerado no diretório do repositório de arquivos, que pode ser acessado através da tela [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos).

![Imagem 40: Editar destino: Este botão permite realizar a edição do destino configurado.](https://ajuda.sankhya.com.br/hc/article_attachments/16746208743191) **Editar destino:** Este botão permite realizar a edição do destino configurado.

![Imagem 41: Remover destino: Através deste botão, tem-se a exclusão do destino.](https://ajuda.sankhya.com.br/hc/article_attachments/16746194585367) **Remover destino:** Através deste botão, tem-se a exclusão do destino.

Ao final, tem-se a etapa onde será possível simular e verificar quais serão os títulos que se encaixarão neste evento. Podendo também utilizar filtros específicos nesta pesquisa.

![Imagem 42: Ao final, tem-se a etapa onde será possível simular e verificar quais serão os títulos que se encaixarão neste evento.…](https://ajuda.sankhya.com.br/hc/article_attachments/4412653274263)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos)

#### Registro de Contato p/ cobrança

Este evento tem como característica a inclusão de um registro de contato destinado ao time de cobrança, como por exemplo, um contato via telefone. O registro incluído poderá ser visualizado através da tela [Gerência de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606894-Ger%C3%AAncia-de-Cobran%C3%A7a), aba **"Histórico cobrança"**.

![Imagem 43: Este evento tem como característica a inclusão de um registro de contato destinado ao time de cobrança, como por…](https://ajuda.sankhya.com.br/hc/article_attachments/4412670227351)

O campo **"Descrição"** será preenchido com o nome do evento. Este nome será apresentado na Régua de Cobrança quando o mouse estiver posicionado em cima do evento.

Através do campo **"Acontece"**, determina-se em qual momento o evento será disparado. Tem-se as seguintes opções:

- **Antes do vencimento:** Informa-se o número de dias antes do vencimento;
- **No vencimento**;
- **Após o vencimento:** Será indicado o número de dias após o vencimento;
- **Ao baixar**.

**Nota:** optando-se pela opção Ao baixar, assim que o título for baixado tem-se a execução do evento configurado. Sendo que, ao baixar um título que possui uma baixa com data futura; o envio do evento será realizado no ato da baixa antecipada.

Tem-se nesta etapa os dados relacionados ao responsável pelo contato para cobrança:

![Imagem 44: Tem-se nesta etapa os dados relacionados ao responsável pelo contato para cobrança:](https://ajuda.sankhya.com.br/hc/article_attachments/4412670233367)

O campo **"Ocorrências"** comportará os tipos de ocorrências que podem caracterizar o contato para cobrança. Lembre-se ainda que, o cadastro dessas Ocorrências pode ser realizado na tela [Histórico de Telemarketing/Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112953-Hist%C3%B3rico-de-Telemarketing-Cobran%C3%A7a).

Define-se no campo **"Executante"**, qual usuário irá receber o registro de contato para que seja realizada a ação necessária.

No campo **"Dias para agendamento"**, determina-se quantos dias após a execução do evento será agendada a cobrança.

Informa-se nesta etapa o assunto pelo qual está acontecendo o contato de cobrança:

![Imagem 45: Informa-se nesta etapa o assunto pelo qual está acontecendo o contato de cobrança:](https://ajuda.sankhya.com.br/hc/article_attachments/4412676365591)

O campo **"Observação"** contém algumas variáveis que podem ser utilizadas na formatação do texto. São elas:

- **Email empresa:** &{EMAIL\_EMPRESA};
- **Nome empresa:** &{NOME\_EMPRESA};
- **Razão social empresa:** &{RAZAO\_SOCIAL\_EMPRESA};
- **Nome parceiro:** &{NOME\_PARCEIRO};
- **Total de débito:** &{TOTAL\_DEBITO};
- **CNPJ do parceiro:** &{CPFCNPJ\_PARCEIRO};
- **CNPJ da empresa:** &{CNPJ\_EMPRESA};
- **Quantidade de títulos:** &{QTD\_TITULOS}.

Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento. Podendo também utilizar filtros específicos nesta pesquisa.

![Imagem 46: Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento.…](https://ajuda.sankhya.com.br/hc/article_attachments/4412670550935)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos)

#### \*\*\*\*Alerta/Bloqueio de venda a prazo

Utiliza-se este evento nas situações em que o cliente já se encontra em um nível elevado de inadimplência necessitando assim de um alerta ou do seu bloqueio para vendas a prazo.

![Imagem 47: Utiliza-se este evento nas situações em que o cliente já se encontra em um nível elevado de inadimplência necessitando…](https://ajuda.sankhya.com.br/hc/article_attachments/4412663100695)

O campo **"Descrição"** será preenchido com o nome do evento. Este nome será apresentado na Régua de Cobrança quando o mouse estiver posicionado em cima do evento.

Através do campo **"Acontece"**, determina-se em qual momento o evento será disparado. Tem-se as seguintes opções:

- **Antes do vencimento:** Informa-se o número de dias antes do vencimento;
- **No vencimento**;
- **Após o vencimento:** Será indicado o número de dias após o vencimento;
- **Ao baixar**.

**Observação:** optando-se pela opção Ao baixar, assim que o título for baixado tem-se a execução do evento configurado. Sendo que, ao baixar um título que possui uma baixa com data futura; o envio do evento será realizado no ato da baixa antecipada.

![Imagem 48: Observação: optando-se pela opção Ao baixar, assim que o título for baixado tem-se a execução do evento configurado.…](https://ajuda.sankhya.com.br/hc/article_attachments/4412670571415)

A marcação **"Bloquear venda a prazo"** quando acionada, tem-se o bloqueio do parceiro tratando-se de vendas a prazo. A mensagem informada será registrada no [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610034-Parceiro).

![Imagem 49: Atenção: a Régua de Cobrança não desbloqueia o parceiro automaticamente. Mesmo após a baixa dos títulos em atraso, o…](https://ajuda.sankhya.com.br/hc/article_attachments/27769807334423) **Atenção:** a Régua de Cobrança não desbloqueia o parceiro automaticamente. Mesmo após a baixa dos títulos em atraso, o parceiro continua bloqueado para vendas a prazo, e um evento configurado como Ao baixar também não remove o bloqueio.

Para liberar novas vendas a prazo:

1. Acesse a tela **Parceiros** e selecione o parceiro.
2. Abra a aba **Crédito** e desmarque **"Bloquear venda a prazo"**.
3. Salve a alteração.

Não é necessário apagar o conteúdo do campo **"Motivo de Bloqueio"**. Para fazer o desbloqueio, você precisa ter permissão para alterar o **Cadastro de Parceiros** no **Controle de Acessos**.

Tanto a mensagem quanto a marcação são opcionais, ou seja, pode-se registrar apenas um deles ou ambos.

Quando a marcação **"Adicionar mensagem ao conteúdo do campo motivo de bloqueio"** estiver habilitada, se ao rodar a régua o campo **"Motivo de Bloqueio"** ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacrdito)) estiver preenchido, o sistema irá adicionar o seu conteúdo junto à mensagem do evento.

Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento. Podendo também utilizar filtros específicos nesta pesquisa.

![Imagem 50: Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento.…](https://ajuda.sankhya.com.br/hc/article_attachments/4412670576151)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos)

#### Agenda de recursos

Este evento dispõe de um recurso que permite inserir na agenda diária dos usuários os momentos em que os mesmos deverão realizar o contato de cobrança.

![Imagem 51: Este evento dispõe de um recurso que permite inserir na agenda diária dos usuários os momentos em que os mesmos deverão…](https://ajuda.sankhya.com.br/hc/article_attachments/4412663159959)

O campo **"Descrição"** será preenchido com o nome do evento. Este nome será apresentado na Régua de Cobrança quando o mouse estiver posicionado em cima do evento.

Através do campo **"Acontece"**, determina-se em qual momento o evento será disparado. Tem-se as seguintes opções:

- **Antes do vencimento:** Informa-se o número de dias antes do vencimento;
- **No vencimento**;
- **Após o vencimento:** Será indicado o número de dias após o vencimento;
- **Ao baixar**.

**Nota:** optando-se pela opção Ao baixar, assim que o título for baixado tem-se a execução do evento configurado. Sendo que, ao baixar um título que possui uma baixa com data futura; o envio do evento será realizado no ato da baixa antecipada.

![Imagem 52: Nota: optando-se pela opção Ao baixar, assim que o título for baixado tem-se a execução do evento configurado. Sendo…](https://ajuda.sankhya.com.br/hc/article_attachments/4412676444567)

Através do campo **"Executante"**, determina-se qual é o funcionário que irá efetuar o contato com o cliente.

Os campos **"Início"** e **"Intervalo"** serão preenchidos com a hora em que se iniciará o contato e o intervalo entre um contato e outro.

A marcação **"Dia todo?"** quando acionada, indicará que o contato será efetuado durante todo o dia.

Tem-se no campo **"Título"** uma qualificação para o contato que será realizado.

Na próxima etapa tem-se os dados relacionados ao conteúdo do e-mail:

![Imagem 53: Na próxima etapa tem-se os dados relacionados ao conteúdo do e-mail:](https://ajuda.sankhya.com.br/hc/article_attachments/4412676450967)

O campo **"O quê"** contém algumas variáveis que podem ser utilizadas na formatação da mensagem. Sendo elas:

- **Títulos:** &{LISTA\_TITULOS};
- **Email empresa:** &{EMAIL\_EMPRESA};
- **Nome empresa:** &{NOME\_EMPRESA};
- **Razão social empresa:** &{RAZAO\_SOCIAL\_EMPRESA};
- **Nome parceiro:** &{NOME\_PARCEIRO};
- **Total de débito:** &{TOTAL\_DEBITO};
- **CNPJ do parceiro:** &{CPFCNPJ\_PARCEIRO};
- **CNPJ da empresa:** &{CNPJ\_EMPRESA};
- **Quantidade de títulos:** &{QTD\_TITULOS}.

Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento. Podendo também utilizar filtros específicos nesta pesquisa.

![Imagem 54: Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento.…](https://ajuda.sankhya.com.br/hc/article_attachments/4412663202327)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos)

#### \*\*\*\*Ação Programada

Este evento permite que usuários avançados utilizem ações personalizadas através de rotinas de Banco de Dados ou de Java. As informações mais aprofundadas a respeito destas ações podem ser visualizadas no tópico [Configurando Ações Personalizadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas).

![Imagem 55: Este evento permite que usuários avançados utilizem ações personalizadas através de rotinas de Banco de Dados ou de…](https://ajuda.sankhya.com.br/hc/article_attachments/4412670684823)

O campo **"Descrição"** será preenchido com o nome do evento. Este nome será apresentado na Régua de Cobrança quando o mouse estiver posicionado em cima do evento.

Através do campo **"Acontece"**, determina-se em qual momento o evento será disparado. Tem-se as seguintes opções:

- **Antes do vencimento:** Informa-se o número de dias antes do vencimento;
- **No vencimento**;
- **Após o vencimento:** Será indicado o número de dias após o vencimento;
- **Ao baixar**.

**Observação:** optando-se pela opção Ao baixar, assim que o título for baixado tem-se a execução do evento configurado. Sendo que, ao baixar um título que possui uma baixa com data futura; o envio do evento será realizado no ato da baixa antecipada.

Nesta etapa pode-se configurar os recursos de personalização:

![Imagem 56: Nesta etapa pode-se configurar os recursos de personalização:](https://ajuda.sankhya.com.br/hc/article_attachments/4412663222807)

No campo **"Tipo de Rotina"** tem-se a escolha de qual rotina será utilizada na criação das ações personalizadas.

Tratando-se do tipo de rotina Java, é necessário determinar se a mesma irá **"Usar transação manual"** e qual módulo será empregado (previamente criado na tela [Módulo Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573-M%C3%B3dulo-Java)). Além disso, aponta-se a classe da rotina e caso seja necessário pode-se baixar a biblioteca de extensões.

Para a rotina de Banco de Dados, define-se se a rotina irá Usar transação manual e a descrição que irá identificar a mesma. Posteriormente, clica-se no botão ![Imagem 57: Para a rotina de Banco de Dados, define-se se a rotina irá Usar transação manual e a descrição que irá identificar a…](https://ajuda.sankhya.com.br/hc/article_attachments/15411377823895) **"Criar template da rotina"**.

Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento. Podendo também utilizar filtros específicos nesta pesquisa.

![Imagem 58: Ao final, tem-se a etapa onde é possível simular e verificar quais serão os títulos que se encaixarão neste evento.…](https://ajuda.sankhya.com.br/hc/article_attachments/4412670738839)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#abaeventos) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#top)

### Aba Seleção de títulos

![Imagem 59: Aba Seleção de títulos](https://ajuda.sankhya.com.br/hc/article_attachments/22894777612055)

Na aba Eventos são registrados os eventos que serão aplicados aos títulos listados na tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). Isso possibilita que na aba de Seleção de Títulos sejam identificados quais títulos estão aptos a receber esses eventos.

Para facilitar a busca, utilize o quadrante de **"Filtro Rápido"** disponível na lateral esquerda ou crie os **"Filtros personalizados"** de acordo com as necessidades específicas.

Caso não aplique nenhum filtro, ao clicar no botão ![Imagem 60: Caso não aplique nenhum filtro, ao clicar no botão "Visualizar títulos" , o pop-up "Informe a data de execução" surgirá…](https://ajuda.sankhya.com.br/hc/article_attachments/22894747251223) **"Visualizar títulos"**, o pop-up **"Informe a data de execução"** surgirá na tela solicitando o preenchimento da data de execução dos eventos da Régua de Cobrança.

![Imagem 61: Caso não aplique nenhum filtro, ao clicar no botão "Visualizar títulos" , o pop-up "Informe a data de execução" surgirá…](https://ajuda.sankhya.com.br/hc/article_attachments/22894747265943)

Após o preenchimento, ao pressionar o botão ![Imagem 62: Após o preenchimento, ao pressionar o botão "Aplicar" , serão listados todos os títulos de Movimentação Financeira que…](https://ajuda.sankhya.com.br/hc/article_attachments/16746208747031) **"Aplicar"**, serão listados todos os títulos de Movimentação Financeira que se encontram aptos para receber os eventos previamente cadastrados.

Dessa forma, como mencionado nas informações acima, será possível prosseguir de algumas maneiras, a seguir têm-se um exemplo:

- Suponha-se que na aba Eventos sejam criadas duas opções: **"Dia do vencimento"**, que dispara um e-mail no dia em que o título vence, e **"2 dias"**, que cria um registro na tela [Agenda de Recursos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604574-Agenda-de-Recursos) para os títulos vencidos há dois dias.

![Imagem 63: Suponha-se que na aba Eventos sejam criadas duas opções: "Dia do vencimento" , que dispara um e-mail no dia em que o…](https://ajuda.sankhya.com.br/hc/article_attachments/22894747277079)

- Ao verificar a aba Seleção de títulos, caso não informe nenhum filtro, e informe uma data específica, por exemplo: 18/04/2024, a pesquisa retornará somente os títulos com data de vencimento igual a 16/04/2024 (títulos vencidos há dois dias) e 18/04/2024 (títulos que vencem neste dia) conforme configurado.

**Importante**: será possível cadastrar os eventos conforme a necessidade para efetuar a cobrança de seus títulos.

No entanto, caso utilize algum Filtro rápido ou personalizado, a pesquisa irá retornar somente títulos que estejam nos padrões do filtro utilizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#top)

### \*\*\*\*Botão Outras Opções...

O botão **"Outras Opções..."** é representado pelo ícone ![Imagem 64: O botão "Outras Opções..." é representado pelo ícone e está localizado na parte superior direita da tela, quando…](https://ajuda.sankhya.com.br/hc/article_attachments/16746208749207) e está localizado na parte superior direita da tela, quando acionado apresenta a seguinte opção:

**Visualizar Histórico da Régua:** Através desta opção, tem-se a abertura da tela [Histórico da Régua de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109413-Hist%C3%B3rico-da-R%C3%A9gua-de-Cobran%C3%A7a) para uma análise do histórico de execução da Régua de Cobrança em questão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#top)

### Parâmetros que influenciam esta rotina

#### Parâmetro de otimização de performance para envio de E-mails – THREADMAILRECOB

Para melhorar a performance da execução da Régua de Cobrança, especialmente em situações com grandes volumes de envio de e-mails, foi criado o parâmetro `THREADMAILRECOB`.

**O que é o parâmetro** `**THREADMAILRECOB**`**?**

Este parâmetro define a quantidade de threads (processos paralelos) utilizadas para o envio de e-mails da Régua de Cobrança. Ele pode ser configurado na tela "**Preferências**" e tem como objetivo paralelizar o processamento dos eventos, acelerando o envio das mensagens.
**Como funciona?**
Ao ativar esse parâmetro (THREADMAILRECOB = 2 a 5 threads), o envio de e-mails é distribuído entre várias threads, reduzindo o tempo de execução da rotina. Desse modo, o número da régua é gravado no módulo **Financeiro** no momento em que o registro entra na fila de envio, e não após o envio. Isso evita lentidão no sistema e garante que não ocorram disparos duplicados para o mesmo título.
**Limitações e recomendação de uso:**
Este parâmetro deve ser utilizado apenas em ambientes com alto volume de envios de e-mails de cobrança com anexos, onde a performance pode ser comprometida.
Valor máximo permitido: 5 threads.
A ativação modifica a forma padrão de envio de e-mails, o que pode impactar o comportamento do processo em ambientes com baixa volumetria. Portanto, seu uso deve ser avaliado cuidadosamente.
**Tabelas Relacionadas ao Processo**
Para garantir o correto funcionamento e rastreabilidade, recomenda-se acompanhar o preenchimento das seguintes tabelas:
TMDFMG – Fila de Mensagens: armazena as mensagens a serem enviadas.
TMDAMG – Anexo Mensagens: armazena os arquivos anexados.
TMDAXM – Anexo por Mensagem: realiza a ligação entre as mensagens e seus respectivos anexos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a#top)
