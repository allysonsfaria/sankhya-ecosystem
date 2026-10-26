---
id: "39356664622103"
titulo: "Atualização de valor de insalubridade não refletida no sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39356664622103-Atualiza%C3%A7%C3%A3o-de-valor-de-insalubridade-n%C3%A3o-refletida-no-sistema"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-08-27T18:33:23Z"
rotulos: ["Configuração", "Eventos", "Atualização", "Folha", "Pessoal+", "Artigo criado KCS", "Sankhya RH - KCS", "Insalubridade"]
---

# Atualização de valor de insalubridade não refletida no sistema

**Mensagem**

Foi identificado que o sistema não está calculando o adicional de insalubridade na folha de pagamento nem na rescisão, mesmo com a verba devidamente configurada no cadastro do colaborador.

Além disso, o valor correspondente ao adicional de insalubridade também não está sendo incorporado ao cálculo das férias, impactando a composição da remuneração utilizada para esse processamento.

**Situação**

Ao processar a folha de pagamento mensal ou a rescisão, o evento de insalubridade não é calculado nem apresentado entre os proventos do colaborador, mesmo estando devidamente configurado no cadastro do funcionário. Além disso, ao realizar o cálculo de férias, o valor da insalubridade não está sendo incorporado.

**Solução**

Para resolver este problema, verifique e ajuste as seguintes configurações:

**Cenário 1: "Evento de Insalubridade" não esta sendo calculado na folha de pagamento ou rescisão**

**(1)** Acesse o **"Cadastro de Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários) e localize o colaborador que não está recebendo a insalubridade.

**(2)** Verifique o campo **"Tipo de Tabela de INSS/IRRF/Sal. Fam."** no cadastro do funcionário. Se estiver preenchido com **"Tabela Tipo C"**, altere para **"A – Empresas Privadas"**.

![Imagem 1: (2) Verifique o campo "Tipo de Tabela de INSS/IRRF/Sal. Fam." no cadastro do funcionário. Se estiver preenchido com…](https://ajuda.sankhya.com.br/hc/article_attachments/41274230277015)

**(3)** Acesse a tela de **"Tabela de Faixa"** (Pessoal+ » Cadastros » Tabela de Faixas) e confirme se o tipo de tabela está configurado como **"Empresas Privadas"** e se a tabela de faixa **5 -SALÁRIO MÍNIMO** está devidamente preenchida com os valores vigente no ano, pois essa tabela será considerada para o calculo de insalubridade. 

![Imagem 2: (3) Acesse a tela de "Tabela de Faixa" (Pessoal+ » Cadastros » Tabela de Faixas) e confirme se o tipo de tabela está…](https://ajuda.sankhya.com.br/hc/article_attachments/41329539412887)

**(4)** Salve as alterações realizadas e recalcule a folha.

**Cenário 2:  "Evento de Insalubridade" não está sendo considerado na incorporação para o pagamento de férias**

**(1)** Para cálculo de férias, acesse o **"Cadastro de Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o **"Evento 13 - Insalubridade"**.

**(2)** No evento de insalubridade, verifique o campo **"Incidência sobre Médias"** para que o evento seja considerado como incorporação o campo precisa ser preenchido como **"Incorpora ao Salário"**.

![Imagem 3: (2) No evento de insalubridade, verifique o campo "Incidência sobre Médias" para que o evento seja considerado como…](https://ajuda.sankhya.com.br/hc/article_attachments/41274230277783)

**(3)** Salve as alterações realizadas e recalcule a folha. 

**Causa**

O problema ocorre devido a configurações incorretas no cadastro do funcionário ou no evento de insalubridade:

- O campo **"Tipo de Tabela de INSS/IRRF/Sal. Fam."** está preenchido com **"Tabela Tipo C"** ao invés de **"A – Empresas Privadas"**, impedindo o cálculo correto da insalubridade.
- No cálculo de férias, o evento de insalubridade está configurado para incidir sobre as médias **"Pelo Valor"** ao invés de **"Incorpora ao Salário"**, causando divergências ou duplicidade nos valores.
- A tabela de faixa não está cadastrada corretamente com o tipo **"Empresas Privadas"**.
