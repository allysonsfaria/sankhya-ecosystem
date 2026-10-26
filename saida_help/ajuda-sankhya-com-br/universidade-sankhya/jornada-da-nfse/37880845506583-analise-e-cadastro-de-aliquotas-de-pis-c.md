---
id: "37880845506583"
titulo: "Analise e Cadastro de Alíquotas de PIS/COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880845506583-Analise-e-Cadastro-de-Al%C3%ADquotas-de-PIS-COFINS"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:22Z"
rotulos: ["Alíquotas", "Configuração", "Impostos", "Financeiro", "NFS-e", "PIS/COFINS"]
---

# Analise e Cadastro de Alíquotas de PIS/COFINS

## Alíquotas de PIS/COFINS

Na NFS-e, PIS e COFINS são tributos federais registrados como informações da operação: não reduzem a base do ISS (padrão da NFS-e), mas podem influenciar o valor exibido na nota. O resultado que vai para o XML/RPS e para o financeiro depende da alíquota, do CST e das exceções configuradas (por empresa, parceiro, TOP e tipo de operação). Com essas definições coerentes, a nota sai consistente, com rastreabilidade do cálculo, sem rejeições na prefeitura e sem diferenças entre o valor faturado e o registrado no financeiro.

#### Siga as orientações para realizar a configuração no ERP Sankhya

1. Acesse a tela **Alíquotas de PIS**

**Menu:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS

- Localize e selecione com um duplo clique o registro vinculado à venda de serviço

Valide os dados registrados. Esta tela exibirá as informações configuradas previamente na tela de Serviços de acordo com o contexto adotado para este treinamento.

- Grupo - **TODOS**
- Empresa - **1**
- Tipo de Operação - **VENDA NFS-E**
- Tipo - **Saída**
- Tipo alíquota - **1,65**
- Cód. sit. tributária - **01 Alíquota Normal (Cumulativo / Não cumulativo)**

2. **Acesse a tela Alíquotas de COFINS**
   **Menu:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS

- Localize e selecione com um duplo clique o registro vinculado à venda de serviço

Valide os dados registrados. Esta tela exibirá as informações configuradas previamente na tela de Serviços de acordo com o contexto adotado para este treinamento.

- Grupo - **TODOS**
- Empresa - **1**
- Tipo de Operação - **VENDA NFS-E**
- Tipo - **Saída**
- Tipo alíquota - **7,6**
- Cód. sit. tributária - **01 Alíquota Normal (Cumulativo / Não cumulativo)**

**Estas configurações definem como regra que os produtos/serviços que compõe o grupo TODOS, na empresa informada, quando negociados no tipo de operação definido, terão a incidência da alíquota informada.**
