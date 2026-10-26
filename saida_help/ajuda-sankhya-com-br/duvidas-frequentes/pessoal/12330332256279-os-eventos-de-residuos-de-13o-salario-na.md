---
id: "12330332256279"
titulo: "Os eventos de resíduos de 13º salário não esta indo para a DIRF com base na data de pagamento de acordo com INST NORMATIVA 1500/2014 no Inciso 3º"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12330332256279-Os-eventos-de-res%C3%ADduos-de-13%C2%BA-sal%C3%A1rio-n%C3%A3o-esta-indo-para-a-DIRF-com-base-na-data-de-pagamento-de-acordo-com-INST-NORMATIVA-1500-2014-no-Inciso-3%C2%BA"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:25:19Z"
rotulos: ["Configuração", "Impostos", "Folha", "DIRF", "Resíduos de 13º Salário e DIRF", "Documentos Eletrônicos", "Instrução Normativa"]
---

# Os eventos de resíduos de 13º salário não esta indo para a DIRF com base na data de pagamento de acordo com INST NORMATIVA 1500/2014 no Inciso 3º

Os eventos de resíduos de 13º salário não estão indo para a DIRF com base na data de pagamento de acordo com INST NORMATIVA 1500/2014 no Inciso 3º.

**Parecer da legislação abaixo:**

**A=> INST NORMATIVA 1500/2014** no Inciso 3º que diz "No caso de pagamento de complementação de Gratificação Natalina, posteriormente ao mês de quitação, o imposto deve ser recalculado tomando-se por base o total desse rendimento, mediante utilização da tabela do mês de quitação, deduzindo-se do imposto assim apurado o valor anteriormente.

**B=> ASSUNTO: IMPOSTO SOBRE A RENDA RETIDO NA FONTE - IRRF**
**EMENTA:** DÉCIMO TERCEIRO. ATRASO. COMPLEMENTAÇÃO.
Em caso de décimo terceiro salário pago parceladamente após dezembro, o valor do IRRF a ele relativo, deve obedecer à regra fixada no § 3º do art. 13 da Instrução Normativa RFB nº 1.500, de 29 de outubro de 2014. Os valores do décimo terceiro salário pagos parceladamente a partir de dezembro e os respectivos valores do IRRF devem ser informados na Declaração do Imposto sobre a Renda Retido na Fonte (DIRF) referente ao ano calendário em que cada parcela for paga.

**Conforme parecer acima, temos como padrão de acordo com Cenofisco adotado o princípio do pagamento na natureza em seu ano exercício.**
**Desta forma, o layout de regime de caixa busca os dados da referência, mesmo o valor sendo pago na referência seguinte caindo em outro exercício.**

Caso Cliente entenda e solicite conforme item B, será necessário ajuste da expressão do registro RTIRF, sequência 14 considerando:

Entendimento conforme item A adotado como padrão:
IF(Vars.REGPLR OR Vars.REGRRA, '', ABS(FsomAcuInfRend(Dados\_Detalhe.EMPRESA\_FUNCIONARIO,Dados\_Detalhe.CODIGO\_FUNCIONARIO,vars.ANOBASE,0,'V','K')))

Caso entenda conforme item B Ajustar a expressão do registro:
IF(Vars.REGPLR OR Vars.REGRRA, '', ABS(FCalcInfRend(Dados\_Detalhe.EMPRESA\_FUNCIONARIO,Dados\_Detalhe.CODIGO\_FUNCIONARIO,vars.ANOBASE,0,'V','K')))

Depois de ajustado gerar novamente o arquivo da DIRF e importar.
