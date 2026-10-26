---
id: "37880870889367"
titulo: "Configuração da Tabela de Preço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880870889367-Configura%C3%A7%C3%A3o-da-Tabela-de-Pre%C3%A7o"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:19Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Financeiro", "Prefeituras", "NFS-e"]
---

# Configuração da Tabela de Preço

## Tabela de Preço

A Tabela de Preço é a fonte do valor dos serviços que compõe a NFS-e. É a partir dela (vigente pela data de vigor) que a Central busca o preço unitário do serviço, formando a base do ISS e os totais do XML/RPS. Suas regras e exceções — por Empresa, Parceiro, TOP, perfil, região — garantem que cada nota use a condição comercial correta; já definições como casas decimais e arredondamento influenciam diretamente o valor transmitido à prefeitura. Quando vinculada aos cadastros (ex.: por Parceiro ou Tipo de Negociação), a tabela assegura consistência entre política comercial, cálculo fiscal e financeiro, reduzindo divergências e retrabalho na emissão da NFS-e.

#### Siga as orientações para realizar a configuração no ERP Sankhya

1. **Acesse a tela Tabelas de Preço**

**Menu:** Comercial » Arquivo » Tabelas de Preço

- Localize a tabela **0 - Padrão**

**Aba Histórico de Atualizações**

- Clique em “**+**” (**Cadastrar Tabela de Preço**)
- Nos campos **Dt. Vigor** e **Dt. Alteração** informe a data atual
- **Salve as alterações.**

**Aba Regras**

- Clique em “**+**” (**Cadastrar Exceção de Preço**)
- Busque o serviço no campo **Produto**
- Selecione a opção **Valor** no campo **Tipo**
- Determine o **preço -** 1000,00 - no campo indicado

**Salve as alterações.**
