---
id: "44011876796823"
titulo: "Como importar uma planilha de Produtos?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011876796823-Como-importar-uma-planilha-de-Produtos"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:13:19Z"
rotulos: ["sync_hc", "magis5", "sync_hash_a4c5d4eab215", "magis5_204048273502"]
---

# Como importar uma planilha de Produtos?

## Neste tutorial, você aprenderá a formatar sua planilha de produtos para importá-la com sucesso no Artemis5. Siga os passos abaixo para garantir que sua base de dados esteja corretamente configurada..

#### Passo 1: Preparando a Planilha

### 1.1 Estrutura da Planilha

- **Coluna A**: SKU Externo
- **Coluna B**: Código de Barras
- **Coluna C**: Descrição
- **Coluna D**: Marca
- **Coluna E**: Categoria
- **Coluna F**: Tam/Qtde
- **Coluna G**: Sabor/Cor
- **Coluna H**: NCM
- **Coluna I**: Un Comercial
- **Coluna J**: Origem do Produto
- **Coluna K**: CEST
- **Coluna L**: Unidade/Fração
- **Coluna M**: Regra Padrão
- **Coluna N**: Custo
- **Coluna O**: Venda
- **Coluna P**: Altura
- **Coluna Q**: Largura
- **Coluna R**: Profundidade
- **Coluna S**: Peso Liquido
- **Coluna T**: Peso Bruto
- **Coluna U**: URL da foto
- **Coluna V**: ID Interno

![Imagem 1: Coluna V : ID Interno](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-11.png)

### 1.2 Formato dos Dados

Certifique-se de que cada coluna contenha apenas os dados correspondentes:

- **SKU Externo**: Identificação única do produto no Artemis5. Não pode conter caracteres especiais e não pode ter códigos repetidos.
- **Código de Barras:** Código numérico utilizado para identificar e rastrear produtos automaticamente. Deverá ser enviado, obrigatoriamente, como texto.
- **Descrição:** Nome do Produto. Não pode conter caracteres especiais.
- **Marca:** Marca do produto.
- **Categoria:** Categoria onde o produto está localizado.
- **Tam/Qtde:** Tamanho ou quantidade do produto (por exemplo: 500ml, 1kg, etc.).
- **Sabor/Cor:** Informação sobre o sabor ou cor do produto, relevante para alimentos, bebidas, itens de vestuário, etc.
- **NCM**: Nomenclatura Comum do Mercosul, um código utilizado para classificar produtos na importação/exportação. Não pode conter pontos.
- **Un Comercial:** Unidade de comercialização do produto (por exemplo, unidade, caixa, pacote). Utilizar a seguinte planilha para referência: https://cutt.ly/cetpy5pj
- **Origem do Produto:** Origem da mercadoria, podendo ser nacional ou estrangeira. Utilizar a seguinte planilha para referência: https://cutt.ly/cetpy5pj
- **CEST:** Código Especificador da Substituição Tributária, utilizado para identificar a categoria fiscal do produto.
- **Unidade/Fração:** Detalha se o produto é vendido em unidades inteiras ou frações. Utilizar a seguinte planilha para referência: https://cutt.ly/cetpy5pj
- **Regra Padrão:** Pode ser deixado em branco, será preenchido pela equipe do ERP.
- **Custo**: Valor do custo de aquisição ou produção do produto.
- **Venda**: Preço de venda do produto ao consumidor final.
- **Altura**: Altura do produto, medida em centímetros (80cm = 80). Sempre utilizar vírgula.
- **Largura**: Largura do produto, medida em centímetros (80cm = 80). Sempre utilizar vírgula.
- **Profundidade**: Profundidade do produto, medida em centímetros (80cm = 80). Sempre utilizar vírgula.
- **Peso Liquido**: Peso do produto sem incluir a embalagem, medido em quilogramas (1kg = 1 || 1,99kg = 1,99). Se o campo estiver em branco, preencher com 0 (zero).
- **Peso Bruto**: Peso total do produto incluindo a embalagem, medido quilogramas (1kg = 1 || 1,99kg = 1,99). Se o campo estiver em branco, preencher com 0 (zero).
- **URL da foto**: Endereço da web onde a imagem do produto está armazenada.
- **ID Interno**: Identificação única do produto dentro do Artemis5 da empresa, utilizado apenas para edição do produto.

#### Passo 2: Salvando a Planilha

Após organizar e revisar os dados, salve a planilha no formato **XLSX**:

1. Clique em **Arquivo**.
2. Selecione **Salvar Como**.
3. Escolha o formato **XLSX.**
4. Nomeie o arquivo e clique em **Salvar**.

#### Dicas Adicionais

- Quantidade média de produtos por planilha: até 20mil linhas.
- Peso: Inserir em quilogramas (1kg = 1 || 1,99kg = 1,99). Se o campo estiver em branco, preencher com 0 (zero).
- Medidas (Altura, largura e comprimento): Preencher em centímetros (80cm = 0,80). Sempre utilizar vírgula.
