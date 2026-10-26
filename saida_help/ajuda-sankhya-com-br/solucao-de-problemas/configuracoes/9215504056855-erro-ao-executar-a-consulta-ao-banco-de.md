---
id: "9215504056855"
titulo: "Erro ao executar a consulta ao Banco de Dados para o layout \"XXXX - XXXXX\". Nome de coluna ' ' inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9215504056855-Erro-ao-executar-a-consulta-ao-Banco-de-Dados-para-o-layout-XXXX-XXXXX-Nome-de-coluna-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:25Z"
rotulos: ["Configuração", "Layout", "CORE_E04726", "Erro de Coluna Inválida em Layout de Banco de Dados", "Erro", "Banco de Dados", "Arquivo Remessa"]
---

# Erro ao executar a consulta ao Banco de Dados para o layout "XXXX - XXXXX". Nome de coluna ' ' inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19033208988567) MENSAGEM:**

[CORE\_E04726] Erro ao executar a consulta ao Banco de Dados para o layout "XXXX - XXXXX". Nome de coluna ' ' inválido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033209002903) SITUAÇÃO:**

Ao criar um filtro e inserir uma condição no mesmo a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19033205253399) CAUSA:**

O layout de arquivo de remessa não suporta filtros com campos apelidados.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19033209013271) SOLUÇÃO:**

Não é possível criar um filtro com a query que traz um campo com o nome apelidado, pois isso ocasiona o erro, sendo assim, utilize diretamente o nome do campo da tabela.

Isso já está previsto no manual da tela **Configuração Arquivo Remessa** (Caminho de acesso à tela: Comercial » EDI » Configuração Arquivo Remessa)

**Importante:** Apelidos de colunas não podem ser utilizados na composição das Condições dos campos. Caso um campo seja necessário para definição de filtros, não se deve definir apelidos para o mesmo; o correto a ser feito é a construção do filtro manualmente, através da digitação do nome do campo no Banco de Dados.

**Observação:** A função variavelPorNome(), terá a sua funcionalidade na abaCamposdesta tela, pois tem-se que as querys não interpretam variáveis desenvolvidas para os campos.

[Configuração Arquivo Remessa – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg2ODQyOTA2NTQsInRpY2tldF9pZCI6MjAyMDEyLCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTY1OTE5NDg2Nn0.q9qAi8cYBCkOVPc5uzmBJZxOg3_D5Tun4_9k0Zlc-PY)
