---
id: "31005639163543"
titulo: "Erro 1898 - Matrícula do Trabalhador no Empregador Anterior inválida - Em caso de funcionário transferido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31005639163543-Erro-1898-Matr%C3%ADcula-do-Trabalhador-no-Empregador-Anterior-inv%C3%A1lida-Em-caso-de-funcion%C3%A1rio-transferido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:12Z"
rotulos: ["Folha", "eSocial", "Configuração Funcionários", "Central do eSocial", "Cadastro", "Erro 1898", "Matrícula do Trabalhador no Empregador Anterior inválida", "Em caso de funcionário transferido", "Erro", "Artigo atualizado KCS", "Sankhya RH - KCS"]
---

# Erro 1898 - Matrícula do Trabalhador no Empregador Anterior inválida - Em caso de funcionário transferido

**"Mensagem"**: [1898] Matrícula do trabalhador no empregador anterior inválida. Ação sugerida: deve existir um contrato (S-2190 ou S-2200) no RET do empregador anterior com matrícula do trabalhador idêntica.

Nota: Caso o erro 911 também seja apresentado, verifique se a data informada é anterior ao início da obrigatoriedade do empregador ao eSocial.

### SITUAÇÃO

Ao enviar o evento **"S-2200"** (Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador) ou **"S-1200"** ao eSocial, o sistema apresenta o erro **"1898"**, indicando que a matrícula do trabalhador no empregador anterior está inválida.

### SOLUÇÃO

Para resolver o erro **"1898"**, verifique e ajuste as informações conforme as situações abaixo:

**Situação 1: Funcionário com transferência entre empresas do mesmo grupo**

Acesse o cadastro do funcionário na tela **"Configuração Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários).
 Navegue até a aba **"Afastamento"** e selecione **"Transferido de"**.

![Imagem 1: Verifique se os campos "Matrícula" e "Matrícula Alternativa" estão preenchidos simultaneamente.](https://ajuda.sankhya.com.br/hc/article_attachments/40922934422679)
 Verifique se os campos **"Matrícula"** e **"Matrícula Alternativa"** estão preenchidos simultaneamente.

![Imagem 2: Verifique se os campos "Matrícula" e "Matrícula Alternativa" estão preenchidos simultaneamente.](https://ajuda.sankhya.com.br/hc/article_attachments/40922934424471)

![Imagem 3: Salve as alterações caso seja necessário e gere novamente o evento "S-2200" e/ ou "S-1200" .](https://ajuda.sankhya.com.br/hc/article_attachments/40922978796183)
 Salve as alterações caso seja necessário e gere novamente o evento **"S-2200" e/ ou "S-1200"**.

**Situação 2: Matrícula na empresa anterior divergente do eSocial**

Acesse o cadastro do funcionário na tela **"Configuração Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários).
 Navegue até a aba **"Admissão"** e localize o campo **"Matrícula na Empresa Anterior"**.

![Imagem 4: Consulte no portal do eSocial qual é a matrícula correta registrada na empresa de origem. Ajuste o campo "Matrícula na…](https://ajuda.sankhya.com.br/hc/article_attachments/40922934433559)
 Consulte no portal do eSocial qual é a matrícula correta registrada na empresa de origem.
 Ajuste o campo **"Matrícula na Empresa Anterior"** conforme consta no eSocial.
 Salve as alterações e envie novamente o evento **"S-2200"**.

**Situação 3: Configuração do campo "Cadastro Inicial do Vínculo"**

O campo **"Cadastro Inicial do Vínculo"** (na tela de **Configuração Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários) ou aba **"Admissão"**) deve ser marcado caso o ingresso do trabalhador seja anterior à obrigatoriedade do eSocial. Se o funcionário foi admitido após essa data, o campo deve estar desmarcado. Verifique o status atual e ajuste conforme a regra da data de obrigatoriedade da empresa.

 ![Imagem 5: O campo "Cadastro Inicial do Vínculo" (na tela de Configuração Funcionários" (Pessoal+ » Cadastros » Configuração…](https://ajuda.sankhya.com.br/hc/article_attachments/40922978803863)

### CAUSA

- Preenchimento simultâneo de **"Matrícula"** e **"Matrícula Alternativa"**.
- Divergência entre a matrícula informada no sistema e a registrada no eSocial da empresa anterior.
- Configuração incorreta do campo **"Cadastro Inicial do Vínculo"** em relação à data de obrigatoriedade.
