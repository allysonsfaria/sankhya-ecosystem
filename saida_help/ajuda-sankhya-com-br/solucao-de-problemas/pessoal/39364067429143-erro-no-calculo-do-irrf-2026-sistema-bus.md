---
id: "39364067429143"
titulo: "Erro no Cálculo do IRRF 2026 - Sistema Busca Valores de Dezembro/2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39364067429143-Erro-no-C%C3%A1lculo-do-IRRF-2026-Sistema-Busca-Valores-de-Dezembro-2025"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:06Z"
rotulos: ["Configuração", "Atualização", "Impostos", "Pessoal", "Folha de Pagamento", "IRRF", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no Cálculo do IRRF 2026 - Sistema Busca Valores de Dezembro/2025

**MENSAGEM**

O sistema aplica incorretamente a tabela de IRRF ao realizar cálculos para a competência de janeiro de 2026, utilizando os valores da tabela de dezembro de 2025, o que resulta em valores de imposto divergentes.

**SITUAÇÃO**

Ao processar a **"Folha de pagamento mensal"**, **"Férias"** ou **"Dissídios"** com competência ou pagamento em janeiro de 2026, o sistema não aplica a nova tabela de IRRF vigente para 2026, conforme estabelecido pela Lei nº 15.270/2025. O cálculo apresenta descontos de IRRF para salários abaixo de R$ 5.000,00 ou valores distintos do esperado, o que indica que a nova regra de isenção não está sendo aplicada.

**SOLUÇÃO**

Para corrigir o problema, siga os passos abaixo:

**(1)** Verifique se o **"Módulo Pessoal"** está atualizado para a versão 5.72.4 ou superior. A nova regra de cálculo do IRRF 2026 está disponível somente a partir desta versão. Caso necessário, atualize o módulo.

**É de suma importância que o sistema seja atualizado para as versões mais recentes do módulo Pessoal+/W visando contemplar todas as melhorias já processadas em versão. Para acompanhar as mais recentes, veja o link:**

<https://downloads.sankhya.com.br/consulta-versao?c=1>

**(2)** Acesse a tela **"Tabela de Faixas"** (Pessoal+ » Cadastros » Tabela de Faixas) e localize a tabela **"7542 - Isenção IRRF"**, referente à isenção de IRRF.

![Imagem 1: Verifique se os valores da "7542" estão cadastrados para a referência 01/2026 e meses subsequentes. Caso não estejam,…](https://ajuda.sankhya.com.br/hc/article_attachments/41262610905623)

**(3)** Verifique se os valores da **"7542"** estão cadastrados para a referência 01/2026 e meses subsequentes. Caso não estejam, duplique os dados da referência 01/2026 para os demais meses de 2026.

No link abaixo foram informadas as tabelas atualizadas referentes a 2026.

<https://ajuda.sankhya.com.br/hc/pt-br/articles/37696119134999-Tabelas-de-Faixas-atualizadas-2026>

Para duplicar:

1º Acesse a competência 01/2026

![Imagem 2: 1º Acesse a competência 01/2026](https://ajuda.sankhya.com.br/hc/article_attachments/41262610906903)

2º Será apresentado o card para preenchimento cuja as referências deseja que sejam duplicadas, informe de acordo com o desejado e salve por meio do botão 'duplicar valores':

![Imagem 3: 2º Será apresentado o card para preenchimento cuja as referências deseja que sejam duplicadas, informe de acordo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/41262634113047)

**(4)** Confirme que o evento **"9040 - IRRF"** está ativo e corretamente parametrizado. Caso existam eventos duplicados, desative-os para evitar conflitos no cálculo.

**(5)** Para cálculos de **"Férias"**, verifique a data de pagamento programada. **O IRRF é validado por data de pagamento;** portanto, pagamentos programados para 31/12/2025 não aplicarão a nova regra. Altere a data de pagamento para 01/01/2026 ou posterior.

**(6)** Após realizar os ajustes necessários, execute o recálculo da folha para a competência desejada e valide se o IRRF está sendo calculado corretamente, aplicando a isenção para rendimentos até R$ 5.000,00.

**CAUSA**

O problema ocorre devido a uma ou mais das seguintes causas:

- O **"Módulo Pessoal"** está em versão anterior à 5.72.4, que não possui a implementação da nova regra de IRRF 2026.
- A tabela **"7542"** de isenção de IRRF não possui valores cadastrados para as competências de 2026.
- Existem eventos duplicados ou eventos personalizados conflitando com os eventos padrão do sistema.
- A data de pagamento está programada para 2025, o que impede a aplicação da nova legislação.
- A fórmula de recomposição de IRRF está incorreta ou desatualizada.
