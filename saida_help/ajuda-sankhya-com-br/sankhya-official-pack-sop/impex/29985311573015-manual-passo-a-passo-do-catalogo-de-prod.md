---
id: "29985311573015"
titulo: "Manual passo a passo do catálogo de produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29985311573015-Manual-passo-a-passo-do-cat%C3%A1logo-de-produtos"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:36:42Z"
rotulos: ["Configuração", "br.com.sankhya.core.cad.produtos", "Financeiro", "br.com.sankhya.comercioexterior.exp.puComexCon", "Manual passo a passo do catálogo de produtos", "SISCOMEX", "PUCOMEX", "Portal Único", "Catálogo de Produtos"]
---

# Manual passo a passo do catálogo de produtos

### Configuração PUCOMEX

A configuração de PUCOMEX e necessária para o sistema criar o Tolkien de validação para o sistema realizar a integração com o portal único do Siscomex.

Acesse a tela **"Configuração PUCOMEX"** (ImpEx » Rotinas » Configuração PUCOMEX), clique em incluir e preencha os seguintes campos:

(1)** Empresa:** coloque a empresa que o certificado e os dados pertence.

(1)** Perfil:** para o catálogo de produtos e necessário ser Terceiros (Outros Intervenientes)

- Operador Portuário
- Responsável Legal OE
- Terceiros (Outros Intervenientes)
- PF - Representante de TETI
- Transportador
- Instituição Financeira
- Declarante importador/exportador
- Habilitador
- Depositário
- Ponto de Contato OEA
- Ajudante de Despachante
- Agente de Carga
- Remessa Expressa/Correio

(1)** URL:** campo URL para inserir o endereço do endpoint do serviço do portal siscomex. É o "endereço" para onde as requisições de integração serão enviadas.

(1)** X-CSRF-Expiration:** campo relacionado a tokens de segurança e pode indicar o prazo de expiração para o token CSRF (Cross-Site Request Forgery), um mecanismo de segurança para prevenir ataques.

**(1)** **X-CSRF-Token:** campo para armazenar ou exibir o token CSRF em si. Este token é vital para a segurança das requisições, garantindo que elas venham de uma fonte legítima.

(1)** Set-Token:** campo para armazenamento de um token de sessão ou de acesso que será utilizado para autenticar as requisições do Sankhya junto ao portal sicomex.

(1)** Certificado Digital:** neste campo será feito upload do arquivo do certificado digital (por exemplo, .pfx ou .p12) que será usado para estabelecer uma conexão segura e autenticada.

- Para o catálogo de produtos, só é aceito certificado digital de pessoa física (e-CPF), conforme documentação do portal único do siscomex. E a pessoa já tem que estar cadastrada e vinculada no portal único do siscomex.

(1)** Senha:** campo para inserir a senha de proteção do Certificado Digital. É crucial para que o sistema possa acessar e utilizar o certificado.

