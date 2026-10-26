---
id: "30123356738839"
titulo: "\"UT005023: Exception handling request to /placemm/place/download: java.lang.OutOfMemoryError: Java heap space\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30123356738839--UT005023-Exception-handling-request-to-placemm-place-download-java-lang-OutOfMemoryError-Java-heap-space"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:36:31Z"
rotulos: ["Configuração", "Atualização", "WPM", "Passos para resolver", "Razão do erro", "Detalhe do erro", "add-on", "addon", "Java heap space", "OutOfMemoryError", "UT005023", "Erro", "SankhyaOm"]
---

# "UT005023: Exception handling request to /placemm/place/download: java.lang.OutOfMemoryError: Java heap space"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30123356728727) **MENSAGEM:**

"UT005023: Exception handling request to /placemm/place/download: java.lang.OutOfMemoryError: Java heap space"

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30891465970071) SITUAÇÃO:**

Esse erro ocorre ao **tentar instalar ou atualizar um add-on** no SankhyaOM. Durante esse processo, o sistema precisa alocar memória para manipular os arquivos e concluir a instalação, mas pode falhar devido a **limitações de memória disponíveis no ambiente**.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30123356729751)SOLUÇÃO:**

![Imagem 4: Garanta que o ambiente atenda aos requisitos mínimos recomendados para o SankhyaOM. O ideal é que o servidor tenha pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/31046593462167) **Garanta que o ambiente atenda aos requisitos mínimos** recomendados para o SankhyaOM. O ideal é que o servidor tenha **pelo menos 4GB de RAM** para um funcionamento adequado.

(1)** Método 1: Configuração via WPM (recomendado)**

- Acesse o **WPM** no SankhyaOM;
- Vá até a aba **Configurações;**
- Na seção **Configurações de memória do WildFly**, ajuste os valores de:

  - **Memória inicial (MB):** defina um valor adequado (exemplo: 4096 MB).
  - **Memória máxima (MB):** ajuste conforme necessário (exemplo: 8192 MB).
- Clique em **Salvar** e reinicie o servidor.

(1)** Método 2: Configuração manual no arquivo**

- No Windows, edite o arquivo `standalone.conf.bat` e ajuste a linha:

  ```
  set "JAVA_OPTS=%JAVA_OPTS% -Xms4096m -Xmx8192m"
  ```

- No **Linux**, edite o arquivo standalone.conf que está localizado em:

  ```
  /home/mgeweb/wildfly_XXXX/bin/standalone.conf
  ```

**![Imagem 5: Reinicie o servidor para aplicar as mudanças e tente novamente executar a instalação ou atualização do add-on.](https://ajuda.sankhya.com.br/hc/article_attachments/31046599841687) Reinicie o servidor** para aplicar as mudanças e tente novamente executar a instalação ou atualização do add-on.

**Atenção: os valores citados são apenas exemplos. A definição ideal deve considerar a quantidade total de RAM disponível no servidor e a demanda do ambiente.**

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30123356730391)CAUSA:**

O erro **"Java heap space"** indica que o Java atingiu o limite máximo de memória alocada, impossibilitando a execução da operação. Isso pode ocorrer por diversos motivos, incluindo:

- **Baixa quantidade de memória RAM disponível** no servidor/máquina onde o SankhyaOM está rodando.
- **Configuração inadequada da memória da JVM**, limitando a alocação necessária para processar a instalação do add-on.
