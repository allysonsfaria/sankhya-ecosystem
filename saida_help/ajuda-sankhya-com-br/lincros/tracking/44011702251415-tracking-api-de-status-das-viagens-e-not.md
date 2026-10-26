---
id: "44011702251415"
titulo: "[Tracking] API de Status das Viagens e Notas Fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011702251415--Tracking-API-de-Status-das-Viagens-e-Notas-Fiscais"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T19:09:27Z"
rotulos: ["sync_hc", "lincros", "lincros_13434772", "sync_hash_b333b2c39378"]
---

# [Tracking] API de Status das Viagens e Notas Fiscais

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/44011702503191)

A API pode ser utilizada para retornar informações básicas das rotas e das entregas para o consumo de aplicações externas. É possível requisitar informações sobre:

- Viagens e Entregas
- Viagens e Entregas Detalhadas
- Notas Fiscais
- Itens das Notas Fiscais.

O Lincros Tracking possui quatro APIs que podem ser usadas para extração de dados das viagens;

- **StatusRotas:** Retorna à situação de todas as viagens e todas as entregas;
- **StatusRotasDetalhado:** Retorna à situação de todas as viagens, entregas, notas fiscais e itens das notas fiscais;
- **StatusNotasFiscais:** Retorna a situação de todas as novas fiscais passadas pelo parâmetro do código da entrega;
- **StatusItensNotasFiscais:**Retorna a situação de todos os itens das notas fiscais passadas pelo parâmetro;

## StatusRotas

