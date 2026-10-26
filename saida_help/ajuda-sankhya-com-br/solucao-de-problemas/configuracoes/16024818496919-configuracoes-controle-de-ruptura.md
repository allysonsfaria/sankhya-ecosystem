---
id: "16024818496919"
titulo: "Configurações - Controle de Ruptura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16024818496919-Configura%C3%A7%C3%B5es-Controle-de-Ruptura"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:55:38Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "Análise de Giro", "Estoque", "Controle de Ruptura de Estoque", "ruptura"]
---

# Configurações - Controle de Ruptura

**![Solução](https://ajuda.sankhya.com.br/hc/article_attachments/16024860861975) SOLUÇÃO:**

A solução permitirá aos gestores de compra o controle da ocorrência de rupturas de estoque (períodos de indisponibilidade de estoque), bem como o acompanhamento das ações adotadas para evitar a reincidência.

A solução apresentará a quantidade de dias em que o produto estava indisponível no estoque. E ainda permitirá desconsiderar esse período do cálculo de vendas por dia útil (giro), tornando a estimativa de sugestão de compras giro e giro ajustado mais precisas e condizentes com a realidade da necessidade de reposição.

![Imagem 2: Configuração dos Produtos que se deseja controlar a Ruptura;](https://ajuda.sankhya.com.br/hc/article_attachments/16024815581719) Configuração dos Produtos que se deseja controlar a Ruptura;

- Configurações » Cadastros » Produtos » Produtos »  Aba Medidas e Estoques »  Estoque, Campo "Calcula Ruptura de Estoque?"

![Imagem 3: Configuração dos Grupos de produtos que se deseja controlar a Ruptura;](https://ajuda.sankhya.com.br/hc/article_attachments/16024875580183) Configuração dos Grupos de produtos que se deseja controlar a Ruptura;

- Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços »  Estoque, Campo "Calcula Ruptura de Estoque?:"

![Imagem 4: C onfiguração das Empresas que terão a Ruptura Calculada;](https://ajuda.sankhya.com.br/hc/article_attachments/16024818493719) Configuração das Empresas que terão a Ruptura Calculada;

- Comercial » Preferências » Empresa » Estoque/Preço, campo "Calcular Ruptura de Estoque?"

![Imagem 5: Visualização dos dias de Ruptura na grade da análise de giro;](https://ajuda.sankhya.com.br/hc/article_attachments/16024815584919) Visualização dos dias de Ruptura na grade da análise de giro;

**![Imagem 6: Observação:](https://ajuda.sankhya.com.br/hc/article_attachments/16805284720151) Observação:**

"Após realizadas todas as configurações de ruptura, é necessário aguardar 1 dia para que as informações sejam atualizadas e disponibilizadas. Isso ocorre pois as informações de ruptura são atualizadas todos os dias a 00:00 por um Job automatizado."

A Ruptura começa a contar a partir do dia que o parâmetro **"Executar verificação de Rupturas - EXECVERRUPTURA"** foi ligado.

**Exemplo:** hoje no final do dia o produto tem estoque (Não Ruptura), amanhã no final do dia o produto tem estoque (Não Ruptura), depois de amanhã no final do dia o produto NÃO tem estoque (Há Ruptura de estoque, nesse cenário o sistema contabiliza 1 dia de Ruptura).

**![Imagem 7: Importante:](https://ajuda.sankhya.com.br/hc/article_attachments/16805278615191) Importante:**

Caso o produto esteja com o campo 'Calcula Ruptura de Estoque?' marcado e pertencer a um grupo que não esteja com a configuração, prevalecerá a configuração do produto, do contrário, prevalecerá a configuração do grupo.

Após realizada todas as configurações de ruptura, é necessário aguardar 1 dia para que as informações sejam atualizadas e disponibilizadas. Isso ocorre porque as informações de ruptura são atualizadas todos os dias a 00:00 por um Job automatizado.

![Imagem 8: Os Dashboards são visualizados no Gerente online, relatório 'Ruptura de Estoque'.](https://ajuda.sankhya.com.br/hc/article_attachments/16024875585175)  Os Dashboards são visualizados no Gerente online, relatório 'Ruptura de Estoque'.
