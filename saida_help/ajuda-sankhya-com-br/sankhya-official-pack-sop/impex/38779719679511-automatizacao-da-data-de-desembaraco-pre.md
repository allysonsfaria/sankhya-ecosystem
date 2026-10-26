---
id: "38779719679511"
titulo: "Automatização da Data de Desembaraço Prevista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38779719679511-Automatiza%C3%A7%C3%A3o-da-Data-de-Desembara%C3%A7o-Prevista"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:01:13Z"
rotulos: ["Configuração", "Planejamento", "Atualização", "Importação", "Logística"]
---

# Automatização da Data de Desembaraço Prevista

Este manual explica a nova regra de cálculo automático para a **Data de Desembaraço Prevista**. O objetivo é **garantir que o seu cronograma de importação reflita a situação real da carga**, priorizando datas reais sobre as previsões iniciais.

#### 1. Como funciona o Cálculo Automático?

O sistema agora monitora o status do seu processo e ajusta a data de desembaraço seguindo uma regra de prioridade. O cálculo base é:

> Data de Desembarque (Base) + Lead Time (Dias de Desembaraço) = Data de Desembaraço Prevista

**Regra 1: Quando a carga ainda não desembarcou**

Se o campo **"Data de Desembarque Realizada"** estiver **vazio**, o sistema usará a previsão:

- **Base:** Data de Desembarque Prevista.
- **Resultado:** Data de Desembaraço calculada com base na expectativa de chegada.

**Regra 2: Quando o desembarque é confirmado**

Após o preenchimento da **''Data de Desembarque Realizada''**, a previsão anteriormente informada deixa de ser considerada, e o sistema recalcula os dados com base na data real do desembarque.

- **Base:** Data de Desembarque Realizada (**Prioridade Máxima**).
- **Resultado:** O planejamento passa a refletir o dia real em que a mercadoria chegou.

####

#### 2. Atualização Dinâmica (Gatilhos)

##### O sistema recalcula a data automaticamente sempre que houver alteração em um destes três campos:

- ##### Data de Desembarque Realizada: ao inserir ou modificar essa informação, o sistema refaz o cálculo imediatamente, considerando a data efetiva.
- ##### Data de Desembarque Prevista: quando a data realizada não estiver preenchida, qualquer alteração na previsão atualiza automaticamente a data de desembaraço.
- ##### Lead Time de Desembaraço: ao alterar o prazo estimado do processo (em dias), o sistema recalcula e atualiza a data final.

##### Nota: O valor "0" (zero) no Lead Time é considerado válido e resultará na mesma data da base.

#### 3. Resumo de Prioridades (Tabela de Consulta)

| Cenário | Data Base Utilizada | Regra de Cálculo |
| --- | --- | --- |
| Apenas previsão disponível | Desembarque **Previsto** | Data Prevista + Dias de Lead Time |
| Desembarque realizado | Desembarque **Realizado** | Data Real + Dias de Lead Time |
| Data Real removida | Desembarque **Previsto** | O sistema volta a considerar a Data Prevista |

#### 4. Benefícios para o planejamento

- **Agilidade:** elimina a necessidade de calcular datas manualmente no calendário, tornando o processo mais rápido e prático;
- **Precisão:** o cronograma aduaneiro é atualizado automaticamente conforme as informações reais da operação são registradas;
- **Rastreabilidade:** facilita a identificação de desvios e atrasos em relação ao planejamento inicial.

#####

##### INFORMAÇÕES ADICIONAIS

- ##### Mantenha sempre o campo ''Lead Time de Desembaraço'' atualizado conforme a complexidade de cada processo.
- Sempre que a mercadoria chegar, priorize o preenchimento da ''Data de Desembarque Realizada'' para que todo o fluxo seguinte de desembaraço seja corrigido automaticamente.
