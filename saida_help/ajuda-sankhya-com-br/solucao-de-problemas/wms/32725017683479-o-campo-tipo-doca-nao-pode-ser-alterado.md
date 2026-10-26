---
id: "32725017683479"
titulo: "O campo 'Tipo doca' não pode ser alterado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32725017683479-O-campo-Tipo-doca-n%C3%A3o-pode-ser-alterado"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:30:33Z"
rotulos: ["Configuração", "WMS", "Cadastro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "CORE_E01472", "Aviso: O campo 'Tipo doca' não pode ser alterado", "Tipo de Doca", "Erro", "Doca"]
---

# O campo 'Tipo doca' não pode ser alterado

**MENSAGEM:**
[CORE\_E01472] Aviso: O campo 'Tipo doca' não pode ser alterado.

**SITUAÇÃO:**

Ao cadastrar uma nova doca na tela ''**WMS**'' > ''**Cadastro'**' > ''**Docas**'', o campo ''**Tipo de Doca**'' ficará bloqueado para edição após o cadastro ser finalizado.

**SOLUÇÃO:**

**(1)** Altere o campo ''**Tipo de Doca'**' no WMS:

**(1)**Caso seja necessário alterar o tipo de doca, não será possível editar diretamente. Nesse caso, será necessário excluir a doca existente e criar uma nova com o tipo desejado.

**(2)** Cadastre uma nova doca, com o tipo correto.

**Requisito para exclusão:**
 A doca só pode ser excluída se estiver com a situação **Livre** no sistema.

**CAUSA:**

A mensagem ocorre ao tentar alterar o tipo da doca após ela já ter sido criada e salva no sistema.
