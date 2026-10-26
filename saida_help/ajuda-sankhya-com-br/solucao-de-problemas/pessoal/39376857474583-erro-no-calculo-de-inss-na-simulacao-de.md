---
id: "39376857474583"
titulo: "Erro no cálculo de INSS na simulação de rescisão e no 13º salário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39376857474583-Erro-no-c%C3%A1lculo-de-INSS-na-simula%C3%A7%C3%A3o-de-rescis%C3%A3o-e-no-13%C2%BA-sal%C3%A1rio"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:18Z"
rotulos: ["Configuração", "Impostos", "INSS", "Folha de Pagamento", "Rescisão", "13º Salário", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no cálculo de INSS na simulação de rescisão e no 13º salário

**Mensagem**

O sistema não calcula o desconto de INSS para alguns colaboradores no processamento do 13º salário, ou calcula valores incorretos de INSS em simulações de rescisão.

**Situação**

Ao realizar o cálculo do 13º salário ou processar uma simulação de rescisão, o sistema apresenta inconsistências no cálculo do INSS. Em alguns casos, o desconto não é aplicado para determinados funcionários, mesmo quando deveria haver o desconto. Em outros casos, o valor calculado está incorreto devido a problemas na configuração da tabela de faixas de INSS.

**Solução**

Para corrigir o erro no cálculo de INSS, siga os passos abaixo:

**(1)** Acesse a tela **"Tabela de Faixas"** (Pessoal+ » Cadastros » Tabela de Faixas) e localize a tabela de INSS vigente para o período do cálculo.

![Imagem 1: (1) Acesse a tela "Tabela de Faixas" (Pessoal+ » Cadastros » Tabela de Faixas) e localize a tabela de INSS vigente para…](https://ajuda.sankhya.com.br/hc/article_attachments/40969438609303)

**(2)** Verifique se todas as faixas de INSS estão configuradas corretamente, com os valores de **"Limite Inferior"**, **"Limite Superior"**, **"Alíquota"** e **"Parcela a Deduzir"** de acordo com a legislação vigente.

<https://ajuda.sankhya.com.br/hc/pt-br/articles/37696119134999-Tabelas-de-Faixas-atualizadas-2026>

**(3)** Confira especialmente a última linha da tabela, pois erros nesta faixa são comuns e podem causar o não cálculo do INSS para colaboradores com salários mais altos.

**(4)** Caso identifique alguma inconsistência, corrija os valores da tabela de faixas conforme a legislação atual.

**(5)** Após ajustar a tabela, refaça o cálculo do 13º salário ou da rescisão para o colaborador afetado.

**(6)** Verifique se o evento de desconto **"9030 - INSS 13º"** foi gerado corretamente no cálculo.

**(7)** Caso o problema persista, verifique se há alguma configuração específica no cadastro do colaborador que possa estar impedindo o cálculo do INSS, como categoria diferenciada ou isenção cadastrada indevidamente.

![Imagem 2: (3) Confira especialmente a última linha da tabela, pois erros nesta faixa são comuns e podem causar o não cálculo do…](https://ajuda.sankhya.com.br/hc/article_attachments/40969458520599)

**Causa**

O erro ocorre principalmente devido a configurações incorretas na tabela de faixas de INSS, especialmente na última faixa da tabela. Quando os valores de limite superior, alíquota ou parcela a deduzir estão incorretos, o sistema não consegue calcular corretamente o desconto de INSS para os colaboradores que se enquadram naquela faixa salarial.

Outra causa comum é a falta de atualização da tabela de faixas quando há mudanças na legislação previdenciária, fazendo com que o sistema utilize valores desatualizados para o cálculo.
