---
id: "28131374750103"
titulo: "Produto foi efetivado mesmo com estoque insuficiente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28131374750103-Produto-foi-efetivado-mesmo-com-estoque-insuficiente"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-08-01T01:28:46Z"
rotulos: ["Produtos", "Configuração", "Validação", "Estoque", "Parâmetro", "Produto foi efetivado mesmo com estoque insuficiente", "Artigo atualizado KCS", "CVE - KCS"]
---

# Produto foi efetivado mesmo com estoque insuficiente

Este artigo aborda como resolver o erro **"Estoque insuficiente"** e como configurar o sistema para impedir a saída de produtos sem saldo disponível.

### Situação

A mensagem **"Estoque insuficiente"** pode aparecer ao faturar um pedido de venda, lançar uma nota de devolução, confirmar uma nota de entrada ou movimentar estoque — mesmo quando existe saldo físico cadastrado. Isso acontece porque o sistema está validando o saldo disponível (que considera reservas, lotes e regras de configuração), não apenas o saldo físico bruto.

Situações mais comuns:

- Confirmar pedido de venda com reserva de estoque ativa;
- Faturar pedido diretamente pelo estoque;
- Faturar produto com controle de lote sem informar o lote (o sistema distribui a quantidade pela validade dos lotes e acusa erro se o total for insuficiente);
- Fazer ajuste de estoque quando já existe movimentação posterior que consumiu o saldo.

### Solução

**Grupo de produtos/serviços** (Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços, aba Estoque): confirme o campo "Valida estoque", use **"Empresa/Local"** (recomendado) sempre que possível. Evite deixar como "Não valida".

- Se a marcação **"Pedir Confirmação de Liberação"** estiver ativa, saiba que ela sempre valida **"Pela soma de todas as Empresas"**, independente da opção escolhida acima. Se seu cenário não deve considerar a soma de empresas, desmarque essa opção, caso contrário, a saída pode ser confirmada mesmo sem saldo real no local.

**Cadastro do produto:** verifique se o campo "Controle Adicional" está configurado para lote. Estoque com lote em um produto sem esse controle habilitado impede a validação correta do saldo.

**TOP (Comercial » Arquivo » Cadastros » Tipos de Operação):**

- Confirme se **"Validar Estoque p/ Reservar"** está marcada conforme o comportamento esperado. Desmarcá-la permite estoque negativo quando não há saldo.
- Revise o campo de atualização de estoque (baixa imediata x na confirmação).
- Para lote, confirme "Detalhar lote pela conferência" — o campo "Validar lote conforme Estoque" só fica disponível quando essa opção está ativa.

**Reservas:** se o saldo disponível está negativo, verifique se há excesso de reservas acima do estoque físico.

**Estoque de terceiros:** para movimentações nessa categoria, confirme saldo específico dela, não é somado ao estoque próprio.

**Ajuste de estoque:** se uma movimentação posterior já consumiu o saldo, pode ser necessário cancelá-la antes de corrigir o ajuste.

**Parâmetro VALNOTACONF** (Configurações » Avançado » Preferências): quando desabilitado, impede a validação de alterações em pedidos/notas já confirmados. Avalie habilitá-lo.

**(8)** Em caso de inconsistência pontual entre saldo físico e saldo do sistema, use "Verificação de Saldo de Estoque" (Configurações » Avançado) para localizar a divergência antes de tratar como comportamento esperado.

### Causa

O erro ocorre por uma combinação destes fatores:

1. Saldo físico insuficiente no local de estoque;
2. Excesso de reservas que supera o estoque físico disponível;
3. Produto com lote no estoque, mas sem controle de lote habilitado no cadastro;
4. TOP configurada para validar estoque na reserva ou não atualizar o estoque no momento esperado;
5. Falta de saldo específico em estoque de terceiros;
6. Grupo de produtos configurado sem validação adequada, permitindo saída indevida em determinados fluxos.
