---
id: "360043725114"
titulo: "Configurar controle de acesso para NFC-e no Fast Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043725114-Configurar-controle-de-acesso-para-NFC-e-no-Fast-Service"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:59:57Z"
rotulos: ["Configuração", "Segurança", "Fast Service", "SEFAZ", "NFC-e", "Controle de Acesso", "Configurações para controle de acessos", "Restrições como consulta e exclusão de NFC-e", "Controle de acesso NFC-e no Fast Service"]
---

# Configurar controle de acesso para NFC-e no Fast Service

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16197375937815) SITUAÇÃO:**

Como gerenciar o controle de acessos de seus usuários caixas na emissão de NFC-e. 

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16197375938839) SOLUÇÃO:**

Veja abaixo, as configurações necessárias para controlar Cancelamento, Inutilização, Consulta de NFC-e's pendentes e outras. 

![Imagem 3: Acesse: FastService » Menu » Arquivos » Controle de Acesso » Usuários , b otão "Acessos".](https://ajuda.sankhya.com.br/hc/article_attachments/16197390305943) Acesse: FastService » Menu » Arquivos » Controle de Acesso » Usuários, botão **"Acessos".**

Para inibir que seus usuários caixas possam fazer a Consulta de NFC-e de modo geral, este controle é feito no Controle de Acessos do usuário.

![Imagem 4: Acesse: FastService » Menu » Arquivos » Controle de Acesso » Usuários , a ba Segurança.](https://ajuda.sankhya.com.br/hc/article_attachments/16197390307607) Acesse: FastService » Menu » Arquivos » Controle de Acesso » Usuários, aba **Segurança.**

Para permitir se seu usuário pode visualizar apenas suas NFC-e's emitidas ou não, o controle também é feito no Controle de Acessos, na marcação: **"Ver apenas pedidos/notas incluídos pelo próprio usuário".**

Com esta marcação, o usuário verá apenas suas notas na tela de "**Consultas NFC-e"** (Caminho de acesso: FastService » Menu » Avançado » Consulta NFC-e).

![Imagem 5: FastService » Menu » Avançado » Preferencias » Todas as preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16197390311831) FastService » Menu » Avançado » Preferencias » Todas as preferências

Para bloquear seus usuários de excluir NFC-e's, solicitando a senha do gerente, marque a opção: **"Validar cancelamento de Cupom"** aba **Parâmetros de Telas**

**![Imagem 6: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16197375946007) OBSERVAÇÕES:**

**(2)** Vale reforçar que a Exclusão de NFC-e só é possível para os cupons que ainda não foram enviados a SEFAZ. Caso já esteja enviado para a SEFAZ, cancele o cupom.

**(2)** A tela é chamada tanto com Botão Direito na tela (Excluir NFC-e (CTRL+U) ), tanto quanto em SAIR da tela no meio do processo de venda. 

![Imagem 7: Para inibir seus usuários de inutilizarem numeração de notas, temos a marcação "Inibe acesso a Cancelam./Inutiliz. de…](https://ajuda.sankhya.com.br/hc/article_attachments/16197390323863) Para inibir seus usuários de inutilizarem numeração de notas, temos a marcação **"Inibe acesso a Cancelam./Inutiliz. de Nota"** em FastService » Menu » Arquivos » Controle de Acesso » Usuários, aba: Segurança.

Com esta marcação favorável a inibição ao usuário a inutilização, será apresentado.

![Imagem 8: Acesse FastService » Menu » Avançado » Preferencias » Todas as preferencias . Valide cancelamento de Cupom, na aba:…](https://ajuda.sankhya.com.br/hc/article_attachments/16197375954071) Acesse FastService » Menu » Avançado » Preferencias » Todas as preferencias. Valide cancelamento de Cupom, na aba: Parâmetros de Telas.

Para validar o cancelamento de NFC-e (Aprovada) e solicitar a senha do gerente, a marcação é a mesma da feita no item 3.
