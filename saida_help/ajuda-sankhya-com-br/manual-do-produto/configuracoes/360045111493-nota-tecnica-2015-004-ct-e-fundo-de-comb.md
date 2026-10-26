---
id: "360045111493"
titulo: "Nota Técnica 2015.004 - CT-e - Fundo de Combate a Pobreza"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111493-Nota-T%C3%A9cnica-2015-004-CT-e-Fundo-de-Combate-a-Pobreza"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:51Z"
rotulos: ["CT-e", "Configuração", "DIFAL", "XML", "SEFAZ", "Impostos", "Combate", "Fundo", "Pobreza", "Nota Técnica 2015.004 - CT-e - Fundo de Combate a Pobreza manual", "Atualizações na Nota Técnica 2015.004: CT-e e Fundo de Combate à Pobreza"]
---

# Nota Técnica 2015.004 - CT-e - Fundo de Combate a Pobreza

A Nota Técnica 2015.004 apresenta novas tratativas a serem consideradas para o CT-e. Dentre elas, há modificação no layout da NF-e para que este receba as informações da cobrança de ICMS nas operações interestaduais de vendas a consumidor final não contribuinte do imposto, de forma que, insira ainda novos campos para cálculo do Fundo de Combate à Pobreza UF Destino.  

Para se adequar às modificações, há no sistema novos campos que buscarão essas informações para enviá-las para as tag's do XML, pois são elas que serão validadas para que o CT-e seja aprovado.

Observe abaixo, os campos que receberão os valores do Fundo de Combate à Pobreza: 

|  | **(1)** | **TGFICM.PERCICMSFCP:** tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), campo **"Perc. ICMS Fundo Comb. Pobreza"**; |
| --- | --- | --- |

|  | **(1)** | **TGFDIN.PERCFCP:** tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234), opção **"Perc. para Fundo Comb. Pobreza"**; |
| --- | --- | --- |

|  | **(1)** | TGFDIN.VLRFCP: tela [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593994-Central-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção **"Perc. para Fundo Comb. Pobreza"**. |
| --- | --- | --- |

## Validações na confirmação do CT-e

|  | **(1)** | Caso CT-e a ser confirmado possua documentos anteriores cadastrados (TGFDANT) e o campo **"Tipo de Serviço CT-e"** (aba [CT-e/MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abactemde)) seja definido com a opção **"Normal"** (TGFTOP.TIPSERVCTE = 0), a seguinte mensagem será exibida:  **"Não devem ser informados documentos anteriores para CT-e com o tipo de serviço normal."** |
| --- | --- | --- |
|  |  |
|  |  |

|  | **(1)** | Se o CT-e a ser confirmado possuir dois serviços ou mais, e houver cálculo de DIFAL ou de Pobreza, os percentuais devem ser os mesmos (TGFDIN.ALIQINTDEST e TGFDIN.PERCFCP), caso contrário, a seguinte mensagem será exibida:  **"Verifique a tributação dos componentes do serviço (serviços) o CT-e! Para confirmação do CT-e é necessário que a tributação (CST), a alíquota de ICMS, percentual de redução de base, CFOP, alíquota interna de destino e fundo de combate à pobreza sejam os mesmos."** |
| --- | --- | --- |
|  |  |
|  |  |
|  |  |

## Cálculo do ICMS para o Fundo de Combate à Pobreza

As regras para o cálculo do Fundo de Combate à Pobreza, seguem as mesmas condições para o cálculo do DIFAL. Observe:

|  | **(1)** | O [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado deve possuir o **"Tipo de Movimento"** como **"V-Venda"** ou **"P-Pedido de venda"**; |
| --- | --- | --- |

|  | **(1)** | Na mesma tela, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), a marcação **"Calcular DIFAL Partilhado"** (TGFTOP.CALCDIFALPART) deve ser habilitada; |
| --- | --- | --- |

|  | **(1)** | Além disso, na aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso) o campo **"Tipo de serviço CT-e"** tem de ser definido com a opção **"Normal"**; |
| --- | --- | --- |

|  | **(1)** | O parceiro destinatário, sendo este cadastrado na tela [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), precisar ser configurado com a opção **"Consumidor Final"** do campo **"Classificação ICMS"**, sendo este localizado na aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal). |
| --- | --- | --- |

