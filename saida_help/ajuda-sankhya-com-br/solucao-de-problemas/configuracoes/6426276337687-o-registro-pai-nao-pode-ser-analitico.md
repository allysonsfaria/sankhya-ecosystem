---
id: "6426276337687"
titulo: "O registro pai não pode ser analítico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6426276337687-O-registro-pai-n%C3%A3o-pode-ser-anal%C3%ADtico"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:16:29Z"
rotulos: ["Natureza", "#validadoHugo", "CORE_E04993", "CORE_E03774", "Cadastro", "Erro: Registro Pai Não Pode Ser Analítico", "Erro"]
---

# O registro pai não pode ser analítico

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16461286722071)  MENSAGEM:**

[CORE\_E04993] O registro pai não pode ser analítico.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16461286723991) CAUSA:**

O erro ocorre quando tenta-se cadastrar uma nova natureza (Registro pai) como analítica.

**![Imagem 3: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16461286727703) SOLUÇÃO**

Foi verificado que nessa determinada situação, estava sendo cadastrado um registro filho com uma matriz diferente do registro pai. Para entender na prática, no exemplo em questão, estava sendo cadastrada uma natureza nova, porém, essa natureza  seria um **registro pai,** ou seja, cadastraria novas ramificações para esta mesma natureza, de tal modo, ela não pode ser analítica, apenas os registros filhos podem ser analíticos.
