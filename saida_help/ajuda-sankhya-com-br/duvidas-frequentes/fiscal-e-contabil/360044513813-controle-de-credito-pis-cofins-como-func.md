---
id: "360044513813"
titulo: "Controle de Crédito PIS/COFINS - Como funciona?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044513813-Controle-de-Cr%C3%A9dito-PIS-COFINS-Como-funciona"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:10Z"
rotulos: ["#PUBLIFER", "#revisadojunior", "Configuração", "Crédito", "Impostos", "Financeiro", "EFD Contribuições", "Marcação no EFD-Contribuições", "Processo de Compensação", "Controle de Créditos PIS/COFINS", "PIS/COFINS"]
---

# Controle de Crédito PIS/COFINS - Como funciona?

**(1)** A tela **"Controle de Créditos PIS/COFINS"** é utilizada para demonstrar os saldos de créditos de PIS e COFINS por períodos de apuração (mês a mês) e os respectivos débitos descontados, compensados ou ressarcidos, apresentando os saldos de períodos anteriores e os apurados no próprio período da escrituração.

![Imagem 1: Na tela "EFD - Contribuições" (Livros Fiscais » Conexão » EFD - Contribuições) foi criada a marcação: "Compensar…](https://ajuda.sankhya.com.br/hc/article_attachments/17005298484631) Na tela **"EFD - Contribuições"** (Livros Fiscais » Conexão » EFD - Contribuições) foi criada a marcação: **"Compensar Crédito Registro 1100/1500?"**.

![Imagem 2: O processo de compensação de créditos irá ocorrer à partir da importação do arquivo gerado no EFD-Contribuições…](https://ajuda.sankhya.com.br/hc/article_attachments/17005328846743) O processo de compensação de créditos irá ocorrer à partir da importação do arquivo gerado no EFD-Contribuições contendo **Créditos** ou **Débitos** calculados.

![Imagem 3: Primeiramente, o usuário deverá gerar o SPED-Contribuições com a opção Compensar Crédito - Registro 1100/1500…](https://ajuda.sankhya.com.br/hc/article_attachments/17005298493079) Primeiramente, o usuário deverá gerar o SPED-Contribuições com a opção Compensar Crédito - Registro 1100/1500 desmarcada e, posteriormente, enviar e validar o arquivo no 'PVA - SpedContribuições.'

![Imagem 4: Ainda no PVA, o usuário deverá exportar o 'SPED' validado para um caminho qualquer.](https://ajuda.sankhya.com.br/hc/article_attachments/17005298496535) Ainda no PVA, o usuário deverá exportar o 'SPED' validado para um caminho qualquer.

![Imagem 5: Na Tela EFD - Contribuições deve-se marcar o checkBox 'Compensar Crédito - Registro 1100/1500' e importar o arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/17005298503447) Na Tela EFD - Contribuições deve-se marcar o checkBox **'Compensar Crédito - Registro 1100/1500'** e importar o arquivo validado para o Campo **"Arquivo exportado pelo PVA"**.

![Imagem 6: Após a importação fazer nova geração do SPED:](https://ajuda.sankhya.com.br/hc/article_attachments/17005328935703) Após a importação fazer nova geração do SPED:

- Se o arquivo conter mais **créditos** do que **débitos**, a tela Controle de Créditos PIS/COFINS é preenchida automaticamente.
- Se o arquivo conter mais **débitos** do que **créditos**, os créditos disponíveis de meses anteriores serão utilizados.
- Se o arquivo conter mais **débitos** do que **créditos** e não houver crédito disponível, nada acontece.
