---
id: "27998821987863"
titulo: "Criar/Alterar Registro - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27998821987863-Criar-Alterar-Registro-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Ações e automações"
atualizado_em: "2026-09-23T17:37:42Z"
rotulos: ["Configuração", "Parceiro", "Atualização", "Cadastro", "Analytics Studio", "ID"]
---

# Criar/Alterar Registro - Analytics Studio

O passo Criar/Alterar Registro permite adicionar novos registros ou modificar registros existentes em um cadastro específico. Ele é ideal para operações de inserção e atualização de dados de forma automatizada e controlada.

![Imagem 1: O passo Criar/Alterar Registro permite adicionar novos registros ou modificar registros existentes em um cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/28106725891095)

### Configuração inicial

**Escolha do Cadastro:** primeiro, selecione o cadastro onde os registros serão criados ou alterados. Esse cadastro determina a estrutura dos dados que serão manipulados.

**Método de Transformação:** escolha entre utilizar uma query SQL ou uma das views no-code do [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio) (VIEW de Análise de Dados ou VIEW de Cadastro) para definir os dados que serão processados.

### Definição da chave de alteração

**Chave de alteração:** decida se os registros afetados serão novos ou se deseja alterar registros existentes.

**Opções de chave:**

- **ID:** use o ID como chave para identificar e modificar registros específicos. Esta opção é obrigatória para cadastros com ID inteiro ou varchar.
- **Descrição:** como alternativa, pode-se utilizar a descrição como chave de alteração, dependendo da estrutura do cadastro.

### Mapeamento de atributos

Após definir a query ou a view que retornará os dados, é necessário mapear as colunas do resultado aos atributos do cadastro selecionado.

**Mapeamento de colunas:** as colunas da query ou view serão listadas, e é possível associá-las aos atributos correspondentes do cadastro. Por exemplo, ao trabalhar com o cadastro **"Parceiros"**, que possui atributos como **"ID"**, **"Descrição"**, **"Valor Mensalidade"**, e **"Data de Entrada"**, cada coluna do resultado pode ser mapeada para o respectivo atributo.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=iXqJKZSWBmc)

**Importante:**

- **Adição de Membros em Cadastros com ID Auto-Incremental:** para cadastros com ID autoincremental, o campo ID não será mapeável, pois o sistema gerará o ID automaticamente.
- **Adição de Membros em Cadastros com ID Inteiro ou Varchar:** nesses casos, o ID deve ser fornecido e mapeado obrigatoriamente.
- **Edição de Membros Existentes:** quando a chave de alteração for o ID, será necessário mapear o campo ID do cadastro específico para garantir que os registros corretos sejam alterados.

### Log de execução

O passo Criar/Alterar Registros possui um log detalhado que acompanha todas as execuções, incluindo:

- **Usuário Executor:** quem iniciou a ação.
- **Data e Hora:** quando a ação foi executada.
- **Tempo de Execução:** duração da operação.
- **Resumo:** exibe o que foi aceito ou rejeitado durante o processo.
- **Motivos das Rejeições:** detalha os motivos pelos quais determinados registros não foram processados, permitindo correções e ajustes.

---

![Imagem 2: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157471156375) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
