---
id: "32238275309463"
titulo: "(Visto Fer) Aviso ao Salvar Informações do Contrato de Trabalho do Processo Trabalhista: \"Atenção! Campo Data desligamento (Decisão Judicial) é obrigatório!\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32238275309463--Visto-Fer-Aviso-ao-Salvar-Informa%C3%A7%C3%B5es-do-Contrato-de-Trabalho-do-Processo-Trabalhista-Aten%C3%A7%C3%A3o-Campo-Data-desligamento-Decis%C3%A3o-Judicial-%C3%A9-obrigat%C3%B3rio"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:45Z"
rotulos: ["Contrato", "eSocial", "Configuração Funcionários", "evento S-2200", "Campo Data desligamento", "obrigatório", "Trabalhador contratado pelo declarante", "Trabalhador com vínculo formalizado", "Decisão Judicial", "campo não é exibido", "com inclusão ou alteração de data de desligamento", "Erro", "Central de Projetos"]
---

# (Visto Fer) Aviso ao Salvar Informações do Contrato de Trabalho do Processo Trabalhista: "Atenção! Campo Data desligamento (Decisão Judicial) é obrigatório!"

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32483335101847) **MENSAGEM:**

**"Atenção! Campo Data desligamento (Decisão Judicial) é obrigatório!"**

**![7759daef-4eea-4400-971f-cab8e302d4e6](https://ajuda.sankhya.com.br/hc/article_attachments/32238275282711) SITUAÇÃO:**

Ao tentar salvar as Informações do Contrato de Trabalho do Processo Trabalhista, é exibida a mensagem acima. No entanto, o campo **“Data de desligamento (Decisão Judicial)”** não é exibido na tela para o preenchimento.

**SOLUÇÃO:**

Siga as orientações abaixo para corrigir o erro e salvar as informações corretamente:

![Imagem 3: V erifique o envio do evento S-2200](https://ajuda.sankhya.com.br/hc/article_attachments/32400323491991) Verifique o envio do **evento S-2200**

Acesse os registros do eSocial e certifique-se de que o evento S-2200 do trabalhador em questão foi **enviado com sucesso** e está **com recibo**. 

![Imagem 4: Na tela ''Processo Trabalhista'' (Pessoal+ » Rotinas Folha » Processo Trabalhista), aba “Informações do Trabalhador”,…](https://ajuda.sankhya.com.br/hc/article_attachments/32400323494039) Na tela **''Processo Trabalhista''** (Pessoal+ » Rotinas Folha » Processo Trabalhista), aba **“Informações do Trabalhador”,** marque a opção **“Trabalhador contratado pelo declarante”**.

**Importante**: isso é fundamental para que o sistema identifique a contratação como própria e permita o vínculo com as informações da empresa.

![Imagem 5: Ainda na tela Processo Trabalhista, no card "Informações de Contrato de Trabalho" selecione o tipo de contrato ''3 -…](https://ajuda.sankhya.com.br/hc/article_attachments/32522572740119)  Ainda na tela Processo Trabalhista,  no card **"Informações de Contrato de Trabalho"** selecione o tipo de contrato **''3 - Trabalhador com vínculo formalizado, com inclusão ou alteração de data de desligamento''.**

![Imagem 6: Ai nda na aba do ' 'contrato'', assinale a opção “Incluir data de desligamento” . Somente dessa forma o campo “Data de…](https://ajuda.sankhya.com.br/hc/article_attachments/32522675006231) Ainda na aba do '**'contrato'',** assinale a opção **“Incluir data de desligamento”**. Somente dessa forma o campo **“Data de desligamento (Decisão Judicial)”** será disponibilizado para preenchimento.

**(1)**Após o campo **“Data de desligamento (Decisão Judicial)”** ser exibido, informe a **data de desligamento** e prossiga com o salvamento das informações.

**CAUSA:**

Para o Tipo de Contrato: **''3 - Trabalhador com vínculo formalizado, com inclusão ou alteração de data de desligamento'',** o sistema realiza algumas validações para exibir o campo **“Incluir data de desligamento”:**

- Precisa constar **evento S-2200 (Admissão) enviado com sucesso** e **com recibo do eSocial**.
- Na tela de ''**Informações do Trabalhador''**, o campo **“Trabalhador contratado pelo declarante”** deve estar marcado.
