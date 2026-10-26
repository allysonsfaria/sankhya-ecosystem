---
id: "31005922889367"
titulo: "Liberação de Acessos a um Dashboard Construído no Construtor de Componentes BI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31005922889367-Libera%C3%A7%C3%A3o-de-Acessos-a-um-Dashboard-Constru%C3%ADdo-no-Construtor-de-Componentes-BI"
trilha: "Melhores Práticas > Configurações Sankhya"
atualizado_em: "2026-10-01T17:34:49Z"
rotulos: ["Configuração", "BI", "Passos para resolver", "Razão do erro", "Detalhe do erro", "acessos", "dashboard", "construtor de dash", "construtor de dashboard", "liberacao de acesso"]
---

# Liberação de Acessos a um Dashboard Construído no Construtor de Componentes BI

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31006568326807) **SITUAÇÃO:**

Ao criar um Dashboard através do **Construtor de Componentes BI**, ele não fica disponível para liberação de acessos aos usuários na tela **"Acessos"**.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31005876155031)SOLUÇÃO:**

Para disponibilizar o Dashboard na tela **"Acessos"**, crie o lançador da tela do Dashboard através da funcionalidade **Construtor de Dashboard**.

### Passo a Passo

**![Imagem 3: Crie um novo registro:](https://ajuda.sankhya.com.br/hc/article_attachments/31059018288407) Crie um novo registro:**

- - Acesse a tela **"Construtor de Dashboard";**
  - Crie um novo registro e, preferencialmente, utilize o mesmo nome definido no **Construtor de Componentes BI**.

**![Imagem 4: Associe o Dashboard à Galeria:](https://ajuda.sankhya.com.br/hc/article_attachments/31059008129431) Associe o Dashboard à Galeria:**

- - Vá até a guia **"Galeria"** e procure pelo nome definido na criação do Dashboard, no **Construtor de Componentes BI;**
  - Arraste o Dashboard para a **guia Amarela;**
  - Salve o registro criado.

**![Imagem 5: Crie o Lançador da Tela:](https://ajuda.sankhya.com.br/hc/article_attachments/31059008132503) Crie o Lançador da Tela:**

- - Clique no botão de **"Outras Opções"** e selecione **"Adicionar Lançador";**
  - Defina um nome para a tela (preferencialmente o mesmo utilizado no **Construtor de Componentes BI**);
  - Em **"Pasta de Destino"**, escolha onde esse Dashboard ficará alocado;
  - Salve as configurações.

**![Imagem 6: Liberar acessos:](https://ajuda.sankhya.com.br/hc/article_attachments/31059008133143) Liberar acessos:**

- - Retorne à tela **"Acessos";**
  - Busque pelo nome definido no **Passo 3;**
  - Agora será possível liberar os acessos para os usuários.

Mais informações podem ser visualizadas no artigo: [Construtor de Dashboard](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605574-Construtor-de-Dashboards)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31005922880151)CAUSA:**

Isso ocorre porque o Dashboard foi criado no **Construtor de Componentes BI**, mas não foi vinculado na tela Construtor de Dashboard para que um lançador da tela fosse gerado.
