---
id: "39351023777943"
titulo: "Os valores de IBS/CBS não estão sendo gerados no XML da Nota Fiscal de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39351023777943-Os-valores-de-IBS-CBS-n%C3%A3o-est%C3%A3o-sendo-gerados-no-XML-da-Nota-Fiscal-de-Servi%C3%A7o"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-09-25T02:25:56Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Artigo criado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Docs Eletrônicos - KCS"]
---

# Os valores de IBS/CBS não estão sendo gerados no XML da Nota Fiscal de Serviço

**MENSAGEM**

Os impostos IBS e CBS estão sendo calculados corretamente no sistema, porém não constam no arquivo XML da nota fiscal emitida.

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço (NFS)** em ambiente de produção, o usuário verifica que os tributos **IBS (Imposto sobre Bens e Serviços)** e **CBS (Contribuição sobre Bens e Serviços)** são calculados corretamente pelo motor de cálculo do sistema. No entanto, ao consultar o arquivo XML da nota fiscal emitida e transmitida, as tags correspondentes ao **IBS** e à **CBS** não são apresentadas.

A situação pode ocorrer mesmo quando todas as configurações necessárias para a **Reforma Tributária** já foram realizadas, incluindo a parametrização de **alíquotas**, **cClassTrib** e **CST** dos novos tributos.

**SOLUÇÃO**

**(1)** Acesse a nota pelo Portal de Vendas e abra-a na Central de Vendas. Em seguida, localize a **grade de Itens** da nota e acesse a aba **Consultar/Alterar Dados do Imposto do Item da Nota**.

Confirme se os tributos **IBS** e **CBS** estão sendo calculados corretamente.

**(2)** Verifique se os campos relacionados à **Reforma Tributária** estão devidamente preenchidos no cadastro do serviço (Aba > Serviços), incluindo as informações necessárias para o cálculo do **IBS** e da **CBS**.

![Imagem 1: No Portal de Vendas , acesse botão NFS-e > Gerar JSON e consulte o arquivo JSON da nota para verificar se as…](https://ajuda.sankhya.com.br/hc/article_attachments/43680805196695)

**(3)** No **Portal de Vendas**, acesse botão **NFS-e > Gerar JSON** e consulte o arquivo JSON da nota para verificar se as informações referentes aos tributos **IBS** e **CBS** estão sendo geradas corretamente.

**(4)** Para validar se as notas fiscais estão sendo geradas com as informações corretas.

**CAUSA**

O sistema **Sankhya** já está preparado para calcular e gerar os grupos de tributos **IBS**, **CBS** e **IS**, conforme as **Notas Técnicas da Reforma Tributária**. No entanto, o **XML de retorno do Portal Nacional** não apresenta essas tags enquanto não houver obrigatoriedade estabelecida para sua inclusão.
