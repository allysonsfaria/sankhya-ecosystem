---
id: "42427704585239"
titulo: "Clientes Estrangeiros - Cadastro da NIF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427704585239-Clientes-Estrangeiros-Cadastro-da-NIF"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-03T13:07:40Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452152", "sync_hash_abe5435be92e"]
---

# Clientes Estrangeiros - Cadastro da NIF

## Nesse artigo você encontrará algumas dicas e passo a passo sobre: Cadastro da NIF.

- **O que é NIF ?**

NIF - Número de Identificação Fiscal das empresas prestadoras ou tomadoras de serviços, intangíveis ou outras operações com endereço no Exterior.

No Brasil, nossas empresas utilizam o CNPJ - Cadastro Nacional de Pessoa Jurídica, mantido pelo Ministério da Fazenda.

- **Cadastrar o Campo de NIF ao invés do CNPJ:**

Devemos ir em: Administração > Campos e Formulários > Cliente > Empresa ou Pessoa > Criar Campo - precisamos criar dois campos, o primeiro do tipo **CheckBox**:

- **Cliente é Estrangeiro ?**

Depois basta salvar a criação do campo.

E o segundo será do tipo **Texto Simples**:

- **NIF** - nesse campo devemos ir em: Configurações de Visualização do Campo > Iremos **Ocultar por Padrão** e depois > Regras de Exibição e Ocultação > Configurar > Fórmula Simples e inserir a seguinte fórmula:

if (**INSERIR O CAMPO CLIENTE É ESTRANGEIRO - CHECKBOX**) {false} else {true}

Depois basta salvar a fórmula e a criação do campo.

Agora precisamos ir no campo de **CNPJ** (o campo já estará criado, trata-se de um campo padrão do Ploomes) e ir em: Configurações de Visualização do Campo > Iremos **Ocultar por Padrão** e depois > Regras de Exibição e Ocultação > Configurar > Fórmula Simples e inserir a seguinte fórmula:

if (**INSERIR O CAMPO CLIENTE É ESTRANGEIRO - CHECKBOX**) {true} else {false}

Depois basta salvar a fórmula, campo e formulário.

**Clique [Aqui](https://ploomesov2d9p.hippovideo.io/video/play/QVHnjFpBlSynYvo9at6Hn4M4-tinZumYonQiZIhY0gU?utm_source=hv-campaigns&hreferer=private&_=1618443541361) para visualizar um vídeo com a demonstração e passo a passo desse processo.**
