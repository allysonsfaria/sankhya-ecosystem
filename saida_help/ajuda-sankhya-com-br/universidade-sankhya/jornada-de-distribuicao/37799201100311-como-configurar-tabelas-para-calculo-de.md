---
id: "37799201100311"
titulo: "Como configurar tabelas para cálculo de frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37799201100311-Como-configurar-tabelas-para-c%C3%A1lculo-de-frete"
trilha: "Universidade Sankhya > Jornada de Distribuição"
atualizado_em: "2026-07-22T14:07:54Z"
rotulos: ["Configuração", "Parceiro", "Cidades", "Fórmulas", "Rotas", "Transporte"]
---

# Como configurar tabelas para cálculo de frete

1. **Registro da tabela**

- Acesse a tela **“Tabelas para cálculo de frete”**
  Menu: Comercial » Arquivo » Cadastros » Tabelas para cálculo de frete
- Clique no botão **“+ Novo registro”**.

Insira as informações nos campos:

- **Descrição:** Insira uma descrição clara para a tabela (ex.: “**FÓRMULA FRETE**”).
- **Rateio de Frete:** Escolha a forma de distribuição do frete, como **Valor da Nota**.
- Clique no botão **Salvar [F7]**.

2. **Cadastrar Regiões e Cidades:**

- Na aba **“Região p/ tabela de frete”**
- Clique no botão **+** **Cadastrar região p/Tabela de frete** e em seguida preencha os campos:
- **Região:** Nome da região (ex.: Região Sul).
- Clique no botão **Salvar[F7]**.
- Na grade de cidades, adicione as cidades correspondentes:
- Clique no botão **+ Cadastrar cidades.**
- **Cód. Cidade:** Insira o código de cada cidade incluída na região. (Ex. Uberlândia e Uberaba).
- Clique no botão **Salvar[F7]**.

3. **Definir Rotas:**

- Na aba **“Rotas”**
- Clique no botão **+ Cadastrar** e em seguida preencha os campos:
- **Cidade Origem:** Indique a cidade (Ex. Uberlândia).
- **Cidade Destino:** Indique a cidade (Ex. Uberaba).
- **Região Destino:** Indique a região cadastrada na aba de região para tabela de frete.
- **Evento:** Vincule o evento correspondente ao cálculo de frete (deve ser previamente cadastrado).
- **Obrigatório?:** Marque.

**SUB-ABA GERAL**

- No campo **Fórmula**, insira a regra para o cálculo do frete:

**Insira a fórmula Por Peso:** 

IF(VLRNOTA<=200 , 28.87 , 32)

- Clique no botão **Salvar[F7]**.

4. **Cadastrar Transportadoras:**

Na aba **“Transportadoras”**, insira:

- Clique no botão **+ Cadastrar Transportadora.**
- **Cód. Parceiro:** Identifique o parceiro responsável pelo transporte.
- Após preencher todas as abas e campos obrigatórios, clique em **Salvar**.
