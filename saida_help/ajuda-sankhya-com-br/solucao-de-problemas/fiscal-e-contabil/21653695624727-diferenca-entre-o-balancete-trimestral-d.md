---
id: "21653695624727"
titulo: "Diferença entre o Balancete trimestral das contas de resultados e o Valor apurado para o lucro antes do IRPJ e CSLL na rotina de Apuração de Regime "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21653695624727-Diferen%C3%A7a-entre-o-Balancete-trimestral-das-contas-de-resultados-e-o-Valor-apurado-para-o-lucro-antes-do-IRPJ-e-CSLL-na-rotina-de-Apura%C3%A7%C3%A3o-de-Regime"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-30T11:46:57Z"
rotulos: ["Configuração", "Relatórios", "Impostos", "Contabilização", "Financeiro"]
---

# Diferença entre o Balancete trimestral das contas de resultados e o Valor apurado para o lucro antes do IRPJ e CSLL na rotina de Apuração de Regime 

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21653664278551)SOLUÇÃO:**

Na tela "Apuração do Regime Normal - Lucro Real" No campo "Lucro Antes IRPJ" será apresentado o valor acumulado por competência registrado mês a mês nos lançamentos contábeis referente as contas configuradas.
Para que uma conta entre para a somatória desse campo, no plano de contas aba e-LALUR a opção de conta de resultado, tem que estar marcado.
Estando marcado o valor do lançamento feito com essa conta contemplará o valor de lucro IRPJ.
 
Para conseguir fazer uma comparação entre a apuração e o balancete é preciso filtrar na geração do balancete as contas corretas.

Quando houver divergência é preciso avaliar o zeramento das contas, avaliar se todos os lotes estão fechados. E se não houve nenhuma divergência entre debito e credito.

O parâmetro **VALDEBCREDCTBZ** tem um impacto efetivo no processo de apuração, pois com ele desabilitado o sistema nao valida na contabilização a diferença de debito e credito, e assim tendo impacto no valor da apuração quando se comparado ao balancete.
