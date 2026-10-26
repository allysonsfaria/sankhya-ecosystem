---
id: "https://developer.sankhya.com.br/docs/introducao-sdk-sankhya"
titulo: "🚀 Introdução ao SDK Sankhya"
url: "https://developer.sankhya.com.br/docs/introducao-sdk-sankhya"
atualizado_em: "2026-09-08T19:10:41.000Z"
---

# 🚀 Introdução ao SDK Sankhya

# 🚀 Introdução ao SDK Sankhya

O **SDK Sankhya** é um conjunto de ferramentas projetado para modernizar e simplificar o desenvolvimento na plataforma Sankhya. Ele incorpora conceitos consolidados e amplamente adotados no mercado, com forte inspiração em frameworks como **Spring** e **JPA/Hibernate**.

O objetivo é aprimorar a experiência do desenvolvedor, promovendo a criação de um código mais limpo, manutenível e, acima de tudo, **testável**.

Para atingir essa meta, o SDK se baseia em quatro pilares fundamentais:

***

### 🌟 1. Injeção de Dependências

O SDK implementa um mecanismo de **injeção de dependências (DI)** que automatiza a criação e o fornecimento de objetos.

* **Como funciona?** As dependências são injetadas diretamente no construtor de suas classes.
* **Benefício:** Desacopla os componentes, simplifica o gerenciamento do ciclo de vida dos objetos e, crucialmente, **facilita a criação de testes unitários**, permitindo o uso de *mocks* para isolar e verificar o comportamento de cada componente.

### 🗃️ 2. Camada de Acesso a Dados (Data Layer)

Para simplificar e padronizar a interação com o **Jape**, o SDK introduz uma camada de acesso a dados robusta, inspirada no **Spring Data JPA**.

* **Principal Componente:** O padrão **Repository**, que abstrai a complexidade da persistência de dados.
* **Como funciona?** Você define uma interface e o SDK cria a implementação em tempo de execução, permitindo realizar consultas com anotações como `@Criteria` e `@Query`.
* **Benefício:** Acelera a curva de aprendizado e permite que o desenvolvedor foque na lógica de negócio, não no código *boilerplate* de acesso a dados.

### 🔗 3. Controle Transacional Declarativo

O gerenciamento de transações é simplificado com a anotação `@Transactional`, semelhante ao que existe no Spring.

* **Como funciona?** Com uma única anotação em um método, você define o escopo de uma transação de banco de dados.
* **Benefício:** Garante a atomicidade e a integridade das operações sem a necessidade de controle manual, tornando o código mais limvio e legível.

### ✅ 4. Validação de Dados (Bean Validation)

O SDK integra o **Bean Validation (JSR 303/380)**, permitindo a validação de dados de forma declarativa.

* **Como funciona?** Use anotações como `@NotNull`, `@Size` e `@Email` diretamente nos seus DTOs ou entidades.
* **Benefício:** A validação é executada automaticamente, garantindo a integridade dos dados desde o ponto de entrada até a persistência.

***

### ✨ Principais Benefícios do SDK Sankhya

| Benefício                                | Descrição                                                                                                                       |
| :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| 📉 **Redução da Curva de Aprendizado**   | A familiaridade com padrões de mercado (Spring, JPA) acelera a integração de novos desenvolvedores.                             |
| 🧩 **Código Consistente e Padronizado**  | Promove uma maneira uniforme de interagir com o Jape, melhorando a legibilidade e a manutenção.                                 |
| 🚀 **Foco na Lógica de Negócio**         | Abstrai a complexidade do acesso a dados, permitindo que você se concentre no que realmente importa: as regras de negócio.      |
| 🧪 **Alta Testabilidade**                | A injeção de dependências é um pilar para a criação de código testável, permitindo a validação de componentes de forma isolada. |
| 🛡️ **Validação Automática e Integrada** | Garante a consistência e a integridade dos dados de forma declarativa e reutilizável.                                           |
