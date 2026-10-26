---
id: "25799184380823"
titulo: "Caso de uso - CST 40 ICMS - Nota com SUFRAMA, sem destaque do ICMS em campo próprio e desconto no total da nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25799184380823-Caso-de-uso-CST-40-ICMS-Nota-com-SUFRAMA-sem-destaque-do-ICMS-em-campo-pr%C3%B3prio-e-desconto-no-total-da-nota"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-04T20:04:07Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SUFRAMA", "ICMS", "Impostos"]
---

# Caso de uso - CST 40 ICMS - Nota com SUFRAMA, sem destaque do ICMS em campo próprio e desconto no total da nota

Durante o lançamento de notas com SUFRAMA, ou seja, cuja Alíquota de ICMS está configurada com o campo **"Cód.Mot.Desoneração ICMS"** igual a 7 - SUFRAMA, pode-se realizar o repasse do ICMS "Suframado" sem a necessidade de destacar tais valores em **campos próprios.**

Segue abaixo o exemplo de um caso prático de lançamento:

#### Tela ALIQUOTAS DE ICMS:

Observação ao campo **"% da Base ICMS"** que será considerado para calcular o valor a ser desonerado e abatido no total da nota.

![Imagem 1: Observação ao campo " % da Base ICMS " que será considerado para calcular o valor a ser desonerado e abatido no total…](https://ajuda.sankhya.com.br/hc/article_attachments/25908193692183)

#### Efeito no lançamento da nota:

No exemplo, o total do produto é de R$ 1000,00. Ao configurar em sua alíquota de ICMS o % de 12, percebe-se que foi calculado apenas no campo de desoneração o valor de R$ 120,00 e este valor foi abatido do total da nota, sem o destaque do valor nos campos próprios de ICMS.

![Imagem 2: No exemplo, o total do produto é de R$ 1000,00. Ao configurar em sua alíquota de ICMS o % de 12, percebe-se que foi…](https://ajuda.sankhya.com.br/hc/article_attachments/25908147365399)

#### Veja agora o efeito dessa configuração no XML da nota:

![Imagem 3: Veja agora o efeito dessa configuração no XML da nota:](https://ajuda.sankhya.com.br/hc/article_attachments/25908147370391)
