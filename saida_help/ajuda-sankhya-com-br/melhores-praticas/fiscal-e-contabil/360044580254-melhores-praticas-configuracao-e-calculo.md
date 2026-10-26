---
id: "360044580254"
titulo: "Melhores Práticas - Configuração e Cálculo do CIAP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580254-Melhores-Pr%C3%A1ticas-Configura%C3%A7%C3%A3o-e-C%C3%A1lculo-do-CIAP"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-10-13T16:33:50Z"
rotulos: ["#RevisadoJR", "Configuração", "SPED", "Fiscal", "Crédito", "ICMS", "#ValidadoThiagoArantes", "naopublicarRoger", "Coeficiente de CFOP relatórios de crédito", "Controle de crédito ICMS para ativos", "Cadastro e configuração no sistema", "coeficiente de creditamento", "CIAP"]
---

# Melhores Práticas - Configuração e Cálculo do CIAP

#### O que é CIAP?

O CIAP – Controle de Crédito de ICMS do Ativo Permanente foi instituído pelo Ajuste SINIEF n.º 08/97, sendo que a partir de 2010 o CIAP deixou de ser complementar passando a integrar o projeto SPED Fiscal através do Ato COTEPE 38/2009, modificado, posteriormente, pelo leiaute determinado no Ato COTEPE 47/2009, com obrigatoriedade de entrega a partir de janeiro/2011 para os contribuintes de ICMS, que apuram créditos de ICMS sobre o ‘Ativo Imobilizado’ (Ajuste SINIEF 02/2010).

Assim todos os bens e direitos utilizados por uma empresa, para a realização de suas atividades, serão considerados como ‘Ativo Imobilizado’. É nesse contexto que o CIAP foi criado, para regulamentar o dispositivo da Lei Complementar no. 87/96 (Lei Kandir), que possibilitou a todos os contribuintes do ICMS a apropriação do crédito nas aquisições de bens destinados ao ‘Ativo Permanente’.

Desta forma, todas as operações que envolvam: compras, vendas, baixas e transferência de maquinários, equipamentos, veículos, móveis, utensílios e edificações são demonstradas no CIAP.
O valor referente ao crédito do imposto de ICMS alusivo a um imobilizado será divido em 48 vezes (equivalente a 4 anos), creditando-se apenas de 1/48 (um quarenta e oito avos) por mês sendo que a sua manutenção irá requer um especial controle através do Livro CIAP – “Controle de Crédito do ICMS do Ativo Permanente”.

O Livro CIAP,  antes em papel com pequena possibilidade de cruzamento de dados e identificação de divergências, nessa nova realidade, passou a ser parte integrante da estrutura do SPED Fiscal com forte relacionamento entre as informações, maior facilidade de rastreabilidade com as Notas Fiscais escrituradas, além da evidência do imposto apropriado com a Apuração de ICMS.

Com relação à obrigatoriedade, o Fisco passou a exigir o CIAP rotineiramente, por período de apuração, independente de intimações e fiscalizações estaduais.

Considere as configurações da Aplicação, conforme abaixo:

**![Imagem 1: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/19195539308311) Configurações » Cadastros » Produtos » Produtos**

**Aba Geral:**

Usado como= [Imobilizado]

**Aba Impostos:**

Calcular ICMS: [marcado]
Atualizar CIAP: [marcado]

Com os ‘Bens’ já cadastrados, e efetuados a marcação para atualização do CIAP, para as movimentações de compra, venda, baixa e cálculo do crédito mensal, estes movimentos serão gerados no BLOCO G no EFD FISCAL.

**Aba bens>> Sub-aba CIAP:**

Na aba CIAP do BEM, configura-se os dados necessários para o cálculo correto do crédito a ser apropriado.

Tem-se os campos “Data inicial”, “Data Final”, “Quantidade de meses”, “Valor Crédito de ICMS”, assim como o campo do ‘Tipo de movimento’ (Tipo de Entrada no CIAP), que por default será o ‘IM’, os demais campos deverão ser preenchidos quando existir a informação ou alterados conforme a necessidade, como o campo “Tipo de Entrada do CIAP”.

- **Data inicial:** data de referência inicial do crédito de ICMS do bem;
- **Data Final:** data de referência final para crédito de ICMS do bem;
- **Valor Crédito de ICMS:** valor total do crédito de ICMS que será aproveitado até o final do período;
- **Quantidade de meses:** número de meses para diluição do crédito de ICMS, até o final do período;

**Observação:** Atentar para os bens que já tiveram parcelas apropriadas do CIAP, e que ainda existem parcelas a apropriar. Para essas situações os campos “Data inicial”, “Data Final”, “Quantidade de meses”, “Valor Crédito de ICMS”, devem refletir o período e o saldo do crédito CIAP a apropriar. 

**Exemplo:** Bem adquirido em 01/10/2019, com crédito de CIAP de R$ 1.440,00, foi apropriado até 31/12/2020. Em 01/01/2021 a empresa desse Bem deu go live no Sankhya, restando ainda 30 meses a apropriar, ou seja, até 31/10/2023 e um saldo crédito de CIAP de R$ 990,00, a configuração correta para esse exemplo seria;

**Aba Bens >> Sub-aba CIAP:**

