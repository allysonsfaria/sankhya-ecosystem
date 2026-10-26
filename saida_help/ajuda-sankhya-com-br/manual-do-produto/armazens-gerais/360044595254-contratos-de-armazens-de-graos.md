---
id: "360044595254"
titulo: "Contratos de Armazéns de Grãos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os"
trilha: "Manual do Produto > Suprimentos e Estoque > Armazéns Gerais"
atualizado_em: "2026-07-29T15:07:02Z"
rotulos: ["Configuração", "WMS", "Parceiro", "Contrato", "br.com.sankhya.armazem.cad.cont.armazem", "Estoque", "Contratos de Armazenagem", "APURQTPEDOL", "TOPSCAPTACAO", "CONQTPROD", "Contratos Armazenagem Cadastros", "Armazéns Gerais"]
---

# Contratos de Armazéns de Grãos

```
 Módulo: Armazéns Gerais > Cadastros             Versão disponível: A partir da 4.3
```

---

Toda movimentação deve ter como premissa o registro do contrato realizado junto ao cliente. Esse contrato irá conter as diretrizes negociadas entre as partes e irá determinar o comportamento do sistema em relação ao controle e às ações pertinentes à operação.

Para facilitar sua navegação nas funcionalidades dessa tela, acesse os links abaixo:

