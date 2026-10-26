---
id: "360044109354"
titulo: "Referência REPETIDO para o produto 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109354-Refer%C3%AAncia-REPETIDO-para-o-produto-X"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:55:09Z"
rotulos: ["Produtos", "Configuração", "Preferências", "ORA-20101", "Referência Repetida para 'X'", "Erro"]
---

# Referência REPETIDO para o produto 'X'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16609489333655) MENSAGEM:**

[ORA-20101]: Referência REPETIDO para o produto 'X'

[ORA-06512]: em "SANKHYA.TRG\_INC\_UPT\_TGFPRO\_REFERENCIA", line 49

[ORA-04088]: erro durante a execução do gatilho 'SANKHYA.TRG\_INC\_UPT\_TGFPRO\_REFERENCIA'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16609489334807) SOLUÇÃO:**

![Imagem 3: Caso necessite cadastrar mais de um produto utilizando a mesma referência, o parâmetro abaixo deve estar desligado :](https://ajuda.sankhya.com.br/hc/article_attachments/16609482108439) Caso necessite cadastrar mais de um produto utilizando a mesma referência, o parâmetro abaixo deve estar **desligado**:

- Tela **"Preferências**" (Caminho de acesso: Configurações » Avançado)
- Chave **"VALCODBARREPET - Validar Códigos de Barras repetido?**"
- Campo **"Ligado/Desligado"**: desligado

![Imagem 4: Campo "Ligado/Desligado" : desligado](https://ajuda.sankhya.com.br/hc/article_attachments/15021744231703)

![Imagem 5: Caso a repetição seja indevida, mantenha o parâmetro ligado e realize um filtro por referência, identificando os…](https://ajuda.sankhya.com.br/hc/article_attachments/16609482111255) Caso a repetição seja indevida, mantenha o parâmetro ligado e realize um filtro por referência, identificando os produtos que já a possuem e realizando os devidos ajustes.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16609482113047) CAUSA:**

Ao efetuar o cadastro de um produto, informando no campo 'Referencia' uma informação já existente para outro produto, a mensagem será apresentada.
