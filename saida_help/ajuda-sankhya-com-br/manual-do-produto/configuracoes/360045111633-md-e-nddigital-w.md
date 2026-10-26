---
id: "360045111633"
titulo: "MD-e NDDigital/W"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:58:03Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "MD-e NDDigital/W manual", "Manifestação do Destinatário e Configurações Necessárias", "Documentos Eletrônicos", "NDDigital"]
---

# MD-e NDDigital/W

Temos aqui, um processo em que o destinatário de uma Nota Fiscal Eletrônica se manifesta para a SEFAZ, comunicando ao órgão qual a realidade em relação à nota fiscal emitida para ele. O destinatário poderá comunicar à SEFAZ quatro eventos de manifestação, vejamos abaixo sobre cada um deles:

- **Ciência da Operação:** O destinatário declara ter ciência da operação destinada ao seu CNPJ, mas ainda não possui elementos suficientes para apresentar uma manifestação conclusiva;
- **Confirmação da Operação:** O destinatário confirma a ocorrência da operação e o recebimento da mercadoria;
- **Desconhecimento da Operação:** Neste caso, o destinatário afirma o desconhecimento da operação, não reconhecendo a emissão da NF-e destinada ao seu CNPJ;
- **Operação não Realizada:** Utiliza-se este evento, quando o destinatário reconhece que a operação não foi realizada (com recusa do recebimento da mercadoria e/ou outros) e a justificativa pela qual a operação não se realizou.

Além desses eventos que o destinatário poderá comunicar à SEFAZ, existe um serviço capaz de realizar o download do XML das Notas Fiscais Eletrônicas que foram emitidas para o CNPJ do destinatário e que tiveram o evento de Ciência da Operação registrado. De modo geral, a Manifestação do Destinatário tem o objetivo de evitar-se a emissão de notas fiscais fraudulentas, para destinatários que não possuem ciência ou confirmação de tal operação.

Importante: Uma vez que o destinatário efetuou o evento de Ciência de Operação, este possui 180 dias para que seja feita a manifestação final do documento que é caracterizada por qualquer outro evento. Este prazo poderá sofrer modificações ao longo do tempo pela SEFAZ.

Para mais informações pode-se acessar os seguintes links:

<http://www.nfe.fazenda.gov.br/portal/perguntasFrequentes.aspx?tipoConteudo=yjOJMwFOkA0=>

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=bUBJ/PmtKQo=>

