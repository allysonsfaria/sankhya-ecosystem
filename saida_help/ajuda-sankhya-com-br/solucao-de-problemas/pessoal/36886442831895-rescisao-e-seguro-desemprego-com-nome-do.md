---
id: "36886442831895"
titulo: "Rescisão e Seguro-Desemprego com nome do funcionário incorreto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36886442831895-Rescis%C3%A3o-e-Seguro-Desemprego-com-nome-do-funcion%C3%A1rio-incorreto"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:03Z"
rotulos: ["Relatórios", "RFB", "Folha", "Configuração Funcionários", "Erro", "nome social", "Rescisão e Seguro Desemprego", "nome incompleto do funcionário", "Termo de rescisão", "Arquivo do Seguro Desemprego", "Artigo atualizado KCS", "Sankhya RH - KCS", "Seguro-Desemprego"]
---

# Rescisão e Seguro-Desemprego com nome do funcionário incorreto

SITUAÇÃO

Ao emitir o Recibo de Rescisão e gerar o arquivo do Seguro-Desemprego, o nome do colaborador pode ser apresentado de forma incorreta, utilizando o **Nome Social** em vez do **Nome Civil** cadastrado.

**Exemplo:**

**Termo de rescisão com nome incompleto**

![Imagem 1: Termo de rescisão com nome incompleto](https://ajuda.sankhya.com.br/hc/article_attachments/36909974717719)

**Arquivo Seguro Desemprego**

![Imagem 2: Arquivo Seguro Desemprego](https://ajuda.sankhya.com.br/hc/article_attachments/36909975960471)

MENSAGEM

O arquivo do Seguro-Desemprego é gerado por meio da tela **Gerenciador de Folhas** (**Pessoal+ > Rotinas Folha > Gerenciador de Folhas**).

Para realizar a geração:

1. Selecione a rescisão desejada;
2. Clique no botão **"Gerar arquivo para Seguro-Desemprego"**.

Após a execução da rotina, o sistema gerará automaticamente um arquivo no formato **TXT**, contendo as informações necessárias para importação e processamento do requerimento do Seguro-Desemprego.

![Imagem 3: Após a execução da rotina, o sistema gerará automaticamente um arquivo no formato TXT , contendo as informações…](https://ajuda.sankhya.com.br/hc/article_attachments/36909975965463)

![Imagem 4: Após a execução da rotina, o sistema gerará automaticamente um arquivo no formato TXT , contendo as informações…](https://ajuda.sankhya.com.br/hc/article_attachments/36909975960471)

SOLUÇÃO

Para corrigir a exibição do nome incompleto nos documentos, siga os passos abaixo:

Acesse a tela **Configuração Funcionários** (**Pessoal+ > Cadastros > Configuração Funcionários**) e localize o colaborador desejado.

Analise qual nome está sendo apresentado nos documentos e compare com os campos **Nome** e **Nome Social** cadastrados no sistema.

![Imagem 5: Analise qual nome está sendo apresentado nos documentos e compare com os campos Nome e Nome Social cadastrados no…](https://ajuda.sankhya.com.br/hc/article_attachments/36909974726807)![Imagem 6: Analise qual nome está sendo apresentado nos documentos e compare com os campos Nome e Nome Social cadastrados no…](https://ajuda.sankhya.com.br/hc/article_attachments/41055553476247)

Caso o funcionário possua **Nome Social** cadastrado na Receita Federal (RFB), a opção **"Travesti ou Transexual?"** deverá estar marcada e o campo **"Nome Social"** deverá ser preenchido exatamente conforme registrado na RFB.

Quando essa configuração estiver habilitada, o sistema passará a utilizar o nome social na emissão dos relatórios de **Rescisão** e **Seguro-Desemprego**.

![Imagem 7: Quando essa configuração estiver habilitada, o sistema passará a utilizar o nome social na emissão dos relatórios de…](https://ajuda.sankhya.com.br/hc/article_attachments/36909975967895)

**Se o funcionário não possua Nome Social registrado na Receita Federal ou o campo tenha sido preenchido indevidamente:**

- O campo **"Nome Social"** não deve estar preenchido;
- A opção **"Travesti ou Transexual?"** deve ser desmarcada.

Ao desmarcar o campo **"Travesti ou Transexual"**, o sistema desabilita o campo **"Nome Social"** e os relatórios passarão a ser emitidos conforme o campo **"Nome"** civil no cadastro do funcionário.

![Imagem 8: Ao desmarcar o campo "Travesti ou Transexual" , o sistema desabilita o campo "Nome Social" e os relatórios passarão a…](https://ajuda.sankhya.com.br/hc/article_attachments/36909974726807)

Salve as alterações e gere novamente o documento para validação.

**Exemplo pós-correção:**

**Termo de Rescisão**

![Imagem 9: Termo de Rescisão](https://ajuda.sankhya.com.br/hc/article_attachments/36909975972759)

**Arquivo Seguro Desemprego**

![Imagem 10: Arquivo Seguro Desemprego](https://ajuda.sankhya.com.br/hc/article_attachments/36909974736279)
