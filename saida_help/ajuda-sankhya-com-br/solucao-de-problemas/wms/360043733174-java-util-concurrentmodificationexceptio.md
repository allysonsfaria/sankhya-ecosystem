---
id: "360043733174"
titulo: "Java.util.ConcurrentModificationException ocorre ao tentar logar no Coletor SuperWaba com o WildFly"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733174-Java-util-ConcurrentModificationException-ocorre-ao-tentar-logar-no-Coletor-SuperWaba-com-o-WildFly"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:59:22Z"
rotulos: ["Configuração", "WMS", "Superwaba", "Transporte", "ConcurrentModificationException", "Exclua arquivos temporários", "Incompatibilidade com WildFly", "WildFly", "Erro"]
---

# Java.util.ConcurrentModificationException ocorre ao tentar logar no Coletor SuperWaba com o WildFly

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16418071527447) MENSAGEM:**

'java.util.ConcurrentModificationException'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16418071531927) SITUAÇÃO:**

Ao tentar logar no Coletor SuperWaba, após a troca da Aplicação Jboss 4.0 para WildFly, ocorre a mensagem a seguir.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16418086182167) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse o diretório de instalação Coletor SuperWaba, nos computadores que apresentaram o problema e exclua os arquivos…](https://ajuda.sankhya.com.br/hc/article_attachments/16418071540887) Acesse o diretório de instalação Coletor SuperWaba, nos computadores que apresentaram o problema e exclua os arquivos temporários, deixando apenas os arquivos: **WMS.exe**, **WMS.pdb** e **WMS.prc**.

Ex: C:\SuperWaba\WMS

![Imagem 5: Ex: C:\SuperWaba\WMS](https://ajuda.sankhya.com.br/hc/article_attachments/360058926214)

![Imagem 6: Após a exclusão repita o procedimento em todos os computadores que usam o aplicativo Coletor SuperWaba e acesse…](https://ajuda.sankhya.com.br/hc/article_attachments/16418071544599) Após a exclusão repita o procedimento em todos os computadores que usam o aplicativo Coletor SuperWaba e acesse novamente o coletor.

![Imagem 7: Após a exclusão repita o procedimento em todos os computadores que usam o aplicativo Coletor SuperWaba e acesse…](https://ajuda.sankhya.com.br/hc/article_attachments/360058926234)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16418071546263) CAUSA:**

Ocorre pois os arquivos temporários na pasta de instalação do SuperWaba não são suportados pelo WildFly.
