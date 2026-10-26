---
id: "42950659250199"
titulo: "Produto não Aparece no Catálogo ou na Tela de Vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950659250199-Produto-n%C3%A3o-Aparece-no-Cat%C3%A1logo-ou-na-Tela-de-Vendas"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:07:57Z"
rotulos: ["sync_hc", "vidya", "vidya_593583", "sync_hash_3730346cc44a"]
---

# Produto não Aparece no Catálogo ou na Tela de Vendas

📌 **Sintoma do Erro**
O vendedor tenta buscar por um ou vários produtos específicos no catálogo digital do Vidya Force para montar um pedido, mas o item não é localizado de forma alguma, apesar de constar como cadastrado no ERP.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Catálogo de Produtos** | Grid de produtos vazio ou exibição da mensagem padrão "Utilize o filtro para iniciar a pesquisa...", sem retornar o item desejado na busca por código ou nome. |

🕵️‍♂️ **Causas Mais Comuns**

- **Falta da Flag de Mobilidade:** O parâmetro que autoriza o produto a subir para dispositivos móveis está desativado no cadastro do ERP Sankhya.
- **Sincronização Pendente:** O item sofreu alterações de cadastro ou preço no ERP, mas o smartphone do vendedor ainda não realizou a importação dos novos dados.
- **Gargalo de Filtro:** Filtros internos de categoria ou buscas antigas retidas na barra de ferramentas ocultando o produto.
- **Falta de Espaço/Memória:** O celular do vendedor está sem armazenamento livre, o que corrompe ou interrompe a sincronização do catálogo.

🛠️ **Como Corrigir o Problema**

1. **Checagem no Sankhya:** Acesse o cadastro do produto dentro do ERP Sankhya e certifique-se de que o parâmetro de **mobilidade** está marcado. Se estiver desativado, marque-o e salve.
2. **Forçar Recebimento no App:** No Vidya Force, vá até a área de sincronização e execute o comando **"Sincronizar agora"** ou **"Forçar sincronização"**.
3. **Limpeza de Filtros:** No topo da tela do catálogo, remova todos os chips, categorias ou filtros aplicados para abrir a listagem completa.
4. **Reinstalação Limpa:** Se persistir, limpe o armazenamento do celular, desinstale o app, baixe a versão mais recente e faça uma sincronização inicial completa.

💡 **Quando abrir chamado para a VidyaCode**

- Se a flag de mobilidade estiver correta no Sankhya, a sincronização for concluída sem erros, e mesmo assim o produto sumir do app.
- Se múltiplos produtos sumirem das telas ao mesmo tempo de forma generalizada para toda a equipe de campo.
