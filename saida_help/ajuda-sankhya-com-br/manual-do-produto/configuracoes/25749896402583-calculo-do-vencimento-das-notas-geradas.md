---
id: "25749896402583"
titulo: "Cálculo do vencimento das notas geradas a partir do Faturamento de Contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:42:54Z"
rotulos: ["Configuração", "Faturamento", "Contrato", "CONTSOFT", "Financeiro", "Parâmetro", "Vencimento Fixo", "Data de Faturamento", "Dias Corridos", "cálculo do Vencimento", "Vencimento calculado"]
---

# Cálculo do vencimento das notas geradas a partir do Faturamento de Contratos

Neste artigo serão apresentadas as diversas possibilidades de parametrizações para a realização do cálculo do vencimento das notas geradas a partir do [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos).

Nas negociações contratuais, sabe-se que a variedade de acordos é imensa. Cada contrato possui suas particularidades, desde a periodicidade do faturamento até as condições de pagamento. Diante dessa diversidade é fundamental que o sistema ofereça flexibilidade para configurar o cálculo do vencimento das notas de acordo com as especificidades de cada negócio.

A seguir, serão apresentados os cenários mais comuns e as melhores práticas para ajustar essas parametrizações com o objetivo de fornecer uma visão clara e prática para gestão eficaz dos contratos:

