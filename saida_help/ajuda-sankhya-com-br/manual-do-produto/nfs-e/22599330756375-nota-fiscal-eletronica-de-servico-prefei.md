---
id: "22599330756375"
titulo: "Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Rio Grande do Norte"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > NFS-e"
atualizado_em: "2026-09-15T17:01:30Z"
rotulos: ["Configuração", "Cidades", "Impostos", "Prefeituras", "NFS-e", "Rio Grande do Norte", "Reforma Tributária"]
---

# Nota Fiscal Eletrônica de Serviço - Prefeituras: Estado Rio Grande do Norte

Neste artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do Rio Grande do Norte, para conhecê-las acesse os links abaixo:

| Cidades | |
| --- | --- |
| [Almino Afonso/RN](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#h_01KXJSY8J1BMEP5AH688SJE78Z) | [Natal/RN](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#Natal/RN) |
| [Apodi/RN](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#h_01HRW52N8ZBDCGMNKB4ESWCYNP) | [Parnamirim/RN](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#Parnamirim/RN) |
| [Jardim do Seridó/RN](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#h_01KPTN0TNDBMWSSZ4RD96GP3MH) | [São Fernando/RN](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#01J806BK8NZMXF6HGZXPGNKDHG) |
| [Macaíba/RN](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#Maca%C3%ADba/RN) | [São Tomé/RN](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#h_01KR10CR3BX2R2834YGMZH5SS9) |

### Almino Afonso/RN

O município de Almino Afonso/RN utiliza um **Sistema Próprio Municipal** para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Esta homologação já contempla a adequação aos novos impostos da Reforma Tributária (**IBS e CBS**). Para garantir que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **2400604**.
  - [**Empresas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas)**:** confirme se a **"Inscrição Municipal"** da sua empresa está devidamente preenchida.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** preencha o campo **"Cód. Trib. Município"** com a formatação exigida pela prefeitura. Exemplo: **140101**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Item da Lista de Serviços (LC 116)"** (ex: 14.01), o **"Código CNAE"** (ex: 47890990) e o **"Código NBS"** (ex: 120024000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Configuração para IBS e CBS (Reforma Tributária)** Para que os novos impostos sejam calculados e enviados corretamente ao portal da prefeitura:
  - [**Cadastro de Serviço:**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos), seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#:~:text=Se%C3%A7%C3%A3o%20Reforma%20Tribut%C3%A1ria), preencha o campo **"Código Classificação Tributária Nacional"** (ex: 140101). Configure também as alíquotas de IBS e CBS pertinentes ao serviço.
  - [**Tipos de Operação (TOP)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**:** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), seção [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#01K56TN2K88BREGGCND4D6DBNF), certifique-se de ativar as marcações **"Tem CBS"** e **"Tem IBS"**.
- **Regras de Emissão e Particularidades**
  - **Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40%) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem amparo legal resultarão em rejeição do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#top) 

### Apodi/RN

O município de Apodi/RN utiliza o **Emissor Nacional** (Portal Nacional) para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **2401008**.
  - [**Empresas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas)**:** confirme se a **"Inscrição Municipal"** e o **"Cód. Regime Tribut."** (ex: Lucro Presumido) da sua empresa estão devidamente preenchidos.
- **Série e Numeração (Exigência de 5 dígitos):** por utilizar o Portal Nacional, a prefeitura exige que a série da nota tenha exatamente 5 caracteres. Configure da seguinte forma:
  - **Preferências da Empresa:** (Caminho: [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)) preencha o **"Prefixo Série NFS-e Padrão Nacional"** com 2 dígitos, usando números de **00 a 49**.
  - **TOP (Tipos de Operação):** (Caminho: [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...) > [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)) configure a **"Série Padrão Nacional"** com 3 dígitos (ex: de **001 a 999**) e ative a numeração automática.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** o Portal Nacional exige um formato específico. Adicione o dígito **"01"** ao final do código original do serviço. Exemplo: se o serviço for 14.01, preencha como **14.01.01**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Código de Tributação Municipal"** (ex: 14.01.01.001), o **"Item da Lista de Serviços (LC 116)"** (ex: 14.01), o **"Código CNAE"** (ex: 47890990) e o **"Código NBS"** (ex: 120011000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Regras de Emissão e Particularidades**
  - **Ative o Padrão Nacional:** lembre-se de ativar a marcação **"Emitir NFS-e Padrão Nacional"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).
  - **Múltiplos Itens e E-mails:** para incluir vários serviços diferentes na mesma nota ou enviar o documento para diversos e-mails, ative as opções **"Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json"** no [cadastro da Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades).
  - **Tomador do Exterior e ISS Retido:** o sistema permite a emissão de notas com ISS retido e para clientes do exterior normalmente (mediante preenchimento correto do endereço estrangeiro do tomador).
  - **Cancelamento e Substituição:** o município suporta tanto o **Cancelamento** quanto a **Substituição** de notas via webservice. Ambas as operações podem ser realizadas diretamente pelo sistema Sankhya sem erros.
  - **Atenção às Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40% de dedução) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem esse amparo legal resultarão em rejeição pelo portal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#top) 

### Jardim do Seridó/RN

O município de Jardim do Seridó/RN utiliza o **Emissor Nacional** (Portal Nacional) para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

- **Cadastros Básicos**
  - [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **2405702**.
  - **Empresas:** confirme se a **"Inscrição Municipal"** e o **"Cód. Regime Tribut."** (ex: Lucro Presumido) da sua empresa estão devidamente preenchidos.
- **Série e Numeração (Exigência de 5 dígitos)** Por utilizar o Portal Nacional, a prefeitura exige que a série da nota tenha exatamente 5 caracteres. Configure da seguinte forma:
  - **Preferências da Empresa:** (Caminho: [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)) preencha o **"Prefixo Série NFS-e Padrão Nacional"** com 2 dígitos, usando números de **00 a 49**.
  - **TOP (Tipos de Operação):** (Caminho: botão  [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...) > [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)) configure a **"Série Padrão Nacional"** com 3 dígitos (ex: de **001 a 999**) e ative a numeração automática.
- **Configurações do Serviço:** acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:
  - **Código de Serviço Municipal:** o Portal Nacional exige um formato específico. Adicione o dígito **"01"** ao final do código original do serviço. Exemplo: se o serviço for 14.01, preencha como **14.01.01**.
  - **Preenchimento obrigatório:** não esqueça de informar o **"Código de Tributação Municipal"** (ex: 14.01.01.001), o **"Item da Lista de Serviços (LC 116)"** (ex: 14.01), o **"Código CNAE"** (ex: 47890990) e o **"Código NBS"** (ex: 120011000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).
- **Regras de Emissão e Particularidades**
  - **Ative o Padrão Nacional:** lembre-se de ativar a marcação **"Emitir NFS-e Padrão Nacional"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).
  - **Múltiplos Itens e E-mails:** para incluir vários serviços diferentes na mesma nota ou enviar o documento para diversos e-mails, ative as opções **"Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json"** no [cadastro da Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades).
  - **Tomador do Exterior e ISS Retido:** o sistema permite a emissão de notas com ISS retido e para clientes do exterior normalmente (mediante preenchimento correto do endereço estrangeiro do tomador).
  - **Cancelamento e Substituição:** o município suporta tanto o **Cancelamento** quanto a **Substituição** de notas via webservice. Ambas as operações podem ser realizadas diretamente pelo sistema Sankhya sem erros.
  - **Atenção às Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40% de dedução) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem esse amparo legal resultarão em rejeição pelo portal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#top) 

### Macaíba/RN

O sistema encontra-se apto para emitir NFS-e para o município de Macaíba.

**Observação:** esta prefeitura permitirá a [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) e o cancelamento via webservice.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#top)

### Natal/RN

Os seguintes cadastros estão envolvidos:

![Imagem 1: Na tela Cidades , aba Geral , informe o "Mun. domicílio fiscal" de Natal , sendo este 2408102 e o "Cód. município…](https://ajuda.sankhya.com.br/hc/article_attachments/22599490233367) Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), informe o **"Mun. domicílio fiscal"** de Natal, sendo este 2408102 e o **"Cód. município SIAFI"** 1761.

**Nota:** esta prefeitura permitirá a [Substituição de NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046972414-Funcionalidades-relacionadas-%C3%A0-NFS-e#substituiodenfs-e) via webservice.

#### Cancelamento

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

| **Código** | **Descrição** |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#top)

### Parnamirim/RN

O sistema encontra-se apto para emitir NFS-e para o município de Parnamirim.

**Observação:** a cidade suporta o cancelamento de nota de serviço via webservice.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#top)

### São Fernando/RN

O município de São Fernando/RN utiliza o **Emissor Nacional** (Portal Nacional) para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

**Cadastros Básicos**

- [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **2411809**.
- **Empresas:** confirme se a **"Inscrição Municipal"** e o **"Cód. Regime Tribut."** (ex: Lucro Presumido) da sua empresa estão devidamente preenchidos.

**Série e Numeração (Exigência de 5 dígitos):** por utilizar o Portal Nacional, a prefeitura exige que a série da nota tenha exatamente 5 caracteres. Configure da seguinte forma:

- **Preferências da Empresa:** (Caminho: [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)) preencha o **"Prefixo Série NFS-e Padrão Nacional"** com 2 dígitos, usando números de **00 a 49**.
- **TOP (Tipos de Operação):** (Caminho: botão  [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...) > [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)) configure a **"Série Padrão Nacional"** com 3 dígitos (ex: de **001 a 999**) e ative a numeração automática.

**Configurações do Serviço:** Acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

- **Código de Serviço Municipal:** o Portal Nacional exige um formato específico. Adicione o dígito "01" ao final do código original do serviço. Exemplo: se o serviço for 14.01, preencha como **14.01.01**.
- **Preenchimento obrigatório:** não esqueça de informar o **"Código de Tributação Municipal"** (ex: 14.01.01.001), o **"Item da Lista de Serviços (LC 116)"** (ex: 14.01), o **"Código CNAE"** (ex: 47890990) e o **"Código NBS"** (ex: 120011000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

**Regras de Emissão e Particularidades**

- **Ative o Padrão Nacional:** lembre-se de ativar a marcação **"Emitir NFS-e Padrão Nacional"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).
- **Múltiplos Itens e E-mails:** para incluir vários serviços diferentes na mesma nota ou enviar o documento para diversos e-mails, ative as opções **"Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json"** no [cadastro da Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades).
- **Tomador do Exterior e ISS Retido:** o sistema permite a emissão de notas com ISS retido e para clientes do exterior normalmente (mediante preenchimento correto do endereço estrangeiro do tomador).
- **Cancelamento e Substituição:** o município suporta tanto o **Cancelamento** quanto a **Substituição** de notas via webservice. Ambas as operações podem ser realizadas diretamente pelo sistema Sankhya sem erros.
- **Atenção às Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40% de dedução) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem esse amparo legal resultarão em rejeição pelo portal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#top)

### São Tomé/RN

O município de São Tomé/RN utiliza o **Emissor Nacional** (Portal Nacional) para as Notas Fiscais de Serviço (NFS-e), e a emissão foi homologada de forma automatizada por meio da integração via webservice.

Para que suas notas sejam emitidas e aprovadas sem erros, siga o passo a passo de configuração abaixo:

**Cadastros Básicos**

- [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades)**:** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abageral), preencha o **"Mun. domicílio fiscal"** com o código IBGE **2412906**.
- **Empresas:** confirme se a "Inscrição Municipal" e o "Cód. Regime Tribut." (ex: Lucro Presumido) da sua empresa estão devidamente preenchidos.

**Série e Numeração (Exigência de 5 dígitos)** Por utilizar o Portal Nacional, a prefeitura exige que a série da nota tenha exatamente 5 caracteres. Configure da seguinte forma:

- **Preferências da Empresa:** (Caminho: [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)) preencha o **"Prefixo Série NFS-e Padrão Nacional"** com 2 dígitos, usando números de **00 a 49**.
- **TOP (Tipos de Operação):** (Caminho: botão  [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#botooutrasopes...) > [Controle de Numeração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#controledenumeracao)) configure a **"Série Padrão Nacional"** com 3 dígitos (ex: de **001 a 999**) e ative a numeração automática.

**Configurações do Serviço:** Acesse o cadastro de [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o) (abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaimpostos) e [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaalquotasdeiss)) e revise:

- **Código de Serviço Municipal:** o Portal Nacional exige um formato específico. Adicione o dígito "01" ao final do código original do serviço. Exemplo: se o serviço for 14.01, preencha como **14.01.01**.
- **Preenchimento obrigatório:** não esqueça de informar o **"Código de Tributação Municipal"** (ex: 14.01.01.001), o **"Item da Lista de Serviços (LC 116)"** (ex: 14.01), o **"Código CNAE"** (ex: 47890990) e o **"Código NBS"** (ex: 120011000, conforme a tabela oficial da Nomenclatura Brasileira de Serviços).

**Regras de Emissão e Particularidades**

- **Ative o Padrão Nacional:** lembre-se de ativar a marcação **"Emitir NFS-e Padrão Nacional"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).
- **Múltiplos Itens e E-mails:** para incluir vários serviços diferentes na mesma nota ou enviar o documento para diversos e-mails, ative as opções **"Enviar itens de NFSe separados no Json"** e **"Enviar múltiplos e-mails no Json"** no [cadastro da Cidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades).
- **Tomador do Exterior e ISS Retido:** o sistema permite a emissão de notas com ISS retido e para clientes do exterior normalmente (mediante preenchimento correto do endereço estrangeiro do tomador).
- **Cancelamento e Substituição:** o município suporta tanto o **Cancelamento** quanto a **Substituição** de notas via webservice. Ambas as operações podem ser realizadas diretamente pelo sistema Sankhya sem erros.
- **Atenção às Reduções de Base:** a prefeitura só aceita notas com redução na base de cálculo do ISS (ex: 40% de dedução) caso exista um **benefício fiscal válido atrelado à operação**. Tentativas de redução sem esse amparo legal resultarão em rejeição pelo portal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22599330756375-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras-Estado-Rio-Grande-do-Norte#top)
