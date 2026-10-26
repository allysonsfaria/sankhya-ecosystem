---
id: "4409153118359"
titulo: "Funcionários da CIPA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409153118359-Funcion%C3%A1rios-da-CIPA"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:36:02Z"
rotulos: ["Configuração", "Funcionários", "Ocorrências", "não apagar", "#publicadoHyago", "Folha de Pagamento", "Cadastro: Ocorrência estabilidade", "Parâmetro: FPCODHISESTABIL", "Evento: 122 - Indenização", "CIPA", "Estabilidade"]
---

# Funcionários da CIPA

#### Dúvida:

Como faço para cadastrar os funcionários da CIPA na folha de pagamento, pois eles têm estabilidade?

#### Orientação:

**![Imagem 1: Tenha o cadastro da ocorrência:](https://ajuda.sankhya.com.br/hc/article_attachments/15997147595799)  Tenha o cadastro da ocorrência:**

Lançamentos> Histórico do Funcionário> Histórico de ocorrências:

![Imagem 2: Lançamentos> Histórico do Funcionário> Histórico de ocorrências:](https://ajuda.sankhya.com.br/hc/article_attachments/15695647719703)

**![Imagem 3: Acesse: Rotinas > Todas as Preferências > FPCODHISESTABIL](https://ajuda.sankhya.com.br/hc/article_attachments/15997147599255)  Acesse:  Rotinas > Todas as Preferências > FPCODHISESTABIL**

![Imagem 4: Acesse: Rotinas > Todas as Preferências > FPCODHISESTABIL](https://ajuda.sankhya.com.br/hc/article_attachments/4409140333719)

Informe o código de ocorrência no parâmetro, para que caso haja o desligamento do funcionário seja apresentado uma mensagem de aviso informando a estabilidade do funcionário.

**![Imagem 5: Lance a ocorrência no histórico do funcionário:](https://ajuda.sankhya.com.br/hc/article_attachments/15997147605143) Lance a ocorrência no histórico do funcionário:**

Lançamentos> Histórico do Funcionário> Registros de ocorrências

![Imagem 6: Lançamentos> Histórico do Funcionário> Registros de ocorrências](https://ajuda.sankhya.com.br/hc/article_attachments/4409139992599)

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15997147607063) OBSERVAÇÃO:**

- Se lançar no Registro de Ocorrências o período todo de estabilidade conforme print a cima com data inicio e fim, no cadastro do Histórico de ocorrência só precisa marcar a caixinha de 'Gera indenização' Não precisa informar a quantidade de meses, pode deixar 0 ou em branco, pois nesse caso  o sistema vai entender .
- Se informar a quantidade de meses no histórico de ocorrência, deverá lançar a Ocorrência com a data início e fim iguais, pois quando informa a quantidade de meses, o sistema tem o seguinte comportamento ( Data Fim + Quantidade de Meses).

**![Imagem 8: Evento para cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/15997147610135)  Evento para cálculo**

122 - INDENIZACAO QUEBRA ESTABIL

![Imagem 9: 122 - INDENIZACAO QUEBRA ESTABIL](https://ajuda.sankhya.com.br/hc/article_attachments/4409145859863)

![Imagem 10: 122 - INDENIZACAO QUEBRA ESTABIL](https://ajuda.sankhya.com.br/hc/article_attachments/4409145916567)

![Imagem 11: 122 - INDENIZACAO QUEBRA ESTABIL](https://ajuda.sankhya.com.br/hc/article_attachments/4409145954839)

Fórmula Padrão:

(&F1000 \* &MESESESTABILIDADE) + ((&F1000 / 30) \* &DIASFRACAOESTAB)

Variáveis usadas na fórmula:

- **&MESESESTABILIDADE :**  retorna a quantidade de meses completos no período da estabilidade.
- **&DIASFRACAOESTAB:**  é a soma dos dias no mês da rescisão e os dias no mês de encerramento da estabilidade.
