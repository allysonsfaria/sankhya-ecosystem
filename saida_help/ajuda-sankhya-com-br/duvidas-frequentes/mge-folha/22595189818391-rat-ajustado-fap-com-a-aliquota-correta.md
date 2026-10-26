---
id: "22595189818391"
titulo: "'RAT Ajustado FAP' com a alíquota correta, porém o valor errado no resumo da folha - Pessoal G"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22595189818391--RAT-Ajustado-FAP-com-a-al%C3%ADquota-correta-por%C3%A9m-o-valor-errado-no-resumo-da-folha-Pessoal-G"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-30T19:34:29Z"
rotulos: ["Configuração", "FAP", "Impostos", "Folha", "Pessoal G"]
---

# 'RAT Ajustado FAP' com a alíquota correta, porém o valor errado no resumo da folha - Pessoal G

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/22595214257559) **MENSAGEM:**

'RAT Ajustado FAP' com a alíquota correta, porém o valor errado no resumo da folha - Pessoal G.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/22595189805719)CAUSA:**

Ocorre por falta de configuração.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/22595189804311)SOLUÇÃO:**

Necessário avaliar o registro fiscal da empresa que está sendo gerado o resumo da folha, analisar as alíquotas de taxa de terceiro e FAP, se estiverem corretas, avaliar o RAT Ajustado que trás no resumo da folha da seguinte forma: 

**"Para realizar o cálculo do valor do RAT ajustado pelo Fator Acidentário de Prevenção (FAP), é necessário aplicar a seguinte fórmula: RAT x FAP. Dessa forma, caso a empresa tenha um RAT de 3% e FAP de 0,5%, o RAT ajustado para recolhimento será equivalente a 1,5%."**

Após chegar na alíquota do RAT Ajustado, é necessário pegar a base do INSS e multiplicar pela % encontrada no cálculo anterior, dessa forma, chegará no valor correto que deve apresentar no resumo da folha.

**Exemplo:**

Base INSS: 1.500,00

RAT Ajustado: 1,5%

Cálculo:  1.500,00 \* 1,5 % = R$ 22,50 (Valor ser apresentado no resumo da folha no campo de RAT Ajustado)

Caso o valor apresentando no resumo não seja o correto, é necessário verificar em qual departamento esse colaborador está alocado, entrar no cadastro desse departamento e verificar se no campo **'Registro Fiscal Apro'** consta cadastrado algum registro fiscal, e se sim, verificar se é diferente do informado no cadastro da empresa.

Caso no cadastro do departamento esteja vinculado um registro fiscal diferente do cadastrado na empresa, é importante avaliar com o cliente o por que daquele cadastro.

**OBSERVAÇÃO:**

Importante também informar ao cliente o comportamento do sistema nestes casos, pois se for cadastrado um registro fiscal dentro do departamento do colaborador, todos os colaboradores que estiverem alocados neste mesmo departamento, no resumo da folha irá trazer as alíquotas referente ao registro fiscal do departamento, e não da empresa, porém caso não seja informado registro fiscal dentro do departamento, o sistema irá olhar para o que foi cadastrado na empresa.
