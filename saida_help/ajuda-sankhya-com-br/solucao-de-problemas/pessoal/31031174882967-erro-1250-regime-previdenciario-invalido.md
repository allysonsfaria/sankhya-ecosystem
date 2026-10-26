---
id: "31031174882967"
titulo: "Erro 1250 - Regime Previdenciário inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31031174882967-Erro-1250-Regime-Previdenci%C3%A1rio-inv%C3%A1lido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:19Z"
rotulos: ["Eventos", "eSocial", "Configuração Funcionários", "Central do eSocial", "Regime Previdenciário", "Regime Previdenciário inválido", "Erro 1250", "Erro"]
---

# Erro 1250 - Regime Previdenciário inválido

**MENSAGEM:**

Erro 1250 - Regime Previdenciário inválido. Ação Sugerida: Se o campo 'codCateg' for [101, 102, 103, 105, 106, 107, 108, 111], este campo 'tpRegPrev' não poderá ser preenchido com [2, 4]. Elemento: /eSocial/evtAdmissao/vinculo/tpRegPrev [2] -----------------------------------Erro 1526 - Não é possível receber o evento. Ação Sugerida: Caso tenha sido enviado o evento S-2190 para o mesmo contrato de trabalho (CPF + matrícula) e se 'indRetif' do evento S-2200 for igual a [1]: a) Os campos 'codCateg' e 'natAtividade' informados no evento S-2190 devem ser idênticos ao respectivos campos do evento S-2200 b) O campo 'dtAdm' informado no evento S-2190 deve ser idêntico ao respectivo campo do evento S-2200 c) O campo 'tpRegTrab' deve ser igual a [1] e o campo 'tpRegPrev' deve ser igual a [1, 3]

 **SOLUÇÃO:**

O erro ocorre devido ao preenchimento incorreto do campo **"Regime Previdenciário"** no cadastro do funcionário na tela **"Configurações Funcionários"**.

Assim, ajuste o campo para o regime previdenciário correspondente à categoria do eSocial. Por exemplo, se o código da categoria do eSocial for **101**, o regime previdenciário deverá ser **RPPS - Regime Próprio de Previdência Social**. Após o ajuste, gere novamente o evento.

![Imagem 1: Assim, ajuste o campo para o regime previdenciário correspondente à categoria do eSocial. Por exemplo, se o código da…](https://ajuda.sankhya.com.br/hc/article_attachments/31031168139799)
