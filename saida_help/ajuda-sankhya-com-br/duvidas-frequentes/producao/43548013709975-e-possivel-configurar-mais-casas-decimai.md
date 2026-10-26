---
id: "43548013709975"
titulo: "É possível configurar mais casas decimais para o campo Quantidade na aba Tipos de Amostra, do cadastro do Produto?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548013709975-%C3%89-poss%C3%ADvel-configurar-mais-casas-decimais-para-o-campo-Quantidade-na-aba-Tipos-de-Amostra-do-cadastro-do-Produto"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-09-25T11:37:03Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# É possível configurar mais casas decimais para o campo Quantidade na aba Tipos de Amostra, do cadastro do Produto?

O campo **Quantidade** da aba **Tipos de Amostra**, na tela de **Produtos** (Configurações » Cadastros » Produtos » Produtos) **(QTDPORAMOSTRA - tabela TGFAMP)** é utilizado para registrar a quantidade por amostra em processos de controle de qualidade e produção no ERP Sankhya. Em alguns cenários, pode ser necessário aumentar a precisão desse campo, permitindo o registro de mais casas decimais para atender a processos industriais ou laboratoriais que exigem maior detalhamento.

![Imagem 1: O campo Quantidade da aba Tipos de Amostra , na tela de Produtos (Configurações » Cadastros » Produtos » Produtos)…](https://ajuda.sankhya.com.br/hc/article_attachments/43685519978263)

Por padrão, o sistema Sankhya utiliza duas casas decimais para a quantidade apontada. No entanto, **não** é possível configurar o sistema de forma nativa para aceitar mais casas decimais,

### Avalie os impactos

Ao aumentar o número de casas decimais através de personalização, verifique se os relatórios, integrações e demais processos que utilizam o campo **"QTDPORAMOSTRA"** estão preparados para lidar com a nova precisão. Recomenda-se alinhar a configuração com as necessidades do setor de qualidade e produção, evitando divergências.

Além disso, certifique-se de que os usuários estejam cientes da alteração, pois a digitação e visualização dos valores passarão a considerar mais casas decimais, o que pode impactar processos de conferência e análise.

### Observação

O aumento de casas decimais está condicionado à estrutura do banco de dados e às limitações do sistema. Em alguns casos, campos do banco podem ter restrições quanto ao número máximo de casas decimais suportadas. Caso a tamanho definido ultrapasse esse limite, o sistema pode arredondar ou truncar os valores automaticamente.

Evite definir um número excessivo de casas decimais para não comprometer a performance e a integridade dos dados. Sempre valide a necessidade real de precisão junto à área responsável e realize testes antes de aplicar a alteração em ambiente produtivo.
