---
id: "https://developer.sankhya.com.br/docs/add-on-studio"
titulo: "Add-on Studio"
url: "https://developer.sankhya.com.br/docs/add-on-studio"
atualizado_em: "2025-11-10T23:35:43.000Z"
---

# Add-on Studio

Introdução geral ao Add-on Studio, o ambiente de desenvolvimento integrado para criar extensões.

O Add-on Studio é uma estrutura poderosa baseada em Gradle, criada para simplificar o desenvolvimento de add-ons para o Sankhya Om. Ele foi projetado para que você, desenvolvedor, possa criar soluções de forma eficiente, segura e alinhada às melhores práticas da plataforma.

Com o Add-on Studio, você pode:

* ✅ **Seguir as melhores práticas de desenvolvimento**: Crie add-ons bem estruturados com código organizado, modular e de fácil manutenção.
* 🧪 **Testar localmente**: Valide suas soluções em um ambiente controlado antes de publicar, garantindo a qualidade e reduzindo riscos.
* 🔄 **Integrar com seu Pipeline de CI/CD**: Automatize processos de build, testes e publicação com facilidade.
* 🚀 **Publicar**: Simplifique a distribuição do seu add-on, publicando-o diretamente da linha de comando ou pipeline.

***

### 🔧 Pré-requisitos

Antes de começar, garanta que seu ambiente de desenvolvimento esteja configurado corretamente.

| Ferramenta / Conhecimento | Detalhes                                                                                                    |
| :------------------------ | :---------------------------------------------------------------------------------------------------------- |
| **Conta Sankhya ID**      | Permissão na Área do Desenvolvedor para desenvolver                                                         |
| **Acesso**                | [Área do Desenvolvedor](https://areadev.sankhya.com.br)                                                     |
| **Java (JDK)**            | Versão recomendada pela Sankhya [(Consulte Aqui)](https://downloads.sankhya.com.br/downloads?app=JAVA\&c=1) |
| **Gradle**                | Instalado e configurado no `PATH` do sistema, ou integrado a IDE. Intellij Gerencia automaticamente.        |
| **Conhecimento Básico**   | Desenvolvimento de add-ons para o Sankhya Om                                                                |

> **Nota:** Manter seu ambiente atualizado conforme as recomendações da Sankhya é crucial para evitar problemas de compatibilidade.

***

### 🚀 Passo a passo para começar

1. **Crie o Componente**: Na Área do Desenvolvedor, crie um novo **Componente** para seu add-on. [(Saiba mais)](https://developer.sankhya.com.br/docs/portal-do-desenvolvedor)
2. **Baixe o Template**: Após a criação, o botão **“Baixar Template”** estará disponível. Faça o download.
3. **Extraia o Projeto**: Descompacte o arquivo em seu ambiente de desenvolvimento.
4. **Configure o Ambiente**: Ajuste as dependências e variáveis de ambiente conforme as instruções do projeto.
5. **Desenvolva**: Comece a desenvolver seu add-on, seguindo a estrutura sugerida.
6. **Teste Localmente**: Utilize as ferramentas do Add-on Studio para realizar testes locais.
7. **Automatize**: Integre seu projeto a um pipeline de CI/CD para automatizar builds e testes.

***

### ✨ Boas Práticas

* **Modularize seu Código**: Separe as responsabilidades em diferentes packages(MVC, Clean Architecture, Hexagonal, etc) para facilitar a manutenção.
* **Documente Tudo**: Crie uma documentação clara para seu código e para o usuário final.
* **Use Testes Automatizados**: Garanta a qualidade e a estabilidade do seu add-on com testes unitários e de integração.
* **Gerencie Dependências**: Utilize o `build.gradle` para gerenciar as dependências do projeto de forma explícita.

```groovy
// Exemplo de como declarar dependências no build.gradle
dependencies {
    implementation 'br.com.sankhya.commercial:sankhya-models:1.0.0'
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.8.1'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.8.1'
}
```

***

### 🚫 Anti-Patterns (O que evitar)

* **Código Monolítico**: Evite criar um único módulo com toda a lógica do add-on.
* **"Hardcoding" de Informações**: Não fixe valores como senhas, tokens ou URLs diretamente no código. Use variáveis de ambiente ou as configurações do add-on.
* **Ignorar Testes**: Nunca subestime a importância dos testes. A ausência deles pode levar a falhas inesperadas em produção.
* **Falta de Documentação**: Um add-on sem documentação é difícil de usar e manter, tanto para outros desenvolvedores quanto para os usuários.

***

### ❓ Perguntas Frequentes (FAQ)

**Como configuro o ambiente de desenvolvimento?**\
Consulte o artigo **[“Configuração Inicial do Add-on Studio”](https://developer.sankhya.com.br/docs/configuracao-inicial)** para um guia detalhado sobre a instalação do JDK, Gradle e outras dependências.

**É possível testar add-ons sem publicar no MarketPlace?**\
Sim! O Add-on Studio foi feito para isso. Ele permite testes locais completos, garantindo maior controle de qualidade antes da publicação.

**É possível distribuir add-ons sem publicar no MarketPlace?**\
Sim! Basta seguir o artigo **["Como criar uma solução de uso exclusivo do cliente"](https://developer.sankhya.com.br/docs/criar-uma-solucao-de-uso-exclusivo-do-cliente)**.

**Como posso tirar dúvidas?**\
Para dúvidas, sugestões e troca de conhecimento, utilize a sala [Sankhya Developers](https://community.sankhya.com.br/developers) na comunidade Sankhya Developer. É o local ideal para interagir com outros desenvolvedores e com a equipe da Sankhya.
