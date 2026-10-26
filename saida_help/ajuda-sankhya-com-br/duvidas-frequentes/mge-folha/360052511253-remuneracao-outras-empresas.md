---
id: "360052511253"
titulo: "Remuneração outras empresas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052511253-Remunera%C3%A7%C3%A3o-outras-empresas"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:11Z"
rotulos: ["#criadoroger", "Funcionários", "Impostos", "Folha", "eSocial", "Configuração Funcionários", "Configuração de Remuneração de Outras Empresas"]
---

# Remuneração outras empresas

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19582233622935) SOLUÇÃO:**

![Imagem 2: Acesse 'MGEPessoal >> Arquivos' >> Eventos:](https://ajuda.sankhya.com.br/hc/article_attachments/20471291485719) Acesse 'MGEPessoal >> Arquivos' >> Eventos:

1.1 - Evento 505 - BASE INSS OUTRAS FONTES

Este evento será utilizado quando funcionário (independente do vínculo empregatício) tiver outros vínculos, neste evento em específico será  lançado a base de INSS de outros vínculos.

- **Aba Propriedades:**

![Imagem 3: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/1500000524562)

![Imagem 4: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/19582233636119)

![Imagem 5: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/1500000524582)

- **Aba Incidência:**

![Imagem 6: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360089225933)

**Observação:**

Este evento não possui fórmula e também não é enviado ao e-social.

1.2 - Evento 506- INSS Retido Outras Fontes:

Este evento será utilizado quando o funcionário (independente do vínculo empregatício) tiver outros vínculos, neste evento em específico será lançado o valor retido de inss em outra empresa. 

- **Aba Propriedades:**

![Imagem 7: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360084029993)

- **Aba Incidência:**

![Imagem 8: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360088096974)

- **Aba 'Bases de Cálculo':**

![Imagem 9: Aba 'Bases de Cálculo':](https://ajuda.sankhya.com.br/hc/article_attachments/360088097114)

**Observação:**

Este evento não possui fórmula e também não é enviado ao e-social.

![Imagem 10: Acesse Arquivos > Funcionários > aba Remuneração outras empresas:](https://ajuda.sankhya.com.br/hc/article_attachments/19582233643927) Acesse Arquivos > Funcionários > aba **Remuneração outras empresas:**

![Imagem 11: Acesse Arquivos > Funcionários > aba Remuneração outras empresas:](https://ajuda.sankhya.com.br/hc/article_attachments/360082852754)

Nesse campo deve ser selecionado o indicador de desconto INSS, após selecionado deve ser preenchido os dados da grade inferior com CGC/CPF, Cód. Categoria (E-social). E, caso já tenha sido desligado, informar data de desligamento, caso contrário não preencher o campo.

![Imagem 12: Acesse 'Lançamentos' > Movimentação por funcionário:](https://ajuda.sankhya.com.br/hc/article_attachments/19582233652375) Acesse 'Lançamentos' > **Movimentação por funcionário:**

![Imagem 13: Acesse 'Lançamentos' > Movimentação por funcionário:](https://ajuda.sankhya.com.br/hc/article_attachments/360084030313)

- Ao lançar o evento 505-BASE INSS OUTRAS FONTES será apresentado um pop up onde deve ser selecionado a empresa o qual colaborar teve outra remuneração. Após selecionar a empresa e dar ‘ok’ , deverá preencher as demais informações do evento .
- O mesmo processo de lançamento deve ser feito com o evento 506- INSS Retido Outras Fontes, observando que para este evento não será apresentado o pop up.

![Imagem 14: Por fim, basta realizar o cálculo e conferir os valores.](https://ajuda.sankhya.com.br/hc/article_attachments/19582203127703) Por fim, basta realizar o cálculo e conferir os valores.

**2.0-Remuneração outras empresas na Folha de 13°**

Evento: 502-INSS 13º RETIDO OUTRAS FONTES\*

![Imagem 15: Evento: 502-INSS 13º RETIDO OUTRAS FONTES*](https://ajuda.sankhya.com.br/hc/article_attachments/1500000534581)

Evento:503-BAS INSS 13º OUTRAS FONTES\*

![Imagem 16: Evento: 503-BAS INSS 13º OUTRAS FONTES*](https://ajuda.sankhya.com.br/hc/article_attachments/360099406994)

Lançamento > Movimento de 13° Salário![Imagem 17: Lançamento > Movimento de 13° Salário](https://ajuda.sankhya.com.br/hc/article_attachments/360099406974)

**Observação:** O evento deve ser lançado no movimento de 13°.
