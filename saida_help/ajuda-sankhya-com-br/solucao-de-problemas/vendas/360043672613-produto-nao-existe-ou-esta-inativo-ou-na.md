---
id: "360043672613"
titulo: "Produto não existe ou está inativo ou não pode ser usado aqui"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043672613-Produto-n%C3%A3o-existe-ou-est%C3%A1-inativo-ou-n%C3%A3o-pode-ser-usado-aqui"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:50Z"
rotulos: ["Produtos", "Configuração", "TOP", "Cadastro", "Verifique código ative produto/unidade revise TOP e regras", "Produto inválido ou não acessível", "Código errado produto inativo unidade inativa ou restrição de TOP", "Erro"]
---

# Produto não existe ou está inativo ou não pode ser usado aqui

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16146008850327) MENSAGEM:**

Produto não existe ou está inativo ou não pode ser usado aqui

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16146008855703) SOLUÇÃO:**

De acordo com as possíveis causas da mensagem, listamos os procedimentos para correções:

![Imagem 3: Código informado incorretamente:](https://ajuda.sankhya.com.br/hc/article_attachments/16146008857495) Código informado incorretamente:

- Certifique-se que o código do produto' informado no campo **"Produto"** está correto.

![Imagem 4: Produto INATIVO :](https://ajuda.sankhya.com.br/hc/article_attachments/16146008860311) Produto **INATIVO**:

- Acesse a tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos)  e confirme se o campo **'Ativo**' na aba **"Propriedades"** está marcado para o produto a ser utilizado.
- Em caso negativo, sintonize internamente se essa inativação procede, ou se poderá ser ajustada.

**Unidade Alternativa inativo**

- Acesse o "**[cadastro de Produtos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)** (Caminho de acesso: Configurações » Cadastros » Produtos), aba **"Unidades alternativas"** e verifique se ela está ativa. Caso não esteja, ative a e faça um novo lançamento.

![Imagem 5: TOP com restrição:](https://ajuda.sankhya.com.br/hc/article_attachments/16146008861719) TOP com**restrição:**

Se a situação ocorre em lançamentos através do Portal (Vendas/Compras/Mov.Interna), anote o 'Tipo de Operação (TOP)' que está sendo utilizado e siga com as orientações abaixo:

- Acesse o cadastro de TOP’s (Caminho de acesso: Comercial » Arquivo » Cadastros).
- Acione o botão "**Outras Opções" » "Restrições/Exceções"**.
- Verifique se existem regras vinculadas para "**Produto"**:

![Imagem 6: Verifique se existem regras vinculadas para " Produto" :](https://ajuda.sankhya.com.br/hc/article_attachments/14691396790807)

![Imagem 7: Central de Certificações:](https://ajuda.sankhya.com.br/hc/article_attachments/16146008865047) Central de Certificações:

- Caso a empresa utilize o módulo de 'Central de Certificação', averigue se na tela de "[**Central de Certificações**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053)" (Caminho de acesso: Comercial > Avançado > Certificações > Central de Certificações) exista alguma regra definida para a empresa utilizada e se o usuário da operação está com alguma restrição vinculada em tela "**[Usuários"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874)**(Caminho de acesso: Configurações > Controle de Acesso) Aba: "**Validações".**
- Em caso positivo, sintonize internamente para compreender a necessidade dessa regra no processo da empresa e assim alterar os dados do seu lançamento ou desativar a regra.

**![Imagem 8: OBSERVAÇÃO: O erro pode ocorrer também caso algum processo leve por default o Produto 0 (zero) e este não existe…](https://ajuda.sankhya.com.br/hc/article_attachments/16145989514135) OBSERVAÇÃO:** 
O erro pode ocorrer também caso algum processo leve por default o Produto 0 (zero) e este não existe cadastrado mais na base. Então, se faz necessário intervenção via banco de dados para cadastrar novamente o produto 0 (zero) na base, neste caso pode acionar o Service Desk para apoio no processo.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16146008872599) CAUSA:**

Ocorre quando o produto não está devidamente cadastrado no sistema, com restrições ou inativo.
