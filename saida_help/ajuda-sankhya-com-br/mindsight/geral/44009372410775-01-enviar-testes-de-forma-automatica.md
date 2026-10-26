---
id: "44009372410775"
titulo: "01. Enviar testes de forma automática"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44009372410775-01-Enviar-testes-de-forma-autom%C3%A1tica"
trilha: "Mindsight > Geral"
atualizado_em: "2026-10-05T18:10:57Z"
rotulos: ["sync_hc", "mindsight", "mindsight_200946744092", "sync_hash_87f3e3c6da56"]
---

# 01. Enviar testes de forma automática

Hoje o ATS Mindsight só envia testes automaticamente para os candidatos na etapa de inscrição. Para configurar essa automatização, é necessário seguir os passos abaixo:

1. O usuário deve selecionar o arquétipo que contém os testes que deseja enviar ao criar a vaga:

   - Ao selecionar o arquétipo, o sistema mostra quais são os testes disponíveis:

   ![Imagem 1: Ao selecionar o arquétipo, o sistema mostra quais são os testes disponíveis:](https://ajuda.sankhya.com.br/hc/article_attachments/44009384413079)
2. Na configuração da etapa Inscrição no “Fluxo de etapas”, o usuário pode escolher quais testes quer enviar de forma automática quando o candidato finalizar a inscrição e qual o modelo de e-mail o candidato deve receber:

   - A variável [link\_testes] é obrigatória no corpo do e-mail:

   ![Imagem 2: A variável ( link_testes ) é obrigatória no corpo do e-mail:](https://ajuda.sankhya.com.br/hc/article_attachments/44009338387735)
3. Quando o usuário seleciona para enviar todos os testes na inscrição, eles chegam automaticamente para o candidato da seguinte forma:

   Obs: No conteúdo desse e-mail foi cadastrado apenas a variável com o link dos testes:

![Imagem 3: Quando o usuário seleciona para enviar todos os testes na inscrição, eles chegam automaticamente para o candidato da…](https://ajuda.sankhya.com.br/hc/article_attachments/44009384717591)

## Casos de uso:

- Se o usuário selecionar o template de e-mail, mas não selecionar nenhum teste, o candidato **NÃO** receberá nenhum e-mail, pois o e-mail automático está vinculado aos testes;
- Se o usuário selecionar algum dos testes, mas não selecionar nenhum template, o candidato também **NÃO** receberá nenhum teste, pois não há mensagem cadastrada para o envio.
- É possível alterar o arquétipo, ou seja, a bateria de testes disponíveis para envio, depois da criação da vaga
