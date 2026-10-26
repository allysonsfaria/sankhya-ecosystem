---
id: "38776343427095"
titulo: "Atualização de Nomenclatura e Padronização de Datas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38776343427095-Atualiza%C3%A7%C3%A3o-de-Nomenclatura-e-Padroniza%C3%A7%C3%A3o-de-Datas"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:01:14Z"
rotulos: ["Configuração", "Atualização", "Data de Emissão", "Portal Follow Up", "Alteração na Nomeclatura", "Nomeclatura e Padronização de Datas", "Data de Entrada do Pedido de Compra", "Data de Emissão do Pedido", "Nomenclatura", "Datas"]
---

# Atualização de Nomenclatura e Padronização de Datas

Este documento orienta o usuário sobre as **atualizações visuais e funcionais** no **Portal Follow Up**. O ajuste visa alinhar a **nomenclatura dos campos aos dados reais do sistema**, eliminando divergências na análise de pedidos.

**1. Alteração da Nomenclatura**

Para garantir que o **nome do campo reflita exatamente a sua finalidade**, foi realizada a seguinte substituição na interface do portal:

- **Nomenclatura Antiga**: Data de Emissão do Pedido
- **Nomenclatura Atualizada**: Data de Entrada do Pedido de Compra

##### 2. Padronização da Informação

Anteriormente, o campo **"Data de Emissão"** apresentava divergências, **uma vez que o dado esperado correspondia à data de registro da entrada**. Com a atualização, o campo passa a operar sob as seguintes diretrizes:

- **Vínculo Automático:** A informação é extraída diretamente do campo **"Dt Entrada/Saída"** do Pedido de Compra.
- **Integridade do Dado:** O campo no **Portal Follow Up** é bloqueado para edição manual, garantindo que a informação seja idêntica ao registro original do sistema de origem.

##### 3. Tabela de Referência

| Item | Descrição Anterior | Nova Configuração |
| --- | --- | --- |
| **Nome do Campo** | Data de Emissão do Pedido | **Data de Entrada do Pedido de Compra** |
| **Função** | Preenchimento manual/inconsistente | **Leitura automática (Integrada)** |
| **Origem do Dado** | Variável | **Campo: Dt Entrada/Saída** |
| **Edição** | Permitida | **Bloqueada (Somente Leitura)** |
