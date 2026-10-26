---
id: "360045094233"
titulo: "Melhores Práticas para o Uso de 'CT-e - Conhecimento de Transporte Eletrônico'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094233-Melhores-Pr%C3%A1ticas-para-o-Uso-de-CT-e-Conhecimento-de-Transporte-Eletr%C3%B4nico"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T15:51:23Z"
rotulos: ["DUVIDACTE", "CT-e", "Configuração", "ICMS", "Transporte", "TOP", "Substitui documentos fiscais de transporte", "e-CTE para transporte; e-CNPJ para distribuidoras", "Normal Subcontratação Redespacho Intermediário", "Documentos Eletrônicos"]
---

# Melhores Práticas para o Uso de 'CT-e - Conhecimento de Transporte Eletrônico'

O CT-e (Modelo 57) é um documento fiscal eletrônico instituído pelo AJUSTE SINIEF 09/07(25/10/2007), que poderá ser utilizado para substituir um dos seguintes documentos Fiscais:
• Conhecimento de Transporte Rodoviário de Cargas, modelo 8;
• Conhecimento de Transporte Aquaviário de Cargas, modelo 9;
• Conhecimento Aéreo, modelo 10;
• Conhecimento de Transporte Ferroviário de Cargas, modelo 11;
• Nota Fiscal de Serviço de Transporte Ferroviário de Cargas, modelo 27;
• Nota Fiscal de Serviço de Transporte, modelo 7, quando utilizada em transporte de cargas.

A empresa prestadora de serviços de Transporte para emissao de CT-e, e preciso ter um Certificado Digital especifico para CT-e (e-CTE)

Para empresa emissora de NF-e(Distribuidora) e também possui frota própria, pode-se utilizar o Certificado Digital (e-CNPJ), que engloba transmissões de NF-e e CT-e.

**Premissas:**

- CT-e tem somente incidência do Imposto de ICMS. (TOP)

- Configura-se um serviço e vincula um 'Componente do Serviço' ao serviço. No Cadastro do serviço, aba: Geral, campo 'Componente do Serviço', vincula-se o Componente. Em um CT-e pode conter 1 ou mais componentes, de acordo com o processo da empresa.

- Serviço marca-se apenas o cálculo de ICMS.

**Tipos de CT-e (Conhecimento de Transporte Eletrônico)**

Exemplo de um Transporte de um determinado destino e suas varias formas de emitir a CT-e.

- **CT-e Normal - Ponto A ao D**

Usado para movimentação de um ponto A ao D, sem processo de redespacho normal, redespacho intermediário ou subcontratação

Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
Aba: IMPRESSÃO
CT-e = Normal
Tipo de Serviço CT-e = Normal

Neste cenário, a empresa que atua no ramo de prestação de serviço de transporte, irá prestar o serviço em todo o trajeto.

- **CT-e Subcontratação - Ponto A ao D**

Usado para movimentação de um Ponto A ao D, porém com um processo de subcontratação.

Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
Aba: IMPRESSÃO
CT-e = Normal
Tipo de Serviço CT-e = Subcontratação

Neste cenário, a empresa que atua no ramo de prestação de serviço de transporte, irá contratar uma outra empresa para prestar o serviço em todo o trajeto.

- **CT-e Redespacho Intermediário - Ponto B ao C**

Usado para movimentação de um ponto B ao C, utilizando o redespacho intermediário.

Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
Aba: IMPRESSAO
CT-e = Normal
Tipo de Serviço CT-e = Redespacho Intermediário

Neste cenário, a empresa prestadora do serviço de transporte(X), irá transportar de B ao C e uma transportadora terceira que não iniciou o transporte, porém irá transportar até o final do trajeto, até o Destinatário. Existirá 3 transportadoras distintas atuando nesta entrega.

- **CT-e Redespacho Normal- Ponto C ao D**

Usado para movimentação do ponto C ao D, utilizando redespacho normal.

Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
Aba: IMPRESSÃO
CT-e = Normal
Tipo de Serviço CT-e = **Redespacho**

Neste cenário, a transportadora percorrerá apenas uma parte do trecho Ponto A ao C e contrata outra Empresa para finalizar o trajeto até o final, C ao D.

**Observação:**

- Manual do Contribuinte CT-e:
<http://www.cte.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=YIi+H8VETH0=>

- Relação de Tag's extintos no novo Layout CT-e 3.0
