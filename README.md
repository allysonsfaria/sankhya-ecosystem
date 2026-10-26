# 🚀 Sankhya Ecosystem — Agent Skill

Skill definitiva para desenvolvimento, arquitetura, APIs, customizações e entendimento de telas no ERP **Sankhya OM**.

Projetada para funcionar de forma nativa e automática no **Claude Code**, **OpenAI Codex**, **Antigravity (AGY)**, **Cursor**, **Windsurf** e qualquer IA compatível com a especificação de [Agent Skills](https://github.com/anthropics).

---

## 💡 O que esta Skill faz por você?

Quando instalada, a sua IA ganha conhecimento profundo e imediato sobre todo o ecossistema Sankhya:

- 🧠 **Entendimento de Telas e Regras**: Sabe exatamente como funcionam as telas nativas (*Parceiros, Central de Vendas, Financeiro, Estoque, Fiscal*), quais parâmetros influenciam e onde ficam os menus.
- ⚡ **Backend Java Assertivo**: Gera código correto para **Addon Studio 2.0** (`@ActionButton`, `@Listener`, `@Job`, `@BusinessRule`, `@Callback`) e **Módulos Java legados**.
- 🗄️ **Persistência JAPE**: Domina o framework de banco da Sankhya (`JapeSession`, `DynamicVO`, `JapeFactory.dao`, `FinderWrapper`, `NativeSql` seguro com bind parameters).
- 🌐 **APIs e Integrações**: Exemplos prontos de autenticação (`MobileLoginSP` e OAuth Gateway), consultas paginadas (`CRUDServiceProvider.loadRecords`) e mutações (`saveRecord`).
- 🎨 **Frontend & Telas**: Componentes do **Sankhya Design System (`ez-*`)**, framework legado `sankhya-js` (AngularJS) e **Campos Calculados na Grid (`#type.sql#`)**.
- 📊 **Relatórios & BI**: Regras estritas do **JasperReports 4.0.1** (iReport), NFS-e e Construtor de Componentes de BI.
- 📚 **Acervo Offline (~10.000 manuais)**: Inclui cópia local indexada de todos os manuais do *Ajuda Sankhya* e do *Portal do Desenvolvedor*.

---

## 💬 Como Usar no Dia a Dia (Exemplos de Prompts)

Você não precisa rodar comandos manuais; basta conversar normalmente com a sua IA:

| O que você quer fazer | O que dizer para a IA |
|---|---|
| **Entender uma Tela** | *"Como funciona a tela Cadastro de Parceiros no Sankhya e quais parâmetros influenciam o crédito?"* |
| **Criar Botão de Ação Java** | *"Crie um Action Button para a Central de Vendas que valida os itens da nota e altera o status para processado via JAPE."* |
| **Criar Listener / Gatilho** | *"Crie um @Listener no Addon Studio para a entidade Parceiro impedindo salvar sem CPF/CNPJ válido."* |
| **Integrar via REST / API** | *"Como faço para autenticar e consultar os últimos 50 pedidos de venda usando o loadRecords em Python/Node?"* |
| **Customizar a Grid** | *"Como crio um campo calculado com #type.sql# no Dicionário para exibir uma badge colorida de status na grade?"* |
| **Criar Relatório Formatado** | *"Quais parâmetros nativos o Sankhya passa para o JasperReports 4.0.1 na impressão da Central de Compras?"* |
| **Atualizar Manuais** | *"Atualize o acervo da documentação do Sankhya."* |

---

## ⚡ Instalação Rápida (1 Comando)

### No Windows (PowerShell):
Se você clonou este repositório em sua máquina, copie para o assistente desejado:

```powershell
# Para Claude Code:
Copy-Item -Path ".\sankhya-ecosystem" -Destination "$HOME\.claude\skills\sankhya-ecosystem" -Recurse -Force

# Para OpenAI Codex:
Copy-Item -Path ".\sankhya-ecosystem" -Destination "$HOME\.codex\skills\sankhya-ecosystem" -Recurse -Force

# Para Antigravity (AGY):
Copy-Item -Path ".\sankhya-ecosystem" -Destination "$HOME\.gemini\config\skills\sankhya-ecosystem" -Recurse -Force
```

### No Linux / macOS (Bash):
```bash
# Para Claude Code:
cp -r sankhya-ecosystem ~/.claude/skills/

# Para OpenAI Codex:
cp -r sankhya-ecosystem ~/.codex/skills/

# Para Antigravity (AGY):
cp -r sankhya-ecosystem ~/.gemini/config/skills/
```

---

## 🔍 Busca Local no Acervo (~10.000 artigos em <20ms)

A skill inclui um motor CLI ultrarrápido que pesquisa instantaneamente telas, APIs e procedimentos no acervo offline:

```bash
# Buscar uma tela ou rotina:
python scripts/search_help.py "cadastro de parceiros" -d

# Buscar especificações de APIs:
python scripts/search_help.py "loadRecords" -t api -d

# Buscar soluções de erros ou dúvidas frequentes:
python scripts/search_help.py "limite de credito" -d
```

---

## 🔄 Atualização do Acervo e Novas Fontes

O acervo é atualizado de forma **incremental** (baixa apenas o que mudou nos sites oficiais):

### 1. Atualizar todas as fontes cadastradas:
```bash
python scripts/atualizar_acervo.py
```

### 2. Adicionar um novo portal de documentação:
Edite o arquivo `fontes.json` ou execute pelo terminal:
```bash
python scripts/atualizar_acervo.py --url "https://outro-portal.sankhya.com.br" --nome "Portal Novo" --adicionar
```

---

## 📂 Estrutura do Repositório

```
sankhya-ecosystem/
├── SKILL.md                          # Roteador principal da skill (<500 linhas)
├── README.md                         # Guia completo de uso e instalação
├── fontes.json                       # Configuração de portais para extração incremental
├── references/                       # Guias modulares com progressive disclosure
│   ├── arquitetura/                  # Addon Studio, Módulo Java, JAPE, ModuleConnect, Logging
│   ├── integracao-apis/              # Autenticação, REST, service.sbr, Webhooks
│   ├── telas-e-negocio/              # Telas DWF, catálogo de módulos, consulta ao help
│   ├── frontend-ui/                  # Design System ez-*, sankhya-js, campos calculados
│   ├── banco-dicionario/             # Metamodelo do dicionário, tabelas comuns
│   ├── relatorios-bi/                # JasperReports 4.0.1, Dashboards de BI
│   └── documentacao/                 # Escopo técnico, documento de entrega
├── saida_help/                       # Acervo 100% autocontido (~10.000 arquivos markdown)
│   ├── ajuda-sankhya-com-br/         # Manuais de todas as telas e rotinas do ERP
│   └── developer-sankhya-com-br/     # Referências de APIs e receitas técnicas
├── extractor/                        # Motor de extração incremental embutido
│   ├── extrator_help.py              # Extrator Zendesk API e web crawler
│   ├── fontes.py                     # Módulos de conexão e seletores
│   ├── conversao.py                  # Conversor HTML para Markdown limpo
│   └── requirements.txt              # Dependências Python
└── scripts/                          # Utilitários executáveis
    ├── search_help.py                # Localizador rápido (<20ms) de telas e APIs
    ├── atualizar_acervo.py           # Atualizador incremental multi-fontes
    ├── gerar_catalogo.py             # Gerador/atualizador dinâmico de índices
    ├── catalogo_telas.json           # Catálogo pré-indexado de 9.600+ telas
    └── catalogo_apis.json            # Catálogo pré-indexado de endpoints e receitas
```

---

## 🛡️ Regras de Ouro Técnicas (Embutidas na IA)
1. **Acesso a Dados**: Sempre via JAPE (`DynamicVO`, `JapeFactory.dao`, `FinderWrapper`). `NativeSql` apenas como exceção com parâmetros nomeados (`:param`).
2. **Nomenclatura**: Add-ons nunca usam prefixo `AD_` (reservado para customizações manuais do cliente).
3. **Relatórios**: Compatibilidade estrita com **JasperReports 4.0.1**.
4. **Logging**: Uso exclusivo do `SankhyaLogger` corporativo.