| Parametrizações que influenciam nesta rotina |
| --- |
| [Parametrizar contrato para faturamento com Vencimento Fixo](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#ParametrizarcontratoparafaturamentocomVencimentoFixo) |
| [Parametrizar contrato para faturamento com Vencimento calculado em Dias Úteis a partir da](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#ParametrizarcontratoparafaturamentocomVencimentocalculadoemDias%C3%9AteisapartirdaDatadeFaturamento) [Data de Faturamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#ParametrizarcontratoparafaturamentocomVencimentocalculadoemDias%C3%9AteisapartirdaDatadeFaturamento) |
| [Parametrizar contrato para faturamento com Vencimento calculado em Dias Corridos a partir do](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#ParametrizarcontratoparafaturamentocomVencimentocalculadoemDiasCorridosapartirdodia1%C2%BAdom%C3%AAsdarefer%C3%AAnciafaturada)  [dia 1º do mês da referência faturada](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#ParametrizarcontratoparafaturamentocomVencimentocalculadoemDiasCorridosapartirdodia1%C2%BAdom%C3%AAsdarefer%C3%AAnciafaturada) |
| [Parametrizar contrato para faturamento usando o campo Dia do Pagamento como base para o](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#ParametrizarcontratoparafaturamentousandoocampoDiadoPagamentocomobaseparaoc%C3%A1lculodoVencimento)[cálculo do Vencimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#ParametrizarcontratoparafaturamentousandoocampoDiadoPagamentocomobaseparaoc%C3%A1lculodoVencimento) |
| [Parametrizações com o parâmetro CONTSOFT - Contrato para software? = LIGADO](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#Parametriza%C3%A7%C3%B5escomopar%C3%A2metroCONTSOFT-Contratoparasoftware?=LIGADO) |

### Parametrizar contrato para faturamento com Vencimento Fixo

Neste tópico, realiza-se uma configuração para que as notas fiscais geradas pelo Faturamento de Contratos tenham o dia de vencimento fixo, calculado a partir da referência e independente da data de faturamento.

Por exemplo, se o contrato estabelece que o vencimento das notas será sempre no dia 10 do mês seguinte ao faturamento, então, mesmo que o faturamento da referência de Julho/2024 (01/07/2024) ocorra nos dias 02/07/2024, 05/07/2024 ou 15/07/2024, a nota sempre vencerá no dia 10/08/2024.

![Imagem 1: Acesse a tela Preferências e certifique-se de que o parâmetro "Contrato para software? - CONTSOFT" esteja desligado.](https://ajuda.sankhya.com.br/hc/article_attachments/25749935000343) Acesse a tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) e certifique-se de que o parâmetro **"Contrato para software? - CONTSOFT"** esteja desligado.

![Imagem 2: Acesse a tela Contratos , e ao inserir um novo contrato ou editar um já existente, na aba Propriedades é necessario…](https://ajuda.sankhya.com.br/hc/article_attachments/25749935002391) Acesse a tela [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), e ao inserir um novo contrato ou editar um já existente, na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abapropriedades) é necessario habilitar a marcação **"Dia Fixo para vencimento"**. No campo **"Dia do Pagamento"**, informe o dia para o qual se deseja gerar o vencimento da nota. Já no campo **"Prazo Mensal para Pagamento"**, defina quantos meses subsequentes ao faturamento devem ser considerados para calcular o vencimento da nota.

Exemplo:

Dia do Pagamento: 10
Prazo Mensal para o Pagamento: 1

Ainda nesta tela, o campo **"Prazo de vencimento"** deve ser deixado vazio e a marcação **"Considera dia do pagamento como dia útil"** deve estar desabilitada.

[GIF animado: Imagem 3: Ainda nesta tela, o campo "Prazo de vencimento" deve ser deixado vazio e a marcação "Considera dia do pagamento como…](https://ajuda.sankhya.com.br/hc/article_attachments/25750466411927)

![Imagem 4: Acesse a tela Faturamento de Contratos (Contratos e Serviços»Rotinas» Faturamento de Contratos).](https://ajuda.sankhya.com.br/hc/article_attachments/25994072620567) Acesse a tela Faturamento de Contratos (Contratos e Serviços»Rotinas» Faturamento de Contratos).

Acesse o botão ![Imagem 5: Acesse o botão " Configurações para o Faturamento de Contratos " e desative a marcação "Gerar Financeiro pelo Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/25751848600983) **"Configurações para o Faturamento de Contratos"** e desative a marcação **"Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas"**. Com relação à opção **“Usar Tipo de Negociação do Contrato”**, fica a critério do usuário, porém ela não irá influenciar no cálculo do vencimento, neste caso.

Após realizar as configurações acima, definir os filtros, os parâmetros obrigatórios e aplicar, será possível visualizar o contrato com o campo **"Data Vencimento"** da grade calculado conforme o dia e prazo mensal configurados no contrato.

Exemplo:

Data para Faturamento: 22/07/2024

Mês para Referência: 01/07/2024

Data Vencimento: 10/08/2024

Ao realizar o faturamento, observe que o vencimento da nota estará calculado para o dia 10/08/2024, seguindo as parametrizações realizadas.

[GIF animado: Imagem 6: Ao realizar o faturamento, observe que o vencimento da nota estará calculado para o dia 10/08/2024, seguindo as…](https://ajuda.sankhya.com.br/hc/article_attachments/25752735048983)

![Imagem 7: Acesse a tela Faturamentos de Contratos (Cenário alternativo, somando o prazo do Tipo de Negociação ao Vencimento da…](https://ajuda.sankhya.com.br/hc/article_attachments/25752747801751) Acesse a tela Faturamentos de Contratos (Cenário alternativo, somando o prazo do Tipo de Negociação ao Vencimento da Tela calculado pelo Dia Fixo).

Uma outra alternativa possível para calcular o vencimento das notas é utilizar a configuração anterior como base para os cálculos, mas agora somando o prazo do Tipo de Negociação selecionado à informação exibida no campo Data Vencimento da tela.

Para isso, acesse o botão Configurações para o Faturamento de Contratos e habilite a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas.

Com relação a marcação Usar Tipo de Negociação do Contrato ela deve ser desabilitada caso o objetivo seja utilizar o Tipo de Negociação informado no contrato. Isso geralmente ocorre quando há variações nas negociações realizadas pela empresa juntamente aos seus parceiros.

Porém, caso exista um Tipo de Negociação padrão a ser utilizado no Faturamento de Contratos, a marcação Usar Tipo de Negociação do Contrato deve ser desabilitada, fazendo com que o sistema considere a informação inserida no campo Tipo de Negociação do [Painel de Parâmetros Obrigatórios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654-Faturamento-de-Contratos#paineldeparmetrosobrigatrios) da tela.

Após a realização das configurações acima, definir os filtros, os parâmetros obrigatórios será possível visualizar o contrato com o campo Data Vencimento da grade calculado conforme o dia e prazo mensal configurados no contrato.

Exemplo:

Data para Faturamento: 22/07/2024

Mês para Referência: 01/07/2024

Data Vencimento: 10/08/2024

Considere ainda a utilização do Tipo de Negociação configurado com prazo de 30 dias. Ao realizar o faturamento, observa-se que o Vencimento da Nota estará calculado para o dia 09/09/2024, seguindo as parametrizações realizadas. Observe o exemplo abaixo:

Memória de Cálculo: Data Vencimento da tela + Prazo das Parcelas
Memória de Cálculo: 10/08/2024 + 30 dias
Vencimento da Nota: 09/09/2024

### [GIF animado: Imagem 8: Memória de Cálculo : Data Vencimento da tela + Prazo das Parcelas Memória de Cálculo : 10/08/2024 + 30 dias Vencimento…](https://ajuda.sankhya.com.br/hc/article_attachments/42310530283543)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#top)

### Parametrizar contrato para faturamento com Vencimento calculado em Dias Úteis a partir da Data de Faturamento

Neste tópico realiza-se uma configuração para que as notas fiscais geradas pelo faturamento de contratos tenham o vencimento calculado em dias úteis a partir da Data de Faturamento.

Por exemplo, se o contrato estabelece que o vencimento das notas emitidas será 10 dias úteis após o seu faturamento, então, ao faturar o contrato no dia 10/07/2024, o sistema irá calcular automaticamente o vencimento da nota gerada para o dia 24/07/2024.

![Imagem 9: Por exemplo, se o contrato estabelece que o vencimento das notas emitidas será 10 dias úteis após o seu faturamento,…](https://ajuda.sankhya.com.br/hc/article_attachments/25776511667479)

![Imagem 10: Acesse a tela Preferências e certifique-se de que o parâmetro "Contrato para software? - CONTSOFT" esteja desligado .](https://ajuda.sankhya.com.br/hc/article_attachments/25749935000343) Acesse a tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) e certifique-se de que o parâmetro **"Contrato para software? - CONTSOFT"** esteja desligado**.**

![Imagem 11: Acesse a tela Contratos e, ao inserir um novo contrato ou editar um existente, na aba Propriedades , informe no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/25749935002391) Acesse a tela [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos) e, ao inserir um novo contrato ou editar um existente, na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abapropriedades), informe no campo Dia do pagamento a quantidade de dias úteis que deseja calcular o vencimento das notas, considerando como base a Data de Faturamento e habilite a marcação **"Considera dia do pagamento como dia útil"**.

Exemplo:

Dia do Pagamento: 10

Ainda nesta tela, o campo Prazo de vencimento deve ser deixado vazio, a marcação Dia Fixo para vencimento desabilitada e o valor do campo Prazo Mensal para Pagamento deve ser igual a 0 (zero).

[GIF animado: Imagem 12: Ainda nesta tela, o campo Prazo de vencimento deve ser deixado vazio, a marcação Dia Fixo para vencimento desabilitada…](https://ajuda.sankhya.com.br/hc/article_attachments/25777781420567)

![Imagem 13: Acesse a tela Faturamentos de Contratos , acione o botão Configurações para o Faturamento de Contratos e desabilite a…](https://ajuda.sankhya.com.br/hc/article_attachments/25994072620567) Acesse a tela Faturamentos de Contratos, acione o botão Configurações para o Faturamento de Contratos e desabilite a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas. Com relação à marcação Usar Tipo de Negociação do Contrato, fica a critério do usuário, porém ela não irá influenciar no cálculo do vencimento neste caso.

Após realizar as configurações acima, definir os filtros, os parâmetros obrigatórios e aplicar, será possível visualizar o contrato com o campo Data Vencimento calculado considerando a data de faturamento conforme os dia úteis configurados no contrato a partir do campo Dia do Pagamento.

Exemplo:

Data para Faturamento: 10/07/2024

Mês para Referência: 01/07/2024

Data Vencimento: 24/07/2024

Ao realizar o faturamento, observe que o vencimento da nota estará calculado para 24/07/2024, seguindo as parametrizações realizadas.

[GIF animado: Imagem 14: Ao realizar o faturamento, observe que o vencimento da nota estará calculado para 24/07/2024, seguindo as…](https://ajuda.sankhya.com.br/hc/article_attachments/25778827240087)

![Imagem 15: Acesse a tela Faturamentos de Contratos (Cenário Alternativo, somando o prazo do Tipo de Negociação ao Vencimento da…](https://ajuda.sankhya.com.br/hc/article_attachments/25752747801751) Acesse a tela Faturamentos de Contratos (Cenário Alternativo, somando o prazo do Tipo de Negociação ao Vencimento da Tela calculado pelo Dia Fixo).

Uma outra alternativa possível para calcular o vencimento das notas é utilizar a configuração anterior como base para os cálculos, mas agora somando o prazo do Tipo de Negociação selecionado à informação exibida no campo Data Vencimento da tela.

Para isso, acesse o botão Configurações para o Faturamento de Contratos e habilite a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas.

Com relação a marcação Usar Tipo de Negociação do Contrato ela deve estar habilitada caso o objetivo seja utilizar o Tipo de Negociação informado no contrato. Isso geralmente ocorre quando há variações nas negociações realizadas pela empresa juntamente aos seus parceiros.

Porém, se houver um Tipo de Negociação padrão, a marcação Usar Tipo de Negociação do Contrato deve ser desabilitada, fazendo com que o sistema considere a informação inserida no campo Tipo de Negociação do Painel de Parâmetros Obrigatórios da referida tela.

Após realizar as configurações acima, definir os filtros, os parâmetros obrigatórios e aplicar, será possível visualizar o contrato com o campo Data Vencimento da grade, calculado considerando a data de faturamento e os dias úteis configurados no contrato a partir do campo Dia do Pagamento.

Exemplo:

Data para Faturamento: 10/07/2024

Mês para Referência: 01/07/2024

Data Vencimento: 24/07/2024

Considere ainda que será utilizado o Tipo de Negociação seja configurado com prazo de 30 dias. Ao realizar o faturamento, observe que o vencimento da nota estará calculado para o dia 23/08/2024, seguindo as parametrizações realizadas. Observe o exemplo a seguir:

Memória de Cálculo: Data Vencimento da tela + Prazo das Parcelas

Memória de Cálculo: 24/07/2024 + 30 dias

Vencimento da Nota: 23/08/2024

[GIF animado: Imagem 16: Vencimento da Nota : 23/08/2024](https://ajuda.sankhya.com.br/hc/article_attachments/25781643428247)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#top)

### Parametrizar contrato para faturamento com Vencimento calculado em Dias Corridos a partir do dia 1º do mês da referência faturada

Neste tópico realize uma configuração para que as notas fiscais geradas pelo faturamento de contratos tenham o vencimento calculado em dias Corridos a partir do dia 1º do mês da referência faturada. 

Por exemplo, se o contrato estabelece que o vencimento das notas emitidas terá um prazo de 15 dias corridos para pagamento a partir do dia 1º da referência faturada, então, independente da data de faturamento do contrato, considerando o faturamento da referência de 01/07/2024, o sistema irá calcular automaticamente o vencimento da nota gerada para o dia 16/07/2024.

![Imagem 17: Por exemplo, se o contrato estabelece que o vencimento das notas emitidas terá um prazo de 15 dias corridos para…](https://ajuda.sankhya.com.br/hc/article_attachments/26786134305303)

![Imagem 18: Acesse a tela Preferências e certifique-se que o parâmetro Contrato para software? - CONTSOFT esteja desligado.](https://ajuda.sankhya.com.br/hc/article_attachments/25749935000343) Acesse a tela Preferências e certifique-se que o parâmetro Contrato para software? - CONTSOFT esteja desligado.

![Imagem 19: Acesse a tela Contratos e, ao inserir um novo contrato ou editar um existente, na aba Propriedades , informe no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/25749935002391) Acesse a tela Contratos e, ao inserir  um novo contrato ou editar um existente, na aba Propriedades, informe no campo Dia do Pagamento o valor 0 (zero) e no campo Prazo de Vencimento coloque a quantidade de dias corridos a serem calculados para o vencimento das notas considerando como base o dia 1º do mês de referência faturada. 

Exemplo:

Dia do Pagamento: 0

Prazo de Vencimento: 15

Ainda nesta tela, a marcação Considera dia do pagamento como dia útil deve ser desabilitado, o campo Dia Fixo para vencimento deve estar desativado e o valor do campo Prazo Mensal para Pagamento deve ser igual a 0 (zero).

[GIF animado: Imagem 20: Ainda nesta tela, a marcação Considera dia do pagamento como dia útil deve ser desabilitado, o campo Dia Fixo para…](https://ajuda.sankhya.com.br/hc/article_attachments/26812380797719)

![Imagem 21: Acesse a tela Faturamento de Contratos e acione o botão Configurações para o Faturamento de Contratos e desabilite a…](https://ajuda.sankhya.com.br/hc/article_attachments/25994072620567) Acesse a tela Faturamento de Contratos e acione o botão Configurações para o Faturamento de Contratos e desabilite a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas. Com relação à marcação Usar Tipo de Negociação do Contrato, fica a critério do usuário, porém ela não irá influenciar no cálculo do vencimento neste caso.

Após realizar as configurações acima, definir os filtros, os parâmetros obrigatórios e aplicar, será possível visualizar o contrato com campo Data Vencimento da grade, calculado considerando o 1º dia do mês da referência faturada juntamente com os dias corridos configurados no contrato a partir do campo Dia do Pagamento.

Exemplo:

Data para Faturamento: 10/07/2024

Mês para Referência: 01/07/2024

Data Vencimento: 16/07/2024

Ao realizar o faturamento, observe que o vencimento da nota estará calculado para 16/07/2024, seguindo as parametrizações realizadas.

[GIF animado: Imagem 22: Ao realizar o faturamento, observe que o vencimento da nota estará calculado para 16/07/2024, seguindo as…](https://ajuda.sankhya.com.br/hc/article_attachments/26812610925847)

![Imagem 23: Acesse a tela Faturamentos de Contratos (Cenário alternativo, somando o prazo do Tipo de Negociação ao Vencimento da…](https://ajuda.sankhya.com.br/hc/article_attachments/25752747801751) Acesse a tela Faturamentos de Contratos (Cenário alternativo, somando o prazo do Tipo de Negociação ao Vencimento da Tela calculado pelo Dia Fixo).

Uma outra alternativa possível para calcular o vencimento das notas é utilizar a configuração anterior como base para os cálculos, mas agora somando o prazo do Tipo de Negociação selecionado à informação exibida no campo Data Vencimento da tela.

Para isso, acesse o botão Configurações para o Faturamento de Contratos e habilite a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas.

Com relação a marcação Usar Tipo de Negociação do Contrato ela deve estar habilitada caso o objetivo seja utilizar o Tipo de Negociação informado no contrato. Isso geralmente ocorre quando há variações nas negociações realizadas pela empresa juntamente aos seus parceiros.

Porém, se houver um Tipo de Negociação padrão, a marcação Usar Tipo de Negociação do Contrato deve ser desabilitada, fazendo com que o sistema considere a informação inserida no campo Tipo de Negociação do Painel de Parâmetros Obrigatórios da referida tela.

Após realizar as configurações acima, definir os filtros, os parâmetros obrigatórios e aplicar, será possível visualizar o contrato com o campo Data Vencimento da grade, calculado considerando o 1º dia do mês da referência faturada juntamente com os dias corridos configurados no contrato a partir do campo Dia do Pagamento.

Exemplo:

Data para Faturamento: 10/07/2024

Mês para Referência: 01/07/2024

Data Vencimento: 16/07/2024

Considere ainda a utilização de um Tipo de Negociação configurado com um prazo de 30 dias. Ao realizar o faturamento, observe que o vencimento da nota estará calculado para o dia 15/08/2024, seguindo as parametrizações realizadas. Observe o exemplo a seguir:

Memória de Cálculo: Data Vencimento da tela + Prazo das Parcelas

Memória de Cálculo: 16/07/2024 + 30 dias

Vencimento da Nota: 15/08/2024

[GIF animado: Imagem 24: Vencimento da Nota : 15/08/2024](https://ajuda.sankhya.com.br/hc/article_attachments/26814767643671)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#top)

### Parametrizar contrato para faturamento usando o campo Dia do Pagamento como base para o cálculo do Vencimento

Neste tópico realiza-se uma configuração para que as notas fiscais geradas pelo faturamento de contratos tenham o vencimento calculado usando como base apenas a informação do campo Dia do Pagamento do contrato.

Por exemplo, se o contrato estiver configurado com o Dia do Pagamento igual a 15, ao realizar o faturamento da referência de Julho/2024 (01/07/2024), independente da data em que estiver faturando, o vencimento será calculado para o dia 15/07/2024, ou seja, no dia indicado nas configurações e sempre no mesmo mês de referência indicado nos parâmetros da tela de Faturamento de Contrato.

![Imagem 25: Essa configuração é indicada para os casos em que o processo de faturamento esteja totalmente alinhado para ocorrer…](https://ajuda.sankhya.com.br/hc/article_attachments/25750494624151) Essa configuração é indicada para os casos em que o processo de faturamento esteja totalmente alinhado para ocorrer antes do Dia do Pagamento. Dessa forma, evita-se que a nota seja gerada com um vencimento anterior à Data de Faturamento. Por exemplo, ao faturar no dia 25/07, a nota não deve ter um vencimento em 15/07.

Há, no entanto, um recurso que pode apenas utilizar essa configuração como base e acrescentar a ela o prazo do Tipo de Negociação utilizado no faturamento, que será demonstrado abaixo, no item 4 deste tópico.

![Imagem 26: Acesse a tela Preferências , certifique-se de que o parâmetro CONTSOFT-Contrato para software? esteja desabilitado .](https://ajuda.sankhya.com.br/hc/article_attachments/25749935000343) Acesse a tela Preferências, certifique-se de que o parâmetro CONTSOFT-Contrato para software? esteja desabilitado**.**

![Imagem 27: Acesse a tela Contratos e, ao inserir um novo contrato ou editar um existente, na aba Propriedades , no campo Dia do…](https://ajuda.sankhya.com.br/hc/article_attachments/25749935002391) Acesse a tela Contratos e, ao inserir um novo contrato ou editar um existente, na aba Propriedades, no campo Dia do Pagamento informe  o dia desejado para gerar o vencimento da nota.

Exemplo:

Dia do Pagamento: 15

Ainda nesta tela, o **campo Prazo de vencimento deve estar vazio, as marcações Dia Fixo para vencimento e**Considera dia do pagamento como dia útil **deverão estar desabilitadas e o campo Prazo Mensal para Pagamento deve ter seu valor igual a 0 (zero).**

[GIF animado: Imagem 28: Ainda nesta tela, o campo Prazo de vencimento deve estar vazio, as marcações Dia Fixo para vencimento e Considera dia…](https://ajuda.sankhya.com.br/hc/article_attachments/26812949313559)

![Imagem 29: Acesse a tela Faturamento de Contratos , acione o botão Configurações para o Faturamento de Contratos e desabilite a…](https://ajuda.sankhya.com.br/hc/article_attachments/25994072620567) Acesse a tela Faturamento de Contratos, acione o botão Configurações para o Faturamento de Contratos e desabilite a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas. Com relação a marcação Usar Tipo de Negociação do Contrato, fica a critério do usuário, porém ela não irá influenciar no cálculo do vencimento, neste caso.

Após realizar as configurações acima, definir os filtros, os parâmetros obrigatórios e aplicar, será possível visualizar o contrato com o campo Data Vencimento da grade, que será calculado com base no Dia do Pagamento informado no contrato e no Mês para Referência informado na tela.

Exemplo:

Data para Faturamento: 10/07/2024

Mês para Referência: 01/07/2024

Data Vencimento: 25/07/2024

Ao realizar o faturamento, observe que o vencimento da nota estará calculado para 15/07/2024, seguindo as parametrizações realizadas.

[GIF animado: Imagem 30: Ao realizar o faturamento, observe que o vencimento da nota estará calculado para 15/07/2024, seguindo as…](https://ajuda.sankhya.com.br/hc/article_attachments/26815876810903)

![Imagem 31: Acesse a tela Faturamentos de Contratos (Cenário alternativo, somando o prazo do Tipo de Negociação ao Vencimento da…](https://ajuda.sankhya.com.br/hc/article_attachments/25752747801751)Acesse a tela Faturamentos de Contratos (Cenário alternativo, somando o prazo do Tipo de Negociação ao Vencimento da Tela calculado pelo Dia Fixo).

Uma outra alternativa possível para calcular o vencimento das notas é utilizar a configuração anterior como base para os cálculos, mas agora somando o prazo do Tipo de Negociação selecionado à informação exibida no campo Data Vencimento da tela.

Para isso, acesse o botão Configurações para o Faturamento de Contratos e habilite a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas.

Com relação à marcação Usar Tipo de Negociação do Contrato, ela deve estar habilitada caso o objetivo seja utilizar o Tipo de Negociação informado no contrato. Isso geralmente ocorre quando há variações nas negociações realizadas pela empresa junto a seus parceiros.

Porém, se houver um Tipo de Negociação padrão a ser utilizado no faturamento dos contratos, a marcação Usar Tipo de Negociação do Contrato deve ser desmarcada, fazendo com que o sistema considere a informação inserida no campo Tipo de Negociação na seção de Parâmetros Obrigatórios da tela.

Após realizar as configurações acima, definir os filtros, os parâmetros obrigatórios e aplicar, será possível visualizar o contrato com o campo Data Vencimento da grade,  calculado conforme o Dia do Pagamento informado no contrato e o  Mês para Referência informado na tela.

Exemplo:

Data para Faturamento: 10/07/2024

Mês para Referência: 01/07/2024

Data Vencimento: 15/07/2024

Considere ainda que seja utilizado um Tipo de Negociação configurado com um prazo de 45 dias.

Ao realizar o faturamento, observe que o vencimento da nota estará calculado para 29/08/2024, seguindo as parametrizações realizadas.

Memória de Cálculo: Data Vencimento da tela + Prazo das Parcelas

Memória de Cálculo: 15/07/2024 + 45 dias

Vencimento da Nota: 29/08/2024

[GIF animado: Imagem 32: Vencimento da Nota : 29/08/2024](https://ajuda.sankhya.com.br/hc/article_attachments/26815102162199)

![Imagem 33: Com o parâmetro Contrato para software? - CONTSOFT configurado como desligado, não há nenhuma configuração que calcule…](https://ajuda.sankhya.com.br/hc/article_attachments/25750494624151) Com o parâmetro Contrato para software? - CONTSOFT configurado como desligado, não há nenhuma configuração que calcule o vencimento das notas geradas a partir do faturamento de contratos usando como parâmetro apenas a data de faturamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#top)

### Parametrizações com o parâmetro CONTSOFT - Contrato para software? = LIGADO

![Imagem 34: A ativação desse parâmetro implica em uma série de validações adicionais no Faturamento de Contratos e deve ser…](https://ajuda.sankhya.com.br/hc/article_attachments/25750494624151) A ativação desse parâmetro implica em uma série de validações adicionais no Faturamento de Contratos e deve ser avaliada com cautela antes da sua ativação.

![Imagem 35: Com o parâmetro Contrato para software? - CONTSOFT configurado como ligado, todas as configurações acima citadas ainda…](https://ajuda.sankhya.com.br/hc/article_attachments/25749935000343) Com o parâmetro Contrato para software? - CONTSOFT configurado como ligado, todas as configurações acima citadas ainda prevalecem, desde que não haja informação no campo Tipo de Negociação independente da marcação Usar Tipo de Negociação do Contrato do botão Configurações para o Faturamento de Contratos da tela de Faturamento de Contratos.

![Imagem 36: Com o parâmetro Contrato para software? - CONTSOFT configurado como ligado, todas as configurações acima citadas ainda…](https://ajuda.sankhya.com.br/hc/article_attachments/25938525959319)

![Imagem 37: Caso o parâmetro Contrato para software? - CONTSOFT esteja ligado e tenha informação no campo Tipo de Negociação do…](https://ajuda.sankhya.com.br/hc/article_attachments/25749935002391) Caso o parâmetro Contrato para software? - CONTSOFT esteja ligado e tenha informação no campo Tipo de Negociação do contrato, o comportamento irá prevalecer apenas nos cenários em que a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas, do botão  Configurações para o Faturamento de Contratos estiver habilitada.

![Imagem 38: Caso o parâmetro Contrato para software? - CONTSOFT esteja ligado e tenha informação no campo Tipo de Negociação do…](https://ajuda.sankhya.com.br/hc/article_attachments/25994072620567) Caso o parâmetro Contrato para software? - CONTSOFT esteja ligado e tenha informação no campo Tipo de Negociação do contrato, mas a marcação Gerar Financeiro pelo Tipo de Negociação usando Vencto da tela + (mais) Prazo das parcelas, do botão Configurações para o Faturamento de Contratos estiver desabilitada, o vencimento das notas geradas sempre será calculado considerando a data de Faturamento + (mais) o prazo das parcelas do Tipo de Negociação, com comportamento semelhante ao que ocorre ao lançar uma nota diretamente pelas centrais.

Exemplo:

Data de Faturamento: 20/07/2024

Tipo de Negociação: Prazo 30 dias

Vencimento da Nota: 19/08/2024

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/25749896402583-C%C3%A1lculo-do-vencimento-das-notas-geradas-a-partir-do-Faturamento-de-Contratos#top)
