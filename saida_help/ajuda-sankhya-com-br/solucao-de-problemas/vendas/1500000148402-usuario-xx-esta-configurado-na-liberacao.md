---
id: "1500000148402"
titulo: "Usuário XX está configurado na liberação de cascata do evento YY porém não possui configuração de limite de liberação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000148402-Usu%C3%A1rio-XX-est%C3%A1-configurado-na-libera%C3%A7%C3%A3o-de-cascata-do-evento-YY-por%C3%A9m-n%C3%A3o-possui-configura%C3%A7%C3%A3o-de-limite-de-libera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:26:24Z"
rotulos: ["#criadoRoger", "Configuração", "Eventos", "Usuários", "Liberação de Limites", "Usuário zero não pode ser limitado.", "CORE_E05937", "Controle de Acesso", "Usuário sem limite de liberação configurado", "Configure limite de liberação no cadastro do usuário", "Falta de limite para liberação em cascata"]
---

# Usuário XX está configurado na liberação de cascata do evento YY porém não possui configuração de limite de liberação

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16273566433943) MENSAGEM**:

[CORE\_E05937] Usuário XX está configurado na liberação de cascata do evento YY porém não possui configuração de limite de liberação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16273573614103) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o cadastro de Usuários em: Configurações » Controle de Acesso » Usuários](https://ajuda.sankhya.com.br/hc/article_attachments/16273566438679) Acesse o cadastro de Usuários em: Configurações » Controle de Acesso » Usuários

Selecione o usuário, apresentado da mensagem, clique em Outras Opções » Limites para liberação.
Faça a liberação de acordo com o evento configurado em cascata. Veja abaixo como proceder.

[GIF animado: Imagem 4: Selecione o usuário, apresentado da mensagem, clique em Outras Opções » Limites para liberação. Faça a liberação de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000309681)

![Imagem 5: Após os ajustes, poderá concluir a operação novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16273566442903) Após os ajustes, poderá concluir a operação novamente.

(1)** Nota**: O usuário 0 (zero) não pode ser usuário liberador de nenhum evento, ao tentar configurar o sistema apresenta a seguinte mensagem: Usuário zero não pode ser limitado.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16273566447255) CAUSA:**

Ocorre quando o usuário foi selecionado para ser um dos liberadores do evento em Cascata, porém ainda não possui limite de liberação em seu cadastro.
