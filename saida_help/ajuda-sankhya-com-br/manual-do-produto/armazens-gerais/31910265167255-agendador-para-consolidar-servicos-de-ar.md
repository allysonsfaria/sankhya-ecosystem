---
id: "31910265167255"
titulo: "Agendador para Consolidar Serviços de Armazéns"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31910265167255-Agendador-para-Consolidar-Servi%C3%A7os-de-Armaz%C3%A9ns"
trilha: "Manual do Produto > Suprimentos e Estoque > Armazéns Gerais"
atualizado_em: "2026-07-29T15:06:20Z"
rotulos: ["Configuração", "WMS", "Contrato", "Processamento", "Agendamento", "Agendador", "Sistema de armazéns", "Armazéns", "Armazéns Gerais"]
---

# Agendador para Consolidar Serviços de Armazéns

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313183109655) Módulo: Armazéns Gerais < Rotinas        ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42313189387799) Versão disponível: 4.34
```

Use a funcionalidade do Agendador para customizar e programar a consolidação dos serviços apurados nos contratos de armazenagem em horários específicos para automatizar o processamento dos dados, facilitando a tomada de decisão com informações organizadas e confiáveis.

## Permissões de Acesso

O acesso a esta funcionalidade depende de permissões específicas:

- **Visualizar e configurar o Agendador**
- **Executar o processamento manual** (acesso pela tela "Apuração/Processamento de Contratos" > botão Processar Serviços)

![Imagem 3: Executar o processamento manual (acesso pela tela "Apuração/Processamento de Contratos" > botão Processar Serviços )](https://ajuda.sankhya.com.br/hc/article_attachments/31956550332567)

Caso não visualize alguma das opções acima, entre em contato com o administrador do sistema para verificar suas permissões.

## Configurações

**Aba Horários**

Defina os horários em que a consolidação deve ser executada automaticamente.

![Imagem 4: Defina os horários em que a consolidação deve ser executada automaticamente.](https://ajuda.sankhya.com.br/hc/article_attachments/31915468505495)

**Aba Frequência de Agendamento**

Escolha os dias da semana ou periodicidade (diária, semanal etc.) em que a consolidação será realizada.

![Imagem 5: Escolha os dias da semana ou periodicidade (diária, semanal etc.) em que a consolidação será realizada.](https://ajuda.sankhya.com.br/hc/article_attachments/31915446987671)

**Aba Filtros**

Configure os critérios de seleção dos contratos e tipos de serviços que serão consolidados.

![Imagem 6: Configure os critérios de seleção dos contratos e tipos de serviços que serão consolidados.](https://ajuda.sankhya.com.br/hc/article_attachments/35710430356375)

**Seção Filtros/Parâmetros Obrigatórios**

- **Empresa:** Selecione uma empresa.
- **Parceiro:** Filtre por um cliente ou parceiro específico.
- **Safra:** Defina a safra a ser considerada na apuração.
- **Produto:** Escolha os produtos para incluir.

A caixa suspensa apresenta os parâmetros disponíveis. Selecione a opção aplicável.

**Seção Tipo de Apuração**

- Escolha Expedição/Recepção (padrão) ou Armazenagem.

**Campo Quantidade de Meses a Retroagir**

- Informe por quantos meses o sistema deve retroceder a partir da data de execução da consolidação para considerar os contratos, com base na data de início registrada em cada contrato.

![b0f3dcd4-a47c-4935-997e-b577ce7c2243](https://ajuda.sankhya.com.br/hc/article_attachments/31930379622167) **IMPORTANTE** Quanto maior o período informado, maior será o tempo de execução do agendador e o impacto na performance do sistema. Você pode criar diferentes agendamentos com filtros distintos, se desejar segmentar o processamento por tipos de serviço ou períodos.

## Consolidação Manual na Tela de Apuração

Para executar a consolidação manualmente:

1. Acesse a tela **Apuração/Faturamento de Contratos**.
2. Realize a consulta com os filtros desejados.
3. Localize o botão **Processar Serviços** após o carregamento dos dados.
4. Clique no botão para consolidar os serviços exibidos na tela.  Esta ação substitui qualquer dado processado anteriormente
5. Visualize a mensagem **"Serviços consolidados com sucesso!"**após a finalização.

![9b9087f0-c329-4e14-b4cf-dd5f134049e0](https://ajuda.sankhya.com.br/hc/article_attachments/31930388842647) O botão só estará visível se a consulta tiver retornado dados.

## Resumo das Funcionalidades

| Funcionalidade | Ação Realizada |
| --- | --- |
| Agendar consolidação automática | Permite configurar horário, frequência e filtros dos contratos a consolidar. |
| Consolidar serviços manualmente | Executa a consolidação com base nos dados da consulta atual. |
| Criação de múltiplos agendamentos | Possibilita configurar diferentes critérios e períodos de consolidação. |
| Feedback do sistema | Exibe mensagem de sucesso após o processamento. |
| Controle de acesso | Garante que apenas usuários autorizados realizem operações críticas. |
