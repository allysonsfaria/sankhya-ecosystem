---
id: "360043177914"
titulo: "O Acréscimo / Desconto Flex (XX) excedeu o Limite (YY) do Produto ZZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043177914-O-Acr%C3%A9scimo-Desconto-Flex-XX-excedeu-o-Limite-YY-do-Produto-ZZ"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:23Z"
rotulos: ["#criadoRoger", "#Revisadoclaudio", "CORE_E00398", "Produtos", "Configuração", "Preferências", "CORE_E00399", "CORE_E00400", "CORE_E00397", "Desconto/Acréscimo Flex excedeu limite", "Verificar e ajustar percentuais na aba Flex", "Ligação de parâmetros pode influenciar validações", "Erro"]
---

# O Acréscimo / Desconto Flex (XX) excedeu o Limite (YY) do Produto ZZ

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16161535997975) MENSAGEM**:

[CORE\_E00397] O Desconto Flex (XX) excedeu o Limite (YY) do Produto ZZ

[CORE\_E00398] O Acréscimo Flex (XX) excedeu o Limite (YY) do Produto ZZ

[CORE\_E00399] O Desconto Flex (XX) excedeu o Limite (YY) do Produto ZZ

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16161533306135) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Produtos » Produtos e vá até a Aba: Flex](https://ajuda.sankhya.com.br/hc/article_attachments/16161533306647) Acesse: Configurações » Cadastros » Produtos » Produtos e vá até a Aba: Flex

Quando se trabalha com Conta Corrente Flex é possível determinar faixas e percentuais máximo de acréscimo/desconto para determinados produtos. Então, caso se depare com a mensagem, consulte os %(percentuais) de desconto/acréscimo, verifique nos itens do pedido/nota qual é o percentual/valor de desconto ou acréscimo e faça os devidos ajustes.

![Imagem 4: Quando se trabalha com Conta Corrente Flex é possível determinar faixas e percentuais máximo de acréscimo/desconto para…](https://ajuda.sankhya.com.br/hc/article_attachments/14713435071511)

![Imagem 5: Lembrando que o campo " Vlr Acresc/Desc " apenas será exibido quando a chave de parâmetro " USACAMPOSADCCAR-Utiliza…](https://ajuda.sankhya.com.br/hc/article_attachments/16161533308183) Lembrando que o campo "Vlr Acresc/Desc" apenas será exibido quando a chave de parâmetro "**USACAMPOSADCCAR-Utiliza campos adicionais no carrinho?"** estiver ligado e for pela Central de Notas. Para ligá-lo, acesse a tela "**Preferências"** (Caminho de acesso à tela: Configurações » Avançado » Preferências) e informe a chave de parâmetro.

![Imagem 6: Lembrando que o campo " Vlr Acresc/Desc " apenas será exibido quando a chave de parâmetro " USACAMPOSADCCAR-Utiliza…](https://ajuda.sankhya.com.br/hc/article_attachments/14713484989463)

Ao ligar o parâmetro "**USACAMPOSADCCAR"** algumas validações são disparadas:

- O Acréscimo Flex (X) excedeu o Limite (X) do Produto X;
- O Desconto Flex (X) excedeu o Limite (X) do Produto X;
- O valor do desconto excedeu o saldo disponível do Parceiro X;
- Ao excluir um item que deixará o Saldo Flex negativo, será exibida a mensagem: "A exclusão deixará o saldo disponível do (vendedor/parceiro) X negativo";
- Ao alterar o valor de um item que deixará o Saldo Flex negativo, será apresentado a mensagem: "O valor do desconto excedeu o saldo disponível do (vendedor/parceiro) X".

Este campo não é atualizado na distribuição automática de descontos inseridos diretamente no rodapé da nota, independente dos parâmetros **"DISTJDCONF**" ou **"DISTDESCNFE"** estarem ligados ou não.
Não foi identificado nenhum ponto, independente de validação, que atualize o campo **"VLRACRESCDESC (Vlr. acresc./desc.)"**. Tratando-se de um comportamento do sistema.

![Imagem 7: Após os ajustes, continue com o lançamento do Pedido/Nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16161535999639) Após os ajustes, continue com o lançamento do Pedido/Nota.

**![Imagem 8: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16161533308823) CAUSA**:

Esta mensagem também pode ocorrer ao tentar duplicar um pedido/nota com desconto/acréscimo que talvez extrapole os percentuais máximos do cadastro dos produtos.
