---
id: "39370424310935"
titulo: "Erro ao excluir nota de devolução própria"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39370424310935-Erro-ao-excluir-nota-de-devolu%C3%A7%C3%A3o-pr%C3%B3pria"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-08-31T02:15:56Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Financeiro", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# Erro ao excluir nota de devolução própria

**MENSAGEM**

O sistema não permite excluir isoladamente o título financeiro vinculado a uma nota de devolução.

**SITUAÇÃO**

Ao tentar excluir um título financeiro vinculado a uma nota de devolução, o sistema bloqueia a operação. O usuário espera que o título deveria ter sido removido junto com a devolução.

**SOLUÇÃO**

O comportamento está correto, o sistema não permite excluir só o título, pois ele deve permanecer vinculado à nota enquanto ela existir. Siga esta ordem:

**(1)** **Confirme se a TOP da devolução gera financeiro.** Se sim, é esperado existir um título em Financeiro > Consultas > Movimentação Financeira.

**(2)** **Faça a Compensação da Devolução** (Central de Notas, sobre a nota de devolução, opção Compensação de Devolução), quitando o título da devolução contra o título da venda original. Esse é o fluxo padrão, normalmente não é necessário excluir nada.

**(3)** **Só se realmente precisar remover o título, trate a nota fiscal, não o título diretamente:**

- Se o título **ainda não tem baixa**, e a nota **ainda não foi autorizada/transmitida**, ela pode ser excluída, o título é removido junto.
- Se a nota **já foi autorizada (NF-e)**, ela só pode ser **cancelada**, e apenas dentro do prazo legal de cancelamento.
- Se o título **já tem baixa registrada**, nenhuma das opções acima funciona antes de **estornar a baixa**.

**Importante:** se a nota já foi autorizada e o prazo legal de cancelamento já passou, excluir/cancelar deixa de ser opção, o caminho correto é a compensação (passo 2) ou um documento fiscal complementar.

**CAUSA**

O sistema mantém o vínculo entre nota fiscal e título para preservar a integridade fiscal e contábil. A exclusão do título só é permitida como consequência da exclusão/cancelamento da própria nota, nunca isoladamente, e essas operações têm suas próprias restrições (baixa registrada, prazo legal de cancelamento).
