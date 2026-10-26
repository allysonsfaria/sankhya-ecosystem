---
id: "1500003244882"
titulo: "Afastamento previdenciário sem incidência INSS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003244882-Afastamento-previdenci%C3%A1rio-sem-incid%C3%AAncia-INSS"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-09-11T02:08:15Z"
rotulos: ["Configuração", "Atualização", "Impostos", "eSocial", "Folha de Pagamento", "SEFIP", "Parametrização do Sistema", "Decisão STF: INSS inconstitucional", "Orientações eSocial e SEFIP"]
---

# Afastamento previdenciário sem incidência INSS

| **(1)** De acordo com decisão tomada pelo STF- Supremo Tribunal Federal é inconstitucional a incidência do INSS sobre a contribuição previdenciária patronal, RAT Ajustado e INSS Terceiros nos eventos de afastamento previdenciários por doença ou acidente de trabalho. Essa decisão foi acolhida pelo Governo através do Parecer SEI Nº 16120/2020/ME e consequentemente houveram atualizações tanto no eSocial quanto na SEFIP, por esse motivo atualizamos o sistema em consonância com as novas medidas.  Em relação ao desconto do INSS de responsabilidade do segurado, o eSocial através do [“Perguntas Frequentes”](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes) orientou que também não haverá incidência, baseado no mesmo parecer citado acima, conforme abaixo:  “07.23 - (Atualizado em 01/02/2021) – Parecer SEI Nº 16120/2020/ME: Como deve ser tratada a incidência tributária nos 15 primeiros dias de afastamento que antecedem o benefício de auxílio-doença?   - Durante os primeiros quinze dias do afastamento da atividade por motivo de doença comum, doença ocupacional ou acidente do trabalho, cabe à empresa pagar ao segurado empregado o seu salário integral, porém a contribuição previdenciária patronal, a contribuição de terceiros e o SAT/RAT não incidem sobre esta importância paga pelo empregador referente a esses quinze primeiros dias que antecedem o benefício de auxílio-doença, bem como não há incidência da parte de contribuição previdenciária a cargo do empregado, de acordo com Jurisprudência consolidada do STJ, Parecer SEI Nº 16120/2020/ME. - Em se tratando de empregador pessoa jurídica ou equiparado a pessoa jurídica, o procedimento no eSocial - uma vez confirmado o afastamento superior a 15 dias e que tal afastamento resultou na concessão do benefício de auxílio-doença - inclusive acidentário - (Benefício por Incapacidade Temporária), o empregador deve lançar os respectivos valores referentes aos primeiros 15 dias na folha de pagamento, substituindo a rubrica remuneratória com {codIncCP} = [11 – Mensal], por outra rubrica remuneratória com {codIncCP} = [00 – Não é base de cálculo]. Desta maneira, as contribuições patronais e dos segurados não serão objeto de incidência para esta rubrica.   **A não incidência de contribuições está condicionada a concessão do auxílio-doença.** Nos casos em que essa condição não for implementada, as respectivas rubricas remuneratórias referentes aos dias de afastamento devem ter o {codIncCP}=[11 – Mensal].”   - Lembrando que o Manual da SEFIP não atualizou a regra da não incidência do INSS parte empregado nos primeiros 15 dias de afastamento, por isso cabe ao empregador a tomada de decisão quanto a não incidência. Nos exemplos que iremos apresentar neste documento seguiremos o posicionamento do eSocial. |
| --- |

## Parametrização do Sistema

**Importante:**

| - Utilizar as **versões disponibilizadas a partir do dia 26/02/2021**. |
| --- |

Seguem abaixo as parametrizações que serão necessárias no sistema para que as determinações acima sejam cumpridas.

### ![Imagem 1: Afastamento previdenciário Doença/acidente do trabalho com ocorrência de atestado e auxílio doença reincidente](https://ajuda.sankhya.com.br/hc/article_attachments/42310199831831) Afastamento previdenciário Doença/acidente do trabalho com ocorrência de atestado e auxílio doença reincidente

#### 1.1. Histórico de Ocorrências

**Situação do Funcionário 9- Atestado em dias Parte Empresa**

![Imagem 2: Situação do Funcionário 9- Atestado em dias Parte Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/12147078363927)

Essa é a configuração do código de afastamento do FGTS.

