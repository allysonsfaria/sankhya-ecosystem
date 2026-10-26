---
id: "42427489816599"
titulo: "Boas práticas antes de realizar exclusões, edições em massa, importações e automações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427489816599-Boas-pr%C3%A1ticas-antes-de-realizar-exclus%C3%B5es-edi%C3%A7%C3%B5es-em-massa-importa%C3%A7%C3%B5es-e-automa%C3%A7%C3%B5es"
trilha: "PLOOMES: Automação de propostas  > Conceitos e dicas"
atualizado_em: "2026-08-11T16:14:38Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12116708", "sync_hash_31709b38b3f9"]
---

# Boas práticas antes de realizar exclusões, edições em massa, importações e automações

No Ploomes, algumas entidades podem sofrer exclusões em massa, como **clientes/contatos, workflows/funis e produtos**. Essas ações exigem cuidado, já que a exclusão de um cliente, por exemplo, remove também tudo o que está vinculado a ele. (Oportunidades, registros, documentos, propostas, vendas etc.)

Além disso, outras entidades podem ser **editadas em massa**, seja manualmente ou por meio de automações, como **propostas, documentos e vendas**. Isso significa que alterações aplicadas a uma regra ou condição podem impactar muitos registros de uma só vez.

🔔ATENÇÃO: Exclusões de dados são irreversíveis. Sempre siga boas práticas de backup e validação antes de realizar qualquer ação desse tipo, garantindo segurança e evitando perdas.

## 🔐 Controle de Permissões de Perfil de Usuário

- Restrinja a exclusão de dados apenas ao perfil de **Administrador**.
- Defina perfis de usuários que possam **editar, mas não excluir** dados sensíveis.
- Assim, você reduz riscos de exclusões acidentais.

  [Confira aqui como verificar permissões de perfil](https://sankhya.zendesk.com/hc/pt-br/articles/42427651167383)

## 📋 Planejamento da ação

- **Revise os filtros e condições** aplicados antes de confirmar qualquer ação em massa.
- **Teste em pequena escala** sempre que possível, antes de aplicar em todo o conjunto de dados.
- Para automações de edição, **revise os gatilhos e condições** com atenção antes de ativá-las.
- **Crie versões de teste** em registros limitados para validar o comportamento esperado.
- Utilize **filtros de ID, marcadores** ou critérios semelhantes para que a ação seja aplicada apenas em dados de teste.

  **Veja na prática como isso acontece:**

  1. Ao configurar uma **automação periódica**, um aviso com o número de itens que serão afetados é exibido na região dos filtros.

  ![Imagem 1: Utilize filtros de ID, marcadores ou critérios semelhantes para que a ação seja aplicada apenas em dados de teste. Veja…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1699399595/21651b4562b65a0fc430c3b5c6eb/image.png?expires=1786536000&signature=43709891f75df351f36fbf2e0fdd175e29f1d6509195a7af0e453098a0d68050&req=dSYuH8p3lIRWXPMW3nq%2BgUwbzMFuTtMgYQ%2Be%2FCMKB8kHSD6kGuUXkDaJBQf7%0Ay%2BSIOHjfqnhf3K01aIbVpygnjHE%3D%0A)

  2. Ao fazer uma edição e massa o número de itens afetados aparece ao lado do botão de confirmação e para fazer uma exclusão é necessário digitar "Excluir" após realizar essa ação a exclusão é irreversível.

  [GIF animado: Imagem 2: 2. Ao fazer uma edição e massa o número de itens afetados aparece ao lado do botão de confirmação e para fazer uma…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1703315864/738f0340440c3a0041f82ff9f8e0/edicao_em_massa.gif?expires=1786536000&signature=121731e9a201b471435b46e9804dcd47d7a165e7e648a6546206a20573095008&req=dScnFcp%2FmIlZXfMW3nq%2BgdGO%2F497kgFUDiWWp%2Fw0OL%2FxIXmM2v3vmDXtnxCk%0AzUH91MzD2lJ7GEwse2NBWfDIEls%3D%0A)

## 💾 Use abas como apoio para backup e faça exportação

- **Crie uma aba** com os dados que serão alterados ou excluídos, para acompanhar o impacto da ação.
- Sempre **inclua o campo ID** na exportação — ele será a chave para identificar registros e facilitar correções em caso de necessidade após a ação.
- **Antes de qualquer ação, exporte os dados que serão impactados.**
- **Mantenha uma pasta interna organizada de backups**, com data e descrição da ação, para facilitar consultas futuras.
- Em caso de erro, o **rollback é simples**: basta reimportar o arquivo exportado.
- Você também pode aplicar os **mesmos filtros usados em automações** nas abas, para verificar previamente quais dados serão atingidos.

  ⚠️ **Atenção**: não é possível realizar importação de dados de **propostas, documentos e vendas**. Caso precise aplicar alguma ação nessas entidades, entre em contato com nosso time de suporte.

  [Confira aqui como utilizar abas](https://sankhya.zendesk.com/hc/pt-br/articles/42427636649879)

## 👀 Monitoramento pós-ação

- Após concluir a ação, faça uma auditoria imediata para verificar se o resultado foi o esperado.

- Registre em planilha ou histórico interno qual ação foi feita, quando e por quem.
- Se necessário, realize a importação de backup.

## ❌ Deletei um item que não deveria, e agora?

- **Atenção:** exclusões no Ploomes são **irreversíveis**. Uma vez deletado, o item não pode ser restaurado automaticamente.
- Porém, é possível acessar o item no **registro de modificação** para ver os dados e criar outro manualmente com as mesmas informações.
- Para isso, acesse: **Administração > Registros** e consulte as informações.

  Veja no exemplo abaixo:

  [GIF animado: Imagem 3: Veja no exemplo abaixo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1703327258/740480f2964e0ce1a765fe31a799/log_exclusao.gif?expires=1786536000&signature=386b383654c37af0018370234db04ea13901f0fdcb819453fc061e36ae15f165&req=dScnFcp8moNaUfMW3nq%2BgfqyRGLqOP6Gwh4ZTU0XmZgEAzlQwnWE3vcL7rbT%0AQLuxqVUeTkZHko75jqMcm%2B0O%2B6o%3D%0A)

Veja mais no artigo de [Registros de modificação e de navegação](https://sankhya.zendesk.com/hc/pt-br/articles/42427501276055).

## 🤝 Precisa de ajuda?

Se tiver **qualquer dúvida** ou não se sentir totalmente seguro em relação às ações no Ploomes, procure nosso time de suporte. Estamos à disposição para orientar e garantir que tudo seja feito da forma mais segura possível.

Nosso atendimento é de segunda a sexta, das 9h00 às 18h00.
