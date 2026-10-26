---
id: "7569732674455"
titulo: "Como aceitar produto repetido na nota?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7569732674455-Como-aceitar-produto-repetido-na-nota"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:13:28Z"
rotulos: ["Produtos", "Configuração", "produto", "TOP", "Parâmetros", "Estoque", "#publifer", "tribos", "produto repetido", "item repetido", "Produto repetido na nota", "Aceitar produto repetido", "Parâmetro \"ACEITARPRODREP\""]
---

# Como aceitar produto repetido na nota?

#### Analisar as configurações a seguir : Imagem 1: Analisar as configurações a seguir : Parâmetro "ACEITARPRODREP - Aceitar produto repetido" : Parâmetro "ACEITARPRODREP - Aceitar produto repetido":

Se estiver "**Sim"**, permitirá ao usuário incluir o mesmo produto mais de uma vez na nota. Se estiver **"Não"**, quando o usuário tentar incluir o mesmo produto nos itens da nota o sistema emitirá mensagem ["Já existe este produto na sequência X".](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052112034--CORE-E04343-N%C3%A3o-%C3%A9-permitido-inserir-item-repetido-Produto-XXXX-j%C3%A1-existe-na-sequ%C3%AAncia-X-pelo-executante-X-Como-resolver-)

![Imagem 2: Se estiver " Sim" , permitirá ao usuário incluir o mesmo produto mais de uma vez na nota. Se estiver "Não" , quando o…](https://ajuda.sankhya.com.br/hc/article_attachments/16530106100503)

**Importante:**

Ainda nesse contexto, considerando que seja inserido o mesmo produto, porém com **local de origem e/ou controles diferentes**, a inclusão de forma repetida será permitida, independente dos parâmetros mencionados.

#### Imagem 3: Na TOP, temos também a opção de configurar esta questão: Na TOP, temos também a opção de configurar esta questão:

| - **Tela - Tipos de Operação - TOP** |
| --- |

O campo**"Aceitar Produto Repetido"**serve para determinar se será ou não permitido lançar itens repetidos nos Portais.  Desse modo, temos no campo Aceitar Produto Repetido, as seguintes alternativas:

(1)** Usar o parâmetro Global:** se estiver marcada, o sistema respeitará o que foi definido no parâmetro ACEITARPRODREP.

(1)** Sim:** se estiver marcada, independente do parâmetro global será permitido lançar itens repetidos.

(1)** Não:** se estiver marcada, independente do parâmetro global não será permitido lançar itens repetidos.

![Imagem 4: (1) Não: se estiver marcada, independente do parâmetro global não será permitido lançar itens repetidos.](https://ajuda.sankhya.com.br/hc/article_attachments/16530068227991)

#### Imagem 5: Parâmetro "AGRUPFATSEMP - Agrupar prod. repetido em qualquer faturamento?": Parâmetro "AGRUPFATSEMP - Agrupar prod. repetido em qualquer faturamento?":

Ao lançar um pedido/nota com produtos repetidos e fazer qualquer tipo de faturamento no pedido/nota gerado, se o parâmetro estiver ligado esses produtos repetidos serão agrupados.

**Importante:** caso o parâmetro Agrupar prod. repetido em qualquer faturamento? - AGRUPFATSEMP esteja ativado e esteja sendo utilizada uma TOP cuja marcação **"Copiar liberações quando faturando individualmente"** esteja realizada, ao proceder com um faturamento, o sistema não copia as liberações de limite referentes aos itens do pedido/nota (esta cópia não é feita, pois a tabela pertinente aos itens (TGFITE) irá sofrer modificações; serão copiadas as liberações correspondentes ao cabeçalho do documento).

#### Outros Parâmetros:

- **"ACEITARPRODREPE  - Aceitar prod.repetido para Exec.diferente?"** Ligado

Ao lançar itens repetidos na central, informando o mesmo executante **não permite** itens repetidos. Mas permite itens repetidos na central informando **executantes diferentes,** conforme imagem abaixo:

![Imagem 6: Ao lançar itens repetidos na central, informando o mesmo executante não permite itens repetidos. Mas permite itens…](https://ajuda.sankhya.com.br/hc/article_attachments/16530068234775)

Dessa forma, temos :

| **Cenário 1:**  ACEITARPRODREP - Aceitar produto repetido: **Desligado** ACEITARPRODREPE  - Aceitar prod.repetido para Exec.diferente?: **Desligado**  Ao lançar itens repetidos na central o sistema **não** permite e emite a mensagem abaixo! |
| --- |

| **Cenário 2:**  ACEITARPRODREP - Aceitar produto repetido: **Ligado** ACEITARPRODREPE  - Aceitar prod.repetido para Exec.diferente?: **Desligado**  Ao lançar itens repetidos na central **o sistema permite!** |
| --- |

| **Cenário 3:**  ACEITARPRODREP - Aceitar produto repetido: **Desligado** ACEITARPRODREPE  - Aceitar prod.repetido para Exec.diferente?: **Ligado**  **Ao lançar itens repetidos na central informando o mesmo executante não permite! Mas permite itens repetidos na central informando executantes diferentes.** |
| --- |

| **Cenário 4:**  ACEITARPRODREP - Aceitar produto repetido: **Ligado** ACEITARPRODREPE  - Aceitar prod.repetido para Exec.diferente?: **Ligado**  Aceita lançar itens repetidos **com executantes repetidos** para os mesmos produtos |
| --- |
