---
id: "33279836222103"
titulo: "Não foi possível processar o arquivo. A estrutura do layout não é adequada a estrutura do arquivo ou não foram encontrados os identificadores correspondentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33279836222103-N%C3%A3o-foi-poss%C3%ADvel-processar-o-arquivo-A-estrutura-do-layout-n%C3%A3o-%C3%A9-adequada-a-estrutura-do-arquivo-ou-n%C3%A3o-foram-encontrados-os-identificadores-correspondentes"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:29:09Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "layout", "Passos para resolver", "Razão do erro", "Detalhe do erro", "A estrutura do layout não é adequada a estrutura do arquivo", "ou não foram encontrados os identificadores correspondentes.", "Não foi possível processar o arquivo.", "Layout de Processamento do Arquivo", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Não foi possível processar o arquivo. A estrutura do layout não é adequada a estrutura do arquivo ou não foram encontrados os identificadores correspondentes

**Mensagem**

Não foi possível processar o arquivo. A estrutura do layout não é adequada à estrutura do arquivo ou não foram encontrados os identificadores correspondentes.

**Solução**

Para que o processamento funcione bem, configure corretamente os campos essenciais no layout (Configurações >> Cadastros >> Layouts de Processamento de Arquivo). Eles são:

- **TIP\_MOVTO** – Tipo de movimento;
- **NSU\_TEF\_POS** – NSU gerado pelo TEF (Auttar, SiTef, PayGo etc.);
- **NSU\_ADQUIRENTE** – NSU gerado pela adquirente (autorizadora);
- **COD\_AUTORIZACAO** – Código de autorização da transação gerado pela autorizadora;
- **DT\_MOVTO** – Data da transação;
- **QTD\_PARCELAS** – Quantidade de parcelas da venda, quando parcelada;
- **NRO\_PARCELA** – Número da parcela que está sendo paga;
- **VLR\_PARCELA\_LIQ** – Valor líquido da parcela (sem taxa);
- **VLR\_PARCELA** – Valor bruto da parcela (com taxa);
- **VLR\_TAXA\_AUTORIZACAO** – Valor total da taxa cobrada do cliente pela autorizadora;
- **VLR\_TRANSACAO** – Valor total da transação;
- **DT\_PAGTO** – Necessário quando a opção **"Baixar títulos na data do arquivo"** estiver ativa;
- **NUM\_CONTA\_CORRENTE** – Utilizado quando a opção **"Priorizar Conta e Empresa do arquivo na baixa"** estiver marcada, sendo necessário informar também o campo **DIGITO\_CONTA**;
- **DIGITO\_CONTA** – Dígito da conta corrente.

**Importante:** a posição de cada campo no layout precisa corresponder exatamente à ordem das colunas no arquivo de retorno. Isso significa que o campo com sequência 1 deve estar na primeira posição do arquivo, o de sequência 2 na segunda posição e assim por diante. Por isso, ao configurar o layout, é importante prestar atenção na ordem dos campos conforme a estrutura do arquivo recebido.

Se esse erro continuar acontecendo durante o processamento, veja também os artigos abaixo e consulte o manual da operadora para verificar se o arquivo está dentro do padrão esperado:

- [Conciliação de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334-Concilia%C3%A7%C3%A3o-de-Cart%C3%A3o)
- [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054-Layout-de-Processamento-de-Arquivo)

**Causa**

Esse erro acontece quando o Layout de Processamento do Arquivo não combina com a estrutura do arquivo que está sendo processado.
