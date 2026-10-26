---
id: "360048834473"
titulo: "Pagamento do 1/3 de férias suspenso - MP927. Saiba Mais!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360048834473-Pagamento-do-1-3-de-f%C3%A9rias-suspenso-MP927-Saiba-Mais"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:34:56Z"
rotulos: ["Configuração", "Eventos", "Folha", "INSS", "Férias", "Pagamento de 1/3 de Férias Suspenso - MP927", "IRRF", "MP927"]
---

# Pagamento do 1/3 de férias suspenso - MP927. Saiba Mais!

**![Imagem 1: Posicionamento Jurídico:](https://ajuda.sankhya.com.br/hc/article_attachments/19150000315927) Posicionamento Jurídico:**

**1.1 INSS**

A verba de ⅓ de férias normais será incluída na base de cálculo do INSS da folha mensal da referência do pagamento juntamente com as outras verbas que compõem a base. Por ausência de previsão legal expressa, utilizamos a regra do fato gerador que determina que o tributo só é devido a partir do pagamento da verba.

**1.2 IRRF**

A base de cálculo e retenção do IRRF para a verba de ⅓ de férias normais ocorrerá na folha mensal da referência do pagamento, porém a incidência do IRRF se dará em separado dos demais rendimentos pagos ao empregado que não se refiram a férias. Por ausência também de previsão legal expressa utilizamos como analogia o art. 29, §1º, da Instrução Normativa RFB nº1500 /2014.

**![Imagem 2: Pré Requisito para pagamento do terço Constitucional de férias prorrogado:](https://ajuda.sankhya.com.br/hc/article_attachments/19150000327703) Pré Requisito para pagamento do terço Constitucional de férias prorrogado:**

Parametrizar o sistema e cadastrar os eventos e fórmulas, conforme detalhado abaixo:

**![Imagem 3: Cadastro do Evento e fórmula de quitação ⅓ de férias normais:](https://ajuda.sankhya.com.br/hc/article_attachments/19150000336791) Cadastro do Evento e fórmula de quitação  ⅓ de férias normais:**

**3.1. EVENTO**

Aba Propriedades:

![Imagem 4: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360072088133)

Aba Incidência:

![Imagem 5: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360070939594)

Aba Bases de Cálculo:

![Imagem 6: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360070939654)

**3.2 FÓRMULA**

- Fórmula quitação ⅓ de férias:

ABS(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC,&Refere,'FA','4502,4514,4520,4550'))

Eventos:

- 4602-QUITACAO 1/3 FERIAS MP927
- 4502- SUSPENSÃO 1/3 FÉRIAS MP927
- 4520- SUSPENSÃO ⅓ FÉRIAS MP927 (PROCESSO NOVO DE FÉRIAS)
- 4514- SUSP 1/3 ADIANT FERIAS MP927
- 4550- SUSP 1/3 FERIAS MES COMP MP927

**![Imagem 7: Cadastro do evento e fórmula de quitação do ⅓ abono de férias:](https://ajuda.sankhya.com.br/hc/article_attachments/19149974426391) Cadastro do evento e fórmula de quitação do ⅓ abono de férias:**

**4.1. EVENTO**

**Aba Propriedades:**

![Imagem 8: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360072089353)

**Aba Incidência:**

![Imagem 9: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360070940774)

Aba Bases de Cálculo:

![Imagem 10: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360070940874)

**4.2. FÓRMULA:**

IF(FSomAcu(queFuncionario.CODEMP, queFuncionario.CODFUNC, &ANOATU, 0,'4603', 'V')<>0,0,IF(FSomAcu(queFuncionario.CODEMP, queFuncionario.CODFUNC, &ANOATU, 0,'4504,4540', 'V')<>0,FSomAcu(queFuncionario.CODEMP, queFuncionario.CODFUNC, &ANOATU, 0,'4504,4540', 'V')\*(-1),0))

Eventos:

4603-QUITACAO 1/3 ABONO FER MP927

4504- SUSPENSAO 1/3 ABONO  MP927

**![Imagem 11: Cadastro da Base de Cálculo IRRF Férias MP927:](https://ajuda.sankhya.com.br/hc/article_attachments/19150000347287) Cadastro da Base de Cálculo IRRF Férias MP927:**

**5.1 CADASTRO DA BASE DE CÁLCULO**

Aba Propriedades:

![Imagem 12: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360070941014)

Aba Proventos/Desconto:

![Imagem 13: Aba Proventos/Desconto:](https://ajuda.sankhya.com.br/hc/article_attachments/360072089973)

**![Imagem 14: Cadastro do evento e fórmula INSS Demonstrativo de férias:](https://ajuda.sankhya.com.br/hc/article_attachments/19150000348567) Cadastro do evento e fórmula INSS Demonstrativo de férias:**

**6.1. EVENTO**

Aba Propriedade:

![Imagem 15: Aba Propriedade:](https://ajuda.sankhya.com.br/hc/article_attachments/360072090213)

Aba Incidência:

![Imagem 16: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360072090273)

Aba Bases de Cálculo:

![Imagem 17: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360072090373)

**6.2 FÓRMULA**

XXX Evento Demonstrativo:

IF(QueFuncionario.VINCULO = 2,0,IF(&DIASTRA >= 0,IF(&INSSMESAMES = 'S',&INSSCPLN, IF(&E4602 > FTF(1,3,&E4602 ,&Refere,QueFuncionario.TIPTAB), FTF(1,4,&E4602,&Refere,QueFuncionario.TIPTAB),(((&E4602 \* FTF(1,1,&F5008 ,&Refere,QueFuncionario.TIPTAB)) / 100)))),0))

**Observação 1:** O evento &E4602 corresponde ao evento de quitação de ⅓ de férias, se na base do cliente estiver com o código diferente o mesmo deve ser alterado na fórmula acima.

**Observação 2:** Esse evento não compõe eSocial e precisa ser colocado na Base de Cálculo do IRRF de Férias, conforme print abaixo:

![Imagem 18: Observação 2: Esse evento não compõe eSocial e precisa ser colocado na Base de Cálculo do IRRF de Férias, conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/360070941774)

**![Imagem 19: Cadastro do evento e fórmula IRRF Férias MP927:](https://ajuda.sankhya.com.br/hc/article_attachments/19150000355095) Cadastro do evento e fórmula IRRF Férias MP927:**

**7.1. EVENTO**

Aba Propriedades:

![Imagem 20: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360072090693)

Aba Incidência:

![Imagem 21: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360070942614)

Aba Bases de Cálculo:

![Imagem 22: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360070942694)

**7.2 FÓRMULA IRRF FÉRIAS MP 927**

IF(&E1936>0,(((&E1936\*FTF(2,1,&E1936,&REFEREPAGTO,queFuncionario.TIPTAB)) /100)- FTF(2,2,&E1936,&REFEREPAGTO,queFuncionario.TIPTAB)),0)

**IMPORTANTE !!!**

Os itens a seguir serão de escolha do usuário para lançamento do evento. A rotina 'Movimento por Funcionário' é indicado para lançamentos de eventos para poucos funcionários. Já a rotina de 'Lançamento por Evento' é indicado quando serão muitos funcionários a ter na referência a verba paga. Saliento que, **o lançamento deve ser feito apenas por uma rotina**:

**![Imagem 23: Lançamento do evento pela rotina 'Movimento por Funcionário:](https://ajuda.sankhya.com.br/hc/article_attachments/19150000368023) Lançamento do evento pela rotina 'Movimento por Funcionário:**

![Imagem 24: Lançamento do evento pela rotina 'Movimento por Funcionário:](https://ajuda.sankhya.com.br/hc/article_attachments/360073487454)

- **Evento e descrição do evento:** buscar o código do evento de quitação cadastrado no sistema;
- **Referência:** a referência que deseja quitar a verba de ⅓ de férias normais e/ou ⅓ abono de férias
- **Valor:** deixar em branco, a fórmula do evento de quitação em ambos os casos retornará no cálculo da folha mensal o valor do evento.
- **Índice: colocar índice 1**

**![Imagem 25: Lançamento do Evento pela rotina 'Lançamento por Evento':](https://ajuda.sankhya.com.br/hc/article_attachments/19149974467351)Lançamento do Evento pela rotina 'Lançamento por Evento':**

![Imagem 26: Lançamento do Evento pela rotina 'Lançamento por Evento':](https://ajuda.sankhya.com.br/hc/article_attachments/19150000377879)

- **Evento e descrição do evento:** buscar o código do evento de quitação cadastrado no sistema;
- **Referência:** a referência que deseja quitar a verba de ⅓ de férias normais e/ou ⅓ abono de férias
- **Valor:** deixar em branco, a fórmula do evento de quitação em ambos os casos retornará no cálculo da folha mensal o valor do evento.
- **Índice:** colocar índice 1
- **Botão aplicar**: listará todos os funcionários que terão as verbas de ⅓ de férias normais e ⅓ de abono de férias lançados na folha mensal e calculadas, caso tais verbas tenham sido suspensas no cálculo de férias em referência anterior.
