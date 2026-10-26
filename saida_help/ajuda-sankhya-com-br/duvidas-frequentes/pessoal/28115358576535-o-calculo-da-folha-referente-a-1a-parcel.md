---
id: "28115358576535"
titulo: "O cálculo da folha referente à 1ª parcela do 13º salário não está considerando uma projeção até dezembro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28115358576535-O-c%C3%A1lculo-da-folha-referente-%C3%A0-1%C2%AA-parcela-do-13%C2%BA-sal%C3%A1rio-n%C3%A3o-est%C3%A1-considerando-uma-proje%C3%A7%C3%A3o-at%C3%A9-dezembro"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:26:04Z"
rotulos: ["Configuração", "Folha de Pagamento", "13º Salário", "O cálculo da folha referente à 1ª parcela do 13º salário", "não está considerando uma projeção até dezembro", "Regras de Cálculo", "Pessoal+", "Artigo atualizado KCS", "Sankhya RH - KCS"]
---

# O cálculo da folha referente à 1ª parcela do 13º salário não está considerando uma projeção até dezembro

O cálculo da folha referente à **"1ª parcela do 13º salário"** não está considerando uma projeção até dezembro conforme o esperado. O cálculo desta parcela gera dúvidas sobre a inclusão de médias e a projeção anual.

![Imagem 1: O cálculo da folha referente à "1ª parcela do 13º salário" não está considerando uma projeção até dezembro conforme o…](https://ajuda.sankhya.com.br/hc/article_attachments/28115358541975)

A projeção permite definir se a primeira parcela considera 12/12 avos ou 11/12 avos:

**Interpretação 1 (11/12 avos):** O pagamento considera o período até o mês anterior ao fechamento de dezembro.

**Interpretação 2 (12/12 avos):** O pagamento considera a projeção total do ano, mesmo que o adiantamento ocorra em novembro.

### Funcionamento das médias no 13º salário

As médias não são pagas exclusivamente na segunda parcela. O cálculo é feito de forma completa na segunda parcela para garantir a correção dos valores, incluindo os meses devidos e aplicando os descontos legais. O valor da primeira parcela é abatido, evitando pagamento em duplicidade.

### Solução

**Verifique o sindicato do funcionário:**
Acesse o cadastro do funcionário em (Configurações >> Cadastros >> Pessoal >> Configuração Funcionários). Na aba **"Lotação"**, identifique a qual **"Sindicato"** o funcionário está vinculado.

**Consulte a regra de cálculo do sindicato:**
Acesse a tela de sindicato em (Pessoal+ >> Cadastros >> Sindicato). Verifique o campo **"Regra de Cálculo"** associado ao sindicato.

**Ajuste a regra de cálculo:**
Localize a regra de cálculo em (Pessoal+ >> Cadastros >> Regras de Cálculo). Marque ou desmarque o campo **"Projetar 13° salário até dezembro"** conforme a política da empresa (Marque para 12/12, desmarque para 11/12).

**Recalcule:**
Após realizar o ajuste, recalcule a folha para aplicar as alterações. Caso a alteração não seja aplicada imediatamente, reinicie o sistema no servidor.

### Causa

A regra de cálculo pode estar parametrizada incorretamente, o sistema pode estar retendo cache da configuração anterior ou a regra de negócio da empresa difere do padrão sistêmico.
