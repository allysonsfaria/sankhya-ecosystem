---
id: "37961338448663"
titulo: "Cadastros básicos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37961338448663-Cadastros-b%C3%A1sicos"
trilha: "Universidade Sankhya > Jornada Sankhya Tax"
atualizado_em: "2026-07-22T14:03:33Z"
rotulos: ["Configuração", "Parceiro", "Centro de Resultado", "Impostos", "Financeiro", "Natureza", "Cadastro"]
---

# Cadastros básicos

## Configurações e  cadastros básicos relacionados

#### 1. Introdução

Este documento orienta o usuário no cadastro e nas configurações básicas necessárias para tratar o processamento das notas fiscais de serviço capturadas pelo Sankhya Tax. O intuito é garantir que as integrações ocorram de forma consistente, evitando falhas ou retrabalhos e assegurando maior controle e rastreabilidade das operações fiscais.

#### 2. Como cadastrar Tipos de Negociação

1. Acesse a tela **Tipos de Negociação**

**Menu:** Financeiro » Arquivo » Cadastros » Tipos de Negociação

- Clique no botão “**+ Novo registro**” para criar um novo tipo de negociação.
- Se preferir, você pode clicar em “**Mostrar grade**” e depois em “**Atualizar**” para visualizar os cadastros já existentes. 
  Nessa visualização, é possível duplicar um tipo de negociação já cadastrado. 
  **Atenção:** ao duplicar, o Subtipo deve ser o mesmo daquele que você deseja cadastrar. Após duplicar, atualize as informações necessárias.
- No campo de **Descriçã**o, informe um nome que identifique o tipo de negociação.
  (Ex: **PARCELADO - 12X**).

**Configurar características básicas:**

- Marque o campo "**Ativo**" para disponibilizar o tipo de negociação.
- Selecione o "**Subtipo**" (à vista, **parcelado**, a prazo, etc.)
- Defina a "**Base do prazo**" (**a partir do dia** ou fora o mês)
- Clique em **Salvar** para registrar as informações.

**Configurar parcelas:**

Na aba "**Parcelas**", configure:

- No campo **Prazo para entrada**: o número de dias para o cálculo da **1ª parcela**;
- No campo **Prazo entre as Parcelas:** informe o número de dias entre as parcelas. (Ex: 30)
- No campo **Quantidade de parcelas:** determina-se o número de parcelas que deverão ser geradas. 
  (Ex: 12).
- Clique no botão **Calcular Parcelas**. Automaticamente o sistema irá criar as parcelas no campo a baixo.

  **Opção de digitação:**

**Tem-se as seguintes opções:**

- Digitar Somente Valor;
- Digitar Prazo e Valor;
- **Digitar Somente Data;** (Para o case, aplique essa configuração em todas as parcelas.)
- Digitar Data e Valor;
- Não Digita;
- Digitar Somente Prazo.
- Prazo em dias para o vencimento
- Percentual atribuído a cada parcela
- Banco e conta bancária associada (opcional)
- Tipo de título (opcional, mas importante para classificação) (ex: **Boleto**)

**Finalização:**

- Clique em "**Salvar**".
- Acione o botão "**Confirmar parcela**".

**Observações importantes - boas práticas**

- Cadastre tipos separados para compras e vendas.
- Use códigos 1+ para vendas e 500+ para compras.
- Mantenha organização e clareza no preenchimento dos campos.
- Inative os tipos que não são utilizados ao invés de excluí-los.

#### 3. Como realizar o cadastro de natureza

1. Acesse a tela **Natureza de Receitas e Despesas**

**Menu:** Configurações »  Cadastros »  Gerencial

2. **Utilize a estrutura padrão do sistema**

- Consulte a árvore hierárquica existente para manter a organização padrão.

3. **Adicione uma nova natureza**

- Clique no botão **+ Cadastrar Natureza [F8]**.

4. **Preencha os dados obrigatórios**

- **Código da Natureza**: siga a hierarquia definida pelo sistema.
- **Descrição**: insira o nome descritivo da natureza.
- **Nível**: defina se será uma natureza analítica (sem subdivisões) ou sintética (com subníveis).
- **Tipo de Natureza**: selecione Receita ou Despesa.

5. **Finalize o cadastro**

- Clique no botão **Salvar** para concluir o registro.

**Observações importantes**

- As naturezas são apresentadas em cores diferentes no sistema:
- Azul para receitas e Vermelho para despesas.
- A natureza funcionará como um plano de contas gerencial.
- É recomendado utilizar as naturezas pré-cadastradas no sistema, pois já contêm configurações importantes.

#### 4. Como realizar o cadastro de centro de resultado

1. Acesse a tela **Centro de Resultado**

**Menu:** Configurações » Cadastros » Gerencial » Centros de Resultado

2. **Inicie um novo cadastro**

- Clique em **+ Novo Registro**.

3. **Preencha as informações principais**

- Informe o **código** do centro de resultado (caso não seja gerado automaticamente).
- Defina uma **descrição** clara e objetiva.
- Marque o centro como **ativo** para que possa ser utilizado.

