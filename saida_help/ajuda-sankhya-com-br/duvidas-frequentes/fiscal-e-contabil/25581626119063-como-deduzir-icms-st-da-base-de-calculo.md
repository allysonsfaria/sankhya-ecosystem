---
id: "25581626119063"
titulo: "Como deduzir ICMS/ST da Base de Cálculo do PIS/COFINS?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25581626119063-Como-deduzir-ICMS-ST-da-Base-de-C%C3%A1lculo-do-PIS-COFINS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:45:17Z"
rotulos: ["CT-e", "Configuração", "Fiscal", "NF-e", "Impostos", "TOP", "ICMS ST", "Deduzir", "PIS/COFINS", "ICMS/ST"]
---

# Como deduzir ICMS/ST da Base de Cálculo do PIS/COFINS?

**![Imagem 1: Configurações para deduzir ICMS/ST da Base de Cálculo do PIS/COFINS:](https://ajuda.sankhya.com.br/hc/article_attachments/25581640381847) Configurações para deduzir ICMS/ST da Base de Cálculo do PIS/COFINS:**

Para deduzir ICMS/ST da Base de Cálculo do PIS/COFINS, temos o parâmetro **REDSTBCPISCOF** - Redução do ICMS/ST da BC do PIS e COFINS que, quando ligado, habilita o campo '**Deduzir valor do ICMS/ST na BC do PIS e COFINS?**' (rotina: Empresa, aba: Propriedades):

![Imagem 2: Para deduzir ICMS/ST da Base de Cálculo do PIS/COFINS, temos o parâmetro REDSTBCPISCOF - Redução do ICMS/ST da BC do…](https://ajuda.sankhya.com.br/hc/article_attachments/25581626108695)

Neste campo temos as seguintes opções:

- **Não Deduz:** O valor do ICMS/ST da base de cálculo do PIS/COFINS não será deduzido.

- **Deduz para CT-e:** Ao lançar um CT-e, o valor do ICMS/ST será deduzido da base de cálculo do PIS e COFINS se as alíquotas de PIS e COFINS possuírem um percentual de redução de base. Primeiramente será retirado o valor do ICMS/ST da base, para depois ser aplicado o percentual de redução.

- **Deduz para CT-e e NF-e:** O valor do ICMS/ST da base de cálculo do PIS/COFINS será deduzido tanto para NF-e quanto para CT-e.

- **Deduz para NF-e:** Deduz o valor do ICMS/ST da base de cálculo do PIS/COFINS apenas para NF-e.

- **Configurado pela TOP:** essa opção verificará no cadastro da TOP a aba Impostos se a marcação **"Deduzir valor do ICMS/ST na BC do PIS e COFINS?"** encontra-se marcada:

![Imagem 3: Configurado pela TOP: essa opção verificará no cadastro da TOP a aba Impostos se a marcação "Deduzir valor do ICMS/ST…](https://ajuda.sankhya.com.br/hc/article_attachments/25581626112663)

Caso os campos acima estejam configurados, ao efetuar o lançamento de uma nota, o valor referente ao cálculo de ICMS/ST será subtraído da Base de Cálculo de PIS/COFINS.
