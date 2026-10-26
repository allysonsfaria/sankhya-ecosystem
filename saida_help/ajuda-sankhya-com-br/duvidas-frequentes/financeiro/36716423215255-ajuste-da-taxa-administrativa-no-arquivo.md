---
id: "36716423215255"
titulo: "Ajuste da Taxa Administrativa no Arquivo de Retorno: Instruções para Somar ou Subtrair no Processamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36716423215255-Ajuste-da-Taxa-Administrativa-no-Arquivo-de-Retorno-Instru%C3%A7%C3%B5es-para-Somar-ou-Subtrair-no-Processamento"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:22:27Z"
rotulos: ["Configuração", "Preferências", "Financeiro", "Arquivo de Retorno", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Taxa Administrativa"]
---

# Ajuste da Taxa Administrativa no Arquivo de Retorno: Instruções para Somar ou Subtrair no Processamento

Durante o processamento do **arquivo de retorno bancário**, pode ocorrer de o banco informar um **Valor de Baixa menor** que o **Valor do Título**.

Isso ocorre porque o banco geralmente desconta a **taxa administrativa** (taxa de liquidação do boleto).

Para que o sistema trate corretamente essa diferença, o arquivo de retorno deve conter o **valor da taxa admnistrativa**. Assim o sistema poderá aplicar a lógica definida, somar ou subtrair a taxa, durante o processamento.

#### Procedimento

##### Verifique os parâmetros

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou descrição''** pesquise pelos parâmetros abaixo:

- **SOMATXVLRBAIXA** – Soma a taxa ao valor da baixa no retorno bancário.
- **SUBTXVLRBAIXA** – Subtrai a taxa ao valor da baixa no retorno bancário.

**(3)** Verifique se ambos os parâmetros estão habilitados.

(Esses parâmetros determinam o comportamento padrão com relação a taxa).

##### Configure o tratamento da taxa administrativa

**(1)** Acesse a tela [**''Configuração Arquivo de Retorno''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno) (Financeiro » EDI Bancário » Configuração Arquivo de Retorno).

**(2)** Defina como o sistema deve tratar a taxa administrativa:

- **Considerar configuração global:** Está opção é default (padrão). Quando não for configurada, valerá a configuração da forma que estão os parâmetros na base de dados, ou seja, determina que a rotina terá o comportamento atual.
- **Nada a fazer:** O sistema **ignora a configuração do parâmetro** e **não utiliza em nada a taxa administrativa**, ou seja, nem a soma e nem a subtrai no momento da baixa, de modo que serão respeitados os valores advindos do arquivo de retorno. Qualquer configuração relacionada à isto será ignorada.
- **Somar ao valor recebido:** O sistema **ignora os parâmetros e adiciona o valor da taxa** ao valor recebido, informando o resultado no campo **Valor de baixa**.
- **Subtrair do valor recebido:** O sistema **ignora os parâmetros e subtrai o valor da taxa** do valor recebido, informando o resultado no **valor do desconto do título**.

![Imagem 1: Subtrair do valor recebido: O sistema ignora os parâmetros e subtrai o valor da taxa do valor recebido, informando o…](https://ajuda.sankhya.com.br/hc/article_attachments/36716433448599)

**OBSERVAÇÃO:**

- No layout do arquivo de retorno, é obrigatório incluir o campo **TAXAADMIN** conforme a posição definida no manual do banco.
- A configuração da **Taxa Administrativa** deve estar presente **em todos os segmentos do layout**.
- Caso o layout possua **header** e/ou **trailer**, esses também devem ser configurados.
