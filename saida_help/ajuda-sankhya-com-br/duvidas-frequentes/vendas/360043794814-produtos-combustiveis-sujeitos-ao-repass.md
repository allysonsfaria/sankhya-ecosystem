---
id: "360043794814"
titulo: "Produtos combustíveis sujeitos ao repasse de ST Interestadual - Quais são  as premissas e configurações?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043794814-Produtos-combust%C3%ADveis-sujeitos-ao-repasse-de-ST-Interestadual-Quais-s%C3%A3o-as-premissas-e-configura%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:52Z"
rotulos: ["Alíquotas", "Configuração", "NF-e", "ICMS", "Impostos", "Ative \"CODANPCOMBREP\" e ajuste alíquotas e tabelas de preços", "Use <ICMSST> para produtos com códigos ANP específicos", "Base ST e ICMS calculados conforme a operação (interna/interestadual)", "Combustíveis"]
---

# Produtos combustíveis sujeitos ao repasse de ST Interestadual - Quais são  as premissas e configurações?

Para a NF-e, quando um produto se enquadrar nos códigos ANP divulgados como sujeitos ao repasse do ST, deverá ser gerado o grupo de tags <ICMSST> ao invés do <ICMS60>;

Para isto foi criado o parâmetro: **"CODANPCOMBREP"**
Descrição: Cód. ANP combust. sujeitos a repasse interestadual

Neste parâmetro deverão ser informados os códigos ANP dos produtos sujeitos ao repasse de ST.

Atualmente:
210203001, 320101001, 320101002,320102002, 320102001, 320102003, 320102005, 320201001,320103001,220102001, 320301001, 320103002, 820101032, 820101026, 820101027, 820101004, 820101005, 820101022,820101031, 820101030, 820101014, 820101006, 820101016,820101015, 820101025, 820101017, 820101018, 820101019,820101020, 820101021, 420105001, 420101005, 420101004,420102005, 420102004, 420104001, 820101033, 820101034,420106001, 820101011, 820101003, 820101013, 820101012,420106002, 830101001, 420301004, 420202001, 420301001,420301002, 410103001, 410101001, 410102001, 430101004,510101001, 510101002, 510102001, 510102002, 510201001,510201003, 510301003, 510103001,510301001.

**![Imagem 1: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201514193175) OBSERVAÇÃO:**

Deverá ser feita a manutenção dos códigos caso necessário com a divulgação / exclusão de por parte da ANP.

**Premissas para geração das tags do grupo <ICMSST> ref. aos combustíveis:**

![Imagem 2: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16201514194327) Configurações » Avançado » Preferências

Ligue o parâmetro: **"COMBUSTÍVEL - Distribuidor de combustível?"**

![Imagem 3: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16201537113111) Configurações » Cadastros » Produtos » Produtos

Ter os produtos configurados com os dados na aba combustíveis no cadastro de produtos

![Imagem 4: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16201537115287) Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

Ter a alíquota de ICMS configurada: 60

![Imagem 5: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16201537117847) Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

Ter no cadastro de alíquotas de ICMS, na aba **Combustíveis,** as configurações / valores para cálculos do ST de repasse.
Detalhes da tela:

![Imagem 6: Ter no cadastro de alíquotas de ICMS, na aba Combustíveis, as configurações / valores para cálculos do ST de repasse.…](https://ajuda.sankhya.com.br/hc/article_attachments/14662351347735)

Campo: **"Tabela c/ base para ST em favor da UF de destino"**: o preenchimento deste campo, origina-se do cadastro de uma Tabela de Preços no sistema, que irá caracterizar a base de Substituição Tributária da UF de destino.

Campo: **"Margem Lucro (MVA) UF Destino"**: informe neste campo a Margem de Valor Agregado ou Ajustado da UF de destino.

Campo: **"Alíquota Estado Destino"**: preencha este campo com a alíquota referente ao estado de destino.

Campo: **"Tabela c/base ST operação anterior"**: informe neste campo uma tabela de preços válida para informar o tipo de pauta a ser utilizado.

Campo **"Base ST Operação Anterior":** QTDNEG \* Valor do produto na tabela

Este valor será destacado no DANFE, no quadro Informações Complementares e será registrado no XML da NF-e como uma TAG de informações adicionais, não gerando cálculo de valor.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201514193175) OBSERVAÇÃO:**

As tabelas acima utilizarão tabelas de preço do sistema para informar as diversas pautas existentes (Pauta por PMPF, por VLR Refinaria e por VLR Unitário Médio).

Configure o campo "**Base ST UF Destino"**:

- Se estiver marcado Pauta a base será calculada usando a tabela informada no campo Tabela c/ Base ST em Favor da UF de Destino.
- Se marcar Valor do Produto será usado o valor na nota.

O cálculo é feito da seguinte forma:

- Base ST em Favor da UF de Destino: (QTDNEG \* VLRPROD) + MVA (se for informado).
- ICMS Devido na UF de Destino = Base ST em Favor da UF de Destino \* Alíquota de ICMS p/ UF Destino.

- - Nota: Os campos Base ST UF Destino, Valor ICMS UF Destino e Base ST Operação Anterior, presentes na grade de itens da nota, também são habilitados pelo parâmetro Distribuidor de combustível? - COMBUSTÍVEL, logo, quando este parâmetro estiver desabilitado, estes campos não serão mais visíveis na grade de Itens.

Desta forma, quando um produto comercializado possuir o código ANP (cadastro de produtos » aba **combustíveis**) informado no parâmetro CODANPCOMBREP e configurado as alíquotas / valores, estes serão gerados nas tags da NF-e:

**![Imagem 8: IMPORTANTE: Quando for uma operação interna (dentro do estado):](https://ajuda.sankhya.com.br/hc/article_attachments/17855841939095) IMPORTANTE:**
Quando for uma operação interna (dentro do estado):

- Os valores do ICMS ST retido na UF remetente e valor do ICMS ST da UF destino serão iguais.

Quando for uma operação interestadual (fora do estado):

- Os valores serão diferentes, desde que configurado corretamente o cadastro de alíquotas (aba combustíveis) e possuírem as informações do ST anterior (campos BASESUBSTITANT e VLRSUBSTANT) podem ser alimentados através das rotinas do sistema de rastreamento, pelo importador de XML ou manualmente digitando a informação na nota de compra.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201514193175) OBSERVAÇÃO:**

Todas as informações dos campos estarão disponíveis na grade de itens da central.
