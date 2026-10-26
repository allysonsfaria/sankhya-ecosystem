---
id: "37880608132375"
titulo: "Validação do cadastro de Parceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880608132375-Valida%C3%A7%C3%A3o-do-cadastro-de-Parceiros"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:29Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Financeiro", "NFS-e", "ERP Sankhya"]
---

# Validação do cadastro de Parceiros

## Parceiros

O cadastro do parceiro (tomador) sustenta a emissão de NFS-e no ERP Sankhya: garante identificação correta (PF/PJ, CNPJ/CPF), endereço com CEP válido e classificação fiscal alinhada à TOP VENDA NFSe. Esses dados orientam cálculo de impostos, aderência às regras municipais e transmissão à prefeitura. Um cadastro consistente evita rejeições, assegura validade fiscal e integra a nota ao fluxo operacional e financeiro.

#### Siga as orientações para realizar a configuração no ERP Sankhya

1. Acesse a tela **Parceiros**
   **Menu:** Configurações » Cadastros » Parceiros

- Tipo de Pessoa **- “Física”**
- Sexo - **selecione o gênero do parceiro**
- **Ativo**

**Aba Identificação**

- Preencha os campos com as informações correspondentes:

  - Nome Parceiro - **coloque o seu nome**
  - Razão Social - **nome completo para cadastros de pessoa física**
  - CNPJ/CPF
  - Insc. Estadual/ Identidade
  - Tipo - **“Cliente”**

**Aba Endereço**

- Preencha os campos com as informações correspondentes:

  - CEP - **(Para este treinamento informe 38406184)**
  - Endereço - **será preenchido conforme CEP informado**
  - Número - **(Para este treinamento informe 369)**
  - Bairro - **será preenchido conforme CEP informado**
  - Cód. Cidade - **será preenchido conforme CEP informado**
  - Envio email de pedido / nota - **automático**
  - E-mail - **informe email do parceiro**

**Aba Fiscal**

- No campo **Classificação ICMS**, selecione a opção “**Consumidor Final não Contribuinte**”
- Marque os campos abaixo:

  - Calcular FUNRURAL / INSS - **marcar**
  - Calcular IRF - **marcar**

**Atenção!** O campo ‘Retém ISS’ indica se o parceiro é responsável pela retenção do ISS, conforme a legislação do município do tomador do serviço.

**Aba NF-e/NFS-e/CT-e**

- Nos campos abaixo selecione as informações correspondentes:

  - Geração de boleto nas centrais **- Imprimir e Enviar e-mail**.
  - Tipo do anexo  -  **Arquivo normal (Extensão xml)**
- Informe o email do parceiro nos campos abaixo (para este treinamento informe seu email):

  - **E-mail p/ envio NF-e/NFS-e/CT-e**
  - **E-mail específico p/ envio NFS-e**

**Aba Tipo Negociação**

- Informe o tipo de negociação comercial que deseja priorizar para este parceiro nos campos:

  - Sugestão Entrada/Cotação
  - Sugestão Saída

Para este treinamento informe À VISTA para ambas situações.

- **Salve as alterações realizadas.**
