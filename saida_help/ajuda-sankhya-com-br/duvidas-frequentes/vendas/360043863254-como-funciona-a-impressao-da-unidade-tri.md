---
id: "360043863254"
titulo: "Como funciona a impressão da 'Unidade Tributável' no DANFE?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863254-Como-funciona-a-impress%C3%A3o-da-Unidade-Tribut%C3%A1vel-no-DANFE"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:40Z"
rotulos: ["Produtos", "Configuração", "Impressão", "XML", "DANFE", "CFOP", "Impressão Unidade Tributável", "Impressão no DANFE", "CFOP define exibição tributável"]
---

# Como funciona a impressão da 'Unidade Tributável' no DANFE?

**(1)** Permitir que o implantador do sistema determine, via parâmetro, de acordo com a CFOP se as informações de unidade tributável, quantidade tributável e valor unitário tributável devem ser impressas no DANFE ou não, quando elas são diferentes dos equivalentes comerciais, é uma funcionalidade criada. Uma vez que apenas nas exportações é necessário apresentar informação de ambos os valores (comercial e tributável).

Para essa funcionalidade, siga as orientações abaixo:

![Imagem 1: Tenha o sistema em versões atuais (release disponibilizado 08/01 em diante), ou baixe um modelo DANFE padrão de um…](https://ajuda.sankhya.com.br/hc/article_attachments/17144321894039) Tenha o sistema em versões atuais (release disponibilizado 08/01 em diante), ou baixe um modelo DANFE padrão de um Sankhya em versões atuais e vincule o mesmo nas preferências da empresa.

![Imagem 2: Para que a funcionalidade tenha efeito, crie um parâmetro com a chave " LSTCFOPEXP" . No caso desse parâmetro, ele não…](https://ajuda.sankhya.com.br/hc/article_attachments/17144321896087) Para que a funcionalidade tenha efeito, crie um parâmetro com a chave **"LSTCFOPEXP"**. No caso desse parâmetro, ele não aparece na tela de preferências até ser criado, então deve ser explicitamente criado clicando-se no botão (+)

Tela: **"Preferências"** (Caminho de acesso: Configurações » Avançado):

![Imagem 3: Tela: " Preferências" (Caminho de acesso: Configurações » Avançado):](https://ajuda.sankhya.com.br/hc/article_attachments/5970461166487)

**![Imagem 4: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17144317164183) IMPORTANTE:**

Com a **inexistência do parâmetro** (ou não preenchimento do mesmo), o relatório se comporta da maneira tradicional, ou seja, caso as tags de unidade, quantidade e valor unitário tributáveis estejam diferentes das comerciais, **ambas as informações são visíveis no relatório.**

(1)** Caso de uso:**

![Imagem 5: Considere o CFOP 5103 como CFOP de exportação, dessa forma, inserido no parâmetro LSTCFOPEXP :](https://ajuda.sankhya.com.br/hc/article_attachments/17144321894039) Considere o CFOP 5103 como CFOP de exportação, dessa forma, inserido no parâmetro LSTCFOPEXP:

![Imagem 6: Considere o CFOP 5103 como CFOP de exportação, dessa forma, inserido no parâmetro LSTCFOPEXP :](https://ajuda.sankhya.com.br/hc/article_attachments/5970485307799)

![Imagem 7: Comportamento de impressão após parametrização do parâmetro (veja que os CFOP'S não inseridos no parâmetro apresentaram…](https://ajuda.sankhya.com.br/hc/article_attachments/17144321896087) Comportamento de impressão após parametrização do parâmetro (veja que os CFOP'S não inseridos no parâmetro apresentaram apenas uma linha de "Unidades", considerando a unidade de tributação do XML):

![Imagem 8: Comportamento de impressão após parametrização do parâmetro (veja que os CFOP'S não inseridos no parâmetro apresentaram…](https://ajuda.sankhya.com.br/hc/article_attachments/360088598793)

![Imagem 9: Comportamento com a inexistência ou não configuração do parâmetro (duas linhas apresentando unidade comercial +…](https://ajuda.sankhya.com.br/hc/article_attachments/17144317165335) Comportamento com a inexistência ou não configuração do parâmetro (duas linhas apresentando unidade comercial + tributável, independente do CFOP).

![Imagem 10: Comportamento com a inexistência ou não configuração do parâmetro (duas linhas apresentando unidade comercial +…](https://ajuda.sankhya.com.br/hc/article_attachments/360088598773)

**![Imagem 11: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17144321900183) OBSERVAÇÃO:**

A unidade de tributação é preenchida no cadastro de produtos, na aba **"Unidades alternativas"**. Para mais informações sobre o cadastro da Unidade Alternativa, acesse: [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas)

**![Imagem 12: ATENÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17144317164183) ATENÇÃO:**

- Se o CFOP informado na nota for o mesmo do CFOP informado no parâmetro, a unidade tributável e a unidade comercial serão apresentadas no DANFE;
- Se o CFOP informado na nota for diferente do CFOP informado no parâmetro, somente a unidade tributável será apresentada no DANFE;
- Para impressão somente da unidade comercial, quando o produto possui unidade tributável diferente da unidade comercial, personalize um modelo de DANFE.
