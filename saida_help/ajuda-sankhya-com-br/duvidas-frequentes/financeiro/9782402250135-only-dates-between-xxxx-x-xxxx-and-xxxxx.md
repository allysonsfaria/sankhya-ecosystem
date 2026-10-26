---
id: "9782402250135"
titulo: "Only dates between XXXX X, XXXX and XXXXXX XX, XXXX are accepted"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9782402250135-Only-dates-between-XXXX-X-XXXX-and-XXXXXX-XX-XXXX-are-accepted"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-09-21T17:50:22Z"
rotulos: ["Produtos", "Importação", "Estoque", "Financeiro", "FIN_E00123", "Erro de datas incorretas", "Ajustar controle de produto", "Verificar arquivo e datas", "Erro"]
---

# Only dates between XXXX X, XXXX and XXXXXX XX, XXXX are accepted

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16778960841495) MENSAGEM:**

[FIN\_E00123]: Only dates between XXXX X, XXXX and XXXXXX XX, XXXX are accepted.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16778960844439) SITUAÇÃO:**

Ao tentar processar um arquivo de retorno ou importar dados do Coletor a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16778960846871) SOLUÇÃO:**

![Imagem 4: Acesse o "Processamento Arquivo de retorno" (Caminho de acesso: Financeiro » EDI Bancário » Processamento do Arquivo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16778932717335) Acesse o **"Processamento Arquivo de retorno"** (Caminho de acesso: Financeiro » EDI Bancário » Processamento do Arquivo de Retorno), analise o arquivo na posição de datas (por exemplo, data de vencimento de acordo com o manual do banco utilizado) e verifique se essa data está incorreta;

![Imagem 5: Acesse a " Importação de dados do Coletor" (Caminho de acesso: Inventário » Avançado » Importação de Dados Coletor),…](https://ajuda.sankhya.com.br/hc/article_attachments/16778960852887) Acesse a "**Importação de dados do Coletor"** (Caminho de acesso: Inventário » Avançado » Importação de Dados Coletor), analise o arquivo inserido e verifique se ele possui as datas e se a data da contagem informada é uma data válida. Caso as datas estejam corretas verifique, por exemplo, se no arquivo algum produto possui a informação 'E+13' e se, no cadastro desse produto, realmente possui algum tipo de controle;

![Imagem 6: Se o produto não possuir nenhum controle, retire essa informação 'E+13' do arquivo e gere os dados novamente;](https://ajuda.sankhya.com.br/hc/article_attachments/16778960859671) Se o produto não possuir nenhum controle, retire essa informação 'E+13' do arquivo e gere os dados novamente;

![Imagem 7: Caso ocorra em outro arquivo no momento da geração, abra o arquivo e verifique se existe alguma informação além do…](https://ajuda.sankhya.com.br/hc/article_attachments/16778932723863) Caso ocorra em outro arquivo no momento da geração, abra o arquivo e verifique se existe alguma informação além do Código de barras/código do produto e quantidades.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16778932726551) CAUSA:**

Poderá ocorrer por alguma data ou cadastro incorretos.
