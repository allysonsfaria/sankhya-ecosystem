---
id: "42951000707095"
titulo: "Modelagem de modelos de preenchimento: visão geral e utilização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951000707095-Modelagem-de-modelos-de-preenchimento-vis%C3%A3o-geral-e-utiliza%C3%A7%C3%A3o"
trilha: "MITRA: Planejamento orçamentário  > Modelagem"
atualizado_em: "2026-08-24T13:48:40Z"
rotulos: ["sync_hc", "mitra", "mitra_12", "sync_hash_f58ee29fa799"]
---

# Modelagem de modelos de preenchimento: visão geral e utilização

## Modelagem de modelos de preenchimento: visão geral e utilização

**Módulo:** Modelagem

### O que é e para que serve

A Modelagem é onde o administrador define **como** cada grupo de contas será orçado. O produto traz modelos nativos (Base Zero, Base Histórico, Pessoal e Receita) e permite criar **modelos personalizados**, com fórmulas próprias, para necessidades específicas — por CR ou por pacote.

### Conceitos

- **Modelo (driver):** a forma de construção do valor de uma conta no preenchimento. Cada modelo vira uma aba na tela do gestor.
- **Escopo:** modelos podem ser de **CR** (cada gestor preenche o seu) ou de **Pacote** (um responsável preenche centralizado e o valor é rateado entre CRs).
- **Fórmulas:** linhas calculadas do modelo, com granularidade configurável e possibilidade de rateio; podem ter linhas de entrada personalizadas preenchidas pelo gestor.
- **Ordem:** a sequência dos modelos pode ser reordenada e define a ordem das abas no preenchimento.

### Ações e controles

| Ação | O que faz |
| --- | --- |
| Criar modelo | Adiciona um modelo personalizado, com escopo CR ou Pacote |
| Editar fórmulas | Define as linhas de cálculo e entradas do modelo |
| Publicar versão do modelo | Congela o estado atual das linhas e fórmulas como uma versão consultável |
| Excluir/inativar | Remove o modelo; se já houver orçamento preenchido com ele, a exclusão é bloqueada e o modelo é inativado |
| Reordenar | Ajusta a posição do modelo entre as abas |

### Comportamentos e pontos de atenção

- **Versões de modelo:** cada publicação gera um snapshot com histórico — é possível listar as versões e visualizar o estado de cada uma.
- **Modelos em uso não somem:** a exclusão com orçamento preenchido é bloqueada; o modelo é apenas inativado, preservando os dados lançados.
- O efeito prático do modelo sobre cada CR depende das **Regras contábeis** (vínculo conta × modelo).

### Resultado esperado

Modelos configurados e ordenados; ao abrir o preenchimento, cada CR exibe as abas corretas, com as fórmulas calculando conforme a última versão publicada.

### Artigos relacionados

- Preenchimento do orçamento por modelos: visão geral e utilização
- Regras contábeis: visão geral e utilização

---

### Pendências para validação

1. Confirmar rótulos da tela (botões de criar, publicar versão, reordenar).
2. Confirmar como a inativação é sinalizada visualmente na lista de modelos.
