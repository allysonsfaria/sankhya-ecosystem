---
id: "32692492557335"
titulo: "Arquivo ADRC-ST PR não está gerando os registros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32692492557335-Arquivo-ADRC-ST-PR-n%C3%A3o-est%C3%A1-gerando-os-registros"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:30:44Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "ICMS", "Impostos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Arquivo ADRC-ST PR", "Arquivo ADRC-ST PR caso de uso", "não está gerando os registros", "caso de uso", "ADRC-ST"]
---

# Arquivo ADRC-ST PR não está gerando os registros

Ao gerar o ADRCST, o item marcado e com movimento na referência na tela **"Geração do arquivo ADRC-ST PR"** não está sendo considerado, sendo gerados apenas os registros de abertura e encerramento. 

Este artigo tem por objetivo apresentar um cenário recorrente em determinados clientes.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32692492552855)SOLUÇÃO:**

Em relação ao uso da tela, recomenda-se revisar as configurações básicas conforme orientações do manual: ["**Geração do Arquivo ADRC-ST PR**"](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR).

####

#### Caso de Uso:

NU: 291 >> **COMPRA** (08/02/2024) >> Valor de ST: 1.178,72 total da nota. >> **Tributação: 10**

NU: 290 >> **VENDA** (24/09/2024) >> Produto: 16798 >> Valor do ICMS da ST da operação anterior: 10,60 // Base ST de operação anterior: 93,84 >> **Tributação: 60**

#### **(1)** Registros e suas funções:

1. 0000 >> Cabeçalho
2. 1000 >> Identificação analítica do produto
3. 1010 >> Preenchido por contribuintes enquadrados no Simples Nacional em caso de pedido de ressarcimento ou complementação do imposto
4. 1100 >> Totalização das notas fiscais de entrada declaradas no Registro 1110, deduzidas das devoluções ocorridas no mesmo mês da aquisição do produto
5. 1110 >> Deve conter todas as notas fiscais modelo 55 de entrada da mercadoria declarada no Registro 1000 no período de referência.
6. 1120 >> Notas fiscais modelo 55 referentes às devoluções de compras ocorridas no mesmo mês em que foram registradas as entradas das respectivas mercadorias.
7. 1200 >> Totalídas emitidas em operações internas de venda ao consumidor final, deduzidas das devoluções ocorridas no próprio mês da venda do produto identificado no Registro 1000.
8. 1210 >> Todas as notas fiscais de saídas emitidas em operações internas de venda aos consumidores finais do produto declarado no Registro 1000.
9. 1220 >> Notas fiscais de devolução de venda ocorridas no mesmo mês em que a saída da mesma mercadoria foi apurada.
10. 1300 >> Totalização das notas de saída emitidas para outros estados, conforme declaradas no Registro 1310 do produto identificado no Registro 1000.
11. 1310 >> Notas fiscais de saída emitidas para outros estados do produto declarado no Registro 1000, conforme o Art. 6º do Anexo IX do RICMS/17.
12. 1320 >> Notas fiscais de devoluções de vendas ocorridas no mesmo mês em que foi registrada a saída da mesma mercadoria.
13. 1400 >> Totalização das notas fiscais de venda emitidas em operações internas com produtos alimentícios destinados à merenda escolar, órgãos da administração pública, cozinhas industriais, restaurantes e similares, hotéis e similares, pizzas conforme o art. 119 do Anexo IX do RICMS/2017.
14. 1410 >> Notas fiscais emitidas em operações internas do produto identificado no Registro 1000, conforme regras do Art. 119 do anexo IX do RICMS/17.
15. 1420 >> fiscais de devoluções de vendas ocorridas no mesmo mês em que a saída dessas mercadorias foi registrada.
16. 1500 >> Totalização das notas fiscais de saídas internas destinadas ao contribuinte do Simples Nacional.
17. 1510 >> Notas fiscais de saída interna destinadas ao contribuinte do Simples Nacional do produto declarado no Registro 1000.
18. 1520 >> Notas fiscais de devolução de venda ocorridas no mesmo mês em que foi registrada a saída da mesma mercadoria. As CFOP's atribuídas neste registro serão 1201, 1202, 1203, 1204, 1506, 1207, 1208, 1209, 1212, 213, 1214, 1410, 1411, 1660, 1661 e 1662.
19. 1999 >> Identificação do encerramento do Bloco 1 e a quantidade de registros ou linhas nele existentes.
20. 9000 >> Totalização dos campos de apuração dos valores a ressarcir, recuperar ou complementar dos Registros totalizadores 1200, 1300, 1400 e 1500.
21. 9999 >> Identificação do encerramento do arquivo digital e informação da quantidade de registros ou linhas existentes no arquivo.

**Dessa forma, a nota de venda não estava sendo gerada devido à seguinte premissa do Registro:**

- 1200: Totalização das notas de **saídas emitidas em operações internas de venda ao** **consumidor final**, deduzidas das devoluções ocorridas no próprio mês da venda do produto identificado no Registro 1000.
- 1210: Todas as notas fiscais de **saídas emitidas em operações internas de venda aos** **consumidores finais** do produto declarado no Registro 1000.
- O parceiro estava classificado como **"Revendedor"**. Ao ser alterado para Consumidor Final Contribuinte e/ou Não Contribuinte, **os dados passaram a ser gerados corretamente.**

![Imagem 2: O parceiro estava classificado como "Revendedor" . Ao ser alterado para Consumidor Final Contribuinte e/ou Não…](https://ajuda.sankhya.com.br/hc/article_attachments/33381112349719)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32692525538327)CAUSA:**

Os registros não estavam sendo gerados em virtude de configuração inadequada da classificação fiscal de ICMS do parceiro.
