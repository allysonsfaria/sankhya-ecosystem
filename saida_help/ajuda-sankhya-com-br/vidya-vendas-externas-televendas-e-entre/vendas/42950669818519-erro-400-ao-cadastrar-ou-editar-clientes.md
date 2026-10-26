---
id: "42950669818519"
titulo: "Erro 400 ao Cadastrar ou Editar Clientes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950669818519-Erro-400-ao-Cadastrar-ou-Editar-Clientes"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:09:08Z"
rotulos: ["sync_hc", "vidya", "vidya_593603", "sync_hash_17eee86ad20b"]
---

# Erro 400 ao Cadastrar ou Editar Clientes

📌 **Sintoma do Erro**
O vendedor tenta preencher o formulário para criar um novo cliente ou alterar dados de um parceiro existente, mas o aplicativo bloqueia o salvamento exibindo uma mensagem de falha de protocolo (este erro afeta apenas cadastros, as vendas continuam funcionando normalmente).

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Formulário de Cadastro** | Pop-up de erro contendo a mensagem exata: "Erro ao salvar cliente - Request failed with status code 400". |

🕵️‍♂️ **Causas Mais Comuns**

- **Cache de Sincronização Defasado:** Inconsistência temporária nos arquivos de validação local do aplicativo.
- **Invalidez de Documento:** O CNPJ ou CPF digitado pelo vendedor possui erros, está inativo ou não foi localizado na base de dados da Receita Federal.
- **Inconsistência de Endereço:** O CEP digitado não retorna dados ou o bairro informado não possui correspondência/cadastro prévio nas tabelas do ERP.

🛠 **Como Corrigir o Problema**

1. **Ciclo de Login Limpo:** Vá no menu lateral do aplicativo, acesse a aba **Perfil**, clique em **"Sair"** e aguarde o encerramento total. Abra o app, insira o usuário/senha e aguarde a sincronização inicial terminar para limpar o cache.
2. **Refazer a Operação:** Com o cache higienizado, tente realizar o cadastro ou edição novamente.
3. **Coleta de Evidências:** Se o erro persistir, tire um print da mensagem de erro e anote o CPF ou CNPJ do parceiro que está gerando a falha para análise técnica.

💡 **Quando abrir chamado para a VidyaCode**

- Se o Erro 400 continuar travando a tela mesmo após o procedimento completo de deslogar e logar no aplicativo.
- Quando o documento (CPF/CNPJ) estiver comprovadamente correto e ativo na Receita Federal, mas o app falhar em puxar os dados automatizados.
- Se o cadastro for concluído no aplicativo, mas o parceiro nunca aparecer sincronizado nas tabelas do ERP Sankhya.
- Casos de cadastros duplicados (um mesmo CPF/CNPJ gerando múltiplos códigos de parceiro no ERP) ou quando contatos de entrega anexados ao pedido não forem transmitidos ao Sankhya.
