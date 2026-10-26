---
id: "39340522954263"
titulo: "Folha de Pagamento Calculando 1 Dia a Mais de Atestado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39340522954263-Folha-de-Pagamento-Calculando-1-Dia-a-Mais-de-Atestado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-10T15:10:40Z"
rotulos: ["Configuração", "Ocorrências", "Folha de Pagamento", "Regra de Cálculo", "Artigo criado KCS", "Sankhya RH - KCS", "Atestado"]
---

# Folha de Pagamento Calculando 1 Dia a Mais de Atestado

**MENSAGEM**

O sistema está calculando dias a mais de atestado na folha de pagamento. 
Por exemplo, ao calcular a folha mensal, o sistema considera 30 dias de salário base mais os dia de atestado lançado, totalizando a quantidade de dias superior ao devido. 

**SITUAÇÃO**

Ao calcular a folha de pagamento mensal para funcionários que possuem atestado médico, o sistema está considerando incorretamente o(s) dia(s) do atestado adicional no cálculo. Isso ocorre mesmo quando o funcionário deveria ter apenas 30 dias computados no mês.

**SOLUÇÃO**

Para corrigir este problema, siga os passos abaixo:

**(1)** Acesse a tela **"Ocorrências"** (Pessoal+ » Rotinas Folha » Ocorrências) e localize a ocorrência de atestado utilizada para o funcionário;

**(2)** Verifique se a opção **"Reduz Dias Trabalhados"** está marcada na configuração da ocorrência. 
Caso esteja desmarcada, realize a marcação e salve as alterações;

![Imagem 1: Acesse a "Regra de Cálculo" e verifique se a marcação "Calcula resíduo de afastamento em meses que não possuem 30 dias"…](https://ajuda.sankhya.com.br/hc/article_attachments/41123071425815)

**(3)** Acesse a "Regra de Cálculo" e verifique se a marcação "Calcula resíduo de afastamento em meses que não possuem 30 dias" também está marcada. 
Caso esteja marcada, realize a desmarcação e salve as alterações;

![Imagem 2: Realize o calculo da folha novamente; Valide se o cálculo agora está considerando corretamente os 30 dias, sem o dia…](https://ajuda.sankhya.com.br/hc/article_attachments/41142138812695)

**(4)** Realize o calculo da folha novamente; 

**(5)** Valide se o cálculo agora está considerando corretamente os 30 dias, sem o dia adicional de atestado;

**CAUSA**

O problema ocorre porque a **"Ocorrência"** estava configurada com a opção **"Reduz Dias Trabalhados"** desmarcada. Quando esta opção não está marcada corretamente, o sistema não computa adequadamente os dias de atestado, resultando no cálculo de um dia a mais na folha de pagamento.
Esta configuração incorreta faz com que o sistema some os dias de atestado aos dias trabalhados, ao invés de considerá-los dentro do período mensal padrão de 30 dias.