4. **Configure a estrutura organizacional**

- Indique se o centro é **principal** ou **subordinado**. Caso seja subordinado, vincule-o ao centro de resultado **superior**.
- Ajuste a hierarquia conforme a organização da empresa.

5. **Finalize o cadastro**

- Clique no botão **Salvar** para concluir.

**Observações importantes**

- O centro de resultado é fundamental para análises gerenciais.
- Pode ser utilizado para controle de transferências internas.
- Permite rateio de receitas e despesas por natureza.
- É possível gerar relatórios específicos por centro de resultado.

#### 5. Como cadastrar Parceiros

1. Acesse a tela **Parceiros**

**Menu:** Configurações » Cadastros » Parceiros

2. Inicie um novo cadastro

- Clique em **+ Novo Registro**
- Preencha todos os campos obrigatórios (marcados com asterisco).
- Marque o parceiro como **Ativo** para permitir seu uso no sistema.
- Escolha o **Tipo de Pessoa**: Física ou Jurídica.

**Aba Identificação**

- Preencha o **Nome do Parceiro**.
- Informe a **Razão Social** (se for pessoa jurídica).
- Preencha o **CNPJ** ou **CPF**.
- Informe a **Inscrição Estadual** (se aplicável).
- No campo **Tipo**, selecione as relações com a empresa (ex: cliente, fornecedor, motorista etc.).

**Aba Endereço**

- Digite o **CEP** e pressione Tab ou clique na lupa para preenchimento automático.
- Complete com **número** e **complemento** do endereço.

**Aba Fiscal**

- Selecione a **Classificação ICMS** conforme o tipo de negócio.
- Para **parceiros industriais**, marque a opção **Tem IPI**.

**Aba Tipo de Negociação**

- Configure os **tipos de negociação padrão** para compra e/ou venda. Essas informações serão utilizadas nas centrais de compras e vendas.

3. **Finalização**

- Clique em **Salvar** para confirmar e concluir o cadastro.
  Esse registro estará disponível para vínculo às notas processadas na aba Dados do fornecedor, seção Fornecedores, dentro da tela Captura e importação NFSe

#### 6. Como cadastrar Tipo de Serviços

1. Acesse a tela **Lista de Serviços**
   **Menu:** Comercial » Arquivo » Cadastros » Lista de Serviços

De forma nativa o sistema apresenta cadastro de serviços, utilize o campo de busca para 

verificar se o serviço a ser cadastrado posteriormente possui registro nesta tela. 

2. **Para cadastrar um novo serviço**

- Localize e selecione o registro sintético relacionado ao serviço
- Clique no botão ”**+**” (**Cadastrar Lista de Serviços**)
- Informe o código respeitando a hierarquia já cadastrada
- Descreva o serviço no campo indicado
- Marque os campos **Ativo** e **Analítico**.
- **Salve o registro.**

