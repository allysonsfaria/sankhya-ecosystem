---
id: "9683618833687"
titulo: "Não existe 'Natureza x Serviço x ISS' cadastrado para o Contrato: X, Empresa: X e Natureza: null"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9683618833687-N%C3%A3o-existe-Natureza-x-Servi%C3%A7o-x-ISS-cadastrado-para-o-Contrato-X-Empresa-X-e-Natureza-null"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:06:30Z"
rotulos: ["ISS", "Configuração", "Alíquota de ISS", "Contrato", "Financeiro", "Natureza", "SVC_E00334", "Verifique alíquotas e serviços", "Revise \"Natureza x Serviço\" e \"Natureza de Receita\"", "Considere marcar \"Considerar Contatos/Perfil/Serviço\"", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Não existe 'Natureza x Serviço x ISS' cadastrado para o Contrato: X, Empresa: X e Natureza: null

**MENSAGEM**

[SVC\_E00334]: Não existe **"Natureza x Serviço x ISS"** cadastrado para o Contrato: X, Empresa: X e Natureza: null.

**SITUAÇÃO**

Ao tentar realizar o faturamento de um contrato, o sistema bloqueia a operação e apresenta a mensagem de exceção informando que não existe o vínculo entre **"Natureza x Serviço x ISS"** cadastrado para o contrato específico.

**CAUSA**

O erro ocorre porque a natureza de operação utilizada no contrato não possui o vínculo cadastrado com o serviço correspondente. O sistema exige que, para contratos de serviço que envolvem cálculo de **"ISS"**, exista uma relação configurada entre a natureza de operação, o serviço prestado e a tributação de **"ISS"** aplicável. Sem esse vínculo, o sistema não consegue identificar as regras tributárias necessárias para processar o faturamento, bloqueando a operação.

**SOLUÇÃO**

Verifique se as alíquotas de **"ISS"** e o serviço estão corretas nas seguintes telas:

**(1)** Na tela **"Natureza x Serviço"** (Contratos e Serviços >> Arquivos >> Cadastros >> Naturezas >> Natureza x Serviço)

![Natureza x Serviço](https://ajuda.sankhya.com.br/hc/article_attachments/9683406422039)

**(2)** Na tela **"Natureza de Receita e Despesas"** (Configurações >> Cadastros >> Gerencial >> Natureza de Receitas e Despesas), aba **"Serviços autorizados"**.

![Natureza de Receita e Despesas](https://ajuda.sankhya.com.br/hc/article_attachments/16777470817687)

**(3)** Na tela **"Faturamento de contratos"** (Contratos e Serviços >> Rotinas >> Faturamento de Contratos), aba **"Filtro Personalizado"**, campo **"Considerar contratos/perfil/serviço"**.

![Faturamento de contratos](https://ajuda.sankhya.com.br/hc/article_attachments/16777470822423)

**(4)** A opção **"Considerar contratos/perfil/serviço"** funciona da seguinte maneira:

- Caso o parceiro possua um perfil vinculado e este tenha um perfil de consumo, na nota gerada no faturamento do contrato com essa opção marcada serão gerados também itens para cada produto desse perfil de consumo do parceiro.
- Se esta opção estiver desmarcada e o parâmetro **"Contrato para software? - CONTSOFT"** estiver ligado, o sistema validará se existe **"ISS"** cadastrado para a relação Natureza x Serviço e incluirá um item na nota com valor zero para o serviço encontrado na relação com a natureza.
- Caso a opção esteja desmarcada, considere marcar e realizar o teste.

**(5)** Após realizar as configurações, tente executar novamente o faturamento do contrato.

**CAUSA:**

Quando as configurações necessárias de Narureza X Serviço X ISS não estão devidamente configurados.
