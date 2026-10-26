---
id: "https://developer.sankhya.com.br/docs/03_conf_addonstudio"
titulo: "⚙️ Configurando o Projeto do Add-on Studio"
url: "https://developer.sankhya.com.br/docs/03_conf_addonstudio"
atualizado_em: "2025-11-17T19:17:01.000Z"
---

# ⚙️ Configurando o Projeto do Add-on Studio

Guia para configurar o `build.gradle`, dependências, variáveis de ambiente e boas práticas iniciais.

Depois de preparar o ambiente, o próximo passo é configurar o projeto do seu add-on. Ajustar corretamente os arquivos `settings.gradle` e `build.gradle` é crucial para que o Gradle e o ecossistema Sankhya reconheçam e compilem sua solução.

Este guia detalha as configurações essenciais, a gestão de dependências e as boas práticas para construir um add-on otimizado.

> 📚 **Pré-requisito**: Se você ainda não configurou seu ambiente, consulte nosso guia de [Configurando o Ambiente de Desenvolvimento](https://developer.sankhya.com.br/docs/01_ambiente).

***

### 1. Ajustando o `settings.gradle`

Este arquivo é o coração da estrutura do seu projeto. Ele define o nome raiz e os módulos que o compõem. Sem essa configuração, o Gradle não consegue montar o projeto corretamente.

**Exemplo de configuração:**

```groovy
// Define o nome raiz do projeto. Use um nome único e descritivo.
rootProject.name = 'meu-addon-incrivel'

// Inclui os módulos que fazem parte do projeto.
// 'model' é para a lógica de negócio (backend).
// 'vc' é para componentes de tela (frontend, se aplicável).
include 'model'
include 'vc'
```

> 📘 **Dica:**
>
> * Escolha um nome para `rootProject.name` que reflita o propósito do seu add-on, como `financeiro-avancado` ou `gestao-estoque`.
> * O cliente do seu addon, poderá instalar apenas um addon com esse nome, então escolha com cuidado.

> 🚫 **Evite** usar nomes genéricos como `addon` para `rootProject.name`, pois isso pode causar conflitos se você tiver múltiplos projetos.

***

### 2. Configurando o `build.gradle` (Raiz)

O `build.gradle` na raiz do projeto define as configurações globais do build.

#### a. Identificação do Projeto (`group`)

O `group` é um identificador único para seus pacotes. A convenção é usar seu domínio reverso seguido do nome da aplicação.

**Exemplo:**

```groovy
// Se seu site é "minhaempresa.com.br" e o addon é "addonexemplo"
group = 'br.com.minhaempresa.addonexemplo'
```

**Importante:**\
Alguns grupos são reservados pela sankhya. Qualquer grupo que possua os nomes listados abaixo serão impedidos. Exemplos:

`br`, `br.com`, `sankhya`, `com.sankhya`, `br.com.sankhya`

#### b. Configuração do `snkmodule`

Este bloco informa ao Add-on Studio onde encontrar o servidor Wildfly e qual a versão mínima do Sankhya Om compatível.

```groovy
snkmodule {
    // Caminho para a pasta do Wildfly. O ideal é configurar no arquivo .env.
    serverFolder = System.getenv("WILDFLY_HOME") ?: '/opt/wildfly'
    
    // Versão mínima da plataforma Sankhya que seu add-on suporta.
    plataformaMinima = "4.15"
}
```

> **💡 Boa Prática:** Use um arquivo `.env` na raiz do projeto para definir a variável `WILDFLY_HOME`. Isso evita que caminhos locais fixos sejam compartilhados no controle de versão, facilitando a colaboração em equipe.

#### c. Configurações do Add-on

Este bloco vincula seu projeto à solução registrada na Área do Desenvolvedor.

```groovy
addon {
    // AppKey obtida ao registrar a solução na Área do Desenvolvedor.
    appKey = System.getenv("ADDON_APP_KEY")
    
    // Nome do parceiro (geralmente o nome da sua empresa).
    parceiroNome = "Minha Empresa"
}
```

> 🔐 **Segurança:** Nunca comite sua `appKey` diretamente no `build.gradle` em repositórios públicos. Use o arquivo `.env` (que não é versionado) para armazenar dados sensíveis.

#### d. Configurações de `dependencies` em `buildscript`

Para utilizar a versão 2.0 do Add-on Studio, é necessário garantir que as dependências abaixo estejam configuradas no buildscript:

```groovy
buildscript {

    dependencies {
        classpath "br.com.sankhya.studio:gradle-plugin:2+"
        classpath "com.google.devtools.ksp:symbol-processing-gradle-plugin:2.0.0-1.0.24"
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:2.0.0"
    }
}
```

***

### 3. Gerenciando Dependências

O Gradle já inclui um conjunto de dependências padrão essenciais para o desenvolvimento.

| Módulo `model`  | Módulo `vc` |
| :-------------- | :---------- |
| `mge-modelcore` | `dwf`       |
| `jape`          | `gson-2.1`  |
| `sanutil`       | `sanws`     |
| `mge-param`     | `jape`      |
| ...outras       | ...outras   |

Para adicionar outras dependências, você tem duas opções principais no `build.gradle` dos seus módulos (`model/build.gradle` ou `vc/build.gradle`):

* `implementation`: Usa uma biblioteca que **já existe** no Sankhya Om. O add-on não incluirá o `.jar` da biblioteca, apenas a usará em tempo de execução.
* `moduleLib`: **Incorpora** uma biblioteca ao seu add-on. Isso é útil quando você precisa de uma versão diferente da que existe no Sankhya Om ou uma biblioteca que não está presente.

**Exemplo prático:**

```groovy
dependencies {
    // Usa a biblioteca 'bsh' que já está no monolito.
    // O JAR não será empacotado no seu add-on.
    implementation('br.com.sankhya:bsh-1.3.0:master')
    
    // Empacota a biblioteca 'skw-environment' na versão 1.8.2 dentro do seu add-on.
    // Isso permite usar uma versão específica, diferente da do monolito.
    moduleLib('br.com.sankhya:skw-environment:1.8.2')
}
```

***

### ✨ Boas Práticas

* **Mantenha o Add-on Enxuto**: Use `implementation` sempre que possível para evitar inflar o tamanho do seu add-on com bibliotecas que já existem no ambiente Sankhya.
* **Declare Dependências Explicitamente**: Evite dependências transitivas não controladas. Declare o que você realmente precisa.
* **Use o `.env` para Dados Sensíveis**: Crie um arquivo `.env` na raiz do projeto (e adicione-o ao `.gitignore`) para armazenar chaves, senhas e configurações de ambiente.

  **Exemplo de arquivo `.env`:**

  ```properties
  # .env
  ADDON_APP_KEY=SUA_APP_KEY_AQUI
  WILDFLY_HOME=/opt/wildfly
  ```

  O Add-on Studio carrega automaticamente as variáveis deste arquivo, tornando-as disponíveis para o `build.gradle` através de `System.getenv()`.

### 🚫 Anti-Patterns (O que evitar)

* **"Fat JARs" Desnecessários**: Usar `moduleLib` para tudo resulta em um add-on grande e pesado, podendo causar conflitos de versão (`Jar Hell`).
* **Hardcoding de Caminhos e Chaves**: Fixar caminhos absolutos (como `C:\wildfly`) e chaves secretas no `build.gradle` dificulta o trabalho em equipe e cria riscos de segurança.
* **Nomes de Projeto Genéricos**: Usar `rootProject.name = 'addon'` pode causar colisões se você tiver múltiplos projetos. Seja específico.
* **Ignorar a `plataformaMinima`**: Não definir a versão mínima pode fazer com que seu add-on seja instalado em um ambiente incompatível, gerando erros em produção.
