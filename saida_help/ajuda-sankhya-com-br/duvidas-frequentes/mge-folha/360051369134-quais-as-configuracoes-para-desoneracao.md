---
id: "360051369134"
titulo: "Quais as configurações para desoneração da folha de pagamento?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051369134-Quais-as-configura%C3%A7%C3%B5es-para-desonera%C3%A7%C3%A3o-da-folha-de-pagamento"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:35:03Z"
rotulos: ["Configuração", "Impostos", "eSocial", "Folha de Pagamento", "Configurações para Desoneração da Folha de Pagamento", "Legislação", "CPRB"]
---

# Quais as configurações para desoneração da folha de pagamento?

| - Através da Lei 12.546/2011 foi instituída a denominada **"Desoneração da Folha de Pagamento"**, que substitui parte das contribuições previdenciárias da folha de salários pela receita bruta ajustada. A partir de 01/12/2015, por força da Lei 13.161/2015, a aplicação da desoneração é facultativa, ou seja, o contribuinte pode escolher qual forma de tributar a folha é mais interessante, se pela forma tradicional (contribuição sobre a folha de pagamento) ou se pela forma desonerada (contribuição sobre a receita). |
| --- |

Para tal, seguem as principais configurações:

### 1-  Avançado >> Registro Fiscal:

Acessando a tela do ‘Registro Fiscal’ informaremos os dados referentes aos requisitos para atender a Lei de no 12.546/2011, especificamente no grupo “Desoneração da folha”.

