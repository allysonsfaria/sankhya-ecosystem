---
id: "43673965332247"
titulo: "Como calcular férias, 13º, provisões, aviso e rescisão de horistas pela média"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43673965332247-Como-calcular-f%C3%A9rias-13%C2%BA-provis%C3%B5es-aviso-e-rescis%C3%A3o-de-horistas-pela-m%C3%A9dia"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Adicionais, Horas e Médias da Folha"
atualizado_em: "2026-10-14T11:25:23Z"
---

# Como calcular férias, 13º, provisões, aviso e rescisão de horistas pela média

A partir da versão **5.125**, o Pessoas+ passa a calcular a remuneração-base dos **colaboradores horistas** em férias, 13º salário, provisões, aviso prévio e rescisão considerando a **média do que o colaborador realmente recebeu**, e não mais um valor fixo baseado apenas na carga horária prevista em contrato.

A novidade é **opcional**: cada empresa decide se quer utilizá-la. Quando não ativada, o cálculo permanece exatamente como é hoje.

O cálculo por média para remuneração variável tem respaldo no **art. 142 da CLT** (férias calculadas com base na remuneração devida) e na **Lei nº 4.090/62** (13º salário), além das convenções coletivas aplicáveis às categorias horistas.

#### Para quem é

Este recurso é indicado para empresas e consultorias que processam a folha de **colaboradores horistas**, categoria cuja remuneração varia conforme as horas efetivamente trabalhadas, por conta de escalas, sazonalidade, faltas ou admissão e desligamento no meio do mês.

#### Conceitos rápidos

Para acompanhar o artigo, vale relembrar alguns termos:

- **Horista:** colaborador cuja remuneração é calculada por hora trabalhada, e não por um salário mensal fixo.
- **Média:** valor apurado a partir da remuneração de um conjunto de meses anteriores (a "janela" de apuração), usado como base de cálculo de verbas como férias e 13º.
- **Competência:** o mês de referência de um cálculo (por exemplo, a competência 03/2026).
- **Verbas incorporadas:** valores que passaram a fazer parte fixa da remuneração do colaborador (por exemplo, um adicional já incorporado ao salário).
- **Provisão:** reserva mensal que a empresa registra para cobrir verbas futuras, como férias e 13º.

#### O que muda

Hoje, férias, 13º salário, provisões, aviso prévio e rescisão do horista são calculados como se ele tivesse cumprido **integralmente** a carga horária prevista no contrato. Sempre que as horas realmente trabalhadas são diferentes da carga prevista, o valor calculado fica distante da remuneração que o colaborador de fato recebeu, para mais ou para menos.

Com a novidade ativada, o sistema passa a considerar a **média da remuneração das horas efetivamente trabalhadas**.

|  | Como é hoje | Como fica com a novidade ativada |
| --- | --- | --- |
| Base do cálculo | Carga horária prevista no contrato | Média das horas efetivamente trabalhadas |
| Resultado | Pode divergir do que o colaborador recebeu | Reflete a remuneração real do período |

**Exemplo**

> Os valores abaixo são **apenas um exemplo** para explicar o conceito. Eles não representam parâmetros do sistema nem um cálculo oficial.

Imagine um colaborador horista cuja carga prevista em contrato corresponderia a uma remuneração de **R$ 4.400,00 por mês**. Nos últimos meses, porém, por causa da escala e de algumas faltas, a remuneração média que ele **efetivamente recebeu** foi de **R$ 3.800,00 por mês**.

- **Como é hoje:** as férias seriam calculadas sobre os R$ 4.400,00 (a carga prevista), acima do que ele costuma receber.
- **Com a novidade ativada:** as férias são calculadas sobre a média real de R$ 3.800,00.

O mesmo vale no sentido contrário: se o colaborador tiver trabalhado **mais** horas do que o previsto (por exemplo, média efetiva de R$ 4.900,00), a média capta esse valor maior, e o cálculo o acompanha. A ideia central é que a base de cálculo reflita a realidade, não que ela seja sempre menor.

#### Como funciona

A novidade é ativada em duas etapas de configuração:

