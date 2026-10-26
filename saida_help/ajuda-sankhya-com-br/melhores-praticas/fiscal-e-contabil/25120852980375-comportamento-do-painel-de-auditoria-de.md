---
id: "25120852980375"
titulo: "Comportamento do Painel de Auditoria de Pis e Cofins"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25120852980375-Comportamento-do-Painel-de-Auditoria-de-Pis-e-Cofins"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-09-22T16:56:15Z"
rotulos: ["Configuração", "Relatórios", "Fiscal", "Impostos", "EFD Contribuições", "Comportamento do Relatório de Conferência PIS/COFINS"]
---

# Comportamento do Painel de Auditoria de Pis e Cofins

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/25120852971159) **MENSAGEM:**

Foram identificadas divergências entre o 'Valor Contábil' esperado e o valor apresentado no relatório.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/25120821147543)SOLUÇÃO:**

**Exemplo de caso:**

Possuo uma nota fiscal que inclui frete no valor de R$ 343,72.

O valor contábil deste lançamento é de R$ 4.320,00; contudo, no relatório Painel de Auditoria de Pis e Cofins está sendo apresentado o valor incorreto de R$ 8.640,00.

![Imagem 3: O valor contábil deste lançamento é de R$ 4.320,00; contudo, no relatório Painel de Auditoria de Pis e Cofins está…](https://p23.zdusercontent.com/attachment/9618168/9ziqW5X6lAlPk9ZjiQAOGYJyC?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..AQcSZQSbmWaE7uCjiRrHbA.42AaD2-jHYsUcjg9aA-pWa7c_VTuvINsMoNJXnk6cV4rjyIlaFDHb6xPL1wFta5XxwaGb5u4f_QJZJJg0AfaJ1hdpLQ7MjWP56M4EgeQXofaNAwwc_8z9sfKefgOGT015QIm0G76wgnHOPbX_RmmqD3p3CdJFmUQuQMZf2JOYQlPuJETshaBL9-eK8lX2DdOzCJp8C-9muAiweKgVen0Mau1Hw7wJx66YuWpirhjC09lCR5QIgWMo_ANXJdhbdzDwWOK___zyOCy760IxeB36Ol9TN4A_yQuNIAQ0dF7oO0.P0c9ZZFVxVQzUu13wwqSTQ)

**Explicação:**

**(1)** A tela **"Painel de Auditoria de Pis e Cofins"** apresenta, por padrão, linhas conforme os impostos apurados na tabela TGFDIN (Consultar/Alterar Impostos...). Dessa forma, neste caso analisado, foi gerada uma linha adicional para cada item devido à inclusão do "Frete" no lançamento.

**(1)** Para uma melhor análise dos valores, recomenda-se a utilização do campo **"Tipo Incidência"** (Caminho: Livros Fiscais » Relatórios » Painel de Auditoria de Pis e Cofins), permitindo selecionar quais valores devem ser observados e, assim, evitar a ocorrência de divergências na visualização.

![Imagem 4: (1) Para uma melhor análise dos valores, recomenda-se a utilização do campo "Tipo Incidência" (Caminho: Livros Fiscais…](https://p23.zdusercontent.com/attachment/9618168/PZbglbQh9zgIQwx6kURFWTkP4?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..uFaNSEyYKmtnPqPACqlh_A.-ZmIEa1soy8nsmgjEQVB-dTDWKZE6DW8APvdPLSIdcEpu_LiwUUsaJlqKrWST_4drxdYn572889D1xGjpBCA_Qs__59vZ5PRsl-VeqfweZBA1VX4giuPr_v43TE9fMGMIMx56pLIRABNO3CHzCDHhAoooYziOpkSTSjz2XNyo7mU8ah7Lqo1G7eIGHxI2dncONLLNRnbawFQJZb2qWz6AZpW95LWPCHWGx9w2q8II3JSVuld49MsTRdGIZPhVgy9D33McjPrDOraWKZaDXGJrZMDmkYNFUTXuN7HoKi91bg.7m_bH-yGK9P-13atG3v8zw)
