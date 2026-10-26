---
id: "360052504233"
titulo: "Coluna 'Previsto' da tela de controle de ponto, demonstrando quantidade de horas maior do que carga horária definida. Como analisar ?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052504233-Coluna-Previsto-da-tela-de-controle-de-ponto-demonstrando-quantidade-de-horas-maior-do-que-carga-hor%C3%A1ria-definida-Como-analisar"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:09Z"
rotulos: ["Configuração", "Carga Horária", "Folha de Pagamento", "Parâmetro", "Coluna 'PREVISTO' controle de ponto", "Parâmetro FPFERSEMCOMP: LIGADO", "Completa carga semanal", "Feriado"]
---

# Coluna 'Previsto' da tela de controle de ponto, demonstrando quantidade de horas maior do que carga horária definida. Como analisar ?

#### Considere o seguinte caso de uso:

Foi cadastrado para o funcionário uma carga horaria diária de 08:48, no entanto nos dias 30/06, 01/07, 02/07 e 03/07 ( ter, quar, qui, sex), está demonstrando na coluna Previsto como 9:00 horas

Então foi verificado um cadastro de feriado no dia 29/06 (segunda) e o parâmetro **Feriado de seg.a sexta aumenta hr trab. na semana -** **FPFERSEMCOMP** estava ligado.

| Considere o seguinte caso, para **compreender o funcionamento desse parâmetro**:   - Considere que o sábado deveria ser trabalhado para compor a carga horária semanal do funcionário 'X'. - Porém, a empresa optou por distribuir as horas do sábado na carga horária de segunda à sexta.  Quando, no cenário acima, houver um feriado durante a semana [segunda à sexta]:   1. Com o parâmetro **LIGADO**, as horas de sábado que estavam somadas nesse dia [feriado],serão distribuídas nos demais dias da semana, para assim completar a carga horária semanal. 2. Com o parâmetro **DESLIGADO**, essa distribuição não ocorre, e a carga horária se mantém a mesma |
| --- |

Com parâmetro desligado, as horas previstas ficaram de acordo com a carga horária do funcionário.

![Imagem 1: Com parâmetro desligado, as horas previstas ficaram de acordo com a carga horária do funcionário.](https://ajuda.sankhya.com.br/hc/article_attachments/18849098025239)
