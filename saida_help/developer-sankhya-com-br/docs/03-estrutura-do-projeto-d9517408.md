---
id: "https://developer.sankhya.com.br/docs/03_estrutura-do-projeto"
titulo: "📂 Estrutura de um Projeto Add-on Studio"
url: "https://developer.sankhya.com.br/docs/03_estrutura-do-projeto"
atualizado_em: "2025-11-10T23:35:52.000Z"
---

# 📂 Estrutura de um Projeto Add-on Studio

Explica a organização padrão dos arquivos e diretórios em um projeto de add-on.

Um projeto gerado pelo Add-on Studio segue uma estrutura de diretórios padrão, projetada para organizar de forma clara as diferentes partes da sua aplicação: o back-end (lógica de negócio), o front-end (telas) e os metadados do banco de dados.

Compreender essa estrutura é fundamental para desenvolver e manter seu add-on de forma eficiente.

***

## 🌳 Diretórios Principais

Aqui está uma visão geral dos diretórios mais importantes na raiz do seu projeto:

```
meu-addon/
├── 📂 datadictionary/
├── 📂 dbscripts/
├── 📂 model/
│   └── src/
└── 📂 vc/
    └── src/
```

### 1. `datadictionary/`

Este diretório é o coração da definição de dados do seu add-on. Ele contém os arquivos XML que descrevem as entidades, tabelas, menus e telas que serão adicionados ou modificados no Sankhya Om.

* **`metadados.xml`**: O arquivo principal onde você define:
  * **Entidades (Jape):** A representação das suas tabelas no sistema.
  * **Tabelas e Campos:** A estrutura física das tabelas que serão criadas no banco de dados.
  * **Menus e Telas:** A forma como suas funcionalidades aparecerão na interface do usuário.
  * **Parâmetros:** Configurações customizadas para o seu add-on.

### 2. `dbscripts/`

Este diretório armazena os scripts de banco de dados que precisam ser executados durante a instalação ou atualização do add-on. É usado para tarefas que não são cobertas pelo `metadados.xml`, como a criação de views, triggers ou a execução de migrações de dados complexas.

* **Versionamento:** Os scripts são nomeados sequencialmente (ex: `V1.xml`, `V2.xml`) para garantir que sejam executados na ordem correta.
* **Imutabilidade:** Uma vez que um script é executado em um ambiente, ele não deve ser alterado. Novas mudanças devem ser feitas em um novo arquivo de versão.

### 3. `model/`

Este é o módulo Gradle que contém toda a lógica de **back-end** do seu projeto. É aqui que você escreverá seu código Java.

* **`model/src/main/java/`**: Este é o diretório principal onde todo o seu código-fonte Java deve ser colocado. A estrutura de pacotes (packages) dentro deste diretório deve seguir as convenções do Java, geralmente baseadas no `group` definido no `build.gradle` (ex: `br/com/suaempresa/addon/`).
  * **O que colocar aqui?**
    * Classes de Serviço (`@Service`)
    * Componentes de Negócio (`@Component`)
    * Repositórios (`@Repository`)
    * Entidades POJO (`@JapeEntity`)
    * Regras de Negócio (`@BusinessRule`)
    * Listeners (`@Listener`)
    * Callbacks (`@Callback`)
    * Botões de Ação (`@ActionButton`)

### 4. `vc/`

Este é o módulo Gradle para o **front-end**. Ele contém os arquivos relacionados à interface do usuário, como telas HTML5 customizadas.

* **`vc/src/webapp/html5/`**: Este é o diretório onde você deve colocar todos os seus arquivos de front-end.
  * **O que colocar aqui?**
    * Arquivos `.html` para a estrutura das telas.
    * Arquivos `.js` para a lógica de front-end (usando SankhyaJS ou outras bibliotecas).
    * Arquivos `.css` para a estilização das suas telas.
    * Imagens, fontes e outros recursos estáticos.

A estrutura dentro de `html5/` é flexível, permitindo que você organize seus arquivos em subpastas da maneira que fizer mais sentido para o seu projeto (ex: `css/`, `js/`, `components/`).

***

## ✨ Boas Práticas e Arquitetura de Código

A estrutura de um projeto não é apenas sobre diretórios, mas também sobre como o código é organizado internamente. A escolha da arquitetura correta depende do tamanho e da complexidade do seu add-on. Adotar práticas de desenvolvimento moderno desde o início garante que seu projeto seja escalável, testável e fácil de manter.

### 🚀 Abordagem para Projetos Pequenos e Médios (Foco em Produtividade)

