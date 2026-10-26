---
id: "32275734789527"
titulo: "Cadastro de Regiões"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32275734789527-Cadastro-de-Regi%C3%B5es"
trilha: "Assistente de Melhores Práticas > Configurações para Distribuição"
atualizado_em: "2026-07-22T16:16:18Z"
rotulos: ["Configuração", "Transporte", "Cadastro", "Região", "Logística"]
---

# Cadastro de Regiões

### Descrição

Cadastra as regiões para fracionar um espaço geográfico, facilitando a gestão e a operação. Calcula o frete conforme a localidade e define áreas de atuação para vendedores, por exemplo.

#### Definição dos níveis de hierarquia

A estrutura das regiões segue a seguinte regra:

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

- **Região1** – Nível 1 → **1 dígito**
  - **Região2** – Nível 2 → **1 dígito**
    - **Região3, Região4, Região5, Região6, Região7, Região8** – Nível 3 → **2 dígitos**

Ainda será criado um **Nível 4** com **2 dígitos** para expansão.

A máscara final será:

- **Nível 1:** 1 dígito (**até 9 regiões**)
- **Nível 2:** 1 dígito (**até 9 regiões**)
- **Nível 3:** 2 dígitos (**até 99 regiões**)
- **Nível 4:** 2 dígitos (**até 99 regiões**)

Essa configuração permite futuras expansões sem comprometer a estrutura inicial.

### Como instalar

**1.** Clique em "**Iniciar**".

**2.** Caso exista uma estrutura configurada, finalize o processo.

**3.** Definição dos níveis da hierarquia de regiões.

3.1. Clique em "**+**" para adicionar uma região, preenchendo os campos do formulário com a seguinte informação:

• Nome da região

3.2. Clique em "**Confirmar**" e em "**Avançar**" para prosseguir.

**4.** Verifique o resumo com as regiões configuradas.

**5.** Clique em "**Instalar**" para concluir a configuração.

### Detalhes da instalação

#### Parâmetros Atualizados

- **Máscara para Região (MASCREGIAO):** Atualizada de acordo com os cadastros de regiões.

#### Atualização Sequencial na Tabela

- TSIREG – Cadastro de regiões.

### Como simular

Para acessar os cadastros realizados:

Regiões:

1. vá até Configurações > Cadastros > Endereços > Regiões.
2. clique em "**Mostrar hierarquia**" e em "**Atualizar**".

**Vale saber**

Cada região cadastrada é um passo a mais rumo a uma operação logística mais eficiente. Isso impacta o cálculo de frete, a roteirização e até a performance da sua equipe comercial. Pense bem na hierarquia e nos nomes — a máscara criada agora será a base para o crescimento futuro!