- **URL**: [http://cliente-tracking.lincros.com/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=XXX&senha=X](http://172.30.8.31:5301/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=brf&senha=brf@123)XXXX

  - Obs: Deve ser informado o nome do cliente:

    - [http://NOMECLIENTE-tracking](http://cliente-tracking.lincros.com)
  - Obs²: Informar o usuário e senha

    - [usuario=XXX&senha=X](http://172.30.8.31:5301/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=brf&senha=brf@123)XXXX
- **Método**: GET
- **Parâmetros**: usuario, senha
- **Retorno**:

[

    {

        "CodigoRota": 1060,

        "CodigoRotaNegocio": 1845684,

        "Data": "30/09/2019 00:00:00",

        "DataUltimaAtividade": "01/10/2019 15:56:58",

        "Situacao": "Finalizada",

        "PlacaVeiculo": "ODB2089",

        "EntregasPrevistas": 15,

        "EntregasRealizadas": 15,

        "listRetornoEntregas": [

            {

                "Codigo": 7193,

                "CodigoRota": 1060,

                "Cliente": "IBIRACU COMERCIAL LTDA.",

                "CodigoCliente": "10002651",

                "Data": "30/09/2019 00:00:00",

                "DataRealizada": "30/09/2019 08:08:07",

                "Sequencia": 1,

                "SequenciaCorreta": true,

                "Devolvido": false,

                "Revertida": false,

                "Realizada": true,

                "MotivoDevolucao": "-",

                "CodigoMotivoDevolucao": null,

                "MotivoDevolucaoCentral": "-",

                "CodigoMotivoDevolucaoCentral": null,

                "BaldeioAutomatico": false,

                "Status": 2

            },

]

        "listRetornoColetas": []

    }

]

O campo **Status** é um enumerador, com o seguinte significado:

| Status | Descrição | Detalhe |
| --- | --- | --- |
| 1 | EntregaPendente | Entrega encontra-se pendente |
| 2 | Realizada | Entrega foi confirmada |
| 3 | DevolucaoNaoTratada | Devolução não tratada na atividade de entrega no   cliente |
| 4 | DevolucaoAceita | Devolução tratada como **aceita** pela Equipe de   Monitoramento |
| 5 | Reentrega | Devolução tratada como **reentrega** pela Equipe de   Monitoramento |
| 6 | RetornoAutorizado | Devolução tratada como **revertida** pela Equipe de   Monitoramento |
| 7 | Revertida | Devolução **revertida em entrega** confirmada pelo   motorista |

## StatusRotasDetalhado

- **URL**: [http://cliente-tracking.lincros.com/WS/Retorno.svc/RetornoWeb/StatusRotasDetalhado?usuario=XXX&senha=X](http://172.30.8.31:5301/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=brf&senha=brf@123)XXXX

  - Obs: Deve ser informado o nome do cliente:

    - [http://NOMECLIENTE-tracking](http://cliente-tracking.lincros.com)
  - Obs²: Informar o usuário e senha

    - [usuario=XXX&senha=X](http://172.30.8.31:5301/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=brf&senha=brf@123)XXXX
- **Método**: GET
- **Parâmetros**: usuario, senha, codigoRotaNegocio, dataRota + placa, dataUltimaAtividade, dataRota + situacaoEntrega, codigoNotaFiscal, pnp, itemNF

| Parâmetro | Exemplo |
| --- | --- |
| codigoRotaNegocio | /StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&codigoRotaNegocio=114351974 |
| dataRota + placa | /StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&placa=FST8027&dataRota=2019-08-14 |
| dataRota + situacaoEntrega | /StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&dataRota=2019-08-14&situacaoEntrega=3 |
| dataUltimaAtividade | /StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&dataUltimaAtividade=2019-10-29 |
| codigoNotaFiscal | /StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&codigoNotaFiscal=003246391 |
| codigoUnidadeNegocio + dataRota | /StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&codigoUnidadeNegocio =APU&dataRota=2020-03-17 |
| codigoNotaFiscal + codigoUnidadeNegocio | /StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&codigoNotaFiscal=003246310&codigoUnidadeNegocio =APU |
| pnp | /WS/Retorno.svc/RetornoWeb/StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&dataRota=2020-07-03&pnp=true |
| itemNF | /WS/Retorno.svc/RetornoWeb/StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&dataRota=2020-07-03&itemNF=true |
| dataRotaInicial + dataRotaFinal | /WS/Retorno.svc/RetornoWeb/StatusRotasDetalhado?usuario=lincros&senha=LkJsi!$23&dataRotaInicial=2020-11-09&dataRotaFinal=2020-11-10 |

**Obs**:  A partir da versão 4.0.1, os parâmetros pnp e itemNF foram disponibilizados caso seja necessário limitar a quantidade de informações retornadas na pesquisa, consequentemente diminuindo o tempo de resposta da requisição.

Estes parâmetros podem ser combinados na requisição com todos os demais parâmetros. Segue abaixo descrição de comportamento dos mesmos.

- **pnp**: quando **true**, deve gerar dados nos campos QtdPnpGeradas e QtdPnpTratadas; quanto **false**, não deve considerar estes campos na consulta da request;
- **itemNF**: quando **true**, deve gerar dados dos itens das notas; quando **false**, não deve considerar estes campos na consulta da request;

Se nenhum dos dois parâmetros for informado, por padrão serão considerados **true**

O parâmetro **Situação** disponível na estrutura da **Entrega**, **Nota Fiscal** e **Item** é um discriminator, com o seguinte significado:

| Situação | Descrição | Detalhe |
| --- | --- | --- |
| 1 | NaoApontado | Atividade de entrega encontra-se pendente |
| 2 | NaoEntregue | Atividade de entrega encontra-se pendente ou foi devolvida |
| 3 | Devolvido | Atividade de **devolução não tratada** ou **tratada como aceita** no cliente |
| 4 | Entregue | Atividade de entrega confirmada |
| 5 | Revertido | Atividade de devolução em que foi autorizado o retorno do motorista ao cliente para nova tentativa de entrega |
| 6 | DevolvidaParcialmente | Atividade de devolução confirmada parcialmente |
| 7 | RevertidaParcialmente | Atividade de devolução em que a entrega foi confirmada parcialmente |

O campo **Status** é um enumerator, com o seguinte significado:

| Status | Descrição | Detalhe |
| --- | --- | --- |
| 1 | EntregaPendente | Atividade de entrega encontra-se pendente. |
| 2 | Realizada | Atividade de entrega confirmada. |
| 3 | DevolucaoNaoTratada | Atividade de entrega devolvida **não tratada** pela Equipe de Monitoramento |
| 4 | DevolucaoAceita | Atividade de entrega devolvida tratada como **aceita** pela Equipe de Monitoramento |
| 5 | Reentrega | Atividade de entrega devolvida tratada como reentrega pela Equipe de Monitoramento |
| 6 | RetornoAutorizado | Atividade de entrega devolvida tratada como revertida pela Equipe de Monitoramento |
| 7 | Revertida | Atividade de entrega devolvida revertida em entrega confirmada pelo Motorista |

O campo **IdAcaoDevolucao** é um enumerador em que:

| Id | Descrição | Detalhe |
| --- | --- | --- |
| 0 | NaoTratada | Atividade de entrega devolvida não tratada pela Equipe de Monitoramento |
| 1 | RetornarPDV | Atividade de entrega devolvida tratada como revertida pela Equipe de Monitoramento aguardando o retorno do   motorista ao Ponto de Venda |
| 2 | Aceita | Atividade de entrega devolvida tratada como aceita pela Equipe de Monitoramento |
| 3 | Reentrega | Atividade de entrega devolvida tratada como reentrega pela Equipe de Monitoramento |

- Os campos “**VlDistanciaPrevista**” e “**VlDistanciaRealizada**” estão em metros;
- Campos que não possuírem dados, isto é, campos nulos, podem não ser exibidos no retorno da requisição;

**Retorno**:

[

    {

        "CdRota": 1901792,

        "CdRotaNegocio": "100983725",

        "NmRota": "ZONA OESTE",

        "DtRota": "17/10/2019 00:00:00",

        "DtLargada": "18/10/2019 09:32:42",

        "DtUltimaAtividade": "18/10/2019 15:14:42",

        "NmMotorista": "LUIZ PAULO MENDES MARCELINO",

        "QtPNPsGeradas": 1,

        "QtPNPsTratadas": 1,

        "Situacao": "EmAndamento",

        "CdPlacaVeiculo": "GRB9017",

        "QtEntregaPrevista": 1,

        "QtEntregaRealizada": 1,

        "QtEntregaDevolvida": 0,

        "NmUnidadeNegocio": "TSP APUCARANA",

        "Entregas": [

            {

                "CdRota": 1901792,

                "CdEntrega": 23375751,

                "CdClienteNegocio": "7217169",

                "NmCliente": "SUPERACAO VAREJ DO PECHINCHA EIRELI",

                "DtEntrega": "17/10/2019 00:00:00",

                "DtRealizada": "18/10/2019 09:47:06",

                "QtTempoTotalRealizado": 24,

                "VlDistanciaRealizada": 0,

                "NrLatitudeOcorrencia": -26.9165783,

                "NrLongitudeOcorrencia": -49.0717316,

                "KmDispersao": 0,

                "IdSequencia": 1,

                "IdSequenciaRealizada": 1,

                "IdSequenciaCorreta": true,

                "IdDevolvida": false,

                "IdRevertida": false,

                "IdEntregaRealizada": true,

                "IdAcaoDevolucao": 0,

                "AreaResponsavelDevolucao": 0,

                "IdBaldeioAutomatico": false,

                "QtNotaFiscalPrevista": 1,

                "QtNotaFiscalRealizada": 1,

                "QtItemNotaFiscalPrevisto": 2,

                "QtItemNotaFiscalDevolvido": 0,

                "QtItemNotaFiscalRealizado": 2,

                "Status": "2",

                "SituacaoRota": "EmAndamento",

                "Situacao": "Entregue",

                "Pedidos": [

                    {

                        "CdPedidoNegocio": "1006930415",

                        "NotasFiscais": [

                            {

                                "CdPedidoNegocio": "1006930415",

                                "CdEntrega": 23375751,

                                "CdNotaFiscal": 32620120,

                                "CdNotaFiscalNegocio": "000279501",

                                "DsTipoOperacao": "Venda Normal",

                                "ValorTotalPrevisto": 0,

                                "ValorTotalEntregue": 0,

                                "MotivoDevolucao": 0,

                                "CdMotivoDevolucaoCA": 0,

                                "IdAcaoDevolucao": 0,

                                "AreaResponsavelDevolucao": 0,

                                "IdRealizada": true,

                                "IdRevertida": false,

                                "IdDevolvida": false,

                                "QtItemNotaFiscalRealizado": 2,

                                "QtItemNotaFiscalPrevisto": 2,

                                "QtItemNotaFiscalDevolvido": 0,

                                "SituacaoRota": "EmAndamento",

                                "Situacao": "Entregue",

                                "Itens": [

                                    {

                                        "CdNotaFiscal": 32620120,

                                        "CdProdutoNegocio": "403822",

                                        "NmProduto": "LEITE UHT DESNATADO 1L ELEGE CX 12L",

                                        "VlItem": 0,

                                        "QtdPrevisto": 10,

                                        "ValorTotalComprado": 0,

                                        "IdRevertido": false,

                                        "IdDevolvido": false,

                                        "IdRealizado": true,

                                        "Situacao": "Entregue"

                                    },

                                    {

                                        "CdNotaFiscal": 32620120,

                                        "CdProdutoNegocio": "403849",

                                        "NmProduto": "LEITE UHT SEMI DESNATADO 1L CX 12L",

                                        "VlItem": 0,

                                        "QtdPrevisto": 10,

                                        "ValorTotalComprado": 0,

                                        "IdRevertido": false,

                                        "IdDevolvido": false,

                                        "IdRealizado": true,

                                        "Situacao": "Entregue"

                                    }

                                ]

                            }

                        ]

                    }

                ]

            }

        ]

    }

]

## StatusNotasFiscais

- **URL**: [http://cliente-tracking.lincros.com/WS/Retorno.svc/RetornoWeb/StatusNotasFiscais?usuario=XXX&senha=X](http://172.30.8.31:5301/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=brf&senha=brf@123)XXXX

  - Obs: Deve ser informado o nome do cliente:

    - [http://NOMECLIENTE-tracking](http://cliente-tracking.lincros.com)
  - Obs²: Informar o usuário e senha

    - [usuario=XXX&senha=XXXX](http://172.30.8.31:5301/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=brf&senha=brf@123)
- **Método**: POST
- **Parâmetros**: "listCodigoEntrega": long[]
- ## Exemplo de Body:

         {

         "listCodigoEntrega": [7193, 7194]

    }

## Retorno:

[

    {

        "CodigoNotaFiscal": 7850,

        "NumeroNotaFiscal": "98355",

        "CodigoEntrega": 7193,

        "CodigoNegocio": "98355",

        "CodigoPedidoNegocio": "98355",

        "CodigoRotaNegocio": 1845684,

        "Devolvida": false,

        "Revertida": false,

        "DevolvidaParcialmente": null,

        "Realizada": true,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoNotaFiscal": 7851,

        "NumeroNotaFiscal": "98802",

        "CodigoEntrega": 7194,

        "CodigoNegocio": "98802",

        "CodigoPedidoNegocio": "98802",

        "CodigoRotaNegocio": 1845684,

        "Devolvida": false,

        "Revertida": false,

        "DevolvidaParcialmente": null,

        "Realizada": true,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    }

]

## StatusItensNotasFiscas

- **URL**: [http://cliente-tracking.lincros.com/WS/Retorno.svc/RetornoWeb/StatusItensNotasFiscas?usuario=XXX&senha=XXXX](http://172.30.8.31:5301/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=brf&senha=brf@123)

  - Obs: Deve ser informado o nome do cliente:

    - [http://NOMECLIENTE-tracking](http://cliente-tracking.lincros.com)
  - Obs²: Informar o usuário e senha

    - [usuario=XXX&senha=XXXX](http://172.30.8.31:5301/WS/Retorno.svc/RetornoWeb/StatusRotas?usuario=brf&senha=brf@123)
- **Método**: POST
- **Parâmetros**: "listCodigoNotaFiscal": long[]
- ## Exemplo de Body:

       {

          "listCodigoNotaFiscal": [8360, 8361]

  }

## Retorno

[

    {

        "CodigoItem": 22977,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22978,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22979,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22980,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22981,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22982,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22983,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22984,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22985,

        "CodigoNotaFiscal": 8360,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22986,

        "CodigoNotaFiscal": 8361,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22987,

        "CodigoNotaFiscal": 8361,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    },

    {

        "CodigoItem": 22988,

        "CodigoNotaFiscal": 8361,

        "Devolvido": false,

        "Revertido": false,

        "Realizado": false,

        "CodigoMotivoDevolucao": null,

        "MotivoDevolucao": "-",

        "CodigoMotivoDevolucaoCentral": null,

        "MotivoDevolucaoCentral": "-"

    }

]
