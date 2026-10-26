---
id: "42951001115031"
titulo: "Playground de estudos: visão geral e utilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951001115031-Playground-de-estudos-vis%C3%A3o-geral-e-utiliza%C3%A7%C3%A3o"
trilha: "MITRA: Planejamento orçamentário  > Playground"
atualizado_em: "2026-08-24T13:48:46Z"
rotulos: ["sync_hc", "mitra", "sync_hash_7ea39116f1ce", "mitra_16"]
---

# Playground de estudos: visão geral e utilização

## Playground de estudos: visão geral e utilização

**Módulo:** Playground

### O que é e para que serve

O Playground é o espaço de análises livres sobre os dados do orçamento. Cada **estudo** combina consultas aos dados com um canvas de apresentação, e pode ser construído em conversa com o agente de IA do produto.

### Recursos

| Recurso | O que faz |
| --- | --- |
| Criar estudo | Abre um estudo vazio vinculado ao usuário |
| Consultas seguras | Executa consultas **somente de leitura** sobre os dados (apenas SELECT, uma instrução por vez, com limite de linhas) |
| Canvas versionado | Cada alteração salva do canvas gera uma versão; é possível listar e **restaurar** versões anteriores |
| Renomear | Dá nome ao estudo para organização |
| Compartilhar | Gera um link público com token para leitura do estudo por quem não tem acesso ao aplicativo |
| Excluir | Remove o estudo da lista (exclusão reversível no banco) |

### Comportamentos e pontos de atenção

- **Somente leitura:** o Playground não altera dados do orçamento — as consultas são bloqueadas para qualquer operação de escrita.
- **Compartilhamento é público:** quem tiver o link com token vê o estudo sem login. Não inclua dados sensíveis em estudos compartilhados.
- A conversa com o agente fica registrada no estudo, permitindo retomar o raciocínio depois.

### Resultado esperado

Estudos salvos por usuário, com histórico de versões do canvas e possibilidade de compartilhar análises pontuais sem expor o aplicativo.

---

### Pendências para validação

1. Confirmar rótulos da tela (botões de novo estudo, compartilhar, versões).
2. Confirmar o limite exato de linhas das consultas exibido ao usuário.
