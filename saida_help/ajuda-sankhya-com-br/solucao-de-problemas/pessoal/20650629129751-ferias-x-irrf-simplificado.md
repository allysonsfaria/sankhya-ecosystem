---
id: "20650629129751"
titulo: "Férias x IRRF Simplificado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20650629129751-F%C3%A9rias-x-IRRF-Simplificado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:18:23Z"
rotulos: ["Configuração", "Eventos", "Fórmulas", "Folha", "eSocial", "Alterações INSS nova fórmula provisão INSS férias", "Separar INSS férias e mensal fórmulas e eventos modificados", "INSS férias incidência IRRF identificação evento", "IRRF"]
---

# Férias x IRRF Simplificado

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20650659298455) SOLUÇÃO:**

A partir de 2023, foi estabelecido através da MP 1171/23 um novo modelo do cálculo do IRRF retido, passando a admitir uma dedução simplificada mensal caso o valor da mesma seja maior que os valores das deduções legais (INSS Retido, Dependentes e Pensão Alimentícia).

O nosso sistema, levava para a folha mensal, o valor de INSS junto com o já descontado de férias, com o IRRF simplificado, tivemos que separar os dois valores.

Com isso tivemos que alterar alguns eventos e fórmulas para que a apuração do IRRF funcionasse corretamente, no caso de férias no mês.

**Importante:**

Se estiver utilizando o módulo Pessoal+ e os eventos referidos abaixo estiverem como padrão (protegidos), a atualização será feita automaticamente, através do botão 'Atualizar' da tela principal do cadastro de eventos.

