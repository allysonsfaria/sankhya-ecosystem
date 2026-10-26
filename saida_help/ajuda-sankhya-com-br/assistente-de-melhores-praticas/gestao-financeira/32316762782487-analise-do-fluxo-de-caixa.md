---
id: "32316762782487"
titulo: "Análise do Fluxo de Caixa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32316762782487-An%C3%A1lise-do-Fluxo-de-Caixa"
trilha: "Assistente de Melhores Práticas > Gestão Financeira"
atualizado_em: "2026-07-22T16:13:36Z"
rotulos: ["Configuração", "Relatórios", "Segurança", "Movimentação Financeira", "Financeiro"]
---

# Análise do Fluxo de Caixa

### Descrição

A funcionalidade **Análise do Fluxo de Caixa** permite configurar os parâmetros de inadimplência e liberar acessos para análise e acompanhamento detalhado do fluxo de caixa da empresa.

Ela proporciona:

- Fluxo de Caixa Sintético: Permite alterar, incluir e consultar registros financeiros sintetizados.
- Núcleo de Geração de Fluxo de Caixa: Habilita operações de alteração, inclusão e consulta para usuários e grupos selecionados.
- Receitas e Despesas: Libera acesso completo para visualização e operação, promovendo uma análise financeira integrada.

Além disso, os seguintes parâmetros de inadimplência são configurados para enriquecer as análises:

- Percentual de inadimplência para títulos ainda não vencidos
- Percentual de inadimplência para títulos com atraso de até 2 meses
- Percentual de inadimplência para títulos com atraso superior a 2 meses

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os grupos e/ou usuários responsáveis pela análise do fluxo de caixa.
3. Clique em **"Avançar"**.
4. Defina os percentuais de inadimplência:

4.1 Para títulos ainda não vencidos.

4.2 Para títulos com atraso de até 2 meses.

4.3 Para títulos com atraso superior a 2 meses.

5. Clique em **"Avançar"**.
6. Verifique o resumo com os grupos, usuários e parâmetros definidos.
7. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos**

- Fluxo de Caixa Sintético
- Núcleo de Geração de Fluxo de Caixa
- Receitas e Despesas (via permissões de segurança de usuário)

**Tabelas Atualizadas**

- **TSIUSU**

- Inibe acesso a receitas: desmarcado
- Inibe acesso a despesas: desmarcado

- **TSIPAR**

- PERCINADATU – Percentual de inadimplência para títulos ainda não vencidos
- PERCINADANT – Percentual para atraso de até 2 meses
- PERCINADPOS – Percentual para atraso acima de 2 meses
