---
id: "30699173129751"
titulo: "A baixa de título não foi realizada de forma automática na Movimentação financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30699173129751-A-baixa-de-t%C3%ADtulo-n%C3%A3o-foi-realizada-de-forma-autom%C3%A1tica-na-Movimenta%C3%A7%C3%A3o-financeira"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Dúvidas frequentes "
atualizado_em: "2026-07-29T13:13:03Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Financeiro", "Venda Mais", "Erro"]
---

# A baixa de título não foi realizada de forma automática na Movimentação financeira

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30699195748887)  SITUAÇÃO:**

Se houver algum problema que impeça a baixa automática dos títulos no **Venda Mais**, o sistema registrará um log com os detalhes do bloqueio. Observe abaixo os possíveis motivos de bloqueio:

- **contabilidade fechada** no período;
- **liberação de limites pendente** de aprovação;
- **conta bancária sem saldo** disponível;
- **configuração ausente** ou incorreta.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30699173124887) SOLUÇÃO:**

Nesses casos, você pode verificar os detalhes do problema na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534). Selecione o respectivo título e acione o botão **Outras Opções** > **Venda Mais** > **Ocorrências Venda Mais**.

Lá, você encontrará um log com os motivos que impediram a baixa, permitindo tomar as medidas necessárias para resolver a situação.

![Imagem 3: Lá, você encontrará um log com os motivos que impediram a baixa, permitindo tomar as medidas necessárias para resolver…](https://ajuda.sankhya.com.br/hc/article_attachments/30699175551639)

Faça o download do relatório e verifique o motivo pelo qual a baixa não aconteceu. Na tabela abaixo constam alguns dos principais motivos e suas respectivas soluções:

| **Motivo macro** | **Motivo detalhado** | **O que fazer?** |
| --- | --- | --- |
| **Divergências de          dados** | Valor retornado pelo parceiro      de crédito diverge do valor          líquido do título no sistema. | Conferir o valor que esperava            receber e o que o parceiro                pagou, validar e baixar                        manualmente. |
| **Regras de negócio      internas** | Contabilidade fechada. | Baixar manualmente conforme as    regras atuais de cada empresa. |
| Liberação de limites pendente. | Solicitar aprovação ao                        responsável e baixar                            manualmente. |
| Conta bancária sem saldo. | Informar um saldo na conta              bancária e baixar manualmente. |
| **Falhas de                        conectividade** | API do parceiro fora do ar no      horário estabelecido. | Verifique os títulos a serem                baixados, e realize o processo          manualmente. |
| API da Sankhya fora do ar no      horário estabelecido. | Verifique os títulos a serem                baixados, e realize o processo          manualmente. |