**Para dúvidas relacionadas à Lista de Serviços conforme legislação acesse a** [**Lei Complementar Nº 116**](https://www.planalto.gov.br/ccivil_03/leis/LCP/Lcp116.htm)

#### 7. Como cadastrar Serviços

1. Cadastro de serviços

- Acesse a tela **Serviços**

**Menu:** Configurações » Cadastros » Produtos » Serviço

- Clique em **+ Novo registro** e preencha os campos:

**Painel Principal**

- **Descrição:** Preenchimento obrigatório. Informe a descrição do serviço.
- **Ativo:** Marque para que o serviço esteja disponível para uso.

**Aba Geral**

- **Grupo:** Selecione o grupo ao qual o serviço pertence (precisa estar previamente cadastrado).
- **Unidade Padrão:** Escolha a unidade de medida (ex: Horas, Minutos, Dias – deve estar cadastrada na tela de Unidades).

**Aba Impostos**

- Marque **"Tem ISS"** como **Tributado.**
- **Código de Tributação Município NFS-e**
- **CNAE da empresa**
- **Tipo de Serviço (conforme lista LCP 116)**
- Marque **"Tem INSS",** se houver incidência
- **%Red. Base INSS (se houver)**
- **Imposto de Renda (IRF)**
- Marque **"Tem IRF",** se o serviço estiver sujeito ao imposto.
- **% IRF** (ex: 1,5%)
- **Grupo PIS, Grupo COFINS e Grupo CSLL:** Vincule os grupos previamente cadastrados.
- **Tipo de Serviço:** Vincule corretamente para fins de tributação.
- Clique em **Salvar**.

**Aba Alíquotas de ISS**

- Clique em **+ Novo registro** e preencha:
- **Cidade:** Informe onde a alíquota será aplicada.
- **Empresa:** Selecione a empresa vinculada.
- **Percentual de ISS:** Informe a alíquota.
- **Código de Tributação ISS:**

00 – Tributado

01 – Tributado com ISS Retid

06 – Isento

07 – Não Tributado

- **Tipo de Serviço:** Vincule o código correspondente.
- **Percentual de dedução na base do ISS:** Preencha se houver dedução.
- **Tipo de Dedução da Base de ISS**

Subempreito

Por percentual

Matérias

(Em branco, se não houver)

- Clique em **Salvar**

**Aba Outros Impostos**

- Clique em **+ Novo registro** e preencha:
- **Imposto**
- **Alíquota**
- **Na Nota:** Informe qual deve ser o comportamento sistema quanto a retenção desse imposto na nota
- **No Financeiro Origem Financeiro:** Informe qual deve ser o comportamento sistema quanto a retenção desse imposto no financeiro quando de origem financeiro
- **No Financeiro Origem Estoque:** Informe qual deve ser o comportamento sistema quanto a retenção desse imposto no financeiro quando de origem estoque
- **Ponto de atenção**: Para que os impostos sejam viculados aqui eles devem ser cadastrados de forma prévia na tela **Impostos**.
- Clique em **Salvar**

**Observações importantes**

- As configurações devem seguir a **legislação vigente** e as **regras do município** onde o serviço será prestado.
- Os **grupos de PIS, COFINS e CSLL** devem estar cadastrados antes.
- Para **NFS-e**, o **código de tributação do município** deve ser corretamente preenchido.
- A alíquota de ISS pode ser cadastrada diretamente na tela de serviço.
- Para serviços **isentos ou não tributados**, use a tela específica de **Alíquotas de ISS**.

  Esse registro estará disponível para vínculo às notas processadas na aba Serviço Prestado, seção Serviços, dentro da tela Captura e importação NFSe

#### 8. Como cadastrar Projetos

1. Cadastro de projetos

- Acesse a tela **Projetos**

**Menu:** Configurações » Cadastros » Gerencial » Projetos

- Clique em **+ Novo registro** e preencha os campos:
- **Projeto:** Código identificador do projeto (obrigatório).
- **Identificação:** Nome completo ou título do projeto (obrigatório).
- **Abreviação do Projeto:** Sigla ou nome curto que será usado para referência rápida (obrigatório).
- **Produto:** (Opcional) Vincule um produto ou serviço relacionado ao projeto, se aplicável.
- **Ativo:** Essa opção já vem marcada por padrão e indica que o projeto estará disponível para uso.
- **Analítico:** Também marcada automaticamente. Apenas projetos analíticos são aceitos nas rotinas do sistema.
- **Atenção:** Para criar um projeto sintético (agrupador de outros), desmarque a opção Analítico.
- Clique em **Salvar** para concluir o cadastro.

#### 9. Como cadastrar Tipos de Operação - TOP

1. Acesse a tela **Tipos de Operação - TOP**

**Menu:** Configurações » Cadastros » Tipos de Operação (TOP)

- Clique em **"+ Cadastrar Tipo de Operação [F8]"**
- No **Painel Principal** preencha os campos obrigatórios:
- **Código da Operação (manual ou automático)**
- **Descrição**
- **Tipo:** selecione Entrada ou Saída
- **Grupo**
- Marque a opção **Ativo**

**Aba Geral**

- Marque **"Orçamento"** se a TOP for usada para orçamentos
- Em **Financeiro,** defina a atualização:
- **Despesa, Receita ou Não Atualizar**

**Aba Financeiro**

- Em **Atualização do Financeiro,** defina: Incluir ou Provisionar

**Aba Fiscal**

- Defina o campo **Atualização de Livro ICMS**
- Informe as **CFOPs** para: **Dentro do estado e Fora do estado**
- **Ajuste os parâmetros fiscais específicos, se necessário**

**Aba Estoque**

- Em **Atualização do Estoque**, selecione a movimentação aplicável

**Aba Impressão**

- Configure os parâmetros de impressão
- Defina o tratamento para kits e componentes
- Estabeleça regras para documentos fiscais
- **Outras Opções (...)**
- Configure o controle de numeração
- Defina restrições e exceções aplicáveis

**Observações importantes**

- A TOP deve estar de acordo com a legislação vigente
- Mantenha uma padronização na nomenclatura para facilitar a identificação
- As configurações impactam relatórios fiscais, contábeis e operacionais
- Parâmetros adicionais podem ser necessários dependendo da operação

#### 10. Como cadastrar Modelo de Notas e Pedidos

1. Acesse a tela **Modelo de Notas e Pedidos**

**Menu:** Comercial » Consulta » Modelo de Notas e Pedidos

- Clique no botão “**+**” (**Cadastrar** **Cabeçalho Nota Modelo**)
- Preencha as informações obrigatórias que orientarão o modelo da nota aquisição de serviço.
- Empresa
- Tipo de operação
- Tipo de Negociação
- Natureza
- Centro Resultado

A obrigatoriedade do preenchimento de Natureza e Centro Resultada estão alinhadas 

com as necessidades e diretrizes da empresa.

Os demais campos relacionados a nota fiscal de serviço podem ser alimentados conforme necessidade e realidade da empresa.

Esse registro estará disponível para vínculo às notas processadas na aba Informações da Nota, seção Modelos de notas/pedidos, dentro da tela Captura e importação NFSe
