---
id: "33163963437719"
titulo: "Não foi encontrada nenhuma conta referencial (J051) cadastrada para esta conta contábil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33163963437719-N%C3%A3o-foi-encontrada-nenhuma-conta-referencial-J051-cadastrada-para-esta-conta-cont%C3%A1bil"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:29:17Z"
rotulos: ["Configuração", "ECD", "Fiscal", "Contabilização", "Não foi encontrada nenhuma conta referencial (J051) cadastrada para esta conta contábil", "bloco J", "Erro"]
---

# Não foi encontrada nenhuma conta referencial (J051) cadastrada para esta conta contábil

**MENSAGEM**:

Não foi encontrada nenhuma conta referencial (J051) cadastrada para esta conta contábil

**SITUAÇÃO**:

Toda conta contábil que tenha movimentação ou saldo na ECD precisa estar **associada a uma conta do plano referencial** da Receita, definida no **bloco J** (Informações do Plano de Contas e Mapeamento).

**SOLUÇÃO**:

**(1)** Identifique a conta contábil que está sem vínculo. Para isso, veja no erro ou na pré-validação qual é o código da conta contábil que não está associada.

Acesse a tela **''Plano de Contas''** (Contabilização » Cadastros » Plano de Contas), selecione a conta identificada no passo anterior e, na aba **''Conta Contábil Referencial'**', preencha o campo **''Tipo''** e a **''Conta Referencial Correspondente''.**

![Imagem 1: Acesse a tela ''Plano de Contas'' (Contabilização » Cadastros » Plano de Contas), selecione a conta identificada no…](https://ajuda.sankhya.com.br/hc/article_attachments/33186067821719)

**CAUSA**:

Ocorre durante a validação da ECD (Escrituração Contábil Digital), indicando que a conta contábil usada nos registros **não está vinculada** a uma conta referencial do plano da Receita Federal (Plano Referencial J050/J051).