![Imagem 2: Aba Bens >> Sub-aba CIAP:](https://ajuda.sankhya.com.br/hc/article_attachments/4413633183511)

**![Imagem 3: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/19195539313175) Comercial » Arquivo » Cadastros » Tipos de Operação - TOP**

**Aba Livros Fiscais:**

Tipo de Mov. do Bem (SPED)= [Escolher o tipo de movimento necessário]

**![Imagem 4: Comercial » Arquivo » Cadastros » CFOP](https://ajuda.sankhya.com.br/hc/article_attachments/19195539315479) Comercial » Arquivo » Cadastros » CFOP**

O coeficiente de creditamento é calculado quando as opções do cadastro de CFOP **"Utilizar nas tributadas do CIAP"** e **"Receita Bruta p/ CIAP"** são devidamente configuradas, para as operações de saídas tributadas e de exportação. Dessa forma, o respectivo bem deverá ter sido "inserido/registrado" através de uma nota fiscal de entrada, vinculado a um CFOP devidamente configurado, sem essas configurações no CFOP nas saídas, o cálculo do coeficiente não acontecerá.

Resumindo o cálculo do Coeficiente é: 

TRIBUTADAS E EXPORTAÇÃO / TOTAL DAS SAÍDAS

Para compreender em detalhes como funcionará esse cálculo, verifique:

**Aba: Geral**

**(1)** No campo **"Utilizar nas Tributadas do CIAP"** existem as seguintes opções: “Não Utilizar , Valor Contábil e Base de ICMS” com as seguintes funcionalidades]

![Imagem 5: (1) No campo "Utilizar nas Tributadas do CIAP" existem as seguintes opções: “Não Utilizar , Valor Contábil e Base de…](https://ajuda.sankhya.com.br/hc/article_attachments/19195552920983)

- **Não Utilizar:** Os valores comercializados nesta CFOP não irão compor os valores lançados na coluna 1 do quadro 3 do CIAP MODELO C COMPLETO;
- **Valor Contábil:** O valor contábil escriturado no Livro Fiscal referente a Nota Fiscal movimentada nesta CFOP irá compor os valores lançados na coluna 1 do quadro 3 do CIAP MODELO C COMPLETO;
- **Base de ICMS:** A Base de ICMS escriturada no Livro Fiscal referente a Nota Fiscal movimentada nesta CFOP irá compor os valores lançados na coluna 1 do quadro 3 do CIAP MODELO C COMPLETO;
- **Considerar config. por CST:** Através desta opção, será habilitada para preenchimento a aba Tributações por CFOP, onde realiza-se o vínculo das CST's aos CFOP's;

**Observação:** em operações de vendas tributadas integralmente, o Valor Contábil é igual a Base de ICMS. Assim, poderá ser marcado tanto o Valor Contábil quanto a **"Base de ICMS"**, que o valor a ser considerado será o mesmo. Porém, em uma operação com redução de base, deverá ser marcada somente a opção Base de ICMS. Com isso, a opção Base de ICMS deverá ser considerada na maioria dos casos. A opção Valor Contábil poderá ser utilizada nas vendas de exportação que não possuem Base de ICMS e tem CFOP específicas.

**(1)** Já, o cálculo da Receita Bruta para CIAP, será efetuado de acordo com a opção selecionada no campo **"Receita Bruta p/ CIAP"**. Vale ressaltar que as informações serão apresentadas no relatório CIAP, Modelo C, Quadro 3. As opções apresentadas nesse campo, são:

- **Não afeta:** com essa opção selecionada, o sistema não irá compor o valor do produto no "Total das Saídas (2)", no quadrante 3 da coluna "Operações e prestações (saídas)";
- **Subtrai:** informando essa opção, o sistema irá subtrair o valor do produto do CFOP no valor do Total das Saídas (2), no quadrante 3 da coluna Operações e prestações (saídas);
- **Somar:** indicando essa opção, o sistema irá somar o valor do produto do CFOP no valor do Total das Saídas (2), no quadrante 3 da coluna Operações e prestações (saídas);
- **Busca da Top:** selecionando essa opção, o sistema buscará a configuração realizada no campo "Receita Bruta p/ CIAP", localizado na aba Livro Fiscal, da tela Tipos de Operação - TOP, para gerar as informações do relatório.

**Observação:** caso o campo acima não esteja configurado, o sistema irá considerar a configuração estabelecida no campo **"Receita Bruta p/ EFD Contribuição"** desta aba.

**![Imagem 6: Cálculo do CIAP nos livros fiscais:](https://ajuda.sankhya.com.br/hc/article_attachments/19195539326487) Cálculo do CIAP nos livros fiscais:**

Com todas as configurações anteriores estando feitas, para saber o saldo do ICMS a recolher ou a pagar do CIAP basta acessar no módulo MGE Livros fiscais o relatório do CIAP, que fica no menu: **Relatórios>> CIAP.** Tanto o Modelo C, quanto o modelo C completo trazem as informações do crédito do CIAP, a diferença é a quantidade de informações

O relatório trará informações correspondente ao Crédito a ser apropriado no período (mês): Total de crédito a ser apropriado \* coeficiente / (1/48).

Para mais informações sobre relatório CIAP: 

Link: [Relatório CIAP Modelo C (Completo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596354-Relat%C3%B3rio-CIAP-Modelo-C-Completo-)

![Imagem 7: Este relatório contempla apenas os bens que forem configurados com fração mensal igual 48 meses.](https://ajuda.sankhya.com.br/hc/article_attachments/25864026271767) Este relatório contempla apenas os bens que forem configurados com fração mensal igual 48 meses.

![Imagem 8: Este relatório contempla apenas os bens que forem configurados com fração mensal igual 48 meses.](https://ajuda.sankhya.com.br/hc/article_attachments/4413633230231)