Dessa forma, o cálculo será realizado por item da seguinte forma:

```
        ![Imagem 1: Dessa forma, o cálculo será realizado por item da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/42310973367319) TGFDIN.VLRFCP = TGFDIN.BASE * Perc. ICMS para Fundo Comb. Pobreza
                                 (TGFICMS.PERCFCP)
```

| ![Imagem 2: Dessa forma, o cálculo será realizado por item da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/42310952937111) | No caso de a Alíquota de ICMS ser igual a Alíquota Interna de Destino, não haverá cálculo para o DIFAL, no entanto, caso seja informado o Perc. ICMS Fundo Comb. Pobreza, será calculado o valor do ICMS para o Fundo de Combate a Pobreza, e todas as tag's pertencentes ao Grupo das vendas interestaduais para Consumidor Final não contribuinte do ICMS, serão geradas. |  |
| --- | --- | --- |

No exemplo abaixo, você poderá observar alguns XML's de notas aprovadas:

**(1)** Com DIFAL e com Fundo de Combate à Pobreza:

```
<imp>
        <ICMS>
                <ICMS00>
                        <CST>00</CST>
                        <vBC>535.00</vBC>
                        <pICMS>12.00</pICMS>
                        <vICMS>64.20</vICMS>
                </ICMS00>
        </ICMS>
        <ICMSUFFim>
                <vBCUFFim>535.00</vBCUFFim>
                <pFCPUFFim>2.00</pFCPUFFim>
                <pICMSUFFim>23.00</pICMSUFFim>
                <pICMSInter>12.00</pICMSInter>
                <pICMSInterPart>40.00</pICMSInterPart>
                <vFCPUFFim>10.70</vFCPUFFim>
                <vICMSUFFim>23.54</vICMSUFFim>
                <vICMSUFIni>35.31</vICMSUFIni>
        </imp>
```

**(1)** Com DIFAL e sem Fundo de Combate à Pobreza:

```
<imp>
        <ICMS>
                <ICMS00>
                        <CST>00</CST>
                        <vBC>521.81</vBC>
                        <pICMS>12.00</pICMS>
                        <vICMS>62.62</vICMS>
               </ICMS00>
        </ICMS>
        <ICMSUFFim>
                <vBCUFFim>521.81</vBCUFFim>
                <pFCPUFFim>0.00</pFCPUFFim>
                <pICMSUFFim>23.00</pICMSUFFim>
                <pICMSInter>12.00</pICMSInter>
                <pICMSInterPart>40.00</pICMSInterPart>
                <vFCPUFFim>0.00</vFCPUFFim>
                <vICMSUFFim>22.96</vICMSUFFim>
                <vICMSUFIni>34.44</vICMSUFIni>
         </ICMSUFFim>
  </imp>
```

**(1)** Sem DIFAL e com Fundo de Combate à Pobreza:

```
<imp>
        <ICMS>
                  <ICMS00>
                          <CST>00</CST>
                          <vBC>739.25</vBC>
                          <pICMS>12.00</pICMS>
                          <vCIMS>88.71</vCIMS>
                   </ICMS00>
           </ICMS>
           <ICMSUFFim>
                   <vBCUFFim>739.25</vBCUFFim>
                   <pFCPUFFim>2.00</pFCPUFFim>
                   <pICMSUFFim>0.00</pICMSUFFim>
                   <pICMSInter>12.00</pICMSInter>
                   <pICMSInterPart>40.00</pICMSInterPart>
                   <vFCPUFFim>14.78</vFCPUFFim>
                   <vICMSUFFim>0.00</vICMSUFFim>
                   <vICMSUFIni>0.00</vICMSUFIni>
            </ICMSUFFim>
</imp>
```

**(1)** Sem DIFAL e sem Fundo de Combate à Pobreza:

```
      <imp>
              <ICMS>
                      <ICMS00>
                              <CST>00</CST>
                              <vBC>416.32</vBC>
                              <pICMS>12.00</pICMS>
                              <vICMS>49.96</ICMS>
                       </ICMS00>
               </ICMS>
      </imp>
```

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111493-Nota-T%C3%A9cnica-2015-004-CT-e-Fundo-de-Combate-a-Pobreza#top)
