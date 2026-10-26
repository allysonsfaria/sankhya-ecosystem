---
id: "44011868589847"
titulo: "Como importar uma planilha de Lançamentos Financeiros?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011868589847-Como-importar-uma-planilha-de-Lan%C3%A7amentos-Financeiros"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:13:22Z"
rotulos: ["sync_hc", "magis5", "magis5_204051670429", "sync_hash_3e7a977e0156"]
---

# Como importar uma planilha de Lançamentos Financeiros?

## Neste tutorial, você aprenderá a formatar sua planilha de lançamentos financeiros para importá-la com sucesso no Magis5 ERP.

#### Passo 1: Preparando a Planilha

### 1.1 Estrutura da Planilha

- **Coluna A**: Tipo de Lançamento
- **Coluna B**: ID Cliente ou Fornecedor
- **Coluna C**: ID Empreendimento
- **Coluna D**: Plano de Contas
- **Coluna E**: Centro de Custos
- **Coluna F**: Forma de Pagamento
- **Coluna G**: ID da Conta Bancária
- **Coluna H**: Descrição do Lançamento
- **Coluna I**: Banco
- **Coluna J**: Num C/C
- **Coluna K**: Num Cheque
- **Coluna L**: Data do Cheque
- **Coluna M**: Doc Boleto
- **Coluna N**: Num Boleto
- **Coluna O**: Agência
- **Coluna P**: Conta
- **Coluna Q**: Chave PIX
- **Coluna R**: Dta Competência
- **Coluna S**: Dta Vencimento
- **Coluna T**: Pago
- **Coluna U**: Dta Pagamento
- **Coluna V**: Valor
- **Coluna W**: Desconto
- **Coluna X**: Juros
- **Coluna Y**: Multa
- **Coluna Z**: Observação

![Imagem 1: Coluna Z : Observação](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/08/image-2.png)

### 1.2 Formato dos Dados

Certifique-se de que cada coluna contenha apenas os dados correspondentes:

- **Tipo de Lançamento:** Utilizar "0" para receita ou "1" para despesa
- **ID Cliente ou Fornecedor:** ID referente ao cliente ou fornecedor no empreendimento
- **ID Empreendimento:** ID do empreendimento de lançamento (inserir apenas um empreendimento por planilha)
- **Plano de Contas:** É o plano de contas cadastrado no empreendimento (exemplo: 1000.1)
- **Centro de Custos:** ID referente ao centro de custos no empreendimento
- **Forma de Pagamento:** Utilizar a planilha de [referência - Formas de Pagamento](https://docs.google.com/spreadsheets/d/1GLdvedlo6cDWLsgeH8cbjH0FfJ3xett4SapFvyrWwMQ/pubhtml?gid=1767667187&single=true)
- **ID da Conta Bancária:** ID referente a conta bancária no empreendimento
- **Descrição do Lançamento:** Campo de Texto (exemplo: Pagamento João)
- **Banco:** Utilizar a planilha de [referência - bancos](https://docs.google.com/spreadsheets/d/e/2PACX-1vSv-R0QpI2jRbF3Knd7X1djpNy3zYQG0NFHXlHYeA_z4WgJmFKJmejT_34z40r0bxKWnYuc3bbNtjXR/pubhtml?gid=1516312806&single=true)
- **Num C/C:** Preencher de acordo com a forma de pagamento selecionada. Campo numérico (não inserir letras ou caracteres especiais)
- **Num Cheque:** Preencher de acordo com a forma de pagamento selecionada. Campo numérico (não inserir letras ou caracteres especiais)
- **Data do Cheque:** Preencher de acordo com a forma de pagamento selecionada. Formatos aceitos: dd/mm/aaaa ou dd-mm-aaa (não inserir letras ou qualquer outro caractere especial)
- **Doc Boleto:** Preencher de acordo com a forma de pagamento selecionada. Campo numérico (não inserir letras ou caracteres especiais)
- **Num Boleto:** Preencher de acordo com a forma de pagamento selecionada. Campo numérico (não inserir letras ou caracteres especiais)
- **Agência:** Preencher de acordo com a forma de pagamento selecionada. Campo numérico (não inserir letras ou caracteres especiais)
- **Conta:** Preencher de acordo com a forma de pagamento selecionada. Campo numérico (não inserir letras ou caracteres especiais)
- **Chave PIX:** Preencher de acordo com a forma de pagamento selecionada. Campo numérico (não inserir letras ou caracteres especiais)
- **Dta Competência:** Formatos aceitos: dd/mm/aaaa ou dd-mm-aaa (não inserir letras ou qualquer outro caractere especial)
- **Dta Vencimento:** Formatos aceitos: dd/mm/aaaa ou dd-mm-aaa (não inserir letras ou qualquer outro caractere especial)
- **Pago:** Utilizar "1" para pago e "0" para pendente
- **Dta Pagamento:** Formatos aceitos: dd/mm/aaaa ou dd-mm-aaa (não inserir letras ou qualquer outro caractere especial). Caso o lançamento não esteja pago, deixar em branco
- **Valor:** Não utilizar R$. Utilizar ponto (.) ou vírgula (,) para separar casas decimais
- **Desconto:** Não utilizar R$. Utilizar ponto (.) ou vírgula (,) para separar casas decimais
- **Juros:** Não utilizar R$. Utilizar ponto (.) ou vírgula (,) para separar casas decimais
- **Multa:** Não utilizar R$. Utilizar ponto (.) ou vírgula (,) para separar casas decimais
- **Observação:** Campo de texto livre. Pode-se usar letras e números.

#### Passo 2: Salvando a Planilha

Após organizar e revisar os dados, salve a planilha no formato **XLSX**:

1. Clique em **Arquivo**.
2. Selecione **Salvar Como**.
3. Escolha o formato **XLSX.**
4. Nomeie o arquivo e clique em **Salvar.**

#### Dicas Adicionais

- Quantidade média de itens por planilha: 20 mil linhas