![Imagem 1: Acessando a tela do ‘Registro Fiscal’ informaremos os dados referentes aos requisitos para atender a Lei de no…](https://ajuda.sankhya.com.br/hc/article_attachments/14393072038295)

#### 1.1. Grupo ‘Normal’:

O Grupo ‘Normal’ apresenta os campos ‘Percentual da Receita Bruta para INSS’ que retornará com o percentual reduzido, facilitando a conferência com as Bases do Resumo da Folha.

O processo de 'Desoneração da Folha' não tem ligação direta com o campo 'Percentual de INSS', o cálculo para os valores relacionados ao 'Percentual da Receita Bruta para INSS' atua com um determinado cálculo e o campo 'Percentual de INSS' opera com outro conforme a seguir:

| - **((20 \* (100 - x)) / 100)** , sendo X o valor do percentual da desoneração. |
| --- |

Exemplo Prático:

| - 20 \* (100 - 18) / 100 = 16,4 (valor levado para o campo "Percentual de INSS"). |
| --- |

![Imagem 2: 20 * (100 - 18) / 100 = 16,4 (valor levado para o campo "Percentual de INSS").](https://ajuda.sankhya.com.br/hc/article_attachments/14393125586199)

Valor do INSS da Receita Bruta: deverá ser alimentado manualmente, pelos usuários, com um valor correspondente ao percentual que lhe couber sobre o valor da Receita Bruta, oriunda das atividades que se enquadram nas regras da Lei 12.546/2011.

![Imagem 3: Valor do INSS da Receita Bruta: deverá ser alimentado manualmente, pelos usuários, com um valor correspondente ao…](https://ajuda.sankhya.com.br/hc/article_attachments/14393120785943)

#### 1.2. Grupo '13o Salário’:

No Grupo ‘13o Salário’ temos o campo ‘Percentual da Receita Bruta para INSS’ utilizado para que o usuário insira o percentual da ‘Receita Bruta’ manualmente. O valor informado será utilizado para deduzir o percentual de 20% informado no campo ‘Percentual de INSS’.

Percentual de INSS: será alimentado automaticamente, com o valor de 20% reduzido, conforme o valor inserido no campo ‘Percentual da Receita Bruta para INSS’. Essa redução será conforme é realizado na’ Folha Normal’.

![Imagem 4: Percentual de INSS: será alimentado automaticamente, com o valor de 20% reduzido, conforme o valor inserido no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/14393173689751)

O usuário precisa, primeiramente, apurar o quanto a ‘Receita Desonerada’ representa sobre a ‘Receita Total’. O que será inserido no campo 'Percentual Receita Bruta para INSS', é a diferença entre o ‘Percentual total’ e o ‘Percentual extraído’ da razão citada. Uma vez inserido, ele irá reduzir o percentual aplicado sobre o valor original, informado no campo 'Percentual de INSS'.

#### 1.3. Indicativo de substituição da Contribuição Previdenciária Patronal:

Nesse campo informaremos se a empresa é:

- 1-Totalmente substituída ou
- 2-Parcialmente substituída

O indicativo e o percentual da contribuição patronal a serem aplicados sobre as remunerações pagas, devidas ou creditadas, para os contribuintes enquadrados nos artigos 7o a 9o da Lei no 12.546/2011, conforme classificação tributária indicada no evento de Informações Cadastrais do empregador/contribuinte, serão enviados para o eSocial, através do evento ‘S-1280 Informações Complementares aos Eventos Periódicos’.

![Imagem 5: O indicativo e o percentual da contribuição patronal a serem aplicados sobre as remunerações pagas, devidas ou…](https://ajuda.sankhya.com.br/hc/article_attachments/14393176184599)

### 2- Tela Arquivos >> Empresas:

Na tela da ‘Empresa’, do Pessoal, na aba **‘Informações Fiscais’**, temos o campo **“Indicativo de Desoneração da Folha”** que determina o tipo de desoneração de folha para ser enviado ao E-Social.

![Imagem 6: Na tela da ‘Empresa’, do Pessoal, na aba ‘Informações Fiscais’ , temos o campo “Indicativo de Desoneração da Folha” que…](https://ajuda.sankhya.com.br/hc/article_attachments/360081111414)

### 3- Emissão do Resumo da folha:

No menu Relatório >> Resumo da folha, aplique os filtros Referência, Tipos de Movimento e no grupo Resumo, selecione os campos **‘Demonstrar Resumos de Previdência e FGTS’** e '**Utiliza Valores de Retenção/Compensação de INSS’.**

![Imagem 7: No menu Relatório >> Resumo da folha, aplique os filtros Referência, Tipos de Movimento e no grupo Resumo, selecione os…](https://ajuda.sankhya.com.br/hc/article_attachments/360081111994)

Ao emitir o resumo da folha, o campo "Parte da Empresa" deverá estar igual ao da Registro Fiscal, no campo “Valor do INSS Receita Bruta”.

![Imagem 8: Ao emitir o resumo da folha, o campo "Parte da Empresa" deverá estar igual ao da Registro Fiscal, no campo “Valor do…](https://ajuda.sankhya.com.br/hc/article_attachments/14393168858135)

Repare que foi considerado o percentual parte empresa de 16,4% sobre a Base de INSS no valor de R$15473,49.

![Imagem 9: Repare que foi considerado o percentual parte empresa de 16,4% sobre a Base de INSS no valor de R$15473,49.](https://ajuda.sankhya.com.br/hc/article_attachments/14393180661783)

![Imagem 10: Repare que foi considerado o percentual parte empresa de 16,4% sobre a Base de INSS no valor de R$15473,49.](https://ajuda.sankhya.com.br/hc/article_attachments/14393216720023)

### 4- Geração arquivo DARF e GPS:

O ‘DARF DA RECEITA BRUTA’ e ‘GPS’ juntas serão a soma do valor da GUIA emitida no DARF da Dctfweb, as referidas guias serão impressas acessando o caminho Relatórios >> Gerador Documento/Guias - Gráfico >> Guia de INSS.

![Imagem 11: O ‘DARF DA RECEITA BRUTA’ e ‘GPS’ juntas serão a soma do valor da GUIA emitida no DARF da Dctfweb, as referidas guias…](https://ajuda.sankhya.com.br/hc/article_attachments/360082225393)

Para gerar o arquivo da DARF acesse a tela Guia de INSS, logo em seguida clique sobre o layout da ‘DARF Receita Bruta’.

![Imagem 12: Para gerar o arquivo da DARF acesse a tela Guia de INSS, logo em seguida clique sobre o layout da ‘DARF Receita Bruta’.](https://ajuda.sankhya.com.br/hc/article_attachments/360082225713)

Selecione, nas abas ‘Guia’ e ‘Empresas’, os dados para geração e logo em seguida acione o botão de visualização. Para integrar os valores para pagamento, utilize a aba ‘Financeiro’ para fazer a integração.

![Imagem 13: Selecione, nas abas ‘Guia’ e ‘Empresas’, os dados para geração e logo em seguida acione o botão de visualização. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/14393225345943)

![Imagem 14: Selecione, nas abas ‘Guia’ e ‘Empresas’, os dados para geração e logo em seguida acione o botão de visualização. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/360082225833)

Por último é possível imprimir e integrar com o financeiro a GPS da folha de pagamento.

![Imagem 15: Por último é possível imprimir e integrar com o financeiro a GPS da folha de pagamento.](https://ajuda.sankhya.com.br/hc/article_attachments/360081113834)

Selecione, nas abas ‘Guia’ e ‘Empresas’ os dados para geração, e logo em seguida acione o botão de visualização.

![Imagem 16: Selecione, nas abas ‘Guia’ e ‘Empresas’ os dados para geração, e logo em seguida acione o botão de visualização.](https://ajuda.sankhya.com.br/hc/article_attachments/360081113954)

![Imagem 17: Selecione, nas abas ‘Guia’ e ‘Empresas’ os dados para geração, e logo em seguida acione o botão de visualização.](https://ajuda.sankhya.com.br/hc/article_attachments/14393227527959)

### 5- Conclusão:

Vimos neste artigo como realizar as configurações no MGE Pessoal para que a desoneração da folha seja considerada na totalidade dos impostos da empresa. Assim, a desoneração da folha de pagamento é a possibilidade da retirada da Contribuição Previdenciária Patronal e substituição dela pela CPRB, o imposto que incide sobre a receita bruta do empreendimento.

A Contribuição Previdenciária sobre a Receita Bruta é calculada sobre o montante do negócio, a partir de um percentual que varia de acordo com o ramo. A empresa pode optar anualmente pelo regime que for mais conveniente, sendo sempre o pagamento da CPRB mensal.

Lembrando que as áreas Contábil e Fiscal da empresa poderão apoiar para o preenchimento correto do percentual a ser considerado para a desoneração da folha de pagamento.
