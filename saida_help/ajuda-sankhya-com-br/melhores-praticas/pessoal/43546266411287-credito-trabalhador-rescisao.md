---
id: "43546266411287"
titulo: "Crédito trabalhador - Rescisão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546266411287-Cr%C3%A9dito-trabalhador-Rescis%C3%A3o"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-14T18:47:47Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Crédito trabalhador - Rescisão

### SITUAÇÃO

Ao calcular a rescisão de um colaborador, o sistema não realiza o desconto referente à parcela do Crédito do Trabalhador (empréstimo consignado), mesmo havendo saldo devedor registrado para o funcionário.

### SOLUÇÃO

**(1)** **Consulte as informações do empréstimo consignado**

Acesse o portal Emprega Brasil e confira as informações disponibilizadas para o desconto rescisório.

Para que o desconto do Crédito do Trabalhador seja realizado na rescisão, é necessário que estejam disponíveis o **saldo devedor atualizado da operação de crédito** e o **percentual das verbas rescisórias oferecido em garantia pelo trabalhador**. Caso alguma dessas informações não esteja disponível, o desconto não deverá ser realizado.

**(2)** **Realize a importação do Crédito do Trabalhador**

Acesse a tela **Lançamento de Movimento** (Pessoal+ » Rotinas Folha » Lançamento de Movimento) e realize a importação automática das informações do Crédito do Trabalhador.

Durante o processo, certifique-se de marcar a opção **Rescisão**, para que as informações necessárias ao cálculo rescisório sejam consideradas.

![Imagem 1: Confira a configuração do evento de base de cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/43558788587031)
![Imagem 2: Confira a configuração do evento de base de cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/43558788587927)
**(3)** **Confira a configuração do evento de base de cálculo**

Verifique se o evento **Base Margem Crédito do Trabalhador** está configurado corretamente e se contempla os eventos de remuneração utilizados no cálculo da rescisão.

Para essa conferência, consulte o Manual do Crédito do Trabalhador e valide os códigos de natureza de rubrica que devem compor a base de cálculo do desconto.

**(4)** **Verifique os eventos personalizados**

Caso sejam utilizados eventos personalizados para compor a remuneração do colaborador, acesse a tela **Eventos** (Pessoal+ » Cadastros » Eventos), na aba **Base de Cálculo**, e inclua manualmente os eventos que devem compor a base de cálculo do desconto do Crédito do Trabalhador.

![Imagem 3: Recalcule a rescisão](https://ajuda.sankhya.com.br/hc/article_attachments/43558740647831)

**(5)** **Recalcule a rescisão**

Após realizar as conferências e os ajustes necessários, efetue novamente o cálculo da rescisão e verifique se o desconto do Crédito do Trabalhador foi considerado corretamente.

**Observação:** os eventos padrão Sankhya já possuem vinculação automática à base de cálculo. Para eventos personalizados, é necessário realizar a vinculação manual, quando aplicável.

### CAUSA

A ausência do desconto do Crédito do Trabalhador na rescisão pode ocorrer devido à falta de informações necessárias para o cálculo ou à configuração incorreta da base de cálculo do evento de desconto.

Quando os eventos de remuneração utilizados na rescisão não estão vinculados à base de cálculo correspondente, o sistema pode não identificar corretamente os valores que devem ser considerados para o desconto.

Além disso, a ausência de informações essenciais sobre o empréstimo consignado, como o saldo devedor atualizado ou o percentual das verbas rescisórias oferecido em garantia, impossibilita a apuração do valor passível de desconto.

Nos termos da regulamentação vigente, a realização de eventual desconto nas verbas rescisórias vinculadas à garantia da operação de crédito depende da disponibilização prévia, pela instituição consignatária, das seguintes informações:

I – saldo devedor atualizado da operação de crédito;

II – percentual das verbas rescisórias oferecido em garantia pelo trabalhador no momento da contratação da operação.

A ausência de qualquer uma dessas informações na data do desligamento inviabiliza a operacionalização do desconto sobre as verbas rescisórias. Nessa hipótese, o empregador não deverá efetuar retenção ou repasse relacionado à garantia da operação de crédito, por não dispor dos elementos necessários à apuração do valor passível de desconto.
