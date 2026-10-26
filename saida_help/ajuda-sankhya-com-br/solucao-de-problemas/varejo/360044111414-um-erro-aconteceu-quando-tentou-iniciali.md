---
id: "360044111414"
titulo: "Um erro aconteceu quando tentou inicializar o Borland Database Engine (error $2501)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111414-Um-erro-aconteceu-quando-tentou-inicializar-o-Borland-Database-Engine-error-2501"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-09-22T18:35:06Z"
rotulos: ["Configuração", "Finalize aplicativos BDE e ajuste configurações", "Erro $2501 ao inicializar Borland Database Engine", "Se o BDE não existir peça instalação ao suporte", "Erro", "Database", "BDE", "DELPHI"]
---

# Um erro aconteceu quando tentou inicializar o Borland Database Engine (error $2501)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18664456194327) MENSAGEM:**

Um erro aconteceu quando tentou inicializar o Borland Database Engine (error $2501).

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18664456200471) SITUAÇÃO:**

Ao tentar acessar algum módulo Delphi do sistema, é retornado o erro.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18664479893399) SOLUÇÃO:**

![Imagem 4: Finalize todos os aplicativos que utilizam o BDE. Exemplo: MGe Controle de Produção, MGe Contabilidade, MGe Produção,…](https://ajuda.sankhya.com.br/hc/article_attachments/18664456208407) Finalize todos os aplicativos que utilizam o BDE. Exemplo: MGe Controle de Produção, MGe Contabilidade, MGe Produção, etc.

![Imagem 5: No Menu Iniciar da máquina busque por 'BDE'. Localizado o ícone, clique com botão direito do mouse: Executar como…](https://ajuda.sankhya.com.br/hc/article_attachments/18664479906967) No Menu Iniciar da máquina busque por 'BDE'. Localizado o ícone, clique com botão direito do mouse: Executar como Administrador

![Imagem 6: Aberto o BDE, execute os ajustes abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/18664479912727) Aberto o BDE, execute os ajustes abaixo:

**(1)** Aba: Database

- **BLOB SIZE**: 999 (máximo)
- **BLOBS TO CACHE**: 2048

**(1)** Aba "Configuration" >> [+] Configuration >> [+] System >> [+] INIT

- **SHAREDMEMLOCATION:** 5BDE
- **SHAREDMEMSIZE**: 8196

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/18864461898647) IMPORTANTE:**

Caso o BDE não exista na máquina, será necessário a instalação do mesmo. Esse serviço não é realizado pelo Service Desk Especializado, sendo necessário o direcionamento de um chamado para a Unidade responsável.
