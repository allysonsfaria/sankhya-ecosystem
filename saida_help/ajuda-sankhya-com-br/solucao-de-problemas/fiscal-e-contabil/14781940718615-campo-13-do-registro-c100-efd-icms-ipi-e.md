---
id: "14781940718615"
titulo: "Campo 13 do registro C100 EFD-ICMS/IPI e o tratamento do campo \"Subtipo\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14781940718615-Campo-13-do-registro-C100-EFD-ICMS-IPI-e-o-tratamento-do-campo-Subtipo"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:58:07Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "EFD", "ICMS/IPI", "Subtipo Pagamento: Define forma de pagamento", "Solução: Estabelecer lógica para determinar o tipo de pagamento", "IND_PGTO Valores: 0 à vista 1 a prazo 2 outros"]
---

# Campo 13 do registro C100 EFD-ICMS/IPI e o tratamento do campo "Subtipo"

(1)** SITUAÇÃO:**

Na tela **Tipos de Negociação Comercial » Arquivo » Cadastros » na ABA Características**

Um **"Subtipo"**é utilizado para definir a forma de pagamento que está sendo utilizada na operação realizada; é uma informação que depois de salva, não poderá ser modificada. Teremos as seguintes

opções:

- Cartão de Débito;
- A vista;
- A prazo;
- Parcelada;
- Cheque pré-datado;
- Crediário;
- Financeira;
- Cartão de Crédito.

![Imagem 1: Cartão de Crédito.](https://ajuda.sankhya.com.br/hc/article_attachments/15440416367895)

**TABELA TGFTPV nome do campo SUBTIPOVENDA**

Campo 13 (IND\_PGTO) - Valores válidos: [0, 1, 2, 9]

13 IND\_PGTO Indicador do tipo de pagamento:
0 - À vista;
1 - A prazo;
9 - Sem pagamento.
Obs.: A partir de 01/07/2012 passará a ser:
Indicador do tipo de pagamento:
0 - À vista;
1 - A prazo;
2 - Outros

![Imagem 2: 13 IND_PGTO Indicador do tipo de pagamento: 0 - À vista; 1 - A prazo; 9 - Sem pagamento. Obs.: A partir de 01/07/2012…](https://ajuda.sankhya.com.br/hc/article_attachments/14781971352087)

(2)** CAUSA:**

A causa principal do problema relacionado ao campo "Subtipo" é a falta de definição correta do valor a ser atribuído quando não há uma indicação clara de se a negociação foi à vista ou a prazo. Esse campo é essencial para determinar o valor a ser lançado no campo 13 do C100, que representa o tipo de pagamento realizado na transação.

(3)** SOLUÇÃO:**

Para resolver essa questão, é necessário estabelecer uma lógica adequada no sistema para lidar com diferentes cenários. Recomenda-se seguir os seguintes passos:

1. Identificação do tipo de negociação: Verificar se a negociação é à vista, à prazo ou se não se enquadra em nenhuma dessas categorias.
2. Caso a negociação seja à vista: O sistema deve lançar o valor 0 no campo 13 do C100, indicando que o pagamento foi realizado integralmente no momento da transação.
3. Caso a negociação seja à prazo: O sistema deve lançar o valor 1 no campo 13 do C100, indicando que o pagamento será realizado em uma data futura.
4. Se a negociação não se enquadrar em nenhuma das opções acima: O sistema deve lançar o valor 2 no campo 13 do C100, sinalizando que não foi possível determinar o tipo de pagamento com base nas informações disponíveis.
