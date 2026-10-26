---
id: "29768374469143"
titulo: "Gerar Data Previsão de Entrega - CALLCENTER"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29768374469143-Gerar-Data-Previs%C3%A3o-de-Entrega-CALLCENTER"
trilha: "Sankhya Official Pack - SOP > TMS"
atualizado_em: "2026-07-22T14:36:52Z"
rotulos: ["CT-e", "Configuração", "Transporte", "Lead Time", "NFS-e", "Gerar Data Previsão de Entrega - CALLCENTER", "Call Center"]
---

# Gerar Data Previsão de Entrega - CALLCENTER

Veja neste artigo como **levar para a tela Call Center a data previsão de entrega calculado pelo lead time.**

Vale destacar que nesse **processo é esperado que o cálculo da data prevista de entrega do lead time seja abrangente e considere todas as etapas do processo**, incluindo as interações realizadas na tela do call center

Para execução desse processo são necessárias algumas **precondições**:

**(1)** **Campo "Calcular Dt. Previsão Entrega Frete Distribuição:"** na tela Configurações TMS, tem que estar igual a 'S'

**(1)** Configurar a tela **"Tabela de frete distribuição"**, seção leadtime (Caminho: Pedido configurado > aba roteiro)

**(1)** A TOP configurada no pedido tem que estar com a marcação **"Gera Call Center na Confirmação"** para ser gerado a ordem na tela Call center.

**(1)** Precisa Criar a ordem de carregamento, será levado para tela de viagem, configurar a viagem e gerar o CT-e/NFS-e.

**(1)**Caso o cliente não use o sábado como dia útil, o parâmetro **"FOLGASAB"** precisa estar ligado, para que o cálculo do sistema referente aos dias fique correto

Por fim, **para realizar o processo siga os passos abaixo:**

![Imagem 1: Configure o campo Calcular Dt. Previsão Entrega Frete Distribuição = S na tela "Configuraçoes TMS", aba "Geral";](https://ajuda.sankhya.com.br/hc/article_attachments/29768374442775) Configure o campo Calcular Dt. Previsão Entrega Frete Distribuição = S na tela **"Configuraçoes TMS",** aba **"Geral";**

![Imagem 2: Configure na tela "Tabela de frete Distribuição" os campos "Dias previsão de entrega" , "Dias para expedição" e marque…](https://ajuda.sankhya.com.br/hc/article_attachments/29768374444823) Configure na tela **"Tabela de frete Distribuição"** os campos **"Dias previsão de entrega"**, **"Dias para expedição"** e marque a opção **"Dias corridos";**

![Imagem 3: Configure a ordem de carregamento, selecionando o botão "Gerar viagem". Assim, no momento de gerar viagem será…](https://ajuda.sankhya.com.br/hc/article_attachments/29768374446103) Configure a ordem de carregamento, selecionando o botão **"Gerar viagem".** Assim, no momento de gerar viagem será calculada uma data com base na tabela. Dessa forma será levada a data prevista de entrega para a tela **"Viagem";**

![Imagem 4: Configure a ordem de carregamento, selecionando o botão "Gerar viagem". Assim, no momento de gerar viagem será…](https://ajuda.sankhya.com.br/hc/article_attachments/29768407321495)

![Imagem 5: Configure a ordem de carregamento, selecionando o botão "Gerar viagem". Assim, no momento de gerar viagem será…](https://ajuda.sankhya.com.br/hc/article_attachments/29768407326231)

![Imagem 6: Na tela viagem valide se na aba Geral o campo Data Previsão chegada foi preenchido;](https://ajuda.sankhya.com.br/hc/article_attachments/29768407328023) Na tela viagem valide se na aba Geral o campo Data Previsão chegada foi preenchido;

![Imagem 7: Abra o CT-e gerado na central de vendas e certifique-se de que o campo Previsão de entrega foi preechido…](https://ajuda.sankhya.com.br/hc/article_attachments/29768374452631) Abra o CT-e gerado na central de vendas e certifique-se de que o campo Previsão de entrega foi preechido automaticamente;

![Imagem 8: Abra o CT-e gerado na central de vendas e certifique-se de que o campo Previsão de entrega foi preechido…](https://ajuda.sankhya.com.br/hc/article_attachments/29768407331351)

![Imagem 9: Confirme o CT-e para que seja gerado uma ordem no "Call Center";](https://ajuda.sankhya.com.br/hc/article_attachments/29768407333143) Confirme o CT-e para que seja gerado uma ordem no **"Call Center";**

![Imagem 10: Na tela Call Center o campo Data Previsão de Entrega será preenchido automaticamente.](https://ajuda.sankhya.com.br/hc/article_attachments/29768407334551)  Na tela Call Center o campo Data Previsão de Entrega será preenchido automaticamente.

![Imagem 11: Na tela Call Center o campo Data Previsão de Entrega será preenchido automaticamente.](https://ajuda.sankhya.com.br/hc/article_attachments/29768407335447)
