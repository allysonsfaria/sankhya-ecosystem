---
id: "9799996460183"
titulo: "Operação Bloqueada A empresa da viagem não consegue emitir esse documento por estar configurada com ambiente produção em uma base de teste"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9799996460183-Opera%C3%A7%C3%A3o-Bloqueada-A-empresa-da-viagem-n%C3%A3o-consegue-emitir-esse-documento-por-estar-configurada-com-ambiente-produ%C3%A7%C3%A3o-em-uma-base-de-teste"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:06:06Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Produção", "CORE_E05565", "Bloqueio de Operação por Configuração Incorreta da Base", "Erro", "Base de Dados"]
---

# Operação Bloqueada A empresa da viagem não consegue emitir esse documento por estar configurada com ambiente produção em uma base de teste

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19480724557591) MENSAGEM:**

[CORE\_E05565] Operação Bloqueada: A empresa da viagem não consegue emitir esse documento por estar configurada com ambiente produção em uma base de teste. Avise o administrador para que o mesmo ajuste o registro da base na tela de Administração do servidor.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19480711594775) SITUAÇÃO:**

Ao gerar o lote das notas a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19480711596951) CAUSA:**

Quando a base está registrada como teste incorretamente.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19480724574231) SOLUÇÃO:**

Acesse a tela **Administração do Servidor** (Caminho de acesso à tela: Configurações » Avançado » Administração do Servidor), vá até aba 'Registro de Base de Dados' e verifique se a base está registrada como "Teste", sendo assim, é necessário que seja alterada para "Produção"

![Imagem 5: Acesse a tela Administração do Servidor (Caminho de acesso à tela: Configurações » Avançado » Administração do…](https://ajuda.sankhya.com.br/hc/article_attachments/19480711610647)

[GIF animado: Imagem 6: Cuidado ao alterar o tipo da base pois cada tipo tem suas restrições.](https://ajuda.sankhya.com.br/hc/article_attachments/9799994226967)

Cuidado ao alterar o tipo da base pois cada tipo tem suas restrições.
