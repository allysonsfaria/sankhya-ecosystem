---
id: "37362924220951"
titulo: "Erro 317: O trabalhador do CPF ‘xxx.xxx.xxx-xx’, matrícula ‘xxxxx’, deverá encontrar-se ativo no período ‘2025-10’."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37362924220951-Erro-317-O-trabalhador-do-CPF-xxx-xxx-xxx-xx-matr%C3%ADcula-xxxxx-dever%C3%A1-encontrar-se-ativo-no-per%C3%ADodo-2025-10"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:18Z"
rotulos: ["Eventos", "Fiscal", "eSocial", "Configuração Funcionários", "Central do eSocial", "Erro", "transferência de funcionários entre empresas", "data de pagamento das férias", "Erro 317", "CNPJs de raízes diferentes", "não é possível enviar o S-1200"]
---

# Erro 317: O trabalhador do CPF ‘xxx.xxx.xxx-xx’, matrícula ‘xxxxx’, deverá encontrar-se ativo no período ‘2025-10’.

##### MENSAGEM:

##### Erro 317: O trabalhador do CPF ‘xxx.xxx.xxx-xx’, matrícula ‘xxxxx’, deverá encontrar-se ativo no período ‘2025-10’.

##### Ação sugerida: Verificar se o trabalhador encontra-se ativo no período ou se possui vinculação com outros eventos enviados posteriormente.

##### SITUAÇÃO:

Durante a transferência de funcionários entre empresas com CNPJs de raízes diferentes na referência 11/2025, foram enviados ao eSocial os seguintes eventos: o **S-2299** na empresa de origem e o **S-2200** na empresa de destino.

Após a transferência, foi necessário realizar o cálculo de férias para 3 funcionários na empresa de destino, com data de pagamento em **30/10**. No entanto, não foi possível enviar ao eSocial o **IRRF descontado das férias**, pois, nessa data, os funcionários ainda não estavam ativos na empresa de destino — o vínculo só iniciou em **01/11**.

##### SOLUÇÃO:

Para corrigir o problema, siga estas orientações:

**(1)** Recalcule as férias dos funcionários na empresa de destino.

**(2)** Ajuste o início do gozo das férias para ocorrer **a partir do terceiro dia útil do mês**.

**(3)** Garanta que a **data de pagamento das férias** esteja dentro da mesma referência em que o funcionário já esteja transferido.

Lembre-se: **Não é possível enviar o S-1200** em uma referência na qual o funcionário não possui vínculo ativo na empresa.

##### CAUSA:

O erro ocorre porque **não é permitido iniciar o gozo de férias no mesmo dia da transferência do funcionário**. Conforme a legislação, para que a transferência seja efetivada, o funcionário precisa estar ativo na nova empresa; no entanto, ao iniciar o gozo de férias, ele passa a estar afastado. Como essas duas situações não podem ocorrer simultaneamente, o sistema gera a inconsistência.

Essa condição gera inconsistência no eSocial, resultando no **Erro 317**, já que o sistema exige que o trabalhador esteja **ativo no período da referência** para o envio de eventos remuneratórios (como o S-1200).
