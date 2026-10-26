---
id: "39354152833431"
titulo: "Erro no Cálculo de IRRF para Funcionário com Pensão Alimentícia"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39354152833431-Erro-no-C%C3%A1lculo-de-IRRF-para-Funcion%C3%A1rio-com-Pens%C3%A3o-Aliment%C3%ADcia"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:58Z"
rotulos: ["Configuração", "Eventos", "Impostos", "Folha de Pagamento", "Pensão Alimentícia", "IRRF", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no Cálculo de IRRF para Funcionário com Pensão Alimentícia

**Mensagem**

O sistema está calculando o **"IRRF"** de forma incorreta para funcionários que possuem desconto de **"Pensão Alimentícia"**, não deduzindo o valor da pensão da base de cálculo do imposto ou aplicando a dedução de forma inadequada.

**Situação**

Ao processar a **"Folha de Pagamento Mensal"** (Pessoal+ » Rotinas Folha » Cálculos), o cálculo do **"IRRF"** não está considerando corretamente o desconto de **"Pensão Alimentícia"** como dedução da base de cálculo. O valor do imposto retido está sendo calculado sobre a remuneração total, sem a devida dedução da pensão, resultando em um desconto de imposto maior do que o devido.

**Solução**

Para corrigir o cálculo do **"IRRF"** considerando a pensão alimentícia, siga os passos abaixo:

**(1)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento de **Pensão Alimentícia** cadastrado no sistema.
**(2)** Verifique se o evento possui a **Identificação** correta vinculada, responsável por reconhecer o valor como dedução da base de **IRRF**. A identificação **166** (no caso de evento de pensão para folha mensal) deve estar configurada para que a pensão seja considerada dedutível.
**(3)** Confira se a base de **IRRF** está devidamente vinculada ao evento de pensão, na aba **"Bases de Cálculo"**.
**(4)** Caso a identificação esteja vinculada a um evento incorreto ou inativo, remova-a e associe-a ao evento de pensão ativo utilizado na folha de pagamento.
**(5)** Verifique, no cadastro do dependente, na tela **"Configuração Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários), aba **"Dependentes"**, sub-aba **"Incidências da Pensão"**, se os eventos que devem compor a incidência da pensão estão corretamente vinculados.
**(6)** Após realizar os ajustes necessários, execute o recálculo da folha de pagamento para os funcionários que possuem desconto de **Pensão Alimentícia**.
**(7)** Por fim, valide se o **IRRF** foi calculado corretamente, confirmando se o valor da pensão foi deduzido da base de cálculo antes da aplicação das alíquotas do imposto.

![Imagem 1: (1) Acesse a tela "Eventos" (Pessoal+ » Cadastros » Eventos) e localize o evento de Pensão Alimentícia cadastrado no…](https://ajuda.sankhya.com.br/hc/article_attachments/41291111325719)![Imagem 2: (1) Acesse a tela "Eventos" (Pessoal+ » Cadastros » Eventos) e localize o evento de Pensão Alimentícia cadastrado no…](https://ajuda.sankhya.com.br/hc/article_attachments/41291107744663)![Imagem 3: (1) Acesse a tela "Eventos" (Pessoal+ » Cadastros » Eventos) e localize o evento de Pensão Alimentícia cadastrado no…](https://ajuda.sankhya.com.br/hc/article_attachments/41291111328023)

**Causa**

O erro ocorre quando o evento de **"Pensão Alimentícia"** não possui a identificação adequada vinculada para classificá-lo como dedução da base de **"IRRF"**, ou quando essa identificação está associada a um evento inativo. Nesses casos, o sistema não reconhece o valor da pensão como dedutível, realizando o cálculo do imposto sobre a base total, sem a devida dedução, em desacordo com a legislação tributária vigente.

Além disso, a parametrização incorreta dos eventos de dedução no cadastro das **incidências da pensão** pode impedir que o cálculo do **IRRF** seja processado corretamente, impactando diretamente no valor apurado.
