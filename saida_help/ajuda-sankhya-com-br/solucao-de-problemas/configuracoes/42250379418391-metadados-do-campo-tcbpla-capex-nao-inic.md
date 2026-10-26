---
id: "42250379418391"
titulo: "Metadados do campo TCBPLA->CAPEX não inicializados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42250379418391-Metadados-do-campo-TCBPLA-CAPEX-n%C3%A3o-inicializados"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-14T13:30:34Z"
rotulos: ["Resolução de Erro de Metadados Não Inicializados", "Metadados da entidade"]
---

# Metadados do campo TCBPLA->CAPEX não inicializados

A correção desse erro foi realizada nas versões 4.36b112 e 4.35b811, mas caso não consiga atualizar a base no momento, seguir os passos a baixo para a correção.

**Mensagem**
Erro interno
Não foi possível resolver os meladados da entidade
EmpresaFinanceiro-pt\_BR
Erro ao carregar os metadados da entidade
EmpresaFinanceiro: Erro interno: Metadados do campo
TCBPLA->CAPEX não inicializados

**SITUAÇÃO**

Este erro ocorre ao tentar acessar telas criticas do sistema tais como: **"Portal de Vendas"** e **"Portal de Compras"** após atualização para as versões recentes do Sankhya.

**Solução**
Deve ser realizada a reinicialização das Unidades de Dados das seguintes tabelas e respectivas instâncias:

**TCBPLA**

- PlanoContaECD
- FINPlanoContaComb
- PlanoConta
- PlanoContaEmpresa

**TGFCAB**

- CabecalhoNota

**TGFEMP**

- EmpresaFinanceiro

Esse processo deve ser feito usando a tela Dicionário de Dados (Configurações >> Avançado) conforme video abaixo.

![Imagem 1: Esse processo deve ser feito usando a tela Dicionário de Dados (Configurações >> Avançado) conforme video abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/42250364885655)
