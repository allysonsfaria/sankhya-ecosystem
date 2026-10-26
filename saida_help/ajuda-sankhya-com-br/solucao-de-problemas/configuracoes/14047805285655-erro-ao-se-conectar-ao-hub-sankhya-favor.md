---
id: "14047805285655"
titulo: "Erro ao se conectar ao HUB Sankhya, Favor liberar o endereço 'grupo.sankhya.com.br' porta 443 no seu servidor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14047805285655-Erro-ao-se-conectar-ao-HUB-Sankhya-Favor-liberar-o-endere%C3%A7o-grupo-sankhya-com-br-porta-443-no-seu-servidor"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:59:35Z"
rotulos: ["Configuração", "Segurança", "Sankhya ID", "Conexão com HUB Sankhya: Liberação de Porta e Ajuste de Data", "Erro", "Firewall", "Proxy"]
---

# Erro ao se conectar ao HUB Sankhya, Favor liberar o endereço 'grupo.sankhya.com.br' porta 443 no seu servidor

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16868255594647) MENSAGEM:**

Erro ao se conectar ao HUB Sankhya, Favor liberar o endereço 'grupo.sankhya.com.br' porta 443 no seu servidor!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16868292571031)SOLUÇÃO:**

Verifique as regras de permissões de Firewall/ Proxy no servidor de aplicação e certifique-se de que a porta 443 e endereço 'grupo.sankhya.com.br' esteja liberada.

![Imagem 3: Passos para verificar as regras de permissões de Firewall/ Proxy:](https://ajuda.sankhya.com.br/hc/article_attachments/16868255603991) Passos para verificar as regras de permissões de Firewall/ Proxy:

**(1)** Acesse as configurações do Firewall/ Proxy do servidor;

**(1)** Procure pelas regras de permissões de saída;

**(1)** Certifique-se de que a porta 443 do endereço 'grupo.sankhya.com.br' esteja liberada nas regras de permissões de saída.

Outra solução, é verificar a data e hora do servidor de aplicação em que o serviço Wildfly Sankhya está rodando. É importante que a data e hora do servidor estejam corretas, pois caso contrário, pode ocorrer problemas de autenticação durante a conexão com o HUB Sankhya.

![Imagem 4: Passos para verificar e ajustar a data e hora em ambiente Linux:](https://ajuda.sankhya.com.br/hc/article_attachments/16868292578839) Passos para verificar e ajustar a data e hora em ambiente Linux:

**(1)** Acesse o terminal do servidor;

**(1)** Digite o comando "date" para verificar a data e hora atual;

**(1)** Se a data e hora estiverem incorretas, digite o comando "date -s 'YYYY-MM-DD HH:MM:SS'" para ajustar a data e hora. Substitua 'YYYY-MM-DD HH:MM:SS' pela data e hora corretas;

**(1)** Verifique novamente a data e hora digitando o comando "date" e certifique-se de que a data e hora foram ajustadas corretamente.

![Imagem 5: Passos para verificar e ajustar a data e hora em ambiente Windows:](https://ajuda.sankhya.com.br/hc/article_attachments/16868255608215) Passos para verificar e ajustar a data e hora em ambiente Windows:

**(1)** Clique no botão "Iniciar" e digite "Data e Hora" na barra de pesquisa;

**(1)** Clique em "Alterar data e hora" para abrir as configurações de data e hora;

**(1)** Certifique-se de que a data e hora estejam corretas e ajuste-as, se necessário;

**(1)** Clique em "OK" para salvar as alterações.

![Imagem 6: Depois de seguir esses passos, reinicie o serviço Wildfly Sankhya e tente novamente se conectar ao HUB Sankhya.](https://ajuda.sankhya.com.br/hc/article_attachments/16868292584599) Depois de seguir esses passos, reinicie o serviço Wildfly Sankhya e tente novamente se conectar ao HUB Sankhya.

![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16868292585239) **OBSERVAÇÃO:**

É importante notar que, em alguns casos, o erro também pode ocorrer quando o serviço do HUB da Sankhya está com instabilidade. Nesses casos, a correção do erro não depende das configurações de Firewall/Proxy ou da data e hora do servidor. Caso seguir os passos para verificar e corrigir o erro, mas o problema persistir, é recomendável entrar em contato com o Service Desk da Sankhya para confirmar se o serviço do HUB está funcionando corretamente. Em caso de instabilidade do serviço do HUB, será necessário aguardar a normalização para que a conexão seja restabelecida.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16868292586519)CAUSA:**

O erro ocorre quando a conexão com o HUB Sankhya falha devido à porta 443 e o endereço 'grupo.sankhya.com.br' não estar liberada no servidor;

Data e Hora do Servidor de aplicação incorretas;

Serviço HUB da Sankhya com instabilidade;
