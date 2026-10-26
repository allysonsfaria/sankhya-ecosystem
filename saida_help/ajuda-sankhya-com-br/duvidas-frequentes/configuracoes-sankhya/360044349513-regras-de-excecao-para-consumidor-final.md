---
id: "360044349513"
titulo: "Regras de Exceção para Consumidor Final, Consumidor Contribuinte e Produtor Rural"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044349513-Regras-de-Exce%C3%A7%C3%A3o-para-Consumidor-Final-Consumidor-Contribuinte-e-Produtor-Rural"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-08-12T18:27:11Z"
rotulos: ["#RevisadoBraga", "Configuração", "Fiscal", "Parceiro", "ICMS", "Impostos", "TOP", "Exceções de Tributação por Perfil de Cliente"]
---

# Regras de Exceção para Consumidor Final, Consumidor Contribuinte e Produtor Rural

**(1)** Regras de Exceção para Consumidor Final, Consumidor Contribuinte e Produtor Rural.

(2)** Regra Consumidor Final:**
Primeiro verifica se tem exceção de ICMS para consumidor final dentro do estado. Senão tiver, verifica se tem exceção de ICMS para consumidor final fora do estado.

(2)** Regra Consumidor Contribuinte:**
Primeiro verifica se tem exceção de ICMS para eles fora do estado. Senão tiver, verifica se tem exceção para eles dentro do estado.  A regra para fora do estado será aplicada se na exceção "Tipo 1" a opção Consumidor Contribuinte for selecionada, sendo que esta opção será utilizada nessas operações mesmo que ela seja menos prioritária que as demais. Caso contrário, o sistema buscará a regra dentro do estado.

(2)** Regra Consumidor Final e Consumidor Contribuinte:**
Caso eles não encontrem nada de acordo com o descrito acima procederá da seguinte forma:
Considerará a exceção de dentro do estado mais próximo do processo que está sendo negociado. 
**Exemplo:** exceção por produto, grupo de produto, ICMS do parceiro e etc...

(2)** Regra Produtor Rural:**
Verifica a exceção de produtor rural de acordo com as UF´s envolvidas. Senão encontrar exceção de produtor rural, considerará a exceção mais próxima do processo que está sendo negociado dentro ou fora do estado.
**Exemplo:** Exceção por produto, grupo de produto, ICMS do parceiro e etc...

**(1)** Com o advento do Difal, o que é levado em consideração da regra é a origem e destino do consumidor não contribuinte. Sendo que antes era levado em consideração a operação estadual, agora é levado em consideração o destino e a origem, conforme as configurações, desde de que a TOP esteja marcado para 'Calcular Difal'.
