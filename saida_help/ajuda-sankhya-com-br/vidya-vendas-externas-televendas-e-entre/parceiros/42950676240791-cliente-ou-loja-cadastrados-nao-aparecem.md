---
id: "42950676240791"
titulo: "Cliente ou Loja Cadastrados não Aparecem na Listagem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950676240791-Cliente-ou-Loja-Cadastrados-n%C3%A3o-Aparecem-na-Listagem"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Parceiros"
atualizado_em: "2026-08-24T17:00:15Z"
rotulos: ["sync_hc", "vidya", "sync_hash_fb75877ca8ee", "vidya_593596"]
---

# Cliente ou Loja Cadastrados não Aparecem na Listagem

📌 **Sintoma do Erro**
O vendedor tenta iniciar um atendimento ou vincular uma venda, mas não consegue localizar um cliente ou loja específica na listagem do aplicativo, mesmo sabendo que o parceiro já foi cadastrado no sistema corporativo.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Listagem de Clientes** | Tela de pesquisa de parceiros vazia ou omitindo o nome/razão social do cliente desejado após a digitação dos dados de busca. |

🕵️‍♂️ **Causas Mais Comuns**

- **Ausência de Sincronização:** O parceiro foi incluído ou alterado no sistema recentemente, mas o smartphone do vendedor ainda não importou o novo pacote de dados.
- **Parceiro Inativo:** O cliente está marcado com o status de inativo dentro do ERP Sankhya.
- **Bloqueio de Carteira:** O cliente existe e está ativo, mas não foi formalmente associado ou vinculado à carteira de clientes daquele vendedor específico no ERP.
- **Grupo de Produtos Incompleto:** Configurações estruturais incompletas no ERP, como grupos de produtos sem o campo "Natureza" preenchido.
- **Interrupção de Carga:** O vendedor fechou ou minimizou o aplicativo antes que a sincronização de rotina fosse 100% concluída.

🛠 **Como Corrigir o Problema**

1. **Forçar Recebimento de Dados:** No Vidya Force, oriente o vendedor a tocar no ícone de sincronização (no topo da tela), aguardar o término total do processo sem fechar o app e buscar o cliente novamente.
2. **Ativação no Sankhya:** Acesse o cadastro do parceiro no ERP Sankhya e confirme se ele está marcado como **"Ativo"**. Caso esteja inativo, faça a reativação e peça para o vendedor sincronizar o celular.
3. **Vínculo de Carteira:** No cadastro do vendedor dentro do Sankhya, acesse a aba "Parceiros" ou "Carteira de Clientes" e certifique-se de que o cliente em questão está presente na lista. Se não estiver, adicione-o manualmente e salve.
4. **Correção de Natureza de Grupo:** Se o sumiço estiver atrelado a produtos de grupos específicos, revise o cadastro do grupo no ERP e garanta que o campo "Natureza" esteja preenchido corretamente.

💡 **Quando abrir chamado para a VidyaCode**

- Se o cliente estiver ativo e devidamente vinculado à carteira do vendedor no Sankhya, a sincronização terminar com sucesso e mesmo assim o parceiro sumir do app.
- Quando a falha de visualização de clientes afetar toda a força de vendas de maneira simultânea.
- Se o aplicativo disparar mensagens de erro explícitas na tela durante o processo de sincronização.
- Se o problema persistir por mais de 2 horas após todas as correções cadastrais terem sido aplicadas no ERP.
