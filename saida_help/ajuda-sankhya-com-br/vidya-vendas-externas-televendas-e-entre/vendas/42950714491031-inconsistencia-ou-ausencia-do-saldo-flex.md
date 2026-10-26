---
id: "42950714491031"
titulo: "Inconsistência ou Ausência do Saldo Flex"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950714491031-Inconsist%C3%AAncia-ou-Aus%C3%AAncia-do-Saldo-Flex"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendas"
atualizado_em: "2026-08-24T16:08:51Z"
rotulos: ["sync_hc", "vidya", "vidya_593599", "sync_hash_517531caf30a"]
---

# Inconsistência ou Ausência do Saldo Flex

📌 **Sintoma do Erro**
O vendedor tenta aplicar descontos ou acréscimos utilizando a margem do saldo Flex durante a negociação de um item, mas os percentuais em tela aparecem errados, divergentes do configurado no ERP, ou o recurso fica totalmente indisponível para uso.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Tela de Vendas (Item / Desconto)** | Valores de margem Flex zerados, ausência do campo de aplicação do saldo ou pop-ups bloqueando a ação comercial. |

🕵️‍♂️ **Causas Mais Comuns**

- **Conflito de Hierarquia de Regras:** Existe uma configuração Flex no produto, mas o cadastro do vendedor no ERP possui outra regra diferente — **o aplicativo sempre prioriza o cadastro do vendedor**.
- **Carga de Dados Retida:** Modificações de tabelas feitas no Sankhya que ainda não foram importadas pelo aplicativo de força de vendas.
- **Limitação de Licenciamento:** O módulo comercial Flex não está ativo ou contratado no plano atual da empresa.
- **Quebra de Vínculo de Carteira:** Tentativa de aplicação do saldo Flex em um cliente que não pertence à carteira oficial do vendedor no ERP.

🛠 **Como Corrigir o Problema**

1. **Auditoria de Hierarquia no ERP:** Acesse o cadastro do vendedor dentro do ERP Sankhya e verifique os limites de desconto e acréscimo configurados diretamente no usuário dele, ajustando-os conforme o esperado.
2. **Sincronização de Perfil:** No smartphone do vendedor, acesse o caminho **Perfil → Sincronizar dados** e aguarde o processamento completo dos novos limites.
3. **Cenário de Teste:** Abra um novo pedido real de teste para checar se as novas margens e percentuais do vendedor foram assumidas pela tela de vendas.

💡 **Quando abrir chamado para a VidyaCode**

- Se o vendedor possuir o vínculo correto do cliente em sua carteira e mesmo assim o Flex continuar bloqueado ou exibindo percentuais errados após a sincronização.
- Caso a tentativa de acionar o recurso retorne mensagens de erro técnico do sistema (diferentes do aviso padrão de "funcionalidade não contratada").
- Se as bonificações geradas a partir do saldo Flex não estiverem subindo para o ERP mesmo após restaurar e refazer o pedido.
