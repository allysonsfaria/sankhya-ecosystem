---
id: "32375119187095"
titulo: "Conheça a rotina de IPI Embutido em notas de venda com kit e componente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32375119187095-Conhe%C3%A7a-a-rotina-de-IPI-Embutido-em-notas-de-venda-com-kit-e-componente"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:31:39Z"
rotulos: ["Configuração", "IPI", "Impostos", "TOP", "EDITMPSOMAIPI", "IPI Embutido", "notas de vendas", "Kit e componente", "EDITMPSOMPRECO", "EDITMPSOMAEXT", "GERPERCALIQIPI", "Kit/Componente"]
---

# Conheça a rotina de IPI Embutido em notas de venda com kit e componente

Ao trabalhar com operações nas quais são vendidos produtos do tipo Kit/Componente (cestas básicas, por exemplo) e é necessário embutir o valor do IPI dos produtos, para que ao faturar o pedido de venda, para nota de venda, o total da nota fique igual ao pedido, é indicado usar a **rotina de IPI embutido**.

**Sendo assim, conheça a jornada de uso dessa rotina:**

![Imagem 1: Primeiramente, alguns parâmetros influenciam na rotina de IPI embutido, e estes devem estar configurados da seguinte…](https://ajuda.sankhya.com.br/hc/article_attachments/32536497745047) Primeiramente, alguns parâmetros influenciam na rotina de IPI embutido, e estes devem estar configurados da seguinte maneira:

(1)** EDITMPSOMPRECO:** ligado

(1)** EDITMPSOMAIPI:** desligado

(1)** EDITMPSOMAEXT:** ligado (dispensando digitar o valor do kit, pois ele receberá o valor de seus componentes)

(1)** GERPERCALIQIPI:** ligado, caso contrário, os componentes ficarão com as alíquotas zeradas, porém, com base e valor de IPI.

**(1)** Nesse caso de uso, o parâmetro **CONFKITIND** deve estar **desativado**.

![Imagem 2: Em seguida, na tela de "Produtos", após cadastrar os itens, na aba "Componentes", garanta que os impostos pertinentes a…](https://ajuda.sankhya.com.br/hc/article_attachments/32549114021143) Em seguida, na tela de **"Produtos",**após cadastrar os itens, na aba **"Componentes",**garanta que os impostos pertinentes a esse produto componente estão devidamente cadastrados na aba **"Impostos"**

**Observação:** de maneira geral, ou o KIT é tributado, ou seus componentes, nunca os dois ao mesmo tempo.

![Imagem 3: Observação: de maneira geral, ou o KIT é tributado, ou seus componentes, nunca os dois ao mesmo tempo.](https://ajuda.sankhya.com.br/hc/article_attachments/32376049420311)

![Imagem 4: A TOP anterior à TOP que haverá efetivamente o cálculo do IPI, deve estar com o campo "IPI embutido" desmarcado . No…](https://ajuda.sankhya.com.br/hc/article_attachments/32549509077911) A TOP anterior à TOP que haverá efetivamente o cálculo do IPI, deve estar com o campo **"IPI embutido" desmarcado**. No exemplo, seria a TOP do pedido de venda.

![Imagem 5: A TOP anterior à TOP que haverá efetivamente o cálculo do IPI, deve estar com o campo "IPI embutido" desmarcado . No…](https://ajuda.sankhya.com.br/hc/article_attachments/32376049422871)

![Imagem 6: Já, a TOP de venda, deve ter as marcações para os cálculos dos impostos e o campo IPI embutido deve estar marcado.](https://ajuda.sankhya.com.br/hc/article_attachments/32549496100887) Já, a TOP de venda, deve ter as marcações para os cálculos dos impostos e o  campo IPI embutido deve estar **marcado.**

![Imagem 7: Já, a TOP de venda, deve ter as marcações para os cálculos dos impostos e o campo IPI embutido deve estar marcado.](https://ajuda.sankhya.com.br/hc/article_attachments/32376073466391)

![Imagem 8: Ao lançar o KIT no documento de pedido de venda, não digite o valor do KIT. Pois, por meio do parâmetro EDITMPSOMAEXT,…](https://ajuda.sankhya.com.br/hc/article_attachments/32550460010903) **Ao lançar o KIT no documento de pedido de venda, não digite o valor do KIT.** Pois, por meio do parâmetro EDITMPSOMAEXT, o sistema atribuirá os valores dos componentes ao KIT. E, ao fazer o cálculo do IPI EMBUTIDO, o sistema precisa dessa possibilidade para repassar os devidos valores a todos os itens da nota.

![Imagem 9: Ao lançar o KIT no documento de pedido de venda, não digite o valor do KIT. Pois, por meio do parâmetro EDITMPSOMAEXT,…](https://ajuda.sankhya.com.br/hc/article_attachments/32376364435863)

![Imagem 10: Dessa forma, automaticamente o sistema atribui ao KIT os valores somados dos componentes.](https://ajuda.sankhya.com.br/hc/article_attachments/32550460011543) Dessa forma, **automaticamente** o sistema **atribui ao KIT os valores** somados dos componentes.

![Imagem 11: Dessa forma, automaticamente o sistema atribui ao KIT os valores somados dos componentes.](https://ajuda.sankhya.com.br/hc/article_attachments/32376348804887)

![Imagem 12: Ao faturar o pedido do exemplo, para nota a de venda, tem-se o cálculo do IPI Embutido . No qual, o sistema precisa…](https://ajuda.sankhya.com.br/hc/article_attachments/32550460012695) **Ao faturar o pedido do exemplo, para nota a de venda, tem-se o cálculo do IPI Embutido**. No qual, o sistema precisa rebalancear os valores unitários dos itens da nota, para que o valor que o sistema encontrar de IPI, somado a estes valores, continue dando no total, o valor total do pedido, que nesse exemplo, era de R$ 200,00.

![Imagem 13: Ao faturar o pedido do exemplo, para nota a de venda, tem-se o cálculo do IPI Embutido . No qual, o sistema precisa…](https://ajuda.sankhya.com.br/hc/article_attachments/32376728669335)

![Imagem 14: Na TOP de venda, aba "Impressão" , garanta que o campo "Kit/Componentes - Impressão e Livro Fiscal" esteja configurado…](https://ajuda.sankhya.com.br/hc/article_attachments/32550460013463) Na TOP de venda, aba **"Impressão"**, garanta que o campo **"Kit/Componentes - Impressão e Livro Fiscal"** esteja configurado como **"Componente".**

Com isso, veja que no XML da nota, os valores batem ao analisar os dois componentes da nota e o total da nota.

**Foco nas tags <vProd>, <vIPI> e <vNF>**

<det nItem="1">
<prod>
<cProd>455</cProd>
<cEAN>SEM GTIN</cEAN>
<xProd>COMPONENTE IPI EMBUTIDO</xProd>
<NCM>03078300</NCM>
<cBenef />
<CFOP>5109</CFOP>
<uCom>UN</uCom>
<qCom>1</qCom>
<vUnCom>95.24</vUnCom>
<vProd>95.24</vProd>
<cEANTrib>SEM GTIN</cEANTrib>
<uTrib>UN</uTrib>
<qTrib>1</qTrib>
<vUnTrib>95.24</vUnTrib>
<indTot>1</indTot>
<xPed>49</xPed>
<nItemPed>2</nItemPed>
</prod>
<imposto>
<ICMS>
<ICMS10>
<orig>0</orig>
<CST>10</CST>
<modBC>3</modBC>
<vBC>95.24</vBC>
<pICMS>18.00</pICMS>
<vICMS>17.14</vICMS>
<modBCST>4</modBCST>
<pMVAST>0.0000</pMVAST>
<vBCST>0.00</vBCST>
<pICMSST>0.00</pICMSST>
<vICMSST>0.00</vICMSST>
</ICMS10>
</ICMS>
<IPI>
<cEnq>999</cEnq>
<IPITrib>
<CST>00</CST>
<vBC>95.24</vBC>
<pIPI>5.00</pIPI>
<vIPI>4.76</vIPI>
</IPITrib>
</IPI>
</imposto>
</det>
<det nItem="2">
<prod>
<cProd>456</cProd>
<cEAN>SEM GTIN</cEAN>
<xProd>COMPONENTE 2 IPI EMBUTIDO</xProd>
<NCM>03078300</NCM>
<cBenef />
<CFOP>5109</CFOP>
<uCom>UN</uCom>
<qCom>1</qCom>
<vUnCom>95.24</vUnCom>
<vProd>95.24</vProd>
<cEANTrib>SEM GTIN</cEANTrib>
<uTrib>UN</uTrib>
<qTrib>1</qTrib>
<vUnTrib>95.24</vUnTrib>
<indTot>1</indTot>
<xPed>49</xPed>
<nItemPed>3</nItemPed>
</prod>
<imposto>
<ICMS>
<ICMS10>
<orig>0</orig>
<CST>10</CST>
<modBC>3</modBC>
<vBC>95.24</vBC>
<pICMS>18.00</pICMS>
<vICMS>17.14</vICMS>
<modBCST>4</modBCST>
<pMVAST>0.0000</pMVAST>
<vBCST>0.00</vBCST>
<pICMSST>0.00</pICMSST>
<vICMSST>0.00</vICMSST>
</ICMS10>
</ICMS>
<IPI>
<cEnq>999</cEnq>
<IPITrib>
<CST>00</CST>
<vBC>95.24</vBC>
<pIPI>5.00</pIPI>
<vIPI>4.76</vIPI>
</IPITrib>
</IPI>
</imposto>
</det>
<total>
<ICMSTot>
<vBC>190.48</vBC>
<vICMS>34.28</vICMS>
<vICMSDeson>0.00</vICMSDeson>
<vFCP>0.00</vFCP>
<vBCST>0.00</vBCST>
<vST>0.00</vST>
<vFCPST>0.00</vFCPST>
<vFCPSTRet>0.00</vFCPSTRet>
<vProd>190.48</vProd>
<vFrete>0.00</vFrete>
<vSeg>0.00</vSeg>
<vDesc>0.00</vDesc>
<vII>0.00</vII>
<vIPI>9.52</vIPI>
<vIPIDevol>0.00</vIPIDevol>
<vPIS>0.00</vPIS>
<vCOFINS>0.00</vCOFINS>
<vOutro>0.00</vOutro>
<vNF>200.00</vNF>
</ICMSTot>
</total>
