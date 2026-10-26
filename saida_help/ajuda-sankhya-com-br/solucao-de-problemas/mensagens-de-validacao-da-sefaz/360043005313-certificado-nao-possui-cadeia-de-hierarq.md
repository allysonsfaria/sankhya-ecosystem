---
id: "360043005313"
titulo: "Certificado não possui cadeia de hierarquia CA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043005313-Certificado-n%C3%A3o-possui-cadeia-de-hierarquia-CA"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:15Z"
rotulos: ["ERRONF", "#RevisadoGui", "Configuração", "Certificado", "Segurança", "XML", "Exporte e importe certificado", "Falta de cadeia de certificação", "Certificado sem cadeia CA", "Documentos Eletrônicos"]
---

# Certificado não possui cadeia de hierarquia CA

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16315146758679) MENSAGEM:**

Certificado não possui cadeia de hierarquia CA.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16315157034391) **SOLUÇÃO:**

A cadeia de certificados é uma lista de certificados utilizada para autenticar uma entidade. A cadeia, ou caminho, começa com o certificado daquela entidade e cada certificado na cadeia é assinado pela entidade identificada pelo próximo certificado na cadeia. A cadeia termina com um certificado de CA raiz. O certificado de autoridade de certificação raiz é sempre assinado pela própria autoridade de certificação (CA). As assinaturas de todos os certificados na cadeia devem ser verificadas até que o certificado de CA raiz seja alcançado.

Para correção, siga os passos abaixo:

![Imagem 3: Abra o navegador em que o certificado foi previamente instalado. Normalmente, o mesmo é instalado no Internet Explorer.](https://ajuda.sankhya.com.br/hc/article_attachments/16315157035415) Abra o navegador em que o certificado foi previamente instalado. Normalmente, o mesmo
é instalado no Internet Explorer.

**(2)** Acesse as opções da internet no caminho Ferramentas » Opções da Internet » Aba Conteúdo » Certificados:

![Imagem 4: (2) Acesse as opções da internet no caminho Ferramentas » Opções da Internet » Aba Conteúdo » Certificados :](https://ajuda.sankhya.com.br/hc/article_attachments/360057726773)

![Imagem 5: Selecione o certificado que você quer exportar e clique em “Exportar:](https://ajuda.sankhya.com.br/hc/article_attachments/16315146769175) Selecione o certificado que você quer exportar e clique em “Exportar:

![Imagem 6: Selecione o certificado que você quer exportar e clique em “Exportar:](https://ajuda.sankhya.com.br/hc/article_attachments/360056837894)

![Imagem 7: Siga os passos a seguir realizando as marcações conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16315157042071) Siga os passos a seguir realizando as marcações conforme abaixo:

![Imagem 8: Siga os passos a seguir realizando as marcações conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360057726933)

![Imagem 9: Siga os passos a seguir realizando as marcações conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360057727413)

**![Imagem 10: OBSERVAÇÃO: NÃO marque a opção “Excluir a chave privada se a exportação tiver êxito”](https://ajuda.sankhya.com.br/hc/article_attachments/16315157043863) OBSERVAÇÃO:** **NÃO** marque a opção “Excluir a chave privada se a exportação tiver êxito”

![Imagem 11: OBSERVAÇÃO: NÃO marque a opção “Excluir a chave privada se a exportação tiver êxito”](https://ajuda.sankhya.com.br/hc/article_attachments/360056838114)

![Imagem 12: OBSERVAÇÃO: NÃO marque a opção “Excluir a chave privada se a exportação tiver êxito”](https://ajuda.sankhya.com.br/hc/article_attachments/360056838134)

![Imagem 13: Insira o nome do arquivo que será gerado na exportação.](https://ajuda.sankhya.com.br/hc/article_attachments/16315146778519) Insira o nome do arquivo que será gerado na exportação.

![Imagem 14: Insira o nome do arquivo que será gerado na exportação.](https://ajuda.sankhya.com.br/hc/article_attachments/360056838174)

![Imagem 15: Clique em concluir e o arquivo será gerado no caminho selecionado. Após realizada essa operação, importe o arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/16315146779543) Clique em concluir e o arquivo será gerado no caminho selecionado.
![Imagem 16: Clique em concluir e o arquivo será gerado no caminho selecionado. Após realizada essa operação, importe o arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/16315146781335) Após realizada essa operação, importe o arquivo gerado no Console do SanNFe.

**![Imagem 17: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16315157051543) CAUSA:**

Ocorre quando os certificados não foram gerados com a Cadeia de certificação das Autoridades que regulamenta a confiança do certificado, através de um criterioso processo de identificação, tornando-o um documento eletrônico confiável.

(1)** Artigos relacionados:**

**[Não é possível assinar xml a uf (GO) exige a cadeia de certificado.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042866074)**
