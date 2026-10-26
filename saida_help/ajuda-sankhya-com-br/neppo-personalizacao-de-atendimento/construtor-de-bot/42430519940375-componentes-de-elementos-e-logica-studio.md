---
id: "42430519940375"
titulo: "Componentes de Elementos e Lógica - Studio CX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430519940375-Componentes-de-Elementos-e-L%C3%B3gica-Studio-CX"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:13:05Z"
rotulos: ["sync_hc", "neppo", "neppo_858000290", "sync_hash_97372a3c22f0"]
---

# Componentes de Elementos e Lógica - Studio CX

O **Construtor de Bots do Studio CX** (Plataforma Neppo Omnichannel) disponibiliza uma paleta de componentes no menu lateral direito da Área do Construtor. Esses componentes são os blocos de construção dos fluxos conversacionais: cada um representa uma ação executada pelo bot — enviar mensagens, capturar dados, consultar APIs, aplicar regras de negócio e controlar o encerramento da sessão.

Esta documentação cobre os componentes das categorias **Elementos** e **Lógica**, que formam o núcleo de qualquer fluxo.

---

## Categorias da paleta do construtor

| Categoria | Componentes | Finalidade |
| --- | --- | --- |
| **IA** | OpenAI, Assistente, Fala para texto, Texto para fala, Base de Conhecimento | Recursos de inteligência artificial (LLM, transcrição, RAG) |
| **Elementos** | Texto, Entrada de Dados, Anexo, Menu de Opções | Interação direta com o usuário (enviar e receber conteúdo) |
| **Lógica** | Requisitar API, Neppo API, Redirecionar, Executar Script, Esperar, Condicionar, Para JSON, Iteração, Expressão, Validar, Executar, Sair | Processamento, integrações, decisões e controle de fluxo |
| **Voz** | Componentes marcados com a tag Voz | Recursos específicos de canais de voz |
| **WhatsApp** | Componentes marcados com a tag WhatsApp (ex.: Mensagem Interativa do Menu de Opções) | Recursos exclusivos do canal WhatsApp |
| **Google Agenda** | Buscar/Criar eventos | Integração com agendas Google |
| **Sankhya** | Dados do Cliente, Busca de Produto, Criar Pedido, entre outros | Componentes inteligentes integrados ao ERP Sankhya (ver [Componentes Sankhya](https://sankhya.zendesk.com/hc/pt-br/articles/42430315125271)) |

---

## Conceitos comuns a todos os componentes

- **Variáveis**: a interpolação é feita com a sintaxe `{{variavel}}`. Variáveis são locais por fluxo e passadas adiante como argumentos ao chamar outros fluxos.
- **Variáveis globais de sessão**: `{{firstMessage.message}}`, `{{firstMessage.group}}`, `{{firstMessage.originUser}}`, `{{firstMessage.sessionId}}`, `{{firstMessage.externalProtocol}}`; dados do contato em `{{contact.*}}` (id, userName, displayName, cpf, email, phone etc.); credenciais do Neppo Vault em `{{config.<diretório>.<credencial>}}` (resolvidas somente em runtime).
- **Variável de escopo global**: componentes que armazenam retorno podem marcar a variável como global, tornando-a acessível em todos os fluxos da sessão.
- **Encadeamento**: componentes que desviam o fluxo apontam para um fluxo de destino e podem enviar argumentos (variáveis) junto.

---

## Índice dos componentes documentados

### Elementos

| Componente | Resumo |
| --- | --- |
| Componente Texto | Envia uma mensagem de texto (ou arquivo por URL) ao usuário |
| Componente Entrada de Dados | Faz uma pergunta e armazena a resposta do usuário em uma variável |
| Componente Anexo | Envia um arquivo (imagem, documento, áudio, vídeo) com legenda, até 15 MB |
| Componente Menu de Opções | Apresenta opções (menu padrão ou mensagem interativa de WhatsApp) e desvia o fluxo conforme a escolha |

### Lógica

| Componente | Resumo |
| --- | --- |
| Componente Requisitar API | Executa requisição REST a APIs externas e armazena o retorno |
| Componente Neppo API | Requisição autenticada à API interna da plataforma Neppo (Chat API) |
| Componente Redirecionar | Transfere o atendimento para grupo, agente, fluxo, fila de espera ou pesquisa de satisfação |
| Componente Executar Script | Executa código JavaScript e disponibiliza o retorno em variável |
| Componente Esperar | Pausa o fluxo por um tempo determinado (timer em variável) |
| Componente Condicionar | Avalia múltiplas condições (Se/Condição/Valores) e desvia para o fluxo correspondente |
| Componente Para JSON | Converte uma string JSON (ex.: retorno de API) em objeto navegável |
| Componente Iteração | Percorre uma lista e executa um fluxo para cada item |
| Componente Expressão | Avalia expressão condicional (verdadeiro/falso) ou expressão JavaScript com resultado em variável |
| Componente Validar | Valida a entrada do usuário por tipo (CPF, CNPJ, números etc.) com desvios válido/inválido |
| Componente Executar | Chama outro fluxo como sub-rotina, passando argumentos |
| Componente Sair | Encerra definitivamente a sessão de atendimento |

---

> As páginas filhas desta documentação detalham cada componente com campos de configuração, comportamento, exemplo real de uso (jornada de matrícula escolar de um bot em produção) e boas práticas.
