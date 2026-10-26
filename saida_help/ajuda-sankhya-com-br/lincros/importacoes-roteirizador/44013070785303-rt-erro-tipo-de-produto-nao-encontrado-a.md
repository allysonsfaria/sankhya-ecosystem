---
id: "44013070785303"
titulo: "[RT] - Erro \"Tipo de Produto Não Encontrado\" ao Importar Pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013070785303--RT-Erro-Tipo-de-Produto-N%C3%A3o-Encontrado-ao-Importar-Pedidos"
trilha: "Lincros > Roteirizador > Importações - Roteirizador"
atualizado_em: "2026-10-05T19:47:11Z"
rotulos: ["sync_hc", "lincros", "sync_hash_16ad3703a969", "lincros_13432981"]
---

# [RT] - Erro "Tipo de Produto Não Encontrado" ao Importar Pedidos

## 1. Problema Relatado pelo Cliente

O cliente relatou que, ao tentar importar pedidos em seu depósito, o processo foi interrompido devido ao erro "Tipo de produto não encontrado." Esse erro ocorre porque o tipo de produto associado aos pedidos não está previamente cadastrado na base do sistema.

---

## 2. Passo a Passo para Resolver o Problema

O erro "Tipo de produto não encontrado" ocorre quando um pedido é importado para o sistema com um tipo de produto que não está cadastrado. Para corrigir isso, é importante que seu usuário seja **Manager** ou possua permissão de acesso ao menu de cadastros. Caso possua alguma dessas permissões, siga as etapas abaixo para cadastrar corretamente os tipos de produto:

1. **Acessar o menu de cadastros**:

   - Navegue até o menu **Cadastros** no sistema.
2. **Selecionar Tipos de Produto**:

   - Dentro de **Cadastros**, selecione a opção **Tipos de Produto**.
3. **Criar Novo Tipo de Produto**:

   - Clique em **Novo** para criar um novo tipo de produto.
4. **Preencher as Informações do Tipo de Produto**:

   - **Depósito**: Selecione o depósito.
   - **Descrição**: Informe a descrição do tipo de produto.
   - **Identificador**: Forneça um identificador para o tipo de produto.

     ![Imagem 1: Identificador : Forneça um identificador para o tipo de produto.](https://ajuda.sankhya.com.br/hc/article_attachments/44013062780439)
5. **Confirmar o Cadastro**:

   - Após preencher as informações, clique em **Confirmar** para salvar o tipo de produto.
6. **Repetir o Processo para Todos os Tipos de Produto**:

   - Realize o cadastro de todos os tipos de produto ausentes, conforme necessário.
7. **Tentar Novamente a Importação dos Pedidos**:

   - Após cadastrar todos os tipos de produtos, tente novamente importar os pedidos e realizar a roteirização.

Seguindo esses passos, a importação dos pedidos será bem-sucedida.

---

Este procedimento garantirá que todos os tipos de produto necessários estejam devidamente cadastrados no sistema, permitindo a importação correta dos pedidos que geraram erro.
