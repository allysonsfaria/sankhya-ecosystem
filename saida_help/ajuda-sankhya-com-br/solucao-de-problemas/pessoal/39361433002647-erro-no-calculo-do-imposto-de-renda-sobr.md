---
id: "39361433002647"
titulo: "Erro no cálculo do imposto de renda sobre férias - desconto de ir para salários abaixo de R$ 5.000,00"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39361433002647-Erro-no-c%C3%A1lculo-do-imposto-de-renda-sobre-f%C3%A9rias-desconto-de-ir-para-sal%C3%A1rios-abaixo-de-R-5-000-00"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:02Z"
rotulos: ["Configuração", "Atualização", "Impostos", "Folha", "Férias", "IRRF", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no cálculo do imposto de renda sobre férias - desconto de ir para salários abaixo de R$ 5.000,00

**Mensagem**

O sistema está descontando Imposto de Renda Retido na Fonte (IRRF) no cálculo de férias para funcionários com base de cálculo inferior a R$ 5.000,00 na folha de janeiro de 2026, mesmo com a nova legislação que garante isenção para esta faixa salarial.

**Situação**

Ao processar o **"Cálculo de Férias"** (Pessoal+ » Rotinas Folha » Cálculos) para a referência 01/2026, o sistema está aplicando desconto de IRRF para colaboradores que possuem remuneração tributável inferior a R$ 5.000,00, não respeitando a nova regra de isenção estabelecida pela Lei nº 15.270/2025, que entrou em vigor em janeiro de 2026.

**Solução**

Para corrigir o cálculo do IRRF sobre férias, siga os passos abaixo:

**(1)** Verifique se a **"Tabela de Isenção IRRF 2026" (**Pessoal+ » Cadastros » Tabela de Faixas)  está devidamente cadastrada na competência do cálculo. Esta tabela é essencial para aplicação das novas regras de cálculo.

![Imagem 1: (1) Verifique se a "Tabela de Isenção IRRF 2026" ( Pessoal+ » Cadastros » Tabela de Faixas) está devidamente cadastrada…](https://ajuda.sankhya.com.br/hc/article_attachments/41274164746135)

**(2)** Caso a tabela não esteja presente, realize a atualização da tabela de isenção através do botão demonstrado abaixo:

![Imagem 2: (2) Caso a tabela não esteja presente, realize a atualização da tabela de isenção através do botão demonstrado abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/41274164749719)

**(3)** Confirme que a **"Data de Pagamento"** está programada para 01/01/2026 ou posterior. O IRRF é validado pela data de pagamento, portanto, pagamentos programados para 31/12/2025 ou datas anteriores não aplicarão a nova regra de isenção.

**(4)** Se necessário, ajuste a data de pagamento das férias para uma data válida em 2026 (a partir de 01/01/2026).

**(5)** Realize o recálculo da folha de férias após confirmar que a tabela de isenção está alimentada corretamente na referência do cálculo de férias e a data de pagamento está correta.

**(6)** Valide que o sistema não está mais gerando desconto de IRRF para colaboradores com base de cálculo inferior a R$ 5.000,00, conforme determina a nova legislação.

**Causa**

O erro ocorre por dois motivos principais:

1. Ausência ou informações inconsistentes referente a valores na tabela de isenção: A **"Tabela de Isenção IRRF 2026**, impedindo a aplicação das novas regras estabelecidas pela Lei nº 15.270/2025.
2. Data de pagamento anterior a 2026: O cálculo de IRRF é validado pela **"Data de Pagamento"** programada. Quando as férias estão programadas para pagamento em 31/12/2025 ou datas anteriores, o sistema aplica as regras de IRRF vigentes em 2025, não considerando a nova legislação que entra em vigor apenas para pagamentos a partir de 01/01/2026.
A nova tabela de IRRF em vigor desde janeiro de 2026 garante isenção total para rendas mensais até R$ 5.000,00. A partir de R$ 5.000,01, o imposto passa a ser calculado de forma progressiva com reduções graduais até R$ 7.350,00, conforme estabelecido pela Lei nº 15.270/2025.
