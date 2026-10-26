---
id: "44010938941591"
titulo: "Limite de Mensagens para WhatsApp - Meta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010938941591-Limite-de-Mensagens-para-WhatsApp-Meta"
trilha: "Flowbiz > Meta"
atualizado_em: "2026-10-05T18:51:19Z"
rotulos: ["sync_hc", "flowbiz", "flowbiz_132", "sync_hash_460688e05e5d"]
---

# Limite de Mensagens para WhatsApp - Meta

Recentemente a **Meta definiu um limite diário** para **iniciar novas conversas** com leads via WhatsApp Business API.

Acesse este link e veja o [pronunciamento da Meta](https://developers.facebook.com/docs/whatsapp/messaging-limits/?translation).

Há um teto de **usuários únicos** que sua empresa pode contatar num **período de 24 horas**. Quando esse limite é atingido, não é possível iniciar novas conversas até que a janela de 24 horas seja renovada.

Por padrão, números não verificados começam com um limite de **250 conversas únicas por 24 h**.

Se sua empresa já passou pelo processo de verificação de negócios da Meta ou por um caminho de escalonamento, esse limite inicial pode ser de **2.000 (2K)**.

**Esses limites** se aplicam **apenas a conversas iniciadas pelo negócio** (business-initiated, via template). Eles **não se aplicam** a conversas iniciadas pelo usuário.

As faixas de limite para conversas iniciadas por você são:

- 2K usuários únicos / 24h
- 10K usuários únicos / 24h
- 100K usuários únicos / 24h
- Ilimitado (quando os critérios são atendidos)

## Como funciona o aumento de limite

O limite de mensagens é aumentado automaticamente com base em três critérios principais:

1. **Status do número de telefone**: ele precisa estar “Conectado” / “Ativo”.
2. **Classificação de qualidade (Quality Rating)**: deve estar em nível “Médio” ou “Alto”, considerando feedbacks dos últimos 7 dias, como bloqueios, denúncias ou como os usuários responderam às mensagens.
3. **Uso do limite atual**: nos últimos 7 dias, você deve ter iniciado conversas com pelo menos metade do seu limite. Por exemplo, se seu limite atual é de 10.000, nos últimos 7 dias você deve ter iniciado pelo menos 5.000 conversas únicas.

Se todos os critérios forem atendidos, a Meta normalmente **eleva seu limite em um nível dentro de 6 a 24 horas**, dependendo da fonte.

Se a qualidade cair (ou seja, muitos bloqueios ou denúncias), o limite pode ser mantido ou até reduzido em um nível.

Caso ainda tenha dúvidas, é só entrar em contato com nossa equipe de suporte pelo chat da ferramenta — estamos aqui para ajudar! 😊
