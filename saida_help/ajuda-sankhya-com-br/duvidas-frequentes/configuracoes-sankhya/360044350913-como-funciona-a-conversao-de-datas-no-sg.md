---
id: "360044350913"
titulo: "Como funciona a Conversão de Datas no SGBD?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044350913-Como-funciona-a-Convers%C3%A3o-de-Datas-no-SGBD"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:02Z"
rotulos: ["#PUBLIFER", "#MANUALT.I", "Configuração", "Oracle", "SQL Server", "Data", "Conversão de Datas em SGBD", "SGBD"]
---

# Como funciona a Conversão de Datas no SGBD?

**(1)** Abaixo serão listados os comandos padrões para conversão de datas.

Lembrando que o Service Desk Sankhya Jiva não presta suporte/treinamento relacionado ao conhecimento em comandos de banco de dados, e qualquer apoio relacionado a esse deverá ser prestado junto ao analista de banco de sua Unidade/Filial.

(2)** SQL SERVER:**

![Imagem 1: "Ano-Mês-Dia Hora:Minuto:Segundo”:](https://ajuda.sankhya.com.br/hc/article_attachments/17155289581335)  "Ano-Mês-Dia Hora:Minuto:Segundo”:

- **SELECT CONVERT(VARCHAR(19), GETDATE(), 120):** Resultado: String, "2018-10-30 12:49:44"
- **SELECT GETDATE():** Resultado: Date, "2018-10-30 12:49:44"

![Imagem 2: “Dia/Mês/Ano”:](https://ajuda.sankhya.com.br/hc/article_attachments/17155306173463) “Dia/Mês/Ano”:

- **SELECT FORMAT(GETDATE(), 'dd/MM/yyyy'):** Resultado: String, "30/10/2018"
- **SELECT CONVERT(VARCHAR, GETDATE(), 103):** Resultado: String, "30/10/2018"

![Imagem 3: “Ano-Mês-Dia”:](https://ajuda.sankhya.com.br/hc/article_attachments/17155306178455) “Ano-Mês-Dia”:

- **SELECT CONVERT(DATE, GETDATE()):** Resultado: Date, "2018-10-30"
- **SELECT CONVERT(VARCHAR, CAST(GETDATE() AS DATE), 120):** Resultado: String, "2018-10-30"

![Imagem 4: “Hora:Minuto:Segundo”.](https://ajuda.sankhya.com.br/hc/article_attachments/17155306181015) “Hora:Minuto:Segundo”.

- **SELECT CONVERT(TIME, GETDATE()):** Resultado: Date, "12:49:44"
- **SELECT FORMAT(GETDATE(), 'hh:mm:ss'):** Resultado: String, "12:49:44"

![Imagem 5: “Dia da Semana, Dia do Mês de Nome do Mês de Ano”.](https://ajuda.sankhya.com.br/hc/article_attachments/17155306185879) “Dia da Semana, Dia do Mês de Nome do Mês de Ano”.

- **SELECT FORMAT(GETDATE(), 'D', 'pt-BR'):** Resultado: String, "terça-feira, 30 de outubro de 2018"

(2)** ORACLE:**

![Imagem 6: “Ano-Dia-Mês Hora:Minuto:Segundo”:](https://ajuda.sankhya.com.br/hc/article_attachments/17155289581335) “Ano-Dia-Mês Hora:Minuto:Segundo”:

- **SELECT SYSDATE FROM DUAL:** Resultado: Date, "2018-10-30 12:01:08"
- **SELECT TO\_CHAR(SYSDATE, 'yyyy-mm-dd hh24:mi:ss') FROM DUAL:** Resultado: String, "2018-10-30 12:01:08"

![Imagem 7: “Dia/Mês/Ano Hora:Minuto:Segundo”:](https://ajuda.sankhya.com.br/hc/article_attachments/17155306173463) “Dia/Mês/Ano Hora:Minuto:Segundo”:

- **SELECT TO\_CHAR(SYSDATE, 'dd/MM/yyyy hh24:mi:ss') FROM DUAL:** Resultado: String, "30/10/2018 12:01:08"

![Imagem 8: “Dia/Mês/Ano”:](https://ajuda.sankhya.com.br/hc/article_attachments/17155306178455) “Dia/Mês/Ano”:

- **SELECT TO\_CHAR(SYSDATE, 'dd/MM/yyyy') FROM DUAL:** Resultado: String, "30/10/2018"

![Imagem 9: “Hora:Minuto:Segundo”:](https://ajuda.sankhya.com.br/hc/article_attachments/17155306181015) “Hora:Minuto:Segundo”:

- **SELECT TO\_CHAR(SYSDATE, 'hh:mm:ss') FROM DUAL:** Resultado: String, "12:01:08"

![Imagem 10: Hora:Minuto:Segundo.Milésimos”:](https://ajuda.sankhya.com.br/hc/article_attachments/17155306185879) Hora:Minuto:Segundo.Milésimos”:

**SELECT TO\_CHAR(systimestamp, 'HH24:MI:ss.FF') FROM DUAL**

Resultado: String, "12:01:08.658385"

- Para o Oracle é  diferente, para isto, temos a função: NLS\_DATE\_FORMAT.
- NLS\_DATE\_FORMAT especifica o valor default de formatação para usar com os comandos TO\_CHAR e TO\_DATE.
- Por default, o valor deste parâmetro é determinado por outra função, NLS\_TERRITORY.
- Para alteração a formatação deste NLS\_DATE\_FORMAT, rode o seguinte comando:
- **ALTER SESSION SET nls\_date\_format='dd/mm/yyyy hh24:mi:ss';**
- **Observação:** ete comando altera apenas a formação da SUA sessão no SGBD, não irá mudar a formatação padrão do SGBD. Ou seja, apenas o seu TOAD/afins, será afetado.

**(1)** Formatadores Comuns

(2)** SQL Server:**

dd -> número do dia;

MM -> número do mês;

yy -> 2 dígitos do ano (18);

yyyy -> 4 dígitos do ano (2018);

hh -> número da hora, com formato 12hrs;

HH -> número da hora, com formato 24hrs;

mm -> número de minutos;

ss -> número dos segundos;

ff -> número dos milésimos;

(2)** Oracle:**

DD -> número do dia;

MM -> número do mês;

YY -> 2 dígitos do ano (18);

YYYY -> 4 dígitos do ano (2018);

HH -> número da hora, com formato 12hrs;

HH24 -> número da hora, com formato 24hrs;

MI -> número de minutos;

SS -> número dos segundos;

FF -> número dos milésimos;
