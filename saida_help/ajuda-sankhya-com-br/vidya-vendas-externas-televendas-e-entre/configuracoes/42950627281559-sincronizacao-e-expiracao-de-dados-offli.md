---
id: "42950627281559"
titulo: "Sincronização e Expiração de Dados Offline"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950627281559-Sincroniza%C3%A7%C3%A3o-e-Expira%C3%A7%C3%A3o-de-Dados-Offline"
trilha: "VIDYA: Vendas externas, televendas e entregas > Configurações"
atualizado_em: "2026-08-24T16:59:33Z"
rotulos: ["sync_hc", "vidya", "vidya_593582", "sync_hash_ea82924ac6cc"]
---

# Sincronização e Expiração de Dados Offline

📌 **Sintoma do Erro**
A equipe de vendas externa fica sem acesso a informações cruciais (como tabelas de preços e estoques atualizados) ao entrar em zonas sem cobertura de internet, ou o aplicativo exige sincronizações repetitivas de forma inconveniente.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Painel Web (Administração)** | Campos de controle de parâmetros em texto e chaves seletoras (toggles) para configuração de rotinas automatizadas de dados. |

🕵️‍♂️ **Causas Mais Comuns**

- **Parâmetro Desconfigurado:** O campo que determina o tempo de vida dos dados offline no celular está zerado ou sem preenchimento.
- **Inércia de Inicialização:** A opção de varredura automática ao abrir o software está desligada.
- **Falha de Atualização Local:** O vendedor não abriu o aplicativo conectado à internet após a alteração dos parâmetros no painel.

🛠️ **Como Corrigir o Problema**

1. **Acesso Administrativo:** Logue na interface web de administração do Vidya Force.
2. **Localizar Parâmetros:** Navegue até a seção de **Parâmetros de Sincronização**.
3. **Estipular Prazo Offline:** Localize o parâmetro **"Tempo para dados offline"** e digite o número de **horas** que os dados poderão ser consultados sem internet antes de expirar.
4. **Ativar Gatilho de Entrada:** Ligue a chave seletora **"Sincronizar ao iniciar"** para que o app busque atualizações toda vez que for aberto.
5. **Propagação da Regra:** Salve as alterações e peça para os vendedores abrirem e fecharem o aplicativo uma vez enquanto estiverem conectados à internet para baixar a nova regra.

💡 **Quando abrir chamado para a VidyaCode**

- Se as opções e parâmetros citados não estiverem visíveis ou acessíveis no seu painel web.
- Caso o aplicativo ignore o prazo configurado e continue bloqueando os dados ou exigindo sincronização antes do tempo determinado
