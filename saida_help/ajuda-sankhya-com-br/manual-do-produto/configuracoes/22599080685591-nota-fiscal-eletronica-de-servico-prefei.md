---
id: "22599080685591"
titulo: "Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Piauí"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22599080685591-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Piau%C3%AD"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-30T13:19:38Z"
rotulos: ["Parceiro", "Cidades", "Prefeituras", "NFS-e", "Piauí"]
---

# Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Piauí

Neste artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do Piauí, para conhecê-las acesse os links abaixo:

| **Cidades** | |
| --- | --- |
| [Jaicós/PI](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599080685591-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Piau%C3%AD#h_01KYHXMP93GWPFCSGBA142DPD9) | [Teresina/PI](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599080685591-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Piau%C3%AD#Teresina/PI) |
| [Picos/PI](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599080685591-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Piau%C3%AD#Picos/PI) |  |

### Jaicos/PI

O município de Jaicós/PI utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o "Mun. domicílio fiscal" com o código IBGE **2205201**.
  - [**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)**:** confirme se a "Inscrição Municipal" da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo "Cód. Trib. Município" com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o "Item da Lista de Serviços (LC 116)" (ex: 1401), o "Código CNAE" (ex: 4520001) e o "Código NBS" (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)** Para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - **Cadastro de** [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o)**:** na [aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), [seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - [**Tipos de Operação (TOP)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**:** na [aba Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF) da TOP, certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599080685591-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Piau%C3%AD#top)

### Picos/PI

O sistema encontra-se apto para emitir NFS-e para o município de Picos.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599080685591-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Piau%C3%AD#top)

### Teresina/PI

O sistema encontra-se apto para emitir NFS-e para o município de Teresina.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599080685591-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Piau%C3%AD#top)
