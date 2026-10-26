---
id: "https://developer.sankhya.com.br/docs/faq"
titulo: "Perguntas Frequentes"
url: "https://developer.sankhya.com.br/docs/faq"
atualizado_em: "2025-11-10T23:37:04.000Z"
---

# Perguntas Frequentes

# 🔧 Configuração e Pré-requisitos

### Quais são os requisitos mínimos para usar o Add-on Studio?

* Java 1.8
* IDE como IntelliJ (recomendado), VS Code ou Eclipse
* Docker (para bancos de teste local - Oracle/SQL Server)
* WildFly 23.0 (para deploy local)
* Cadastro na [Área do Desenvolvedor Sankhya](https://areadev.sankhya.com.br/)

### Preciso pagar para usar o Add-on Studio?

Não, o Add-on Studio é gratuito para desenvolvedores registrados no ecossistema Sankhya.

### Como configuro o ambiente de desenvolvimento pela primeira vez?

* Baixe o [projeto modelo](https://sankhyadist.s3.sa-east-1.amazonaws.com/addon-template.zip)
* Siga o guia de [Preparação de Ambiente](https://developer.sankhya.com.br/docs/prepara%C3%A7%C3%A3o-de-ambiente-para-desenvolver-add-on)
* Configure os arquivos `settings.gradle` e `build.gradle` com o nome do seu projeto.
  * No arquivo `build.gradle` configure o `serverFolder` como no exemplo abaixo, para que seja apresentada a task `deployAddon`:

<Image align="center" src="https://files.readme.io/c41d68b3d8346cb928632248329e9be169c2345b437590625b8ed96e8fd1b5b3-image.png" />

<br />

***

# 🚀 Desenvolvimento

### Como estruturar meu add-on corretamente?

* Use o padrão de pastas:
  * `datadictionary/` para arquivos XML de metadados
  * `dbscripts/` para migrações de banco (ex: `V1.xml`, `V2.xml`)
  * `src/main/resources/META-INF/` para parâmetros (`parameters.xml`)

### Posso usar bibliotecas externas no meu add-on?

Sim, mas:

* Use `moduleLib` no `build.gradle` para libs específicas do add-on
* Evite conflitos com dependências nativas do Sankhya Om

### Como debuggar meu add-on localmente?

* Habilite o modo debug no WildFly
* Execute:
  ```bash
  ./gradlew clean deployAddon
  ```

para liberar a versão para teste local

***

# 📦 Publicação e Distribuição

### Como publicar meu add-on no Sankhya Place?

* Execute:
  ```bash
  ./gradlew publishAddon -Pusuario=email -Psenha=senha -PpublishPlace=true -PprivateKey=/caminho/chave.key
  ```
* A primeira publicação deve ser feita manualmente na [Área do Desenvolvedor](https://areadev.sankhya.com.br).

### Preciso assinar meu add-on? Como gerar a chave?

Sim! A chave de assinatura é obrigatória e pode ser obtida pelo administrador da Área do Desenvolvedor. Armazene o arquivo *.key* em um local seguro.

### Quanto tempo leva para o add-on ser aprovado?

O processo é automático, mas pode ser validado pela equipe Sankhya em casos específicos.

***

# 🔄 Migração e Compatibilidade

### Como migrar um projeto antigo (DWF) para o Add-on Studio?

Com os arquivos de metadados e scripts da última versão da Extensão gerada

Execute:

```
./gradlew importAndConvertDD -PlocationMetadata=pasta/metadata.xml -PlocationScripts=pasta/scripts/

```

### Meu add-on funciona em todas versões do Sankhya Om?

A versão mínima desde que superior a 4.28 pode deve ser definida a partir da variável:

```
snkmodule  {
   serverFolder = '${wildfly.home}' // /home/user/wildfly/
   plataformaMinima = "4.X"
}
```

as bibliotecas disponíveis viabiliza o desenvolvimento de soluções na versão corrente e duas anteriores.

### Posso desenvolver add-ons para o Sankhya Om Cloud?

Sim, todos os nossos clientes podem receber um add-on a depender apenas da versão em que o cliente esteja utilizando. Lembrando a instalação de soluções ocorre exclusivamente via loja de soluções.

***

# ❌ Solução de Problemas

### Erro ao fazer deploy local. O que verificar?

* WildFly está rodando?
* `serverFolder` no `build.gradle` aponta para o diretório correto?
* Logs do WildFly (`standalone/log/server.log`)

### Meu add-on não aparece no Sankhya Om após a instalação. Por quê?

* Verifique se a `appKey` no `build.gradle` está correta
* Confira os logs do servidor (erros de inicialização)

### Como atualizar um add-on já publicado?

* Incremente a versão no `build.gradle`
* Republique com `publishAddon`

### Falha na comunicação com nexus

Se receber o erro "FAILURE: Build failed with an exception."

Alterar no arquivo build.gradle o conteúdo:

```
url = uri("https://nexus-repository.sankhya.com.br/repository/maven-releases/")
```

para:

```gradle
url = uri("https://artifacts-partners.sankhya.com.br/repository/maven-releases")
```

Verificar o arquivo \*-model/build.gradle. Caso exista a tag repositories, a mesma deverá ser removida. O arquivo ficará parecido com o exemplo abaixo:

```gradle
dependencies {
    compileOnly 'org.projectlombok:lombok:1.18.24'
    annotationProcessor 'org.projectlombok:lombok:1.18.24'
}
test {
    useJUnitPlatform()
}
```

***

# 💡 Dicas de Boas Práticas

### Como garantir que meu add-on seja seguro e estável?

Teste em sandbox antes de publicar

* Use prefixos únicos para tabelas/parâmetros (ex: `nomeaddon_parametro`)
* Documente requisitos e compatibilidade

### Posso monetizar meu add-on?

Sim! No Sankhya Place, você pode definir modelos de licença.

### Onde busco ajuda adicional?

* [Documentação Oficial](https://developer.sankhya.com.br)
* [Comunidade de desenvolvedores Sankhya](https://community.sankhya.com.br/developers)
