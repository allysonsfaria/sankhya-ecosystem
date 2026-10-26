---
id: "360044615753"
titulo: "Somente Transferência pode atualizar Livro de Entrada e de Saída ao mesmo tempo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615753-Somente-Transfer%C3%AAncia-pode-atualizar-Livro-de-Entrada-e-de-Sa%C3%ADda-ao-mesmo-tempo"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:48Z"
rotulos: ["#PUBLIFER", "CORE_E02583", "Configuração", "ICMS", "TOP", "Livro Fiscal", "Transferência", "Restrição na Atualização do Livro Fiscal"]
---

# Somente Transferência pode atualizar Livro de Entrada e de Saída ao mesmo tempo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16310479390231) MENSAGEM:**

[CORE\_E02583] Somente Transferência pode atualizar Livro de Entrada e de Saída ao mesmo tempo.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16310494157207) SOLUÇÃO:**

Caso o campo **"Tipo de Movimento"** seja **diferente** de "**Transferência"** não poderá ser utilizada a opção **"Ambos"** no campo **"Atualização de Livro de ICMS"**. Dessa forma, ajuste esse campo conforme necessidade, após isso salve o cadastro.

![Imagem 3: Tela ' Tipos de Operação - TOP ' (Caminho de acesso: Comercial » Arquivo » Cadastros), a ba " Livro Fiscal " , campo…](https://ajuda.sankhya.com.br/hc/article_attachments/17378762012183) Tela '[**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)' (Caminho de acesso: Comercial » Arquivo » Cadastros), aba **"[Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)"**, campo Atualização de Livro ICMS:

![Top](https://ajuda.sankhya.com.br/hc/article_attachments/15532393776663)

**(2)** **Não atualiza:** As operações que utilizam esta TOP não atualizam o Módulo de Livros Fiscais.

**(2)** **Livro de entrada:** As operações que utilizam esta TOP atualizam o Módulo de Livros Fiscais, movimento de entrada.

**(2)** **Livro de saída:** As operações que utilizam esta TOP atualizam o Módulo de Livros Fiscais, movimento de saída.

**(2)** **Ambos:** As operações que utilizam esta TOP atualizam o Módulo de Livros Fiscais, movimentos de entrada e saída. Pode ser utilizado para transferências.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16310494161687) CAUSA:**

Caso o campo Tipo de Movimento seja diferente da Transferência, não poderá ser utilizada a opção Ambos no campo Atualização de Livro de ICMS.
