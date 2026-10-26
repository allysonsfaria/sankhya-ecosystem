---
id: "36023043808663"
titulo: "GRRF - Guia de Recolhimento Rescisório do FGTS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36023043808663-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-do-FGTS"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-08-18T19:55:04Z"
rotulos: ["Configuração", "Guia", "Impostos", "eSocial", "GRRF", "Rescisão", "FGTS", "Rescisório", "bases", "complementares", "GFIP", "20%", "Recolhimento", "multa", "40%"]
---

# GRRF - Guia de Recolhimento Rescisório do FGTS

#### GRRF (Guia de Recolhimento Rescisório do FGTS)

A GRRF é o documento utilizado para efetuar o recolhimento do FGTS referente ao mês da rescisão e da multa rescisória de 40% (ou 20%) sobre o saldo do FGTS, quando aplicável.

Instituída para centralizar e automatizar o recolhimento do FGTS devido na rescisão contratual, a GRRF garante que os valores sejam devidamente depositados antes de o trabalhador realizar o saque junto à Caixa Econômica Federal.

Além disso, a GRRF formaliza o recolhimento do FGTS incidente sobre as verbas rescisórias, assegurando que o empregado desligado tenha acesso correto e regular aos valores a que tem direito.

#### Diferenças entre GRRF, GFIP e FGTS Mensal

**(1)** **GFIP (Guia de Recolhimento do FGTS e Informações à Previdência Social):**

Utilizada para o recolhimento mensal do FGTS e o envio de informações à Previdência Social;

Era o principal meio de comunicação entre as empresas e os órgãos governamentais antes do eSocial e DCTFWeb, que estão substituindo progressivamente sua utilização;

Continua sendo necessária em situações específicas não abrangidas pelo eSocial.

**(1)** **FGTS Mensal:**

Corresponde ao depósito de 8% sobre a remuneração mensal de cada empregado;

O recolhimento deve ser feito até o dia 20 do mês seguinte ao da competência;

Garante o acúmulo do saldo do FGTS durante o vínculo empregatício.

**(1)** **GRRF (Guia de Recolhimento Rescisório do FGTS):**

Utilizada exclusivamente no momento da rescisão contratual;

Recolhe o FGTS referente ao mês da rescisão e a multa rescisória de 40% (ou 20%), quando aplicável;

Deve ser transmitida até o 10º dia contado a partir da data de desligamento do empregado.

#### Situações em que a GRRF Deve Ser Gerada

A GRRF (Guia de Recolhimento Rescisório do FGTS) deve ser gerada sempre que ocorrer uma movimentação rescisória que gere direito ao saque do FGTS.

**(1)** **Com multa rescisória (40% ou 20%):**

- A guia deve ser emitida nas seguintes situações:
- Dispensa sem justa causa, multa de 40% sobre o saldo do FGTS;
- Rescisão antecipada de contrato por prazo determinado, multa de 40%;
- Extinção do contrato por acordo entre as partes, multa de 20%.

**(1)** **Sem multa rescisória:**

- Mesmo sem a incidência de multa, a GRRF ainda deve ser gerada quando há rescisão nas situações abaixo:
- Término normal do contrato por prazo determinado;
- Pedido de demissão;
- Dispensa por justa causa.

**(1)** **Casos em que a GRRF não deve ser gerada:**

- Quando não há vínculo de FGTS, como nos casos de estagiários, autônomos ou diretores não optantes;
- Para rescisões processadas pelo FGTS Digital, quando o empregador já utiliza o novo modelo de recolhimento.

#### Configuração de Bases

A correta parametrização dos eventos e bases de cálculo é essencial para a geração correta da GRRF e demais relatórios. Qualquer configuração incorreta pode gerar divergências nos valores e informações transmitidas.
Por isso, é importante validar e ajustar as bases sempre que forem realizadas conferências ou alterações nos eventos. A seguir, estão listadas as bases disponíveis para configuração no sistema:

![Imagem 1: A correta parametrização dos eventos e bases de cálculo é essencial para a geração correta da GRRF e demais relatórios.…](https://ajuda.sankhya.com.br/hc/article_attachments/36023043797271)

#### Mapeamento de Bases com os Campos da GRRF

![Imagem 2: Mapeamento de Bases com os Campos da GRRF](https://ajuda.sankhya.com.br/hc/article_attachments/36023043797911)

#### Bases Relacionadas ao FGTS Mensal e Demais Verbas

![Imagem 3: Bases Relacionadas ao FGTS Mensal e Demais Verbas](https://ajuda.sankhya.com.br/hc/article_attachments/36023043805719)

#### Observações Importantes

- As bases complementares (1825, 1826 e 1827) devem ser utilizadas conforme as regras específicas do cálculo da GRRF, variando conforme o tipo de desligamento e as verbas rescisórias envolvidas;
- A identificação correta das bases é fundamental para assegurar a consistência dos valores enviados à Caixa Econômica Federal.
