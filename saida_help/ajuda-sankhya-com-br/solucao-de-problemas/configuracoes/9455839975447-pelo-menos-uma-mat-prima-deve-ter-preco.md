---
id: "9455839975447"
titulo: "Pelo menos uma Mat.Prima deve ter preço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9455839975447-Pelo-menos-uma-Mat-Prima-deve-ter-pre%C3%A7o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:46Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "TOP", "Estoque", "Financeiro", "CORE_E01244", "Configuração de Preços para Produtos KIT"]
---

# Pelo menos uma Mat.Prima deve ter preço

(1)**  MENSAGEM:**

[CORE\_E01244]  Pelo menos uma Mat.Prima deve ter preço.

(2)** CAUSA:**

 Ocorre quando se realiza negociações com um produto 'KIT'. e nenhum de seus componentes possui preço de tabela.

(3)** SOLUÇÃO:**

Verificar as seguintes configurações para cálculo do preço do componente.

- **Tipos de operação TOP** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP)

**Usar como Preço:** Preço de Venda

![Imagem 1: Usar como Preço: Preço de Venda](https://ajuda.sankhya.com.br/hc/article_attachments/15448029833751)

- **Tabela de preços** (Comercial » Arquivo » Tabelas de Preços)

Criado uma tabela e adicionar o item com o seu preço.

![Imagem 2: Criado uma tabela e adicionar o item com o seu preço.](https://ajuda.sankhya.com.br/hc/article_attachments/9455636998039)

- Cadastros de **Parceiros** (Configurações » Cadastros » Parceiros)

Aba Grupo ICMS/ISS por Empresa >> Adicionando a EMPRESA e a Tabela de Preço criada anteriormente 
![Imagem 3: Aba Grupo ICMS/ISS por Empresa >> Adicionando a EMPRESA e a Tabela de Preço criada anteriormente](https://ajuda.sankhya.com.br/hc/article_attachments/15448066797463)

- Cadastro da **Empresa** (Comercial » Preferências » Empresa)

Aba Estoque/Preço>> Tabela de preço para venda Vincular tabela criada anteriormente

![Imagem 4: Aba Estoque/Preço>> Tabela de preço para venda Vincular tabela criada anteriormente](https://ajuda.sankhya.com.br/hc/article_attachments/15448083008791)

- **PARÂMETROS QUE INFLUENCIAM**

**TIPTABPRECOS:** Parceiro/Empresa (Conforme informado que a tabela de preço seria por parceiro e empresa)

**USARCODTABEMP:** Ligado

**PRECOPORCONT:** Desligado

**PRECOPORLOC:** Desligado
