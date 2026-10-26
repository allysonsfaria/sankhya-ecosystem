---
id: "37361520919319"
titulo: "Erro ao Excluir Ocorrência de Funcionário(a): “Falha ao deletar a ocorrência. Motivo: null”"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37361520919319-Erro-ao-Excluir-Ocorr%C3%AAncia-de-Funcion%C3%A1rio-a-Falha-ao-deletar-a-ocorr%C3%AAncia-Motivo-null"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:13Z"
rotulos: ["Ocorrências", "Folha", "Configuração Funcionários", "Erro", "Erro ao excluir ocorrência de funcionário(a)", "excluir o último lançamento de ocorrência", "ocorrências recorrentes ativas", "configuração incorreta da ocorrência recorrente existente", "Recorrente"]
---

# Erro ao Excluir Ocorrência de Funcionário(a): “Falha ao deletar a ocorrência. Motivo: null”

**MENSAGEM:**

“Falha ao deletar a ocorrência. Motivo: null”

![Imagem 1: “Falha ao deletar a ocorrência. Motivo: null”](https://ajuda.sankhya.com.br/hc/article_attachments/37361520918679)

##### SITUAÇÃO:

##### Ao tentar excluir o último lançamento de ocorrência da funcionário(a), o sistema apresentou a mensagem de erro acima. A exclusão não foi concluída, mesmo tratando-se do último registro lançado.

#####

##### SOLUÇÃO:

**(1)** Acesse a tela [**''Ocorrências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494-Ocorr%C3%AAncias) (Pessoal+ » Rotinas Folha » Ocorrências).

**(2)** Localize a ocorrência que precisa ser excluída.

**(3)** Verifique se existem **ocorrências recorrentes ativas** para o colaborador(a).

**(4)** Confirme que todas as ocorrências recorrentes que exigem **anexo de atestado** possuam o documento vinculado.

**(5)** Ajuste qualquer configuração inconsistente da ocorrência recorrente.

**(6)** Após realizar as correções, **exclua novamente o lançamento de ocorrência**.

##### CAUSA:

O erro ocorre quando existe uma ocorrência configurada como ''**Recorrente''** que não possui um **anexo de atestado** vinculado.

Essa configuração inconsistente faz com que o sistema acione um **gatilho de validação**, bloqueando a exclusão da ocorrência e exibindo a mensagem de erro sem detalhar o motivo (“null”).

##### OBSERVAÇÃO:

- Ocorrências marcadas como ''Recorrentes'' exigem validações adicionais no sistema.
- A ausência de **anexo obrigatório (atestado)** em ocorrências desse tipo pode gerar inconsistências e bloqueios operacionais.
- O erro não está relacionado à tentativa de exclusão em si, mas sim à **configuração incorreta da ocorrência recorrente existente**.
