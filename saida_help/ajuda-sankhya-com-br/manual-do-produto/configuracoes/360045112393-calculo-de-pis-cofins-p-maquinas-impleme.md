---
id: "360045112393"
titulo: "Cálculo de PIS/COFINS p/ Máquinas/Implementos/Veículos Usados considerando o custo de compra como redução da base de Cálculo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112393-C%C3%A1lculo-de-PIS-COFINS-p-M%C3%A1quinas-Implementos-Ve%C3%ADculos-Usados-considerando-o-custo-de-compra-como-redu%C3%A7%C3%A3o-da-base-de-C%C3%A1lculo"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:59:04Z"
rotulos: ["Configuração", "NF-e", "Cálculo de PIS/COFINS p/ Máquinas/Implementos/Veículos Usados considerando o custo de compra como redução da base de Cálculo", "Cálculo de PIS/COFINS p/ Máquinas/Implementos/Veículos Usados considerando o custo de compra como redução da base de Cálculo manual", "Impostos", "TOP", "Estoque", "TOPPISREDAQUIS", "Cálculo de PIS/COFINS em Veículos Usados", "Maquinas", "PIS/COFINS"]
---

# Cálculo de PIS/COFINS p/ Máquinas/Implementos/Veículos Usados considerando o custo de compra como redução da base de Cálculo

Para efetuar este cálculo, você deve realizar primeiramente as seguintes configurações:

Na tela de [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), crie uma TOP de Venda com as configurações de Cálculo para PIS/COFINS (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos)):

[GIF animado: Imagem 1: Na tela de Cadastro de Tipos de Operação - TOP , crie uma TOP de Venda com as configurações de Cálculo para PIS/COFINS…](https://ajuda.sankhya.com.br/hc/article_attachments/4415571889559)

| ``` ![Imagem 2: A criação da TOP deve ser configurada em conformidade ao seu processo normal. O que é r elevante, nesse caso, é a TOP…](https://ajuda.sankhya.com.br/hc/article_attachments/42311008595607) A criação da TOP deve ser configurada em conformidade ao seu processo normal.              O que é relevante, nesse caso, é a TOP calcular PIS\COFINS. ``` |
| --- |

Depois, para que o sistema saiba qual TOP será utilizada para o cálculo, no parâmetro **"TOP p/calc.PIS/COFINS red.pela aquisição - TOPPISREDAQUIS"**, insira o Código da TOP de Venda.

**Observação:** ao emitir notas com uma determinada TOP de Venda informada no parâmetro acima, ao realizar emissões de notas, o controle do Produto deve ser o mesmo da Nota de Compra, Complementar e Venda, para que dessa forma, o valor total de compra seja deduzido da base de cálculo de PIS/COFINS. Então, quando uma nota de venda for gerada, o sistema buscará o valor referente à nota complementar com a data/horário posterior à última nota de compra do produto.

Lembrando que, para que o cálculo da redução do PIS e COFINS seja realizado para mais de uma TOP de Venda, o campo **"Calcula PIS/COFINS red. pela aquisição"** da TOP, aba Impostos, deve estar configurado. Este campo possui as seguintes opções:

- **Usa do parâmetro:** quando esta opção for selecionada, o sistema irá considerar a configuração feita no parâmetro TOPPISREDAQUIS.
- **Não calcula:** com esta opção, o sistema não realizará o cálculo da redução da base de PIS e COFINS.
- **Usa da TOP:** com esta opção selecionada, será utilizada a TOP para o cálculo da redução da base de PIS e COFINS e desconsiderada a configuração feita no parâmetro de chave TOPPISREDAQUIS.

Agora, configure o Produto com a Classificação Tributária e Controle de Estoque. Para isso, no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), selecione o Produto que será utilizado; este deverá usar Controle adicional de estoques do tipo **"Livre"**(aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque)), onde, na Nota de Compra do Produto, você deve indicar um número de Série/Placa/Chassi que identifique o Item. Além disso, no campo **"Classificação Substituição Tributária"**(aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos)), você deve selecionar a opção **"Veículos automotores"**:

[GIF animado: Imagem 3: Agora, configure o Produto com a Classificação Tributária e Controle de Estoque . Para isso, n o Cadastro de Produtos ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4415556151191)

Na Nota de Venda, utilizando a TOP definida no parâmetro, no momento do cálculo de PIS e COFINS, o sistema irá procurar uma nota que atualize estoque e que o controle do item seja o mesmo da Nota de Venda (caso exista mais de uma Nota de Compra, será considerada a mais recente) e reduzirá a base de cálculo, subtraindo o valor total da compra do produto encontrado sem rateios de despesas acessórias (Valor total do produto), sendo que, se o valor da venda for menor que o da compra, o valor da base reduzida será zerada.

| ``` ![Imagem 4: Quando não for encontrada nenhuma nota de entrada, será exibida uma mensagem e a operação será desfeita.](https://ajuda.sankhya.com.br/hc/article_attachments/42311008600087) Quando não for encontrada nenhuma nota de entrada, será exibida uma mensagem              e a operação será desfeita. ``` |
| --- |

Considere o seguinte exemplo:

Temos a Nota de Compra nunota 2731 e a Nota de Venda nunota 2735. Sendo que, na Nota de Venda, a BASERED foi reduzida do valor da Nota de Venda com o valor de Compra, por exemplo:

 152,00-100,00 = 52,00.

O valor do imposto calculado na venda foi:

 52,00 \*1,65% = 0,86.

Assim, no XML da NF-e, as tags **<vBC>** do PIS e COFINS deverão vir corretamente calculadas:

```
 <PIS>

                                 <PISAliq>

                                         <CST>01</CST>

                                         <vBC>52.00</vBC>

                                         <pPIS>1.65</pPIS>

                                         <vPIS>0.86</vPIS>

                                 </PISAliq>

                         </PIS>

                         <COFINS>

                                 <COFINSAliq>

                                         <CST>01</CST>

                                         <vBC>52.00</vBC>

                                         <pCOFINS>1.65</pCOFINS>

                                         <vCOFINS>0.86</vCOFINS>

                                 </COFINSAliq>

                         </COFINS>
```
