---
id: "25990416001047"
titulo: "Sugestão de Local de Venda no PDV Web"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25990416001047-Sugest%C3%A3o-de-Local-de-Venda-no-PDV-Web"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:18:27Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "TOP", "Estoque", "PDV Web", "LOCALPADRAO", "REPETELOCALANT", "FILEMPLOCALEST", "Sugestão de Local de Venda no PDV Web"]
---

# Sugestão de Local de Venda no PDV Web

No [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047), durante a inclusão de itens em uma nota de venda, o sistema pode sugerir o local padrão. Essa funcionalidade agiliza o processo de inserção e minimiza erros relacionados às informações de local nas notas de vendas.

O sistema segue a hierarquia abaixo para determinar o local durante o lançamento de vendas:

![Imagem 1: Busca o local informado no campo "Local Padrão" , da aba Impostos / Informações por Empresa do Cadastro de Produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/25990355417623) Busca o local informado no campo **"Local Padrão"**, da aba [Impostos / Informações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) para a empresa do cabeçalho.

Se houver um local informado diferente de zero, este será utilizado. Caso contrário, o sistema segue para a opção 2.

![Imagem 2: Busca o local informado no campo "Local Padrão" , da aba Estoque/Preço nas Preferências da Empresa utilizada no…](https://ajuda.sankhya.com.br/hc/article_attachments/25990415987863) Busca o local informado no campo **"Local Padrão"**, da aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo) nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) utilizada no cabeçalho da nota.

Caso exista local informado e seja diferente de zero esse será o local usado, do contrário passa para a opção 3.

![Imagem 3: Se o parâmetro "Repete último local digitado?- REPETELOCALANT" estiver ligado, a aplicação buscará o local utilizado no…](https://ajuda.sankhya.com.br/hc/article_attachments/25990355421591) Se o parâmetro **"Repete último local digitado?- REPETELOCALANT"** estiver ligado, a aplicação buscará o local utilizado no item lançado anteriormente.

No entanto, o parâmetro REPETELOCALANT só funcionará se houver uma configuração prévia para a escolha de local e pelo menos um item já tiver sido adicionado à venda. 

Se o local for diferente de zero, ele será utilizado; caso contrário, o sistema avança para a próxima opção.

![Imagem 4: Caso a opção "Sugerir local padrão do parceiro?" da aba Geral , do Tipo de Operação-TOP utilizada no lançamento, esteja…](https://ajuda.sankhya.com.br/hc/article_attachments/25990355424151) Caso a opção **"Sugerir local padrão do parceiro?"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), do [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) utilizada no lançamento, esteja marcada e exista informação no campo **"Parceiro Remetente"** do lançamento, o sistema buscará o local do parceiro remetente (campo **"Local padrão para produtos"**, aba [Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abainformaes), tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)).

Se o local for válido (diferente de zero), ele será usado; caso contrário, o sistema prossegue para a próxima opção.

![Imagem 5: Busca no Cadastro de Produtos .](https://ajuda.sankhya.com.br/hc/article_attachments/25990415992215) Busca no Cadastro de Produtos.

Se o local for diferente de zero, ele será utilizado; caso contrário, o sistema passa para a próxima opção.

![Imagem 6: Busca o local do parâmetro "Local Padrão para Pedidos e Notas - LOCALPADRAO" . Lembrando que esse parâmetro é por…](https://ajuda.sankhya.com.br/hc/article_attachments/25990415995031) Busca o local do parâmetro **"Local Padrão para Pedidos e Notas - LOCALPADRAO"**. Lembrando que esse parâmetro é por usuário. 

Se houver um local informado diferente de zero, ele será utilizado. Caso contrário, passa para a próxima opção.

![Imagem 7: Caso o parâmetro "Informa menor local de armazenagem com estoque-INFMINLOC" esteja ligado a aplicação buscará na tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/25990355434135) Caso o parâmetro **"Informa menor local de armazenagem com estoque-INFMINLOC"** esteja ligado a aplicação buscará na tabela de estoque (TGFEST) o menor local com estoque para esse produto, respeitando as restrições para local da TOP e a informação do parâmetro **"Filtro de empresas/local de estoque. - FILEMPLOCALEST"**.
