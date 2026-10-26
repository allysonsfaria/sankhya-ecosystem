---
id: "37880563761047"
titulo: "Como configurar Tipos de Operação — TOP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880563761047-Como-configurar-Tipos-de-Opera%C3%A7%C3%A3o-TOP"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-10-08T18:01:32Z"
rotulos: ["Configuração", "Fiscal", "TOP", "Prefeituras", "NFS-e"]
---

# Como configurar Tipos de Operação — TOP

## Tipos de Operação - TOP

Na emissão de NFS-e, a configuração da TOP é determinante para o processo funcionar corretamente. É nela que você define se haverá atualização financeira, cálculo de impostos e impressão da nota, garantindo que o documento atenda às exigências fiscais do município. Como a TOP centraliza essas regras, qualquer ajuste deve ser feito com cuidado e sempre validado por quem domina os processos da empresa.  Uma alteração impacta diretamente os novos lançamentos, podendo mudar como a nota é gerada e transmitida. Ao configurar a TOP corretamente, você assegura que a NFS-e seja emitida com validade fiscal e integrada ao fluxo operacional do ERP Sankhya.

#### Siga as orientações para realizar a configuração no ERP Sankhya

 **1**. Acesse a tela **Tipos de Operação - TOP**

**Menu:** Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

- Localize a TOP - VENDA NFS-e para realizar as configurações

**Aba Geral**

- Selecione nos campos abaixo as seguintes opções:
- Exigir Pedido - **Não Exigir**
- Financeiro - **Receitas**
- Marque a opção “**Copiar liberações quando faturando individualmente**”
- Marque a opção “**Atualiza Contabilidade**”

**Seção Preço/custo**

- Selecione nos campos abaixo as seguintes opções:
- Precifica - **Não atualiza custo e nem preço de venda**
- Usar como Preço - **Preço de Venda**

**Seção Apoio a Decisão**

- Identificador de Devolução - **Não**
- Tipo para análise - **Venda**

**Seção Análise de Giro**

- Atualizar Última Compra - **Não Atualizar**
- Atualizar Última Venda - **Não Atualizar**
- Análise de Giro - **Desconsiderar**

**Aba Livro Fiscal**

- Selecione nos campos abaixo as seguintes opções:

  - Atualização de Livro ICMS - **Não atualiza**
  - Atualização de Livro ISS - **Prestações**
  - Forma de Recolhimento ISS - **Normal**
  - Modelo Documento ISS - **03 - Nota Fiscal de serviços (modelo 3)**
  - Marque a opção “**Validar Totais da Nota na Geração do Livro?**”

**Seção CFOP**

- No campo **Top trabalha com CFOP para**, selecione a opção “**Ambos**”.

**Aba Financeiro**

- Selecione nos campos abaixo as seguintes opções:

  - Atualização do financeiro - **Incluir**
  - Comissão - **Calcular**

**Aba Estoque**

- Selecione nos campos abaixo as seguintes opções:

  - Atualização do Estoque - **Nenhuma**
  - Atualiza estoque MP -  **Nenhuma**
  - Atualização do Bem - **Não atualizar**

**Aba NF-e/NFC-E**

- Selecione nos campos abaixo as seguintes opções:

  - Modelo do Documento - **1 - Nota Fiscal**
  - Indicador de Presença para NF-e/NFC-e/CF-e: - **0 - Não se aplica**
  - NF-e - **Convencional (Não Usa NF-e)**
  - Tipo de Emissão - **Normal**

**Aba Impostos**

- Selecione nos campos abaixo as seguintes opções:

  - Cálculo de ICMS, IPI e ISS - **Calcula e não digita**
  - Código Sit.Trib.IPI Saída - **(-1) Não sujeita ao IPI**
- Marque as opções abaixo:

  - **Tem FUNRURAL/INSS**
  - **Tem IRF**
  - **Tem ISS**

**Aba NFS-e**

- Selecione nos campos abaixo as seguintes opções:

  - Mod. Imp. RPS - **32 - RPS UBERLÂNDIA**
    modelo da RPS utilizado no município
  - Mod. Imp. NFS-e - **31 - NFSE UBERLÂNDIA**
    modelo da NFS-e utilizado no município
  - Cód. Natureza Oper. ISS (NFS-e) - **A - Sem Dedução**
    Consultar regras fiscais do município - [Ajuda Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras)
  - NFS-e - **Normal**

**Aba Impressão**

- Selecione nos campos abaixo as seguintes opções:

  - Base numeração - **"Venda"**
  - Tipo de Numeração - **"Empresa/Série"**
  - Imprimir -**"Na confirmação"**
  - Imprimir Boleto/Duplicata -**"Na confirmação"**
  - Kit/Componentes - Impressão e Livro Fiscal\* - **Componentes**
- Numeração somente automática - **marcar**

**Aba E-mails da TOP**

- Selecione nos campos abaixo as seguintes opções:

  - Tipo - **"Fixo"**
    Escolha entre Parceiro; Parc. destinat.; Parc. transp.; Parc. consig.; Parc. remetente; Matriz do parceiro; Usuário resp. pelo CR; Fixo; Usuário; Vendedor/Comprador; Funcionário; Contatos.
  - E-mail - **insira o email de acordo com o tipo definido**
  - Modelo -**"NFS-e"**
- Ativo -**marcado**
- **Salve as alterações realizadas.**

**2.  Valide Restrições e Exceções**

- Para esta TOP nenhuma restrição deve estar configurada.

**3.  Configure o Controle de Numeração**

- Acione o botão “**...**” (**Outras Opções…**), localizado no menu principal superior.
- Selecione a opção **Controle de Numeração**.
- Clique em “+” (Cadastrar Controle de Numeração)
- Preencha os campos:

  - Empresa - 1
  - Série - NF
  - Mod.Doc.Fiscal - selecionar a opção "01 - Nota Fiscal"
  - Numeração somente automática - marcar
  - Último Código - 1
- Salve o registro.

Crie um modelo para cada empresa.
