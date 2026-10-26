---
id: "31667959763735"
titulo: "Como lançar o crédito do trabalhador (eConsignado) no MGE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:31:57Z"
rotulos: ["Configuração", "Eventos", "eSocial", "Folha de Pagamento", "Lançamento de Movimento", "FGTS", "empréstimo consignado", "eConsignado", "Crédito do trabalhador", "crédito do trabalhador MGE", "crédito eConsignado"]
---

# Como lançar o crédito do trabalhador (eConsignado) no MGE

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310252973719) Versão disponível: a partir da 4.65.05 / sanEsocial 3.11
```

---

Agora, o MGE permite que você registre o empréstimo do tipo **eConsignado** (também chamado de [Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/30769824971031)), conforme as novas regras do governo. Esse tipo de desconto é informado ao eSocial usando um novo formato (versão S-1.3).

O fluxo para **a solicitação do crédito eConsignado** ocorrerá da seguinte maneira:

| ![Imagem 2: O fluxo para a solicitação do crédito eConsignado ocorrerá da seguinte maneira:](https://ajuda.sankhya.com.br/hc/article_attachments/42310252976023) | 1. **Colaborador**: |
| --- | --- |
| - acessa a CTPS Digital; - simula o empréstimo; - envia a proposta ao banco. |

| ![Imagem 3: envia a proposta ao banco.](https://ajuda.sankhya.com.br/hc/article_attachments/42310191154967) | 2. **Banco**: |
| --- | --- |
| - analisa a proposta considerando a margem de consignação no eSocial; - aprova e faz o contrato do empréstimo. |

| ![Imagem 4: aprova e faz o contrato do empréstimo.](https://ajuda.sankhya.com.br/hc/article_attachments/42310191155351) | 3. **Empresa**: |
| --- | --- |
| - recebe a notificação do DET (Domicílio Eletrônico Trabalhista) para acessar o Portal Emprega Brasil; - no portal, consulta o extrato consolidado dos empréstimos consignados; - realiza o lançamento do empréstimo na folha de pagamento do colaborador; - realiza o cálculo da folha mensal ou rescisão com o desconto; - envia o evento correspondente ao desconto ao eSocial. |

| ![Imagem 5: envia o evento correspondente ao desconto ao eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/42310252979607) | 4. **eSocial**: |
| --- | --- |
| - envio da rubrica com natureza 9253 e o código de FGTS 31 pelo evento S-1010; - envio do desconto da parcela do empréstimo através dos eventos S-1200/S-2299 ou S-2399.   **Nota:** o eSocial Simplificado (MEI, Segurado Especial e Doméstico), o                      desconto ocorre automaticamente. |

| ![Imagem 6: Nota: o eSocial Simplificado (MEI, Segurado Especial e Doméstico), o desconto ocorre automaticamente.](https://ajuda.sankhya.com.br/hc/article_attachments/42310252980503) | 5. **Portal FGTS Digital**: |
| --- | --- |
| - emite a GFD (Guia de Recolhimento Digital) mensal com os valores das parcelas dos empréstimos informadas ao eSocial;   ![Imagem 7: A empresa deve pagar a GFD via PIX.](https://ajuda.sankhya.com.br/hc/article_attachments/31716812759831) A empresa deve pagar a GFD via PIX. |

| ![Imagem 8: A empresa deve pagar a GFD via PIX.](https://ajuda.sankhya.com.br/hc/article_attachments/42310191158423) | 6. **Caixa Econômica Federal**: |
| --- | --- |
| - recebe o pagamento da GFD e repassa as parcelas aos bancos contratados. |

---

Para registrar esse empréstimo no MGE é necessário realizar o cadastro dos eventos e fórmulas correspondentes, além do lançamento do movimento, garantindo que os descontos sejam aplicados corretamente na folha de pagamento e enviados ao eSocial conforme as exigências legais.

Acesse os links a seguir, para conhecer o detalhamento de cada passo.

| [Pré-requisitos para lançamento do eConsignado](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Pr%C3%A9requisitosparalan%C3%A7amentodoeConsignado) |
| --- |
| [Cadastro de fórmulas e eventos do crédito do trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Cadastrodef%C3%B3rmulaseeventosdocr%C3%A9ditodotrabalhador) |
| [Cadastro de eventos de provisão nas férias e desconto da provisão mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Cadastrodeeventosdeprovis%C3%A3onasf%C3%A9riasedescontodaprovis%C3%A3omensal) |
| [Cadastro de eventos de provisão no adiantamento salarial](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Cadastrodeeventosdeprovis%C3%A3onoadiantamentosalarial) |
| [Lançamento crédito do trabalhador eConsignado](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Lan%C3%A7amentocr%C3%A9ditodotrabalhadoreConsignado) |
| [Cálculo da folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#C%C3%A1lculodafolha) |
| [Geração e envio dos eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Gera%C3%A7%C3%A3oeenviodoseventos) |

---

### Pré-requisitos para lançamento do eConsignado

Para lançar o eConsignado, considere as seguintes regras:

- folha **mensal** ou de **rescisão**;
- funcionários cadastrados com código de categoria:
  - 101 a 106 (empregados);
  - 111 (empregado doméstico);
  - 721 (diretor não empregado com FGTS).

**Nota:** se tentar lançar para outro tipo de folha ou funcionário, o sistema não vai permitir e exibirá uma mensagem de alerta. Além disso, o botão **Finalizar adição** estará desabilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Para)

### Cadastro de fórmulas e eventos do crédito do trabalhador

![Imagem 9: Evento Parcela Crédito Trabalhador (desconto efetivo da parcela)](https://ajuda.sankhya.com.br/hc/article_attachments/31741917492119) **Evento Parcela Crédito Trabalhador (desconto efetivo da parcela)**

Será o evento padrão e o que será enviado para o eSocial. Ele será responsável por trazer o valor exato do desconto do crédito do trabalhador considerando o limite permitido por lei (margem consignável).

- **Configuração do evento**:
  - aba Propriedades;

![Imagem 10: aba Propriedades;](https://ajuda.sankhya.com.br/hc/article_attachments/31741905171223)

![Imagem 11: Como o evento utiliza uma fórmula que calcula o desconto com base na margem consignável, é imprescindível que o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/31716812759831) Como **o evento utiliza uma fórmula que calcula o desconto com base na margem consignável, é imprescindível que o campo Unidade esteja configurado como Quantidade**. Caso contrário, a fórmula será desconsiderada.

Mesmo com a Unidade parametrizada como Quantidade, o valor do desconto deverá ser informado no campo Valor durante o lançamento do movimento.

- - aba Incidência;

![Imagem 12: aba Incidência;](https://ajuda.sankhya.com.br/hc/article_attachments/31742061446423)

- - aba Bases de Cálculo.

![Imagem 13: aba Bases de Cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/31742163672599)

- **Fórmula vinculada - 10332**.

Preencha a fórmula abaixo no campo **Fórmula**:

(MemSetVar('MargemCredAcum', IF(&EMMMM = 0, 0, MemGetVar('MargemCredAcum'))) \* 0) + IF(QUEMOVIMENTO.VLRMOV > 0, IF(MemSetVar('MargemCred', &EBBBB \* (35/100)) > 0, IF((MemGetVar('MargemCred') - MemGetVar('MargemCredAcum') < QUEMOVIMENTO.VLRMOV), MemGetVar('MargemCred') - MemGetVar('MargemCredAcum'), QUEMOVIMENTO.VLRMOV + (MemIncVar('MargemCredAcum', QUEMOVIMENTO.VLRMOV) \* 0)), 0), 0)

sendo:

**EMMMM** = Código do evento crédito do trabalhador informado no Lançamento de Movimento.
**EBBBB** = Código do evento de Base da Margem Crédito Trabalhador

![Imagem 14: Base da Margem Crédito Trabalhador](https://ajuda.sankhya.com.br/hc/article_attachments/31742570319255) **Base da Margem** **Crédito Trabalhador**

É a base de cálculo utilizada para verificar o valor que será descontado da parcela considerando a margem consignável de 35% do salário.

- **Configuração do evento**:
  - aba Propriedades;

![Imagem 15: aba Propriedades;](https://ajuda.sankhya.com.br/hc/article_attachments/34420333339671)

- - aba Proventos/Descontos.

![Imagem 16: aba Proventos/Descontos.](https://ajuda.sankhya.com.br/hc/article_attachments/31747178935959)

**Observação:** nessa base de cálculo estarão os mesmos eventos vinculados a base de INSS.

- **Fórmula vinculada**:
  - sem fórmula vinculada.

![Imagem 17: Evento demonstrativo da parcela do Crédito Trabalhador](https://ajuda.sankhya.com.br/hc/article_attachments/31742794815255) **Evento demonstrativo da parcela do Crédito Trabalhador**

É o evento responsável por retornar o valor exato da parcela do crédito do trabalhador sem considerar a margem consignável. O valor presente nesse evento é o mesmo lançado no sistema através da comunicação feita pelo governo ao empregador.

- **Configuração do evento**:
  - aba Propriedades;

![Imagem 18: aba Propriedades;](https://ajuda.sankhya.com.br/hc/article_attachments/31742794817303)

- - aba Incidência;

![Imagem 19: aba Incidência;](https://ajuda.sankhya.com.br/hc/article_attachments/31742800081431)

- - aba Bases de Cálculo.

![Imagem 20: aba Bases de Cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/31742835069335)

- **Fórmula vinculada**.

Preencha a seguinte **Fórmula**:

ABS(FBM(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'M','EMMMM','V'))

sendo:

**EMMMM** = código do evento crédito do trabalhador informado no lançamento de movimento.

![Imagem 21: Parcela não descontada do Crédito Trabalhador](https://ajuda.sankhya.com.br/hc/article_attachments/31743197011479) **Parcela não descontada do Crédito Trabalhador**

É o evento responsável por retornar o valor não descontado do trabalhador quando não há margem consignável suficiente para quitação total da parcela. Quando o evento não for listado no cálculo, significa que o trabalhador possui margem consignável para o desconto total da parcela.

- **Configuração do evento**:
  - aba Propriedades;

![Imagem 22: aba Propriedades;](https://ajuda.sankhya.com.br/hc/article_attachments/31743197014167)

- - aba Incidência;

![Imagem 23: aba Incidência;](https://ajuda.sankhya.com.br/hc/article_attachments/31743218395543)

- - aba Bases de Cálculo.

![Imagem 24: aba Bases de Cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/31743218397591)

- **Fórmula vinculada**.

Preencha a fórmula abaixo no campo **Fórmula**:

IF(MemSetVar('Credtrab', ABS(FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &REFERE, 'M', &ETTTT, 'V') + FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC,&REFERE, 'R', &ETTTT, 'V'))) > 0, IF((MemSetVar('MargemCred', &EMMMM \* (35/100)) > 0), IF(MemGetVar('MargemCred') < MemGetVar('Credtrab'), MemGetVar('Credtrab') - MemGetVar('MargemCred'), 0), 0), 0)

sendo:

**ETTTT** = Código do evento Desconto crédito do trabalhador informado no Lançamento de Movimento

**&EMMMM** = Código do evento de Base da Margem Crédito Trabalhador

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Para)

### Cadastro de eventos de provisão nas férias e desconto da provisão mensal

Conforme descrito no tópico [9 Situações Especiais](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/tutorial-credito-do-trabalhador.pdf) previstas no manual do crédito do trabalhador:

1. no caso de **desligamento** do empregado, o empregador aplica o desconto nas verbas rescisórias, observado o **limite legal de 35%** da remuneração disponível, calculada na mesma forma que nas folhas mensais.
2. nas situações em que o empregado **não tem valores de vencimento suficientes a receber naquele mês** (considerando o conceito de remuneração disponível da Portaria MTE n.º 435/2025) para cobrir o valor da parcela, será feito o **desconto parcial**, devendo o empregador informar ao trabalhador que o desconto não foi efetuado integralmente e **orientando-o a buscar a instituição financeira para a regularização da dívida**.
3. em casos de férias ou outras antecipações, como adiantamento de salário, o empregador **poderá** **provisionar** recursos para garantir saldo suficiente para efetivação do desconto da parcela do empréstimo do empregado no momento do fechamento da folha.

#### ![Imagem 25: Prov. Créd. Trabalhador férias](https://ajuda.sankhya.com.br/hc/article_attachments/31741917492119) Prov. Créd. Trabalhador férias

- aba Propriedades;

![Imagem 26: aba Propriedades;](https://ajuda.sankhya.com.br/hc/article_attachments/31743637925271)

- aba Incidências;

![Imagem 27: aba Incidências;](https://ajuda.sankhya.com.br/hc/article_attachments/32764467797783)

- aba Bases de Cálculo.

![Imagem 28: aba Bases de Cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/31743790389143)

**Descrição:** PROV. DESCONTO CRED TRAB. FERIAS

**Fórmula:** IF(MemSetVar('ProvCred', ABS(FBM(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'M','TTTT','V'))) > 0, IF(MemSetVar('MargemProv', &EXXXX \* (35/100)) > 0, IF(MemGetVar('MargemProv') < MemGetVar('ProvCred'), MemGetVar('MargemProv'), MemGetVar('ProvCred')), 0), 0)

**Índice:** 0

sendo:

**TTTT** = Código do evento crédito do trabalhador informado no lançamento de movimento

**&EXXXX** = Código do evento de **base** de crédito do trabalhador

#### ![Imagem 29: Ressarc. Cred. Trab. Férias](https://ajuda.sankhya.com.br/hc/article_attachments/31742570319255) Ressarc. Cred. Trab. Férias

- aba Propriedades;

![Imagem 30: aba Propriedades;](https://ajuda.sankhya.com.br/hc/article_attachments/31743878711703)

- aba Incidências;

![Imagem 31: aba Incidências;](https://ajuda.sankhya.com.br/hc/article_attachments/32764467798295)

- aba Bases de Cálculo.

![Imagem 32: aba Bases de Cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/31743891453591)

**Descrição:** RESSARC. CRED. PROV. FERIAS

**Fórmula:** IF(((&F**UUUU** <= 0) AND (&I**VVVV** <= 0)), 0, IF((MemSetVar('ProvCredComp', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '**QQQQ**')) / IF(MemSetVar('IndProvCredComp', IF(MemSetVar('Ind4410', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '**RRRR**, **SSSS**')) > 0, MemGetVar('Ind4410'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'F,1,2,3', '**TTTT**'))) > 0, MemGetVar('IndProvCredComp'), 1)) \* (&F**UUUU** + &I**VVVV**)) > 0), MemGetVar('ProvCredComp'), IF((MemSetVar('ProvCredProx', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '**QQQQ**')) / IF(MemSetVar('IndProvCredProx', IF(MemSetVar('Ind4410Prox', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '**RRRR**, **SSSS**')) > 0, MemGetVar('Ind4410Prox'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1), 'F,1,2,3', '**VVVV**'))) > 0, MemGetVar('IndProvCredProx'), 1)) \* (&F**UUUU** + &I**VVVV**)) > 0), MemGetVar('ProvCredProx'), IF((MemSetVar('ProvCredProx1', (ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '**QQQQ**')) / IF(MemSetVar('IndCredINSSProx1', IF(MemSetVar('Ind4410Prox1', FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '**RRRR**, **SSSS**')) > 0, MemGetVar('Ind4410Prox1'), FBIND(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-2), 'F,1,2,3', '**TTTT**'))) > 0, MemGetVar('IndCredINSSProx1'), 1)) \* (&F**UUUU** + &I**VVVV**)) > 0) AND (&MESATU = 3), MemGetVar('ProvCredProx1'), 0))))

**Índice:** 0

sendo:

**UUUU** = Código da fórmula de Dias de Férias na Referência - exemplo: &F**4432**

**VVVV** = Código do do evento de Licença remunerada na competência - exemplo: &I**4330**

**QQQQ** = Código do evento PROV. DESCONTO CRÉD TRAB. - exemplo: **44**

**RRRR** = Código do evento FÉRIAS do recibo de férias - exemplo: **4410**

**SSSS** = Código do evento de Licença remunerada do recibo de férias - exemplo: **4070**

**TTTT** = Código do evento de médias de férias do recibo de férias - exemplo: **4430**

![Imagem 33: Após a criação dos eventos e fórmulas é necessário o envio da rubrica com natureza 9253 e o código de FGTS 31 pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/31743943538711) Após a criação dos eventos e fórmulas é necessário o envio da rubrica com natureza 9253 e o código de FGTS 31 pelo evento S-1010 na Central do eSocial.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Para)

### Cadastro de eventos de provisão no adiantamento salarial

Ainda, conforme descrito no tópico [9 Situações Especiais](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/tutorial-credito-do-trabalhador.pdf), item 3, no manual do crédito do trabalhador:

Em casos de férias ou outras antecipações, **como adiantamento de salário**, o empregador **poderá** **provisionar** recursos para garantir saldo suficiente para efetivação do desconto da parcela do empréstimo do empregado no momento do fechamento da folha.

![Imagem 34: Provisão de desconto do crédito do trabalhador no adiantamento salarial](https://ajuda.sankhya.com.br/hc/article_attachments/31741917492119) **Provisão de desconto do crédito do trabalhador no adiantamento salarial**

- **Configuração do evento**:
  - aba Propriedades;

**Descrição:** PROV. DESC. CRED. TRAB. ADTO

![Imagem 35: Descrição: PROV. DESC. CRED. TRAB. ADTO](https://ajuda.sankhya.com.br/hc/article_attachments/32870013317015)

- - aba Incidência;

![Imagem 36: aba Incidência;](https://ajuda.sankhya.com.br/hc/article_attachments/32870074927767)

- - aba Bases de Cálculo.

![Imagem 37: aba Bases de Cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/32870074929431)

- **Fórmula vinculada.**

**PROV. DESC. CRED. TRAB. ADTO**

IF(MemSetVar('Credito', ABS(FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &REFERE, 'M', '10106', 'V') + FBM(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &REFERE, 'R', '10106', 'V'))) > 0, IF(MemSetVar('MargAdpPer', &E1929 \* (35/100)) > 0, IF(MemGetVar('MargAdpPer') > ((MemGetVar('Credito') \* QueFuncionario.PERCADIANTAMENTO) / 100), ((MemGetVar('Credito') \* QueFuncionario.PERCADIANTAMENTO) / 100), MemGetVar('MargAdpPer')), 0),0)

Onde:

**TTTT**  = Código do evento crédito do trabalhador informado no lançamento de movimento

**&EXXXX** = Código do evento de base de crédito do trabalhador

![Imagem 38: Ressarcimento do desconto do crédito do trabalhador no adiantamento salarial](https://ajuda.sankhya.com.br/hc/article_attachments/31742570319255) **Ressarcimento do desconto do crédito do trabalhador no adiantamento salarial**

- **Configuração do evento**:
  - aba Propriedades;

**Descrição:** RESSARC. DESC. CRED. ADTO

![Imagem 39: Descrição: RESSARC. DESC. CRED. ADTO](https://ajuda.sankhya.com.br/hc/article_attachments/32870783360791)

- - aba Incidência;

![Imagem 40: aba Incidência;](https://ajuda.sankhya.com.br/hc/article_attachments/32870783362199)

- - aba Bases de Cálculo.

![Imagem 41: aba Bases de Cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/32870805013143)

- **Fórmula vinculada.**

**RESSARC. DESC. CRED. ADTO MGE**

IF(ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'A', 'YYYY')) > 0, ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, &Refere, 'A', 'YYYY')),0)

Onde:

**YYYY** = Código do evento de provisão de desconto de crédito do trabalhador no adiantamento

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Para)

### Lançamento crédito do trabalhador eConsignado

Você pode fazer o lançamento nas telas:

- **Movimentação por Funcionário**

[GIF animado: Imagem 42: Movimentação por Funcionário](https://ajuda.sankhya.com.br/hc/article_attachments/31668403017751)

- **Movimento de Rescisão**

[GIF animado: Imagem 43: Movimento de Rescisão](https://ajuda.sankhya.com.br/hc/article_attachments/31668313602967)

Ao acessar as referidas telas, selecione a empresa, o funcionário, a referência e o evento com a rubrica **9253 - eConsignado**. Em seguida, você deve configurar os seguintes campos:

- **tipo de desconto**: preencha sempre o número **1** (que significa eConsignado);
- **código da instituição**: informe o código com 3 números (conforme tabela do Banco Central);
- Instituição financeira;
- **número do contrato**: preencha o número do contrato do empréstimo que deve ter entre 1 e 15 caracteres;
- **outras informações do desconto**: descreva qualquer detalhe sobre o empréstimo.

**Importante**

- Se o funcionário **não tiver o código de categoria permitido**, o sistema bloqueia o lançamento.
- Apenas folhas **Mensais** ou de **Rescisão** aceitam esse evento.
- **Não é possível** lançar eventos de eConsignado na movimentação **Por Evento** e nem **diretamente no cálculo da folha Mensal ou de Rescisão.**

Em todos os casos acima é exibida uma mensagem explicando o motivo do bloqueio, não sendo possível salvar o lançamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Para)

### Cálculo da folha

Após lançar o evento de empréstimo eConsignado (com rubrica= 9253 e código de incidência para o FGTS = 31) para o funcionário, efetue o cálculo da folha mensal ou de rescisão:

**(1)** mensal (Cálculos > Individuais > folha normal);

[GIF animado: Imagem 44: (1) mensal (Cálculos > Individuais > folha normal);](https://ajuda.sankhya.com.br/hc/article_attachments/31668917292311)

**(1)** rescisão (Cálculos > Individuais > rescisão).

[GIF animado: Imagem 45: (1) rescisão (Cálculos > Individuais > rescisão).](https://ajuda.sankhya.com.br/hc/article_attachments/31668965463319)

![Imagem 46: No cálculo de colaboradores que possuem mais de um desconto de Crédito do Trabalhador, a opção "Agrupar descontos" não…](https://ajuda.sankhya.com.br/hc/article_attachments/31716812759831) No cálculo de colaboradores que possuem mais de um desconto de Crédito do Trabalhador, a opção **"Agrupar descontos"** não soma os eventos com natureza de rubrica 9253 (Empréstimo eConsignado - desconto), pois cada contrato deve ser enviado ao eSocial separadamente, garantindo que as informações sejam transmitidas conforme as regras oficiais.

![Imagem 47: No cálculo de colaboradores que possuem mais de um desconto de Crédito do Trabalhador, a opção "Agrupar descontos" não…](https://ajuda.sankhya.com.br/hc/article_attachments/35698515921815)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Para)

### Geração e envio dos eventos

Depois de calcular a folha, acesse a tela **Central do eSocial**, para gerar e enviar o evento **S-1200** (Remuneração Mensal).

Em caso de rescisão, o evento correspondente ao tipo de desligamento, sendo o **S-2299** (Rescisão) ou **S-2399** (Rescisão por Término de Contrato).

Dessa forma, o desconto será informado no **grupo de Informações de Desconto de Empréstimo em Folha (descFolha)** do eSocial.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/31667959763735-Como-lan%C3%A7ar-o-cr%C3%A9dito-do-trabalhador-eConsignado-no-MGE#Para)
