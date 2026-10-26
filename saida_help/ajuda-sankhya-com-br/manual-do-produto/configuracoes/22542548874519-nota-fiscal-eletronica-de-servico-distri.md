---
id: "22542548874519"
titulo: "Nota Fiscal Eletrônica de Serviço: Distrito Federal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22542548874519-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Distrito-Federal"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:41:38Z"
rotulos: ["ISS", "Configuração", "Cidades", "NATOPEISSTOPEMP", "NFS-e", "Distrito Federal", "<Endereço>", "NFSEMAXNOTALOTE", "NFSEFORLC116CI", "NFSEOBSITERPS", "Cad. Mun. Contribuintes"]
---

# Nota Fiscal Eletrônica de Serviço: Distrito Federal

Nesse artigo serão apresentadas as especificações de emissão de NFS-e das cidades localizadas no estado do Distrito Federal, para conhecê-las acesse os links abaixo:

| **Cidades** | | | | |
| --- | --- | --- | --- | --- |
| [Brasília/DF](https://ajuda.sankhya.com.br/hc/pt-br/articles/22542548874519-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Distrito-Federal#bras%C3%ADlia/df) | | | |  |

####

### Brasília/DF

A Secretaria de Economia do Distrito Federal implantou, a partir de 01/01/2023, o Sistema de Gerenciamento do Imposto Sobre Serviços - ISS, utilizando modelo próprio de Nota Fiscal de Serviços Eletrônica - NFS-e (Padrão ABRASF) em substituição à Nota Fiscal Eletrônica - NF-e modelos 55 e 65.

---

![Imagem 1: Informações importantes referente à tags da cidade de Brasília](https://ajuda.sankhya.com.br/hc/article_attachments/22589273476247) **Informações importantes referente à tags da cidade de Brasília**

Para preencher a tag **<Discriminação>**, o sistema observará o campo **"Conteúdo a ser enviado na descrição de NFS-e"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), **aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) > [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaGeralSub-abaNFS-e)**. Se for diferente de **"null"** serão levadas as descrições conforme a seleção. Se for igual a **"null**" será observado o parâmetro **"Conteúdo a ser enviado na descrição de NFS-e - NFSEOBSITERPS"** e levada a descrição conforme foi selecionado.

Para a tag **<InformaçõesComplementares>** será levada a informação que estiver no campo **“Observação”** ([Grade Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho), da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)) do cabeçalho da nota fiscal.

Na tag **<Endereço>**, quando o UF do Tomador for diferente de **"EX"** serão levados os seguintes dados:

| **tcEndereco** | | | |
| --- | --- | --- | --- |
| Representação completa do endereço | | | |
| **Nome** | **Tipo** | **Ocorrência** | **Descrição** |
| Endereco | tsEndereco | 1-1 | Tipo e nome do logradouro |
| Numero | tsNumeroEndereco | 1-1 | Número do imóvel |
| Complemento | tsComplementoEndereco | 0-1 | Complemento do Endereço |
| Bairro | tsBairro | 1-1 | Nome do bairro |
| CodigoMunicipio | tsCodigoMunicipioIbge | 1-1 | Código da cidade |
| Uf | tsUf | 1-1 | Sigla do estado |
|  |  |  |  |
| Cep | tsCep | 1-1 | CEP da localidade |

E quando o UF do Tomador for igual a **"EX"**, levará os dados abaixo:

| **tcEnderecoExterior** | | | |
| --- | --- | --- | --- |
| Representação completa do endereço | | | |
| **Nome** | **Tipo** | **Ocorrência** | **Descrição** |
| CodigoPais | tsCodigoPaisIbge | 1-1 | Código do país da tabela de país do IBGE |
| EnderecoCompletoExterior | tsEnderecoCompletoExterior | 1-1 | Descrição do endereço |

