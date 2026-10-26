---
id: "39335348558359"
titulo: "Como atualizar a Tabela de IRRF 2026 no MGEPessoal?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39335348558359-Como-atualizar-a-Tabela-de-IRRF-2026-no-MGEPessoal"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:44Z"
rotulos: ["Configuração", "Atualização", "Impostos", "Folha de Pagamento", "MGEPessoal", "IRRF", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como atualizar a Tabela de IRRF 2026 no MGEPessoal?

A Lei n.º 15.270/2025, com vigência a partir de **01/01/2026**, trouxe mudanças importantes na tributação do **Imposto de Renda da Pessoa Física (IRRF)**. Essas alterações impactam diretamente o cálculo da folha de pagamento e exigem atualizações no sistema para garantir conformidade com as novas determinações legais.

A tabela de faixas de IRRF **não sofreu alteração** por parte do governo, permanecendo a mesma de 2025. No entanto, foi incluída a **tabela de faixa de isenção**, que estabelece que rendimentos até R$ 5.000,00 não terão desconto de IR, rendimentos de R$ 5.000,01 a R$ 7.350,00 terão isenção parcial, e acima disso terá desconto normal.

### Principais Impactos da Nova Legislação

As mudanças trazidas pela Lei n.º 15.270/2025 incluem:

- **Isenção de IRRF para rendimentos mensais de até R$ 5.000,00:** colaboradores dentro desse limite deixam de sofrer retenção de IRRF na folha.

- **Readequação das faixas de tributação:** para salários acima do limite de isenção, as novas alíquotas e deduções alteram o valor retido e o cálculo das bases.

- **Atualização das tabelas e eventos de IRRF no sistema:** o sistema atualizará automaticamente todos os eventos de IRRF necessários para atender às novas regras.

### Requisitos para Atualização no MGEPessoal

Para atender à nova regra de IRRF para 2026 no **"MGEPessoal"**  , é necessário atualizar o executável a **"**versão **4.66.0.32** ou superior e **criar manualmente** a tabela de faixas, os eventos de isenção e as fórmulas.

**Importante:** empresas que utilizam eventos personalizados de IRRF deverão revisar e ajustar manualmente suas configurações para garantir conformidade com a Lei n.º 15.270/2025.

### Como Funciona a Nova Faixa de Isenção

Para adequação da faixa de desconto de IRRF, o sistema considera a **base cheia sem deduções**, ou seja, não entram no cálculo dependentes, INSS, pensão alimentícia e outros descontos. Dessa forma:

- Rendimentos até **R$ 5.000,00:** não terão desconto de IR.

- Rendimentos de **R$ 5.000,01 a R$ 7.350,00:** terão isenção parcial.

- Rendimentos **acima de R$ 7.350,00:** terão desconto normal conforme tabela de IRRF.

Por exemplo, um funcionário com salário de R$ 5.026,53 já terá desconto de IRRF, pois ultrapassa o limite de isenção total.

### **(1)** Atualize o MGE Pessoal para a versão: 4.66.0.32 ou superior.

**(2)** Crie a **tabela de faixa** com o código: 7542 - ISENÇÃO DE IRRF:

![Imagem 1: (2) Crie a tabela de faixa com o código: 7542 - ISENÇÃO DE IRRF:](https://ajuda.sankhya.com.br/hc/article_attachments/41456702632343)

**(3)** Configure as **fórmulas** para isenção do IRRF:

Material de apoio com informações das fórmulas:

<https://ajuda.sankhya.com.br/hc/pt-br/articles/36943074544023-Parametriza%C3%A7%C3%A3o-de-eventos-para-c%C3%A1lculo-da-Isen%C3%A7%C3%A3o-do-IRRF-2026-MGE-Pessoal>

### Materiais de Apoio

Consulte os artigos disponíveis na Central de Ajuda para obter orientações detalhadas sobre a criação manual de tabelas, eventos e fórmulas de IRRF, caso necessário:

<https://ajuda.sankhya.com.br/hc/pt-br/articles/36943074544023-Parametriza%C3%A7%C3%A3o-de-eventos-para-c%C3%A1lculo-da-Isen%C3%A7%C3%A3o-do-IRRF-2026-MGE-Pessoal>

<https://ajuda.sankhya.com.br/hc/pt-br/articles/37092183320087-Exemplos-de-C%C3%A1lculo-do-IRRF-2026-Lei-n%C2%BA-15-270-2025>

<https://ajuda.sankhya.com.br/hc/pt-br/articles/37696119134999-Tabelas-de-Faixas-atualizadas-2026>
