---
id: "21631135942679"
titulo: "Configurações - Gerar registro 0220 utilizando UND enviada pelo Fornecedor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21631135942679-Configura%C3%A7%C3%B5es-Gerar-registro-0220-utilizando-UND-enviada-pelo-Fornecedor"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:49:59Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Parceiro", "EFD"]
---

# Configurações - Gerar registro 0220 utilizando UND enviada pelo Fornecedor

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21657027847959) **SITUAÇÃO:**

Melhores Praticas para gerar registro 0220 utilizando UND enviada pelo Fornecedor.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21631098150679)SOLUÇÃO:**

Para que esse processo funcione, temos um passo a passo a verificar:
 
Vimos que na Nota, o Produto foi feito a entrada como CX (CAIXA), que é a Unidade Alternativa que foi configurada no Produto.
 
Para que na Geração do 0220 o mesmo recebe a Unidade do Parceiro, no caso a Unidade configurada na tela Produtos, aba Produtos Equivalentes. É preciso validar as seguintes configurações.
 
![Imagem 3: Para que esse processo funcione, temos um passo a passo a verificar: Vimos que na Nota, o Produto foi feito a entrada…](https://ajuda.sankhya.com.br/hc/article_attachments/21657027857815) Acesse tela Preferencias > Empresa >> Aba EFD - Escrituração Fiscal Digital
 
Verifique se o Campo "Gerar registro 0220 utilizando UND enviada pelo Fornecedor" está marcado. Caso não esteja, para que a configuração do Registro 0220 levar a UND do Parceiro, o campo deve-se estar marcado.
 
![Imagem 4: Para que esse processo funcione, temos um passo a passo a verificar: Vimos que na Nota, o Produto foi feito a entrada…](https://ajuda.sankhya.com.br/hc/article_attachments/21657027873303) Tela Produtos, aba Unidade Alternativa >> Sub aba 0220 UND Conversão - EFD
 
![Imagem 5: Para que esse processo funcione, temos um passo a passo a verificar: Vimos que na Nota, o Produto foi feito a entrada…](https://ajuda.sankhya.com.br/hc/article_attachments/21657027888407)

Nessa tela é preciso configurar a devida opção para gerar o Registro 0220, onde temos 3 opções.
 
![Imagem 6: Nessa tela é preciso configurar a devida opção para gerar o Registro 0220, onde temos 3 opções. Opção Utiliza a Unidade…](https://ajuda.sankhya.com.br/hc/article_attachments/21657027857815) Opção Utiliza a Unidade Alternativa, sendo assim NÂO irá levar para o EFD a UNIDADE do Parceiro.
![Imagem 7: Nessa tela é preciso configurar a devida opção para gerar o Registro 0220, onde temos 3 opções. Opção Utiliza a Unidade…](https://ajuda.sankhya.com.br/hc/article_attachments/21657027873303) Opção utiliza a UND do Produto Equivalente, sendo assim essa opção irá levar a UNIDADE configurada na Aba Produtos Equivalentes, e assim levando ao registro 0220 a UNIDADE do Parceiro.
![Imagem 8: Nessa tela é preciso configurar a devida opção para gerar o Registro 0220, onde temos 3 opções. Opção Utiliza a Unidade…](https://ajuda.sankhya.com.br/hc/article_attachments/21657071922711) Opção "A Partir da Função", essa terceira opção seria utilizada na necessidade de criar um processo personalizado, liberado o acesso a uma Function, criada na implementação para uma função personalizada no Banco de Dados.
 
Após verificar a tela Unidade Alternativa, vamos para a segunda configuração.
 
![Imagem 9: Nessa tela é preciso configurar a devida opção para gerar o Registro 0220, onde temos 3 opções. Opção Utiliza a Unidade…](https://ajuda.sankhya.com.br/hc/article_attachments/21657071922711) Tela Produtos, aba Produtos Equivalentes.

 
![Imagem 10: Nessa tela, se deve configurar o seguinte: Código do Parceiro a fazer essa Utilização O Campo "UNIDADE" deve-se…](https://ajuda.sankhya.com.br/hc/article_attachments/21657071942423)
 
Nessa tela, se deve configurar o seguinte:

![Imagem 11: Nessa tela, se deve configurar o seguinte: Código do Parceiro a fazer essa Utilização O Campo "UNIDADE" deve-se…](https://ajuda.sankhya.com.br/hc/article_attachments/21657027857815) Código do Parceiro a fazer essa Utilização
![Imagem 12: Nessa tela, se deve configurar o seguinte: Código do Parceiro a fazer essa Utilização O Campo "UNIDADE" deve-se…](https://ajuda.sankhya.com.br/hc/article_attachments/21657027873303) O Campo "UNIDADE" deve-se configurar com a Unidade que foi utilizada na Nota. Por exemplo (Caso na Nota tenha sido utilizada a Unidade Alternativa CX (CAIXA), deve-se configurar o campo Unidade na tela Produtos Equivalentes como CX (CAIXA).
![Imagem 13: Nessa tela, se deve configurar o seguinte: Código do Parceiro a fazer essa Utilização O Campo "UNIDADE" deve-se…](https://ajuda.sankhya.com.br/hc/article_attachments/21657071922711) O Campo "UNIDADE DO PARCEIRO" deve-se configurar conforme a Unidade do Parceiro, sendo esse o campo que irá para o Registro 0220 conforme a Unidade que preencher.
 
Após fazer as configurações basta gerar o EFD - Fiscal e será levado ao Registro 0220 a UND configurada do Parceiro.
