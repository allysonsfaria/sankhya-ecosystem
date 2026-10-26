---
id: "1500002031022"
titulo: "Base não pode ser registrada como produção, pois ela não possui informações sobre o nó"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002031022-Base-n%C3%A3o-pode-ser-registrada-como-produ%C3%A7%C3%A3o-pois-ela-n%C3%A3o-possui-informa%C3%A7%C3%B5es-sobre-o-n%C3%B3"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:49Z"
rotulos: ["Configuração", "Produção", "#formatadoroger", "OS1491363", "Cadastro", "Problema no Registro da Base de Dados", "Erro", "Base de Dados"]
---

# Base não pode ser registrada como produção, pois ela não possui informações sobre o nó

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16287564863767) MENSAGEM**:

Base não pode ser registrada como produção, pois ela não possui informações sobre o nó.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16287564868887) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Faça o login com usuário SUP;](https://ajuda.sankhya.com.br/hc/article_attachments/16287539075351) Faça o login com usuário SUP;

![Imagem 4: Acesse a tela: Administração do Servidor » Aba 'Registro de base de dados ;](https://ajuda.sankhya.com.br/hc/article_attachments/16287564874007) Acesse a tela: Administração do Servidor » Aba 'Registro de base de dados;

![Imagem 5: Identifique a base registrada como PRODUÇÃO. Caso necessite de ser substituída, proceda com o ajuste, caso não, deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/16287564877079) Identifique a base registrada como PRODUÇÃO. Caso necessite de ser substituída, proceda com o ajuste, caso não, deverá registrar a nova base como Teste, Treinamento.

**![Imagem 6: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16287564881047) CAUSA**:

Ocorre quando o cliente já possui uma base de PRODUÇÃO registrada e o mesmo está tentando registrar uma outra base de Produção. A aplicação só permite o registro de apenas 1 (uma) base de Produção, os restantes podem ser registrados como Teste, Treinamento, quantas bases desejar.
