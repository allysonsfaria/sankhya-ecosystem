---
id: "32174169073047"
titulo: "Cadastro de Empresas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32174169073047-Cadastro-de-Empresas"
trilha: "Assistente de Melhores Práticas > Configurações Iniciais"
atualizado_em: "2026-07-22T16:17:41Z"
rotulos: ["Configuração", "Empresa", "Parceiro", "Importação", "SEFAZ", "EFD"]
---

# Cadastro de Empresas

### Descrição

O Cadastro de Empresas é a primeira configuração do sistema. A busca e integração de dados é automática, proporcionando mais agilidade e precisão ao processo.

Se houver múltiplas empresas e CNPJs, e o sistema não identificar a empresa principal, ela deve ser selecionada na etapa correspondente.

A importação de dados das empresas é realizada por meio de consultas ao **CNPJ**, permitindo o acesso a informações básicas das entidades. Para complementar esses dados, é possível importar **informações da Escrituração Fiscal Digital (EFD)**.

Essa solução garante que os campos mapeados sejam corretamente capturados e integrados ao ERP, priorizando **precisão, automação e consistência** no cadastro empresarial.

O Assistente busca as informações da empresa nas seguintes fontes:

- **Licença** – dados de autorização de uso do sistema.
- **Receita Federal** – informações cadastrais, como razão social, CNPJ e CNAE (consulta a APIs públicas: CNPJA.COM, CNPJS.DEV, CNPJS.WS, Receita.WS) .
- **SEFAZ** – dados fiscais, como inscrição estadual e regime tributário (consulta por meio de integração com o Infosimples).
- **Arquivo EFD** – dados como inscrição municipal da entidade, perfil de apresentação do arquivo fiscal, indicador de tipo de atividade, dados do contador.

Durante o processo, o sistema exibe o status **"Buscando Empresas"**, garantindo visibilidade do progresso.

### Como instalar

1. Clique em **"Iniciar"**. O sistema listará as empresas licenciadas.
2. Defina a **empresa principal** para as rotinas de gestão.
3. Clique em **"Avançar"**.
4. Verifique as empresas que serão configuradas.
5. Escolha se deseja complementar o cadastro com o **upload do SPED Fiscal**:

      5.1 **Se sim**: clique em **"Sim, complementar o cadastro por meio do upload do SPED Fiscal."**

      Envie um arquivo **.txt** para uma única empresa ou **.zip** para múltiplas empresas.

      5.2 **Não**: clique em **"Não, utilizar apenas os dados já coletados para cadastrar as empresas."**

![495b9bfc-3e43-423b-ba7c-4aef8cbd564c](https://ajuda.sankhya.com.br/hc/article_attachments/32174185853463) Só é possível complementar os dados da empresa com o SPED na instalação de uma Nova Empresa. Não é possível importar dados do SPED para complementar cadastros já existentes.

6. Clique em **"Avançar"**.
7. Revise o **resumo** das empresas que serão configuradas.
8. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

Com base nos dados inseridos ou alterados durante a instalação, o sistema realiza a atualização sequencial das seguintes tabelas:

**1. Cadastro de endereço** (caso o endereço ainda não esteja registrado)

- TSITEND – tipo de endereço
- TSIEND – endereço
- TSIBAI – bairro
- TSICID – cidade

**2. Outras tabelas atualizadas**

- TSIEMP – empresa(s)
- TGFPAR – parceiros, inserindo os dados de cada empresa e do contador, se houver.
- TGFEMP – preferências básicas conforme regime tributário e atividade, além da ativação das empresas cadastradas.

**TGFORD** - ordens de carga, para cada empresa cadastrada no sistema.

### Como simular

Para acessar os cadastros realizados:

1. Acesse a tela **“Empresas”**:

- vá até: Configurações > Cadastros > Empresas;
- pesquise um registro ou clique em **"Mostrar grade"** e **"Atualizar"**.

2. Acesse a tela **“Parceiros”:**

- vá até Configurações > Cadastros > Parceiros;
- pesquise um registro ou clique em **"Mostrar grade"** e **"Atualizar"**.

3. Acesse a tela **“Empresa”:**

- vá até: Comercial > Preferências > Empresa;
- pesquise um registro ou clique em **"Mostrar grade"** e **"Atualizar"**.

4. Acesse a tela **“Ordens de Carga”:**

- vá até: Comercial > Rotinas > Ordens de Carga;
- pesquise um registro ou clique em **"Mostrar grade"** e **"Atualizar"**.

**Vale saber**

Se o sistema encontrou mais de uma empresa, vale a pena conferir qual delas será usada como principal nas rotinas de gestão. Para deixar os dados ainda mais completos, importe o SPED Fiscal — isso ajuda a preencher campos que não vêm da Receita ou SEFAZ, como o nome do contador e o tipo de atividade.

Quanto mais informações agora, menos ajustes depois!
