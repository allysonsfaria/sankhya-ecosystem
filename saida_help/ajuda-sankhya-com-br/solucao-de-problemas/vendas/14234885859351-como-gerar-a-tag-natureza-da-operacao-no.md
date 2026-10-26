---
id: "14234885859351"
titulo: "Como Gerar a TAG Natureza da Operação no JSON para GW Enotas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14234885859351-Como-Gerar-a-TAG-Natureza-da-Opera%C3%A7%C3%A3o-no-JSON-para-GW-Enotas"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:59:03Z"
rotulos: ["Configuração", "TOP", "Natureza", "Prefeituras", "NFS-e", "Ajuste na parametrização", "Código incorreto na NFS-e", "Falha na configuração do JSON"]
---

# Como Gerar a TAG Natureza da Operação no JSON para GW Enotas

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912204293015) SITUAÇÃO:**

Durante emissão de NFS-e, existem prefeituras, que exigem que seja enviado o código 1 - Exigível mesmo no tipo de operação estar informado código 3 - Isenção.

Que é o correto no exemplo abaixo.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912204294295) SOLUÇÃO:**

![Imagem 3: Para a correção, parametrize a TOP, na aba "NFS-e", no campo "Cód. Natureza Oper. ISS (NFS-e)" com o valor correto e…](https://ajuda.sankhya.com.br/hc/article_attachments/16912216629527) Para a correção, parametrize a TOP, na aba **"NFS-e",** no campo **"Cód. Natureza Oper. ISS (NFS-e)"** com o valor correto e desejado conforme imagem abaixo:

![Imagem 4: Para a correção, parametrize a TOP, na aba "NFS-e", no campo "Cód. Natureza Oper. ISS (NFS-e)" com o valor correto e…](https://ajuda.sankhya.com.br/hc/article_attachments/14690078394775)

![Imagem 5: Após isso, verifique na tela "Cidades", buscando pelo município desejado.](https://ajuda.sankhya.com.br/hc/article_attachments/16912204297495) Após isso, verifique na tela **"Cidades",** buscando pelo município desejado.

Na aba NFS-e,  marque o campo **"Gerar Código Natureza Operação ISS no JSON"**.

![Imagem 6: Na aba NFS-e, marque o campo "Gerar Código Natureza Operação ISS no JSON" .](https://ajuda.sankhya.com.br/hc/article_attachments/14690080976151)

![Imagem 7: Para que seja enviado e gerado a TAG EXIGIBILIDADE no JSON. Após as configurações serem realizadas, gere uma nova nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16912216630935) Para que seja enviado e gerado a TAG EXIGIBILIDADE no JSON. Após as configurações serem realizadas, gere uma nova nota.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16912216632087) CAUSA:**

Acontece quando a informação mesmo parametrizada na TOP não é levada para o JSON devido a não marcação do campo no cadastro de cidades.
