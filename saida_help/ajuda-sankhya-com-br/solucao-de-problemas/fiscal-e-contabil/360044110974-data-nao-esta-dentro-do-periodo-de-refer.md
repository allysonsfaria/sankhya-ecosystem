---
id: "360044110974"
titulo: "Data não está dentro do período de referência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110974-Data-n%C3%A3o-est%C3%A1-dentro-do-per%C3%ADodo-de-refer%C3%AAncia"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:45Z"
rotulos: ["Configuração", "Agendamento", "Contabilização", "Financeiro", "Prioridade em campos incorretos", "Ajustar agendamento ou usar modo manual", "Data fora do período", "Erro"]
---

# Data não está dentro do período de referência

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18610396502807) MENSAGEM:**

Data não está dentro do período de referência.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18610455746199) SITUAÇÃO:**

Ao executar a contabilização pela tela de Agendamento do Sankhya OM mesmo que os lançamentos a serem contabilizados estejam dentro do período os mesmos não são contabilizados e é apresentada a mensagem que o documento está fora da referência.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18610455761559) CAUSA:**

Quando se utiliza o tipo de execução de forma manual mesmo informando o período no filtro,  o sistema utiliza da prioridade aos campos citados acima e causa a mensagem.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18610396529687) SOLUÇÃO:**

Acesse Contabilização » Rotinas » Agendamento

Aba: Parâmetros
--**Processamento dia a dia**--

- Qtde de dias a retroceder em relação a data de processamento?
- Qtde de dias a processar?

Considere o conceito dos campos acima o seguinte:
Para processamento da constante ${dia-a-dia}:

Por exemplo, se a data do processamento for 13/01 qtde de dias a retroceder for 5:
Então o dia que começa o processamento é dia 08/01.
Se qtde de dias a processar for 2, serão processados os dias 8 e 9/01.
Se qtde de dias a processar for 4, serão processados os dias 8, 9, 10 e 11/01.

Caso a contabilização seja de acordo com o período desejado e digitado na Contabilização Manual, considere criar um agendamento do tipo 'Manual' e não informar valores nos respectivos campos indicado acima, ou ajustar o agendamento utilizado. Salve o registro, efetue a contabilização e posteriormente volte os valores anteriormente informado nos campos.
