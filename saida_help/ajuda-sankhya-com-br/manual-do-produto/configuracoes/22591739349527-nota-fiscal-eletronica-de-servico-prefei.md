---
id: "22591739349527"
titulo: "Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Maranhão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T18:55:17Z"
rotulos: ["Configuração", "Cidades", "Impostos", "Prefeituras", "NFS-e", "Maranhão"]
---

# Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Maranhão

Neste artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do Maranhão, para conhecê-las acesse os links abaixo:

| **Cidades** | |
| --- | --- |
| [Benevides/MA](https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o#Benevides/MA) | [Riachão/MA](https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o#h_01KYHXBBGT8Q4NN9Y6DEW1PQHA) |
| [Imperatriz/MA](https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o#Imperatriz/MA) | [São Luís/MA](https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o#S%C3%A3oLu%C3%ADs/MA) |

### Benevides/MA

O sistema encontra-se apto para emitir NFS-e para o município de Benevides.

**Observação:** a cidade não suporta o cancelamento de nota de serviço via webservice, este deverá ser feito diretamente na prefeitura.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o#top)

### Imperatriz/MA

O sistema encontra-se apto para emitir NFS-e para o município de Imperatriz.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o#top)

### Riachão/MA

O município de Riachão/MA utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o "Mun. domicílio fiscal" com o código IBGE **2109502**.
  - [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a "Inscrição Municipal" da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo "Cód. Trib. Município" com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o "Item da Lista de Serviços (LC 116)" (ex: 1401), o "Código CNAE" (ex: 4520001) e o "Código NBS" (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)** Para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - **Cadastro de** [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)**:** na [aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), [seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - [**Tipos de Operação (TOP)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**:** na [aba Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF) da TOP, certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o#top)

### São Luís/MA

Os seguintes cadastros estão envolvidos:

![Imagem 1: Na tela Cidades , aba Geral , após cadastrar a cidade, informe o "Mun. domicílio fiscal" de São Luís, sendo este…](https://ajuda.sankhya.com.br/hc/article_attachments/22591770302743) Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), após cadastrar a cidade, informe o **"Mun. domicílio fiscal"** de São Luís, sendo este 2111300 e o **"Cód. município SIAFI"** 0921.

![Imagem 2: Depois, acesse a tela Serviço , aba Impostos e informe o código de tributação no município, o tipo de serviço e o CNAE…](https://ajuda.sankhya.com.br/hc/article_attachments/22591770305559) Depois, acesse a tela [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7os#abaimpostos) e informe o código de tributação no município, o tipo de serviço e o CNAE da empresa.

![Imagem 3: * Acesse as Preferências da Empresa , aba Documentos Fiscais Eletrônicos , sub-aba NFS-e > Geral e defina no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/22591739335831) **\*Acesse as**[**Preferências da Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)**, aba** [**Documentos Fiscais Eletrônicos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)**, sub-aba** [**NFS-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) **>** [**Geral**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e) **e defina no campo "Regime esp. trib. ISS (NFS-e)"\*, o regime especial de tributação ISS a ser utilizado pela empresa conforme as opções admitidas:**

| **Código** | **Descrição** |
| --- | --- |
| C | Isenta de ISS |
| E | Não Incidência no Município |
| F | Imune |
| K | Exigibilidade Susp. Dec.J/Proc.A |
| N | Não Tributável |
| T | Tributável |
| G | Tributável Fixo |
| H | Tributável S.N |
| M | MEI (Simples Nacional) |

![Imagem 4: Nos Tipos de Operação - TOP , acesse a aba NFS-e e configure no campo "Cód. Natureza Oper. ISS (NFS-e)" a natureza a…](https://ajuda.sankhya.com.br/hc/article_attachments/22591770308631) **Nos**[**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top)**, acesse a aba** [**NFS-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse)**e configure no campo "Cód. Natureza Oper. ISS (NFS-e)" a natureza a ser utilizada na operação. São permitidas as seguintes opções:**

| **Código** | **Descrição** |
| --- | --- |
| A | Sem dedução |
| B | Com dedução/Materiais |
| C | Imune/Isenta ISSQN |
| D | Devolução/Simples remessa |
| J | Intermediação |

#### Cancelamento

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

| **Código** | **Descrição** |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

Observação: a prefeitura de São Luís permite que somente a série **"99"** seja enviada na NFS-e. Além disso, a numeração da nota deve ser sequencial. Caso alguma nota seja aprovada fora da sequência é necessário alterar no site da prefeitura a sua numeração por meio do [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao) para o número da última nota aprovada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22591739349527-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Maranh%C3%A3o#top)
