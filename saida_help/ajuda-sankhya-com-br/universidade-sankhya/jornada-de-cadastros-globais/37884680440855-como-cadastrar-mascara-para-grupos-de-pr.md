---
id: "37884680440855"
titulo: "Como cadastrar Máscara para Grupos de Produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37884680440855-Como-cadastrar-M%C3%A1scara-para-Grupos-de-Produtos"
trilha: "Universidade Sankhya > Jornada de Cadastros Globais"
atualizado_em: "2026-07-22T14:05:56Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Cadastro"]
---

# Como cadastrar Máscara para Grupos de Produtos

## O que é o cadastro da máscara de grupo de produtos?

O cadastro de máscara para grupo de produtos no ERP Sankhya permite estruturar e padronizar os códigos que serão usados para identificar os grupos de produtos de forma hierárquica. Essa configuração define quantos níveis a estrutura terá (limitado a quatro) e quantos dígitos serão utilizados em cada nível (máximo de três dígitos por nível), respeitando um total de até nove dígitos válidos. Esse padrão facilita a organização e análise dos produtos dentro da empresa. 

#### Cadastre a máscara que será utilizada no cadastro do Grupo de Produtos

1. Cadastro de **Máscara para Grupos de Produtos**

- Acesse a tela **Máscara para Grupos de Produtos**

**Menu:** Configurações » Avançado » Máscaras »  Máscara para Grupo de Produtos

- Defina a estrutura da máscara:
- A máscara pode conter até 4 níveis hierárquicos
- Informe a quantidade de dígitos para cada nível
- Exemplo de estrutura: "**9\.9\.9\.99;0**", neste exemplo, a configuração seria:
- Nível 1 - 1
- Nível 2 - 1
- Nível 3 - 1
- Nível 4 - 2
- Clique em **Salvar**

#### Observações importantes

- Após a criação de grupos com base nessa máscara, não será mais possível alterar a estrutura, por isso é fundamental definir esse padrão com cuidado antes de iniciar os cadastros.
- A máscara pode ter **até 4 níveis** e no máximo **9 dígitos somando tudo**.
- Os níveis podem ter **quantidades diferentes de dígitos** (ex: 2 no primeiro nível, 3 no segundo, etc.).
