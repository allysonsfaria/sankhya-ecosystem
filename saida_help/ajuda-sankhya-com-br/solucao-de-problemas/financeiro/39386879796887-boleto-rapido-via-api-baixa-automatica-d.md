---
id: "39386879796887"
titulo: "Boleto Rápido via API: Baixa automática de títulos não realizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39386879796887-Boleto-R%C3%A1pido-via-API-Baixa-autom%C3%A1tica-de-t%C3%ADtulos-n%C3%A3o-realizada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-24T15:36:40Z"
rotulos: ["Configuração", "Movimentação Financeira", "Atualização", "Financeiro", "Baixa", "API", "Artigo criado KCS", "Financeiro - KCS"]
---

# Boleto Rápido via API: Baixa automática de títulos não realizada

**MENSAGEM**

Os títulos não estão sendo baixados automaticamente via API, mesmo com a liquidação sendo exibida na tela **"Acompanhamento de Boletos - API"** (Financeiro »   Consultas Acompanhamento de Boletos - API).

**SITUAÇÃO**

Este problema ocorre quando os boletos são enviados e recebidos corretamente pela API, porém a baixa automática não é executada na tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira). A liquidação aparece registrada no acompanhamento de boletos, mas o status do título não é atualizado no sistema.

**SOLUÇÃO**

A solução para este problema varia conforme a causa identificada. Siga as orientações abaixo:

**Atualização do sistema**

**(1)** Verifique a versão atual do sistema Sankhya Om.
**(2)** Caso esteja em versão anterior à 4.35b439, realize a atualização para a versão igual ou superior.
**(3)** Monitore as próximas baixas automáticas para confirmar o comportamento esperado.

**Verificação do credenciamento da API**

**(1)** Acesse a tela **"Acompanhamento de Boletos - API"** (Financeiro »  Consultas Acompanhamento de Boletos - API).
**(2)**  Verifique se o credenciamento da conta bancária está ativo.
**(3)** Caso o credenciamento esteja inativo ou descredenciado, realize um novo credenciamento da conta bancária.
**(4)** Após o novo credenciamento, o banco identificará automaticamente os títulos pendentes e efetuará as baixas, sem necessidade de processamento manual.

**(5)** Ainda nesta tela, verifique as ações automáticas configuradas para o retorno da API. Na opção "Baixa Automática", é necessário que esteja definida a execução da baixa com base na "data de pagamento" ou na "data de crédito em conta", garantindo assim que o processo seja realizado automaticamente.

![Imagem 1: (5) Ainda nesta tela, verifique as ações automáticas configuradas para o retorno da API. Na opção "Baixa Automática", é…](https://ajuda.sankhya.com.br/hc/article_attachments/39628385549975)

**Verifique o campo Baixa via API**
**(1)** Acessa a tela **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira)
**(2)** Verifique o campo "**Baixa via API**" se o mesmo consta com alguma mensagem de erro, realize a devida correção e proceda com a baixa manual do titulo.
**(3)** Monitore as próximas baixas automáticas para confirmar o ajuste realizado.

![Imagem 2: Verifique o campo Baixa via API (1) Acessa a tela "Movimentação Financeira" (Financeiro » Rotinas » Movimentação…](https://ajuda.sankhya.com.br/hc/article_attachments/39627854425495)

**CAUSA**

Esse incidente ocorre porque a liquidação dos boletos é recebida corretamente pela API, porém a baixa automática não é realizada no financeiro devido a inconsistências de configuração, como versão do sistema desatualizada, problemas no credenciamento da API ou ausência/erro nos parâmetros de baixa automática.