Porém, quando o tomador do serviço for instituição governamental e não tiver Inscrição Municipal será necessário informar no campo **"Cad. Mun. Contribuintes"** da aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao) no Cadastro de Parceiro, o número do CNPJ do tomador.

Se houver um cadastro de parceiro estrangeiro e o campo **"Identificação de Estrangeiro"** na aba Identificação no Cadastro de Parceiro estiver preenchido, ao emitir uma NFS-e, a tag **<nifTomador>** será gerada e preenchida no XML com essa informação. No entanto, se o campo não for preenchido, a tag será gerada sem informação e a nota não será aprovada. 

A tag **<ExigibilidadeISS>** será preenchida conforme as configurações da [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Natureza da Operação ISS/Município](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanaturezadaoperaoissmunicpio); caso não tenha configuração, buscará da mesma tela na aba [NFSe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse), campo **"Cód. Natureza Oper. ISS (NFS-e)"**.

#### Cancelamento

Ao solicitar o cancelamento de uma NFS-e será aberto um pop-up para informar um dos motivos a seguir:

| **Código** | **Descrição** |
| --- | --- |
| 1 | Erro na emissão |
| 2 | Serviço não prestado |
| 4 | Duplicidade na nota |

**Importante:** os códigos **"3 - Erro de assinatura"** e **"5 - Erro de processamento"** são de uso restrito da Administração Tributária Municipal.

Com relação ao método síncrono, o número máximo de RPS por lote permitido pelo sistema é de 10 notas. Sendo assim, essa quantidade deverá ser ajustada no parâmetro **"Qtd. máxima de notas em um lote NFS-e - NFSEMAXNOTALOTE"**.

No cadastro dos Tipos de Operação - TOP, o **"Código Cód. Natureza Oper. ISS"** da aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfse) são permitidas as seguintes opções:

| **Código** | **Descrição** |
| --- | --- |
| 1 | Exigível |
| 2 | Não incidência |
| 3 | Isenção |
| 4 | Exportação |
| 5 | Imunidade |
| 6 | Exigibilidade suspensa por Decisão Judicial |
| 7 | Exigibilidade suspensa por Processo Administrativo |

**Observação:** este campo também poderá ser preenchido na aba [Natureza da Operação ISS/Município](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanaturezadaoperaoissmunicpio), quando o parâmetro **"Utilizar Cód. Nat. Operação ISS por Top/Empresa - NATOPEISSTOPEMP"** estiver habilitado.

---

![Imagem 2: Informações adicionais sobre as configurações dessa cidade:](https://ajuda.sankhya.com.br/hc/article_attachments/22589273476247) **Informações adicionais sobre as configurações dessa cidade:**

Além das configurações mencionadas, verifique os seguintes pontos:

![Imagem 3: Certifique-se de que o parâmetro "Usa formatação LC116 do cadastro da cidade? - NFSEFORLC116CI" esteja ativado;](https://ajuda.sankhya.com.br/hc/article_attachments/22589301569175) Certifique-se de que o parâmetro **"Usa formatação LC116 do cadastro da cidade? - NFSEFORLC116CI"** esteja ativado;

![Imagem 4: Na tela Cidades , na aba NFS-e , as marcações "Não formatar LC116" e "Remover zero a esquerda LC116" devem estar…](https://ajuda.sankhya.com.br/hc/article_attachments/22589273508375) Na tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913), na aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e), as marcações **"Não formatar LC116"** e **"Remover zero a esquerda LC116"** devem estar desligadas;

![Imagem 5: Por fim, as informações abaixo devem apresentar o seguinte formato:](https://ajuda.sankhya.com.br/hc/article_attachments/22589273510423) Por fim, as informações abaixo devem apresentar o seguinte formato:

- tag **<ItemListaServico>**01.05**</ItemListaServico>**;
- tag **<CodigoTributacaoMunicipio>**105**</CodigoTributacaoMunicipio>**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22542548874519-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Distrito-Federal#top)
