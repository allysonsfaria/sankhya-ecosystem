---
id: "22599692930711"
titulo: "Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Acre"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22599692930711-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Acre"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:42:13Z"
rotulos: ["Configuração", "Alíquota de ISS", "Cidades", "Parceiros", "Impostos", "Prefeituras", "NFS-e", "Acre", "Documentos Eletrônicos"]
---

# Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Acre

Neste artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do Acre, para conhecê-las acesse os links abaixo:

| Cidades | |
| --- | --- |
| [Cruzeiro do Sul/AC](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599692930711-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Acre#cruzeirodosulac) | [Senador Guiomard/AC](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599692930711-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Acre#01HTYSWY4KZ52HSYS21N68H9SC) |
| [Rio Branco/AC](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599692930711-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Acre#RioBranco/AC) |  |

### Cruzeiro do Sul/AC

**(emissões temporariamente indisponíveis, sob responsabilidade do município)**

**Esse município continua a utilizar o emissor próprio municipal**

Os seguintes cadastros estão envolvidos:

**(1)** Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Cruzeiro do Sul, sendo este 1200203 e o **"Cód. município SIAFI"** 0107.

**(2)** Nos [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), acesse a aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) e configure no campo **"Cód. Natureza Oper. ISS (NFS-e)"** a natureza a ser utilizada na operação. São permitidas as seguintes opções:

| **Código** | **Descrição** |
| --- | --- |
| 1 | Tributação no Município |
| 2 | Tributação fora do Município |
| 3 | Isenção |
| 4 | Imune |
| 5 | Exigibilidade uspensa por decisão judicial |
| 6 | Exigibilidade suspensa por procedimento administrativo |

**(3)** Acesse as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) e defina no campo **"Regime esp. tributação ISS (NFS-e)"** o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:

| **Código** | **Descrição** |
| --- | --- |
| 0 | Normal/Nenhum |
| 1 | Microempresa municipal |
| 2 | Estimativa |
| 3 | Sociedade de profissionais |
| 4 | Cooperativa |
| 5 | Microempresário Individual(MEI) |
| 6 | Microempresário e Empresa de Pequeno Porte (ME EPP) |

#### Cancelamento

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

| **Código** | **Descrição** |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599692930711-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Acre#top)

### Rio Branco/AC

**Esse município utiliza o emissor nacional a partir de 2026**

**(1)** Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Rio Branco, sendo este 1200401 e o **"Cód. município SIAFI"** 1390.

**(2)** Serie e numeração das notas

O Portal nacional exige para emissões via webservice uma serie com 5 caracteres, para isso acesse:

- **Preferências >**[**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**>**[**Documentos Fiscais Eletrônicos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)**>**[**NFS-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e)**>**[**Geral**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Geral) e configure o campo **"Prefixo Série NFS-e Padrão Nacional”** preenchendo com 2 dígitos respeitando o intervalo de 00 a 49.
- Comercial » Arquivo » Cadastros » [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) > [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...) e localize o item **"Controle de Numeração"**. Configure a **"Série"** (Padrão Nacional) utilizando um valor numérico de 001 a 999, bem como o campo de **"Numeração"**. Recomendamos ativar a numeração automática para garantir a integridade dos dados.

(3)** Revise as configurações do Serviço**

Na tela [Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), acesse as abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss) ou [Configuração por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa) (conforme o modelo da sua organização) e revise o preenchimento dos campos abaixo:

- **Código de Serviço Municipal**: atualize o código antigo para o novo formato padronizado. Por exemplo: de 01.02 para 01.02.01.001.
- **Regra Geral (Portal Nacional)**: o preenchimento padrão deve ser o item da lista de serviço acrescido do sufixo 01.

**Nota:** alguns municípios exigem também o complemento 001. Consulte a documentação local para confirmar a exigência.

**Código NBS:** preencha conforme a [tabela oficial da Nomenclatura Brasileira de Serviços](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc/anexoviii-correlacaoitemnbsindopcclasstrib_ibscbs_v1-00-00.xlsx/@@download/file).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599692930711-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Acre#top)

### Senador Guiomard/AC

O município de Senador Guiomard/AC utiliza o **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **1200450**.
  - [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Regras de Emissão e Particularidades**
  - **Múltiplos Itens e E-mails:** para incluir vários serviços na mesma nota ou enviar o documento para diversos e-mails, ative as opções **"Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json"** no cadastro da [Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599692930711-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Acre#top)
