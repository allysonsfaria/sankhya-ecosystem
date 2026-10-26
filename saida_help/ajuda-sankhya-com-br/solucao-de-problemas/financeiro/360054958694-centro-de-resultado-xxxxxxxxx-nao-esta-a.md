---
id: "360054958694"
titulo: "Centro de Resultado XXXXXXXXX não está ativo ou não é analítico. Financeiro de Nro Único: XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360054958694-Centro-de-Resultado-XXXXXXXXX-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico-Financeiro-de-Nro-%C3%9Anico-XXXX"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:27:53Z"
rotulos: ["Configuração", "Movimentação Financeira", "Centro de Resultado", "TOP", "Financeiro", "não apagar", "Centro inativo não analítico", "Verificar produto ativar e marcar centro como analítico", "Usar CR de cabeçalho ou hierarquia testar novamente"]
---

# Centro de Resultado XXXXXXXXX não está ativo ou não é analítico. Financeiro de Nro Único: XXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16939450587543) MENSAGEM:**

Centro de Resultado XXXXXXXXX não está ativa ou não é analítico. Financeiro de Nro Único: XXXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16939450588567) SOLUÇÃO:**

Acesse primeiro o cadastro do produto utilizado no lançamento, aba **"Venda"** e verifique se o campo Centro de Resultado está preenchido.

![Imagem 3: Acesse primeiro o cadastro do produto utilizado no lançamento, aba "Venda" e verifique se o campo Centro de Resultado…](https://ajuda.sankhya.com.br/hc/article_attachments/14817006284567)

Caso o campo esteja preenchido, verifique no cadastro do centro de resultado se o mesmo é sintético e se está ativo, pois é necessário que os campos **"Analítico"** e **"Ativo"** estejam flegados.

![Imagem 4: Caso o campo esteja preenchido, verifique no cadastro do centro de resultado se o mesmo é sintético e se está ativo,…](https://ajuda.sankhya.com.br/hc/article_attachments/14817114985879)

Caso não tenha a configuração acima, realize os seguintes passos:

Identifique qual Centro de Resultado será utilizado para o lançamento do respectivo financeiro, considerando o comportamento do sistema, conforme abaixo:

![Imagem 5: Se o parâmetro "Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB" estiver habilitado, será utilizado o mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/16939450590999) Se o parâmetro **"Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB"** estiver habilitado, será utilizado o mesmo Centro de Resultado inserido no cabeçalho do lançamento;

![Imagem 6: Se o parâmetro "Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB" estiver habilitado, será utilizado o mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/13737341752471)

Nesse caso, altere o Centro de Resultado do lançamento ou certifique-se que esse esteja **ativo** e seja analítico, através de seu cadastro na tela **"Centros de Resultado"** (Caminho de acesso: Configurações » Cadastros » Gerencial » Centros de Resultado); Feito isso, teste o faturamento novamente.

![Imagem 7: Se o parâmetro citado no item 1 estiver desabilitado, o sistema segue a seguinte hierarquia para preenchimento do…](https://ajuda.sankhya.com.br/hc/article_attachments/16939450592791) Se o parâmetro citado no item 1 estiver desabilitado, o sistema segue a seguinte hierarquia para preenchimento do Centro de Resultado do Financeiro:

"Em específico para o Centro de Resultado, caso este não esteja informado no **Tipo de Negociação**, ele será preenchido no Financeiro da Nota, com o valor informado no **cadastro de "Vendedores/Compradores"**; não sendo este informado, será pega a informação da aba **"Identificação no cadastro de "Usuários"**; caso este também não esteja informado, o Centro de Resultado do Financeiro da Nota irá seguir ao preenchimento realizado no **"Cabeçalho da Nota**."

- Identificado o Centro de Resultado a ser utilizado, certifique-se que esse esteja **ativo** e seja analítico, através de seu cadastro na tela Centros de Resultado (Caminho de acesso: Configurações » Cadastros » Gerencial » Centros de Resultado). Feito isso, teste o faturamento novamente.

![Imagem 8: Identificado o Centro de Resultado a ser utilizado, certifique-se que esse esteja ativo e seja analítico, através de…](https://ajuda.sankhya.com.br/hc/article_attachments/14817274128535)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16939450593303) CAUSA:**

Ao tentar faturar o pedido com uma TOP que gera financeiro o sistema tentou inserir um Centro de Resultado que não é analítico ou não esta ativo, ou informar um centro de resultado no cadastro do produto que não é analítico.
