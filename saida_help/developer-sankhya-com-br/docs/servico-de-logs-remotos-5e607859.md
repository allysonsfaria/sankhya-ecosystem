---
id: "https://developer.sankhya.com.br/docs/serviço-de-logs-remotos"
titulo: "📡Serviço de Logs Remotos"
url: "https://developer.sankhya.com.br/docs/serviço-de-logs-remotos"
atualizado_em: "2026-02-24T18:50:41.000Z"
---

# 📡Serviço de Logs Remotos

<br />

> ⚠️ **Acesso Antecipado (Beta)**
>
> Esta documentação refere-se a uma versão em acesso antecipado do **SDK Sankhya**. As funcionalidades e APIs estão sujeitas a modificações. Para obter acesso, envie um e-mail para <developer@sankhya.com.br> informando a **`appkey`** do seu projeto.

# 📡Serviço de Logs Remotos

***

## Visão Geral

O serviço de logs remotos permite que aplicações que utilizam o **SDK Sankhya** enviem logs de maneira centralizada para análise, auditoria e monitoramento.

Essa abordagem evita que cada aplicação mantenha sua própria infraestrutura de logs e facilita:

* Monitoramento de erros em produção
* Auditoria de operações críticas
* Detecção de comportamentos anômalos
* Suporte técnico e diagnóstico

***

## Como Funciona

Quando a funcionalidade está habilitada para o projeto:

1. O SDK intercepta mensagens enviadas pelos loggers suportados.
2. Os logs são normalizados e enriquecidos com contexto (quando disponível), como usuário, transação, módulo, etc.
3. Os logs são enviados para o serviço remoto de armazenamento e análise.

Não é necessário alterar o código que já faz logging — a configuração ocorre automaticamente.

***

## Loggers Suportados

Atualmente, os seguintes loggers são compatíveis com o serviço de logs remotos:

| Framework               | Suporte     | Observação                      |
| ----------------------- | ----------- | ------------------------------- |
| Log4J 1.x               | ✅ Suportado | Versões anteriores ao Log4J2    |
| JUL (java.util.logging) | ✅ Suportado | Configuração automática via SDK |

***

## Ativação

A ativação é **automática** para projetos aprovados no programa Beta. Nenhuma configuração manual adicional é necessária.

Para verificar se o serviço está ativo:

* Gere um log de nível `INFO` ou superior em sua aplicação.
* Consulte o painel de observabilidade disponibilizado pela Sankhya ou solicite confirmação ao suporte.

***

## Recomendações de Uso

Para aproveitar o serviço de logs remotos de forma eficiente:

* Utilize níveis de log de maneira consistente (ex.: `ERROR` para exceções reais).
* Inclua contexto útil (ex.: ID de pedido, usuário, etapa do processo).
* Evite logar objetos grandes ou dados sigilosos.

**Consequência de má utilização:**
Logs excessivos podem aumentar custos e dificultar a análise, além de impactar a performance da aplicação.

***

## Condições de Uso

O serviço de logs remotos não é habilitado automaticamente para todos os projetos. Para garantir estabilidade, capacidade e segurança, existem condições e regras para utilização:

* É necessário configurar o componente de logs na Área do Desenvolvedor para habilitar o recebimento.

Após a aprovação, o serviço é ativado sem alterações no código, desde que o projeto utilize um dos loggers suportados.
