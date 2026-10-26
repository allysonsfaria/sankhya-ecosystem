---
id: "360044576454"
titulo: "No Balanço Patrimonial, o somatório do saldo inicial (VL_CTA_INI) das linhas de detalhe (IND_COD_AGL= “D”) do Ativo (IND_GRP_BAL= “A”) esta diferente do somatorio do saldo final (VL_CTA_INI) das linhas de detalhe[...]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044576454-No-Balan%C3%A7o-Patrimonial-o-somat%C3%B3rio-do-saldo-inicial-VL-CTA-INI-das-linhas-de-detalhe-IND-COD-AGL-D-do-Ativo-IND-GRP-BAL-A-esta-diferente-do-somatorio-do-saldo-final-VL-CTA-INI-das-linhas-de-detalhe"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:51:32Z"
rotulos: ["#criadoRoger", "Configuração", "ECD", "Contabilidade", "Financeiro", "Balanço Patrimonial", "avulsa", "Saldo inicial do Ativo difere do Passivo no Balanço Patrimonial.", "Compare saldos do balancete com o balanço do arquivo txt.", "Verifique se Ativo e Passivo batem; ajuste se necessário.", "Erro"]
---

# No Balanço Patrimonial, o somatório do saldo inicial (VL_CTA_INI) das linhas de detalhe (IND_COD_AGL= “D”) do Ativo (IND_GRP_BAL= “A”) esta diferente do somatorio do saldo final (VL_CTA_INI) das linhas de detalhe[...]

**![Imagem 1: MENSAGEM](https://ajuda.sankhya.com.br/hc/article_attachments/18612377691031) MENSAGEM**

No Balanço Patrimonial, o somatório do saldo inicial (VL\_CTA\_INI) das linhas de detalhe (IND\_COD\_AGL= “D”) do Ativo (IND\_GRP\_BAL= “A”) esta diferente do somatorio do saldo final (VL\_CTA\_INI) das linhas de detalhe (IND\_COD\_AGL= “D”) do Passivo (IND\_GRP\_BAL= “P”).

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/18612377700631) SITUAÇÃO**

Ao tentar validar o arquivo ECD, o seguinte erro é apresentado do validador

**Observação:** Abaixo, é citado o registro J100, **mas** as informações podem ser consideradas para os demais registros, a depender do caso.

**![Imagem 3: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/18612377703575) SOLUÇÃO**

![Imagem 4: Tire um balancete do ano todo da empresa que está sendo analisada, neste balancete do sistema deve-se primeiro…](https://ajuda.sankhya.com.br/hc/article_attachments/18612384109975) Tire um balancete do ano todo da empresa que está sendo analisada, neste balancete do sistema deve-se primeiro verificar:

ATIVO BATE COM PASSIVO?

- Se a resposta for **positiva**, então a sua contabilidade está correta e pode ser que esteja faltando alguma conta para vincular ao código aglutinador do Balanço Patrimonial na rotina Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD>> Balanço Patrimonial
- Se a resposta for **negativa**, então isso significa que sua contabilidade está com os lançamentos errados, ou seja: não foi encerrada adequadamente, sendo necessário que se acerte os lançamentos de modo que o ativo bata com o passivo.

![Imagem 5: Faça uma comparação dos saldos das contas partindo do balancete do sistema para o balanço do arquivo txt (BLOCO J100),…](https://ajuda.sankhya.com.br/hc/article_attachments/18612384116631) Faça uma comparação dos saldos das contas partindo do balancete do sistema para o balanço do arquivo txt (BLOCO J100), sugiro que se compare sempre olhando primeiro no balancete do sistema para o do txt e não ao contrário, pois no txt aparecem muito mais contas, no balanço do txt as contas estarão disponibilizadas.

Verifique quais contas são vinculadas a estes códigos na rotina Contabilidade » Conexão » ECD » Configuração P/ ECD » Demonstrativos ECD>> Balanço Patrimonial.
