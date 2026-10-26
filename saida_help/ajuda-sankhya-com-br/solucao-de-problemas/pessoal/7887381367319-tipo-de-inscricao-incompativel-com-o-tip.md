---
id: "7887381367319"
titulo: "Tipo de inscrição incompatível com o tipo de lotação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7887381367319-Tipo-de-inscri%C3%A7%C3%A3o-incompat%C3%ADvel-com-o-tipo-de-lota%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:24:20Z"
rotulos: ["Configuração", "Empresa", "Parceiro", "não apagar", "#ValidadoAline", "eSocial", "Erro 389", "Central do eSocial", "Verifique tipo de lotação", "Erro 389: inscrição incompatível", "Ajuste e reenviar S-1020", "Erro"]
---

# Tipo de inscrição incompatível com o tipo de lotação

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16541989997079) MENSAGEM**:

Erro 389 - Tipo de inscrição incompatível com o tipo de lotação
Ação Sugerida: O campo deverá ser preenchido com um Tipo de Inscrição compatível com o Tipo de Lotação, conforme definido na "Tabela 10 - (Tipo de Lotação)".
Elemento: /eSocial/evtTabLotacao/infoLotacao/alteracao/dadosLotacao/tpInsc[1]

Erro 388 - Tipo de lotação incompatível.
Ação Sugerida: Tipo de Lotação deverá ser compatível com a classificação tributária do empregador cadastrada para o período da lotação.
Elemento: /eSocial/evtTabLotacao/infoLotacao/inclusao/dadosLotacao/tpLotacao
[00]"

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16541963651479) SITUAÇÃO:**

Ao tentar enviar o S-1020 ocorre o erro.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16541990001687)SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo:

#### SankhyaOM

![Imagem 4: Acesse a tela "Empresa" (Configurações » Cadastros » Pessoal » Empresas);](https://ajuda.sankhya.com.br/hc/article_attachments/16541963655831) Acesse a tela **"Empresa"** (Configurações » Cadastros » Pessoal » Empresas);

![Imagem 5: Na aba "Informações fiscais" verifique o tipo de lotação;](https://ajuda.sankhya.com.br/hc/article_attachments/16541963657111) Na aba **"Informações fiscais"** verifique o tipo de lotação;

![Imagem 6: Na aba "Informações fiscais" verifique o tipo de lotação;](https://ajuda.sankhya.com.br/hc/article_attachments/16541963663639)

![Imagem 7: Se o tipo de lotação não for compatível com o tipo de inscrição da empresa, faça o ajuste da lotação;](https://ajuda.sankhya.com.br/hc/article_attachments/16541963660055) Se o tipo de lotação não for compatível com o tipo de inscrição da empresa, faça o ajuste da lotação;

**(4)** Em seguida, acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e, na aba **"Lotação",** preencha ou faço o devido ajuste do campo **"Tipo de lotação";**

![Imagem 8: (4) Em seguida, acesse a tela "Parceiros" (Configurações » Cadastros » Parceiros) e, na aba "Lotação", preencha ou faço…](https://ajuda.sankhya.com.br/hc/article_attachments/33226412280727)

**(5)** Após isso, gere o S-1020 para envio novamente.

---

#### MGE Pessoal: Arquivos » Empresas, aba 'Informações Fiscais'

**(1)**  Acesse a tela **"Empresa"** (Arquivos>> Empresas) e na aba **"Informações fiscais"** verifique o tipo de lotação;

![Imagem 9: (1) Acesse a tela "Empresa" (Arquivos>> Empresas) e na aba "Informações fiscais" verifique o tipo de lotação;](https://ajuda.sankhya.com.br/hc/article_attachments/16541963665175)

**(2)** Se o tipo de lotação não for compatível com o tipo de inscrição da empresa, faça o ajuste da lotação;

**(3)** Depois, acesse a tela **"Parceiros"** (MGEPessoal » Arquivos » Parceiros), na aba **"Tomador",** preencha o campo **"Tipo de Lotação"** e salve a alteração;

![Imagem 10: (3) Depois, acesse a tela "Parceiros" (MGEPessoal » Arquivos » Parceiros), na aba "Tomador", preencha o campo "Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/33227211594135)

**(4)** Por fim, vá até a tela **"Central do E-social"** (MGEPessoal » Avançado » Central do E-social) e transmita novamente as obrigações.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16541990017303)CAUSA:**

Ocorre quando o tipo de inscrição está incompatível com o tipo de lotação informada, neste caso precisa verificar na "Tabela 10 - (Tipo de Lotação)" para configurar corretamente o campo tipo de lotação.

[Site do esocial:](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/leiautes-do-esocial-v2-5-anexo-i-tabelas-nt-19-2020.pdf/view)
