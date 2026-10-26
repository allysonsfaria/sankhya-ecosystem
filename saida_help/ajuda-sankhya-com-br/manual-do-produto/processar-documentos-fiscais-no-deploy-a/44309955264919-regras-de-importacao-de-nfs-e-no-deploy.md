---
id: "44309955264919"
titulo: "Regras de importação de NFS-e no Deploy Agent"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44309955264919-Regras-de-importa%C3%A7%C3%A3o-de-NFS-e-no-Deploy-Agent"
trilha: "Manual do Produto > Inteligência e Análise > Deploy Agent > Processar documentos fiscais no Deploy Agent"
atualizado_em: "2026-10-21T21:03:54Z"
---

# Regras de importação de NFS-e no Deploy Agent

## O que é e para que serve

A importação de NFS-e (Nota Fiscal de Serviços Eletrônica) no Deploy Agent traz para o Sankhya Om as notas de serviço que o cliente já emitiu ou tomou, com prestador, tomador, serviços e tributos municipais.

Este artigo reúne as regras que o Deploy Agent aplica na importação.

## Conversão por IA

Como o formato da NFS-e varia entre municípios, cada nota é padronizada por IA num formato único antes do processamento. Os campos desse formato estão em **Referência técnica**, no fim deste artigo.

Campos não preenchidos na nota de origem não são aproveitados, desde que as informações exigidas estejam presentes.

## Informações exigidas

A nota só é processada com estas informações:

- **Sempre exigidas:** número da nota, data de emissão, razão social do prestador, logradouro e CEP do prestador, razão social do tomador, logradouro e CEP do tomador, e valor do serviço.
- **Exigidas em grupo** (basta uma opção do grupo):
  - identificação do prestador: CNPJ ou CPF;
  - identificação do tomador: CNPJ, CPF ou identificação de tomador estrangeiro;
  - classificação do serviço: item da lista de serviços, CNAE ou código de tributação do município.

Um serviço só é considerado quando tem valor: serviço sem valor não gera item na nota.

## Nota própria e nota tomada

A empresa da nota é localizada pela identificação do prestador, em nota própria, ou do tomador, em nota tomada. Ela precisa estar cadastrada no Sankhya Om; se não for localizada, o processamento falha.

| Cenário | Parceiro cadastrado | Tipo de operação |
| --- | --- | --- |
| Nota própria, emitida pela empresa | Tomador | Venda de serviço |
| Nota tomada, sem retenção de ISS | Prestador | Compra de serviço sem retenção |
| Nota tomada, com retenção de ISS | Prestador | Compra de serviço com retenção |

A retenção é reconhecida quando a nota indica ISS retido pelo tomador, inclusive nas notas emitidas pelo ambiente nacional. A associação do CNAE à empresa só acontece em nota própria.

## Número e valor da nota

- **Número:** quando o RPS tem número válido, ele é usado como número da nota. Caso contrário, a nota é registrada sem número de origem.
- **Valor total:** é a soma dos serviços, com preferência pelo valor líquido e, na falta dele, pelo valor bruto. O total informado no cabeçalho da nota não sobrescreve esse cálculo.

## O que é cadastrado ou atualizado no Sankhya Om

O processamento acontece em duas etapas:

| Etapa | O que é processado |
| --- | --- |
| **1. Cadastros básicos** | País, estado, cidade, bairro, CEP, endereço, empresa, parceiro, classificação da operação e serviço |
| **2. Nota e movimentos** | Cabeçalho, itens, financeiro, ISS, demais impostos retidos e arquivos da nota |

A partir da nota, o Deploy Agent cria ou atualiza:

