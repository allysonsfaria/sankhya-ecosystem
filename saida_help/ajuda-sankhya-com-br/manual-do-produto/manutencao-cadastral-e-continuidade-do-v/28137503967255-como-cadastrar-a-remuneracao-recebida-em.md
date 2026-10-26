---
id: "28137503967255"
titulo: "Como cadastrar a remuneração recebida em outras empresas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28137503967255-Como-cadastrar-a-remunera%C3%A7%C3%A3o-recebida-em-outras-empresas"
trilha: "Manual do Produto > Pessoas+ > Colaboradores > Manutenção Cadastral e Continuidade do Vínculo"
atualizado_em: "2026-10-02T15:19:40Z"
rotulos: ["Impostos", "Admissão", "Pessoal", "eSocial", "Configuração Funcionários", "Cadastro de Remuneração em outras Empresas - Pessoal +"]
---

# Como cadastrar a remuneração recebida em outras empresas

No múltiplos vínculos o empregado tem associação empregatícia com mais de uma empresa, ou seja, ele trabalha em dois ou mais CNPJ's ao mesmo tempo, podendo o vínculo de trabalho ter a mesma categoria ou categorias distintas, como a 101 (empregado geral) e a 701 (autônomo), por exemplo.

Para isso é necessário o cadastro correto desses vínculos, visto que na soma dos salários não poderá ocorrer o recolhimento de INSS acima do teto.

No Pessoal +, acesse a tela de **"Configuração de Funcionários",** aba **"Admissão"** e preencha os campos abaixo:

![Imagem 1: No Pessoal +, acesse a tela de "Configuração de Funcionários", aba "Admissão" e preencha os campos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/28148046751383)

No campo **"Indicativo de Desconto do INSS em Outra Empresa"** escolha a opção que se enquadra a cada trabalhador.

⦁ Contribuição descontada por outra Empresa sobre valor menor que o teto;

⦁ Contribuição descontada por outra Empresa sobre valor do teto;

⦁ Contribuição descontada pela Empresa;

⦁ Não se aplica.

Em seguida, preencha a aba **"Remuneração Outras Empresas"**:

![Imagem 2: No Pessoal +, acesse a tela de "Configuração de Funcionários", aba "Admissão" e preencha os campos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/28148035153559)

Devem conter as informações de CNPJ da empresa em que possui o outro vínculo e categoria. Essa aba também possui o campo de **"Data de Desligamento"**, caso esse vínculo se encerre.

Após o cadastro, faça o lançamento dos eventos **"505 - BASE INSS OUTRAS FONTES"** e **"506 - INSS RETIDO OUTRAS FONTES"**, na tela de "**Lançamento de Movimento"**.

Conforme imagem abaixo, ao incluirmos o evento 505 no movimento Mensal é lançado um pop-up com a informação do CNPJ cadastrado na tela de **"Configuração de funcionários"**, é preciso confirmar:

![Imagem 3: Conforme imagem abaixo, ao incluirmos o evento 505 no movimento Mensal é lançado um pop-up com a informação do CNPJ…](https://ajuda.sankhya.com.br/hc/article_attachments/28148039549719)

Depois, insira também o valor do evento e confirme:

![Imagem 4: Depois, insira também o valor do evento e confirme:](https://ajuda.sankhya.com.br/hc/article_attachments/28148860111511)

![Imagem 5: Depois, insira também o valor do evento e confirme:](https://ajuda.sankhya.com.br/hc/article_attachments/28148860112151)

Veja o mesmo lançamento com o evento 506, mas dessa vez incluindo o valor descontado de INSS por outra fonte:

![Imagem 6: Veja o mesmo lançamento com o evento 506, mas dessa vez incluindo o valor descontado de INSS por outra fonte:](https://ajuda.sankhya.com.br/hc/article_attachments/28148898248855)

![Imagem 7: Veja o mesmo lançamento com o evento 506, mas dessa vez incluindo o valor descontado de INSS por outra fonte:](https://ajuda.sankhya.com.br/hc/article_attachments/28137503962391)

Lembrando que esses eventos também poderão ser lançados de forma fixa, caso esses valores não alterem nos próximos meses. Ou, conforme feito acima, lançando no movimento mensal, caso seja variável.

Esses são os dados básicos para cadastramento da Remuneração outras empresas, os quais têm impacto direto na **apuração dos impostos** na **folha de pagamento** e no **envio dos eventos ao eSocial**.

Portanto, ao seguir este **passo a passo de forma correta**, as etapas subsequentes serão realizadas com sucesso, garantindo a conformidade e a precisão nos cálculos de tributos e encargos sociais.
