---
id: "35134864204311"
titulo: "Importação de CT-e com a Nota Técnica 2025.002-RTC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35134864204311-Importa%C3%A7%C3%A3o-de-CT-e-com-a-Nota-T%C3%A9cnica-2025-002-RTC"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Importação de documentos fiscais"
atualizado_em: "2026-07-29T16:12:05Z"
rotulos: ["CT-e", "Fiscal", "XML", "Importação", "Reforma Tributária", "Documentos Eletrônicos"]
---

# Importação de CT-e com a Nota Técnica 2025.002-RTC

**Módulo:** Fiscal
**Versão mínima:** 5.15.2 (Módulo Livros Fiscais) · 4.35b190 (Sankhya W)
**Caminho de acesso:** **Comercial › Rotinas › Portal de Importação do XML**

**Você encontra neste artigo:**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/35134864204311-Importa%C3%A7%C3%A3o-de-CT-e-com-a-Nota-T%C3%A9cnica-2025-002-RTC#oque)
- [Como funciona ao importar um CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/35134864204311-Importa%C3%A7%C3%A3o-de-CT-e-com-a-Nota-T%C3%A9cnica-2025-002-RTC#como-funciona)
- [Como usar](https://ajuda.sankhya.com.br/hc/pt-br/articles/35134864204311-Importa%C3%A7%C3%A3o-de-CT-e-com-a-Nota-T%C3%A9cnica-2025-002-RTC#jornada)

---

## O que é e para que serve

Com a implementação da **Nota Técnica 2025.002-RTC**, o [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) foi aprimorado para tratar automaticamente os novos tributos da Reforma Tributária: **CBS (Contribuição sobre Bens e Serviços)**, **IBS (Imposto sobre Bens e Serviços)** e **IS (Imposto Seletivo)**. A atualização automatiza a leitura e o cálculo desses impostos conforme a configuração do [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de importação, garantindo conformidade com as novas diretrizes fiscais.

Com essa funcionalidade, você pode definir se os valores serão importados diretamente do XML ou calculados pelo sistema, e os valores de IBS, CBS e IS ficam sempre visíveis para conferência, validação ou edição a qualquer momento.

---

## Como funciona ao importar um CT-e

O processo é executado em três etapas automáticas:

1. **Leitura automática dos tributos:** o sistema varre o arquivo XML do CT-e, identifica os campos específicos de IBS, CBS e IS e importa os valores diretamente para os campos correspondentes no Sankhya OM.
2. **Cálculo complementar:** caso algum tributo não esteja especificado no XML, o sistema calcula os valores automaticamente com base nas alíquotas previamente configuradas no ambiente, assegurando a conformidade fiscal do documento.
3. **Registro na base de dados:** os valores de IBS, CBS e IS são salvos nos campos apropriados — tanto no cabeçalho quanto nos itens da nota — garantindo rastreabilidade e integração com os módulos fiscais e contábeis.

---

## Como usar

1. Acesse **Comercial › Rotinas › Portal de Importação do XML**.
2. Selecione o arquivo XML do CT-e que deseja importar ou escolha um registro já recebido via MD-e (Manifesto de Documentos Eletrônicos) ou e-mail.
3. Defina a **TOP de importação** que contém a política de cálculo de tributos desejada.
4. Clique em **Processar** e confira os valores na tela de validação.

O tratamento dos tributos depende diretamente da configuração do campo **Cálculo de ICMS, IPI e ISS** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) do cadastro do [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP):

| Configuração na TOP | Como o sistema trata o IBS, CBS e IS |
| --- | --- |
| **Não calcula e não digita** | Ignora os valores, mesmo que presentes no XML. Os tributos não serão considerados nem calculados. |
| **Calcula e digita** | Calcula e registra os tributos com base nas configurações do Sankhya OM, desconsiderando os valores do XML. Permite editar os valores manualmente nas Centrais. |
| **Calcula e não digita** | Calcula e registra os tributos com base nas configurações do Sankhya OM, desconsiderando os valores do XML. Não permite edição manual dos valores. |
| **Não calcula e digita** | Importa e grava apenas os valores já existentes no arquivo XML, sem realizar novos cálculos. |
| **Calcula na confirmação** | Calcula e registra os tributos somente no momento da confirmação da nota, utilizando as alíquotas configuradas no Sankhya OM e ignorando os valores do XML. |

**💡 Dica**

Para entender o contexto completo da Reforma Tributária e os demais recursos relacionados, consulte também:

- [Guia da Reforma Tributária](https://www.sankhya.com.br/guia-reforma-tributaria/#introducao)
- [Glossário de Termos Técnicos Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais)
- [Portal de Importação do XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML)
- [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)
- [Seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/categories/34702076010775-Reforma-tribut%C3%A1ria)
