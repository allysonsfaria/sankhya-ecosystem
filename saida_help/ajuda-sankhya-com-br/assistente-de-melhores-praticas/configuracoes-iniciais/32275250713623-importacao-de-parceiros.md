---
id: "32275250713623"
titulo: "Importação de Parceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32275250713623-Importa%C3%A7%C3%A3o-de-Parceiros"
trilha: "Assistente de Melhores Práticas > Configurações Iniciais"
atualizado_em: "2026-07-22T16:17:19Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Importação", "Cadastro"]
---

# Importação de Parceiros

### Descrição

Permite a **importação e configuração de clientes e fornecedores**, garantindo que os dados sejam completos, padronizados e validados automaticamente. Inclui verificação de duplicidade, conferência de campos obrigatórios, consulta de endereços via CEP e classificação fiscal.

#### Etapas do processo

**Verificação de duplicidade**
O sistema verifica se o **CNPJ/CPF** já está cadastrado. Se houver duplicidade, o registro é ignorado e o motivo aparece no **log de erros**.

**Conferência de campos obrigatórios**
Caso faltem informações essenciais (**Nome, CNPJ/CPF, Endereço ou CEP**), o sistema bloqueia o cadastro até que os dados sejam corrigidos.

**Consulta e padronização de endereços**
O sistema busca automaticamente os dados do **CEP** informado. Se necessário, complementa as informações com registros existentes. Caso não encontre, cria um novo endereço no banco de dados.

**Cadastro e ajustes**
Cada parceiro é cadastrado com todos os dados validados. Caso haja um **ID Externo**, ele será incluído no registro.

**Classificação automática**
Com base no **CNPJ/CPF**, o sistema determina a classificação fiscal do parceiro:

- **Revendedor** → Pessoa Jurídica com Inscrição Estadual
- **Isento de ICMS** → Pessoa Jurídica com Inscrição ISENTO
- **Consumidor Final** → Pessoa Física

### Como instalar

1. Clique em "**Iniciar**".

2. Clique na opção "**Planilha modelo**" ou "**Notas Fiscais Eletrônicas (NF-e)**"

2.1. Se a escolha for "**Planilha modelo**":

2.1.1 Clique em "**Baixar Modelo**" para fazer o download da planilha modelo que deverá ser preenchida para a importação de parceiros.

2.1.2. Faça o upload da planilha preenchida nos formatos .xls ou .xlsx.

2.1.3. Clique em "**Avançar**".

2.2. Se a escolha for "**Notas Fiscais Eletrônicas (NF-e)**":

2.2.1 Adicione o arquivo zipado dos documentos fiscais emitidos ao longo dos últimos 6 meses, pelo menos.

2.2.1.1 Clique no botão "**Avançar**".

2.2.2 Se arquivos já estiverem sido adicionados anteriormente, basta escolher adicionar novos arquivos ou usar o que já foram adicionados, através das opções:

2.2.2.1 Sim, utilizar apenas os arquivos que já foram importados. Clique em "**Avançar**".

2.2.2.2 Não, utilizar apenas novos arquivos que serão importados. Adicione o arquivo zipado dos documentos fiscais emitidos. Clique em "**Avançar**" para continuar.

3. Verifique o resumo com uma prévia dos parceiros que serão instalados.

4. Clique em "**Instalar**" para finalizar a configuração.

### Detalhes da instalação

Com base nos dados inseridos durante a instalação, se os CEP´s não estiverem cadastrados, o sistema realiza a atualização sequencial das seguintes tabelas:

**1. Cadastro de endereço (caso o endereço ainda não esteja registrado)**

TSITEND – tipo de endereço

TSIEND – endereço

TSIBAI – bairro

TSICID – cidade

**2. Outras tabelas atualizadas**

TGFPAR – Cadastro de parceiros

### Como simular

Para acessar os cadastros realizados:

**Parceiros**:

1. Vá até Configurações > Cadastros > Parceiros.
2. Clique em "**Mostrar grade**" e "**Atualizar**".

**Vale saber**

Planilha ou NF-e? A planilha dá mais controle, mas usar as NF-es acelera tudo — ideal se a empresa já emite notas com frequência. O sistema cuida da validação dos dados, evita duplicidades e até classifica os parceiros automaticamente. Quanto mais completos os dados agora, menos retrabalho depois.
