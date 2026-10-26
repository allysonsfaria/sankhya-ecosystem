---
id: "360044519733"
titulo: "Qual é a condição do sistema (SankhyaW), para preencher o campo Conta em Dados da Baixa, na Mov. Financeira?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044519733-Qual-%C3%A9-a-condi%C3%A7%C3%A3o-do-sistema-SankhyaW-para-preencher-o-campo-Conta-em-Dados-da-Baixa-na-Mov-Financeira"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T15:55:55Z"
rotulos: ["#validadoElisangela", "Configuração", "Contas", "Movimentação Financeira", "Preferências", "Financeiro", "Conflito com contas monitoradas", "Preenche 'Conta' com prioridade", "SUBSTCONTA substitui se ligado"]
---

# Qual é a condição do sistema (SankhyaW), para preencher o campo Conta em Dados da Baixa, na Mov. Financeira?

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17114790598295) **SITUAÇÃO:**

O sistema segue a seguinte condição para preencher o campo 'Conta' em Dados da Baixa:

![Imagem 2: Primeiro pega a Conta, vinculada no usuário pela aba: "Contas p/ Baixa" .](https://ajuda.sankhya.com.br/hc/article_attachments/17114774122007) Primeiro pega a Conta, vinculada no usuário pela aba: **"Contas p/ Baixa"**.

**(1)** Se estiver vazio: busca a Conta padrão para Baixa, vinculado no usuário, pelo Botão: Outras Opções>>Configurações do Usuário, campo **"Numero da Conta padrão na baixa"**, Lógico = 'S'

**(1)** Se estiver vazio: busca a conta bancaria, diretamente do Titulo Financeiro (Campo: **"Conta Bancária"**, aba: **"Lançamentos"**)

**(1)** Se estiver vazio: busca a Conta, marcada como **"Exclusiva da Empresa"**, na qual o código da empresa vinculada no cadastro da conta seja igual ao código da empresa vinculada ao titulo.

![Imagem 3: Se a conta bancária não estiver marcada como 'Exclusiva da empresa', o sistema considera a Ordem pelo Índice da Tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/17114774129815) Se a conta bancária não estiver marcada como 'Exclusiva da empresa', o sistema considera a Ordem pelo Índice da Tabela de Conta Bancária (TSICTA), que neste caso o índice utilizado e CODEMP.TSIEMP. Isso significa que não necessariamente vai buscar o menor numero de conta cadastrada.

![Imagem 4: Se não houver nenhuma conta com código da empresa igual o código da empresa do título financeiro, o sistema emite a…](https://ajuda.sankhya.com.br/hc/article_attachments/17114790622871) Se não houver nenhuma conta com código da empresa igual o código da empresa do título financeiro, o sistema emite a mensagem ao clicar no botão Baixar:

**Baixa não pode ser realizada!**
**Não há conta bancária!**

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17114790625815) OBSERVAÇÃO:**

**(1)** Parâmetro: **SUBSTCONTA - Substitui Conta do Financeiro com Conta Baixa**

![Imagem 6: (1) Parâmetro: SUBSTCONTA - Substitui Conta do Financeiro com Conta Baixa](https://ajuda.sankhya.com.br/hc/article_attachments/13450294752151)

**(1)** Se o parâmetro estiver **ligado**, a Conta Bancaria do Título (se houver) será alterado pela conta que foi informado na tela de baixa;

**(1)** Para as empresas que trabalham com conta monitorada, essa preferência entra em conflito com a regra do sistema para não permitir alterar a conta informada no financeiro quando essa é uma conta monitorada.

Isso se dá pois quando um título é baixado no caixa, por exemplo, na próxima remessa ele deverá ser informado ao banco para que o mesmo realize a baixa do título em seu sistema.
