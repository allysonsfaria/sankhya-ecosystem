---
id: "360044597494"
titulo: "Ajuste SINIEF 13, de 26 de Julho de 2013"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597494-Ajuste-SINIEF-13-de-26-de-Julho-de-2013"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:27Z"
rotulos: ["AJUDA DO SKW", "Configuração", "CONFAZ", "Nota de Empenho", "SINIEF", "Ajuste SINIEF 13", "de 26 de Julho de 2013 manual", "Parceiro", "NF-e", "XML", "TOP", "Ajuste SINIEF 13: Novas Configurações", "Documentos Eletrônicos"]
---

# Ajuste SINIEF 13, de 26 de Julho de 2013

Visando o atendimento ao ajuste estabelecido pela CONFAZ (Conselho Nacional de Política Fazendária), que estabeleceu procedimentos relacionados à entrega de bens e mercadorias a terceiros, adquiridos por órgãos ou entidades da Administração Pública Direta da União, dos Estados, do Distrito Federal e dos Municípios, bem como suas autarquias e fundações públicas, algumas novas configurações deverão ser realizadas em nosso sistema, de modo a respeitar o estabelecido pelo Conselho.

As configurações a serem revistas são:

Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce), observe o campo **"Gerar endereço de entrega no XML da NF-e"**. Ele pode ser definido dentre três opções, são elas:

- **Nenhum:** Selecionando essa opção, não será gerada a tag **<entrega>** no XML da NF-e.
- **Parceiro principal:** Por esta opção, serão utilizadas as informações de entrega do parceiro da nota, referentes aos dados complementares do Parceiro; além de gerar a tag **<entrega>** no XML da NF-e com estas informações.
- **Parceiro destinatário:** Através dessa opção, são utilizadas as informações de entrega geradas a partir dos dados para o parceiro destinatário; caso não existam informações nos dados complementares, as informações usadas para geração da tag **<entrega>** serão do próprio Cadastro do Parceiro Destinatário.

![Imagem 1: Parceiro destinatário: Através dessa opção, são utilizadas as informações de entrega geradas a partir dos dados para o…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002040901)

No lançamento de uma NF-e, temos o campo **"Nota de Empenho"\*** (lembrando que este campo deve ser previamente inserido no layout da nota), onde informamos a numeração da nota de empenho; uma vez que você preencher este campo, fará com que a tag **<xNEmp>** seja gerada no XML da NF-e.

![Imagem 2: No lançamento de uma NF-e, temos o campo "Nota de Empenho" * (lembrando que este campo deve ser previamente inserido no…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001985482)

**\*** É uma ordem de serviço em que determinada transação teve sua realização autorizada, e teve o comprometido de pagamento. Sem esse documento, a empresa que executou os serviços ou vendeu as mercadorias não receberá os valores devidos. Essa nota de empenho é utilizada por órgãos públicos, por ocasião das concorrências e cartas convites (licitações em geral).
