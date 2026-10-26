---
id: "360042563554"
titulo: "Alíquota de ICMS superior a definida para a operação interestadual (NT2017/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042563554-Al%C3%ADquota-de-ICMS-superior-a-definida-para-a-opera%C3%A7%C3%A3o-interestadual-NT2017-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-27T20:14:31Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "CFOP", "693", "Refaça faturamento NF-e", "Rejeição 693: ICMS alto", "Verifique e ajuste alíquotas", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Alíquota de ICMS superior a definida para a operação interestadual (NT2017/002)

**Mensagem**

693 - Rejeição: Alíquota de ICMS superior à definida para operação interestadual

**Situação**

Como existem muitas exceções e campos associados a essa regra de validação é importante ficar atento. Intuitivamente, a atitude mais comum é alterar a alíquota do ICMS para o valor correspondente à alíquota prevista em operações interestaduais, valor que é esperado pela Sefaz devido à forma como foi preenchida a NF-e.

**Solução**

**(1)** Na **"Central de Vendas"** (Comercial >> Rotinas), identifique o **"Cód.Alíq.ICMS"** na linha de cada item.

**(2)** Acesse **"Alíquotas de ICMS"** (Comercial >> Arquivo >> Cadastros >> Alíquotas), busque pelos códigos constatados no item anterior e confira junto ao contador se os campos **"Alíquota"**, **"Alíquota Interna Destino"** e **"Alíquota p/origem estrangeira"** estão de acordo com a operação.

**(3)** Caso utilize regras fiscais automáticas, verifique se a configuração da regra está parametrizada corretamente para aplicar a alíquota interestadual adequada.

**(4)** Após os ajustes, proceda com a inutilização ou exclusão da respectiva NF-e e, em seguida, refaça o faturamento.

**CAUSA**

Quando for emitida uma NF-e sob todas as circunstâncias abaixo, será retornada a rejeição **"693 - Alíquota de ICMS superior à definida para a operação interestadual"**:

- Se a Operação Interestadual de Saída Normal, onde os campos idDest = 2, tpNF = 1 e finNFe = 1;
- Se a Origem da Mercadoria for igual a 1, 2, 3 ou 8:

  - 1 = Estrangeira - Importação direta, exceto a indicada no código 6;
  - 2 = Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7;
  - 3 = Nacional, mercadoria ou bem com conteúdo de importação superior a 40% e inferior ou igual a 70%;
  - 8 = Nacional, mercadoria ou bem com conteúdo de importação superior a 70%.
- Se o emitente for de um estado da Região Sul ou Sudeste (exceto Espírito Santo) e emitir NF-e para destinatário localizado nos estados do Norte, Nordeste, Centro-Oeste e Espírito Santo, com valor da alíquota (pICMS) maior que 7.00%;
- Se o valor da alíquota do ICMS for maior do que 12.00% para os demais casos;
- Se houver negociação com consumidor contribuinte e não contribuinte de fora do estado, deverá haver uma regra específica no cadastro de **"Alíquotas de ICMS"**.

**EXCEÇÕES E OBSERVAÇÕES**

- Para as NFe com Data de Emissão anterior a 01/07/2016, a regra de validação acima não se aplica para destinatário Não Contribuinte (tag: dest / indIEDest = 9)
- A regra de validação não se aplica na venda de veículos novos (tag: veicProd) se existir ao menos um item de Venda direta para grandes consumidores (tpOp = 3), ou de Faturamento direto para consumidor final (tpOp = 2)
- A regra de validação não se aplica para as operações com CFOP de Retorno de Mercadorias ou Anulação de Valor (Tabela CFOP, indRetor = 1 ou indAnula = 1) (tabela de CFOP específicos são apresentados no final do artigo)
- A regra de validação não se aplica para as operações de venda à ordem (CFOP 6.118, 6.119, 6.122 e 6.123)
- A regra de validação não se aplica se informada UF do local de entrega (tag: entrega/UF) diferente da UF do emitente (tag: enderEmit/UF)
- A regra de validação não se aplica se informada UF do local de retirada (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF)
