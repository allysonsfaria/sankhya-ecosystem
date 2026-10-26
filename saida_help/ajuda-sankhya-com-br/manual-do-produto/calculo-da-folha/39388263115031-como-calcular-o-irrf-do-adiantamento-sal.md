---
id: "39388263115031"
titulo: "Como calcular o IRRF do adiantamento salarial (regra 2026)?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39388263115031-Como-calcular-o-IRRF-do-adiantamento-salarial-regra-2026"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Cálculo da Folha"
atualizado_em: "2026-09-27T17:41:16Z"
rotulos: ["Configuração", "Atualização", "Impostos", "Folha de Pagamento", "Sankhya", "IRRF", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como calcular o IRRF do adiantamento salarial (regra 2026)?

A partir de janeiro de 2026, com a vigência da [**Lei nº 15.270/2025**](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm), o cálculo do IRRF sobre adiantamento salarial passou por mudanças significativas. A nova legislação estabelece uma **fórmula de redução do imposto** que considera os rendimentos tributáveis do período, impactando diretamente o cálculo quando há adiantamento quinzenal.

Este artigo explica como o sistema Sankhya realiza o cálculo correto do IRRF considerando tanto a folha mensal quanto o adiantamento salarial, aplicando a nova metodologia de cálculo e a recomposição de bases quando necessário.

### Entendendo a nova regra de cálculo do IRRF

A partir do mês de janeiro do ano-calendário de 2026, será concedida redução do imposto sobre os rendimentos tributáveis sujeitos à incidência mensal do Imposto sobre a Renda das Pessoas Físicas, de acordo com a seguinte tabela:

Tabela de redução do imposto mensal.

![Imagem 1: Tabela de redução do imposto mensal.](https://ajuda.sankhya.com.br/hc/article_attachments/40837713327255)

Ou seja, para rendimentos tributáveis de até **R$ 5.000,00**, o valor é totalmente isento de Imposto de Renda.

Para rendimentos tributáveis entre **R$ 5.000,01 e R$ 7.350,00**, aplica-se uma redução calculada pela fórmula: **R$ 978,62 - (0,133145 x rendimentos tributáveis sujeitos à incidência mensal)**,.

Já para rendimentos tributáveis a partir de **R$ 7.350,01**, permanece o calculo normal conforme a tabela progressiva do Imposto de Renda.

### Cálculo do IRRF na folha de adiantamento

Quando há **adiantamento salarial**, o sistema realiza o cálculo do IRRF considerando a recomposição das bases. O processo segue os seguintes passos:

**(1)** Identifique os **rendimentos tributáveis**, que correspondem ao salário bruto menos o valor do adiantamento já pago.

**(2)** Verifique em qual faixa o valor dos rendimentos tributáveis apurados se enquadra para aplicação da nova regra.

**(3)** Após calcule a **base de cálculo do IRRF** subtraindo do salário bruto o valor do adiantamento, o INSS e os dependentes (quando aplicável).

**(4)** Aplique a alíquota correspondente da tabela progressiva sobre a base de cálculo do IR e, em seguida, deduza a parcela a deduzir correspondente.

**(5)** Subtraia o **valor da redução calculado** no passo 2 do IRRF calculado no passo 4 para obter o valor final a descontar, **se necessário**.

**Exemplo prático para rendimentos tributavéis de R$ 5.000,01 a R$ 7.350,00:**

Colaborador com salário de R$ 8.535,00 adiantamento de R$ 3.414,00.
Folha de adiantamento, pagamento 20/05.

![Imagem 2: Colaborador com salário de R$ 8.535,00 adiantamento de R$ 3.414,00. Folha de adiantamento, pagamento 20/05.](https://ajuda.sankhya.com.br/hc/article_attachments/40837777636375)

Folha mensal, pagamento 05/06.

![Imagem 3: Folha mensal, pagamento 05/06.](https://ajuda.sankhya.com.br/hc/article_attachments/40837713328279)![Imagem 4: Folha mensal, pagamento 05/06.](https://ajuda.sankhya.com.br/hc/article_attachments/40837713328791)

###

### Memoria de calculo:

Adiantamento R$ 3.414,00

Mensal : R$ 9.279,15

Rendimentos tributavéis: R$ 9.279,15 - 3.414,00 =  R$ 5.865,15

Aplicando a formula:

978,61 - (0,133145 \* 5.865,15)

978,61 - 780,91

**= R$ 197,69 valor da redução**

**Em seguida fazemos o calculo deduzindo o valor das deduções legais ou simplificado.**

R$ 5.865,15 - R$ 988,07

= R$ 4.877,08 \* 27,5% - 908,73 (INSS)

= R$432,46 - R$ 197,69

**= R$ 234,77 valor final do desconto de IR do colaborador**

**Observação:**

Dentro do LOG do evento 9040 ele demostra a recomposição de IR das bases 1904 da folha de adiantamento e da folha mensal, e demostra também o valor dos rendimentos tributavéis na função **(RendTrib),** conforme print abaixo:

![Imagem 5: Dentro do LOG do evento 9040 ele demostra a recomposição de IR das bases 1904 da folha de adiantamento e da folha…](https://ajuda.sankhya.com.br/hc/article_attachments/40837777637399)

###

### Configurações que impactam o cálculo

Algumas configurações no sistema podem impactar diretamente o cálculo do IRRF sobre adiantamento:

**Regime da empresa (Caixa ou Competência):** Esta configuração interfere diretamente na **recomposição do IRRF** quando há adiantamento. Verifique se o regime está configurado corretamente na tela de cadastro da empresa (Configurações » Cadastros » Pessoal » Empresas).
 ![Imagem 6: Regime da empresa (Caixa ou Competência): Esta configuração interfere diretamente na recomposição do IRRF quando há…](https://ajuda.sankhya.com.br/hc/article_attachments/40880029743127)

**Evento de dependentes (999):** Na aba "**Padrão**" ou **"Personalizado"** do cadastro do evento (Pessoal+ » Cadastros » Eventos), certifique-se de que a opção **"Regra de cálculo em folha de adiantamento"** esteja **desmarcada**. Quando marcada indevidamente, o sistema considera o desconto de dependentes tanto na folha mensal quanto no adiantamento, causando duplicidade.

![Imagem 7: Evento de dependentes (999): Na aba " Padrão " ou "Personalizado" do cadastro do evento (Pessoal+ » Cadastros »…](https://ajuda.sankhya.com.br/hc/article_attachments/40880015897367)

**Evento de adiantamento:** Utilize sempre o **evento padrão do sistema (evento 650)** para adiantamento salarial. Eventos personalizados podem não aplicar corretamente a nova regra de cálculo do IRRF.

### Recomposição de bases em múltiplas folhas

Quando o colaborador possui **mais de uma folha no mesmo mês** (por exemplo, folha mensal e rescisão), o sistema realiza automaticamente a **recomposição das bases tributáveis** para aplicar corretamente a nova regra do IRRF.

Neste cenário, o sistema:

- Soma todos os rendimentos tributáveis do período, considerando a data de pagamento (folha mensal, rescisão e/ou adiantamento).
- Soma todas as deduções legais aplicáveis, como INSS e dependentes.
- Aplica, quando cabível, a fórmula de redução sobre o total dos rendimentos tributáveis.
- Calcula o IRRF total do período e deduz os valores de IRRF já retidos em pagamentos anteriores realizados no mesmo mês (sempre considerando data de pagamento).

**Observação:** caso tenha sido utilizada o desconto simplificado, o respectivo valor será considerado apenas uma única vez na apuração do calculo.

Para que a recomposição funcione corretamente, é fundamental que o sistema esteja atualizado com a **versão Módulo Pessoal 5.75.1 ou superior**.

### Materiais de referência oficial

Para aprofundar o conhecimento sobre a nova legislação, consulte os materiais oficiais da Receita Federal:

- [Tabelas IRRF 2026:](https://www.gov.br/secom/pt-br/acompanhe-a-secom/noticias/2026/01/nova-tabela-do-ir-veja-faixas-e-aliquotas-e-saiba-mais-sobre-medida-que-isenta-o-pagamento-para-quem-ganha-ate-r-5-mil) Acesse a documentação oficial com as novas faixas e alíquotas.
- [Exemplos de aplicação da Lei nº 15.270/2025](https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas?utm_source=chatgpt.com): Consulte casos práticos disponibilizados pela Receita Federal.
- Artigos Sankhya: "[Exemplos de Cálculo do IRRF 2026 – Lei nº 15.270/2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/37092183320087-Exemplos-de-C%C3%A1lculo-do-IRRF-2026-Lei-n%C2%BA-15-270-2025)" e "[Imposto de renda 2026: entenda os impactos no Cálculo da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/36918778442391-Imposto-de-renda-2026-entenda-os-impactos-no-C%C3%A1lculo-da-Folha-de-Pagamento)".
- [Simulador de alíquota efetiva IRPF](https://www27.receita.fazenda.gov.br/simulador-irpf/)

Caso persista alguma divergência após verificar todas as configurações mencionadas, certifique-se de que o sistema está atualizado e recalcule a folha de pagamento para aplicar corretamente as novas regras.

Caso o evento de IR esteja configurado como **personalizado**, verifique se as fórmulas vinculadas aos eventos de IR são as fórmulas padrão do sistema ou se são formulas personalizadas.

Se estiver utilizando fórmulas personalizadas, consulte a fórmula padrão correspondente na rotina **Fórmulas** (Pessoal+ » Cadastros » Fórmulas) e vincule o código da fórmula padrão ao cadastro do evento.

![Imagem 8: Se estiver utilizando fórmulas personalizadas, consulte a fórmula padrão correspondente na rotina Fórmulas ( Pessoal+ »…](https://ajuda.sankhya.com.br/hc/article_attachments/40880015898903)![Imagem 9: Se estiver utilizando fórmulas personalizadas, consulte a fórmula padrão correspondente na rotina Fórmulas ( Pessoal+ »…](https://ajuda.sankhya.com.br/hc/article_attachments/40880029744791)

Por outro lado, se o evento de IR for um **evento padrão do sistema**, a configuração já estará correta e não será necessário realizar ajustes.
