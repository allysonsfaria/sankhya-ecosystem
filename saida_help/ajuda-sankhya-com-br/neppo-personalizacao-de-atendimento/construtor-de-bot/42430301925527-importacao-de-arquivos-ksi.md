---
id: "42430301925527"
titulo: "Importação de Arquivos -KSI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430301925527-Importa%C3%A7%C3%A3o-de-Arquivos-KSI"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:02:45Z"
rotulos: ["sync_hc", "neppo", "neppo_857997390", "sync_hash_92fb5db4085e"]
---

# Importação de Arquivos -KSI

## Visão Geral

Este documento tem como finalidade orientar a utilização da funcionalidade NEPPO Vault para fins de importação de arquivos do KSI.

A atualização dos arquivos será realizada diariamente às 22:00, de forma automatizada uma vez cadastrado o arquivo XML corretamente. Toda configuração é feita uma única vez e só precisa ser alterada em caso de atualização do arquivo xml por algum motivo especifico.

## Usabilidade

Para cadastrar o arquivo XML, o usuário deverá acessar a funcionalidade disponibilizada NEPPO Vault.

![Imagem 1: Para cadastrar o arquivo XML, o usuário deverá acessar a funcionalidade disponibilizada NEPPO Vault.](https://ajuda.sankhya.com.br/hc/article_attachments/42637712932759)

Após acessada a funcionalidade, o usuário precisará criar um diretório. Para isso, deverá acionar o botão "Criar diretório", que exibirá uma nova linha.

![Imagem 2: Após acessada a funcionalidade, o usuário precisará criar um diretório. Para isso, deverá acionar o botão "Criar…](https://ajuda.sankhya.com.br/hc/article_attachments/42637681891991)

Na linha exibida, o usuário deverá informar a nomenclatura padrão definida “imobiliarias” em minúsculo e no plural, e acionar o botão “salvar”.

Caso o diretório seja criado com outra nomenclatura, não será reconhecido e acarretará na não atualização do arquivo no bot.

![Imagem 3: Caso o diretório seja criado com outra nomenclatura, não será reconhecido e acarretará na não atualização do arquivo no…](https://ajuda.sankhya.com.br/hc/article_attachments/42637682159639)

Após criar o diretório, o usuário deverá acionar o ícone "Novo item", onde será exibido uma interface para preenchimento dos dados de Nome, Descrição, Formato e Valor.

![Imagem 4: Após criar o diretório, o usuário deverá acionar o ícone "Novo item", onde será exibido uma interface para…](https://ajuda.sankhya.com.br/hc/article_attachments/42637657084567)

No campo “Nome” usuário deverá informar o nome padrão definido "ksi" em minúsculo, no campo "Descrição" poderá conter uma descrição livre definida pela usuário, no Campo "Formato" deverá ser selecionada a opção "json" e no campo "Valor" deverá ser informado a URL do arquivo XML.

Regras de formatação:

- Todas as URLs devem estar **entre colchetes** `[]`.
- Cada URL deve ser envolvida por **aspas duplas** `"`.
- Utilize **vírgula** `,` para separar as URLs.
- Exemplo de inserção com apenas 1 URL: [“cliente.com\_xml\_xml\_ksi\_zap\_vrsync\_0\_0\_0.xml"];
- Exemplo de inserção com mais de 1 URL:["cliente.com\_xml\_xml\_ksi\_zap\_vrsync\_0\_0\_0.xml", "cliente.com\_xml\_xml\_ksi\_zap\_vrsync\_0\_0\_0.xml"]

![Imagem 5: Exemplo de inserção com mais de 1 URL:("cliente.com_xml_xml_ksi_zap_vrsync_0_0_0.xml",…](https://ajuda.sankhya.com.br/hc/article_attachments/42637686034199)![Imagem 6: Exemplo de inserção com mais de 1 URL:("cliente.com_xml_xml_ksi_zap_vrsync_0_0_0.xml",…](https://ajuda.sankhya.com.br/hc/article_attachments/42637657854871)

Encerrado o preenchimento, o usuário deverá acionar o botão “Salvar” finalizando o cadastro do arquivo XML.