![Imagem 2: Se estiver utilizando o módulo Pessoal+ e os eventos referidos abaixo estiverem como padrão (protegidos), a atualização…](https://ajuda.sankhya.com.br/hc/article_attachments/20650659299351)

#### Configuração de Eventos e Fórmulas

**Módulo Pessoal+**

Deverão ser feitos manualmente caso os eventos discriminados abaixo não estejam protegidos (sem cadeado no card).

![Imagem 3: Alteração da Configuração de Eventos:](https://ajuda.sankhya.com.br/hc/article_attachments/20650629095575) **Alteração da Configuração de Eventos:**

**(1)** XXXX - Ressarcimento INSS Férias

Acesse a tela **Eventos** (Pessoal+ » Cadastros » Eventos) selecione o evento com a descrição:  RESSARCIMENTO INSS FÉRIAS e faça as alterações listadas abaixo:

- Retire a incidência de IRRF:

Aba Avançado/ Campo IRRF - selecionar a opção “Não Incide”.

![Imagem 4: Aba Avançado/ Campo IRRF - selecionar a opção “Não Incide”.](https://ajuda.sankhya.com.br/hc/article_attachments/20650659303191)

**(1)** Retire a identificação do Evento

Aba Básico>> Campo “Identificação do evento”>> Selecionar a opção “0 - Sem Identificação”.

![Imagem 5: Aba Básico>> Campo “Identificação do evento”>> Selecionar a opção “0 - Sem Identificação”.](https://ajuda.sankhya.com.br/hc/article_attachments/20650659303959)

**(1)** Altere a incidência IRRF na aba Esocial

Aba ESOCIAL>> Campo “Incidência p/ IRRF” >> Alterar a incidência de IRRF para “09 - VERBA TRANSITADA PELA FOLHA DE PAGAMENTO DE NATUREZA DIVERSA DE RENDIMENTO OU RETENCAO/ISENCAO/DEDUCAO DE IR”.

![Imagem 6: Aba ESOCIAL>> Campo “Incidência p/ IRRF” >> Alterar a incidência de IRRF para “09 - VERBA TRANSITADA PELA FOLHA DE…](https://ajuda.sankhya.com.br/hc/article_attachments/20650659306391)

![Imagem 7: Alteração da fórmula de INSS:](https://ajuda.sankhya.com.br/hc/article_attachments/20650659307799) **Alteração da fórmula de INSS:**

**XXXX - INSS**

Acesse a tela **Fórmulas** (Pessoal+ » Cadastros » Fórmulas), selecione a fórmula com a descrição: INSS e alterar o texto da fórmula para: 

IF((fTemNaLista(formatnumeric('00', QueFuncionario.VINCULO), '02,80,90,99') = 'S') OR (QueFuncionario.CODCATEGESOCIAL = 111), 0, IF(&DIASTRA >= 0, TRUNCFOL(IF(@F\_RECOMPOSICAOBASEINSS > FTF(1, 3, @F\_RECOMPOSICAOBASEINSS, &Refere, QueFuncionario.TIPTAB), FTF(1, 4, @F\_RECOMPOSICAOBASEINSS, &Refere, QueFuncionario.TIPTAB) - @F\_RECOMPOSICAOINSSRETIDO, (((@F\_RECOMPOSICAOBASEINSS \* FTF(1, 1, @F\_RECOMPOSICAOBASEINSS, &Refere, QueFuncionario.TIPTAB)) / 100) - @F\_RECOMPOSICAOINSSRETIDO)), 2), 0)) - IF(@E\_RESSARCIMENTOINSSFERIAS > 0, @E\_RESSARCIMENTOINSSFERIAS ,0)

![Imagem 8: Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o…](https://ajuda.sankhya.com.br/hc/article_attachments/20650659310359) Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o INSS da folha mensal.

**Evento**

**XXXX - INSS Descontado nas férias**

![Imagem 9: XXXX - INSS Descontado nas férias](https://ajuda.sankhya.com.br/hc/article_attachments/20650629114263)

![Imagem 10: XXXX - INSS Descontado nas férias](https://ajuda.sankhya.com.br/hc/article_attachments/20650659318295)

![Imagem 11: XXXX - INSS Descontado nas férias](https://ajuda.sankhya.com.br/hc/article_attachments/20650659319831)

**Fórmula**

![Imagem 12: Fórmula](https://ajuda.sankhya.com.br/hc/article_attachments/20650629119127)

**Fórmula do valor:**

IF((@F\_DIASDEFERIASNAREFERENCIA <= 0), 0, IF((MemSetVar('ProvINSSComp', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '@C\_PROVISAODEDESCONTOINSS')) / IF(MemSetVar('IndProvINSSComp', IF(MemSetVar('Ind4410', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '@C\_FERIAS, @C\_LICENCAREMUNERADA')) > 0, MemGetVar('Ind4410'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '@C\_MEDIADEFERIAS'))) > 0, MemGetVar('IndProvINSSComp'), 1)) \* @F\_DIASDEFERIASNAREFERENCIA) > 0), MemGetVar('ProvINSSComp'), IF((MemSetVar('ProvINSSProx', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '@C\_PROVISAODEDESCONTOINSS')) / IF(MemSetVar('IndProvINSSProx', IF(MemSetVar('Ind4410Prox', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '@C\_FERIAS, @C\_LICENCAREMUNERADA')) > 0, MemGetVar('Ind4410Prox'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '@C\_MEDIADEFERIAS'))) > 0, MemGetVar('IndProvINSSProx'), 1)) \* @F\_DIASDEFERIASNAREFERENCIA) > 0), MemGetVar('ProvINSSProx'), IF((MemSetVar('ProvINSSProx1', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '@C\_PROVISAODEDESCONTOINSS')) / IF(MemSetVar('IndProvINSSProx1', IF(MemSetVar('Ind4410Prox1', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '@C\_FERIAS, @C\_LICENCAREMUNERADA')) > 0, MemGetVar('Ind4410Prox1'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '@C\_MEDIADEFERIAS'))) > 0, MemGetVar('IndProvINSSProx1'), 1)) \* @F\_DIASDEFERIASNAREFERENCIA) > 0) AND (&MESATU = 3), MemGetVar('ProvINSSProx1'), 0))))  

**MGE/ Módulo MGE Pessoal**

**Configuração de Eventos e Fórmulas**

Deverão ser feitos manualmente caso os eventos discriminados  abaixo não estejam protegidos (campo “Protegido” desmarcado).

