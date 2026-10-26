---
id: "39323672402967"
titulo: "Desconto promocional acima do permitido ao faturar pedido após o fim da promoção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39323672402967-Desconto-promocional-acima-do-permitido-ao-faturar-pedido-ap%C3%B3s-o-fim-da-promo%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-10-08T13:00:44Z"
rotulos: ["DUVIDANF", "Configuração", "Fiscal", "NF-e", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# Desconto promocional acima do permitido ao faturar pedido após o fim da promoção

Quando um pedido é digitado no último dia de validade de uma promoção e a nota fiscal é emitida no dia seguinte, o sistema **não reconhece mais o desconto promocional na nota**, mesmo que o pedido tenha sido criado dentro do período válido da promoção. O desconto do pedido é levado para a nota, mas, na confirmação, passa a ser tratado como **desconto acima do permitido**.

Este é o **comportamento padrão do sistema**, que sempre considera a **data de vigência do desconto promocional** na data da nota fiscal. Atualmente, não existe uma configuração disponível para alterar esse processo e fazer com que o sistema considere a data do pedido ao invés da data de emissão da nota. O que pode ser configurado é a reação do sistema quando o desconto fica acima do permitido.

### Como o sistema valida o desconto promocional

O sistema realiza a **validação do desconto promocional** pela data da nota fiscal, e não pela data do pedido. No faturamento, a nota recebe como data de negociação o dia em que o faturamento é feito. Isso significa que:

**• Data do pedido:** 31/01/2024 (último dia da promoção) - Promoção aplicada no pedido
**• Data da nota fiscal:** 01/02/2024 (após o término da promoção) - O desconto do pedido é copiado para a nota, mas a promoção não está mais vigente

Quando a nota fiscal é confirmada, o sistema **verifica o desconto máximo permitido** para cada item, considerando as promoções vigentes na data da nota. Como a promoção já expirou, o desconto herdado do pedido fica acima do permitido. O resultado (aviso, liberação ou bloqueio) depende do parâmetro **VALDESCMAX**, explicado abaixo.

**Atenção:** se a TOP usada no faturamento estiver com a opção **"Recalcular preço prod. ao faturar"** marcada, o preço do item é buscado novamente na tabela de preços. O percentual de desconto do pedido é mantido, mas a promoção por quantidade cadastrada **em valor** (que altera o preço unitário) é perdida, mesmo dentro do período da promoção.

### Alternativas para evitar a perda do desconto

Para garantir que o desconto promocional seja aceito na nota fiscal, considere as seguintes práticas:

**• Emita a nota fiscal no mesmo dia do pedido:** Sempre que possível, gere a nota fiscal ainda dentro do período de validade da promoção.
**• Estenda o período da promoção:** Configure a promoção com um dia adicional de validade para cobrir possíveis emissões de notas no dia seguinte.
**• Aprove a liberação do desconto:** Se o parâmetro VALDESCMAX estiver configurado para não aceitar desconto acima do permitido e a empresa usar liberação de limites, a confirmação gera uma solicitação de liberação. Com a aprovação do liberador, a nota é confirmada com o desconto do pedido. Lançar o desconto manualmente na nota não resolve, pois ele passa pela mesma validação.

### Configurações relacionadas ao desconto promocional

No cadastro do **Tipo de Negociação**, as opções de desconto promocional definem como a promoção é aplicada:

**• Considerar Sempre:** O sistema sempre tentará aplicar o desconto promocional, validando a vigência na data da operação.
**• Considerar por Qtde/Desconto:** O sistema considera a quantidade e o desconto configurados na promoção.

Essas configurações influenciam como o sistema aplica os descontos, mas **não alteram a regra de validação pela data de vigência** no momento da emissão da nota fiscal.

Já o parâmetro **"VALDESCMAX - Valida desconto máximo (Produto e Tipo Negociação)?"** define o que acontece quando o desconto da nota fica acima do permitido:

**• Não Valida:** a nota é confirmada sem verificar o desconto.
**• Valida e Aceita (padrão):** exibe o aviso "Desconto acima do permitido no cadastro." e confirma a nota com o desconto do pedido.
**• Valida e Não Aceita / Valida e Não Aceita (Exceto Prod. Promoção):** com o parâmetro **"USALIBLIM - Usar liberação de limites por alçada?"** ligado, gera uma solicitação de liberação. Sem ele, bloqueia a confirmação com o aviso "Desconto acima do permitido no cadastro."
**• Valida e Não Aceita (Somente Na Confirmação):** confere o desconto total da nota. Com liberação de limites, gera uma solicitação de liberação. Sem ela, bloqueia com o aviso "Desconto acima do permitido no cadastro de produto."
