---
id: "360044109674"
titulo: "O usuário logado não possui permissão para alterar o documento \"X\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109674-O-usu%C3%A1rio-logado-n%C3%A3o-possui-permiss%C3%A3o-para-alterar-o-documento-X"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-24T14:27:34Z"
rotulos: ["#PUBLIFER", "#Revisadoclaudio", "CORE_E02777", "Configuração", "Portal de Compras", "Portal de Vendas", "Controle de Acesso", "Restrições de Acesso para Alteração de Documentos", "Erro"]
---

# O usuário logado não possui permissão para alterar o documento "X"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17564900051479) MENSAGEM:**

[CORE\_E02777] O usuário logado não possui permissão para alterar o documento "X".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17799757536407) SOLUÇÃO:**

Será necessário que o responsável por liberações de acesso na empresa, revise os acessos do usuário logado no momento dessa validação, de forma que a opção "Alterar" esteja liberada para o tipo de movimentado mencionado.

![Imagem 3: Acesse a tela ' Acessos' (Configurações » Controle de Acesso), e de acordo com o Portal e 'Tipo de Movimento' a serem…](https://ajuda.sankhya.com.br/hc/article_attachments/17564900072727) Acesse a tela '**Acessos'** (Configurações » Controle de Acesso), e de acordo com o Portal e 'Tipo de Movimento' a serem utilizados, verifique as liberações abaixo:

**Portal de Vendas:**

- Comercial >> Rotinas >> Portal de vendas >> Pedidos >> **Alterar**
- Comercial >> Rotinas >> Portal de vendas >> Notas >> **Alterar**
- Comercial >> Rotinas >> Portal de vendas >> Devolução >>**Alterar**

**Portal de Compras:**

- Comercial >> Rotinas >> Portal de Compras >> Pedidos >>**Alterar**
- Comercial >> Rotinas >> Portal de vendas >> Notas >> **Alterar**
- Comercial >> Rotinas >> Portal de vendas >> Devolução >> **Alterar**

**Portal de Mov.Internas:**

- Comercial >> Rotinas >>Portal de Mov.Internas >> Devoluções de Requisição >> **Alterar**
- Comercial >> Rotinas >> Portal de Mov.Internas >> Pedidos de Requisição >> **Alterar**
- Comercial >> Rotinas >> Portal de Mov.Internas >> Requisições >> **Alterar**
- Comercial >> Rotinas >> Portal de Mov.Internas >> Transferências >> **Alterar**

![Imagem 4: Realizadas as liberações acima, conforme necessidade do usuário, faça um novo teste.](https://ajuda.sankhya.com.br/hc/article_attachments/17564900085143) Realizadas as liberações acima, conforme necessidade do usuário, faça um novo teste.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17564900109591) CAUSA:**

Ocorre ao tentar alterar documentos referente determinado tipo de movimento, quando o usuário logado não possuir os acessos de alteração necessários.

**![Imagem 6: Ocorre ao tentar alterar documentos referente determinado tipo de movimento, quando o usuário logado não possuir os…](https://ajuda.sankhya.com.br/hc/article_attachments/17564900134423) OBSERVAÇÃO:**

Nas Centrais de Notas, a alteração só será considerada após a confirmação do lançamento em questão (STATUSNOTA = 'L').
