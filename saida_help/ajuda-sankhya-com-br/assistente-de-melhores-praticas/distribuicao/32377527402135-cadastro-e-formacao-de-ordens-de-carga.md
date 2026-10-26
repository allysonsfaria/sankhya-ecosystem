---
id: "32377527402135"
titulo: "Cadastro e Formação de Ordens de Carga"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32377527402135-Cadastro-e-Forma%C3%A7%C3%A3o-de-Ordens-de-Carga"
trilha: "Assistente de Melhores Práticas > Distribuição"
atualizado_em: "2026-07-22T14:31:37Z"
rotulos: ["Configuração", "WMS", "Transporte", "Preferências", "Ordens de Carga", "Logística"]
---

# Cadastro e Formação de Ordens de Carga

### Descrição

A funcionalidade **Cadastro e Formação de Ordens de Carga** permite configurar regras específicas e liberar os acessos necessários para a criação e gestão de ordens de carga, assegurando personalização e controle logístico do processo.

Ela oferece os seguintes recursos:

- **Cadastro de Ordens de Carga**: Permite consultar, incluir e alterar ordens de carga, proporcionando controle completo sobre a formação das cargas.
- **Configuração de Preferências**: Habilita ajustes como bloqueio por capacidade do veículo, preservação de vínculo em duplicações e devoluções, e regras para alteração de ordens fechadas.
- **Gestão personalizada do processo logístico**: Garante que as ordens de carga sigam regras específicas definidas pela empresa, fortalecendo a rastreabilidade e a governança operacional.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os grupos e/ou usuários responsáveis pela criação e formação de ordens de carga.
3. Clique em **"Avançar"**.
4. Defina as preferências de formação de carga:

        4.1 Bloquear excesso de carga conforme a capacidade do veículo.

        4.2 Preservar ordem de carga ao duplicar pedidos/notas.

        4.3 Preservar ordem de carga em devoluções de venda.

        4.4 Manter ordem de carga vinculada ao MDF-e encerrado.

        4.5 Permitir pedidos/notas com data anterior ao início da OC.

        4.6 Permitir alteração de ordens de carga fechadas.

    5. Clique em **"Avançar"**.

    6. Verifique o resumo com os grupos, usuários e preferências definidas.

    7. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos**

- Cadastro de Ordens de Carga
- Formação de Cargas

**Tabelas Atualizadas**

**TSIPAR**

- EXCESSOCARGA: Bloqueio de excesso de carga conforme capacidade do veículo.
- LIMPAROC: Indicador para limpar ou preservar a OC ao duplicar pedido/nota (valores invertidos).
- LIMPOCDEV: Preservação da OC em devoluções.
- ORDCARGMDFENC: Bloqueio de reutilização da OC vinculada a MDF-e encerrado.
- DTNEGDTINICOC: Permite vínculo com pedidos/notas com data anterior ao início da OC.
- ALTOCFECFORMOC: Permite alteração de ordens de carga fechadas.
