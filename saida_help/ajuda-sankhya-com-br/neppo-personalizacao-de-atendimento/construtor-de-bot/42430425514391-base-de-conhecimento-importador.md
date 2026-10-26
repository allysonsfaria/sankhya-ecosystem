---
id: "42430425514391"
titulo: "Base de Conhecimento - Importador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430425514391-Base-de-Conhecimento-Importador"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T17:04:04Z"
rotulos: ["sync_hc", "neppo", "neppo_857999909", "sync_hash_f38303de6a3c"]
---

# Base de Conhecimento - Importador

Esta documentação detalha o módulo de Base de Conhecimento, focado em aumentar a autonomia do usuário ao permitir a gestão de fontes estáticas e dinâmicas, upload de múltiplos arquivos e URLs em uma mesma base, e agendamento de atualizações.

[GIF animado: Imagem 1: Esta documentação detalha o módulo de Base de Conhecimento, focado em aumentar a autonomia do usuário ao permitir a…](https://ajuda.sankhya.com.br/hc/article_attachments/42639687314071)

O importador de Base de Conhecimento está localizado em:

**Menu -> Construtor de bot (Studio CX) → Configurações → Importar Base de Conhecimento**

Índice:

- [1. Visão geral da funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430425514391-Base-de-Conhecimento-Importador#1-Visao-geral-da-funcionalidade)
- [2. Gestão e listagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430425514391-Base-de-Conhecimento-Importador#2-Gestao-e-listagem)

Navegue também:
Como importar fontes

---

## 1. Visão geral da funcionalidade

A base de conhecimento pode ser gerada pela interface da plataforma a partir de duas formas:

1. Upload de arquivos
2. Importação por URL

Depois que a fonte é enviada, o processo segue, em alto nível, estas etapas:

1. O sistema valida se a fonte pode ser acessada.
2. O sistema valida se o formato é suportado.
3. O conteúdo é lido e transformado em blocos de conhecimento.
4. Esses blocos são preparados para geração de embeddings.
5. Os embeddings são gerados e indexados.
6. A base passa a poder ser usada pelo assistente nas respostas.
7. A qualidade do resultado depende diretamente de dois fatores:

- a validade técnica da fonte importada;
- a organização do conteúdo dentro dessa fonte.

Não basta o arquivo ser aceito. Ele também precisa estar bem estruturado para que o sistema consiga dividir o conteúdo de forma coerente e recuperar a informação correta depois.

---

## 2. Gestão e listagem

Esta tela oferece a visão geral e a governança das suas bases de conhecimento.

![Imagem 2: Esta tela oferece a visão geral e a governança das suas bases de conhecimento.](https://ajuda.sankhya.com.br/hc/article_attachments/42639749783959)

1. **Ações Globais:**

- **Barra de pesquisa:** Utilize para realizar buscas rápidas pelo nome da base.
- **Botão "+ Nova Base":** Inicia o fluxo de criação de uma nova base de dados.

2. **Tabela de Dados:**

| Coluna | Descrição |
| --- | --- |
| **Nome** | Identificação principal da base |
| **Início da última importação** | Registra a ultima data e hora que a base foi atualizada. |
| **Status da última importação** | Mostra o estado atual do processamento da base. |
| **Duração da última importação** | Permite visualizar quanto tempo a base levou para ser gerada. |
| **Alterada por** | Oferece rastreabilidade e auditoria, registrando qual foi o usuário que gerou a base. |
| **Alterada em** | Registra a data e hora que a base de conhecimento teve alteração. |
| **Status** | Permite ativar ou desativar\* a base. |
| **Ações** | **Ícone de Lápis (Editar):** Redireciona para a tela de configurações da base. |
| **Ícone de Lixeira (Excluir):** Exclui a base de conhecimento. Uma mensagem de aviso pedirá confirmação antes da ação irreversível. |
| **Ícone de Play (Executar):** Força uma sincronização e reimportação manual dos dados instantaneamente. |

Desativar uma base faz com que o bot pare de responder com base nesses dados instantaneamente.

- **Navegação:** Utilize a paginação no rodapé para controlar a quantidade de "Linhas por página" visualizadas.

---

Índice:

- [1. Visão geral da funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430425514391-Base-de-Conhecimento-Importador#1-Visao-geral-da-funcionalidade)
- [2. Gestão e listagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/42430425514391-Base-de-Conhecimento-Importador#2-Gestao-e-listagem)

Navegue também:
Como importar fontes
