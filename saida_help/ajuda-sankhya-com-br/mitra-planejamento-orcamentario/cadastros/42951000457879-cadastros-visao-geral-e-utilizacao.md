---
id: "42951000457879"
titulo: "Cadastros: visão geral e utilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951000457879-Cadastros-vis%C3%A3o-geral-e-utiliza%C3%A7%C3%A3o"
trilha: "MITRA: Planejamento orçamentário  > Cadastros"
atualizado_em: "2026-08-24T13:48:37Z"
rotulos: ["sync_hc", "mitra", "mitra_10", "sync_hash_bd53a822811a"]
---

# Cadastros: visão geral e utilização

## Cadastros: visão geral e utilização

**Módulo:** Cadastros

### O que é e para que serve

O módulo de Cadastros mantém os dados mestres que sustentam todo o orçamento. Sem eles não há preenchimento: os CRs definem quem orça, as contas definem o quê, e os gestores definem os responsáveis.

### Cadastros disponíveis

| Cadastro | Principais campos | Recursos da listagem |
| --- | --- | --- |
| **Empresas** | Nome, CNPJ, situação (ativa/inativa) | Busca por nome ou CNPJ, filtro por situação, paginação |
| **Centros de resultado** | Código, nome, empresa, situação | Busca, filtro por empresa, paginação |
| **Contas contábeis** | Código, nome, tipo, natureza, situação | Busca por código ou nome, filtro por tipo, paginação |
| **Colaboradores** | Nome, CR, empresa, cargo, data de admissão, salário, tipo de contrato (CLT/PJ) | Filtro por CR, busca por nome ou cargo, paginação |
| **Cargos** | Nome, salário médio, situação | Usados nas contratações projetadas |
| **Gestores** | Nome, e-mail, CRs e pacotes sob responsabilidade | O e-mail é o destino do link de preenchimento |

Em todos os cadastros é possível criar, editar e excluir registros.

### Comportamentos e pontos de atenção

- **Situação (ativo/inativo):** registros inativados deixam de aparecer nas seleções, preservando o histórico das versões anteriores.
- **Vínculos importam:** o CR pertence a uma empresa; o colaborador pertence a um CR; o gestor é vinculado a CRs e pacotes. Esses vínculos definem o escopo de cada gestor no preenchimento e no link.
- **Colaboradores alimentam a folha:** salário, tipo de contrato e cargo são a base da projeção de pessoal.

### Resultado esperado

Com os cadastros completos, a criação de versões, as regras contábeis e o preenchimento encontram todos os dados necessários — cada gestor enxerga exatamente os seus CRs.

### Artigos relacionados

- Projeção de pessoal (folha): visão geral e utilização

---

### Pendências para validação

1. Confirmar os rótulos das telas e botões de cada cadastro.
2. Confirmar se a exclusão é bloqueada quando o registro está em uso em alguma versão.