| Funcionalidades da tela | |
| --- | --- |
| [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#PaineldeFiltros) | [Cabeçalho do Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#cabe%C3%A7alhodocontrato) |
| [Aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#abapropriedades) | [Aba Quebras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#abaquebras) |
| [Aba Comercialização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#abaComercializacao) | [Aba Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#abaservios) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) | [Botão Edição múltipla](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#BotaoEdi%C3%A7%C3%A3oMultipla) |

### Painel de Filtros

Para que as informações sejam apresentadas na tela, clique em ![Imagem 1: Para que as informações sejam apresentadas na tela, clique em "Aplicar" ou informe os campos "Nro. Contrato" , "Safra"…](https://ajuda.sankhya.com.br/hc/article_attachments/26898305536023) **"Aplicar"** ou informe os campos **"Nro. Contrato"**, **"Safra"**, **"Parceiro"** e **"Empresa"** para refinar as buscas.

![Imagem 2: Para que as informações sejam apresentadas na tela, clique em "Aplicar" ou informe os campos "Nro. Contrato" , "Safra"…](https://ajuda.sankhya.com.br/hc/article_attachments/27404234275735)

Além disso, é possível filtrar pela **"Situação do Contrato"** escolhendo entre:

- Ativo;
- Cancelado;
- Finalizado.

Pode-se selecionar a**"Modalidade do Contrato"**:

- Comercialização;
- Armazenagem.

É possível também filtrar pelo **"Tipo de Armazenador"**:

- Comprador;
- Depositante.

Por fim, é possível filtrar pelo **"Grupo de Contratos"**, cujas opções são exibidas com base no preenchimento do campo **"Grupo"** no [Cabeçalho do Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#cabe%C3%A7alhodocontrato).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#top)

### Cabeçalho do Contrato

![Imagem 3: Cabeçalho do Contrato](https://ajuda.sankhya.com.br/hc/article_attachments/20152574349591)

O campo **"Número do contrato"** é preenchido automaticamente e de forma sequencial, para indicar o número do Contrato de Armazenagem.

Através do campo **"Produto"**, vincule um Produto a um Contrato de Armazenagem.

O campo **"Empresa"** é destinado à Empresa relacionada ao respectivo Contrato de Armazenagem.

**Observação:** é possível limitar o acesso dos usuários dessa tela para que eles possam visualizar apenas  os registros das empresas desejadas. Para essa ação, é necessário criar uma regra na tela [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es) e, em seguida, vinculá-la no cadastro do(s) usuário(s) desejado(s) por meio da aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes).

No campo **"Situação do contrato"** selecione a situação atual do Contrato que pode ser **"Ativo"**, **"Cancelado"** ou **"Finalizado"**.

Lembre-se que, o campo **"Situação do Contrato"** é utilizado exclusivamente para fins de filtro. A situação definida no contrato não é considerada no momento do faturamento. Caso exista quantidade disponível para faturamento, o processo poderá ser realizado mesmo que o contrato esteja com situação Cancelado ou Finalizado.

No campo **"Modalidade de Contrato"** indique o tipo do contrato por meio das opções **"Armazenagem"** ou **"Comercialização"**. Ainda sobre esse campo, é importante ressaltar que:

- Quando a opção Comercialização for selecionada, o campo Tipo de Armazenador ficará definido com a opção Depositante. Além disso, ao escolher a opção Comercialização, somente as abas [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254#abapropriedades) e [Comercialização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#abaComercializacao) poderão ser editadas.
- Caso já existam movimentações lançadas para o contrato nas telas [Controle de Portaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria), [Laudo de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074-Laudo-de-Classifica%C3%A7%C3%A3o), [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054-Pesagem) e nas Centrais, não será possível editar o campo Modalidade de Contrato.
- É preciso possuir a licença **"30935 - Comercialização de Grãos/W"** para que o campo Modalidade de Contrato seja exibido.

O campo **"Tipo de Armazenador"** é apenas informativo e tem as seguintes opções:

- **Depositante:** selecione essa opção quando o Parceiro é o próprio responsável pelo envio do produto para o armazém.
- **Comprador:** indique essa opção quando o contrato origina-se de uma transferência de titularidade de estoque disponível no armazém em nome de outro parceiro.

Busque a **"Safra"**  à qual o Contrato de Armazenagem pertence. Faça esse cadastro na tela [Safras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595174-Safras).

Informe o **"Parceiro"** do respectivo Contrato de Armazenagem.

O campo **"Inscrição Estadual"** é de preenchimento automático e exibirá a Inscrição Estadual do Parceiro informado no Contrato.

O campo **"Endereço"** exibe o Endereço do Parceiro informado no Contrato, sendo também de preenchimento automático pelo sistema.

O campo **"Grupo"** é utilizado para agrupar contratos relacionados. Vale destacar que o sistema não possui um cadastro prévio de grupos. Portanto, se o grupo desejado não estiver disponível no momento do cadastro, basta inseri-lo no campo correspondente, e ele será criado automaticamente, ficando disponível para futuros cadastros. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#top)

### Aba Propriedades

![Imagem 4: Aba Propriedades](https://ajuda.sankhya.com.br/hc/article_attachments/20152650174231)

No campo **"Contrato Interno"**, informe o número do contrato interno utilizado por cada empresa.

Os campos **"Data do contrato"** e **"Data de término"** são informativos, referente ao período de vigência do contrato.

Indique no campo **"Padrão de Classificação"** o Padrão de Classificação a ser aplicado no contrato. Esse cadastro é feito previamente na tela [Padrões de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108593-Padr%C3%B5es-de-Classifica%C3%A7%C3%A3o). Essa informação influenciará no laudo de classificação dos produtos recebidos no armazém.

Em **"Regras p/ Laudo nas Saídas"**, selecione uma dentre as opções abaixo para a definição da regra para aplicação de laudos na classificação de saída:

- **Vincula e desconta:** indicando essa opção, o sistema exigirá o vínculo do laudo e aplicará os devidos descontos;
- **Não vincula:** selecionando essa opção, o botão **"Laudo"** da tela [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054-Pesagem) será desabilitado e exibirá o botão ![botão-gerar-saída-tela-pesagem](https://ajuda.sankhya.com.br/hc/article_attachments/15992605482007) **"Gerar Saída"** na mesma tela sem a exigência do vínculo do laudo;
- **Vincula e não desconta:** irá exigir o registro do laudo e o vínculo dele, mas não haverá aplicação do desconto no campo **"Descontos"**.

**Nota:** se a pesagem de um contrato com o **"Tipo de Movimentação"** igual a **"Saída"** já tiver sido realizada, o sistema não permitirá a alteração do campo Regras p/ Laudo nas Saídas no registro do contrato nessa tela.

**Observação:** quando um segundo contrato com o mesmo ticket for inserido nas telas Pesagem e [Controle de Portaria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria) com o Tipo de Movimentação igual a Saída e **"Carga"**, respectivamente, e o primeiro contrato estiver com uma opção do campo Regras p/ Laudo nas Saídas diferente do segundo contrato, a inclusão deste útimo não será permitida, ou seja, as opções definidas no campo Regras p/ Laudo nas Saídas nos dois contratos precisam ser iguais.

Informe no campo **"Unidade de Conversão p/ SC"** o valor pelo qual o Peso em Kg deverá ser dividido para conversão da quantidade em SC.

O campo **"Moeda"** lista todos os valores de moedas cadastrados do Tipo igual à Valor e será utilizado na valorização do estoque disponível, considerando a cotação atual dos produtos.

No campo **"Pedidos de Captação"**, serão listados todos os pedidos confirmados do respectivo parceiro e produto do contrato, cujo o Tipo de Operação-TOP esteja informada no parâmetro **"Tops de PDs de Captação - TOPSCAPTACAO"**. 

A marcação **"Valida pendência financeira x estoque disponível"** define se, na emissão das notas de saída, o contrato estará sujeito à liberação caso o valor do estoque disponível seja menor do que a pendência financeira do parceiro.

**Nota:** caso o parâmetro **"Incluir na validação de pendências financeiras x estoque disponível valor serviços - VALPENFINEXPRECARM"** esteja ligado, além do valor já faturado em aberto, o sistema considerará para esta validação, os valores já apurados e pendentes de faturamento para os serviços de Expedição/Recepção e Armazenagem na tela [Apuração/Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049658374-Apura%C3%A7%C3%A3o-Faturamento-de-Contratos).

Os campos **"Tipo de Título"** e **"Tipo de Negociação"** buscarão os tipos de títulos e tipos de negociação previamente cadastrados e serão utilizados no Cabeçalho das Notas de Movimentações.

Os campos **"Natureza"**, **"Centro de Resultado"** e **"Projeto"** são padrões de classificação do sistema e deverão ser utilizados no cabeçalho das notas de movimentações.

O campo **"Contato"** é obrigatório para indicação do contato do Parceiro responsável pelo Contrato de Armazenagem. Para isso, esse contato necessita estar previamente configurado na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacontatos).

O campo **"CIF / FOB"** indica o tipo de transporte do Contrato de Armazenagem. As notas relacionadas às movimentações do contrato deverão utilizar essa informação para preenchimento do respectivo campo no lançamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#top)

### Aba Quebras

![Imagem 6: Aba Quebras](https://ajuda.sankhya.com.br/hc/article_attachments/13147235022999)

![Imagem 7: Ao efetuar qualquer alteração nesta aba para um contrato Ativo , o sistema exibirá uma mensagem informando que será…](https://ajuda.sankhya.com.br/hc/article_attachments/20147274031767) Ao efetuar qualquer alteração nesta aba para um contrato Ativo, o sistema exibirá uma mensagem informando que será feito o reprocessamento da quebra ao confirmar esta operação. 

Selecione no campo **"Tipo de Quebra"** o tipo de quebra que será aplicado ao contrato, de acordo com as opções abaixo:

- **Quebra de Massa:**

| ```  ((Méd. Pond. Ui - Méd. Pond. UF) / (100 - Méd. Pond. Uf)) * 100 ``` |
| --- |

onde, **"Méd. Pond. Ui"** é igual a média ponderada da umidade inicial e **"Méd. Pond. Uf"** é igual a média ponderada da umidade final.

**Observação:** a quebra de massa é calculada apenas sobre o valor líquido, após os descontos inerentes ao processo de qualidade.

- **Quebra-Técnica:**

| ```  Saldo de Estoque do período x % Quebra Técnica ``` |
| --- |

onde, **"%Quebra Técnica"** se refere ao informado no campo do contrato.

A Quebra Técnica visa corrigir o estoque do cliente, devido à perda de umidade no processo de armazenamento. Seus descontos são realizados conforme periodicidade e percentual acordado em contrato. Além disso, com esta opção indicada o campo **"Tipo de Isenção"** será habilitado.

**Observação:** para ativar a apuração de quebras sobre os pedidos de devolução gerados em contratos que tenham o Tipo de Quebra igual a Quebra Técnica, ligue o parâmetro **"Apurar Quebra Técnica sobre Pedido de Devolução - APURQTPEDOL"**. Esta apuração irá considerar a Periodicidade de Desconto e o % Quebra-Técnica parametrizados e neste caso, não haverá tratativas para cobrança proporcional e período de isenção.

---

**APURQTPEDOL (Apurar Quebra Técnica sobre Pedido de Devolução):** Este parâmetro foi criado para um caso específico de **ajuste de quebra técnica** em pedidos de devolução.

- **LIGADO:** O sistema busca as notas de origem da quebra primeiro nos **Pedidos de Devolução** pendentes (Tipo 2) e, em seguida, nas **Notas Fiscais de Depósito** pendentes (Tipo 1).
- **DESLIGADO:** O sistema considera como origem **apenas as Notas Fiscais de Depósito** (Tipo 1).

O objetivo principal é considerar a diferença de quebra que surge quando um pedido de devolução é gerado antes do faturamento, mas novas quebras ocorrem nesse intervalo. Ao estar ligado, o sistema considera essa diferença no pop-up de saída para abater o saldo de estoque corretamente.

- No entanto, não o habilite se já houver **movimentações de entrada e saída** (pode quebrar o processo de faturamento) ou se o saldo de estoque for gerado por **mais de um Romaneio/NF-Depósito**.

---

- **Quebra de Transbordo:** a fórmula é Entradas x % informada no campo do contrato.
- **Isento:** esta opção indica a isenção de quebras no contrato. Dessa forma, ao selecionar esta opção todos os demais campos da aba serão desabilitados para edição.

No campo **"% Quebra Técnica"**informe o percentual a ser aplicado na Quebra Técnica.

Indique no campo **"% Umidade Padrão"** o percentual de umidade padrão a ser considerado na fórmula para o cálculo da Quebra de Massa.

Ao escolher a opção Quebra-Técnica no campo Tipo de Quebra, é possível especificar se o **"Tipo de Isenção"** será **"Por dias"** ou **"Por períodos"**. 

Preencha o campo **"Prazo de Carência"** com o período de carência a ser considerado no cálculo da Quebra-Técnica.

Defina a **"Periodicidade de Desconto"** de acordo com as opções a seguir:

- **Diária:** apuração diária;
- **Quinzenal:** 1º ao 15º dia e 16º ao último dia do mês, com apuração nos dias 16 e 1, respectivamente;
- **Mensal:** 1º ao último dia do mês, com apuração no dia 1 do mês subsequente.

A marcação **"Cobrar Proporcional"** indica a aplicação promocional do percentual de Quebra-Técnica, levando em consideração a data de entrada da movimentação e a periodicidade de apuração.

Informe no campo **"% Quebra Transbordo"** o percentual a ser aplicado na Quebra de Transbordo.

O campo **"Característica Analisável"** será habilitado apenas quando o Tipo de Quebra for igual à **"Quebra de Massa"**.

**Observação:** caso o usuário tente alterar qualquer informação no contrato que já possua lançamentos de isenção de quebras, o sistema apresentará uma mensagem sinalizando que a alteração não será permitida.

---

**![Imagem 8: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/20147451074711) Informações adicionais**

Quando o parâmetro **"Configuração de Quebra-Técnica por Produto - CONQTPROD"** estiver ligado, os campos mencionados terão o seguinte comportamento:

- Se o campo Tipo de Quebra estiver com a opção Quebra-Técnica selecionada, os campos % Quebra Técnica e Periodicidade de Desconto ficarão desabilitados.
- Quando o contrato for salvo, o campo % Quebra Técnica será preenchido com o valor percentual definido para o respectivo produto no campo % Quebra Técnica, localizado na sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque) da tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113).
- O campo Periodicidade de Desconto será definido com a alternativa **"Quinzenal"**.
- Os valores de % Quebra Técnica por produto serão apresentados nas apurações, para o Tipo de Apuração **"Quebras"** da tela [Apuração/Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049658374).

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#top)

### Aba Comercialização

```
 Esta aba estará disponível a partir da versão 4.19 do sistema.
```

Para configurar estar aba, o campo Modalidade do Contrato deve ser definido com a opção Comercialização.

![Imagem 9: Para configurar estar aba, o campo Modalidade do Contrato deve ser definido com a opção Comercialização .](https://ajuda.sankhya.com.br/hc/article_attachments/13147608381207)

Assim, o sistema irá dispor os seguintes campos:

O campo **"Tipo de Contrato"** possui as seguintes opções:

- **Compra a Fixar:** essa opção indica que o valor final do contrato será negociado posteriormente, após a entrega, e formalizado via processo de Fixação de Contratos;
- **Compra Fixada:** ao definir essa opção, o valor negociado será o preço final de compra do produto;
- **Venda Fixada:** com essa opção configurada, o valor negociado será o preço final da venda do produto.

Preencha o campo **"Quantidade Negociada"** com a quantidade de negociação, utilizando 2 casas decimais.

O campo **"Preço de Pauta/SC"** irá listar as moedas cadastradas do Tipo [Valor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754) e será habilitado apenas quando a opção Compra a Fixar desta aba estiver selecionada no campo Tipo de Contrato. 

Já no campo **"Valor Negociado/SC"** insira o valor negociado por saca do produto. Esse campo ficará desabilitado para edição quando a opção Compra a Fixar estiver selecionada no campo Tipo de Contrato. 

O valor inserido no campo **"Valor Total Negociado"** será calculado da seguinte maneira:

```
 Quantidade Negociada x (Valor Negociado/SC / Unidade de Conversão p/ SC)
```

Informe a data de início e final da entrega nos campos **"Data Início da Entrega"** e **"Data Final da Entrega"**, respectivamente.

Em **"% Tolerância Excedente"** indique a tolerância aceitável para exceder a quantidade do contrato, seja esta na compra ou na venda.

Caso queira que na pesagem não seja exigido o pedido, desabilite a marcação **"Exige Pedido na Pesagem"** que por padrão é habilitada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#top)

### Aba Serviços

Nesta aba, são apresentadas as seguintes sub-abas para configuração:

#### Sub-aba Expedição/Recepção

#### ![Imagem 10: Sub-aba Expedição/Recepção](https://ajuda.sankhya.com.br/hc/article_attachments/42313208110231)

Defina o **"Tipo de Cobrança"** de acordo com as opções:

- Por valor;
- Percentual;
- Isento.

**Observação:** ao selecionar a opção Isento, todos os demais campos desta sub-aba serão desabilitados para edição.

Configure o **"Tipo de Apuração por Percentual"** conforme as opções:

- **Estoque:** por meio dessa opção, a retenção irá ocorrer em uma apuração posterior à entrada das notas, conforme definido no campo **"Percentual (%)"** da tela [Tabela de Preços por Umidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595234), deduzindo a quantidade retida do saldo disponível no momento;
- **Serviço:** se selecionada essa opção, a retenção será realizada diretamente na pesagem, seguindo o campo Percentual (%) da tela Tabela de Preços por Umidade, porém, de forma a considerar a quantidade retida na entrada do romaneio no estoque.

A **"Tabela de Preços por Umidade"** é destinada à informação da tabela de preços por umidade, sendo que, deverão ser cadastradas previamente na tela [Tabela de Preços Por Umidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595234-Tabela-de-Pre%C3%A7os-por-Umidade).

No campo **"Periodicidade de Cobrança"** temos as opções abaixo:

- **Quinzenal:** 1º ao 15º dia e 16º ao último dia do mês, com apuração nos dias 16 e 1, respectivamente;
- **Mensal:** 1º ao último dia do mês, com apuração no dia 1 do mês subsequente;
- **Final do Contrato:** após finalizar as movimentações do contrato.

Os campos **"Centro de Resultado"** e **"Natureza"** são padrões de classificação do sistema e deverão ser utilizados no Cabeçalho das Notas de Faturamento de Serviço.

Os campos **"Tipo de título"** e **"Tipo negociação"** irão listar os tipos de títulos e tipos de negociação cadastrados no sistema e deverão ser utilizados no Cabeçalho das Notas de Faturamento de Serviço.

No campo **"Serviço"**, informe o serviço que será utilizado no faturamento das notas de Expedição/Recepção.

A marcação **"Apurar por peso líquido"** indica se a apuração dos serviços deverá ser feita sobre o peso líquido (antes da aplicação dos descontos do laudo de classificação) ou sobre o peso corrigido apurado (considerando os descontos do laudo de classificação).

#### Sub-aba Armazenagem

![Imagem 11: Sub-aba Armazenagem](https://ajuda.sankhya.com.br/hc/article_attachments/13148144156055)

O campo **"Tipo de Cobrança"** possui as seguintes opções:

- **Isento:** selecionando essa opção todos os demais campos desta sub-aba serão desabilitados para edição.
- **Sobre o saldo:** indicando essa opção a **"Periodicidade de Cobrança"** só poderá ser **"Quinzenal"** ou **"Mensal"**.
- **Sobre a entrada:** quando essa opção for escolhida, desabilitará o campo **"Períodos de Carência"**.

No campo **Periodicidade de Cobrança**, selecione o intervalo para a geração das cobranças:

- **Quinzenal:** a apuração ocorre no dia 16 (referente ao período do dia 1º ao 15) e no dia 1º (referente ao período do dia 16 ao último dia do mês). Ao selecionar esta opção, defina o comportamento da data projetada:

  - **A partir da Data de Entrada (Padrão):** a contagem considera dias corridos a partir da entrada.

    - Exemplo: Entrada em 10/01 com 2 períodos de carência; a cobrança inicia em 10/02.
  - **A partir do Início do Período de Cobrança:** a contagem inicia a partir do primeiro dia do período vigente.

    - Exemplo: Entrada em 10/01 com 2 períodos de carência; a cobrança inicia em 01/02.
- **Mensal:** apuração do 1º ao último dia do mês, com processamento no dia 1º do mês subsequente.
- **Final do Contrato:** a cobrança ocorre apenas após a finalização de todas as movimentações previstas.

No campo **"Períodos de Carência"** informe o período de carência a ser considerado no cálculo da cobrança de armazenagem.

Os campos **"Centro de Resultado"** e **"Natureza"** são padrões de classificação do sistema e deverão ser utilizados no Cabeçalho das Notas de Faturamento de Serviço.

Os campos **"Tipo de título"** e **"Tipo negociação"** irão listar os tipos de títulos e tipos de negociação cadastrados no sistema e deverão ser utilizados no Cabeçalho das Notas de Faturamento de Serviço.

A marcação **"Apurar por peso líquido"** indica se a apuração dos serviços deverá ser feita sobre o peso líquido (antes da aplicação dos descontos do laudo de classificação) ou sobre o peso corrigido apurado (considerando os descontos do laudo de classificação).

Na parte inferior dessa sub-aba, tem-se os campos:

![Imagem 12: Na parte inferior dessa sub-aba, tem-se os campos:](https://ajuda.sankhya.com.br/hc/article_attachments/20150083383063)

No campo **"Referência"** informe a data de referência que equivale o preço a ser considerado;

Defina no campo **"Valor"** o preço por SC a ser cobrado a título de serviço de armazenagem;

No campo **"Serviço"** serão listados os serviços que poderão ser utilizados no faturamento das notas de armazenagem.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#top)

### Botão Outras Opções...

Por meio do botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992659932183) **"Outras Opções..."**, localizado no topo da tela pode-se:

#### Gerar Pedido de Armazenagem

Esta opção permite gerar o pedido de armazenagem a partir do Contrato de Armazenagem. Ao acionar a opção, será aberto o pop-up abaixo:

![Imagem 14: Esta opção permite gerar o pedido de armazenagem a partir do Contrato de Armazenagem . Ao acionar a opção, será aberto…](https://ajuda.sankhya.com.br/hc/article_attachments/13161101347735)

Preenchendo as informações do pop-up, pode-se gerar o pedido de armazenagem para que ele seja lançado no [Portal Armazéns](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049698494-Portal-Armaz%C3%A9ns) com as respectivas informações.

#### Gerar Pedido de Compra

Essa opção poderá ser acionada quando a opção Compra Fixada ou Compra a Fixar do campo Tipo de Contrato da aba Comercialização for definida. 

![Imagem 15: Essa opção poderá ser acionada quando a opção Compra Fixada ou Compra a Fixar do campo Tipo de Contrato da aba…](https://ajuda.sankhya.com.br/hc/article_attachments/13160937486487)

Desse modo, ao selecioná-la, o pop-up **"Gerar Pedido de Compra"** será exibido na tela. Este possui os seguintes campos:

No **"Tipo Operação"**, você poderá selecionar as TOP's ativas que estejam configuradas com o **"Tipo de Movimento"** como **"O - Pedido de Compra"** e o campo **"Movimento Armazém"** da aba [Armazéns](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaarmaz%C3%A9ns) definido com a opção **"Compra"**.

Pode-se definir também a **"Série"**, a **"Data de Emissão"** e o **"Local"** do pedido.

O campo **"Quantidade"** trará a mesma informação do campo **"Quantidade negociada"** da aba Comercialização.

Em **"Valor Unitário"**, caso o contrato seja do tipo Compra Fixada, o valor exibido será o resultante do seguinte cálculo do contrato:

```
 Valor Total Negociado/SC / Unidade de Conversão p/SC
```

Porém, caso o contrato esteja contextualizado com a opção **"Compra a Fixar"** do campo Tipo de Contrato definida, este campo será calculado dividindo o valor mais recente cadastrado na moeda vinculada ao campo Preço de Pauta/SC pelo valor do campo Unidade de Conversão p/SC do contrato.

Assim, ao clicar no botão **"Ok"**, o documento será gerado com as informações do contrato e aquelas definidas no pop-up dito acima.

#### Gerar Pedido de Venda

A opção **"Gerar Pedido de Venda"** poderá ser utilizada da mesma forma que a opção Gerar Pedido de Compra, porém apenas para os contratos de comercialização que utilizam a opção **"Venda Fixada"** do campo Tipo de Contrato configurada.  

Portanto, ao selecioná-la, o pop-up **"Gerar Pedido de Venda"** será exibido na tela. Este possui as seguintes opções:

![Imagem 16: Portanto, ao selecioná-la, o pop-up "Gerar Pedido de Venda" será exibido na tela. Este possui as seguintes opções:](https://ajuda.sankhya.com.br/hc/article_attachments/13161089809047)

No **"Tipo Operação"**, você poderá selecionar as TOP's ativas que estejam configuradas com o **"Tipo de Movimento"** como **"P - Pedido de Venda"** e o campo **"Movimento Armazém"** da aba [Armazéns](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaarmaz%C3%A9ns) definido com a opção **"Venda"**.

Pode-se definir também a **"Série"**, a **"Data de Emissão"** e o **"Local"** do pedido.

O campo **"Quantidade"** trará a mesma informação do campo **"Quantidade negociada"** da aba Comercialização.

Em **"Valor Unitário"**, caso o contrato seja do tipo Venda Fixada, o valor do contrato a ser exibido será o resultado do cálculo:

```
 Valor Total Negociado/SC / Unidade de Conversão p/SC
```

Assim, quando você clicar no botão  **"Ok"**, o documento será gerado com as informações do contrato e aquelas definidas no pop-up dito acima.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#top)

### Botão Edição múltipla

O botão ![Edição](https://ajuda.sankhya.com.br/hc/article_attachments/15992583560855) **"Edição múltipla"** permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão, será possível editar os campos correspondentes de todos os registros de uma só vez. 

Por exemplo, com os contratos em modo grade na tela Contratos de Armazéns de Grãos selecione-os e em seguida clique no botão Edição Múltipla, assim os campos poderão ser editados simultaneamente para todos os selecionados. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os#top)
