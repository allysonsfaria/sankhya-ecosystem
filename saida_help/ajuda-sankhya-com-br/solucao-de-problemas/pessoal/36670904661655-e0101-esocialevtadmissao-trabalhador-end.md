---
id: "36670904661655"
titulo: "E0101 esocialevtAdmissao/trabalhador/endereco/brasil/codMuncic"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36670904661655-E0101-esocialevtAdmissao-trabalhador-endereco-brasil-codMuncic"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-18T19:53:52Z"
rotulos: ["Configuração", "Cidades", "Mun. domicílio fiscal", "Admissão", "eSocial", "E0101", "Central do eSocial", "Evento s-2200", "Cód. Logradouro p/ E-social", "tabela do IBGE"]
---

# E0101 esocialevtAdmissao/trabalhador/endereco/brasil/codMuncic

**MENSAGEM:**

E0101 esocialevtAdmissao/trabalhador/endereco/brasil/codMuncic

**SITUAÇÃO:**

A mensagem de erro é apresentada ao tentar realizar o envio do **evento S-2200** (Admissão) pela Central do eSocial.

**SOLUÇÃO:**

**(1)** Acesse a tela [**''Cidades''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(2)** Na aba **''Geral''**, o campo **''Mun. domicílio fiscal''** deve estar preenchido conforme a **tabela do IBGE**.

![Imagem 1: (2) Na aba ''Geral'' , o campo ''Mun. domicílio fiscal'' deve estar preenchido conforme a tabela do IBGE .](https://ajuda.sankhya.com.br/hc/article_attachments/36694158106903)

**(3)** Em seguida, acesse a tela [''**Endereços''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602274-Endere%C3%A7os) (Configurações » Cadastros » Endereços » Endereços), e verifique se o campo ''**Cód. Logradouro p/ E-social''** está preenchido corretamente.

![Imagem 2: (3) Em seguida, acesse a tela '' Endereços'' (Configurações » Cadastros » Endereços » Endereços), e verifique se o…](https://ajuda.sankhya.com.br/hc/article_attachments/36694142853015)

**(4)** Após as devidas correções, gere novamente o evento **S-2200** e libere-o para envio.

**(1)**Conforme o leiaute eSocial, a tag [dtAvPrv](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html) (Data de concessão do aviso prévio) deve obrigatoriamente ser preenchida com uma data válida que atenda aos seguintes critérios:

**Validação:** se informada, deve ser igual ou posterior à data de admissão e igual ou anterior a [dtDeslig](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html#2299_infoDeslig_dtDeslig).

**CAUSA:**

O erro ocorre porque o layout do eSocial **exige que essas informações estejam corretamente cadastradas** para envio do evento.

Campos como **Município do domicílio fiscal** e **Código do Logradouro para eSocial** são obrigatórios, e qualquer inconsistência impede a validação do S-2200.

![Imagem 3: Campos como Município do domicílio fiscal e Código do Logradouro para eSocial são obrigatórios, e qualquer…](https://ajuda.sankhya.com.br/hc/article_attachments/36670904661527)
