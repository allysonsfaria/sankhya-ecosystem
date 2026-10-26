---
id: "8296928689687"
titulo: "Modelo padrão não encontrado no sistema, saiba como proceder"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8296928689687-Modelo-padr%C3%A3o-n%C3%A3o-encontrado-no-sistema-saiba-como-proceder"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-12T13:43:39Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "TOP", "Natureza", "não apagar", "Modelo padrão ausente", "Configure modelos de notas", "Importação sem configuração"]
---

# Modelo padrão não encontrado no sistema, saiba como proceder

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16593458482967) MENSAGEM:**

Modelo padrão não encontrado no sistema.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16593433336983) SITUAÇÃO:**

Ao tentar importar um XML no portal de Importação de XML a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16593458489495)SOLUÇÃO:**

É necessário algumas configurações de modelo de notas para que a importação seja bem sucedida. São elas:

**![Imagem 4: Modelo de Notas na tela: "Modelo de Notas e Pedidos" :](https://ajuda.sankhya.com.br/hc/article_attachments/16593458491031) Modelo de Notas na tela:** [**"Modelo de Notas e Pedidos"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514)**:**

Cadastre um modelo que será associado à empresa, que servirá de base para a Nota de Compra com as informações que não estão contidas no XML como: TOP (tipo de movimento compra), Natureza, Centro de Resultado etc. O Tipo de Negociação informado no modelo poderá ser utilizado na importação em algumas situações.

![Imagem 5: Modelo de importação de XML na tela: "Preferências da Empresa" :](https://ajuda.sankhya.com.br/hc/article_attachments/16593433345303) **Modelo de importação de XML na tela:** [**"Preferências da Empresa"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)**:**

Inclua no cadastro da empresa um ou mais modelos de importação através da aba **"Modelo de Importação de XML"**. Deve ser informada, além do modelo de notas e pedidos, a **"Natureza da operação"**. Pode-se ter vários modelos cadastrados por empresa, mas é obrigatório que exista um modelo de importação padrão, não sendo possível ter mais de um modelo padrão cadastrado por empresa.

No momento da importação do XML nesta tela, quando o sistema buscar o modelo de importação de XML, ele verificará o campo<natOp>do XML e o campo**" Natureza da Operação"**. Ambos os valores dos campos deverão ficar com letras maiúsculas e sem acento ou cedilha.

Em seguida, o sistema verificará o valor do campo **"Pesquisa da nat. de operação"** também presente nas Preferências da Empresa, aba [**"Modelo de Importação de XML"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893#abamodelodeimportaodexml) e adotará o seguinte comportamento, de acordo com a definição do referido campo:

(1)** Igual:** compara-se o texto do campo <**natOp**> com o campo **"Natureza da Operação"**, de modo que somente será utilizado o modelo de importação, caso os valores sejam exatamente iguais;

(1)** Contendo:** é feita a comparação do texto do campo <**natOp**> com o campo Natureza da Operação no qual, somente será utilizado o modelo de importação caso o valor do campo Natureza da Operação esteja contido no campo <**natOp**>;

(1)** Começando com:** compara-se o texto do campo <**natOp**> com o campo Natureza da Operação de modo que somente será utilizado o modelo de importação caso o valor do campo <**natOp**> seja iniciado com o valor do campo Natureza da Operação;

(1)** Terminando com:** é feita a comparação do texto do campo <**natOp**> com o campo Natureza da Operação no qual, somente será utilizado o modelo de importação caso o valor do campo <**natOp**> termine com o valor do campo Natureza da Operação.

**OBSERVAÇÃO:** Se já existem **modelos cadastrados na aba Modelo de Importação de XML e o erro persistir**, **verifique se algum deles está marcado como Padrão**. Sem essa marcação em pelo menos um modelo, a importação falha. Marque manualmente um dos modelos existentes como Padrão

**Importante:** caso deseje poderá verificar o manual completo no link abaixo:

[Portal de importação de XML – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjoxNTIwMDAxOTI1ODgyLCJ0aWNrZXRfaWQiOjE4ODkxNiwiY2hhbm5lbF9pZCI6NjMsInR5cGUiOiJTRUFSQ0giLCJleHAiOjE2NTM4NDMyMjZ9.vsiwdHYXQMgZ9rYCgzwm3DvggTHoqToVEbkLD7dy_5M)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16593458497303)CAUSA:**

Ocorre ao tentar importar um XML e não existe um modelo de notas devidamente configurado.