Para a maioria dos add-ons, a produtividade é a chave. Uma arquitetura pragmática que agiliza o desenvolvimento é a mais indicada. O objetivo é entregar valor rapidamente, mantendo o código organizado.

**Organização por Funcionalidade (Package by Feature):**

Em vez de separar as classes por tipo (ex: `services`, `repositories`), agrupe-as pela funcionalidade a que pertencem. Isso mantém o código relacionado próximo, facilitando a localização e a modificação.

```
br/com/suaempresa/addon/
├── 📂 faturamento/
│   ├── FaturamentoService.java
│   ├── FaturamentoRepository.java
│   ├── NotaFiscal.java (@JapeEntity)
│   └── NotaFiscalDTO.java
└── 📂 estoque/
    ├── EstoqueService.java
    ├── ProdutoEstoque.java (@JapeEntity)
    └── ConsultaEstoqueDTO.java
```

**Diretrizes:**

1. **Use o SDK Sankhya ao Máximo:** Aproveite `@Service`, `@Repository`, `@JapeEntity` e a injeção de dependências (`@Inject`) para eliminar código boilerplate e focar na lógica de negócio.
2. **Simplicidade é a Chave:** Se uma lógica de negócio é simples, ela pode residir diretamente no `@Service`. Não há necessidade de criar uma camada `@Component` separada para cada pequena tarefa. A camada de negócio pode ser introduzida quando a complexidade aumentar.
3. **DTOs como Contrato:** Use Data Transfer Objects (DTOs) como entrada para seus `@Service` para validar os dados de forma clara. Para respostas simples, retornar a própria `@JapeEntity` pode ser aceitável para acelerar o desenvolvimento, mas esteja ciente do acoplamento que isso gera.
4. **Mantenha a Coesão:** Todo o código relacionado a uma funcionalidade (ex: "Faturamento") deve estar no mesmo pacote.

### 🏛️ Abordagem para Projetos Grandes e Complexos (Foco em Manutenibilidade)

Para add-ons que são verdadeiros sistemas dentro do Sankhya, com múltiplas integrações e regras de negócio complexas, a manutenibilidade a longo prazo é a prioridade. Uma arquitetura mais robusta e em camadas, inspirada em princípios como a Arquitetura Limpa (Clean Architecture), é essencial.

**Organização por Camada (Package by Layer):**

Esta abordagem clássica separa estritamente as responsabilidades, tornando o projeto mais fácil de entender para novos desenvolvedores e mais seguro para modificar.

```
br/com/suaempresa/addon/
├── 📂 api/
│   ├── FaturamentoController.java  (@Service)
│   └── EstoqueController.java      (@Service)
├── 📂 business/
│   ├── FaturamentoBusinessService.java (@Component)
│   └── EstoqueBusinessService.java     (@Component)
├── 📂 domain/
│   ├── model/
│   │   ├── NotaFiscal.java (@JapeEntity)
│   │   └── Produto.java    (@JapeEntity)
│   └── repository/
│       ├── FaturamentoRepository.java
│       └── ProdutoRepository.java
└── 📂 dto/
    ├── FaturamentoRequestDTO.java
    └── FaturamentoResponseDTO.java
```

**Diretrizes:**

1. **Separação Estrita de Camadas:**
   * **`api`(ou`controller`):** Contém as classes `@Service`. A única responsabilidade é orquestrar a requisição: receber DTOs, chamar a camada de negócio e retornar uma resposta. **Nenhuma regra de negócio aqui.**
   * **`business`(ou`service`):** Contém os `@Component`s com a lógica de negócio principal. Orquestra chamadas a repositórios e outros componentes.
   * **`domain`:** O coração da aplicação. Contém as entidades (`@JapeEntity`) e as interfaces dos repositórios. Esta camada não deve depender de nenhuma outra.
   * **`dto`:** Objetos de Transferência de Dados. Usados como contratos de entrada e saída da camada `api`, desacoplando o modelo de domínio da exposição externa.
2. **Inversão de Dependência (SOLID):** A camada de negócio (`business`) deve depender de abstrações (interfaces de repositório), não de implementações concretas. A implementação do repositório é fornecida pelo framework em tempo de execução.
3. **Programe para Interfaces:** Sempre que possível, defina uma interface para seus serviços de negócio (`FaturamentoBusinessService`) e sua implementação (`FaturamentoBusinessServiceImpl`). Isso facilita a testabilidade e a substituição de implementações.
4. **DTOs são Obrigatórios:** Nunca exponha suas entidades (`@JapeEntity`) diretamente na API. Use DTOs para controlar exatamente quais dados são enviados e recebidos, evitando vazamento de informações e acoplamento excessivo.
