---
id: "34894300284183"
titulo: "Não foi encontrado item de tarefa pendente (Ressuprimentos/Restrições)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34894300284183-N%C3%A3o-foi-encontrado-item-de-tarefa-pendente-Ressuprimentos-Restri%C3%A7%C3%B5es"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:28Z"
rotulos: ["Configuração", "WMS", "Estoque", "Erro", "Não foi encontrado item de tarefa pendente", "Ressuprimentos pendentes", "Restrições de usuários/equipamento", "Agrupamento de pedido em sep. convencional", "(Ressuprimentos/Restrições)", "Ressuprimentos", "Restrições"]
---

# Não foi encontrado item de tarefa pendente (Ressuprimentos/Restrições)

**MENSAGEM**

Não foi encontrado item de tarefa pendente: Possíveis causas: Ressuprimentos pendentes. Restrições de usuários/equipamento. Agrupamento de pedido em sep. convencional.

**SITUAÇÃO**

A mensagem aparece quando o usuário tenta **iniciar uma separação** no sistema WMS, mas não consegue prosseguir devido a **dependências pendentes**, **restrições de configuração** ou **incompatibilidades entre equipamento e endereços**.

**SOLUÇÃO**

**(1)** Acesse a tela **"Gerência do WMS"** (WMS » Gerência » Gerência do WMS), filtre a separação que será iniciada e verifique em **"Itens da Tarefa"** o campo **"Depende de outras"**. Se estiver marcado como **"Sim (Pendente)"**, clique no botão **"Dependentes"** para identificar a tarefa dependente. Caso seja reabastecimento, realize o reabastecimento antes de iniciar a separação.

**(2)** Acesse a tela **"Tipos de Equipamento"** (WMS » Cadastros » Tipos de Equipamento), identifique o equipamento utilizado e valide o **nível mínimo**, **nível máximo**, **tarefas permitidas** e **unidades permitidas** para o equipamento.

**(3)** Acesse a tela **"Endereço de Armazenamento"** (WMS » Cadastros » Endereço de Armazenamento), filtre o endereço de origem e destino e valide o nível do endereço na aba **"Medidas"**, campo **"Nível"**. O nível do equipamento deve estar dentro do nível do endereço de origem e destino.

**(4)** Acesse a tela **"Configurações por Usuário"** (WMS » Rotinas » Configurações por Usuário), filtre o usuário executante e valide as **unidades permitidas** e **tarefas permitidas** para o usuário.

**(5)** Acesse a tela **"Área de Separação"** (WMS » Cadastros » Área de Separação), filtre a área de separação da tarefa e verifique se o usuário separador está cadastrado dentro da área de separação na aba **"Separadores"**.

**CAUSA**

A mensagem ocorre quando existe um **ressuprimento pendente**, **restrição de usuário ou equipamento**, ou **falta de configuração** para o separador no sistema WMS.