- **Parceiro:** com razão social, nome fantasia, identificação, inscrições, telefone, e-mail e endereço (país, estado, cidade, bairro, CEP e logradouro).
- **Serviço:** criado quando ainda não existe, a partir da classificação e da discriminação da nota.
- **Empresa:** passa a calcular IRRF, FUNRURAL e ISS, é registrada como participante do fluxo de NFS-e e recebe o regime especial de tributação do ISS como padrão. A inscrição municipal informada na nota é gravada nos dados da empresa.
- **Nota fiscal:** cabeçalho (número, data, série, código de verificação, discriminação) e um item por serviço, com valor e ISS.
- **Financeiro:** o título correspondente, a partir da data de emissão e do valor total dos serviços.
- **Impostos:** ISS e retenções de PIS, COFINS, IRRF, INSS e CSLL. Para cada tributo retido com valor maior que zero, é criada a configuração entre serviço, operação e imposto.

## Referência técnica: XML padronizado da NFS-e

Cada NFS-e municipal é normalizada por IA para este formato único antes de ser processada. Use esta referência na integração e no preparo dos arquivos.

Saída no Sankhya Om por bloco do XML padronizado:

| Bloco do XML | O que é gerado ou atualizado |
| --- | --- |
| Identificação da nota | Cabeçalho: número, data, série, código de verificação, discriminação |
| Serviços | Itens da nota, com valor e ISS por item |
| Serviços e identificação | Título financeiro, a partir do valor total e da data de emissão |
| ISS do serviço | Configuração de ISS por serviço e operação |
| Impostos retidos do serviço | Configuração das retenções de PIS, COFINS, IRRF, INSS e CSLL |
| Identificação da nota e ISS | Arquivos da nota armazenados no ERP |
| Prestador ou tomador | Parceiro, com razão social, identificação, inscrições, telefone e e-mail |
| Serviços | Serviço, criado quando ainda não existe |
| ISS do serviço | Tipo de operação aplicado à nota |
| Serviços | CNAE associado à empresa, apenas em nota própria |
| Prestador | Configurações da empresa, incluindo inscrição municipal e parâmetros de ISS |
| Endereço | Endereço, bairro, cidade, estado, país e CEP |

Legenda de obrigatoriedade: **Obrigatório** (o campo precisa estar presente), **Grupo** (ao menos um campo do grupo precisa estar presente), **Opcional** (aproveitado quando presente).

Estrutura geral:

```
<nfse>
  <rps/>
  <prestador>
    <endereco/>
  </prestador>
  <tomador>
    <endereco>
      <exterior/>
    </endereco>
  </tomador>
  <servicos>
    <item>
      <iss/>
    </item>
    ...
  </servicos>
</nfse>
```

Clique nas opções abaixo para expandir as tags de cada bloco:

**🔹Identificação da nota**

Tags sob a raiz `<nfse>`:

| Tag | Tipo | Obrigatoriedade | Descrição |
| --- | --- | --- | --- |
| `<numero>` | inteiro | Obrigatório | Número da nota |
| `<dataEmissao>` | data | Obrigatório | Data de emissão |
| `<serie>` | texto | Opcional | Série da nota |
| `<ufPrestacao>` | texto | Opcional | UF de prestação |
| `<cidadePrestacao>` | texto | Opcional | Cidade de prestação |
| `<codigoIBGEPrestacao>` | texto | Opcional | Código do município de prestação |
| `<municipioGerador>` | texto | Opcional | Município que gerou a nota |
| `<baseISSTotal>` | numérico | Opcional | Base do ISS total da nota |
| `<valorISSTotal>` | numérico | Opcional | Valor do ISS total da nota |
| `<valorTotalServicos>` | numérico | Opcional | Valor total dos serviços |
| `<infoComplementar>` | texto | Opcional | Informações complementares |

**🔹RPS**

Tags sob `<nfse><rps>`: `<numero>` (inteiro, opcional), `<serie>` (texto, opcional), `<dataEmissao>` (data, opcional).

**🔹Prestador**

Tags sob `<nfse><prestador>`:

| Tag | Tipo | Obrigatoriedade | Descrição |
| --- | --- | --- | --- |
| `<razaoSocial>` | texto | Obrigatório | Razão social |
| `<nomeFantasia>` | texto | Opcional | Nome fantasia |
| `<cnpj>` | texto | Grupo | CNPJ |
| `<cpf>` | texto | Grupo | CPF |
| `<inscricao>` | texto | Opcional | Inscrição municipal |
| `<telefone>` | texto | Opcional | Telefone |
| `<email>` | texto | Opcional | E-mail |

Grupo de identificação do prestador: ao menos `<cnpj>` ou `<cpf>`.

Endereço do prestador (`<nfse><prestador><endereco>`): `<logradouro>` e `<cep>` obrigatórios; `<tipoLogradouro>`, `<numero>`, `<complemento>`, `<bairro>`, `<cidade>`, `<codigoIBGE>` e `<uf>` opcionais.

**🔹Tomador**

Tags sob `<nfse><tomador>`:

| Tag | Tipo | Obrigatoriedade | Descrição |
| --- | --- | --- | --- |
| `<razaoSocial>` | texto | Obrigatório | Razão social |
| `<nomeFantasia>` | texto | Opcional | Nome fantasia |
| `<cnpj>` | texto | Grupo | CNPJ |
| `<cpf>` | texto | Grupo | CPF |
| `<idEstrangeiro>` | texto | Grupo | Identificação de tomador estrangeiro |
| `<telefone>` | texto | Opcional | Telefone |
| `<email>` | texto | Opcional | E-mail |

Grupo de identificação do tomador: ao menos `<cnpj>`, `<cpf>` ou `<idEstrangeiro>`.

Endereço do tomador (`<nfse><tomador><endereco>`): `<logradouro>` e `<cep>` obrigatórios; `<tipoLogradouro>`, `<numero>`, `<complemento>`, `<bairro>`, `<cidade>`, `<codPais>`, `<codigoIBGE>` e `<uf>` opcionais. Para tomador estrangeiro, `<exterior>` traz `<codPais>` e `<nomePais>` (ambos opcionais).

**🔹Serviços**

Tags sob `<nfse><servicos><item>`, um por serviço da nota; um `<item>` só é gerado quando há `<valor>`:

| Tag | Tipo | Obrigatoriedade | Descrição |
| --- | --- | --- | --- |
| `<valor>` | numérico | Obrigatório | Valor do serviço |
| `<itemLista>` | texto | Grupo | Item da lista de serviços |
| `<cnae>` | texto | Grupo | Código CNAE |
| `<codigoTribMunicipio>` | numérico | Grupo | Código de tributação do município |
| `<discriminacao>` | texto | Opcional | Discriminação do serviço |
| `<valorLiquido>` | numérico | Opcional | Valor líquido |
| `<valorDeducoes>` | numérico | Opcional | Valor das deduções |
| `<pis>`, `<cofins>`, `<irrf>`, `<inss>`, `<csll>` | numérico | Opcional | Tributos retidos |

Grupo de classificação do serviço: ao menos `<itemLista>`, `<cnae>` ou `<codigoTribMunicipio>`.

ISS do serviço (`<nfse><servicos><item><iss>`): `<aliquota>`, `<base>`, `<valor>`, `<valorRetido>`, `<retido>` (booleano) e `<retidoNacional>` (numérico), todos opcionais.

> **ℹ️ Nota**
>
> O bloco `<servicos>` é sempre gerado primeiro; a ordem dos demais blocos não é determinística. Use seletores por nome de tag, nunca por posição. Valores monetários e alíquotas usam ponto como separador decimal, sem formatação de moeda. O indicador de retenção no padrão nacional é numérico e distinto do indicador booleano de ISS retido: concilie a representação desse indicador entre o formato gerado pela IA e as regras de consumo no ERP.

Clique nas opções abaixo para expandir os exemplos de XML:

**🔹Exemplo com um serviço, prestador e tomador nacionais**

