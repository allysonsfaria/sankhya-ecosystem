---
id: "39370172436375"
titulo: "Como resolver o aviso \"Você não possui acesso para configurar a grade\"?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39370172436375-Como-resolver-o-aviso-Voc%C3%AA-n%C3%A3o-possui-acesso-para-configurar-a-grade"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-01T17:53:15Z"
rotulos: ["Configuração", "Usuários", "Segurança", "Central de Vendas", "Parâmetro", "Artigo criado KCS", "CVE - KCS", "Comercial"]
---

# Como resolver o aviso "Você não possui acesso para configurar a grade"?

Este aviso aparece quando o usuário tenta configurar a grade de uma tela no sistema Sankhya, mas não possui as permissões necessárias. Ele só é exibido quando o parâmetro **UTLCGFACCESSGRD** está habilitado e o usuário não tem a permissão **"Configurar"** na tela. Se o usuário já tem essa permissão e o aviso continua, confira se ela foi dada na tela certa: nas Centrais, o sistema verifica a permissão do Portal correspondente (veja o final deste artigo).

A configuração de acesso às grades permite que administradores controlem quais usuários podem personalizar o layout das telas, garantindo padronização quando necessário ou flexibilidade para usuários específicos.

### Quando este aviso aparece

O aviso **"Você não possui acesso para configurar a grade"** pode aparecer em diversas telas do sistema, incluindo:

- **"Portal de Pedidos"** (Comercial » Pedido Web » Portal de Pedidos) - na edição de registros.
- **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas) - na aba itens, modo formulário.
- **"Portal de Cotação"** (Cotação » Rotinas » Portal de Cotação Online) - na cotação de compras.
- Outras Centrais e Portais do sistema.

### Como habilitar o acesso à configuração de grade

Para permitir que o usuário configure as grades das telas, siga os passos abaixo:

**(1)**  Acesse a tela **"Acessos"** (Configurações » Controle de Acesso » Acessos).
**(2)**  Localize o usuário ou grupo de usuários que precisa ter acesso à configuração de grade.
**(3)**  Selecione a rotina ou módulo específico onde o usuário precisa configurar a grade. Nas Centrais, selecione o Portal correspondente (veja **"Observações importantes sobre centrais e portais"**).
**(4)**  Habilite a opção **"Configurar"** para o usuário ou grupo selecionado.
**(5)**  Acesse a tela de **"Preferências"** (Configurações » Avançado » Preferências).
**(6)**  Localize o parâmetro **"UTLCGFACCESSGRD - Usa permissão de acesso de Configurar para grid"** e confirme que ele está habilitado. É ele que faz o sistema exigir a permissão **"Configurar"** para as grades.
**(7)**  Salve as alterações e oriente o usuário a desconectar e reconectar no sistema para que as permissões sejam aplicadas.

### Como funciona o controle de configuração de grade

Quando o parâmetro **UTLCGFACCESSGRD** está habilitado, o sistema passa a respeitar as permissões configuradas na tela de **"Acessos"**. Isso significa que:

- Usuários com a permissão **"Configurar"** poderão personalizar as grades das telas.
- Usuários sem a permissão visualizarão apenas a configuração padrão definida pelo usuário **"SUP"**.
- Qualquer configuração de grade realizada anteriormente por usuários sem permissão será ignorada, e a configuração do **"SUP"** será carregada.

Com o parâmetro **desabilitado** (padrão do sistema), não há esse controle: todos os usuários podem configurar as grades, com ou sem a permissão **"Configurar"**.

### Configuração padrão pelo usuário SUP

Para garantir que todos os usuários sem permissão de configuração visualizem um layout padronizado, o usuário **"SUP"** deve configurar a grade da forma desejada. Esta configuração servirá como padrão para todos os usuários que não possuem a permissão **"Configurar"**.

**(1)**  Acesse o sistema com o usuário **"SUP"**.
**(2)**  Abra a tela desejada e configure a grade conforme o layout padrão necessário.
**(3)**  Remova a permissão **"Configurar"** dos usuários que devem visualizar apenas o layout padrão.

### Observações importantes sobre centrais e portais

Nas **"Centrais"**, o sistema não verifica a permissão **"Configurar"** da própria Central, e sim a do Portal correspondente. Por isso, habilite a permissão **"Configurar"** na tela do Portal, conforme a correspondência:

- **"Central de Vendas"** → **"Portal de Vendas"**.
- **"Central de Compras"** → **"Portal de Compras"**.
- **"Central de Movimentações Internas"** → **"Portal de Mov. Internas"**.
- **"Central de Produção"** → **"Ordens de Produção"**.

Além disso, há uma configuração diferente para cada **"Tipo de Movimento"**. Quando uma configuração específica não é encontrada pelo sistema, ele utilizará a configuração padrão.
