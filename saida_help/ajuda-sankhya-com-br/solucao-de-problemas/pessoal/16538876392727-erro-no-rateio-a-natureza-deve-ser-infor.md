---
id: "16538876392727"
titulo: "Erro no rateio. A Natureza deve ser informada. O parâmetro 'EXIGNATCFR' está ligado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16538876392727-Erro-no-rateio-A-Natureza-deve-ser-informada-O-par%C3%A2metro-EXIGNATCFR-est%C3%A1-ligado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:17:34Z"
rotulos: ["Configuração", "Rateio", "Centro de Resultado", "Financeiro", "Natureza", "CORE_E05388", "Eventos Empresa/Departamento Funcionário", "Eventos Empresa/Departamento Funcionário com CR/Natureza ≠ 0", "EXIGCRCFR ligado exige Centro de Resultado e Natureza cadastrados"]
---

# Erro no rateio. A Natureza deve ser informada. O parâmetro 'EXIGNATCFR' está ligado

**Tipos de Rateio:

Existem 3 tipos possíveis de rateio:**

- Por eventos,
- Por Empresa/Departamento
- Por Funcionário. 

  E para cada tipo de rateio os parâmetros abaixo possui uma funcionalidade:

**Para Rateio por eventos:**

Com o parâmetro **"Exigir CR na central/financeiro/rateio? - EXIGCRCFR"** ligado é necessário garantir que todos os eventos que serão utilizados tenham Centro de Resultado e Natureza cadastrados e diferente de 0 na tela "Eventos".

**Para Rateio por Empresa/Departamento:**

**"Exigir CR na central/financeiro/rateio? - EXIGCRCFR"** caso esteja ligado é necessário garantir que a Empresa ou Departamento tenham Centro de Resultado cadastrado e diferente de zero e, que tenha a Natureza cadastrada e diferente de zero na Configuração de Integração Financeira.

**Por Rateio por Funcionário:**

**"Exigir CR na central/financeiro/rateio? - EXIGCRCFR"** caso esteja ligado é necessário garantir que o Centro de Resultado no cadastro de Rateio do funcionário seja diferente de zero e que na Configuração de Integração Financeira tenha a Natureza cadastrada diferente de zero.
