---
id: "35135179341463"
titulo: "Processo Importação de NF-e com a Nota Técnica 2025.002 - RTC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35135179341463-Processo-Importa%C3%A7%C3%A3o-de-NF-e-com-a-Nota-T%C3%A9cnica-2025-002-RTC"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Importação de documentos fiscais"
atualizado_em: "2026-07-29T16:12:07Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "Impostos", "TOP", "Reforma Tributária"]
---

# Processo Importação de NF-e com a Nota Técnica 2025.002 - RTC

**Módulo:** Comercial
**Caminho de acesso:** Menu Principal › Comercial › Rotinas › Portal de Importação do XML
**Versão mínima:** 5.15.2 (Módulo Livros Fiscais) · 4.35b190 (Sankhya W)

---

## O que é e para que serve

O [**Portal de Importação do XML**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) foi atualizado com a **Nota Técnica 2025.002-RTC** para reconhecer e processar automaticamente os tributos da Reforma Tributária — Contribuição sobre Bens e Serviços (CBS), Imposto sobre Bens e Serviços (IBS) e Imposto Seletivo (IS) — em Notas Fiscais Eletrônicas (NF-e). O sistema lê os valores diretamente do XML, aplica as regras fiscais vigentes e registra todas as informações de forma integrada, eliminando cálculos e preenchimentos manuais. O portal não realiza lançamentos contábeis nem substitui a validação da política fiscal interna da sua empresa.

---

## Como importar uma NF-e

1. Acesse **Menu Principal › Comercial › Rotinas › Portal de Importação do XML**.
2. Selecione o arquivo XML da NF-e ou escolha um registro já recebido via MD-e (Manifesto de Documentos Eletrônicos) ou e-mail.
3. Clique em **Processar**.
4. Valide as informações e possíveis divergências na tela de conferência e confirme a importação.

Durante o processamento, o sistema executa as seguintes etapas automaticamente:

- **Leitura dos tributos:** identifica os campos de IBS, CBS e IS no XML e armazena os valores no Sankhya Om.
- **Cálculo complementar:** se o fornecedor não informar algum dos tributos no XML, o sistema calcula automaticamente usando as alíquotas configuradas no Sankhya Om.
- **Registro na base de dados:** grava os valores — lidos ou calculados — nos campos corretos do cabeçalho e dos itens da nota, garantindo rastreabilidade e integração com os módulos fiscais e contábeis.
- **Exibição para conferência:** apresenta os valores de IBS, CBS e IS de forma destacada na tela de conferência, permitindo validação e edição conforme a configuração do sistema.

---

## Como a TOP define o tratamento dos tributos

O tratamento de IBS, CBS e IS durante a importação depende da configuração do campo **Cálculo de ICMS, IPI e ISS** na aba [**Impostos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) do cadastro do [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP):

| Configuração na TOP | Como o sistema trata IBS, CBS e IS |
| --- | --- |
| **Não calcula e não digita** | Ignora completamente os valores, mesmo que presentes no XML. Os tributos não são considerados nem calculados. |
| **Calcula e não digita** | Calcula e registra os tributos com base nas configurações do Sankhya Om, desconsiderando os valores do XML. Não permite edição manual. |
| **Calcula e digita** | Calcula os tributos e os apresenta na tela de importação. Você pode validar, editar ou optar por usar os valores originais do XML. |
| **Não calcula e digita** | Importa e grava apenas os valores de IBS, CBS e IS que constam no XML, sem realizar nenhum cálculo adicional. |
| **Calcula na confirmação** | Executa o cálculo dos tributos somente no momento da confirmação da nota, usando as alíquotas do Sankhya Om e desconsiderando os valores do XML. |

**💡 Dica**

Para mais informações sobre o Portal de Importação do XML, acesse [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML). Para o contexto legislativo dos tributos, consulte o [Glossário de Termos Técnicos Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais), o [Guia da Reforma Tributária](https://www.sankhya.com.br/guia-reforma-tributaria/#introducao) e a [Seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/categories/34702076010775-Reforma-tribut%C3%A1ria) na Central de Ajuda.
