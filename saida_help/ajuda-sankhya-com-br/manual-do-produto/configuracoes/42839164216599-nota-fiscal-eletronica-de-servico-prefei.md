---
id: "42839164216599"
titulo: "Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Amapá"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-01T11:57:00Z"
rotulos: ["Especificações por Prefeituras", "Macapá/AP", "Configuração para IBS e CBS (Reforma Tributária)", "Código Classificação Tributária Nacional", "Sistema Próprio Municipal", "Santana/AP", "Vitória do Jari/AP", "Amapá/AP", "Porto Grande/AP", "Oiapoque/AP"]
---

# Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Amapá

Neste artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do **Amapá**, para conhecê-las acesse os links abaixo:

| Cidades | |
| --- | --- |
| [Amapá/AP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#h_01M0DJ6T8NJEH38PEFWXQ7AQYE) | [Santana/AP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#h_01M0D9Q7ZNFVTQAAYSMRWEN0TB) |
| [Macapá/AP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#h_01M0DG84CTT0046771RDQ7DMKM) | [Vitória do Jari/AP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#h_01M0D9Q7ZNFVTQAAYSMRWEN0TB) |
| [Oiapoque/AP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#h_01M0DGRSNN30ZBVKD12YHB0BCG) |  |
| [Porto Grande/AP](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#h_01M0DGRSNN30ZBVKD12YHB0BCG) |  |

### Amapá/AP

O município de Amapá/AP utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **1600105**.
  - [**Empresas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)**: para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - **Cadastro de Serviço:** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), seção **Reforma Tributária**, preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - **Tipos de Operação (TOP):** na aba **Impostos**, seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#top)

### Macapá/AP

O município de Macapá/AP utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **1600303**.
  - [**Empresas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)**: para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - **Cadastro de Serviço:** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), seção **Reforma Tributária**, preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - **Tipos de Operação (TOP):** na aba **Impostos**, seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#top)

### Oiapoque/AP

O município de Oiapoque/AP utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **1600501**.
  - [**Empresas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)**: para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - **Cadastro de Serviço:** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), seção **Reforma Tributária**, preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - **Tipos de Operação (TOP):** na aba **Impostos**, seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#top)

### Porto Grande/AP

O município de Porto Grande/AP utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **1600535**.
  - [**Empresas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)**: para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - **Cadastro de Serviço:** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), seção **Reforma Tributária**, preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - **Tipos de Operação (TOP):** na aba **Impostos**, seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#top)

### Santana/AP

O município de Santana/AP utiliza o **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **1600600**.
  - [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)**: para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - **Cadastro de Serviço:** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), seção **Reforma Tributária**, preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - **Tipos de Operação (TOP):** na aba **Impostos**, seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

    [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#top)

### Vitória do Jari/AP

O município de Vitória do Jari/AP utiliza o **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **1600808**.
  - [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 1401), o **"Código CNAE"** (ex: 4520001) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)**: para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - **Cadastro de Serviço:** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), seção **Reforma Tributária**, preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - **Tipos de Operação (TOP):** na aba **Impostos**, seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/42839164216599-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Amap%C3%A1#top)
