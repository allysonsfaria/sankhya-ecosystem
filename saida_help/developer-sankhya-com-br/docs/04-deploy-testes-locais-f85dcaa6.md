---
id: "https://developer.sankhya.com.br/docs/04_deploy_testes_locais"
titulo: "🧪 Testando e Publicando seu Add-on"
url: "https://developer.sankhya.com.br/docs/04_deploy_testes_locais"
atualizado_em: "2025-11-10T23:35:51.000Z"
---

# 🧪 Testando e Publicando seu Add-on

Depois de configurar o projeto, é hora de testar, depurar e, finalmente, publicar seu add-on. Este guia aborda o processo de deploy local para testes e o comando para publicação na Área do Desenvolvedor.

***

### 1. Testes em Ambiente Local (Deploy Local)

Antes de distribuir seu add-on, é crucial validá-lo em um ambiente local. Isso permite encontrar e corrigir bugs de forma rápida e segura.

#### a. Habilitando o Modo de Depuração (Debug)

Para depurar seu código Java enquanto ele roda no servidor, você precisa habilitar a porta de depuração no Wildfly.

1. **Inicie o Wildfly com o parâmetro`--debug`** . Esta é a forma mais simples e recomendada.

   ```shell
   # No Linux/macOS
   ./standalone.sh --debug

   # No Windows
   .\standalone.bat --debug
   ```

   Isso habilitará a depuração na porta padrão `8787`.

2. **Configure sua IDE para conectar ao processo remoto**.
   * No IntelliJ, vá em `Run > Edit Configurations...`.
   * Clique no `+` e selecione `Remote JVM Debug`.
   * Dê um nome para a configuração (ex: "Debug Wildfly Local").
   * Mantenha o `Host` como `localhost` e `Port` como `8787`.
   * Clique em `OK`.

Agora, você pode iniciar a sessão de depuração na sua IDE e colocar breakpoints no seu código.

#### b. Executando o Deploy Local

Com o Wildfly rodando, use o seguinte comando Gradle para limpar o projeto e fazer o deploy do seu add-on no servidor local:

```shell
./gradlew clean deployAddon
```

O Gradle irá compilar seu código, empacotar o add-on e copiá-lo para a pasta `deployments` do seu Wildfly.

<Callout icon="🔍" theme="default">
  ### **Verifique os Logs**: Acompanhe o console do Wildfly para garantir que o deploy foi bem-sucedido. Se houver erros, os logs são o primeiro lugar para procurar pistas.
</Callout>

***

### 2. Publicando o Add-on

Após validar seu add-on localmente, o próximo passo é publicá-lo na **Área do Desenvolvedor** para que possa ser distribuído aos clientes.

#### a. Comando de Publicação

O comando `publishAddon` envia seu add-on para a Área do Desenvolvedor. Ele requer suas credenciais do Sankhya ID e o caminho para sua chave de assinatura.

* **No Linux/macOS:**
  ```shell
  ./gradlew clean publishAddon \
    -Pemail="seu-email@sankhya.com.br" \
    -Ppassword="sua-senha" \
    -PprivateKey="/caminho/para/sua/assinatura.key"
  ```

* **No Windows (PowerShell):**
  ```powershell
  ./gradlew clean publishAddon `
    -Pemail="seu-email@sankhya.com.br" `
    -Ppassword="sua-senha" `
    -PprivateKey="C:\caminho\para\sua\assinatura.key"
  ```

<Callout icon="🔐" theme="default">
  ### **Segurança**: **Nunca** exponha sua senha diretamente na linha de comando em ambientes de CI/CD. Use secrets ou variáveis de ambiente. Para desenvolvimento local, considere usar o `local.properties` para armazenar suas credenciais.
</Callout>

***

### ✨ Boas Práticas

* **Automatize com CI/CD**: Integre os comandos `deployAddon` (para um ambiente de homologação) e `publishAddon` em seu pipeline de CI/CD (GitHub Actions, GitLab CI, Azure DevOps).
* **Use Variáveis de Ambiente para Credenciais**: Em seu pipeline, armazene o e-mail, a senha e a chave privada como "secrets".
  ```shell
  # Exemplo em um script de CI/CD
  ./gradlew clean publishAddon \
    -Pemail="$SANKHYA_EMAIL" \
    -Ppassword="$SANKHYA_PASSWORD" \
    -PprivateKey="$SANKHYA_PRIVATE_KEY_PATH"
  ```
* **Verifique a`plataformaMinima`** : Antes de publicar, certifique-se de que a versão mínima do Sankhya Om definida no `build.gradle` é compatível com os ambientes dos seus clientes.
* **Revise os Logs de Publicação**: Sempre verifique o output do comando `publishAddon` para confirmar que o processo foi concluído sem erros.

### 🚫 Anti-Patterns (O que evitar)

* **Publicar sem Testar**: Nunca execute `publishAddon` sem antes ter validado exaustivamente o add-on com `deployAddon` em um ambiente local ou de homologação.
* **"Hardcoding" de Credenciais**: Comitar senhas ou chaves no seu repositório Git é uma falha grave de segurança.
* **Ignorar o Controle de Versão do Add-on**: Cada publicação deve corresponder a uma versão clara e bem definida do seu add-on (gerenciada no `build.gradle`). Não publique repetidamente a mesma versão com alterações diferentes.
* **Esquecer a Chave Privada**: O parâmetro `-PprivateKey` é **obrigatório**. A publicação falhará sem ele.
