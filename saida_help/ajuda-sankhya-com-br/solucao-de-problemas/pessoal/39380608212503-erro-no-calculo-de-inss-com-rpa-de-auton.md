---
id: "39380608212503"
titulo: "Erro no cálculo de INSS com RPA de autônomo - Desconto indevido sobre teto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39380608212503-Erro-no-c%C3%A1lculo-de-INSS-com-RPA-de-aut%C3%B4nomo-Desconto-indevido-sobre-teto"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:25Z"
rotulos: ["Ocorrências", "Impostos", "Folha", "INSS", "Configuração Funcionários", "Artigo criado KCS", "Sankhya RH - KCS", "RPA"]
---

# Erro no cálculo de INSS com RPA de autônomo - Desconto indevido sobre teto

**MENSAGEM**

O sistema não está apurando corretamente o valor do INSS do RPA de autônomo, gerando divergência no desconto.

**SITUAÇÃO**

Ao realizar o cálculo de RPA para um autônomo prestador de serviços, o sistema apresenta inconsistências no cálculo do INSS quando existem múltiplos RPAs para o mesmo profissional dentro da mesma competência.

Nesses casos, o sistema acumula os valores dos RPAs na base de cálculo do INSS. Como exemplo, ao emitir um RPA de R$ 168,54 e posteriormente outro de R$ 134,82, o log de cálculo demonstra uma base de INSS de R$ 303,36 (soma dos dois recibos). Entretanto, na folha mensal é apresentada apenas a base de R$ 134,82, ocasionando divergências e, consequentemente, cálculo incorreto do desconto de INSS.

Além disso, foram identificados cenários em que o sistema não realiza o cálculo do INSS ao atingir ou ultrapassar o teto previdenciário, bem como situações em que o limite de retenção não é considerado corretamente durante o processamento.

**SOLUÇÃO**

A solução varia conforme a causa identificada. Siga as orientações abaixo:

**Para inconsistência por uso de eventos diferentes:**

**(1)** Acesse a tela **"Cálculos"** (Pessoal+ » Rotinas Folha » Cálculos) e verifique qual evento está sendo utilizado para o desconto de INSS de serviços nas folhas já calculadas (evento **"348",** evento **"9100" ou algum outro que seja utilizado para o desconto**).

**(2)** Identifique se houve alternância entre os eventos de desconto ao longo dos cálculos realizados.

**(3)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e inative o evento que não foi utilizado na maioria dos cálculos, garantindo a padronização dos próximos processamentos. Para corrigir a base de cálculo, será necessário recalcular as folhas que foram processadas com o evento que foi inativado.

**(4)** A partir da referência seguinte, utilize somente o evento um evento seja o **348, 9100** ou algum outro cadastrado na sua base, para evitar inconsistências futuras.

**Para erro na tabela de faixas de salário mínimo:**

**(1)** Acesse a tela **"Tabela de Faixas"** (Pessoal+ » Cadastros » Tabela de Faixas) e verifique se os valores de salário mínimo e teto do INSS estão corretos e atualizados conforme a legislação vigente.

![Imagem 1: (1) Acesse a tela "Tabela de Faixas" (Pessoal+ » Cadastros » Tabela de Faixas) e verifique se os valores de salário…](https://ajuda.sankhya.com.br/hc/article_attachments/41099617497367)

**(2)** Corrija os valores incorretos na tabela de faixas, incluindo todas as faixas necessárias, especialmente a última linha que representa o teto.

**(3)** Realize o recálculo da folha de pagamento para que o sistema aplique os valores corretos.

**Para INSS não calculado:**

**(1)** Acesse a tela **"Configuração Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários) e localize o funcionário autônomo.

**(2)** Verifique se o campo **"Código de Ocorrência FGTS"** está preenchido. A fórmula de cálculo valida este código para processar o INSS. E verifique se o Tipo de Tabela de INSS/IRRF/SAL.FAM esta preenchido como "A".

![Imagem 2: (2) Verifique se o campo "Código de Ocorrência FGTS" está preenchido. A fórmula de cálculo valida este código para…](https://ajuda.sankhya.com.br/hc/article_attachments/41099667431959)

**(3)** Vincule a ocorrência **"13"** ao funcionário e realize o recálculo do RPA.

![Imagem 3: (3) Vincule a ocorrência "13" ao funcionário e realize o recálculo do RPA.](https://ajuda.sankhya.com.br/hc/article_attachments/41099667432343)

**CAUSA**

As principais causas identificadas para este erro são:

**1. Alternância de eventos de desconto:** Quando o desconto de INSS é realizado por eventos diferentes ao longo das folhas (evento **"9100"** nas primeiras folhas e evento **"348"** nas folhas subsequentes), o sistema não consegue identificar corretamente os valores já descontados anteriormente, impedindo a recomposição correta do INSS.

**2. Tabela de faixas incorreta:** Valores incorretos ou ausentes na tabela de faixas de salário mínimo e teto do INSS impedem o cálculo correto, especialmente quando o valor atinge ou supera o teto estabelecido pela legislação.

**3. Ausência de código de ocorrência FGTS:** A fórmula de cálculo do sistema valida o código de ocorrência FGTS para processar o INSS. Quando este campo não está preenchido no cadastro do funcionário, o desconto não é calculado.
