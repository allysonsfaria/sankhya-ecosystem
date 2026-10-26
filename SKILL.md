---
name: sankhya-ecosystem
description: |
  Guia definitivo e hub especialista em desenvolvimento, arquitetura, customizações, integrações e funcionamento de telas no ecossistema do ERP Sankhya OM.
  Use SEMPRE que o usuário mencionar desenvolvimento no Sankhya, criação de Add-on ou Módulo Java, persistência com JAPE (JapeSession, DynamicVO, JapeFactory, NativeSql), consultas ao Dicionário de Dados (metamodelo TDDTAB, TDDCAM e entidades nativas como TGFPAR, TGFCAB, TGFITE, TGFFIN, TGFPRO, TGFEST, TGFTOP), integração via APIs REST oficiais ou barramento tradicional (/mge/service.sbr, MobileLoginSP, CRUDServiceProvider.loadRecords, saveRecord), dúvidas sobre como funciona qualquer tela do sistema (Parceiros, Central de Vendas, Financeiro, Estoque, Fiscal, etc.), personalizações com Sankhya Design System (ez-*), campos calculados (#type.sql#), relatórios JasperReports (iReport 4.0.1), componentes de BI, elaboração de escopos e documentos de entrega técnica, ou pedidos para atualizar o acervo/documentação do Sankhya (update de manuais, sincronizar help).
---

# Hub Especialista no Ecossistema Sankhya OM

Este guia atua como ponto central de arquitetura, consulta técnica e desenvolvimento para soluções integradas ao ERP Sankhya OM.

---

## 1. Regras Fundamentais e Inegociáveis

1. **Acesso a Dados Sempre por JAPE**:
   - `JapeFactory.dao(...)`, `DynamicVO`, `FinderWrapper` e `EntityFacade` são a forma canônica de persistência.
   - `NativeSql` é reservado apenas para consultas analíticas complexas e **SEMPRE** com parâmetros nomeados (`:param`).
   - Toda operação de persistência deve rodar dentro de `JapeSession.open()` e `hnd.execWithTX(...)`.
2. **Convenção de Prefixos no Banco**:
   - Campos e tabelas criados manualmente pelo usuário no Sankhya recebem prefixo `AD_`.
   - Em artefatos empacotados por Add-on Studio, **NUNCA** use `AD_`. Utilize prefixo de 3 a 5 letras da empresa/solução (ex: `XYZ_TABELA`).
3. **Singletons Thread-Safe**:
   - Serviços (`@Service`, `@Controller`) e Actions são compartilhados entre threads. Nunca declare atributos de instância mutáveis com dados da requisição ou do usuário.
4. **Compatibilidade de Relatórios**:
   - O motor de relatórios do Sankhya exige estritamente a versão **JasperReports 4.0.1**.

---

## 2. Roteamento Rápido por Tipo de Demanda

Identifique o objetivo da solicitação e consulte o arquivo de referência correspondente antes de gerar código ou responder:

### A. Backend Java e Arquitetura
- **Addon Studio 2.0**: Anotações `@ActionButton`, `@Listener`, `@Job`, `@BusinessRule`, `@Callback`, `@Controller` → [addon-studio.md](references/arquitetura/addon-studio.md)
- **Módulo Java Clássico**: Extensões legadas via JAR manual sem Addon Studio → [modulo-java.md](references/arquitetura/modulo-java.md)
- **Persistência JAPE**: Sessões, transações autônomas, CRUD com DynamicVO e NativeSql seguro → [jape-persistencia.md](references/arquitetura/jape-persistencia.md)
- **Comunicação Inter-Módulos**: `ModuleConnect` e `ProxyConnect` desacoplados → [module-proxy-connect.md](references/arquitetura/module-proxy-connect.md)
- **Segurança e Logging**: Uso obrigatório do `SankhyaLogger`, prevenção a SQL injection e conformidade → [seguranca-logging.md](references/arquitetura/seguranca-logging.md)

### B. Integrações e APIs Externas
- **Autenticação**: Login no barramento clássico (`MobileLoginSP.login`) e API Gateway OAuth/Bearer → [autenticacao.md](references/integracao-apis/autenticacao.md)
- **APIs REST Oficiais**: Consulta paginada (`CRUDServiceProvider.loadRecords`) e mutações (`saveRecord`) → [rest-apis.md](references/integracao-apis/rest-apis.md)
- **Barramento Tradicional**: Chamadas via `/mge/service.sbr` em JSON e XML → [service-sbr.md](references/integracao-apis/service-sbr.md)
- **Webhooks e Padrões de Integração**: Sincronização assíncrona bidirecional → [webhooks-receitas.md](references/integracao-apis/webhooks-receitas.md)

### C. Entendimento de Telas, Regras e Manuais
- **Como Funcionam as Telas**: Estrutura DWF, grades, formulários e abas contextuais → [guia-telas-sankhya.md](references/telas-e-negocio/guia-telas-sankhya.md)
- **Mapa de Módulos e Fluxos**: Ciclo integrado de Vendas, Compras, Financeiro e Estoque → [catalogo-modulos.md](references/telas-e-negocio/catalogo-modulos.md)
- **Consulta ao Acervo Local**: Localização de manuais de telas e resolução de erros → [consulta-ajuda-telas.md](references/telas-e-negocio/consulta-ajuda-telas.md)

### D. Frontend e Customizações Visuais
- **Sankhya Design System**: Componentes web modernos (`ez-*`), DataUnit e formulários → [design-system-ez.md](references/frontend-ui/design-system-ez.md)
- **Framework Legado (sankhya-js)**: Telas em AngularJS 1.x e ServiceProxy → [sankhya-js.md](references/frontend-ui/sankhya-js.md)
- **Campos Calculados na Grid**: HTML, botões e popups dinâmicos em colunas via SQL (`#type.sql#`) → [campos-calculados.md](references/frontend-ui/campos-calculados.md)

### E. Banco de Dados e Dicionário
- **Metamodelo do Dicionário**: Tabelas `TDDTAB`, `TDDCAM`, `TDDLIG`, `TDDOPC` e tipos de campos → [metamodelo-dicionario.md](references/banco-dicionario/metamodelo-dicionario.md)
- **Tabelas Essenciais**: Guia com as entidades centrais (`TGFCAB`, `TGFPAR`, `TGFPRO`, `TGFFIN`, etc.) → [tabelas-essenciais.md](references/banco-dicionario/tabelas-essenciais.md)

### F. Relatórios, BI e Documentação
- **JasperReports e NFS-e**: Diretrizes de formatação, parâmetros de contexto e sub-relatórios → [jasper-reports.md](references/relatorios-bi/jasper-reports.md)
- **Painéis e Dashboards de BI**: Construtor de BI, gadgets e estrutura de filtros → [bi-dashboards.md](references/relatorios-bi/bi-dashboards.md)
- **Proposta Técnica e Escopo**: Modelo padronizado para especificação de demandas → [escopo-tecnico.md](references/documentacao/escopo-tecnico.md)
- **Documento de Entrega**: Checklist de implantação, homologação e deploy de pacotes → [documento-entrega.md](references/documentacao/documento-entrega.md)

---

## 3. Investigando Telas com o Utilitário de Busca

Quando o usuário perguntar como funciona uma tela específica (ex: *Cadastro de Parceiros*, *Central de Vendas*, *Movimentação Financeira*), ou sobre um erro específico do ERP, utilize o script de busca local incluído na skill:

```bash
python scripts/search_help.py "<termo-ou-nome-da-tela>" -d
```

O script consulta o catálogo indexado dos ~10.000 artigos oficiais do Sankhya Help e Portal do Desenvolvedor, exibindo os parâmetros associados, a trilha no sistema e o caminho do arquivo completo para consulta detalhada.

---

## 4. Atualização Periódica do Acervo e Referências

Quando o usuário pedir para **atualizar o acervo**, **rodar update**, **sincronizar manuais** ou **baixar novidades do Sankhya**, execute o script de atualização incremental embutido:

```bash
python scripts/atualizar_acervo.py
```

### O que o comando faz automaticamente:
1. Conecta na API pública do Zendesk (`ajuda.sankhya.com.br`) e no Portal do Desenvolvedor (`developer.sankhya.com.br`).
2. Compara `_estado.json` e baixa **somente** artigos criados ou modificados desde a última execução (operação leve e rápida).
3. Atualiza os arquivos Markdown na pasta interna `saida_help/`.
4. Reconstrói os catálogos indexados `catalogo_telas.json` e `catalogo_apis.json`.
5. Propaga automaticamente os novos arquivos para as IAs locais instaladas (Claude, Codex, AGY).
