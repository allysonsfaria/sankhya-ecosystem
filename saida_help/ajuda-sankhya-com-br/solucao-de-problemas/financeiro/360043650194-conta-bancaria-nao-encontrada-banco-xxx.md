---
id: "360043650194"
titulo: "Conta bancária não encontrada. Banco: XXX, Agência: YYYYY, Conta: ZZZZZZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043650194-Conta-banc%C3%A1ria-n%C3%A3o-encontrada-Banco-XXX-Ag%C3%AAncia-YYYYY-Conta-ZZZZZZ"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:01:02Z"
rotulos: ["#criadoRoger", "Configuração", "Contas", "Financeiro", "Conta bancária não encontrada", "Verificar cadastro ativo e correto", "Ajustar posições no layout", "Erro", "EDI Bancário"]
---

# Conta bancária não encontrada. Banco: XXX, Agência: YYYYY, Conta: ZZZZZZ

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16173678375703) MENSAGEM**:

Conta bancária não encontrada. Banco: XXX, Agência: YYYYY, Conta: ZZZZZZ

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16173694635031) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela " Contas " (Caminho de acesso: Configurações » Cadastros » Bancários » Contas ):](https://ajuda.sankhya.com.br/hc/article_attachments/16173694638871) Acesse a tela **"[Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113)"** (Caminho de acesso: Configurações » Cadastros » Bancários » Contas):

- Verifique se a conta utilizada está cadastrada e **"Ativa"**
- Identifique a respectiva Conta Bancária e verifique o número correto da conta cadastrada no sistema, junto com número da agência e Número do Banco. (Campos "**Conta", "Banco" e "Agência bancária"**).
- Para os três campos, principalmente Agência Bancária e Conta verifique se possui 0 (zero) a esquerda ou dígito verificador (o digito do verificador não pode ter o separador 'hífen').

![Imagem 4: Para os três campos, principalmente Agência Bancária e Conta verifique se possui 0 (zero) a esquerda ou dígito…](https://ajuda.sankhya.com.br/hc/article_attachments/14601516564119)

![Imagem 5: Acesse a tela " Configuração Arquivo de Retorno " (Caminho de acesso: Financeiro » EDI Bancário » Configuração Arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/16173678386583) Acesse a tela **"[Configuração Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033)"** (Caminho de acesso: Financeiro » EDI Bancário » Configuração Arquivo de Retorno):

- Identifique o Layout do Retorno Bancário, no **"Detalhe"** do layout veja a posição dos campos Banco, Agência e Conta Bancária. A posição **"Início"** e **"Fim"** de cada campo determina os valores que serão lidos no arquivo de Retorno.

![Imagem 6: Identifique o Layout do Retorno Bancário, no "Detalhe" do layout veja a posição dos campos Banco, Agência e Conta…](https://ajuda.sankhya.com.br/hc/article_attachments/14601471477783)

**(1)** **EXEMPLO¹:**

**Cadastro da conta**
Conta >> 114802
**Agência >> 7939**
Banco >> 341

Ao processar o arquivo de retorno são consideradas as posições de cada campo no layout.
Conta >> 114802
**Agência >> 07939**

O zero a esquerda é um campo informado, então como no sistema não tem o 0 (zero) é preciso diminuir as posições do layout.

**(1)** **EXEMPLO²:**

Ajuste nas posições do Layout:
Agência >> 53 a 57 >> Alteramos para 54 a 57 pegando apenas 7939 para a agência.

É preciso sempre consultar o Manual do Banco, para verificar a correta posição do Layout de Arquivo de Retorno, antes de efetuar qualquer alteração. 

**![Imagem 7: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16173678390935) CAUSA**:

Ocorre quando alguma posição de Agência, Conta e ou Banco está incorreta ou a conta está inativa ou não cadastrada.
