---
id: "14221087610903"
titulo: "A conta selecionada não possui modelo de boleto vinculado. Por favor informe um Modelo de boleto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14221087610903-A-conta-selecionada-n%C3%A3o-possui-modelo-de-boleto-vinculado-Por-favor-informe-um-Modelo-de-boleto"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-09-28T18:44:28Z"
rotulos: ["Configuração", "Contas", "Boleto", "Financeiro", "CORE_E01381", "Conta sem Modelo", "Cadastro da Conta", "Vínculo do Modelo", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# A conta selecionada não possui modelo de boleto vinculado. Por favor informe um Modelo de boleto

[CORE\_E01381] A conta selecionada não possui modelo de boleto vinculado. Por favor informe um modelo de boleto.

### SITUAÇÃO

Esta mensagem aparece ao tentar **"Imprimir um boleto"** no sistema. O erro ocorre quando o usuário seleciona uma conta bancária para emissão do boleto, mas o sistema identifica que não há um modelo de boleto configurado para aquela conta específica.

### SOLUÇÃO

Para resolver este erro, verifique se a conta bancária está configurada corretamente e se há alguma configuração de modelo de boleto na aba **Boleto(s)/Duplicatas**, na tela Contas. Essa situação ocorre porque não há um modelo de boleto cadastrado dentro da conta. O Sankhya trabalha com dois níveis de cadastro para modelos de boleto:

Seguem as orientações para resolução:

**(1)** Acesse **Financeiro » Relatórios » Modelos de Boleto(s) >** Clique em **+ (Novo) >** Informe a **Descrição** do modelo.

**(2)**Clique em **Outras Opções** e faça o download do arquivo correspondente ao seu processo.

**(3)**Na aba **Arquivo**, clique em **Adicionar Arquivo** e selecione o arquivo baixado > Salve o cadastro.

![Imagem 1: (3) Na aba Arquivo , clique em Adicionar Arquivo e selecione o arquivo baixado > Salve o cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/43824875689239)

**Observação:** Certifique-se de utilizar o arquivo correspondente ao layout adotado pela instituição financeira e ao processo utilizado pela empresa, garantindo o correto funcionamento da emissão dos boletos.

**Após criar o modelo de boleto, realize o vínculo dele ao cadastro de modelos de impressão.**

**(1)** Acesse **Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)**.

**(2)** Clique em **Cadastrar** ou **Novo** para incluir um novo registro.

**(3)** Preencha os campos obrigatórios:

- **Descrição:** informe um nome que facilite a identificação do modelo (exemplo: **Modelo Boleto Banco XXX**).
- **Número do relatório:** selecione o modelo de boleto criado anteriormente na tela **Modelos de Boleto(s)** (exemplo: **Modelo Boleto Banco XXX**).

**(4)** Clique em **Salvar** para concluir o cadastro.

> **Importante:** o modelo de boleto deve ter sido criado previamente na tela **Modelos de Boleto(s)** para que esteja disponível na seleção do campo **Número do relatório**.

![Imagem 2: Importante: o modelo de boleto deve ter sido criado previamente na tela Modelos de Boleto(s) para que esteja disponível…](https://ajuda.sankhya.com.br/hc/article_attachments/43824875690647)

**Vincular à Conta Bancária**

**(1)**Acesse: **Configurações » Cadastros » Bancários » Contas**, selecione a conta bancária desejada e clique na aba **"Boleto(s)/Duplicatas"**

**(2)**Agora o modelo criado na Etapa 1 deverá aparecer no campo **"Modelo"** ou **"Modelo Cobrança";**

![Imagem 3: (2) Agora o modelo criado na Etapa 1 deverá aparecer no campo "Modelo" ou "Modelo Cobrança";](https://ajuda.sankhya.com.br/hc/article_attachments/43824844978711)

### CAUSA

Ocorre quando o modelo de boleto não está informado no cadastro da conta utilizada para a impressão.

###
