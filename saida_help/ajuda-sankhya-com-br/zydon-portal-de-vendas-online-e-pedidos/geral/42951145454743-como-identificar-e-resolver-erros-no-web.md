---
id: "42951145454743"
titulo: "Como identificar e resolver erros no Webhook?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951145454743-Como-identificar-e-resolver-erros-no-Webhook"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T13:54:58Z"
rotulos: ["zydon", "sync_hc", "zydon_213266014768", "sync_hash_c33e11880dbf"]
---

# Como identificar e resolver erros no Webhook?

## O que é um Webhook?

Um webhook é um mecanismo de comunicação entre sistemas, permitindo que um serviço envie informações automaticamente para outro assim que determinados eventos ocorrem. No contexto da Central de Pedidos, os webhooks são utilizados para notificar sistemas externos sobre a criação e atualização de pedidos.

Neste artigo, trataremos especificamente do webhook relacionado à **criação de pedidos**.

## O que acontece quando ocorre um erro no Webhook?

Quando um pedido na Central de Pedidos apresenta um erro no webhook, um e-mail e enviado automaticamente para os membros da organização. Esse e-mail informa que há um pedido com erro e inclui detalhes para que a equipe possa identifica-lo e tomar as devidas providencias.

O mesmo pedido também exibe um ícone de alerta na coluna Erro de Webhook, na lista da Central de Pedidos. Passe o mouse sobre o ícone para ver rapidamente a mensagem de erro, sem precisar abrir o pedido; ao abrir os detalhes do pedido, essa mesma mensagem aparece em um aviso no topo da pagina.

## Como corrigir erros no Webhook

Se você receber uma notificação de erro no webhook, siga os passos abaixo para resolver o problema:

1. **Acesse a Central de Pedidos**

   - Entre no sistema e localize o pedido com erro.
   - Os detalhes do erro estarão disponíveis na página do pedido.
2. **Analise a causa do erro**

   - Alguns erros podem ocorrer por razões simples, como estoque insuficiente ou falhas temporárias de conexão.
3. **Corrija o problema e reenvie o pedido**

   - Se a causa do erro já foi resolvida, você pode reenviar o pedido para que ele seja reprocessado.
   - Para isso, acesse a seção de 'Ações' do pedido e clique em **'Reenviar'**.
4. **Verifique a configuração do Webhook**

   - Se o erro persistir, pode haver um problema na configuração do webhook. Certifique-se de que os endpoints configurados estão corretos e operacionais.

     Para uma analise tecnica mais detalhada, um administrador pode acessar Configuracoes > Webhooks > Pedidos e clicar em Ultimas requisicoes no card do evento correspondente. Essa tela mostra o historico de chamadas (status Enviado ou Falhou, tempo de resposta) e permite abrir cada requisicao para ver os Headers e o Payload completo enviados, alem da Resposta recebida do sistema externo.
5. **Entre em contato com o suporte**

   - Caso o problema continue mesmo após a revisão, entre em contato com o suporte técnico ou com o consultor responsável pela implantação.

## Exemplo de erro: Erro interno #1001

Esse erro pode indicar um problema interno no processamento do webhook. Caso ele ocorra, siga as etapas acima para tentar resolvê-lo e, se necessário, acione o suporte técnico para uma análise mais aprofundada. Outro exemplo real e Unauthorized - token refreshed, que geralmente indica que a credencial de acesso ao sistema externo expirou ou foi renovada e precisa ser reconfigurada.

---

Para mais informações ou qualquer outra dúvida, entre em contato com nossa equipe de suporte.

---

Crie sua conta agora: <https://admin.zydon.com.br/criacao-conta>
