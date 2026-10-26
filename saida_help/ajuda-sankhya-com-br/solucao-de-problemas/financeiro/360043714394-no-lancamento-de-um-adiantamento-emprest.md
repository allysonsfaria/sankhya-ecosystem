---
id: "360043714394"
titulo: "No lançamento de um Adiantamento/Empréstimo, o código do parceiro é alterado ao Concluir"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043714394-No-lan%C3%A7amento-de-um-Adiantamento-Empr%C3%A9stimo-o-c%C3%B3digo-do-parceiro-%C3%A9-alterado-ao-Concluir"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:32Z"
rotulos: ["#validadoElisangela", "Configuração", "Parceiro", "Preferências", "Financeiro", "Adiantamento/Empréstimo", "Código do parceiro alterado ao concluir", "Ajuste parâmetro \"CODPARCFUNCS\" para 0", "Parametrização depende do uso de parceiro coringa"]
---

# No lançamento de um Adiantamento/Empréstimo, o código do parceiro é alterado ao Concluir

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17285691809943) SITUAÇÃO:**

No lançamento de um Adiantamento/Empréstimo, o código do parceiro é alterado ao Concluir.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17285649014679) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/17285649020439) Acesse: Configurações » Avançado » Preferências

**"CODPARCFUNCS-Parceiro p/empréstimo p/Funcionários":** altere para 0 (zero)

Esse comportamento ocorre sempre que o parâmetro: CODPARCFUNCS - Parceiro p/empréstimo p/Funcionários estiver configurado com um valor diferente de 0 (zero).

Pois, no momento da inclusão do Adiantamento/Empréstimo será mantido o Código do Parceiro que estiver informado no parâmetro mencionado acima.

![Imagem 4: Acesse: Configurações » Rotinas » Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/article_attachments/17285649027863) Acesse: Configurações » Rotinas » Adiantamento/Empréstimo

Após o ajuste no parâmetro, acesse novamente a rotina e efetue o lançamento do Adiantamento/Empréstimo.

**![Imagem 5: NOTA:](https://ajuda.sankhya.com.br/hc/article_attachments/17285649035799) NOTA:**

Fica a critério da empresa a alteração do parâmetro. Pois, caso o Departamento Pessoal utilize um Parceiro **'coringa'** para Adiantamento/Empréstimo para Funcionário, o parâmetro precisa estar com o código do Parceiro coringa.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17285649045143) CAUSA:**

Ocorre quando há um valor diferente de 0 (zero) no parâmetro CODPARCFUNCS.
