# Sankhya Ecosystem — Agent Skill

Skill especialista no ecossistema de desenvolvimento do ERP **Sankhya OM**, compatível com **Claude Code**, **OpenAI Codex**, **Antigravity (AGY)**, **Cursor**, **Windsurf** e outros assistentes de IA baseados no padrão de Agent Skills.

---

## 📌 Conteúdo da Skill

- **Backend Java**: Addon Studio 2.0 (`@ActionButton`, `@Listener`, `@Job`, `@BusinessRule`, `@Callback`), Módulos Java legados, persistência com JAPE e `NativeSql`, `ModuleConnect`, `ProxyConnect` e logging com `SankhyaLogger`.
- **APIs e Integrações**: APIs REST v0/v1/v2 (`loadRecords`, `saveRecord`), barramento `/mge/service.sbr` (JSON e XML), autenticação `MobileLoginSP` e API Gateway.
- **Telas e Negócio**: Funcionamento de telas no modelo DWF/DynamicForm, fluxo integrado de módulos (Comercial, Financeiro, Estoque, Fiscal) e consulta indexada a ~10.000 manuais oficiais.
- **Frontend & UI**: Sankhya Design System (`ez-*`), componentes legados `sankhya-js` (AngularJS) e campos calculados (`#type.sql#`).
- **Banco de Dados**: Dicionário de Dados (`TDDTAB`, `TDDCAM`, `TDDLIG`) e cheat sheet de tabelas centrais (`TGFCAB`, `TGFITE`, `TGFPAR`, `TGFFIN`, etc.).
- **Relatórios & BI**: JasperReports 4.0.1 / iReport, NFS-e e Construtor de Componentes de BI.
- **Documentação de Projetos**: Templates padronizados para Proposta Técnica de Escopo e Documento de Entrega de Soluções.

---

## 📂 Estrutura de Arquivos

```
sankhya-ecosystem/
├── SKILL.md                          # Definição principal e roteador da skill
├── README.md                         # Guia de instalação e compartilhamento
├── fontes.json                       # Configuração de URLs/portais a serem extraídos
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
│   └── requirements.txt              # Dependências
└── scripts/                          # Utilitários executáveis
    ├── search_help.py                # Localizador rápido (<20ms) de telas e APIs
    ├── atualizar_acervo.py           # Atualizador incremental multi-fontes
    ├── gerar_catalogo.py             # Gerador/atualizador dinâmico de índices
    ├── catalogo_telas.json           # Catálogo pré-indexado de 9.600+ telas
    └── catalogo_apis.json            # Catálogo pré-indexado de endpoints e receitas
```

---

## 🔄 Como Atualizar ou Adicionar Novas Fontes

### 1. Atualizar todas as fontes cadastradas (padrão):
```bash
python scripts/atualizar_acervo.py
```
O script lê `fontes.json`, baixa apenas o que foi alterado em cada portal, reconstrói o catálogo e sincroniza com o Claude, Codex e AGY.

### 2. Adicionar uma nova fonte de documentação:
Você pode editar diretamente o arquivo `fontes.json` ou rodar via terminal:
```bash
python scripts/atualizar_acervo.py --url "https://outro-portal.sankhya.com.br" --nome "Portal X" --adicionar
```
Isso baixa a nova documentação, salva em `fontes.json` para atualizações futuras e indexa no catálogo de busca imediatamente.

---

## 🚀 Como Instalar nos Clientes de IA

### 1. Claude Code
Copie a pasta para o diretório de skills do usuário ou do projeto:
```bash
# Escopo de usuário:
cp -r sankhya-ecosystem ~/.claude/skills/

# Ou no repositório atual:
cp -r sankhya-ecosystem .claude/skills/
```

### 2. Antigravity (AGY)
```bash
# Copie para a pasta de skills do perfil:
cp -r sankhya-ecosystem ~/.gemini/config/skills/
```

### 3. OpenAI Codex / Assistentes Genéricos
Basta apontar o contexto para a pasta da skill ou copiar para a pasta de regras/skills do projeto (`.agent/skills/` ou `.codex/skills/`).

---

## 🔎 Utilitário de Busca de Telas e APIs

A skill inclui um mecanismo que consulta o acervo offline de ~10.000 manuais e documentações extraídas do Sankhya Help Center:

```bash
# Buscar uma tela ou procedimento:
python scripts/search_help.py "cadastro de parceiros" -d

# Buscar documentação de API ou método:
python scripts/search_help.py "loadRecords" -t api -d
```
