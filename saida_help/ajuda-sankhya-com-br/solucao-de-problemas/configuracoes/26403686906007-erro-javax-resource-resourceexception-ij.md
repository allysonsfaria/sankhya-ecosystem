---
id: "26403686906007"
titulo: "Erro: javax.resource.ResourceException: IJ000453: Unable to get managed connection for java:/MGEDS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26403686906007-Erro-javax-resource-ResourceException-IJ000453-Unable-to-get-managed-connection-for-java-MGEDS"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-18T10:32:52Z"
rotulos: ["Configuração", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "IJ000453: Unable to get managed connection for java:/MGEDS", "Erro: javax.resource.ResourceException", "Erro", "Banco de Dados", "Conexão"]
---

# Erro: javax.resource.ResourceException: IJ000453: Unable to get managed connection for java:/MGEDS

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26403731838615) **MENSAGEM:**

Erro: javax.resource.ResourceException: IJ000453: Unable to get managed connection for java:/MGEDS

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26403686885911)SOLUÇÃO:**

Caso o servidor seja hospedado em nuvem, acione a hospedeira para análise.

Caso o servidor seja local, é necessario atuação de um DBA interno para análise do causador do erro.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26403731850007)CAUSA:**

Esse erro ocorre devido falhas de comunicação com banco de dados. Podendo ser por diversos fatores, como estouro de pools de conexão, falha na rede, erro de compilação de objetos, problema com serviço do Oracle entre outros.
