---
id: "26487224917655"
titulo: "Reversão / Recuperação de Devedores Duvidosos Baixa Parcial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26487224917655-Revers%C3%A3o-Recupera%C3%A7%C3%A3o-de-Devedores-Duvidosos-Baixa-Parcial"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:41:59Z"
rotulos: ["Contabilização", "Financeiro", "Reversão / Recuperação de Devedores Duvidosos Baixa Parcial", "Provisão", "Devedores Duvidosos", "Recuperação de Crédito"]
---

# Reversão / Recuperação de Devedores Duvidosos Baixa Parcial

Quando uma dívida que já foi provisionada como devedores duvidosos (PDD) é recebida parcialmente, a contabilidade precisa ajustar os valores. Esse processo envolve a reversão da provisão correspondente à parte que foi paga. Assim, o registro contábil reflete corretamente o que foi recuperado e o saldo restante do cliente.

Basicamente, a empresa deve:

![Imagem 1: Registrar o valor que foi recebido, reconhecendo a entrada de dinheiro;](https://ajuda.sankhya.com.br/hc/article_attachments/26492003111191) Registrar o valor que foi recebido, reconhecendo a entrada de dinheiro;

![Imagem 2: Reverter a provisão para devedores duvidosos referente à quantia recebida, pois essa parte já não é mais considerada um…](https://ajuda.sankhya.com.br/hc/article_attachments/26492018334231) Reverter a provisão para devedores duvidosos referente à quantia recebida, pois essa parte já não é mais considerada um risco;

![Imagem 3: Deixar o restante da dívida não paga ainda provisionado como devedores duvidosos, até que seja confirmado o recebimento…](https://ajuda.sankhya.com.br/hc/article_attachments/26492003121431) Deixar o restante da dívida não paga ainda provisionado como devedores duvidosos, até que seja confirmado o recebimento ou perda dessa parte.

Dessa forma, os registros contábeis ficam corretos tanto para o valor recuperado quanto para a parte ainda incerta.

**1° Passo:**

Na tela **"Movimentação Financeira"**, no campo **"PDD":** marque o Financeiro como PDD

![Imagem 4: Na tela "Movimentação Financeira" , no campo "PDD": marque o Financeiro como PDD](https://ajuda.sankhya.com.br/hc/article_attachments/26487224900631)

Na tela **"Contabilização de Devedores Duvidosos"** (Caminho: Contabilização » Arquivos » Contabilização de Devedores Duvidosos) contabilize esse título marcado como PDD na provisão de devedores duvidosos.

![Imagem 5: Na tela "Contabilização de Devedores Duvidosos" (Caminho: Contabilização » Arquivos » Contabilização de Devedores…](https://ajuda.sankhya.com.br/hc/article_attachments/26487224902039)

**Exemplo:**

- Lançamento contábil da Provisão do título não recebido

**Valor:** 8.000,00 Reais

D - Conta 1668  DESPESA COM DEVEDORES DUVIDOSOS ( Resultado)

C - Conta 1666 (-) PROVISAO P/CREDITOS LIQ.DUVIDOSA ( Ativo)

**Saldo da Conta:** 1666  8.000,00 (Credor)

![Imagem 6: Saldo da Conta: 1666 8.000,00 (Credor)](https://ajuda.sankhya.com.br/hc/article_attachments/26487163655959)

**2° Passo: Baixa Parcial 1**

Efetuada a baixa no valor de 1.200,00 , o título 162 baixou e o sistema deu origem ao título 163 no valor de 6.800,00 (valor remanescente).

![Imagem 7: Efetuada a baixa no valor de 1.200,00 , o título 162 baixou e o sistema deu origem ao título 163 no valor de 6.800,00…](https://ajuda.sankhya.com.br/hc/article_attachments/26492968531351)

**3° Passo: Baixa Parcial 2**

Efetuada baixa no valor de 2.500,00, o título 163 baixou e o sistema deu origem ao título 164.

![Imagem 8: Efetuada baixa no valor de 2.500,00, o título 163 baixou e o sistema deu origem ao título 164.](https://ajuda.sankhya.com.br/hc/article_attachments/26492983196439)

**4° Passo: Contabilização da Provisão de Devedores Duvidosos -  Provisão da Baixa Parcial**

**Exemplo:**

- Lançamento contábil da Provisão do título não recebido

**Valor:** 2.500,00 Reais

D - Conta 1668  DESPESA COM DEVEDORES DUVIDOSOS ( Resultado)

C - Conta 1666 (-) PROVISAO P/CREDITOS LIQ.DUVIDOSA ( Ativo)

**Saldo da conta:** 10.500,00 (Credor)

![Imagem 9: Saldo da conta: 10.500,00 (Credor)](https://ajuda.sankhya.com.br/hc/article_attachments/26487224906263)

**5° Passo: Recuperação feita com o parâmetro TITPDDVLRLANC Desligado** 

**Exemplo:**

**Lanc 1:**

**Valor:** 1200,00 Reais (referente a primeira baixa)

C - Conta 1669  RECEITA REVERSAO/ RECUP DEV. DUVIDOSOS ( Resultado)

D - Conta 1666 (-) PROVISAO P/CREDITOS LIQ.DUVIDOSA ( Ativo)

**Saldo da conta:** 9.300,00 (Credor)

**Lanc 2:**

**Valor:** 2.500,00 Reais (referente a baixa parcial)

C - Conta 1669  RECEITA REVERSAO/ RECUP DEV. DUVIDOSOS ( Resultado)

D - Conta 1666 (-) PROVISAO P/CREDITOS LIQ.DUVIDOSA ( Ativo)

**Saldo da conta:** 6.8000,00 (Credor)

![Imagem 10: Saldo da conta: 6.8000,00 (Credor)](https://ajuda.sankhya.com.br/hc/article_attachments/26487163660567)

**6° Passo: Recuperação feita com o parâmetro TITPDDVLRLANC ligado**

**Exemplo:**

**Lanc 1**

**Valor:** 8.000,00 Reais (referente a primeira baixa, aqui o sistema assume o valor do título original)

D - Conta 1669  RECEITA REVERSAO/ RECUP DEV. DUVIDOSOS ( Resultado)

C - Conta 1666 (-) PROVISAO P/CREDITOS LIQ.DUVIDOSA ( Ativo)

**Saldo da conta:** 2.500,00 (Credor)

**Lanc 2**

**Valor:** 2.500,00 Reais (referente a baixa parcial)

D - Conta 1669  RECEITA REVERSAO/ RECUP DEV. DUVIDOSOS ( Resultado)

C - Conta 1666 (-) PROVISAO P/CREDITOS LIQ.DUVIDOSA ( Ativo)

**Saldo da conta:** 0,00 (Credor)

![Imagem 11: Saldo da conta: 0,00 (Credor)](https://ajuda.sankhya.com.br/hc/article_attachments/26487163661975)

Como se pode ver, na primeira recuperação, em que o valor do título atualmente é 1.200,00 (pós baixa parcial), foi feita a contabilização usando o parâmetro **TITPDDVLRLANC**. Este parâmetro utiliza o valor do lançamento contábil original do PDD (provisão antes da 1° baixa parcial), permitindo que a recuperação seja baseada no valor original do título e não apenas na baixa parcial.

**7° Passo: Valor Remanescente**

Após as baixas parciais, como o sistema recuperou o valor original do primeiro lançamento, o saldo da conta zerou. Então, é necessário marcar o título que ficou sem baixar como PDD, acessar a tela de Contabilização de Devedores Duvidosos e contabilizar esse título.

![Imagem 12: Após as baixas parciais, como o sistema recuperou o valor original do primeiro lançamento, o saldo da conta zerou.…](https://ajuda.sankhya.com.br/hc/article_attachments/26492968538007)

Como pode-se ver no razão, a conta vai ficar com o saldo de PDD igual ao valor do título que ainda não foi baixado/recuperado.

![Imagem 13: Como pode-se ver no razão, a conta vai ficar com o saldo de PDD igual ao valor do título que ainda não foi…](https://ajuda.sankhya.com.br/hc/article_attachments/26487163664023)

Todo esse processo se dá porque na baixa parcial o título assume o valor da baixa e os demais que vão sendo gerados perdem o vínculo com o original.
