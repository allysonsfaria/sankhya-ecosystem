---
id: "360044110794"
titulo: "A natureza \"XX\" da conta \"X.X.X.XX.XXXX\" pai do código de aglutinação \"XX.XX\" é inválida para o tipo de demonstração \"J150\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110794-A-natureza-XX-da-conta-X-X-X-XX-XXXX-pai-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-XX-XX-%C3%A9-inv%C3%A1lida-para-o-tipo-de-demonstra%C3%A7%C3%A3o-J150"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:04Z"
rotulos: ["#criadoRoger", "#revisadojunior", "ECD", "Fiscal", "Centro de Resultado", "Contabilização", "Plano de Contas", "Definir Grupo de Conta", "Natureza inválida para DRE", "Grupo incorreto", "Erro"]
---

# A natureza "XX" da conta "X.X.X.XX.XXXX" pai do código de aglutinação "XX.XX" é inválida para o tipo de demonstração "J150"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16416309507223) MENSAGEM:**

A natureza "XX" da conta "X.X.X.XX.XXXX" pai do código de aglutinação "XX.XX" é inválida para o tipo de demonstração "J150".

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16416293342615) SITUAÇÃO:**

Ao validar as informações do ECD-Contábil, ocorre a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16416309510935) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Contabilização » Cadastros » Plano de Contas](https://ajuda.sankhya.com.br/hc/article_attachments/16416293346071) Acesse: Contabilização » Cadastros » Plano de Contas

- Selecione as Contas, indicada na descrição da mensagem.
- Defina o campo: **Grupo de Conta:[04-Centro de Resultado]**

![Imagem 5: Defina o campo: Grupo de Conta:(04-Centro de Resultado)](https://ajuda.sankhya.com.br/hc/article_attachments/360060157254)

![Imagem 6: Após os ajustes, gere novamente o arquivo para transmissão.](https://ajuda.sankhya.com.br/hc/article_attachments/16416293347479) Após os ajustes, gere novamente o arquivo para transmissão.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16416309516055) CAUSA:**

Ocorre devido ao grupo de conta que participam da elaboração da DRE (registro J150) estar com o campo **"Grupo de Conta"** da tela **"Plano de Contas"** diferente da opção **"04 - Contas de resultado"**.
