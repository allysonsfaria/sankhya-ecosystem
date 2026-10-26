---
id: "36012858488215"
titulo: "Campo de Cidade de Trabalho retorna valor padrão após o cadastro de funcionário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36012858488215-Campo-de-Cidade-de-Trabalho-retorna-valor-padr%C3%A3o-ap%C3%B3s-o-cadastro-de-funcion%C3%A1rio"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-18T19:57:07Z"
rotulos: ["Configuração", "Funcionários", "Parceiro", "Cidades", "Preferências", "valor", "FPTOMADORDEP", "cadastro", "Campo", "retorna", "funcionário", "Cidade de Trabalho", "padrão", "Duplicado"]
---

# Campo de Cidade de Trabalho retorna valor padrão após o cadastro de funcionário

**SITUAÇÃO:**

Ao cadastrar um novo colaborador por meio da duplicação de um registro existente, o sistema substitui automaticamente o valor do campo **“Cidade de Trabalho”**, independentemente do dado informado no cadastro original.

Esse comportamento ocorre de forma automática e padronizada, conforme as regras internas de definição da localidade no momento da criação do novo cadastro.

**Cadastro anterior:**

![Imagem 1: Cadastro anterior:](https://ajuda.sankhya.com.br/hc/article_attachments/36174853112855)

**Cadastro Duplicado:**

![Imagem 2: Cadastro Duplicado:](https://ajuda.sankhya.com.br/hc/article_attachments/36174853113495)

**SOLUÇÃO:**

Se o desejo é manter a cidade informada manualmente, é necessário desativar o parâmetro **''FPTOMADORDEP'**' (Configurações» Avançado» Preferências). Caso o comportamento esperado seja que o sistema utilize automaticamente a cidade vinculada ao Parceiro do departamento, o parâmetro deve permanecer ativado.

**CAUSA:**

A situação ocorre devido à ativação do parâmetro FPTOMADORDEP. Quando esse parâmetro está ligado, o tomador é associado ao departamento, e o sistema passa a definir automaticamente a Cidade de Trabalho conforme a cidade cadastrada no Parceiro vinculado ao departamento ao qual o colaborador está relacionado.

![Imagem 3: A situação ocorre devido à ativação do parâmetro FPTOMADORDEP . Quando esse parâmetro está ligado, o tomador é…](https://ajuda.sankhya.com.br/hc/article_attachments/36174853116823)

![Imagem 4: A situação ocorre devido à ativação do parâmetro FPTOMADORDEP . Quando esse parâmetro está ligado, o tomador é…](https://ajuda.sankhya.com.br/hc/article_attachments/36174809200791)