![Imagem 3: Essa é a configuração do código de afastamento do FGTS.](https://ajuda.sankhya.com.br/hc/article_attachments/15070373860631)

#### 1.2. Registro de Ocorrência:

![Imagem 4: 1.2. Registro de Ocorrência:](https://ajuda.sankhya.com.br/hc/article_attachments/15070403384727)

#### 1.3. Configurações do Evento 113- Parte Empresa de Afastamentos:

![Imagem 5: 1.3. Configurações do Evento 113- Parte Empresa de Afastamentos:](https://ajuda.sankhya.com.br/hc/article_attachments/15070422339735)

![Imagem 6: 1.3. Configurações do Evento 113- Parte Empresa de Afastamentos:](https://ajuda.sankhya.com.br/hc/article_attachments/15070413893271)

**Fórmula 113- Parte Empresa de Afastamentos**

(&F1007 / 30) \* &DiasAfaEmpresa

**Fórmula do índice**

&DiasAfaEmpresa

&F1007: COMPOSIÇÃO SALÁRIO PARA FOLHA

#### 1.4. Cálculo Folha Mensal:

![Imagem 7: 1.4. Cálculo Folha Mensal:](https://ajuda.sankhya.com.br/hc/article_attachments/15070427825431)

#### 1.5. Resumo da Folha:

![Imagem 8: 1.5. Resumo da Folha:](https://ajuda.sankhya.com.br/hc/article_attachments/15070463184663)

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16305049124759) OBSERVAÇÃO:**

Verifique se os valores dos campos bateram na Guia GPS e na Integração com o Financeiro da Guia, de acordo com o Resumo da Folha.

### Imagem 10: Afastamento previdenciário Doença/Acidente do trabalho com lançamento da ocorrência de auxílio doença/acidente de… Afastamento previdenciário Doença/Acidente do trabalho com lançamento da ocorrência de auxílio doença/acidente de trabalho diretamente (sem ocorrência anterior de atestado médico):

#### 2.1. Registro de Ocorrências

![Imagem 11: 2.1. Registro de Ocorrências](https://ajuda.sankhya.com.br/hc/article_attachments/15070435100311)

#### 2.2 Cálculo Mensal

![Imagem 12: 2.2 Cálculo Mensal](https://ajuda.sankhya.com.br/hc/article_attachments/15070453727127)

#### 2.3. Resumo da Folha

![Imagem 13: 2.3. Resumo da Folha](https://ajuda.sankhya.com.br/hc/article_attachments/15070450901911)

**![Imagem 14: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16305049124759) OBSERVAÇÃO:**

Verifique se os valores dos campos bateram na Guia GPS e na Integração com o Financeiro da Guia, de acordo com o Resumo da Folha.

### Imagem 15: SEFIP (Atualizada até 04/01/2021) [SEFIP](https://www.caixa.gov.br/Downloads/fgts-manuais-e-cartilhas-operacionais/Manual_SEFIP_8_40_Jan2021.pdf) (Atualizada até 04/01/2021)

#### 3.1. Leiaute atual

Disponibilizado no [Place](http://place.sankhya.com.br/)

#### 3.2. Atualizações da SEFIP- Afastamento temporário referente aos primeiros 15 (quinze) dias que antecedem ao auxílio-doença por motivo de doença ou de acidente

![Imagem 16: 3.2. Atualizações da SEFIP- Afastamento temporário referente aos primeiros 15 (quinze) dias que antecedem ao…](https://ajuda.sankhya.com.br/hc/article_attachments/15070491054999)

**Sequência 16- Remuneração sem 13º- Base de Cálculo para incidência do FGTS**

![Imagem 17: Sequência 16- Remuneração sem 13º- Base de Cálculo para incidência do FGTS](https://ajuda.sankhya.com.br/hc/article_attachments/15070521002775)

![Imagem 18: Sequência 16- Remuneração sem 13º- Base de Cálculo para incidência do FGTS](https://ajuda.sankhya.com.br/hc/article_attachments/360104306033)

**Sequência 19- Ocorrência**

![Imagem 19: Sequência 19- Ocorrência](https://ajuda.sankhya.com.br/hc/article_attachments/360104306053)

![Imagem 20: Sequência 19- Ocorrência](https://ajuda.sankhya.com.br/hc/article_attachments/15070505356311)

**Sequência 20- Valor descontado do Segurado**

O Manual da SEFIP não deixa claro se compactua com o posicionamento dado pelo eSocial referente ao desconto do INSS segurado. Por isso cabe ao empregador decidir pela incidência ou não do INSS segurado, desabilitando o evento como base de cálculo do INSS caso decida pela não incidência.

Seguindo as orientações dadas pelo eSocial quanto a não incidência de INSS de responsabilidade do segurado nos valores dos 15 primeiros dias do afastamento previdenciário, o valor dessa SEFIP ficaria R$ 69,99 referente ao INSS dos dias efetivamente trabalhados

**Sequência 21- Remuneração base de Cálculo da Contribuição Previdenciária**

Conforme mencionado na sequência anterior, apesar do Manual não deixar claro se compactua ou não com a não incidência do INSS sobre os valores dos 15 primeiros dias do afastamento, na sequência 21 o Manual já afirma, no exemplo, que os valores a serem apresentados nesta sequência será referente aos dias efetivamente trabalhados mesmo afirmando no mesmo Manual que, “a princípio, o campo Base de Cálculo da Previdência Social deve ser igual ao campo Remuneração sem 13º Salário”, conforme print do Manual abaixo: 

![Imagem 21: Conforme mencionado na sequência anterior, apesar do Manual não deixar claro se compactua ou não com a não incidência…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003266582)

![Imagem 22: Conforme mencionado na sequência anterior, apesar do Manual não deixar claro se compactua ou não com a não incidência…](https://ajuda.sankhya.com.br/hc/article_attachments/15070477728151)

![Imagem 23: Conforme mencionado na sequência anterior, apesar do Manual não deixar claro se compactua ou não com a não incidência…](https://ajuda.sankhya.com.br/hc/article_attachments/15070539156631)

Seguindo as orientações dadas pelo eSocial quanto a não incidência de INSS de responsabilidade do segurado nos valores dos 15 primeiros dias do afastamento previdenciário, o valor dessa sequência na SEFIP ficaria R$ 933,33 referente ao INSS dos 14 dias efetivamente trabalhados
