---
id: "360044089313"
titulo: "Já existe uma nota com este número lançada no dia XX/XX/XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044089313-J%C3%A1-existe-uma-nota-com-este-n%C3%BAmero-lan%C3%A7ada-no-dia-XX-XX-XXXX"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:32Z"
rotulos: ["DUVIDANF", "CORE_E02251", "Configuração", "Parceiro", "NF-e", "TOP", "CORE_E02399", "Validação de Numeração", "Lançamento de Nota", "Tipos de Operação (TOP)", "Erro"]
---

# Já existe uma nota com este número lançada no dia XX/XX/XXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16092600496279) MENSAGEM:**

[CORE\_E02251] Já existe uma nota com este número lançada no dia XX/XX/XXXX.

![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16092571613335) **SITUAÇÃO:**

Ao efetuar o lançamento de uma Nota, apresenta a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16092571617175) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 4: Acesse a tela " Tipos de Operação - TOP " (Caminho para acesso: Comercial » Arquivo » Cadastros » Tipos de Operação -…](https://ajuda.sankhya.com.br/hc/article_attachments/16092571621015) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)["](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)**(Caminho para acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

**(2)** Aba **"Impressão";**

**(2)** Campo **"Valida Numeração por"**, verificar a configuração neste campo:

![Imagem 5: (2) Campo "Valida Numeração por" , verificar a configuração neste campo:](https://ajuda.sankhya.com.br/hc/article_attachments/14477861859607)

De acordo com a configuração disposta no campo acima, a validação ocorrerá, se proíbe ou NÃO, e de acordo com a combinação, não poderá existir um novo lançamento igual.

**Exemplo:** PROIBIR - Parceiro/Numero/Série

**(2)** Não poderá haver uma mesma nota do mesmo parceiro, mesmo número e mesma série.

**(2)** Esta configuração impede que ocorra lançamentos em duplicidades. Por exemplo, um setor de Compras onde exista vários usuários lançando notas de compras e com isso existe o risco de duplicar informações no sistema.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16092571628183) CAUSA:**

Ocorre geralmente em lançamentos de compra, quando se tenta efetuar um lançamento com o mesmo número de nota, que já esta lançado no sistema.
