---
id: "360043576054"
titulo: "Nota associada por remessa não pode ser alterada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043576054-Nota-associada-por-remessa-n%C3%A3o-pode-ser-alterada"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:13Z"
rotulos: ["CORE_E02721", "Configuração", "Segurança", "Impostos", "Nota Fiscal", "Preferências", "Configuração de permissões", "Restrição de Alteração em Notas Associadas por Remessa: Solução de Configuração"]
---

# Nota associada por remessa não pode ser alterada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16105578714263) MENSAGEM:**

[CORE\_E02721] Nota associada por remessa não pode ser alterada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16105578717079) SOLUÇÃO:**

Caso seja necessário realizar alguma correção e/ou atualização de impostos em notas de compra, que possuem "Número de Remessa", faça a configuração das opções abaixo:

![Imagem 3: Acesse a Tela " Preferências " (Configurações » Avançado) .](https://ajuda.sankhya.com.br/hc/article_attachments/16105546811799) Acesse a Tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)"** (Configurações » Avançado).

![Imagem 4: Busque pela chave "ALTERANUREM - Alterar notas com NUREM"](https://ajuda.sankhya.com.br/hc/article_attachments/16105578718487) Busque pela chave **"ALTERANUREM - Alterar notas com NUREM"**

![Imagem 5: Altere para Ligado:](https://ajuda.sankhya.com.br/hc/article_attachments/16105578719127) Altere para Ligado:

![Imagem 6: Altere para Ligado:](https://ajuda.sankhya.com.br/hc/article_attachments/12291909631639)

![Imagem 7: Acesse a tela " Usuários " , localize o usuário que terá permissões para alterar notas ligadas pelo número de remessa.](https://ajuda.sankhya.com.br/hc/article_attachments/16105546813591) Acesse a tela **"[Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios)"**, localize o usuário que terá permissões para alterar notas ligadas pelo número de remessa.

![Imagem 8: Na aba "Segurança", marque a opção "Permite alterar notas ligadas pelo número de remessa" :](https://ajuda.sankhya.com.br/hc/article_attachments/16105546814103) Na aba **"Segurança",** marque a opção **"Permite alterar notas ligadas pelo número de remessa"**:

![Imagem 9: Na aba "Segurança", marque a opção "Permite alterar notas ligadas pelo número de remessa" :](https://ajuda.sankhya.com.br/hc/article_attachments/14501016994583)

(2)** Permite alterar notas ligadas pelo número de remessa:** Esta opção permite ao usuário realizar a edição em notas ligadas por remessa. Caso seja necessário realizar alguma correção e/ou atualização de impostos em notas de compra, a utilização desta opção se faz necessária para conclusão do fechamento do mês. Para que esta opção seja apresentada na tela para utilização, ative o parâmetro Alterar notas com NUREM - ALTERANUREM.

**(2)** Além da marcação acima, valide se a opção **"Altera registros confirmados"** está marcada.

![Imagem 10: Além disso, para sucesso na edição de uma nota, vá até a TOP utilizada no lançamento da mesma, acesse a aba "Geral" e…](https://ajuda.sankhya.com.br/hc/article_attachments/16105546814871) Além disso, para sucesso na edição de uma nota, vá até a TOP utilizada no lançamento da mesma, acesse a aba **"Geral"** e marque o campo **"Permitir alteração após confirmar".** Por fim, a própria nota deve possuir o campo **"Nro Remessa"** preenchido com um valor diferente de "0" (zero).

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16105578721431) CAUSA:**

Mensagem apresentada ao tentar alterar notas que possuem "Nro Remessa" preenchidos, sem que as devidas permissões tenham sido aplicadas.
