---
id: "9803371607831"
titulo: "Parceiro com X título(s) vencido(s) no Financeiro. Seu limite é de XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9803371607831-Parceiro-com-X-t%C3%ADtulo-s-vencido-s-no-Financeiro-Seu-limite-%C3%A9-de-XX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:05:54Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Crédito", "Financeiro", "CORE_E01797", "Limite de Títulos Vencidos Excedido"]
---

# Parceiro com X título(s) vencido(s) no Financeiro. Seu limite é de XX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19551658822423) MENSAGEM:**

[CORE\_E01797] Parceiro com X título(s) vencido(s) no Financeiro. Seu limite é de XX. Maior atraso é X. A tolerância é XX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19551620530711) SITUAÇÃO:**

Ao tentar confirmar a nota a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19551658845591) CAUSA:**

Quando a tolerância para títulos vencidos desse parceiro já estão no limite definido.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19551620558231) SOLUÇÃO:**

Habilite o parâmetro **"Usar liberação de limites por alçada? - USALIBLIM"**.

![Imagem 5: Habilite o parâmetro "Usar liberação de limites por alçada? - USALIBLIM" .](https://ajuda.sankhya.com.br/hc/article_attachments/19551658859543)

Defina um usuário liberador para o evento 22 - Quantidade Máxima de títulos vencidos.

![Imagem 6: Defina um usuário liberador para o evento 22 - Quantidade Máxima de títulos vencidos .](https://ajuda.sankhya.com.br/hc/article_attachments/19551658872215)

![Imagem 7: Defina um usuário liberador para o evento 22 - Quantidade Máxima de títulos vencidos .](https://ajuda.sankhya.com.br/hc/article_attachments/19551620585239)

Acesse o cadastro de **Parceiros** (Caminho de acesso à tela: Configurações » Cadastros » Parceiros), vá até a aba 'Crédito' e verifique a quantidade de dias informados no campo "Quant.Máx.Títulos Vencidos"

![Imagem 8: Acesse o cadastro de Parceiros (Caminho de acesso à tela: Configurações » Cadastros » Parceiros), vá até a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/19551658898711)

A **"Qtd. máx. de títulos vencidos"** se refere à quantidade limite de títulos que o sistema irá utilizar para fazer a validação de títulos vencidos para cada Parceiro. Na tela onde são cadastrados os [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral), marcação **"Validar Qtd. Máx. Títulos Vencidos"**, configure para que seja feita a validação dos títulos vencidos. Se ultrapassada a quantidade de títulos vencidos, o sistema irá apresentar a seguinte mensagem:

**"Parceiro com XX título(s) vencido(s) no Financeiro. Seu limite é de YY. Maior atraso é ZZ. A tolerância é XX."**

Verifique também no cadastro do tipo de título utilizado se o campo **"Validar Qtd. Máx. Títulos Vencidos"**está selecionado.

![Imagem 9: Verifique também no cadastro do tipo de título utilizado se o campo "Validar Qtd. Máx. Títulos Vencidos" está…](https://ajuda.sankhya.com.br/hc/article_attachments/19551620603799)

No campo **"Validar Qtd. Máx. Títulos Vencidos"** você define se será ou não validada a quantidade máxima de títulos vencidos, configurada na aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito) do [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros). Assim, no faturamento de um título que tenha este campo configurado, o sistema verificará quantos títulos vencidos há para o parceiro. Se estes excederem a quantidade informada no campo **"Quant.Máx.Títulos Vencidos"** da aba Crédito no Cadastro do Parceiro, o sistema barrará o faturamento.