1. **Marque a rubrica como incidente em médias.** A rubrica de salário hora-variável deve estar marcada como incidente em médias pelo índice na tela **Eventos (**aba **Avançado >** campo **Incide sobre médias = Incide nas médias pelo índice)**.

   ![Imagem 1: Marque a rubrica como incidente em médias. A rubrica de salário hora-variável deve estar marcada como incidente em…](https://ajuda.sankhya.com.br/hc/article_attachments/43676000228631)
2. **Ative a opção na regra de cálculo.** Na tela **Regras de Cálculo** > Propriedades > Geral, ative a opção **Remuneração Horistas sobre média**.

   ![Imagem 2: Ative a opção na regra de cálculo. Na tela Regras de Cálculo > Propriedades > Geral, ative a opção Remuneração Horistas…](https://ajuda.sankhya.com.br/hc/article_attachments/43674282848407)

Feito isso, a parcela variável da remuneração do horista deixa de ser calculada pela fórmula fixa e passa a ser apurada pelo cálculo de médias já existente no sistema, o mesmo mecanismo usado hoje para horas extras, comissões e adicionais.

Observe o efeito em cada verba:

- **Férias:** calculadas com base na média da remuneração do período.
- **13º salário:** também passa a usar a média.
- **Aviso prévio:** acompanha a mesma base de média.
- **Rescisão:** acompanha automaticamente a média, porque suas parcelas (férias proporcionais, 13º proporcional e aviso prévio indenizado) reaproveitam os mesmos cálculos de férias, 13º e aviso.
- **Provisões de férias e de 13º:** passam a refletir a média, de modo que o valor provisionado ao longo do mês fique alinhado ao valor que será efetivamente pago.
- **Verbas incorporadas:** continuam sendo somadas normalmente ao cálculo, **fora da média**.

O **pagamento mensal normal** do horista não muda: continua sendo calculado pelas horas apontadas no mês.

#### Como conferir o cálculo

Você pode auditar a composição da média diretamente no **relatório de médias já existente**, que mostra as competências consideradas, as horas e os valores aplicados. Não é necessária nenhuma tela nova para essa conferência.

#### Pontos de Atenção

- **Definição do número de meses da média:** a quantidade de meses considerada continua sendo definida pela empresa ou consultoria, conforme a convenção coletiva (CCT) aplicável. O sistema não interpreta a CCT automaticamente.
- **Colaborador sem competências válidas no período:** se, na janela considerada, não houver nenhuma competência com horas apuradas (por exemplo, colaborador afastado durante todo o período), o valor da média será **zero**, e a verba considerará apenas o que houver de verbas incorporadas. Esse é o comportamento esperado, não é erro de configuração.
- **Admissão recente:** quando o colaborador tem menos tempo de casa do que a janela configurada, a média considera apenas os meses existentes desde a admissão.
- **Colaboradores com mais de um contrato:** a média é apurada **por contrato**, e não agrupada pela pessoa.
- **Não é retroativo:** a mudança vale para os cálculos feitos **após a ativação**. Competências já fechadas e enviadas ao eSocial não são recalculadas.
- **Comportamento de quem não ativar:** empresas que não ativarem a novidade continuam com o cálculo atual, sem qualquer alteração.

#### Perguntas Frequentes

**1. A ativação é obrigatória?**

Não. Cada empresa decide se quer ativar. Sem ativação, o cálculo permanece como é hoje.

**2. Isso muda o pagamento mensal do horista?**

Não. O pagamento mensal continua sendo calculado pelas horas apontadas no mês. A mudança afeta férias, 13º, aviso prévio, rescisão e as provisões dessas verbas.

**3. A novidade sempre reduz o valor pago?**

Não. A média reflete a remuneração real do período, pode ser menor ou maior que o cálculo atual, dependendo das horas efetivamente trabalhadas.

**4. Preciso recalcular competências anteriores?**

Não. A novidade vale para os cálculos feitos após a ativação; períodos já fechados e enviados ao eSocial não são reprocessados.

**5. Onde confiro como a média foi formada?**

No relatório de médias já existente, que discrimina as competências, as horas e os valores considerados.

**6. As verbas incorporadas entram na média?**

Não. Elas continuam sendo somadas ao cálculo normalmente, mas fora da média.

#### Artigos Relacionados

- [Cálculo de Férias](https://ajuda.sankhya.com.br/hc/pt-br/sections/39716344517783-C%C3%A1lculo-de-F%C3%A9rias)
- [Cálculo e Pagamento do 13º Salário](https://ajuda.sankhya.com.br/hc/pt-br/sections/39716664334615-C%C3%A1lculo-e-Pagamento-do-13%C2%BA-Sal%C3%A1rio)
- [Cálculo da Rescisão por Tipo de Desligamento](https://ajuda.sankhya.com.br/hc/pt-br/sections/39717055008279-C%C3%A1lculo-da-Rescis%C3%A3o-por-Tipo-de-Desligamento)
- [Como alterar o período das médias do 13º de 6 para 12 meses?](https://ajuda.sankhya.com.br/hc/pt-br/articles/39354981257111)
