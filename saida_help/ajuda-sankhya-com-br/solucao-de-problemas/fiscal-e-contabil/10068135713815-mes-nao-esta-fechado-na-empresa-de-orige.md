---
id: "10068135713815"
titulo: "Mês não está fechado na empresa de origem. Situação na Empresa XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10068135713815-M%C3%AAs-n%C3%A3o-est%C3%A1-fechado-na-empresa-de-origem-Situa%C3%A7%C3%A3o-na-Empresa-XX"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:04:48Z"
rotulos: ["Configuração", "Contabilização", "Preferências", "Financeiro", "CTB_E00058", "Mês não fechado na empresa de origem", "Data de referência menor que data inicial de consolidação", "Ajuste datas de referência nas preferências da empresa", "Erro"]
---

# Mês não está fechado na empresa de origem. Situação na Empresa XX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19258794115479) MENSAGEM:**

[CTB\_E00058] Mês não está fechado na empresa de origem. Situação na Empresa.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19258794121751) SITUAÇÃO:**

Ao tentar realizar a consolidação a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19258765058583) CAUSA:**

Ocorre quando a data de REFERÊNCIA (Preferências da Empresa Contábil) das empresas de origem, está menor que a data inicial do período de consolidação informada na própria tela "Consolidação de Empresas".

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19258765060631) SOLUÇÃO:**

Acesse a tela **Empresa** (Caminho de acesso à tela: Contabilização » Preferências » Empresa), vá até a aba 'Exercício', de todas as empresas configuradas, e verifique se as datas do campo "dt.referencia" estão iguais, pois elas devem ser a mesma data. Caso identifique que as datas estão diferentes, realize os devidos ajustes.

Alinhe também a data do campo REFERÊNCIA, nas preferências da empresa de origem, ela deve ser igual ou superior a data inicial do período de contabilização.

![Imagem 5: Alinhe também a data do campo REFERÊNCIA, nas preferências da empresa de origem, ela deve ser igual ou superior a data…](https://ajuda.sankhya.com.br/hc/article_attachments/19258794134039)
