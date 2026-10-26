---
id: "42427294355351"
titulo: "R27- Como gerar o relatório de absenteísmo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427294355351-R27-Como-gerar-o-relat%C3%B3rio-de-absente%C3%ADsmo"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:53:04Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_705f41d3822a", "pontotel_6a3329ed48abe8c04826beb6"]
---

# R27- Como gerar o relatório de absenteísmo

O relatório R27, disponível na plataforma Pontotel, apresenta os indicadores de **absenteísmo voluntário, involuntário e total** dos colaboradores, trazendo uma visão consolidada sobre ausências dentro da empresa. Esse relatório é fundamental para o RH acompanhar padrões de faltas, analisar impactos na produtividade e embasar estratégias de gestão de pessoas.

---

## Passo a passo para gerar o relatório R27

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Selecione a opção "**R27 - Relatório de absenteísmo**".
3. Configure os filtros.

![Imagem 1: Configure os filtros.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1ivygxl.png)

**Escolha quem analisar**: Use as abas no topo para definir a base do relatório: **locais de trabalho**, **empregados** ou **grupos**. Selecione os itens desejados.
**Defina o período**: Informe **início período** e **fim período**. Esse intervalo determina **de quando até quando** o absenteísmo será calculado no arquivo.
**Opções extras** (marque apenas o que precisar):

- **Omitir empregado com valores zerados**: remove da planilha quem não teve ausências/ocorrências no período.
- **Exibir empregados demitidos**: inclui desligados dentro do período analisado.
- **Desconsiderar horas que entraram para o banco de horas**: ignora apontamentos já enviados ao BH, para não contabilizar como ausência.
- **Omitir faltas, atrasos e saídas antecipadas em caso de BH positivo no período**: se o colaborador fecha o período com saldo de BH positivo, não conta essas ocorrências negativas no relatório.
- **Incluir aba de total por empregador**: adiciona uma aba no arquivo com médias de absenteísmo por empregador.
- **Incluir aba de total por local de trabalho**: diciona uma aba no arquivo com médias de absenteísmo por local de trabalho.
- **Considerar suspensão no relatório**: contabiliza **suspensões** no cálculo (entra no bloco de ausências involuntárias).

4. Clique em "Gerar excel" para iniciar o processamento do relatório.
5. No menu de navegação, clique no **ícone de sino** (Notificações), para acompanhar o arquivo ser gerado.
6. Quando chegar a "100%", o relatório será baixado automaticamente.

---

## Entenda o relatório

O relatório é exportado em formato Excel e apresenta diversas colunas com informações detalhadas sobre cada colaborador. Veja abaixo o que significa cada campo, e também as fórmulas utilizadas para chegar nos valores de determinados campos:

- Colunas |**Senha, Código, Nome, CPF, Função, Departamento, Local de Trabalho, Data de admissão**: dados cadastrais do colaborador.
- Coluna I |**Tempo de casa:** Tempo de vínculo do empregado até uma data de referência do relatório, expresso em anos decimais (duas casas).
- Coluna J |**Total de horas previstas do período:**quantidade de horas de trabalho esperadas no período.
- Coluna K | **Total de horas de falta:**quantidade de horas de falta dentro do período.
- Coluna L |**Total de horas de atraso:**quantidade de horas de atraso (em relação à jornada esperada), feito pelo colaborador dentro do período.
- Coluna M | **Total de saída antecipada:**quantidade de horas de saída antecipada (em relação à jornada esperada), feita pelo colaborador dentro do período**.**
- Coluna N |**Total de horas de ausência injustificada:** soma do tempo de falta, atraso e saída antecipada. **Fórmula**: **K + L + M**
- Coluna O |**Total de horas de dispensa:** quantidade de ausências justificadas por meio de dispensa (parcial ou do dia todo), como afastamentos médicos.
- Coluna P | **Total**: soma das ausências justificadas e injustificadas. **Fórmula**: **N + O**
- Coluna Q |**% Absenteísmo voluntário**: percentual de ausências voluntárias em relação ao total de horas previstas no período. **Fórmula**: **(N ÷ J) × 100**.
- Coluna R |**% Absenteísmo involuntário**: percentual de ausências justificadas em relação ao total de horas previstas no período. **Fórmula**: **(O ÷ J) × 100**.
- Coluna S**| % Absenteísmo total**: percentual total de ausências (voluntárias + involuntárias) em relação às jornadas de trabalho previstas. **Fórmula**: **(P ÷ J) × 100**.

Além das informações individuais por colaborador, o relatório também permite calcular médias de absenteísmo:

- **Por local de trabalho**: some os percentuais de absenteísmo dos colaboradores de um mesmo local e divida pelo número de colaboradores.
- **Por empregador**: siga a mesma lógica, considerando todos os funcionários vinculados ao empregador.

---

## Conclusão

O **Relatório R27 – Absenteísmo** é uma ferramenta essencial para monitorar ausências, diferenciar motivos voluntários e involuntários e identificar impactos no desempenho da equipe. Com ele, o RH pode tomar decisões mais estratégicas, implementar ações de engajamento e reduzir os índices de absenteísmo.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
