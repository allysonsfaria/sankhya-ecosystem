---
id: "360043660753"
titulo: "Desconto acima do permitido no tipo de negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043660753-Desconto-acima-do-permitido-no-tipo-de-negocia%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:14Z"
rotulos: ["Configuração", "Validação", "Desconto", "Preferências", "CORE_E02008", "Desconto Excedido: Mensagem de erro", "Configurações de Validação: Ajuste necessário", "Parâmetro e Solução: Verificação e ajuste", "Comercial"]
---

# Desconto acima do permitido no tipo de negociação

**![Imagem 1: MENSAGEM](https://ajuda.sankhya.com.br/hc/article_attachments/16142745466007) MENSAGEM**

[CORE\_E02008] Desconto acima do permitido no tipo de negociação.

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16142729366423) SITUAÇÃO**

Ao tentar efetuar a confirmação de um Pedido/Nota, a seguinte mensagem é apresentada.

**![Imagem 3: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16142745470871) SOLUÇÃO**

Avalie se as configurações abaixo estão de acordo com o desconto desejado para esse cenário, em sua empresa:

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação](https://ajuda.sankhya.com.br/hc/article_attachments/16142729374103) Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação

- Aba: **"Características"**, campo **"% Desconto Máximo"**:

![Imagem 5: Aba: "Características" , campo "% Desconto Máximo" :](https://ajuda.sankhya.com.br/hc/article_attachments/14686256672919)

![Imagem 6: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16142745477399) Acesse: Configurações » Avançado » Preferências

Parâmetro: **"VALDESCMAX- Valida desconto máximo"**

![Imagem 7: Parâmetro: "VALDESCMAX- Valida desconto máximo"](https://ajuda.sankhya.com.br/hc/article_attachments/12125939829271)

- **NÃO VALIDA** - não será validado desconto máximo em nenhuma hipótese, independente dos percentuais cadastrados.
- **VALIDA E ACEITA** - o sistema emitirá mensagens de alerta sempre que os descontos nas vendas forem superiores a qualquer um dos percentuais informados nos cadastros de produtos e tipos de negociação, mas permitirá a confirmação das vendas.
- **VALIDA E NÃO ACEITA** - o sistema emitirá mensagens sempre que os descontos forem superiores a qualquer um dos percentuais informados nos cadastros de produtos e tipos de negociação e não permitirá a venda. Se o parâmetro **"Usa liberação de limites por alçada? (USALIBLIM)"** estiver **"Sim"**, o sistema abrirá a tela para solicitação de liberação de limites.
- **VALIDA E NÃO ACEITA** **(Exceto Prod. em Promoção)** - o sistema não validará o desconto máximo para produtos que estejam em promoção. Os produtos que não estão em promoção serão validados e o sistema não permitirá a conclusão da venda, exceto se for solicitada a liberação.
- **VALIDA E NÃO ACEITA** (**Somente na confirmação**) - o sistema não validará nenhum tipo de desconto máximo ao confirmar itens. Assim, quando o usuário for confirmar a nota, serão feitas todas as validações.

**![Imagem 8: IMPORTANTE](https://ajuda.sankhya.com.br/hc/article_attachments/16142729382167) IMPORTANTE**

No campo %Desconto Máximo a informação '0' (zero) corresponde a um desconto máximo de 0%. Caso não deseje aplicar desconto máximo para determinado tipo de negociação, o campo deve estar vazio.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16142745482263) CAUSA:**

Ao confirmar lançamentos, quando o desconto aplicado for superior ao %desconto máximo do tipo de negociação utilizado e o parâmetro VALDESCMAX encontrar-se configurado como 'Valida e não aceita', será apresentada a mensagem.
