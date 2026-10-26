---
id: "44011290458391"
titulo: "[TMS] - Erro ao Clonar Tabela de Frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011290458391--TMS-Erro-ao-Clonar-Tabela-de-Frete"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:00:54Z"
rotulos: ["sync_hc", "lincros", "sync_hash_34c21f63b1bb", "lincros_13438773"]
---

# [TMS] - Erro ao Clonar Tabela de Frete

**1 - Problema Relatado pelo Cliente:**O cliente informou que o sistema não está permitindo a clonagem da tabela de frete. Não foi especificada uma mensagem de erro, mas a funcionalidade não está disponível para execução.

![Imagem 1: 1 - Problema Relatado pelo Cliente: O cliente informou que o sistema não está permitindo a clonagem da tabela de frete.…](https://ajuda.sankhya.com.br/hc/article_attachments/44011258553495)

## 2 - Motivo do Problema

O sistema impede a clonagem da tabela porque **já existe uma versão clonada**.

🔹 **Padrão de Nomeação:** Quando uma tabela de frete é clonada, o sistema cria automaticamente uma nova tabela seguindo este formato:
➡ **Nome da Tabela + (Clonada)**

Se uma tabela já foi clonada anteriormente com esse padrão de nome, o sistema não permite uma nova clonagem até que a tabela existente seja **renomeada ou excluída**.

---

## 3 - Como Resolver o Problema

✔ **Passo 1: Verificar se a tabela já foi clonada**

1. Acesse o sistema e localize a tabela de frete em:
   **Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete**
2. Verifique se já existe uma tabela com o nome no formato **"(Clonada)"**.

![Imagem 2: Verifique se já existe uma tabela com o nome no formato "(Clonada)" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011321468567)

✔ **Passo 2: Renomear ou Excluir a Tabela Clonada**
Se já houver uma tabela clonada, siga uma das opções abaixo:

➡ **Opção 1: Renomear a Tabela Clonada**

1. Acesse o gerenciamento de tabelas de frete.
2. Edite a tabela clonada e altere o nome dela, removendo ou modificando a parte **"(Clonada)"**.

➡ **Opção 2: Excluir a Tabela Clonada**

1. Se a tabela clonada não for mais necessária, exclua-a do sistema.
2. Após a exclusão, tente realizar a clonagem novamente.

---

✔ **Passo 3: Validar a Nova Clonagem**

1. Após renomear ou excluir a tabela clonada anterior, tente realizar a clonagem novamente.
2. Verifique se a nova tabela foi criada corretamente e se está disponível para uso.

---

## 4 - Caso o Problema Persista

Se mesmo após seguir esses passos a clonagem ainda não for permitida, entre em contato com o suporte técnico para uma análise mais detalhada.
