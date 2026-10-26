---
id: "42950664033687"
titulo: "Vendedor não Consegue Acessar o App (Problemas de Login)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950664033687-Vendedor-n%C3%A3o-Consegue-Acessar-o-App-Problemas-de-Login"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Vendedor"
atualizado_em: "2026-08-24T16:08:03Z"
rotulos: ["sync_hc", "vidya", "vidya_593584", "sync_hash_f8225652c46f"]
---

# Vendedor não Consegue Acessar o App (Problemas de Login)

📌 **Sintoma do Erro**
O vendedor insere suas credenciais na tela inicial do aplicativo, mas é impedido de entrar devido a mensagens de erro na validação ou travamentos no fluxo de carregamento.

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Tela de Login / Entrada** | Indicador circular de carregamento travado infinitamente ou alertas com avisos textuais de erro de conexão, token inválido ou falha de autenticação. |

🕵️‍♂️ **Causas Mais Comuns**

- **Usuário Vencido/Inativo:** O cadastro do vendedor dentro do ERP Sankhya está marcado como inativo ou a sua data limite de expiração foi ultrapassada.
- **Digitação Incorreta:** Erros ao digitar maiúsculas, minúsculas ou espaços invisíveis inseridos pelo corretor do celular no campo de senha.
- **Falta de Diretriz de Servidor:** Os parâmetros lógicos de apontamento do Servidor da empresa não foram inseridos ou foram limpos do aplicativo.
- **Direitos de Acesso:** O funcionário possui login para usar o computador na empresa, mas não recebeu a liberação de acesso ao módulo específico do Vidya Force no ERP.

🛠️ **Como Corrigir o Problema**

1. **Reinicialização do App:** Force o encerramento completo do aplicativo (remova-o da lista de apps abertos em segundo plano) e tente logar novamente após 1 minuto para descartar instabilidades de rede.
2. **Auditoria de Status (ERP):** Acesse o cadastro do usuário vendedor dentro do Sankhya e valide se a flag **"Ativo"** está marcada e se o campo de data de expiração não está vencido.
3. **Revisar Parâmetros:** Certifique-se de que os dados de servidor e filial da empresa estão devidamente preenchidos nas configurações de inicialização do app.
4. **Reset de Senha:** Caso o erro persista, gere uma nova senha temporária direto no Sankhya (ex: `123456`) e peça para o vendedor tentar o acesso com a nova credencial.

💡 **Quando abrir chamado para a VidyaCode**

- Se o usuário estiver ativo e com todas as permissões comerciais validadas no Sankhya, mas o login seguir rejeitado.
- Se a mensagem em tela citar falhas de infraestrutura como "problema de token" ou "servidor não encontrado" com a internet do celular funcionando perfeitamente.
- Caso vários vendedores percam o acesso simultaneamente.
