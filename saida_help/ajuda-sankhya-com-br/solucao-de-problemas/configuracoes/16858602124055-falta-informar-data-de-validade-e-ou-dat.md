---
id: "16858602124055"
titulo: "Falta informar Data de Validade e/ou Data de Fabricação em alguns produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16858602124055-Falta-informar-Data-de-Validade-e-ou-Data-de-Fabrica%C3%A7%C3%A3o-em-alguns-produtos"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:54:16Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Preferências", "CORE_E04788", "Falta de Informação sobre Data de Validade e Fabricação em Produtos", "Erro"]
---

# Falta informar Data de Validade e/ou Data de Fabricação em alguns produtos

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16858638135319)  MENSAGEM:**

[CORE\_E04788] Falta informar Data de Validade e/ou Data de Fabricação em alguns produtos.
[ { Produto: xx, Lote: xxx} ].

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16858646476055) CAUSA:**

A solicitação de 'Data de Fabricação' e 'Data de Validade' acontecerá nas seguintes condições:

![Imagem 3: Tela Preferência (Configurações » Avançado) , parâmetros:](https://ajuda.sankhya.com.br/hc/article_attachments/16858602118167) Tela **Preferência** (Configurações » Avançado), parâmetros:

- **Usar data de Fabricação junto com Lote? - LOTEDTFAB**
- **Usar data de validade junto com Lote? - LOTEDTVAL**
- **Informações adicionais para** **Lotes? - LOTEINFO**

Se LIGADOS, para cada produto, as marcações detalhadas abaixo (Utiliza data de Fabricação  e Utiliza data de Validade**)**serão consideradas, e as datas de fabricação/validade exigidas:

![Imagem 4: Tela 'Produtos' (Configurações » Cadastros » Produtos):](https://ajuda.sankhya.com.br/hc/article_attachments/16858618262423) Tela 'Produtos' (Configurações » Cadastros » Produtos):

- **Utiliza data de Fabricação**
- **Utiliza data de Validade**

Os campos "Utiliza data de Fabricação" e "Utiliza data de Validade" estão relacionados ao controle de estoque de produtos; posto isto, se aplicam à produtos que utilizam controle adicional por número de lote e/ou data de validade (aba Medidas e Estoque, sub-aba Controle Adicional).

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/16858625048087) IMPORTANTE:**

Quando o parâmetro **"Usar data val. fab. junto com Lote, por produto? - LOTEDTVALFABPRO"** estiver ligado, o sistema exigirá as validações das marcações Utiliza data de Fabricação e Utiliza data de Validade.

![Imagem 6: Quando o parâmetro "Usar data val. fab. junto com Lote, por produto? - LOTEDTVALFABPRO" estiver ligado, o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/16866260273431) Tela **Produtos** (Configurações » Cadastros » Produtos)

Na aba **Estoque**, pode existir linhas de estoque sem Data de Validade e Data de Fabricação para o Lote apresentado na mensagem de erro. Deve ser avaliado o motivo de controlar data de validade e fabricação e não ter essa informação para o determinado Lote, assim tomando a melhor decisão naquele caso (exclusão, edição,...).

**![Imagem 7: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16858602119447) SOLUÇÃO:**

![Imagem 8: Verifique para o produto apresentado na mensagem da nota, o preenchimento das informações 'Data de validade' e 'Data de…](https://ajuda.sankhya.com.br/hc/article_attachments/16858618263959) Verifique para o produto apresentado na mensagem da nota, o preenchimento das informações 'Data de validade' e 'Data de fabricação':

- Central de Notas  >> Itens >> Outras Opções >> **Informações de Controle Adicional**

![Imagem 9: Central de Notas >> Itens >> Outras Opções >> Informações de Controle Adicional](https://ajuda.sankhya.com.br/hc/article_attachments/16858625049495)