![Imagem 13: Alteração da Configuração de Eventos XXXX - RESSARCIMENTO INSS FERIAS](https://ajuda.sankhya.com.br/hc/article_attachments/20650629095575)**Alteração da Configuração de Eventos**
**XXXX - RESSARCIMENTO INSS FERIAS**

**(1)** Acesse o menu “Eventos” Selecione o evento com a descrição: RESSARCIMENTO INSS FERIAS e fazer as alterações listadas abaixo:

**XXXX - RESSARCIMENTO INSS FERIAS**

Retire a incidência de IRRF: Aba Base de Cálculo / Campo IRRF - selecionar a opção “Não Incide”.

![Imagem 14: Retire a incidência de IRRF: Aba Base de Cálculo / Campo IRRF - selecionar a opção “Não Incide”.](https://ajuda.sankhya.com.br/hc/article_attachments/20650629120535)

**(1)** Retire a identificação do Evento: Aba Propriedades>> Campo “Identificação do Evento”>> Selecionar a opção “0 - Sem Identificação”.

![Imagem 15: (1) Retire a identificação do Evento: Aba Propriedades>> Campo “Identificação do Evento”>> Selecionar a opção “0 - Sem…](https://ajuda.sankhya.com.br/hc/article_attachments/20650659324311)

**(1)** Altere a incidência IRRF na aba Esocial

Aba Incidência >> Campo “Incidência p/ IRRF” >> Alterar a incidência de IRRF para “09 - VERBA TRANSITADA PELA FOLHA DE PAGAMENTO DE NATUREZA DIVERSA DE RENDIMENTO OU RETENCAO/ISENCAO/DEDUCAO DE IR”.

![Imagem 16: Aba Incidência >> Campo “Incidência p/ IRRF” >> Alterar a incidência de IRRF para “09 - VERBA TRANSITADA PELA FOLHA DE…](https://ajuda.sankhya.com.br/hc/article_attachments/20650659325335)

![Imagem 17: Alteração da fórmula de INSS:](https://ajuda.sankhya.com.br/hc/article_attachments/20650659307799) **Alteração da fórmula de INSS:**

**XXXX - INSS**

**(1)** Acesse a tela Fórmulas, selecione a fórmula com a descrição: INSS e altere o texto da fórmula para: 

IF((fTemNaLista(formatnumeric('00', QueFuncionario.VINCULO), '02,80,90,99') = 'S') OR (QueFuncionario.CODCATEGESOCIAL = 111),0,IF(&DIASTRA >= 0,TRUNCFOL(IF(&INSSMESAMES = 'S',0, IF(&F5080 > FTF(1,3,&F5080,&Refere,QueFuncionario.TIPTAB), FTF(1,4,&F5080,&Refere,QueFuncionario.TIPTAB) - &F5090,(((&F5080 \* FTF(1,1,&F5080,&Refere,QueFuncionario.TIPTAB)) / 100) - &F5090))),2),0)) - IF(&E9340>0, &E9340,0)

![Imagem 18: Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o…](https://ajuda.sankhya.com.br/hc/article_attachments/20650659310359) Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o INSS da folha mensal.
Evento:  XXXX - INSS DESCONTADO NAS FERIAS

![Imagem 19: Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o…](https://ajuda.sankhya.com.br/hc/article_attachments/20650629123863)

![Imagem 20: Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o…](https://ajuda.sankhya.com.br/hc/article_attachments/20650659327255)

![Imagem 21: Houve a necessidade da criação de um novo evento e fórmula para separar os valores da provisão de INSS nas férias e o…](https://ajuda.sankhya.com.br/hc/article_attachments/20650659328535)

**Fórmula:**

**XXXX - INSS Férias**

IF((&F4432 <= 0), 0, IF((MemSetVar('ProvINSSComp', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '9330')) / IF(MemSetVar('IndProvINSSComp', IF(MemSetVar('Ind4410', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '4410')) > 0, MemGetVar('Ind4410'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '4430'))) > 0, MemGetVar('IndProvINSSComp'), 1)) \* &F4432) > 0), MemGetVar('ProvINSSComp'), IF((MemSetVar('ProvINSSProx', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '9330')) / IF(MemSetVar('IndProvINSSProx', IF(MemSetVar('Ind4410Prox', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '4410')) > 0,MemGetVar('Ind4410Prox'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '4430'))) > 0, MemGetVar('IndProvINSSProx'), 1)) \* &F4432) > 0), MemGetVar('ProvINSSProx'), 0)))
