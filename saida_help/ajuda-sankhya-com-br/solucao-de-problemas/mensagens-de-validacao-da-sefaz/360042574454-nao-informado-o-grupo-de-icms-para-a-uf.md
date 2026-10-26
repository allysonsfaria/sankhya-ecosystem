---
id: "360042574454"
titulo: "Não informado o grupo de ICMS para a UF de destino (NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574454-N%C3%A3o-informado-o-grupo-de-ICMS-para-a-UF-de-destino-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-25T04:35:50Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "DIFAL", "SEFAZ", "ICMS", "Impostos", "694", "Falta de Grupo ICMS para UF de Destino", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Não informado o grupo de ICMS para a UF de destino (NT2015/003)

**MENSAGEM**

[694] Rejeição: Não informado o grupo de ICMS para a UF de destino [nItem:1]. As configurações relacionadas ao DIFAL não estão corretas para o(s) produto(s).

**SITUAÇÃO**

Esta rejeição ocorre ao tentar emitir uma **"Nota Fiscal Eletrônica (NF-e) modelo 55"** em uma operação interestadual destinada a um parceiro classificado como **"Consumidor Final Não Contribuinte"**. O sistema não localiza as configurações necessárias do grupo de ICMS para a UF de destino, impedindo o cálculo do **"DIFAL (Diferencial de Alíquota)"** conforme a **"Nota Técnica 2015.003"**.

A validação é acionada quando todas estas condições estão presentes simultaneamente:

- Operação Interestadual (idDest=2)
- Operação com Consumidor Final (indFinal=1)
- Operação com Não Contribuinte (indIEDest=9)
- Não é operação de prestação de serviços
- Não está enquadrada nas exceções previstas

**CAUSA**

A rejeição ocorre porque o sistema não encontrou as configurações necessárias do **"DIFAL"** para calcular e informar o grupo de ICMS destinado à UF de destino. Isso acontece quando uma ou mais das seguintes configurações estão ausentes ou incorretas:

- Ausência de cadastro de **"Partilha DIFAL"** para o ano vigente
- Campo **"Calcular DIFAL Partilhado"** desmarcado no Tipo de Operação (TOP)
- Campo **"Calcular DIFAL?"** desmarcado no cadastro do Produto
- Classificação ICMS do parceiro diferente de **"Consumidor Final Não Contribuinte"**
- Ausência de cadastro de **"Alíquota de ICMS"** para a UF de destino com tipo de exceção adequado
- Configuração incorreta do **"Tipo de Substituição"** no produto

A **"Nota Técnica 2015.003"** estabelece a obrigatoriedade de informar o grupo de ICMS para a UF de destino em operações interestaduais destinadas a consumidor final não contribuinte, visando o correto recolhimento do **"DIFAL"** entre os estados de origem e destino.

**Exceções à Regra:**

A validação da rejeição 694 não se aplica nas seguintes situações:

- Devolução de Mercadoria (finNFe=4) que referencie NF-e com chave de acesso anterior a 2016
- NF-e de entrada (tpNF=0)
- Operações com CFOP de Retorno ou Remessa de Mercadorias
- Emitentes optantes pelo **"Simples Nacional"** (CRT=1)
- NF-e complementares (finNFe=2) ou de ajuste (finNFe=3)
- Operações com combustíveis derivados de petróleo (códigos ANP específicos)
- Operações isentas, imunes ou não tributadas (CST 40, 41, CSOSN 103, 300, 400)
- Quando a UF do local de entrega for igual à UF do emitente
- Notas fiscais com data de emissão anterior a 01/07/2016

**SOLUÇÃO**

Para resolver esta rejeição, execute as configurações abaixo na sequência apresentada:

**(1)** Acesse a tela **"Partilhas DIFAL"** (Configurações >> Cadastros >> Partilhas DIFAL) e cadastre o percentual de partilha para o ano vigente. Para operações a partir de 2023, configure o percentual como 100%.

**(2)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP), selecione o TOP utilizado na operação, vá para a aba **"Impostos"** e marque o campo **"Calcular DIFAL Partilhado"**.

**(3)** Acesse a tela **"Produtos"** (Configurações >> Cadastros >> Produtos), localize o produto que apresentou a rejeição, vá para a aba **"Impostos"** ou **"Impostos/Informações por Empresa"** e execute as seguintes configurações:
Marque o campo **"Calcular DIFAL?"**
Configure o campo **"Tipo de Substituição"** conforme orientações da contabilidade

**(4)** Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros), localize o cliente destinatário, vá para a aba **"Fiscal"** e no campo **"Classificação ICMS"** selecione a opção **"Consumidor Final Não Contribuinte"**.

**(5)** Acesse a tela **"Alíquotas de ICMS"** (Comercial >> Arquivo >> Cadastros >> Alíquotas >> Alíquotas de ICMS) e verifique se existe cadastro de alíquota para a combinação de UF de origem e UF de destino da operação. Caso não exista, crie uma nova alíquota configurando:
**"Alíquota Interna de Destino"**: informe o percentual conforme legislação do estado de destino
**"Tipo de Exceção"**: selecione **"1 - Consumidor Final Não Contribuinte"**
**"Percentual do Fundo de Combate à Pobreza"**: se aplicável ao estado de destino

**(6)** Após realizar todas as configurações, relance os itens da nota fiscal, inative ou inutilize a nota anterior se necessário e gere um novo lote para transmissão. O sistema calculará automaticamente o **"DIFAL"** e incluirá o grupo de ICMS para a UF de destino no XML.

**Observações Importantes:**

- Se existir benefício fiscal de redução de base de cálculo no destino, o valor da base de cálculo do ICMS de destino (vBCUFDest) deverá ser informado considerando esse benefício.
- Verifique se as taxas de exceção para alíquotas de PIS e COFINS foram previamente cadastradas, especialmente se a nota contiver itens com CST Isento e CST Normal.
- Esta configuração é necessária apenas para operações interestaduais destinadas a Consumidor Final Não Contribuinte.
