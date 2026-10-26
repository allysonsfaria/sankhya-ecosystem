---
id: "38294287877527"
titulo: "Erro ao carregar pop-up \"Página não está funcionando\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38294287877527-Erro-ao-carregar-pop-up-P%C3%A1gina-n%C3%A3o-est%C3%A1-funcionando"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-10T20:36:09Z"
rotulos: ["Configuração", "XML", "WildFly", "Erro", "Está página não está funcionando", "Undertow", "Limitação do servidor", "WildFly versão 23", "Documentos Eletrônicos"]
---

# Erro ao carregar pop-up "Página não está funcionando"

**MENSAGEM**

Está Página não está funcionando

**SITUAÇÃO**

Ao tentar abrir algum **pop-up** do sistema, o mesmo fica em branco ou apresenta a mensagem "está página não está funcionando".

**ATENÇÃO**:

O procedimento a seguir deve ser executado **exclusivamente por um Administrador de Sistemas com conhecimento em Linux** ou pela **equipe de Cloud**, caso o ambiente esteja hospedado em nuvem. Antes de iniciar, é **obrigatória a verificação da versão do WildFly em uso**. As configurações descritas neste procedimento **aplicam-se somente ao WildFly versão 23**. A execução em versões diferentes pode causar falhas na inicialização, comportamentos inesperados ou indisponibilidade do ambiente.

**SOLUÇÃO:**

**(1)** Acesse o arquivo **standalone.xml** dentro do servidor aplicação.

**(2)** Dentro do arquivo localize linha descrita como "**server name="**

![Imagem 1: (2) Dentro do arquivo localize linha descrita como " server name="](https://ajuda.sankhya.com.br/hc/article_attachments/38294316366743)

**(3)** Localize o **listener** configurado, que pode estar como **HTTP** ou **HTTPS**, especialmente se houver certificado SSL autoassinado configurado diretamente no **WildFly**.

![Imagem 2: (3) Localize o listener configurado, que pode estar como HTTP ou HTTPS , especialmente se houver certificado SSL…](https://ajuda.sankhya.com.br/hc/article_attachments/38294316367383)

**(4)** Na mesma linha, adicione o seguinte parâmetro:

```
 allow-unescaped-characters-in-url="true"
```

**Exemplo**:

![Imagem 3: Exemplo :](https://ajuda.sankhya.com.br/hc/article_attachments/38294287866647)

**(5)** Após realizar a alteração, salve o arquivo. Caso esteja utilizando o **vi** na linha de comando, execute `:wq!` para salvar e sair.

**(6)** Em seguida, reinicie o **WildFly** para que a configuração seja aplicada.

```
jb_startprod
```

**CAUSA:**

O erro acontece por uma limitação do **Undertow**, servidor utilizado pelo **WildFly**, que não permite alguns caracteres especiais na URL, como as chaves `{}`.

```
Referencia: https://datatracker.ietf.org/doc/html/rfc1738#page-3
```

O Undertow aplica essa restrição nas versões do WildFly, pois quando a URL de um pop-up é construída, podem ser utilizados caracteres especiais como `{}`, o que faz com que a requisição seja bloqueada.

![Imagem 4: O Undertow aplica essa restrição nas versões do WildFly, pois quando a URL de um pop-up é construída, podem ser…](https://ajuda.sankhya.com.br/hc/article_attachments/38586379869463)

Para permitir o uso desses caracteres e contornar essa limitação do servidor, deve ser adicionado o parâmetro `allow-unescaped-characters-in-url="true"` .

Alguns exemplos de telas que utilizam esse tipo de pop-up são:

- Portal de Importação XML
- Módulo Java
- Construtor de Componentes BI

![Imagem 5: Construtor de Componentes BI](https://ajuda.sankhya.com.br/hc/article_attachments/38294316371351)

![Imagem 6: Construtor de Componentes BI](https://ajuda.sankhya.com.br/hc/article_attachments/38294287869591)
