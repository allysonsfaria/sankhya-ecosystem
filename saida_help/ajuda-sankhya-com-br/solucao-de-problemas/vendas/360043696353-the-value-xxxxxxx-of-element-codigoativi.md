---
id: "360043696353"
titulo: "The value 'XXXXXXX' of element 'CodigoAtividade' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043696353-The-value-XXXXXXX-of-element-CodigoAtividade-is-not-valid"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:25Z"
rotulos: ["#criadoRoger", "Configuração", "Impostos", "Prefeituras", "NFS-e", "Valor 'XXXXXXX' inválido para 'CodigoAtividade'", "Atualize o Código CNAE na tela \"Serviço\"", "Todos os serviços na nota devem ter o mesmo CNAE", "CNAE"]
---

# The value 'XXXXXXX' of element 'CodigoAtividade' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16454017266583) MENSAGEM:**

cvc-type.3.1.3: The value 'XXXXXXX' of element 'CodigoAtividade' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454017269655) SOLUÇÃO:**

![Imagem 3: Acesse a tela "Serviço " (Caminho de acesso: Configurações » Cadastros » Produtos ) e para os serviços utilizados no…](https://ajuda.sankhya.com.br/hc/article_attachments/16454000189847) Acesse a tela [**"Serviço**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553)" (Caminho de acesso: Configurações » Cadastros » Produtos) e para os serviços utilizados no lançamento, realize as verificações a seguir:

- Aba: "**Imposto"**
- Campo '**CNAE':** informe o Código CNAE do Serviço, de acordo com instruções do CONTADOR.

![Imagem 4: Salve qualquer alteração efetuada nos serviços, redigite o serviço na nota e refaça a geração de lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16454017274519) Salve qualquer alteração efetuada nos serviços, redigite o serviço na nota e refaça a geração de lote.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454000195095) OBSERVAÇÃO:**

Se houver mais de um serviço na nota, ambos devem ter o mesmo CNAE. Dois ou mais CNAE's diferentes em uma nota de serviço não serão aceitos por qualquer prefeitura.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16454000199063) CAUSA:**

Ocorre quando o Código CNAE do Serviço, está incorreto/inválido.
