---
id: "39379487442839"
titulo: "Erro na importação de funcionários via busca de CEP no Pessoal+ - Não insere rua, bairro e cidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39379487442839-Erro-na-importa%C3%A7%C3%A3o-de-funcion%C3%A1rios-via-busca-de-CEP-no-Pessoal-N%C3%A3o-insere-rua-bairro-e-cidade"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:20Z"
rotulos: ["Configuração", "Cidades", "Importação", "Preferências", "Pessoal+", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro na importação de funcionários via busca de CEP no Pessoal+ - Não insere rua, bairro e cidade

**Mensagem**

O sistema não insere corretamente os dados de endereço, bairro e cidade na tabela funcionários ao realizar a importação de cadastro de funcionários utilizando a funcionalidade de busca de CEP.

**Situação**

Ao realizar a importação de cadastro de funcionários no módulo **"Pessoal+"**  utilizando a funcionalidade de busca de CEP no site dos Correios, o sistema não preenche automaticamente os campos de logradouro, bairro e cidade na tabela funcionários, mesmo após a consulta retornar os dados corretamente.

**Solução**

Para resolver o problema de preenchimento automático dos dados de endereço, siga os passos abaixo:

**(1)** Acesse o módulo **"Pessoal+"** (Configurações » Cadastros » Pessoal » Configuração Funcionários) e localize o cadastro do funcionário que apresenta o problema.
**(2)** Verifique se o parâmetro Configurações » Avançado » Preferências **"Tipo de Consulta de CEP"** (TIPOCONSULTACEP) está configurado como **"Usa informações dos Correios"**.
**(3)** Confirme se o parâmetro Configurações » Avançado » Preferências **"URL Web Service Correios"** (URLWSCORREIOS) está corretamente preenchido com a URL válida para consulta de CEPs.
**(4)** Realize uma nova busca pelo CEP desejado no campo correspondente e pressione **"Enter"** ou **"Tab"** para executar a consulta.

![Imagem 1: Verifique se o CEP informado está correto e existe na base dos Correios. Caso necessário, valide o CEP diretamente no…](https://ajuda.sankhya.com.br/hc/article_attachments/40875637148311)
**(5)** Verifique se o CEP informado está correto e existe na base dos Correios. Caso necessário, valide o CEP diretamente no site dos Correios antes de realizar a importação.
**(6)** Após a consulta retornar os dados corretamente, confirme se os campos **"Logradouro"**, **"Bairro"** e **"Cidade"** foram preenchidos automaticamente.
**(7)** Salve o cadastro do funcionário e verifique se as informações foram gravadas corretamente na tabela funcionários.

**Causa**

O problema pode ocorrer devido a **inconsistências no CEP informado**, que pode não existir na base dos Correios ou estar desatualizado. Além disso, a **configuração incorreta dos parâmetros** TIPOCONSULTACEP e URLWSCORREIOS pode impedir que o sistema realize a consulta adequadamente e preencha os dados de endereço na tabela funcionários.

Outra causa comum é a **falta de conexão ou instabilidade** no serviço de consulta dos Correios no momento da importação, o que impede o retorno correto das informações de endereço.
