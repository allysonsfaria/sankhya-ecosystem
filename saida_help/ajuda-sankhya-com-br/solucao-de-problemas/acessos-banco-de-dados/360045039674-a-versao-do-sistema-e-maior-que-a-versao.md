---
id: "360045039674"
titulo: "A versão do sistema é maior que a versão do banco de dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045039674-A-vers%C3%A3o-do-sistema-%C3%A9-maior-que-a-vers%C3%A3o-do-banco-de-dados"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T15:33:16Z"
rotulos: ["Produtos", "Configuração", "Atualização", "Sankhya-W", "Atualização Versão Banco de Dados", "Erro"]
---

# A versão do sistema é maior que a versão do banco de dados

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18606682468759) MENSAGEM:**

A versão do sistema é maior que a versão do banco de dados.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18606666259735) CAUSA:**

Mensagem apresentada quando utilizado um executável com versão superior a versão do banco de dados.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18606682485143) SOLUÇÃO:**

Analise a versão do banco e versão do executável utilizadas:

Ajuda >> Autoria:

![Imagem 4: Ajuda >> Autoria:](https://ajuda.sankhya.com.br/hc/article_attachments/18606682492439)

Note, no exemplo acima, que a versão é superior a versão atual do banco de dados. Nesse caso, o banco de dados deverá ser atualizado, para que o respectivo executável possa ser utilizado sem erros. Para tal, solicite apoio ao profissional de T.I/banco de dados da empresa.

**Informações Importantes:**

Caso trabalhe com MGE/G1 e Jiva/Sankhya-W, você NÃO deve executar scripts de banco separadamente usando o "SnkScript". Deve ser executado exclusivamente através dos pacotes de atualizações do Sankhya-W. O "SnkScript" deve executar scripts de banco para clientes que usam APENAS o MGE/G1.

Para mais detalhes sobre a atualização via WPM verifique o artigo:

Produto Sankhya: [Melhores práticas para configuração e atualização agendada via WPM.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580074)
