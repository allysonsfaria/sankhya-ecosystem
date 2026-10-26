---
id: "https://developer.sankhya.com.br/docs/migrando-extensoes-que-usam-o-dwf-para-o-add-on-studio"
titulo: "Migração DWF para o Add-on Studio"
url: "https://developer.sankhya.com.br/docs/migrando-extensoes-que-usam-o-dwf-para-o-add-on-studio"
atualizado_em: "2026-03-09T12:03:12.000Z"
---

# Migração DWF para o Add-on Studio

<br />

# Migrando Extensões Desenvolvidas com DWF para o Add-on Studio

## Visão Geral

A manutenção de extensões desenvolvidas com o **DWF (Development Wizard Framework)** pode ser complexa, pois exige a restauração de backups do banco de dados e a configuração de um ambiente compatível com as ferramentas legadas.

Com o lançamento do **Add-on Studio**, esse processo se torna mais simples e eficiente, permitindo a evolução e manutenção das extensões diretamente na nova ferramenta, eliminando a dependência do DWF. Para isso, é necessário restaurar e importar o dicionário de dados para a nova estrutura.

***

## 📋 Pré-requisitos

Antes de iniciar a migração, certifique-se de ter:

* ✅ Backup completo do dicionário de dados legado (arquivo `.xml`)
* ✅ Scripts de banco de dados (`mssqlserver.sql` e `oracle.sql`)
* ✅ Código-fonte completo do add-on legado (classes Java e recursos)
* ✅ Projeto template configurado de acordo com as configurações do addon a ser migrado (veja seção [Configurando o Projeto do Add-on Studio](https://developer.sankhya.com.br/docs/03_conf_addonstudio))

***

## 🚀 Processo de Migração

A migração é dividida em três etapas principais:

1. **Configuração do Projeto Template**
2. **Importação e Conversão do Dicionário de Dados**
3. **Migração do Código-Fonte**

***

## 1. Configuração do Projeto Template

### Opção A: Criar nova solução via Área do Desenvolvedor

1. Acesse a [Área do Desenvolvedor Sankhya](https://areadev.sankhya.com.br)
2. Crie uma nova solução e um componente add-on, preenchendo as informações solicitadas.
3. Baixe o template do projeto e extraia-o em seu ambiente de desenvolvimento.
4. Configure de acordo com os passos descritos em [Configurando o Projeto do Add-on Studio](https://developer.sankhya.com.br/docs/03_conf_addonstudio)

### Opção B: Caso já tenha uma solução existente

1. Baixe o template do projeto e extraia-o em seu ambiente de desenvolvimento.
2. Configure de acordo com os passos descritos em [Configurando o Projeto do Add-on Studio](https://developer.sankhya.com.br/docs/03_conf_addonstudio)

### Estrutura Esperada do Projeto

Após criar o projeto template, você terá a seguinte estrutura:

```
meu-addon-migrado/
├── build.gradle
├── settings.gradle
├── gradle.properties
├── datadictionary/          # Metadados XML (será preenchido na importação)
├── dbscripts/               # Scripts de banco (será preenchido na importação)
├── model/                   # Módulo back-end
│   ├── build.gradle
│   └── src/
│       └── main/
│           ├── java/        # Código Java (migrar código legado aqui)
│           └── resources/
└── vc/                      # Módulo front-end
    └── src/
        └── webapp/
            └── html5/       # HTML, CSS, JS
```

***

## 2. Como Restaurar e Importar o Dicionário de Dados

Acessando o projeto template já configurado, dentro da sua IDE favorita (IntelliJ, VsCode, etc), siga os passos abaixo para importar o dicionário de dados legado.

### 2.1. Preparar os Arquivos Legados

Normalmente os arquivos serão encontrados em:

* `meu-projeto.war/WEB-INF/dictionary/metadata.xml`
* `meu-projeto.war/WEB-INF/script/mssqlserver.sql`
* `meu-projeto.war/WEB-INF/script/oracle.sql`

Caso contrário basta localizar os arquivos no seu computador.

**Organize seus arquivos em um diretório temporário:**

```
/meu-backup-dwf/
├── metadata.xml              # Dicionário de dados legado
└── scripts/
    ├── mssqlserver.sql      # Script SQL Server
    └── oracle.sql           # Script Oracle
```

### 2.2. Executar o Comando de Importação

A partir do terminal, aberto no diretório raiz do seu **projeto template configurado** e execute:

```bash
./gradlew importAndConvertDD -PlocationMetadata=/meu-backup-dwf/metadata.xml -PlocationScripts=/meu-backup-dwf/scripts/
```

> **🚧 ATENÇÃO**
>
> Substitua os caminhos pelos caminhos reais dos seus arquivos:
>
> * `locationMetadata` deve apontar para um arquivo `.xml`
> * `locationScripts` deve apontar para um **diretório** contendo os scripts SQL nomeados como `mssqlserver.sql` e `oracle.sql`

### 2.3. Resultado da Importação

O comando analisará o dicionário de dados legado e o adaptará para o novo formato. Os arquivos convertidos serão armazenados em:

* **`datadictionary/`** - Metadados estruturados por contexto (menus, tabelas, tabelas nativas etc.)
* **`dbscripts/`** - Scripts de banco versionados (V1.xml, V2.xml, etc.)

#### Estrutura de Metadados Gerada

Para melhor organização e manutenção, os metadados são estruturados separadamente:

```
datadictionary/
├── MEUMENU.xml            # Menus
├── MINHATABELA.xml        # Tabelas customizadas
├── NATIVE_TABLES.xml      # Extensões de tabelas nativas
```

> **❗️ IMPORTANTE**
>
> Durante a geração das tabelas, é **essencial definir a primary key corretamente** para garantir o perfeito funcionamento das funcionalidades associadas. Revise os XMLs gerados e valide as chaves primárias.
>
> Veja [Dicionário de Dados (Data Dictionary)](https://developer.sankhya.com.br/docs/01_dicionario-de-dados)

***

## 3. Migração do Código-Fonte

Após a importação do dicionário de dados, é necessário migrar o código Java legado para o novo projeto.

### 3.1. Copiar Estrutura de Pacotes

Copie a estrutura de pacotes do projeto legado para o novo projeto, mantendo a organização e a estrutura de pastas definidas nas configurações do build.gradle da raiz do projeto (ex:`group = br.com.empresa.addon`).

### 3.2. Copiar Arquivos de Resources

Copie arquivos da pasta resources caso existam do projeto legado para o novo projeto.

***

## 4. Problemas Comuns e Soluções

### Erros relacionados a "Primary key"

**Causa**: A tabela convertida não possui chave primária definida.

**Solução**: Edite o XML da tabela em `datadictionary/` e adicione a tag `<primaryKey>`:

```xml
<table name="MINHATABELA">
    <primaryKey>
        <field name="CODIGO"/>
    </primaryKey>
    <!-- ... -->
</table>
```

### Erro: "Arquivo fornecido não contém metadados válidos."

**Causa**: O caminho fornecido não aponta para um arquivo com estrutura válida para conversão.

**Solução**: Verifique se o conteúdo do arquivo é válido no formato esperado.

### Erro: "Arquivo fornecido não existe no caminho especificado ..."

**Causa**: O caminho fornecido para o arquivo de metadados ou scripts está incorreto ou o arquivo não existe.

**Solução**: Verifique se o caminho está correto e se o arquivo `.xml`

### Erro: "Pasta fornecida não existe no caminho especificado ..."

**Causa**: O diretório de scripts não existe ou está vazio.

**Solução**: Certifique-se de que o diretório contém os arquivos `mssqlserver.sql` e `oracle.sql`.

***

## 💡 Dicas Importantes

> **✅ Boas Práticas**
>
> * Sempre mantenha backup do código legado antes de iniciar a migração
> * Migre funcionalidades de forma incremental (feature por feature)
> * Utilize DTOs para entrada/saída de serviços (nunca exponha entidades)
> * Aproveite a migração para melhorar a arquitetura e aplicar padrões modernos
> * Configure versionamento de código (Git) desde o início
>
> **⚠️ Cuidados**
>
> * Não use prefixo `AD_` em tabelas customizadas (reservado para uso interno)
> * Valide todas as primary keys após a conversão
> * Teste todas as funcionalidades críticas antes de ir para produção
> * Revise e ajuste os XMLs gerados automaticamente

***

**Sucesso na sua migração! 🚀**
