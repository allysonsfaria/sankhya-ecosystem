---
id: "7238900539159"
titulo: "A exclusão de remuneração desligamento e tsv término não é aceita quando houver pagamento relacionado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7238900539159-A-exclus%C3%A3o-de-remunera%C3%A7%C3%A3o-desligamento-e-tsv-t%C3%A9rmino-n%C3%A3o-%C3%A9-aceita-quando-houver-pagamento-relacionado"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:24:09Z"
rotulos: ["Pagamento", "não apagar", "#validadoAnaLucia", "eSocial", "Erro 851", "Central do eSocial", "Exclusão com pagamento", "Regime exclua pagamento", "Exclusão sem pagamento", "Erro", "Desligamento", "Remuneração"]
---

# A exclusão de remuneração desligamento e tsv término não é aceita quando houver pagamento relacionado

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16506061587863) MENSAGEM**:

Erro 851 - A exclusão de remuneração desligamento e tsv término não é aceita quando houver pagamento relacionado. Ação Sugerida Antes de excluir a remuneração ou desligamento exclua as informações de pagamento relacionadas

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16506090554903) SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo:

![Imagem 3: Verifique primeiramente se a empresa é regime de caixa ou competência.](https://ajuda.sankhya.com.br/hc/article_attachments/16506090558871) Verifique primeiramente se a empresa é regime de caixa ou competência.

| **Exemplo:** está tentando excluir o S-1200 de 05/2022 de uma empresa que é regime de caixa. O S-1210 do mês 05/2022 e 06/2022 já foram enviados. Nesse caso terá que excluir os S-1210 do mês 06/2022 para conseguir excluir o S-1200 do mês 05/2022, pois o S-1210 de 06/2022 é o pagamento referente a remuneração do mês 05/2022. |
| --- |

![Imagem 4: Se a empresa é regime de competência, exclua o S-1210 do mês 05/2022, que é a referência do evento de remuneração que…](https://ajuda.sankhya.com.br/hc/article_attachments/16506090565143) Se a empresa é regime de competência, exclua o S-1210 do mês 05/2022, que é a referência do evento de remuneração que está tentando excluir.

![Imagem 5: Após verificar, acesse a central do eSocial e localize o S-1210 e realize a exclusão. Após isso, será possível excluir…](https://ajuda.sankhya.com.br/hc/article_attachments/16506061603607) Após verificar, acesse a central do eSocial e localize o S-1210 e realize a exclusão. Após isso, será possível excluir o evento de remuneração (S-1200,S-2299,S-2399).

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16506061605271)CAUSA:**

Este erro ocorre no retorno do registro **S-1200/ S-2299 ou S-2399 - (Exclusão dos eventos)** quando este está tentando excluir os registros de remuneração, sem antes excluir o pagamento efetuado no registro **S-1210 - (Pagamentos de Rendimentos do Trabalho)**.

**Eventos de Remuneração:**

**S-1200 -** Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social;

**S-2299** - Desligamento;

**S-2399** - Trabalhador Sem Vínculo de Emprego/Estatutário - Término;
