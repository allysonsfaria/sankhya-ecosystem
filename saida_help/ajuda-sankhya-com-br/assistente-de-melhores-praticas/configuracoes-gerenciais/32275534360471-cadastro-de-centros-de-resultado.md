---
id: "32275534360471"
titulo: "Cadastro de Centros de Resultado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32275534360471-Cadastro-de-Centros-de-Resultado"
trilha: "Assistente de Melhores Práticas > Configurações Gerenciais"
atualizado_em: "2026-07-22T16:16:59Z"
rotulos: ["Configuração", "Centro de Resultado", "Gerencial", "Financeiro", "Cadastro"]
---

# Cadastro de Centros de Resultado

### Descrição

Define um **Centro de Resultado** como um subconjunto de uma empresa, onde receitas e despesas podem ser analisadas separadamente. Isso possibilita avaliar seu desempenho e compará-lo ao da empresa como um todo.

Exemplos de Centros de Resultado incluem **departamentos, obras, unidades de negócio, agências e filiais**.

#### Definição dos níveis de hierarquia

A estrutura do Centro de Resultado segue a seguinte regra:

- **Máscara:** Até **9 dígitos** e **4 níveis hierárquicos**.
- **Quantidade de dígitos por nível:**
  - Se houver **menos de 5 itens** → **1 dígito**
  - Se houver **mais de 5 itens e menos de 50 itens** → **2 dígitos**
  - Se houver **mais de 50 e menos de 500 itens** → **3 dígitos**
  - Se houver **mais de 500 e menos de 5000 itens** → **4 dígitos**
  - Se houver **5000 itens ou mais** → **5 dígitos**

Se a soma dos dígitos dos níveis cadastrados for menor que **9**, a estrutura pode ser expandida.

#### Exemplo de estrutura

Se cadastrada a seguinte hierarquia:

- **CR1** – Nível 1 → **1 dígito**
  - **CR2** – Nível 2 → **1 dígito**
    - **CR3, CR4, CR5, CR6, CR7, CR8** – Nível 3 → **2 dígitos**

Ainda será criado um **Nível 4** com **2 dígitos** para expansão.

A máscara final será:

- **Nível 1:** 1 dígito (**até 9 centros de resultado**)
- **Nível 2:** 1 dígito (**até 9 centros de resultado**)
- **Nível 3:** 2 dígitos (**até 99 centros de resultado**)
- **Nível 4:** 2 dígitos (**até 99 centros de resultado**)

Essa configuração permite futuras expansões sem comprometer a estrutura inicial.

### Como instalar

**1.** Clique em "**Iniciar**".

**2.** Caso exista uma estrutura configurada, finalize o processo.

**3.** Defina o controle por Centro de Resultado que poderá ser obrigatório, opcional ou não necessário nas centrais, financeiros e rateio.

3.1. O cadastro do Centro de Resultado será obrigatório ou opcional nas Centrais, Financeiros e Rateio.

3.1.1. Clique em "**+**" para adicionar um Centro de Resultado, preenchendo os campos do formulário com a seguinte informação:

• Nome do Centro de resultado

3.1.2. Clique em "**Confirmar**" e "**Avançar**" para prosseguir.

3.2. O cadastro do Centro de Resultado não é necessário nas Centrais, Financeiros e Rateio.

**4.** Clique em "**Avançar**".

**5.** Verifique o resumo com os Centros de Resultados configurados.

**6.** Clique em "**Instalar**" para concluir a configuração.

### Detalhes da instalação

#### Parâmetros Atualizados

- **Máscara para o Centro de Resultado (MASCCENCUS):** Atualizada de acordo com os cadastros de Centro de Resultado.
- **Exigir CR na Central/Financeiro/Rateio? (EXIGCRCFR):** Atualizado conforme a configuração do **passo 3** da instalação.

#### Atualização Sequencial na Tabela

- **TSICUS** – Cadastro de Centro de Resultados.

### Como simular

Para acessar os cadastros realizados:

Centros de Resultado:

1. vá até Configurações > Cadastros > Gerencial > Centros de Resultado.
2. clique em "**Mostrar hierarquia**" e "**Atualizar**".

**Vale saber**

Vai cadastrar os Centros de Resultado? Pense na hierarquia desde já! A máscara se adapta conforme o volume, então quanto mais organizado o início, mais fácil escalar depois. E se definir que o uso será obrigatório, o sistema já garante o controle dos lançamentos — sem chance de faltar o Centro de Resultado nas análises!
