---
id: "39354714123287"
titulo: "Importar Dados da SEFAZ: erro de certificado digital não encontrado, mesmo com certificado configurado no Console NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39354714123287-Importar-Dados-da-SEFAZ-erro-de-certificado-digital-n%C3%A3o-encontrado-mesmo-com-certificado-configurado-no-Console-NF-e"
trilha: "Solução de Problemas > Erros Internos"
atualizado_em: "2026-10-16T15:30:26Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Importação", "SEFAZ", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# Importar Dados da SEFAZ: erro de certificado digital não encontrado, mesmo com certificado configurado no Console NF-e

**Mensagem**

Ao tentar importar o cadastro de parceiros pela opção **"Importar Dados da SEFAZ"**, o sistema apresenta erro informando que não foi encontrado certificado ativo, mesmo com o certificado digital da empresa ativa devidamente configurado no **"Console NF-e"**.

**Situação**

Na base de dados existem múltiplas empresas cadastradas, sendo que apenas uma está ativa e em operação. Ao acessar a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e tentar importar dados cadastrais utilizando a funcionalidade **"Importar Dados da SEFAZ"**, o sistema retorna erro relacionado à ausência de certificado digital, mesmo que o certificado da empresa ativa esteja corretamente configurado no **"Console NF-e"**.

**Solução**

Para resolver este problema, ajuste o parâmetro que define qual empresa será utilizada para buscar o certificado digital:

**(1)** Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).
**(2)** Localize o parâmetro **"Empresa padrão para utilização do certificado digital" (EMPPADCERTDIG)**.
**(3)** Verifique o código de empresa informado no parâmetro. Ele deve ser de uma empresa cujo CNPJ tenha certificado digital registrado e dentro da validade no **"Console NF-e"** (aba **"Registro de Certificados"**). Se estiver apontando para uma empresa inativa ou sem certificado, altere para o código da empresa ativa que possui o certificado digital configurado.

**(7)** Salve a alteração e tente realizar novamente a importação dos dados cadastrais pela **"SEFAZ"**.

**Causa**

O erro ocorre porque o parâmetro **"Empresa padrão para utilização do certificado digital" (EMPPADCERTDIG)** estava configurado com o código de uma empresa inativa, que não possuía certificado digital. Para consultar a **"SEFAZ"**, o sistema usa sempre a empresa definida neste parâmetro e procura, no **"Console NF-e"**, o certificado registrado para o CNPJ dessa empresa. Ele não utiliza a empresa logada nem procura o certificado de outra empresa. Como não havia certificado para o CNPJ configurado, a importação falhava, mesmo que outra empresa ativa possuísse certificado corretamente instalado no **"Console NF-e"**.
