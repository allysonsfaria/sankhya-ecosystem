---
id: "36236154453655"
titulo: "O que é a tag <modFrete> na NF-e?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36236154453655-O-que-%C3%A9-a-tag-modFrete-na-NF-e"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:23:21Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Transporte", "tag <modFrete>", "CIF", "Por conta do Remetente (CIF)", "Por conta de Terceiros", "Sem frete", "FOB", "Por conta do Destinatário (FOB)", "tipo de frete utilizado na operação", "Transporte Próprio por conta do Remetente", "Transporte Próprio por conta do Destinatário", "Documentos Eletrônicos"]
---

# O que é a tag <modFrete> na NF-e?

A tag `<modFrete>` define o **modo de frete** da NF-e, ou seja, **quem é o responsável pelo transporte da mercadoria**.

Esse campo é obrigatório e precisa ser preenchido corretamente na emissão da nota, a fim de **evitar rejeições da SEFAZ**.

#### Valores diferentes para `<modFrete>`

##### A SEFAZ define valores numéricos padronizados para a tag `<modFrete>` a fim de identificar o tipo de frete utilizado na operação.

##### Esses valores garantem que o sistema compreenda quem paga e executa o transporte, permitindo uma interpretação fiscal e logística correta da nota.

| Valor | Descrição | Responsável |
| --- | --- | --- |
| **0** | **Por conta do Remetente (CIF)** | O remetente (quem está emitindo a nota) contrata e paga o frete para entregar ao destinatário. |
| **1** | **Por conta do Destinatário (FOB)** | O destinatário contrata e paga o frete. |
| **2** | **Por conta de Terceiros** | Um terceiro, diferente de remetente e destinatário, contrata o frete. |
| **3** | **Transporte Próprio por conta do Remetente** | O remetente faz o transporte com veículo próprio. |
| **4** | **Transporte Próprio por conta do Destinatário** | O destinatário faz o transporte com veículo próprio. |
| **9** | **Sem frete** | Não há cobrança de frete. |

###

#### CIF e FOB na prática

Os termos **CIF** e **FOB** são utilizados para definir **quem é o responsável pelo frete** e **até onde vai a responsabilidade do vendedor ou comprador** na entrega da mercadoria.

| Termo | Significado | Responsável pelo frete | Valor `<modFrete>` |
| --- | --- | --- | --- |
| **CIF** | Cost, Insurance and Freight – Por conta do **Remetente** | O vendedor (remetente) é responsável pelo transporte até o destino. | `<modFrete>0</modFrete>` |
| **FOB** | Free On Board – Por conta do **Destinatário** | O comprador (destinatário) é responsável pelo transporte. | `<modFrete>1</modFrete>` |

#### Exemplo no XML

![Imagem 1: Exemplo no XML](https://ajuda.sankhya.com.br/hc/article_attachments/36236154453015)
