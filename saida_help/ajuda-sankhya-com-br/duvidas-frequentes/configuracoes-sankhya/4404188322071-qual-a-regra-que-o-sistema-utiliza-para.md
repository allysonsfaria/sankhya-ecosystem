---
id: "4404188322071"
titulo: "Qual a regra que o sistema utiliza para sugerir local na venda? "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404188322071-Qual-a-regra-que-o-sistema-utiliza-para-sugerir-local-na-venda"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:23:25Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "TOP", "Vendas", "Estoque", "não apagar", "#validadoTiagoBarbosa", "Regra de Sugestão de Local na Venda"]
---

# Qual a regra que o sistema utiliza para sugerir local na venda? 

Na inclusão de itens em uma nota de venda, o sistema pode sugerir o local padrão, dessa forma, o processo de inserção nas notas pode ser agilizado e menos erros referentes às informações de locais nas notas de vendas podem ser evitados.

**O sistema acompanha a hierarquia a seguir para buscar o local no lançamento de vendas:**

![Imagem 1: Busca o local informado na aba "Impostos por Empresa" (TGFPEM) do cadastro do produto para a empresa do cabeçalho. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16345731110935) Busca o local informado na aba **"Impostos por Empresa"** (TGFPEM) do cadastro do produto para a empresa do cabeçalho.
Caso exista local informado e seja diferente de zero esse será o local usado, senão vai para a opção 2.

![Imagem 2: Busca o local informado na aba "Impostos por Empresa" (TGFPEM) do cadastro do produto para a empresa do cabeçalho. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16345731113879) Busca o local informado nas preferências da empresa utilizada no cabeçalho da nota.
Caso exista local informado e seja diferente de zero esse será o local usado, senão vai para a opção 3.

![Imagem 3: Busca o local informado na aba "Impostos por Empresa" (TGFPEM) do cadastro do produto para a empresa do cabeçalho. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16345731116439) Caso o parâmetro **"REPETELOCALANT"** esteja ligado, a aplicação buscará o local do item lançado anteriormente.
Caso exista local informado e seja diferente de zero esse será o local usado, senão vai para a opção 4.

![Imagem 4: Busca o local informado na aba "Impostos por Empresa" (TGFPEM) do cadastro do produto para a empresa do cabeçalho. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16345731117975) Caso a opção **"Sugerir local padrão do parceiro?"** do cadastro da TOP utilizada no lançamento esteja marcada e exista informação no campo **"Parceiro Remetente"** do lançamento, sendo VENDAS o sistema buscará o local do parceiro remetente.
Caso exista local informado e seja diferente de zero esse será o local usado, senão vai para a opção 5.

![Imagem 5: Busca o local informado na aba "Impostos por Empresa" (TGFPEM) do cadastro do produto para a empresa do cabeçalho. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16345747205399) Busca o local do cadastro do produto.
Caso exista local informado e seja diferente de zero esse será o local usado, senão vai para a opção 6.

![Imagem 6: Busca o local informado na aba "Impostos por Empresa" (TGFPEM) do cadastro do produto para a empresa do cabeçalho. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16345731126679) Busca o local do parâmetro **"LOCALPADRAO"** (Esse parâmetro é por usuário).
Caso exista local informado e seja diferente de zero esse será o local usado, senão vai para a opção 7.

![Imagem 7: Busca o local informado na aba "Impostos por Empresa" (TGFPEM) do cadastro do produto para a empresa do cabeçalho. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16345747207959) Caso o parâmetro **"INFMINLOC"** esteja ligado a aplicação buscará na tabela de estoque (TGFEST) o menor local com estoque para esse produto, obedecendo as restrições para local da TOP e a informação do parâmetro **"FILEMPLOCALEST"**.
