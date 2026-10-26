---
id: "27173707142679"
titulo: "Veja como importar uma Nota Fiscal utilizando os impostos do arquivo XML e mantendo o CST do IPI informado na TOP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27173707142679-Veja-como-importar-uma-Nota-Fiscal-utilizando-os-impostos-do-arquivo-XML-e-mantendo-o-CST-do-IPI-informado-na-TOP"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-09-03T14:13:28Z"
rotulos: ["Configuração", "NF-e", "XML", "Impostos", "TOP", "mportar uma Nota Fiscal utilizando os impostos do arquivo XML", "mantendo o CST do IPI informado na TOP", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Veja como importar uma Nota Fiscal utilizando os impostos do arquivo XML e mantendo o CST do IPI informado na TOP

#### SITUAÇÃO:

O Portal de Importação de XML permite definir se os impostos serão calculados pelo sistema ou importados exatamente como constam no arquivo XML.

Para evitar divergências fiscais e preservar os valores de ICMS, IPI, PIS, COFINS (além de IBS, CBS e IS nas versões compatíveis), configure o Tipo de Operação (TOP) para utilizar a opção **"Não calcula e digita".**

#### **(1)**Quando utilizar esta configuração?

Utilize esta configuração quando a empresa desejar:

- Importar os valores de impostos exatamente como emitidos pelo fornecedor;
- Evitar recálculos automáticos durante a importação;
- Reduzir divergências entre o XML e a nota lançada no sistema.

#### **(1)**Como funciona a configuração da TOP

A definição é realizada em:

Comercial → Arquivo → Cadastros → Tipos de Operação (TOP) → Aba Impostos

As opções disponíveis são:

| Configuração | Comportamento |
| --- | --- |
| Calcula e digita | Permite escolher entre usar os impostos do Sistema ou do Arquivo quando houver divergência. |
| Não calcula e digita | Importa os impostos do XML (recomendado). |
| Calcula e não digita | Calcula os impostos e ignora os valores do XML. |
| Não calcula e não digita | Não calcula nem importa os novos impostos. |
| Calcula na confirmação | Os impostos são calculados somente na confirmação da nota. |

#### **(1)**Configuração recomendada para utilizar os impostos do arquivo XML

Para garantir que os valores de impostos sejam importados exatamente como constam no XML e aplicar essa regra para todas as notas que utilizarem a mesma TOP, siga os passos abaixo:

**(1)** Acesse a tela de **"TOP"** (Comercial> Arquivo> Cadastro> Tipos de Operação ) e localize a TOP utilizada nas importações de notas fiscais.

**(2)** Na Aba Impostos, localize o campo **"Cálculo de ICMS, IPI, ISS, IBS, CBS e IS"**.

**(3)** Selecione a opção "**Não calcula e digita**" e salve a alteração.

Dessa forma, o Portal de Importação utilizará automaticamente os valores do XML, sem apresentar a escolha entre Sistema e Arquivo.

###

#### **(1)**Tratamento do CST de IPI

Além da configuração da TOP, o Portal de Importação possui uma preferência que permite converter o CST de IPI informado no XML durante a importação.

**Portal de Importação de XML > Outras Opções > Preferências para Importar NFe > Realizar conversão do CST de IPI do XML**

![Imagem 1: Portal de Importação de XML > Outras Opções > Preferências para Importar NFe > Realizar conversão do CST de IPI do XML](https://ajuda.sankhya.com.br/hc/article_attachments/43198767176343)

Quando essa preferência estiver habilitada, o sistema realizará a conversão do CST conforme a Tabela de Conversão de CST de IPI.

Exemplo:

- CST de IPI no XML: 50
- CST importado: 00 (de acordo com a tabela de conversão)

**(2)** Existe ainda o parâmetro **PADCSTIPITOPNCD – Padrão CST.IPI pela TOP com Não Calcula e Digita?**

Quando este parâmetro estiver habilitado, o sistema assumirá o CST de IPI configurado na TOP, mesmo utilizando a opção Não calcula e digita.

Caso seja necessário manter o CST de IPI informado no XML, verifique a preferência de conversão e o parâmetro PADCSTIPITOPNCD, pois essas configurações podem alterar o CST durante a importação.

#### **(1)**Importante

- Aplicação global: a configuração da TOP será aplicada às importações que utilizarem essa TOP.
- Grupos fiscais: o sistema processa corretamente os grupos gCompra e gTrib, incluindo reduções de base e diferimento quando presentes no XML.
- Novos tributos: versões compatíveis com a Nota Técnica 2025.001-RTC v1.05b também importam os tributos IBS, CBS e IS diretamente do XML.
- Despesas acessórias: caso existam alertas de divergência, confirme se a TOP está configurada como **Não calcula e digita** e revise as preferências de importação do CST de IPI.

####
