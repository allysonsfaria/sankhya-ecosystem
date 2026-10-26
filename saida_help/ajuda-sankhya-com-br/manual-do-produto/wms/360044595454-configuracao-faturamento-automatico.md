---
id: "360044595454"
titulo: "Configuração Faturamento Automático"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595454-Configura%C3%A7%C3%A3o-Faturamento-Autom%C3%A1tico"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:13:26Z"
rotulos: ["AJUDA DO SKW", "manual", "br.com.sankhya.mgewms.rot.faturamentoautomaticowms", "Configuração Faturamento Automático manual", "Configuração", "Relatórios", "WMS", "Faturamento", "Log", "Automatização do faturamento de notas", "Configuração de e-mails para relatórios", "Registro de erros no faturamento"]
---

# Configuração Faturamento Automático

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311509414167) Módulo: WMS > Rotinas
```

---

Esta tela permite efetuar o cadastro das empresas cujos pedidos devem ser faturados automaticamente, ou seja, temos o faturamento do pedido e a impressão da nota de forma automática ao final do processo de conferência.

![Imagem 2: Esta tela permite efetuar o cadastro das empresas cujos pedidos devem ser faturados automaticamente, ou seja, temos o…](https://ajuda.sankhya.com.br/hc/article_attachments/360085097014)

Informe no campo **"Série para Faturamento da Nota"** a série que será utilizada para o faturamento automático das notas. Caso o campo **"Série da nota"** se encontre preenchido na nota, este terá prioridade e será empregado no faturamento.

O campo **"Situação da Separação para Faturamento do Pedido"** permite determinar à partir de qual situação no fluxo WMS da separação do pedido, que o mesmo poderá ser faturado.

**Nota:** mesmo que o parâmetro **"Permite faturar antes da conferência de volumes? - FATANTESCONFVOL"** esteja desligado, se o referido campo estiver configurado com a opção **"Aguardando conferência volumes"**, o faturamento ocorrerá antes da conferência dos volumes.

O campo **"Dt. Último Faturamento Automático"** exibe o momento em que foi realizado o último faturamento automático.

O **"Filtro Faturamento Automático"** tem por finalidade flexibilizar a utilização desta tela, não se limitando apenas as Empresas. Assim, pode-se, por exemplo, criar um filtro personalizado por transportadora, ou seja, o faturamento automático da empresa somente ocorrerá com as notas da transportadora em questão.

**Seção E-mail**

A marcação **"Receber Relatório de Notas Faturadas"** determina se a relação das notas que foram faturadas automaticamente, deve ser enviada via e-mail.

Ao acionar a marcação **"Receber Relatório de Pedidos Não Faturados"**, você estará indicando que a relação dos pedidos que não foram faturados automaticamente em decorrência de algum erro, será enviada via e-mail.

O campo **"E-mail"** será preenchido com o endereço de e-mail para recebimento da relação de notas faturadas e ou pedidos não faturados automaticamente, sendo que, você pode informar um ou vários e-mails separados por **";"**.

**Botão Log faturamento automático WMS**

Ao clicar no botão ![Imagem 3: Ao clicar no botão , a tela de "Log faturamento automático WMS" é aberta apresentando a relação das notas pertencentes…](https://ajuda.sankhya.com.br/hc/article_attachments/16840974468887), a tela de **"Log faturamento automático WMS"** é aberta apresentando a relação das notas pertencentes à empresa que geraram algum tipo de erro durante a tentativa de faturamento automático.

O parâmetro **"Quantos dias o log fat auto deve ser mantido? - QTDDIALOGFATAUT"** define a quantidade de dias que os registros apresentados nesta tela devem ser mantidos. O valor padrão é 30 dias.
