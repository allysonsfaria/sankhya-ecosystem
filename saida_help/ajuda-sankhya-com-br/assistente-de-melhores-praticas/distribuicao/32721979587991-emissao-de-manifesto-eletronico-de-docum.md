---
id: "32721979587991"
titulo: "Emissão de Manifesto Eletrônico de Documentos Fiscais (MDF-e)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32721979587991-Emiss%C3%A3o-de-Manifesto-Eletr%C3%B4nico-de-Documentos-Fiscais-MDF-e"
trilha: "Assistente de Melhores Práticas > Distribuição"
atualizado_em: "2026-07-22T14:30:41Z"
rotulos: ["MDF-e", "Configuração", "SEFAZ", "Transporte", "RNTRC", "Documentos Eletrônicos"]
---

# Emissão de Manifesto Eletrônico de Documentos Fiscais (MDF-e)

### Descrição

A funcionalidade **Emissão de MDF-e** permite configurar as preferências por empresa, usuários responsáveis e acessos necessários para gerar o Manifesto Eletrônico de Documentos Fiscais (MDF-e), garantindo conformidade fiscal e operacional no transporte de cargas em território nacional.

Ela oferece os seguintes recursos:

- **Configuração por Empresa:** Define empresas que emitem MDF-e e suas preferências específicas como emissão apenas com documentos próprios, participação em programas fiscais (Canal Verde), classificação como transportadora e número do RNTRC.
- **Controle de Acessos:** Permite selecionar os usuários ou grupos responsáveis pela emissão do MDF-e.
- **Configuração de Numeração:** Cria automaticamente o controle de numeração do MDF-e por empresa.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione as empresas ativas que realizam a emissão de MDF-e.
3. Configure as preferências de emissão para cada empresa (**"documentos próprios"**, **"canal verde"**, **"tipo de transportadora"**, **"RNTRC"**).
4. Selecione os grupos e/ou usuários responsáveis pela emissão do MDF-e.
5. Clique em **"Avançar"** para revisar as informações.
6. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos liberados**

- Emissão de MDF-e
  Caminho: Viagens de Transporte
  Permissões: Consultar, Incluir, Alterar

**Tabelas atualizadas**

- TGFEMP – Cadastro de Empresas
  Atualização das preferências de emissão de MDF-e por empresa: **"documentos próprios"**, **"canal verde"**, **"tipo de transportadora"**, **"versão de emissão"**.
- TSIEMP – Empresas do Sistema
  Atualização do número do RNTRC no cadastro da empresa.
- TGFNUM – Controle de Numeração
  Criação de controle de numeração para MDF-e, por empresa, se não existente.

**![ea4ea863-3e71-48a7-9fb4-2269a7319ef0](https://ajuda.sankhya.com.br/hc/article_attachments/32721936554007) Vale saber**

Tenha atenção na configuração das preferências por empresa, como **"emissão apenas com documentos próprios"**, participação no **"Canal Verde"** e o **"número do RNTRC"**. Isso evita erros na emissão e agiliza o processo.
