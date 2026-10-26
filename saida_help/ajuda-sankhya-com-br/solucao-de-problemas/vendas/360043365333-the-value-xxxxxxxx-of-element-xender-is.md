---
id: "360043365333"
titulo: "The value 'XXXXXXXX' of element 'xEnder' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043365333-The-value-XXXXXXXX-of-element-xEnder-is-not-valid"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:13Z"
rotulos: ["#PUBLIFER", "Configuração", "Parceiro", "NF-e", "Central de Vendas", "SEFAZ", "Valor 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' excede o limite de 60 caracteres", "Reduza o tamanho do endereço na tela 'Parceiros'", "Endereço com mais caracteres do que o permitido pela SEFAZ", "Erro"]
---

# The value 'XXXXXXXX' of element 'xEnder' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16453261162519) MENSAGEM:**

cvc-maxLength-valid: Value 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' with length = 'X' is not facet-valid with respect to **maxLength '60'** for type #AnonType\_xEndertransportatranspinfNFeTNFe'. 
cvc-type3.1.3: The value 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX' of element 'xEnder' is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453293208727) SITUAÇÃO:**

Ao realizar emissão de NF-e pela tela "[**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414)" no **SankhyaW**, a nota ficará com Status: 'Aguardando Correção'. Acessando a opção (**...**)>>**Ver Acompanhamento,** é possível consultar o detalhe da rejeição a seguir.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453293212567) SOLUÇÃO:**

Para correção seguir os passos abaixo:

![Imagem 4: Identificar através da mensagem retornada, qual é o endereço causador da rejeição.](https://ajuda.sankhya.com.br/hc/article_attachments/16453261169431) Identificar através da mensagem retornada, qual é o endereço causador da rejeição.

**Exemplo:**
The value '**Avenida MARIO GURGEL, 5030 SALA 101 SETOR CENTRO ADM AB'** of element 'xEnder' is not valid.

![Imagem 5: A mensagem está validando a quantidade de caracteres utilizados na descrição do respectivo endereço. É possível…](https://ajuda.sankhya.com.br/hc/article_attachments/16453293223447) A mensagem está validando a **quantidade de caracteres** utilizados na descrição do respectivo endereço. É possível identificar a quantidade de caracteres que foram utilizados e a quantidade esperada através da mensagem de validação. Veja o exemplo abaixo:

cvc-maxLength-valid: Value 'Avenida MARIO GURGEL, 5030 N. 5030 SALA 101 SETOR CENTRO ADM AB' **with length = '63'** is not facet-valid with respect to **maxLength '60'** for type

- Tamanho Atual: 63 caracteres
- Tamanho Esperado: 60 caracteres

![Imagem 6: Para solucionar a rejeição, acesse o cadastro de " Parceiros" (Caminho de acesso: Configurações » Cadastros) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16453293228183) Para solucionar a rejeição, acesse o cadastro de **"[Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)** (Caminho de acesso: Configurações » Cadastros), selecione o parceiro referente ao endereço rejeitado e na aba "**Endereço"** veja para qual dos campos é possível abreviar informações. Para o caso exemplificado seria possível abreviar o "**Complemento**":

![Imagem 7: Para solucionar a rejeição, acesse o cadastro de " Parceiros" (Caminho de acesso: Configurações » Cadastros) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/14395569114135)

![Imagem 8: Realizado o ajuste, redigite os dados do cabeçalho e gere um novo lote da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16453293235095) Realizado o ajuste, redigite os dados do cabeçalho e gere um novo lote da nota.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16453261181719) CAUSA:**

Mensagem apresentada quando a quantidade de caracteres enviadas para a tag de endereço é maior que a quantidade aceita pela SEFAZ.