![Imagem 1: (1) Senha: campo para inserir a senha de proteção do Certificado Digital. É crucial para que o sistema possa acessar e…](https://ajuda.sankhya.com.br/hc/article_attachments/29985599705495)

Após cadastrar as configurações de PUCOMEX para cada empresa é necessário autenticar a mesma, através do botão **“Autenticar PUCOMEX”**

![Imagem 2: Após cadastrar as configurações de PUCOMEX para cada empresa é necessário autenticar a mesma, através do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/29985599706007)

### Cadastro de Atributos

No cadastro de atributos, crie os atributos que serão vinculados aos produtos a serem enviados para o catálogo de produtos conforme a tabela do portal único do siscomex.

Para cadastrar um atributo, clique em incluir e preencha os seguintes campos:

- **Ativo**: sinaliza se o atributo estar ativo ou não;
- **Atributo Condicionante:** sinaliza se esse atributo é uma condicionante para outros atributos;
- **Data de Alteração:** fica registrada quando houver alguma alteração no cadastro desse atributo;
- **Cód. Usuário Alteração:** ficar registrado o usuário que realizou a alteração no atributo;
- **NCM:** cite a qual NCM esse atributo é vinculado;
- **Código do Atributo:** inclua o código de atributos conforme a tabela disponível no portal único do Siscomex;
- **Descrição do Atributo:** coloque a descrição desse atributo, conforme a tabela do portal único do Siscomex;
- **Modalidade:** escolha se o atributo é para Importação ou Exportação conforme a tabela do portal único do Siscomex;
- **Orgãos:** informe o órgão que realiza a fiscalização desse atributo.
- **Data Inicio da vigência:** informe a data inicial da vigência do atributo conforme a tabela do portal único do Siscomex;
- **Data Final da vigência:** informe a data fim da Vigência do atributo conforme a tabela do portal único do Siscomex.

![Imagem 3: Data Final da vigência: informe a data fim da Vigência do atributo conforme a tabela do portal único do Siscomex.](https://ajuda.sankhya.com.br/hc/article_attachments/29987305937559)

### Operador Logístico

No cadastro de parceiros, preencha as informações de Operador logístico na aba **“Operador Estrangeiro”.** Para tal, clique em incluir e preencha os campos abaixo:

- **Empresa:** a qual esse parceiro é vinculado como Operador logístico;
- **Cód. País:** informe o país que o operador logístico pertence;
- **Número de identificação (TIN):** coloque o código TIN conforme o país do operador logístico;
- **E-mail:** cadastre o e-mail do operador logístico;
- **Código interno:** informe o código interno do operador logístico;
- **Código postal:** cadastre o código postal do operador logístico, conforme as regras do país que o mesmo pertence;
- **Logradouro:** coloque o logradouro do operador logístico;
- **Cidade:** vincule o operador logístico a cidade que o mesmo pertence;
- **Número:** coloque o número conforme o endereço do operador logístico;
- **Agência Emissora:** insira a agência emissora o operador logístico participa.

![Imagem 4: Agência Emissora: insira a agência emissora o operador logístico participa.](https://ajuda.sankhya.com.br/hc/article_attachments/29988409920023)

### Catálogo de Produtos

Na aba **"Catálogo de produtos"**, inclua os dados e os atributos necessários para o mesmo conforme a tabela estabelecida do Portal Único do Siscomex. Nesta aba também é possível acompanhar e fazer a manutenção do catálogo de produtos, bem como enviar para ser integrado.

Clique em inserir para configurar o produto para ser enviado para o catálogo de produtos:

- **Empresa:** inclua em qual empresa esse produto pertence para o catálogo de produtos.

#### Aba Geral

- **Sequência:** será demonstrada a sequência das configurações de catálogo de produtos;
- **Situação:** será demonstrado se essa configuração está ativa ou inativa;
- **Modalidade de Operação:** sinaliza se esse produto vai ser utilizado em importação ou exportação;
- **NCM:** será indicado qual NCM vai ser utilizado para o catálogo de produtos;
- **Código Interno do Produto:** será colocado qual o código interno que será utilizado para o catálogo de produtos;
- **Operador Logístico:** indica qual operador logístico é responsável por esses produtos. O parceiro deve estar pré-configurado conforme o item Operador Logístico deste manual;
- **Descrição do produto:** indica qual descrição será levada para o catálogo de produtos;
- **Detalhamento Complementar do Produto:** coloque o detalhamento complementar do produto para ser enviado para o catálogo de produtos;
- **Última versão:** sinalize que esse registro é a última versão enviada;
- **Versão:** demonstre a versão que esse produto está no catálogo de produtos;
- **Sincronizado:** apresenta se esse produto já foi sincronizado ou não no catálogo de produto do portal único do Siscomex.

![Imagem 5: Sincronizado: apresenta se esse produto já foi sincronizado ou não no catálogo de produto do portal único do Siscomex.](https://ajuda.sankhya.com.br/hc/article_attachments/29988409922327)

Ao acessar a aba **"Previa de Parcelas**", será possível ver todas as parcelas geradas pelos contratos cambias. Essas parcelas serão geradas automaticamente na **"Movimentação Financeira"**, como **"Provisões".** Para o financeiro ter no fluxo a previsibilidade do pagamento das parcelas do contrato cambial.

![Imagem 6: Ao acessar a aba "Previa de Parcelas ", será possível ver todas as parcelas geradas pelos contratos cambias. Essas…](https://ajuda.sankhya.com.br/hc/article_attachments/29988394310039)

Para **transformar uma prévia de parcela em financeiro Real**, selecione as parcelas que deseja atualizar e acesse o botação de ação **"Confirmar Financeiro"**. O sistema irá transformar a prévia do financeiro em um financeiro "Real", no qual o mesmo entra no fluxo de caixa real da empresa para pagamento.

![Imagem 7: Para transformar uma prévia de parcela em financeiro Real , selecione as parcelas que deseja atualizar e acesse o…](https://ajuda.sankhya.com.br/hc/article_attachments/29988394311191)

Após clicar na opção **"Confirmar Financeiro"**, o sistema apresentará a mensagem abaixo, indicando quantas parcelas foram atualizadas no financeiro.

![Imagem 8: Após clicar na opção "Confirmar Financeiro" , o sistema apresentará a mensagem abaixo, indicando quantas parcelas foram…](https://ajuda.sankhya.com.br/hc/article_attachments/29988409924503)

Antes de **"Gerar o Financeiro"** das prévias das parcelas é possível realizar algumas alterações, para serem atualizadas na transformação do financeiro provisão para financeiro real. São elas:

- **Marcar que o Financeiro se trata de um adiantamento:** com isso, o sistema além de atualizar a Despesa da provisão, também criará uma Receita, para que a mesma possa ser utilizada posteriormente na compensação financeira, para fechamento do contrato cambial e calculo da variação cambial.

![Imagem 9: Marcar que o Financeiro se trata de um adiantamento: com isso, o sistema além de atualizar a Despesa da provisão,…](https://ajuda.sankhya.com.br/hc/article_attachments/29988540341399)

- **Atualizar o valor da cotação da moeda da parcela em questão:** utilizando o campo **"Vlr. Cotação Atualizada”** o usuário consegue colocar qual valor da cotação de moeda deve ser atualizada na movimentação financeira.

![Imagem 10: Atualizar o valor da cotação da moeda da parcela em questão: utilizando o campo "Vlr. Cotação Atualizada” o usuário…](https://ajuda.sankhya.com.br/hc/article_attachments/29988524742039)

- **Atualizar a data de vencimento da parcela do contrato:** é possível preencher uma nova data de vencimento no campo **"Dt. Vencimento"**, para o sistema atualizar na movimentação financeira a data de vencimento da movimentação financeira.

![Imagem 11: Atualizar a data de vencimento da parcela do contrato: é possível preencher uma nova data de vencimento no campo "Dt.…](https://ajuda.sankhya.com.br/hc/article_attachments/29988524744215)

- É possível através do botão **“Mov. Financeira”**, selecionar a parcela e abrir diretamente a movimentação financeira.

![Imagem 12: É possível através do botão “Mov. Financeira” , selecionar a parcela e abrir diretamente a movimentação financeira.](https://ajuda.sankhya.com.br/hc/article_attachments/29988915561879)

Na aba **"Financeiro"**, o sistema apresenta os principais dados das movimentações financeiras das parcelas do contrato. Para que o usuário não necessite fazer o acesso à tela de movimentação financeira.

![Imagem 13: Na aba "Financeiro" , o sistema apresenta os principais dados das movimentações financeiras das parcelas do contrato.…](https://ajuda.sankhya.com.br/hc/article_attachments/29988899593367)

### Aba Despesas Bancárias

Na aba **"Despesas Bancárias"**, pode-se incluir as despesas bancárias, por parcela, que podem incorrer. Os campos que devem ser preenchidos são:

- **Histórico**
- **Cód. Parceiro Banqueiro**
- **TOP**
- **Cód. Conta**
- **Dt. Neg**
- **Vlr. Despesa Banqueiro**
- **Cód. Natureza**
- **Dt. Vencimento**

![Imagem 14: Dt. Vencimento](https://ajuda.sankhya.com.br/hc/article_attachments/29988899599255)

### Confirmar Financeiros

Selecione todos os contratos que deseja confirmar o financeiro e clique no botão **“Confirmar Financeiros”:**

![Imagem 15: Selecione todos os contratos que deseja confirmar o financeiro e clique no botão “Confirmar Financeiros”:](https://ajuda.sankhya.com.br/hc/article_attachments/29988899602199)

### Campos de Controle do Contrato

Na aba **"Geral"** dos Contrato Cambais, existem certos campos pelos quais é possível avaliar alguns pontos, como valor do contrato em aberto, valor do contrato em reais, entre outros. 
Segue a relação desses campos:

#### Vlr em Moeda Corrente

Nesse campo o sistema apresenta o valor do contrato em R$.

![Imagem 16: Nesse campo o sistema apresenta o valor do contrato em R$.](https://ajuda.sankhya.com.br/hc/article_attachments/29988915573015)

#### Saldo Aberto Moeda

Neste campo o sistema apresenta o valor em aberto do contrato em Moeda, ou seja, o valor do contrato menos as parcelas que já foram baixadas.

![Imagem 17: Neste campo o sistema apresenta o valor em aberto do contrato em Moeda, ou seja, o valor do contrato menos as parcelas…](https://ajuda.sankhya.com.br/hc/article_attachments/29988915575191)

#### Saldo Aberto Moeda Corrente

Neste campo o sistema apresenta o valor em aberto do contrato em moeda corrente, ou seja, ele apresenta o valor em aberto do contrato em R$.

![Imagem 18: Neste campo o sistema apresenta o valor em aberto do contrato em moeda corrente, ou seja, ele apresenta o valor em…](https://ajuda.sankhya.com.br/hc/article_attachments/29988915577111)
