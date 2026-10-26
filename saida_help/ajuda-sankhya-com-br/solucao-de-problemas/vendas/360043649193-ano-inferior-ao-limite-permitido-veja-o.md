---
id: "360043649193"
titulo: "Ano inferior ao limite permitido, veja o parâmetro de Limite Inferior para Ano"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043649193-Ano-inferior-ao-limite-permitido-veja-o-par%C3%A2metro-de-Limite-Inferior-para-Ano"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:52Z"
rotulos: ["#criadoRoger", "Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "Ano abaixo limite", "Ajuste parâmetro \"LIMINFANO\"", "Verifique datas lançadas", "Erro"]
---

# Ano inferior ao limite permitido, veja o parâmetro de Limite Inferior para Ano

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16137522035607) MENSAGEM:**

Ano inferior ao limite permitido, veja o parâmetro de Limite Inferior para Ano.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16137522038551) SOLUÇÃO:**

![Imagem 3: Certifique-se que as datas envolvidas no processo foram lançadas de acordo com o esperado. Visto que essa situação pode…](https://ajuda.sankhya.com.br/hc/article_attachments/16137512464023) Certifique-se que as datas envolvidas no processo foram lançadas de acordo com o esperado. Visto que essa situação pode ocorrer por alguma falha de digitação, exemplo: Ao tentar definir uma data de vencimento como 01/01/2019, digita-se 01/01/1019.

![Imagem 4: Caso as datas estejam corretas, acesse a tela " Preferências " (Caminho de acesso: Configurações/Avançado) , busque…](https://ajuda.sankhya.com.br/hc/article_attachments/16137522041367) Caso as datas estejam corretas, acesse a tela **"[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)"** (Caminho de acesso: Configurações/Avançado), busque pela chave **"LIMINFANO"**, no campo **"Inteiro"** informe a quantidade de anos de retroação permitidos para movimentações/consultas no sistema.

![Imagem 5: Caso as datas estejam corretas, acesse a tela " Preferências " (Caminho de acesso: Configurações/Avançado) , busque…](https://ajuda.sankhya.com.br/hc/article_attachments/14664254846487)

![Imagem 6: Após ajuste do parâmetro quando se tratar de lançamentos nos Portais, por exemplo o faturamento de um Pedido de Venda,…](https://ajuda.sankhya.com.br/hc/article_attachments/16137522043287) Após ajuste do parâmetro quando se tratar de lançamentos nos Portais, por exemplo o faturamento de um Pedido de Venda, abra o lançamento de origem na Central e acione a opção **"Refazer Financeiro"** disponível no botão "**Outras Opções**".

![Imagem 7: Após ajuste do parâmetro quando se tratar de lançamentos nos Portais, por exemplo o faturamento de um Pedido de Venda,…](https://ajuda.sankhya.com.br/hc/article_attachments/14664199771287)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16137512474903)CAUSA:**

Mensagem apresentada ao tentar executar qualquer operação no sistema, com lançamentos e/ou títulos financeiros com limite de data de retroação superior ao definido no parâmetro **"LIMINFANO"**.
