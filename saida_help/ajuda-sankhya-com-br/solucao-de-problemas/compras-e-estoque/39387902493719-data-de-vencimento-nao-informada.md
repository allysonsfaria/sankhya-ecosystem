---
id: "39387902493719"
titulo: "Data de vencimento não informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39387902493719-Data-de-vencimento-n%C3%A3o-informada"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T13:30:31Z"
rotulos: ["CT-e", "Configuração", "XML", "Importação", "Financeiro", "Erro", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# Data de vencimento não informada

### SITUAÇÃO

Ao importar um arquivo XML de CT-e pelo **Portal de Importação** (**Comercial > Rotinas > Portal de Importação de XML**), o sistema pode exibir a mensagem: **"Data de Vencimento não informada."**

Essa mensagem impede a conclusão da importação e ocorre quando o campo **Dt. Vencimento** não está preenchido ou quando as preferências de importação estão configuradas para solicitar a data ao usuário, mas nenhuma data é informada.

### SOLUÇÃO

Para concluir a importação, siga os passos abaixo:

**(1)** Acesse o **"Portal de Importação"** (Comercial » Rotinas » Portal de importação de XML) e localize o CT-e que apresentou o erro.
**(2)** Na grade principal, preencha manualmente o campo **Dt. Vencimento** com a data desejada para o vencimento do título financeiro.
**(3)** Confirme a importação. O sistema processará o CT-e sem novas ocorrências.

**Configurar o preenchimento automático da data de vencimento**

Caso deseje evitar o preenchimento manual em futuras importações:

**(4)** No **Portal de Importação**, clique em **Outras Opções > Preferências de Importação de CT-e.**
**(5)** No campo **Expira em**, altere a opção **Solicitar ao usuário** para uma das seguintes alternativas:

- **Data Atual:**  utiliza data atual
- **Data de Negociação :** utiliza a data de negociação do documento.
- **Data de Vencimento :** utiliza a data de vencimento informada no XML.
- **Data Solicitada :** utiliza uma data específica configurada.

**(6)** Salve as alterações. A partir dessa configuração, o sistema preencherá automaticamente a data de vencimento conforme a regra selecionada.

### CAUSA

O problema ocorre quando o campo **Expira em** está configurado como **Solicitar ao usuário** e nenhuma data de vencimento é informada durante a importação do CT-e.
