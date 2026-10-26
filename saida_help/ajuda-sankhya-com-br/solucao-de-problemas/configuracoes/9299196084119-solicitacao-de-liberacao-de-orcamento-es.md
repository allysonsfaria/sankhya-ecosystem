---
id: "9299196084119"
titulo: "Solicitação de liberação de orçamento está pendente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9299196084119-Solicita%C3%A7%C3%A3o-de-libera%C3%A7%C3%A3o-de-or%C3%A7amento-est%C3%A1-pendente"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:59Z"
rotulos: ["Configuração", "Metas", "Preferências", "Financeiro", "Orçamento", "CORE_E05411", "Gestão de Orçamentos: Resolução de Pendências"]
---

# Solicitação de liberação de orçamento está pendente

**Mensagem:**

[CORE\_E05411]  Solicitação de liberação de orçamento está pendente.

**Causa:**

Ocorre quando o orçamento não é aprovado.

**Solução:**

Na estrutura de metas e orçamentos temos a seguinte configuração:

- Ignora orçamento não previsto = marcado
- Quando exceder a Despesa Prevista = Avisar e Não aceitar o lançamento
- No Planejamento de Metas e Orçamentos, se a coluna de Previstos estiver zerada e a coluna de realizados estiver preenchida, ao fazer um lançamento com esse projeto, o sistema solicita a liberação dessa meta.
- Para não solicitar essa liberação, o cliente tira o 'zero - 0,00' da coluna de previstos, logo a coluna de realizado também fica sem registros, aí dessa forma o sistema não solicita a liberação.

Verificar a configuração na tela **Preferências** (Configurações » Avançado » Preferências) do parâmetro **'METZERONAOPREV - Considera orçamento zerado como não previsto?'**caso esteja desligado basta ligá-lo e realizar o teste novamente.

![Imagem 1: Verificar a configuração na tela Preferências (Configurações » Avançado » Preferências) do parâmetro 'METZERONAOPREV -…](https://ajuda.sankhya.com.br/hc/article_attachments/14367412079767)
