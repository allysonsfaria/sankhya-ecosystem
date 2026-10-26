---
id: "9472966512919"
titulo: "Não é permitido inserir item repetido. Produto XXX já existe na sequência X"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9472966512919-N%C3%A3o-%C3%A9-permitido-inserir-item-repetido-Produto-XXX-j%C3%A1-existe-na-sequ%C3%AAncia-X"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:45Z"
rotulos: ["Produtos", "Configuração", "NF-e", "TOP", "Estoque", "Preferências", "CORE_E04344", "Erro ao Inserir Item Repetido na NF-e"]
---

# Não é permitido inserir item repetido. Produto XXX já existe na sequência X

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19296909183511) MENSAGEM:**

[CORE\_E04344] Não é permitido inserir item repetido. Produto XXX já existe na sequência X.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19296909191703) SITUAÇÃO:**

Ao lançar produto repetido na NF-e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19296909195287) CAUSA:**

Ao tentar inserir um produto repetido na nota, mas a configuração da TOP e dos parâmetros não estão configurados para aceitar.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19296909199383) SOLUÇÃO:**

Acesse a tela **Preferências** (Caminho de acesso à tela: Configurações » Avançado » Preferências) e verifique se os parâmetros abaixo estão ligados:

- **ACEITARPRODREPE**-Aceitar prod.repetido para Exec.diferente?
- **ACEITARPRODREP**-Aceitar produto repetido?

![Imagem 5: ACEITARPRODREP -Aceitar produto repetido?](https://ajuda.sankhya.com.br/hc/article_attachments/19296909200279)

![Imagem 6: ACEITARPRODREP -Aceitar produto repetido?](https://ajuda.sankhya.com.br/hc/article_attachments/19296909211287)

Verifique também no cadastro do **Tipo de Operação TOP** (Caminho de acesso à tela: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) a Opção: **Aceitar Produto Repetido.**

**Importante: Na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque), o campo "Aceitar Produto Repetido" deve estar configurado igual a "Sim".**

![Imagem 7: Importante: Na aba Estoque , o campo "Aceitar Produto Repetido" deve estar configurado igual a "Sim".](https://ajuda.sankhya.com.br/hc/article_attachments/19296969815447)
