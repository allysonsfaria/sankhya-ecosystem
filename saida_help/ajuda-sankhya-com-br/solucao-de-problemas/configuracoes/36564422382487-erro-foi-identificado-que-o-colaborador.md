---
id: "36564422382487"
titulo: "Erro: Foi identificado que o colaborador indicado está associado a outra empresa. Para continuar, será necessário solicitar à empresa X que remova o acesso anterior"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36564422382487-Erro-Foi-identificado-que-o-colaborador-indicado-est%C3%A1-associado-a-outra-empresa-Para-continuar-ser%C3%A1-necess%C3%A1rio-solicitar-%C3%A0-empresa-X-que-remova-o-acesso-anterior"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-31T00:03:48Z"
rotulos: ["Configuração", "Segurança", "Parceiro", "Sankhya ID", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Administração de Pessoas", "Area do Desenvolvedor", "Artigo atualizado KCS", "Plataforma - KCS", "Desenvolvedor", "area dev"]
---

# Erro: Foi identificado que o colaborador indicado está associado a outra empresa. Para continuar, será necessário solicitar à empresa X que remova o acesso anterior

**MENSAGEM**

"Foi identificado que o colaborador indicado está associado a outra empresa. Para continuar, será necessário solicitar à empresa X que remova o acesso anterior".

**SOLUÇÃO**

A **"**[**Área do Desenvolvedor**](https://areadev.sankhya.com.br/)**"** é o ambiente onde você gerencia soluções, aplicações e tokens de integração. Problemas de acesso podem ocorrer por falta de permissões ou por conflitos de vínculo com múltiplas empresas.

**Caso a empresa que apresente na mensagem não seja a empresa de atuação o usuário precisa acionar essa empresa para solicitar o seu desvinculo onde a mesma deve seguir o mesmo passo descrito abaixo solicitando a desmarcação de seus acessos da área do desenvolvedor para receber as novas marcações da empresa de atuação.**

**IMPORTANTE: Um usuário não pode ser Administrador ou Desenvolvedor da área dev de mais de uma empresa, podendo somente receber a marcação de Desenvolvedor Terceiro em mais de uma empresa.**

**(1)** Acesse o **"Sankhya ID"** através do link: [https://login.sankhya.com.br](https://login.sankhya.com.br/) (Utilize um usuário com perfil de **"Administrador do Place"**).

**(2)** Clique em **"Gestão de acessos"**.

**(3)** Selecione a empresa e clique no ícone do lápis.

**(4)** Localize o usuário utilizando a barra de pesquisa.

**(5)** Clique em **"Editar Permissões"** na empresa desejada.

**(6)** Clique em "**Editar Usuário"**

**(7)** Na opção de **Permissões** utilizando a barra de rolagem localize a opção **"Área do Desenvolvedor"** selecione as permissões desejadas ao usuário. Lembrando que **Um usuário não pode ser Administrador ou Desenvolvedor da área dev de mais de uma empresa, podendo somente receber a marcação de Desenvolvedor Terceiro em mais de uma empresa.**

**(8)**  Realize um novo acesso na **"Área do Desenvolvedor"**.

**CAUSA**

O erro ocorre porque o **"Sankhya ID"** possui limitações para usuários com permissões de **"Administrador"** e/ou **"Desenvolvedor"** em múltiplas empresas simultaneamente na **"Área do Desenvolvedor"**. Caso o usuário possua vínculos ativos em outras organizações, o sistema bloqueia a nova alteração. É necessário desvincular o acesso anterior para prosseguir.
