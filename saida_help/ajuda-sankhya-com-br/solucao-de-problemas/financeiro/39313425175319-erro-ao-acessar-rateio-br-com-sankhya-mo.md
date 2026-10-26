---
id: "39313425175319"
titulo: "Erro ao Acessar Rateio - br/com/sankhya/modelcore/crudlisteners/RateioPanelCrudListener"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39313425175319-Erro-ao-Acessar-Rateio-br-com-sankhya-modelcore-crudlisteners-RateioPanelCrudListener"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-10-14T19:35:50Z"
rotulos: ["Movimentação Financeira", "Atualização", "Financeiro", "Erro", "Artigo criado KCS", "Financeiro - KCS", "Design System"]
---

# Erro ao Acessar Rateio - br/com/sankhya/modelcore/crudlisteners/RateioPanelCrudListener

**Mensagem**

Erro ao carregar registros br/com/sankhya/modelcore/crudlisteners/RateioPanelCrudListener

**Situação**

Ao tentar acessar a tela de rateio a partir da **"Movimentação Financeira"** (Financeiro » Rotinas » Movimentação Financeira) no layout **"Design System"**, o sistema apresenta uma mensagem de erro e trava, impedindo a realização do rateio de despesas por centro de custo. O erro pode ocorrer tanto ao tentar abrir um rateio existente quanto ao criar um novo rateio para títulos financeiros.

**Solução**

Para corrigir este erro, é necessário atualizar o módulo **"Financeiro BFF"** e as telas do **"Design System"**. Siga o procedimento abaixo:

**(1)** Acesse o sistema utilizando o **"Usuário SUP"**.

**(2)** Abra a tela **"Movimentação Financeira"** (Financeiro Consultas Movimentação Financeira) utilizando o layout **"Design System"**.

**(3)** Clique no **"Ícone do Usuário"** localizado no canto superior da tela.

**(4)** Selecione a opção **"Atualizar Telas do Design System"**.

**(5)** Aguarde o processo de atualização ser concluído. Caso apareça alguma mensagem de erro durante a atualização, clique no **"Botão OK"** para prosseguir.

**(6)** Feche completamente a tela **"Movimentação Financeira"**.

**(7)** Reabra a tela **"Movimentação Financeira"** e realize um teste de rateio em um dos títulos para validar a correção.

**Observação:** A atualização corrige o erro a partir da versão 1.19.1 do módulo **"Financeiro BFF"**. Após a atualização, o erro não voltará a ocorrer.

**Causa**

O erro está relacionado a uma incompatibilidade de versão do módulo **"Financeiro BFF"** com o layout **"Design System"**. A funcionalidade de rateio no layout **"Design System"** requer uma versão atualizada do módulo para funcionar corretamente. Versões anteriores à 1.19.1 apresentam este problema ao tentar carregar os registros da tela de rateio através do listener **"RateioPanelCrudListener"**.
