---
id: "360055738333"
titulo: "Como lançar uma ocorrência de estabilidade e realizar o cálculo da indenização na rescisão."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360055738333-Como-lan%C3%A7ar-uma-ocorr%C3%AAncia-de-estabilidade-e-realizar-o-c%C3%A1lculo-da-indeniza%C3%A7%C3%A3o-na-rescis%C3%A3o"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:21Z"
rotulos: ["#criadoroger", "Configuração", "Eventos", "Ocorrências", "Preferências", "Folha", "Rescisão", "Ocorrência de estabilidade", "Crie evento", "Configure estabilidade"]
---

# Como lançar uma ocorrência de estabilidade e realizar o cálculo da indenização na rescisão.

Configuração de ocorrência para lançamento de estabilidade e o uso do parâmetro que ativa a análise da estabilidade no momento do cálculo de rescisão.

![Imagem 1: Acesse o histórico de Ocorrências em (MGEPessoal>>Lançamentos>>Historico de Funcionarios>>Historico de Ocorrencias)](https://ajuda.sankhya.com.br/hc/article_attachments/18943054238999) Acesse o histórico de Ocorrências em (MGEPessoal>>Lançamentos>>Historico de Funcionarios>>Historico de Ocorrencias)

![Imagem 2: Acesse o histórico de Ocorrências em (MGEPessoal>>Lançamentos>>Historico de Funcionarios>>Historico de Ocorrencias)](https://ajuda.sankhya.com.br/hc/article_attachments/360090762794)

Para que gere a indenização na rescisão, é preciso marcar a opção "gera indenização por rescisão durante estabilidade".

![Imagem 3: Acesse a tela de preferências em (MGEPessoal>>Avançado>>Preferencias>>Todas as Preferências) Incluir o código do…](https://ajuda.sankhya.com.br/hc/article_attachments/18943026996247) Acesse a tela de preferências em (MGEPessoal>>Avançado>>Preferencias>>Todas as Preferências)
Incluir o código do histórico da ocorrência no parâmetro: **FPCODHISESTABIL**

![Imagem 4: Acesse a tela de preferências em (MGEPessoal>>Avançado>>Preferencias>>Todas as Preferências) Incluir o código do…](https://ajuda.sankhya.com.br/hc/article_attachments/18943026998679)

![Imagem 5: Acesse a tela de eventos em (MGEPEssoal>>Arquivos>>Eventos) Cariar um evento de Indenização por estabilidade com uma…](https://ajuda.sankhya.com.br/hc/article_attachments/18943027002647) Acesse a tela de eventos em (MGEPEssoal>>Arquivos>>Eventos)
Cariar um evento de Indenização por estabilidade com uma formula(Avançado>>Formulas de Cálculo) conforme abaixo:

![Imagem 6: Acesse a tela de eventos em (MGEPEssoal>>Arquivos>>Eventos) Cariar um evento de Indenização por estabilidade com uma…](https://ajuda.sankhya.com.br/hc/article_attachments/360090765454)

**Fórmula:**
(QueFuncionario.SALBASE \* IF(queFuncionario.TIPSAL = 5, QueFuncionario.HORASSEM \* 5, 1)) \* &MESESESTABILIDADE

**Fórmula indice:**
&MESDIRESTABILIDADE
