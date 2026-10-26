---
id: "18563646412951"
titulo: "Ao gerar o relatório de Conferencia DARF  0561 no MGE Pessoal os valores de IRRF retido estão divergentes."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18563646412951-Ao-gerar-o-relat%C3%B3rio-de-Conferencia-DARF-0561-no-MGE-Pessoal-os-valores-de-IRRF-retido-est%C3%A3o-divergentes"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-30T19:35:59Z"
rotulos: ["Configuração", "Relatórios", "Impostos", "DARF", "Relatório DARF 0561", "Valores de IRRF", "Configuração do Filtro", "IRRF", "MGE Pessoal"]
---

# Ao gerar o relatório de Conferencia DARF  0561 no MGE Pessoal os valores de IRRF retido estão divergentes.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18563646402583) **MENSAGEM:**

Ao gerar o relatório de Conferencia DARF 0561 no MGE Pessoal os valores de IRRF retido estão divergentes.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18563610259479)CAUSA:**

Filtro das ligações do relatorio esta configurado incorretamente.

**![Imagem 3: SOLUÇÃO: O correto é gerar o relatório da DARF 0561 da referência MM/AAAA e ele os valores retidos de IRRF referente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/18563655147799)SOLUÇÃO:**

O correto é gerar o relatório da DARF 0561 da referência MM/AAAA e ele os valores retidos de IRRF referente ao (período 01/MM/AAAA a 30 ou 31/MM/AAAA).

Para isso o relatório DARF 0561 precisa estar com filtro configurado corretamente.

**Para configurar o Filtro:**

Acessar a rotina:  Relatórios/ Programável para Cálculos/ A Definir / Conferência DARF 0561 relatório vá na aba "Detalhes", selecionar o campo "Valor do evento", clique botão direito e selecione "Manutenção", na lateral direita da tela, onde ficam os detalhes dos campos, incluir a linha BAS.TIPFOLHA = FOL.TIPFOLHA no campo "Ligações" (pode clicar 2x no campo que irá abrir uma caixinha onde fica mais visual para alteração.
 
![Imagem 4: Para configurar o Filtro: Acessar a rotina: Relatórios/ Programável para Cálculos/ A Definir / Conferência DARF 0561…](https://ajuda.sankhya.com.br/hc/article_attachments/18575005270167)
 
Este campo deve ficar da seguinte forma:
 
BAS.CODEMP = FOL.CODEMP
BAS.CODFUNC = FOL.CODFUNC
BAS.REFERENCIA = FOL.REFERENCIA
BAS.TIPFOLHA = FOL.TIPFOLHA
