---
id: "43548958403863"
titulo: "Erro na abertura de Caixa: AberturaCaixaSP.abreCaixaAtualizandoSessao"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548958403863-Erro-na-abertura-de-Caixa-AberturaCaixaSP-abreCaixaAtualizandoSessao"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-10-02T14:42:21Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Erro na abertura de Caixa: AberturaCaixaSP.abreCaixaAtualizandoSessao

**MENSAGEM**

- Falha ao tentar chamar o serviço 'AberturaCaixaSP.abreCaixaAtualizandoSessao'

**SITUAÇÃO**

A mensagem é apresentada quando o usuário tenta abrir um novo caixa, mas já existe uma sessão de caixa aberta para o terminal ou conta utilizada.

Ela também pode ocorrer quando:

- o usuário não está configurado corretamente como **operador de caixa**;
- a conta vinculada ao usuário já possui um caixa aberto em outro usuário.

**SOLUÇÃO**

**(1)** Verifique se existe algum caixa em aberto para o usuário ou para a conta utilizada. Para isso, acesse a tela **"Fechamento de Caixa"** (Financeiro Relatórios Fechamento de Caixa) e filtre pelo período e usuário. Caso sejam identificados caixas sem data de fechamento, realize o fechamento do caixa antes de tentar abrir um novo.

**(2)** Caso não tenha acesso à tela **"Fechamento de Caixa**, utilize o **"DBExplorer"** (Configurações » Avançado » DBExplorer) e execute o comando: **SELECT \* FROM TGFCAI WHERE DTFECHAMENTO IS NULL**. Caso sejam retornados registros, verifique o usuário responsável e realize o fechamento do caixa correspondente.

**(3)** Verifique se o usuário está configurado como operador de caixa. Para isso, acesse a tela **"Usuários"** (Configurações Cadastros Usuários) e confirme se a opção **"Usuário Caixa"** está habilitada.

**(4)** Verifique se as contas de caixa estão vinculadas ao usuário. Na tela **"Usuários"** (Configurações Cadastros Usuários), acesse a aba de contas e confirme se as contas necessárias para a operação estão vinculadas ao usuário.

**(5)** Após realizar os ajustes, tente novamente abrir o caixa. Se a mensagem persistir, verifique se a mesma conta de caixa não está vinculada ou sendo utilizada por outro usuário com uma sessão de caixa aberta.

Exemplo de consulta no **"DBExplorer"**:

![Imagem 1: Exemplo de consulta no "DBExplorer" :](https://ajuda.sankhya.com.br/hc/article_attachments/43548958388375)

Exemplo de identificação de caixas em aberto na tela de **"Fechamento de Caixa"**:

![Imagem 2: Exemplo de identificação de caixas em aberto na tela de "Fechamento de Caixa" :](https://ajuda.sankhya.com.br/hc/article_attachments/43548958395287)

**CAUSA**

A mensagem ocorre quando há tentativa de abrir um novo caixa e a sessão anterior ainda está aberta. Também pode ocorrer quando o usuário não está configurado como **operador de caixa**, não possui **contas de caixa vinculadas** ou quando a conta de caixa já está sendo utilizada por outro usuário.
