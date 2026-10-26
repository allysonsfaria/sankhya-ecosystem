---
id: "360044617473"
titulo: "O código da atividade econômica informado deve ser um código válido da tabela 9"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617473-O-c%C3%B3digo-da-atividade-econ%C3%B4mica-informado-deve-ser-um-c%C3%B3digo-v%C3%A1lido-da-tabela-9"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:52:53Z"
rotulos: ["Configuração", "Impostos", "EFD", "MS1106", "Verifique e ajuste campos como \"Cód. Atividade CPRB\" e \"CNAE\".", "Transmita novamente o Reinf após os ajustes.", "Código da atividade econômica deve ser válido na tabela 9.", "Erro", "Tabela 9", "Reintegra"]
---

# O código da atividade econômica informado deve ser um código válido da tabela 9

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16416187286679) MENSAGEM:**

[MS1106]: O código da atividade econômica informado deve ser um código válido da tabela 9.

**![Imagem 2: SITUAÇÃO: Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.](https://ajuda.sankhya.com.br/hc/article_attachments/16416153518871) SITUAÇÃO:**
Ao transmitir as informações do EFD-Reinf, ocorre a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16416187290647) SOLUÇÃO:**

Considere o comportamento da aplicação, conforme abaixo:

(2)** Serviço:**
Configurações » Cadastros » Produtos » Serviço

(2)** Produto:**
Configurações » Cadastros » Produtos » Produtos

![Imagem 4: O sistema verifica se o produto ou serviço possui o campo 'Enquadrado no Reintegra/Prev'(Aba: Impostos) configurado:](https://ajuda.sankhya.com.br/hc/article_attachments/16416153522967) O sistema verifica se o produto ou serviço possui o campo 'Enquadrado no Reintegra/Prev'(Aba: Impostos) configurado:

![Imagem 5: O sistema verifica se o produto ou serviço possui o campo 'Enquadrado no Reintegra/Prev'(Aba: Impostos) configurado:](https://ajuda.sankhya.com.br/hc/article_attachments/14996664602775)

![Imagem 6: Se estiver configurado, o sistema verifica se o campo "Cód. Atividade CPRB (Reintegra/Prev.)" está preenchido. Este…](https://ajuda.sankhya.com.br/hc/article_attachments/16416187293719) Se estiver configurado, o sistema verifica se o campo **"Cód. Atividade CPRB (Reintegra/Prev.)"** está preenchido. Este campo estando preenchido, ele o utiliza como código de atividade.

Não estando preenchido o campo Cód. Atividade CPRB (Reintegra/Prev.) o sistema verifica se o campo **"Código Atividade Reintegra"** está preenchido e se estiver o sistema o utiliza como código de atividade.

![Imagem 7: Se o campo Código Atividade Reintegra não estiver preenchido, ele verifica se trata-se de receita oriunda da venda de…](https://ajuda.sankhya.com.br/hc/article_attachments/16416187294999) Se o campo Código Atividade Reintegra não estiver preenchido, ele verifica se trata-se de receita oriunda da venda de um produto e ou serviço.

- Se Produto: sendo a receita oriunda da venda de um produto ele considera o conteúdo do campo 'NCM' da aba Geral do cadastro do produto;
- Se Serviço: sendo a receita oriunda da venda de um serviço ele verifica o conteúdo do campo 'CNAE' informado na aba Impostos do cadastro de serviços;

![Imagem 8: Estando o campo "CNAE" preenchido ele o utiliza como código de atividade. Caso contrário, não estando o campo CNAE…](https://ajuda.sankhya.com.br/hc/article_attachments/16416153527575) Estando o campo **"CNAE"** preenchido ele o utiliza como código de atividade. Caso contrário, não estando o campo CNAE preenchido, ele utiliza o conteúdo do campo **"Código Atividade Prest. Serviços e Produtos"** informado na aba **"Reintegra Previdência"** da tela **"Preferencias Empresas"**.

![Imagem 9: Caso o campo "Enquadrado no Reintegra/Prev" não esteja configurado ele utiliza o conteúdo do campo Código Atividade…](https://ajuda.sankhya.com.br/hc/article_attachments/16416153528343) Caso o campo **"Enquadrado no Reintegra/Prev"** não esteja configurado ele utiliza o conteúdo do campo Código Atividade Prest. Serviços e Produtos informado na aba Reintegra Previdência da tela Preferencias Empresas (Caminho de acesso: Comercial » Preferências » Empresa).

![Imagem 10: Efetue os devidos ajustes, de acordo com a considerações acima, caso tenha dúvidas quanto à informação do Código CNAE,…](https://ajuda.sankhya.com.br/hc/article_attachments/16416153531159) Efetue os devidos ajustes, de acordo com a considerações acima, caso tenha dúvidas quanto à informação do Código CNAE, busque orientações do Contador para obter o valor correto.

![Imagem 11: Após os ajustes, transmita novamente o Reinf.](https://ajuda.sankhya.com.br/hc/article_attachments/16416203867927) Após os ajustes, transmita novamente o Reinf.

**![Imagem 12: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16416203874327) CAUSA:**

Ocorre quando informamos um 'Código de Atividades, Produtos e Serviços Sujeitos à CPRB' não constante na tabela 9 disponível no 'Anexo I dos Leiautes da EFD-Reinf - Tabelas', disponível no link: <http://sped.rfb.gov.br/arquivo/download/2779>
