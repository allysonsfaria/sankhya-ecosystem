---
id: "39956897991831"
titulo: "Alteração não permitida, pois o produto não é controlado por WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39956897991831-Altera%C3%A7%C3%A3o-n%C3%A3o-permitida-pois-o-produto-n%C3%A3o-%C3%A9-controlado-por-WMS"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-10-20T20:34:02Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Alteração não permitida", "Erro", "Alterar Un. Alternativa", "Unidade Alternativas", "Alterar a Unidade Alternativa"]
---

# Alteração não permitida, pois o produto não é controlado por WMS

**MENSAGEM**

Alteração não permitida, pois o produto não é controlado por WMS

**SITUAÇÃO**

Ao tentar alterar a unidade alternativa no botão **''Alterar Un. Alternativa''** na aba **''Unidade Alternativas''** do cadastro do produto é apresentado a mensagem.

**SOLUÇÃO**

O botão ''Alterar Un. Alternativa'' foi desenvolvido para atender a um processo específico do WMS.

Inicialmente, **não havia uma validação que restringisse o uso para produtos não controlados pelo WMS**. Essa validação passou a ser aplicada a partir das versões 4.29b41 e 4.28b103 ou superiores.

Atualmente, **não é recomendada a alteração direta de informações relacionadas à unidade alternativa**. Como medida de segurança, **o sistema passou a bloquear essa prática por padrão, evitando inconsistências e problemas futuros**.

Quando for necessário realizar alterações, a orientação é cadastrar uma nova unidade alternativa.

**Exemplo:**
Se um produto é comercializado em caixa (CX) com 10 unidades e passará a ter 12 unidades, o ideal é cadastrar uma nova unidade (como CX1) com a nova quantidade e inativar a anterior.

Vale destacar que alterar diretamente o controle do produto para WMS, bem como modificar sua unidade alternativa, pode gerar impactos no estoque e na área fiscal.

**CAUSA**

O motivo dessa validação é que, ao alterar uma unidade alternativa já utilizada em lançamentos, a visualização das notas já emitidas também pode ser alterada. Isso ocorre porque a quantidade é armazenada no banco de dados na unidade padrão.
