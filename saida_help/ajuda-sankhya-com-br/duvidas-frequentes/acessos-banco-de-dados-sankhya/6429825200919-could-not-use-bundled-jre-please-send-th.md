---
id: "6429825200919"
titulo: "Could not use bundled JRE. Please send this log file to your software vendor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6429825200919-Could-not-use-bundled-JRE-Please-send-this-log-file-to-your-software-vendor"
trilha: "Dúvidas Frequentes > Acessos/Banco de Dados - Sankhya"
atualizado_em: "2026-07-22T15:16:21Z"
rotulos: ["Produtos", "Configuração", "Solução comum", "Mensagens de erro", "falta de dll's", "erro Windows dll", "Erro", "Windows"]
---

# Could not use bundled JRE. Please send this log file to your software vendor

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16457758063767) MENSAGEM**:

Mensagens de erro que podem ser apresentadas e têm a mesma solução:

Could not use bundled JRE. Please send this log file to your software vendor

The JVM found at .\jre is damaged. Please reinstall or define EXE4J\_JAVA\_HOME to point to an installed JDK or JRE.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457773704855) CAUSA:**

Falta de dll's específicas para o Sistema Operacional Windows.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457773709079) SOLUÇÃO:**

O instalador e o inicializador das aplicações Sankhya para Windows utilizam o install4j, que depende de dll's da Microsoft que só são incluídos por padrão no Windows 7 e superiores.
No Windows Server 2008, Windows XP e em algumas outras versões, instale o pacote "Microsoft Visual C++ 2010 Service Pack 1 Redistributable", disponível abaixo:
