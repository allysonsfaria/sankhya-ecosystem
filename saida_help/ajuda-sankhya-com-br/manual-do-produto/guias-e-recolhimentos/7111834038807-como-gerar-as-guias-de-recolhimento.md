---
id: "7111834038807"
titulo: "Como gerar as guias de recolhimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7111834038807-Como-gerar-as-guias-de-recolhimento"
trilha: "Manual do Produto > Pessoas+ > Encargos e Obrigações Legais > Guias e Recolhimentos"
atualizado_em: "2026-10-02T15:55:11Z"
rotulos: ["Integração Financeira", "Folha", "DIRF", "DARF", "Geração de Guias", "SEFIP", "br.com.sankhya.rh.GeracaoGuias Integração Financeira SEFIP", "lotação de obra", "FPSEFIPLOTACAO", "GRRF", "GPS", "Declaração anual IRRF geração arquivo emissão demonstrativo rendimentos", "Emissão arquivo SEFIP integração financeira importação leiautes", "Recolhimento FGTS rescisório geração guia integração financeira", "Pessoal+", "FPCOMPENSCAMPO9"]
---

# Como gerar as guias de recolhimento

```
 Módulo: Pessoal+ > Rotinas Folha
```

---

Nesta tela serão realizadas as emissões dos arquivos de conexão para a SEFIP, DIRF, GRRF, DARF e GPS, além de integrar seus respectivos valores ao financeiro.

![geração](https://ajuda.sankhya.com.br/hc/article_attachments/15777451374231)

Ao acessar a tela, **"Selecione o tipo de guia"** que deseja gerar a emissão, dentre as opções:

| [SEFIP](https://ajuda.sankhya.com.br/hc/pt-br/articles/7111834038807-Como-gerar-as-guias-de-recolhimento#sefip) | [GRRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/40469921798935) | [DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167) | [GPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/7111834038807-Como-gerar-as-guias-de-recolhimento#gps) | [DARF](https://ajuda.sankhya.com.br/hc/pt-br/articles/7111834038807-Como-gerar-as-guias-de-recolhimento#darf) |
| --- | --- | --- | --- | --- |

---

![Imagem 2: Antes de gerar essas guias é necessário realizar a importação dos seus respectivos leiautes. Para isso, acione o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16805593929111) Antes de gerar essas guias é necessário realizar a importação dos seus respectivos leiautes. Para isso, acione o botão **"Importar Leiautes das Guias"**, selecione a guia que deseja importar o leiaute e clique em **"Importar Guias"**.

![importaçao](https://ajuda.sankhya.com.br/hc/article_attachments/15778187981207)

Com as guias importadas será apresentada a mensagem:

**"Guias importadas com sucesso!"**

---

## SEFIP

A geração do arquivo SEFIP - Sistema Empresa de Recolhimento do FGTS e Informações à Previdência Social é realizada para enviar as informações da folha calculada no sistema para o aplicativo Sefip da Caixa. Além de ter a possibilidade de integrar com o financeiro apenas os devidos valores relativos ao FGTS da folha.

Após realizada a importação do leiaute, sua base estará pronta para que o arquivo SEFIP seja emitido. Dessa forma, acesse a tela Geração de Guias, em seguida, acione o menu **"SEFIP"** e **"Geração da Guia"**, respectivamente.

![geraçao](https://ajuda.sankhya.com.br/hc/article_attachments/15791108997655)

De acordo com o manual da SEFIP, o arquivo deverá ser gerado levando em consideração os códigos de recolhimento, portanto, deverá se atentar e alterar tanto o arquivo de leiaute, quanto o código de recolhimento se necessário.

Na etapa **1 - Informações Gerais**, selecione o **"Arquivo de Leiaute"** utilizando o código ou a lupa como apoio na busca do arquivo.

![etapa](https://ajuda.sankhya.com.br/hc/article_attachments/15792787217943)

**Importante:** existem dois leiautes distintos que deverão ser usados considerando as possíveis situações ocorridas na competência, que são:

- **11 - Sefip 650**: responsável pelo envio das informações dos empregados que tiveram cálculo de folha de Dissídio/Convenção Coletiva/ACT;
- **8 - Sefip**: referente aos recolhimentos gerais dentro do prazo, constando todos os cálculos dos demais tipos de folha, exceto os cálculos por definição dos reajustes sindicais anuais.

Informe a **"Referência"** e a **"Empresa Responsável"** para qual será gerado o arquivo.

Indique se o **"Tipo de Folha"** será **"Normal"**, **"Somente 13º"** ou **"Normal e 13º"**.

Os indicadores **"Recolhimento do FGTS"** e **"Recolhimento do INSS"** sinalizam para o validador da SEFIP se as informações estão ou não dentro do prazo legal. Preencha também a **"Data"** do recolhimento.

É importante ressaltar que se for **"Recolhimento** **em atraso"** deverá ser informada ainda a Data do efetivo recolhimento. Com isso, as informações geradas serão acrescidas de juros/multas, automaticamente no campo **"Índice Cálculo JAM"**.

Informe no campo **"Contato da empresa responsável"** o nome do responsável pelo envio das informações.

O campo **"Código Recolhimento"** é uma chave para a SEFIP e indica qual a natureza das informações, por exemplo, o código **"115"**, utilizado para recolhimento/declaração referente a situações que não se enquadrem nos demais códigos de recolhimento.

O recolhimento/declaração ao FGTS, bem como, a declaração ao FGTS devem ser indicados por meio do campo **"Modalidade"**, de acordo com as seguintes opções:

- **Recolhimento ao FGTS e Declaração à Previdência**: indica que haverá recolhimento ao FGTS e prestação de informações à Previdência;
- **1 Declaração para FGTS e à Previdência**: deve ser utilizada nas situações em que não é recolhido o FGTS devido no mês de competência, configurando a confissão de débito para o Fundo de Garantia, bem como, para prestar informações à Previdência;
- **9 Confirmação de informações anteriores – Rec/Decl. ao FGTS e Decl. à Previdência**: deve ser usada para retificar informações de SEFIP já transmitidas.

Nos campos **"Inscrição da Software House"** e **"Tipo de Inscrição da Software House"** preencha as informações relacionadas a Empresa que desenvolveu o Software.

Após todo o preenchimento, clique em **"Próximo"** ou na etapa seguinte.

A etapa **2 - Autônomos (Financeiro)** deverá ser preenchida em casos de geração do arquivo para autônomos. Nesse caso, informe a **"Natureza"**, o **"Vínculo"**, a **"Categoria"** e o código **"CBO"** destes.

![etapa](https://ajuda.sankhya.com.br/hc/article_attachments/15792787220503)

Não havendo esses funcionários, avance para a próxima etapa.

Na etapa **3 - Empresas**, selecione a Empresa do arquivo a ser gerado.

![etapa](https://ajuda.sankhya.com.br/hc/article_attachments/15792787224727)

Selecione na etapa **4 - Funcionários**, quem irá compor o arquivo. Aqui, pode-se definir **"Filtros"** padrões e personalizados, incluindo condições. É importante filtrar os funcionários que estão em **"Situação normal"** para que não haja divergências no arquivo.

![etapa](https://ajuda.sankhya.com.br/hc/article_attachments/15793043140631)

**Observação:** funcionários afastados deverão ser enviados para SEFIP nas seguintes condições:

- No mês de afastamento, informe a remuneração correspondente aos dias efetivamente trabalhados, acrescidos dos 15 dias iniciais de responsabilidade do empregador/contribuinte;
- Se os 15 dias ultrapassarem o mês de afastamento, a remuneração correspondente aos dias excedentes deve ser informada na GFIP/Sefip do mês seguinte;
- No mês de retorno, informe a remuneração correspondente aos dias efetivamente trabalhados.

Por fim, na etapa **5 - Gerar**, clique no botão **"Gerar"**. Logo após, acesse o aplicativo da SEFIP e realize a importação da folha.

![etapa](https://ajuda.sankhya.com.br/hc/article_attachments/15797502629911)

**Observação:** ao realizar a importação do arquivo para filiais no aplicativo da SEFIP, os campos **"CNAE-Preponderante"** e **"F.A.P"** devem ser preenchidos manualmente.

**Importante:** empresas que possuem configuração de lotação de obra devem ativar o parâmetro **"Gerar SEFIP sem validar lotação? - FPSEFIPLOTACAO"** para que a SEFIP seja gerada em um único arquivo para todas as empresas. Caso o parâmetro esteja desabilitado, será gerado um arquivo para cada empresa.

---

### Integração Financeira

Com o arquivo SEFIP gerado, realize a integração com o Financeiro. Para isso, retorne a tela principal da Geração de Guias e clique novamente no menu SEFIP, em seguida no menu **"Financeiro"**.

![financeiro](https://ajuda.sankhya.com.br/hc/article_attachments/15797303183383)

Na aba **"Geral"**, seção **"Informações Gerais"**, defina se a **"Guia"** será emitida por **"Empresa"** ou **"Departamento"**. Indique também a **"Empresa"** responsável pelos dados da integração financeira.

Se definida a geração por Departamento, será apresentado o campo de **"Grau"**, que, por padrão, o sistema preenche automaticamente.

Abaixo é possível **"Selecionar Departamentos"** que vão compor o arquivo. Caso deseje selecioná-los, clique em cima do campo para escolher.

No grupo **"Gerar Por"**, as opções **"FGTS"** e **"FGTS Menor Aprendiz"** permitem informar se gerará o arquivo somente para Menor Aprendiz ou para os demais vínculos.

![financeiro](https://ajuda.sankhya.com.br/hc/article_attachments/15797303185943)

Em **"Dados da Folha"**, marque os tipos de **"Folhas"** e selecione a **"Referência"** para a integração.

![financeiro](https://ajuda.sankhya.com.br/hc/article_attachments/15797303187223)

A seção **"Valores"** está relacionada às informações em caso de pagamento fora do prazo. Assim, estando preenchidas todas as informações, clique no botão **"Gerar Demonstrativo"** localizado no canto superior direito da tela.

Serão apresentadas na tela as informações para conferência, sendo possível imprimir ou apenas fechar o arquivo após a conferência.

![demonstrativo](https://ajuda.sankhya.com.br/hc/article_attachments/15797303189143)

Clique na aba **"Integração Financeira"** e selecione a configuração financeira para a integração no campo **"Integrando com financeiro com base na configuração"**.

![integrar](https://ajuda.sankhya.com.br/hc/article_attachments/15797303191959)

Preencha as demais informações, como, **"Data de Negociação"**, **"Data de Vencimento"**, **"Data de Entrada e Saída"**, **"Natureza" e "Histórico"**.

Por fim, clique em **"Integrar Financeiro"** e confirme a integração financeira.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7111834038807-Como-gerar-as-guias-de-recolhimento#top)

##

## GPS

A GPS - Guia da Previdência Social é um documento hábil para o recolhimento das contribuições sociais a ser utilizado pelos contribuintes individuais, contribuintes facultativos e para o empregado doméstico. No caso de empresas, estas contribuições deverão ser recolhidas em GPS mediante débito em conta, o que traz comodidade para o contribuinte e ao mesmo tempo melhora a segurança no trato das informações.

Atualmente com a entrada em vigor da DCTF Web, o empregador passou a utilizar o DARF Previdenciário, essa nova guia será emitida após a transmissão da DCTF Web, pelo o [Portal do e-CAC](https://www.gov.br/receitafederal/pt-br/canais_atendimento/atendimento-virtual).

Na tela Geração de Guias tem-se a possibilidade de informar as compensações e retenções que ocorrerão na referência, bem como, realizar a emissão de demonstrativo para conferência e integração com financeiro.

Ao acessar a referida tela, clique no menu **"GPS"**. Em seguida, preencha as informações da aba **"Geral"**, sendo elas:

![aba](https://ajuda.sankhya.com.br/hc/article_attachments/15772043105303)

Na seção **Informações Gerais**, indique se os dados da guia a ser gerada pertence a **"Matriz"** ou a **"Filial"** e selecione a(s) **"Empresas"** e **"Departamentos"**.

Em seguida, em **Dados da Folha**, selecione o **"Tipo de folha"**, a **"Referência"** e a **"Data de Vencimento"**. Efetue a marcação **"Utiliza valor de retenção no 13º salário"** se assim desejar.

| **Retenção de terceiros**   - Para que os valores referentes à **retenção de terceiros** sejam gerados corretamente **tanto na guia GPS quanto no Resumo da Folha**, é necessário garantir as seguintes configurações:    1. **Parâmetro FPCOMPENSCAMPO9 ligado**: esse parâmetro habilita a compensação dos valores de retenção de terceiros nas contribuições previdenciárias.   2. **Na geração da guia GPS**, a opção **Utiliza valor de retenção no 13º salário** deve estar desmarcada. As retenções não se aplicam às folhas de 13º salário, portanto essa opção não deve ser marcada.   3. **Na geração do Resumo da Folha, os tipos de folha selecionados devem ser os mesmos utilizados na geração da GPS**, **exceto o tipo 13º Salário**, que **não deve ser incluído**, pois não participa dessa dedução. |
| --- |

Preencha os **Valores** referentes ao **"Faturamento"**, **"Autônomo/Funrural"**, aos índices de **"Atualização Monetária"** e **"Juros/Multas"**.

Depois, clique na aba **"Compensações"** para informar as devidas compensações. Acione então, o botão **"Inserir Compensação"** e preencha a **"Referência"**, os códigos da **"Empresa"**, **"Parceiro"** e **"Natureza"**, o **"Vlr. Original"**, o **"Saldo a Comp."**, a **"Dt. Recolhimento"** e clique no botão **"Salvar"**.

![compensaçoes](https://ajuda.sankhya.com.br/hc/article_attachments/15775105291543)

Para excluir uma Compensação, basta passar o mouse em cima da linha desejada que o botão **"Excluir este registro"** será exibido ao final da mesma linha.

Se tiver valores para retenção, clique na aba **"Valor Retenção"** e habilite a marcação **"Utiliza Valor Retenção"**, assim, os valores já registrados serão apresentados na seção **Registros encontrados**.

![retençao](https://ajuda.sankhya.com.br/hc/article_attachments/15775853944855)

Caso seja necessário alterar algum valor, selecione a linha desejada e clique no botão **"Modo Edição de Registros"**. Mas se precisar inserir outros valores, basta acionar o botão **"Inserir Retenção"** e preencher as informações solicitadas.

Informe como essa **"Retenção"** será realizada, dentre as seguintes opções:

- Pela data da Negociação;
- Pela data da Baixa;
- Digitação manual.

Para excluir uma Retenção passe o mouse em cima da linha desejada para que o botão **"Excluir este registro"** seja exibido ao final da mesma linha.

Após todas as configurações, pode gerar a guia clicando no botão **"Gerar GPS"** posicionado no canto superior direito da tela.

![guia](https://ajuda.sankhya.com.br/hc/article_attachments/15775808873751)

Conforme demonstrado acima, serão apresentadas na tela as informações para conferência. Sendo possível também imprimir o arquivo ou apenas fechá-lo após conferência.

Por fim, acesse a aba **"Financeiro"** para integrar os valores de compensações e retenções ao financeiro.

![integrar](https://ajuda.sankhya.com.br/hc/article_attachments/15775981742103)

Selecione no campo **"Integrando com financeiro com base na configuração \*"** a base de cálculo para esta integração conforme as seguintes opções: **"INSS"**, **"IRRF"**, **"Autônomos"**, **"Folha"**, **"Salário normal"**, **"Férias"**, **"Rescisão"** e **"FGTS"**. Informe as datas de **"Negociação"**, **"Vencimento"** e **"Entrada e Saída"**, bem como, o código da **"Natureza"**.

Caso tenha alguma informação adicional, descreva-a no campo **"Histórico"**. Para finalizar, clique no botão **"Integrar Financeiro"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7111834038807-Como-gerar-as-guias-de-recolhimento#top)

## DARF

A DARF (Documento de Arrecadação de Receitas Federais) é uma guia que serve para arrecadar os impostos, contribuições e taxas que estão embutidas nas operações financeiras. Esse documento é um dos principais instrumentos de recolhimento de tributos à Receita Federal.

Para gerar o arquivo da DARF, acesse a tela Geração de Guias, clique no menu **"DARF"** e escolha o **"Tipo de DARF"** que deseja gerar entre as opções: **"Individual"**, **"Coletiva"** e **"Receita Bruta"**.

[GIF animado: Imagem 20: Para gerar o arquivo da DARF , acesse a tela Geração de Guias , clique no menu "DARF" e escolha o "Tipo de DARF" que…](https://ajuda.sankhya.com.br/hc/article_attachments/15776192566807)

---

#### **(1)** DARF Individual

Caso queira gerar a DARF Individual, basta clicar nessa opção. A DARF Individual é utilizada nos casos em que já foi realizada a geração da guia coletiva e, para um funcionário não houve o recolhimento naquele momento, portanto, deve ser usada como exceção.

Na aba **"Processamento"**, seção **"Informações Gerais"** indique como a **"Geração da guia"** será realizada conforme as opções abaixo:

- **Matriz e filiais**: valor total unificado considerando todas empresas ligadasà matriz;
- **Empresa**: valor separado por CNPJ selecionado.

Selecione a **"Empresa"** e o **"Funcionário"** desejado.

![informaçoes](https://ajuda.sankhya.com.br/hc/article_attachments/15776755467927)

Na seção **"Dados da Folha"** escolha o **"Tipo de Folha"**, o **"Tipo de Receita"**, o **"Fato Gerador"** que é a referência do pagamento e a **"Data da negociação"** que é a data de referência de lançamento, a **"Data de Vencimento"** e a **"Data de Entrada e Saída"**.

![dados](https://ajuda.sankhya.com.br/hc/article_attachments/15776755470615)

Informe em **"Valores"**, o percentual de **"%Multa"** e **"%Juros"**. 

![valores](https://ajuda.sankhya.com.br/hc/article_attachments/15776710554263)

Após preencher todas as informações, clique no botão **"GERAR DARF"**. 

[GIF animado: Imagem 24: Após preencher todas as informações, clique no botão "GERAR DARF" .](https://ajuda.sankhya.com.br/hc/article_attachments/15776266695319)

Desse modo, serão apresentadas na tela as informações para conferência. Sendo possível também imprimir o arquivo ou apenas fechá-lo após conferência.

Também é possível definir o código e nome do funcionário para histórico, para isso, realize a marcação **"Usar código e nome do funcionário na composição do histórico?"** da aba **"Financeiro"**.

---

#### **(1)** DARF Coletiva

Agora, para gerar a guia coletiva, retorne à tela inicial da Geração de Guias e, em seguida, clique na opção Coletiva.

Preencha as mesmas informações citadas acima nas seções Informações Gerais, Dados da Folha e Valores.

Depois, basta clicar no botão GERAR DARF.

[GIF animado: Imagem 25: Depois, basta clicar no botão GERAR DARF .](https://ajuda.sankhya.com.br/hc/article_attachments/15776192581399)

Assim, serão apresentadas na tela as informações para conferência, sendo possível imprimir o arquivo ou apenas fechá-lo após conferência.

**Observação:** para realizar a integração coletiva da DARF, não pode haver nenhuma integração.

---

#### **(1)** DARF Receita Bruta

A DARF Receita Bruta é gerada de forma semelhante às demais, bem como, sua integração com o financeiro.

![Imagem 26: A geração da guia da DARF Receita Bruta é feita exclusivamente por empresas optantes pela desoneração da folha de…](https://ajuda.sankhya.com.br/hc/article_attachments/16590897255319) A geração da guia da DARF Receita Bruta é feita exclusivamente por [empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214-Registro-Fiscal#AbaDesonera%C3%A7%C3%A3odaFolha) optantes pela desoneração da folha de pagamento no todo ou em partes.

Primeiramente, indique na aba Processamento as Informações Gerais referentes à Geração da guia por e o Código da Empresa para qual deseja gerar a guia.

**Nota:** a seleção da opção Matriz e filiais do campo Geração da guia por pode ser realizada apenas pelas empresas matrizes, de modo que a visualização da guia será consolidada pela soma da receita bruta da matriz com as filiais (CNPJ Raiz). Assim, caso queria a visualização individual, ou seja, por empresa, deve-se selecionar a opção **"Empresa"**, dessa forma, todas as empresas, sejam elas matrizes ou filiais, estarão disponíveis para seleção e visualização.

![inf](https://ajuda.sankhya.com.br/hc/article_attachments/15777117823767)

Em seguida, preencha os Dados da Folha com o **"Período de Apuração"** e a Data de Vencimento.

![dados](https://ajuda.sankhya.com.br/hc/article_attachments/15777046436119)

Por fim, defina os Valores referentes ao percentual de %Multa e %Juros e clique no botão GERAR DARF.

![valores](https://ajuda.sankhya.com.br/hc/article_attachments/15777046439191)

---

### Integração Financeira

![Imagem 30: A integração com o financeiro da guia DARF Receita Bruta será realizada apenas pela geração da guia por Matriz e…](https://ajuda.sankhya.com.br/hc/article_attachments/16805593929111) A integração com o financeiro da guia DARF Receita Bruta será realizada apenas pela geração da guia por Matriz e filiais, de modo que, quando a geração for realizada por Empresa, a aba **"Financeiro"** não será habilitada. O financeiro dessa guia irá integrar apenas o valor total da receita bruta pelo CNPJ raiz, ou seja, Matriz mais filiais ou apenas matriz quando não houver filiais geradas por meio da configuração da opção Matriz e filiais do campo Geração da guia por.

Após conferir os valores da guia gerada, pode-se realizar a integração com o financeiro. Para isso, clique na aba Financeiro e, em seguida, selecione a configuração financeira para a integração, a **"Data de Negociação"**, a **"Data de Vencimento"**, a **"Data de Entrada e Saída"**, a **"Natureza"** e o **"Histórico"** e por último, clique no botão **"INTEGRAR FINANCEIRO"**.

![integrar](https://ajuda.sankhya.com.br/hc/article_attachments/15777221033367)

Caso tente realizar a integração de uma guia que já havia sido integrada, será exibida a seguinte mensagem:

**"Falha ao realizar a integração financeira!**
**Motivo: Guia DARF já integrada ao financeiro para essa empresa e referência! Nº Financeiro:01234"**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7111834038807-Como-gerar-as-guias-de-recolhimento#top)