[Premissas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#premissas)                                                              [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#configuraes)

[Utilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#utilizao)                                                              [Tabelas de integração Sankhya x NDDigital](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#tabelasdeintegraosankhyaxnddigital)

## Premissas

Para utilização deste processo, são necessários os seguintes fatores:

- Possuir um certificado digital do tipo A1 credenciado juntamente a SEFAZ;
- Portar o produto **"30610 –  NOTA FISCAL ELETRÔNICA/W"**;
- Conter o produto **"30655 – PORTAL DE IMPORTAÇÃO DOC. ELETRÔNICOS"**;
- Dispor do produto **"30428 – MD-e NNDigital /W"**;
- Não possuir o produto **"30672 – MANIFESTO DO DESTINATÁRIO/W"**;
- Compreender as [Tabelas de integração Sankhya x NDDigital](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#tabelasdeintegraosankhyaxnddigital), assim como seus objetos complementares (índices, triggers, etc):

TBDATABASEINPUTENTRY

TBDATABASEINTEGRATIONENTRY

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#top)

## Configurações

Nas [Preferências de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abanf-enfc-e), a opção **"Utiliza MD-e"** irá caracterizar que a empresa em questão emprega o MD-e NDDigital.

Além disso, no campo **"Nome Job NDDigital"** deve ser especificado o nome do JOB disponibilizado pela NDDigital, pois os registros de evento serão criados com esta instrução.

**Importante:** a aplicação da NDDigital utiliza esse dado como uma espécie de chave de identificação do cliente, logo, deve-se buscar o nome junto a equipe da NDD.

Na tela [Configuração MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599234-Configura%C3%A7%C3%A3o-MD-e-DF-e) configure os seguintes campos:

No campo **"Intervalo Consulta em horas"** descreva o intervalo ao qual o Sankhya-W irá realizar a consulta nas tabelas de integração com a NDDigital em busca de dados referente a manifestação (nf-e, evento de manifestação e/ou cancelamento).

Por meio do campo **"Modelo de relatório Danfe"** informe qual modelo de relatório o sistema deve utilizar para apresentar o XML de documentos baixados pela integração caso o usuário deseje visualizar o documento no Portal de Importações. O botão **"Baixar modelo padrão"** realiza o download de um modelo padrão Sankhya, edita-lo e depois cadastra-lo como um modelo de relatório para ser utilizado aqui.

O botão **"Consultar Notas"** realiza a pesquisa nas tabelas de integração com a NDDigital imediatamente.

Na grade **"Mensagens MD-e"** são apresentados os registros das consultas realizadas nas tabelas de integração em busca de documentos e/ou eventos. Os registros desta grade podem ser considerados registros de log de execução.

**Nota:** todas as alterações feitas na tela deverão ser gravadas por meio do botão **"Salvar"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#top)

## Utilização

O [Portal de importações de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) é a principal rotina utilizada para execução do processo de recebimento de documentos eletrônicos e consequentemente importação, visto que os documentos (XMLs das notas de compras) são recebidos pela aplicação NDDigital e em seguida disponibilizados no contexto Sankhya para avaliação e posterior importação por parte do usuário nesta rotina.

Além da importação de documentos, você será capaz de comandar os eventos referentes ao manifesto de destinatário sobre documentos. É importante salientar que existe a possibilidade de comandar eventos sobre documentos ainda não importados, visto que uma vez sinalizado que uma determinada operação não foi realizada, não faz sentido realizar a importação de tal documento para base de dados.

Os eventos podem ser comandados a partir da seleção de um documento (seleção de uma linha na grade) e escolha do evento a partir do botão **"MD-e"**.

![Imagem 1: Os eventos podem ser comandados a partir da seleção de um documento (seleção de uma linha na grade) e escolha do evento…](https://ajuda.sankhya.com.br/hc/article_attachments/15614999987479)

Através da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237174-Central-de-Compras), pode-se comandar os eventos de manifesto do destinatário, bem como, visualizar os manifestos realizados para o documento em questão. A ação pode ser comanda a partir do botão **"MD-e"** e seleção da opção desejada. Este modo de operação faz sentido quando o documento já existe internamente no sistema, ou seja, a nota de compra já foi lançada no Sankhya-W.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#top)

## Tabelas de Integração Sankhya x NDDigital

Segue abaixo as tabelas de integração do Sankhya com o NDDigital:

-------------------ORCL create table TBDATABASEINPUTENTRY------------------------

CREATE TABLE TBDATABASEINPUTENTRY

              (

              ID           NUMBER(20) NOT NULL,

              DOCUMENTDATA            BLOB NOT NULL,

              STATUS NUMBER(5) NOT NULL,

              JOB VARCHAR2(60),

              DOCUMENTUSER VARCHAR2(30) NULL,

              KIND NUMBER(5) NOT NULL,

              CONSTRAINT TBDATABASEINPUTENTRY\_PK PRIMARY KEY(ID) ENABLE

              )

/

CREATE INDEX TBDATABASEINPUTENTRY\_IDX1 ON TBDATABASEINPUTENTRY (STATUS, JOB)

/

CREATE SEQUENCE TBDATABASEINPUTENTRY\_SEQ

              START WITH 1

              INCREMENT BY 1

              MAXVALUE 1.0E28

              MINVALUE 1

              NOCYCLE

              CACHE 20

              NOORDER

/

CREATE OR REPLACE TRIGGER "BI\_TBDATABASEINPUTENTRY" BEFORE INSERT ON TBDATABASEINPUTENTRY

FOR EACH ROW

              WHEN (new.ID IS NULL) BEGIN

              SELECT "TBDATABASEINPUTENTRY\_SEQ".NEXTVAL INTO :new.ID FROM dual;

END;

/

ALTER TRIGGER "BI\_TBDATABASEINPUTENTRY" ENABLE;

/

-----------------MSSQL create table TBDATABASEINPUTENTRY--------------------------

SET ANSI\_NULLS ON

GO

SET QUOTED\_IDENTIFIER ON

GO

IF NOT EXISTS (SELECT \* FROM sys.objects WHERE object\_id = OBJECT\_ID(N'[TBDATABASEINPUTENTRY]') AND type in (N'U'))

BEGIN

CREATE TABLE [TBDATABASEINPUTENTRY](

[id] [bigint] IDENTITY(1,1) NOT NULL,

[documentdata] [varbinary](max) NOT NULL,

[status] [smallint] NOT NULL,

[job] [varchar](60) NULL,

[documentuser] [varchar](30) NULL,

[kind] [smallint] NOT NULL,

CONSTRAINT [PK\_TBDATABASEINPUTENTRY] PRIMARY KEY CLUSTERED

(

[id] ASC

)WITH (PAD\_INDEX  = OFF, IGNORE\_DUP\_KEY = OFF) ON [PRIMARY]

) ON [PRIMARY]

END

GO

IF NOT EXISTS (SELECT \* FROM sys.indexes WHERE object\_id =

OBJECT\_ID(N'[TBDATABASEINPUTENTRY]') AND name = N'IX\_TBDATABASEINPUTENTRY')

CREATE NONCLUSTERED INDEX [IX\_TBDATABASEINPUTENTRY] ON [TBDATABASEINPUTENTRY]

(

[status] ASC,

[job] ASC

)WITH (PAD\_INDEX  = OFF, IGNORE\_DUP\_KEY = OFF) ON [PRIMARY]

-----------------------ORCL create table TBDATABASEINTEGRATIONENTRY------------------------

CREATE TABLE TBDATABASEINTEGRATIONENTRY (

          CONNECTORINTEGRATIONID NUMBER(20) NOT NULL PRIMARY KEY,

           DOCUMENTDATA BLOB NOT NULL ,

           STATUS INTEGER NOT NULL ,

           KIND INTEGER NOT NULL

)

CREATE SEQUENCE "CONNECTORINTEGRATIONID\_SEQ"

 START WITH 1

 MAXVALUE 1.0E28

 MINVALUE 1

 NOCYCLE

 CACHE 20

 NOORDER;

/

CREATE OR REPLACE TRIGGER "BI\_CONNECTORINTEGRATION"

  BEFORE INSERT

  ON TBDATABASEINTEGRATIONENTRY

  FOR EACH ROW

  WHEN (NEW.CONNECTORINTEGRATIONID IS NULL)

BEGIN

  SELECT "CONNECTORINTEGRATIONID\_SEQ".NEXTVAL

    INTO :NEW.CONNECTORINTEGRATIONID

    FROM DUAL;

END;

/

ALTER TRIGGER "BI\_CONNECTORINTEGRATION" ENABLE

--------------------MSSQL create table TBDATABASEINTEGRATIONENTRY-----------------------

CREATE TABLE [TBDATABASEINTEGRATIONENTRY](

           [CONNECTORINTEGRATIONID] [bigint] IDENTITY(1,1) NOT NULL,

           [DOCUMENTDATA] [varbinary] (max) NOT NULL ,

           [STATUS] [int] NOT NULL ,

           [KIND] [int] NOT NULL

CONSTRAINT [PK\_CONNECTORINTEGRATION] PRIMARY KEY CLUSTERED

(

           [CONNECTORINTEGRATIONID] ASC

)WITH (PAD\_INDEX  = OFF, IGNORE\_DUP\_KEY = OFF) ON [PRIMARY]

) ON [PRIMARY]

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111633-MD-e-NDDigital-W#top)