```
<?xml version="1.0" encoding="UTF-8"?>
<nfse>
  <servicos>
    <item>
      <cnae>6201501</cnae>
      <codigoTribMunicipio>620150</codigoTribMunicipio>
      <cofins>115.00</cofins>
      <csll>45.00</csll>
      <discriminacao>Desenvolvimento de software sob demanda conforme contrato 2026/001</discriminacao>
      <inss>55.00</inss>
      <irrf>50.00</irrf>
      <iss>
        <aliquota>5.00</aliquota>
        <base>5000.00</base>
        <retido>true</retido>
        <retidoNacional>1</retidoNacional>
        <valor>250.00</valor>
        <valorRetido>250.00</valorRetido>
      </iss>
      <itemLista>01.01</itemLista>
      <pis>25.00</pis>
      <valor>5000.00</valor>
      <valorDeducoes>0.00</valorDeducoes>
      <valorLiquido>4510.00</valorLiquido>
    </item>
  </servicos>
  <numero>12345</numero>
  <dataEmissao>2026-06-16</dataEmissao>
  <serie>A</serie>
  <ufPrestacao>SP</ufPrestacao>
  <cidadePrestacao>3550308</cidadePrestacao>
  <codigoIBGEPrestacao>3550308</codigoIBGEPrestacao>
  <municipioGerador>3550308</municipioGerador>
  <valorTotalServicos>6000.00</valorTotalServicos>
  <infoComplementar>Contrato firmado em 01/01/2026. Pagamento em 30 dias.</infoComplementar>
  <rps>
    <numero>100</numero>
    <serie>RPS</serie>
    <dataEmissao>2026-06-10</dataEmissao>
  </rps>
  <prestador>
    <razaoSocial>Empresa XYZ Tecnologia Ltda</razaoSocial>
    <nomeFantasia>XYZ Tech</nomeFantasia>
    <cnpj>12345678000190</cnpj>
    <inscricao>1234567</inscricao>
    <telefone>11999999999</telefone>
    <email>contato@xyztech.com.br</email>
    <endereco>
      <tipoLogradouro>Av</tipoLogradouro>
      <logradouro>Paulista</logradouro>
      <numero>1000</numero>
      <complemento>Sala 101</complemento>
      <bairro>Bela Vista</bairro>
      <cidade>São Paulo</cidade>
      <codigoIBGE>3550308</codigoIBGE>
      <cep>01310100</cep>
      <uf>SP</uf>
    </endereco>
  </prestador>
  <tomador>
    <razaoSocial>Cliente ABC S/A</razaoSocial>
    <nomeFantasia>ABC Industrias</nomeFantasia>
    <cnpj>98765432000110</cnpj>
    <telefone>11888888888</telefone>
    <email>fiscal@abcsa.com.br</email>
    <endereco>
      <tipoLogradouro>Rua</tipoLogradouro>
      <logradouro>das Flores</logradouro>
      <numero>50</numero>
      <complemento>Apto 3</complemento>
      <bairro>Centro</bairro>
      <cidade>Campinas</cidade>
      <codPais>BR</codPais>
      <codigoIBGE>3509502</codigoIBGE>
      <cep>13010001</cep>
      <uf>SP</uf>
    </endereco>
  </tomador>
</nfse>
```

**🔹Exemplo de tomador estrangeiro**

```
<tomador>
  <razaoSocial>Foreign Client Corp</razaoSocial>
  <idEstrangeiro>PASS123456</idEstrangeiro>
  <email>client@foreigncorp.com</email>
  <endereco>
    <logradouro>5th Avenue</logradouro>
    <numero>350</numero>
    <cidade>New York</cidade>
    <cep>10118</cep>
    <exterior>
      <codPais>840</codPais>
      <nomePais>Estados Unidos</nomePais>
    </exterior>
  </endereco>
</tomador>
```

#### Saiba mais

- [Conheça o Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/43952524117911): visão geral, abas, indicadores e arquivos processados.
- [Enviar e reprocessar documentos fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309970843159): envio de arquivos, reprocessamento e tratamento de erros.
- [Limites e dúvidas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309955184663): pontos de atenção e perguntas frequentes sobre o Deploy Agent.
