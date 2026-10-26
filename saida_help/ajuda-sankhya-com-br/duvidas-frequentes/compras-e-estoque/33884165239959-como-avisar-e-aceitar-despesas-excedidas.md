---
id: "33884165239959"
titulo: "Como avisar e aceitar despesas excedidas no Planejamento de Metas e Orçamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33884165239959-Como-avisar-e-aceitar-despesas-excedidas-no-Planejamento-de-Metas-e-Or%C3%A7amento"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:28:03Z"
rotulos: ["Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "no Planejamento de Metas e Orçamento", "Propriedades", "ALTRATSEMVALMET", "Como avisar e aceitar despesas excedidas", "Configuração da Estrutura de Metas/Orçamentos", "Metas e Orçamentos"]
---

# Como avisar e aceitar despesas excedidas no Planejamento de Metas e Orçamento

Este artigo explica como configurar o sistema para que, ao registrar lançamentos financeiros que ultrapassem as metas e orçamentos planejados, um aviso seja exibido, mas o lançamento seja permitido normalmente nas centrais (como Central de Compras, Central de Vendas, etc.).

Essa configuração é ideal para empresas que desejam monitorar orçamentos e metas sem bloquear lançamentos que excedam os valores previstos, garantindo controle por meio de alertas informativos sem interromper o processo operacional.

**SOLUÇÃO:**

**(1)** Configuração da Estrutura de Metas/Orçamentos:

- Acesse a tela ''**Configuração da Estrutura de Metas/Orçamentos''** (Metas e Orçamentos» Configuração da Estrutura de Metas/Orçamentos) vá até a aba ''**Propriedades** ''e defina o campo ''**Quando exceder a Despesa Prevista:''** para ''**Avisar e Aceitar o Lançamento''**.

![Imagem 1: Acesse a tela '' Configuração da Estrutura de Metas/Orçamentos'' (Metas e Orçamentos» Configuração da Estrutura de…](https://ajuda.sankhya.com.br/hc/article_attachments/34051802845847)

Assim, o sistema exibirá o alerta de excesso de gasto, mas permitirá que o lançamento seja realizado normalmente.

**(2)** Preferências do Sistema – Parâmetro ''**ALTRATSEMVALMET''**:

- Acesse a tela **"Preferências"** e localize o parâmetro: ALTRATSEMVALMET;
- Altere o parâmetro para: **"Ligado";**

#### Considerações:

- Esse parâmetro é essencial porque, quando desligado, o sistema valida o rateio das despesas e bloqueia lançamentos que ultrapassem o limite previsto na meta;
- Antes de ativar o parâmetro, confirme com o setor responsável se a empresa realmente não quer bloquear lançamentos pela validação do rateio, pois essa alteração reduz o rigor dos controles orçamentários automáticos.

**CAUSA:**

Essa configuração é necessária quando a empresa adota controle orçamentário por metas, mas prefere receber alertas sem bloquear lançamentos em caso de excesso de gastos.

Se os parâmetros não forem ajustados corretamente, o sistema aplicará restrições rígidas, bloqueando lançamentos que ultrapassem as metas, o que pode causar paralisações operacionais, especialmente em empresas que usam metas como referência, não como limite.

O erro mais comum nesse cenário ocorre devido à configuração padrão, que prioriza o bloqueio, sem o ajuste dos parâmetros para flexibilizar o controle.
