---
id: "7405986347799"
titulo: "Configurações Para Emissão de NF Modelo 21 e 22"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7405986347799-Configura%C3%A7%C3%B5es-Para-Emiss%C3%A3o-de-NF-Modelo-21-e-22"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:13:31Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Impostos", "TOP", "Configurações para Emissão de NF Modelo 21 e 22: Detalhes Importantes", "Documentos Eletrônicos"]
---

# Configurações Para Emissão de NF Modelo 21 e 22

#### ![Imagem 1: Cadastro da empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16513427762071) Cadastro da empresa

No cadastro da Empresa (Caminho de acesso: Comercial > Preferência > Empresa > Aba Livros Fiscais > Nota Fiscal de Comunicação/Telecomunicação), preencha o campo **“FISTEL”**.

 

#### ![Imagem 2: Cadastro de parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16513436776215) Cadastro de parceiros

**(1)** Na tela de Parceiros, aba **"Fiscal"**, tem o campo **“Código de identificação do consumidor ou assinante”,** que determina o código que será usado para identificação do consumidor.

**(1)** Com esse campo, tem a marcação **“Utilizar o número do cadastro do parceiro?”**. Quando esse campo estiver **marcado**, o sistema utilizará o código Sankhya para identificar o consumidor. Se estiver **desmarcado**, o sistema irá ler o código informado no campo “Código de identificação do consumidor ou assinante”.

**(1)** Ainda na tela de **"Parceiros"**, aba **"Fiscal"**, informe o **“Tipo de cliente de serviços de comunicação”.** Escolha algum item constante na lista deste campo.

 

#### Imagem 3: Cadastro de produtos Cadastro de produtos

Na tela de **"Produtos"**, aba **"Geral"**, preencha o **“Tipo de Utilização”** do produto conforme a lista constante neste campo.

 

#### ![Imagem 4: Contratos - Campos a serem preenchidos quando o faturamento for feito através de contratos](https://ajuda.sankhya.com.br/hc/article_attachments/16517360937239) Contratos - Campos a serem preenchidos quando o faturamento for feito através de contratos

**(1)** Ligue o parâmetro **"UTILCAMPOCT"** para que os campos a seguir sejam disponibilizados na tela de Contratos.

**(1)** Na tela de **"Contratos"**, Produtos/Serviços, aba **"Geral"**, preencha o campo **“Quantidade de usuário/login”**.

**(1)** Preencha a aba **“Números dos Terminais Telefônicos”** e identifique qual deles é o principal, se houver mais de um. Se tiver somente um, marque este como principal.

**(1)** Preencha no campo **“Características de Serviço de Tele/Comunicação”** o código correspondente às características do serviço. Essas informações deverão ser previamente preenchidas na tela **“Características de Serviço de Tele/Comunicação”.**

**(1)** Preencha a tela Características de Serviço de Tele/Comunicação que possuem os seguintes campos:

**(2)** **Tipo Serviço Comunicação:** obrigatório

**(2)** **Tipo Meio:** obrigatório

**(2)** **Tipo Tecnologia:** obrigatório

**(2)** **Tipo Produto SCM:** Obrigatório se o Tipo Serviço Comunicação = SCM

**(2)** **Tipo Atendimento SCM:** Obrigatório se o Tipo Serviço Comunicação = SCM

**(2)** **Velocidade Contratada SCM:** Obrigatório se o Tipo Serviço Comunicação = SCM

#### ![Imagem 5: Emissão das notas fiscais modelo 21 e 22](https://ajuda.sankhya.com.br/hc/article_attachments/16518067874455) Emissão das notas fiscais modelo 21 e 22

**(1)** Cadastre uma TOP em que o Modelo do documento seja 21 ou 22.

**(1)** Os campos criados na tela de Contratos serão carregados na Central de Vendas, permitindo que o usuário altere as informações na central e emita as notas fiscais com as devidas alterações.

**(1)** Os campos **"FISTEL"** e **"Tipo de Cliente do Serviço de Comunicação"** serão carregados para o cabeçalho na Central de Vendas. O campo **"Tipo de Utilização"** será carregado para a grade de itens da Central de Vendas.

**(1)** O sistema calculará o MD5 (Message Digest 5) que é a autenticação digital da nota fiscal. O código será obtido pela aplicação do algoritmo MD5 (Message Digest 5), formado pelos seguintes dados dos documentos fiscais, na seguinte ordem:

- CNPJ ou CPF do destinatário ou do tomador do serviço;

- Número do documento fiscal;

- Valor total;

- Base de cálculo do ICMS;

- Valor do ICMS;

- Data de emissão;

- CNPJ do emitente do documento fiscal;

- É importante que todos os campos citados acima estejam preenchidos. Muitos deles serão utilizados na geração dos arquivos de remessa.

 

#### ![Imagem 6: Geração dos arquivos de remessa das notas fiscais modelo 21 e 22](https://ajuda.sankhya.com.br/hc/article_attachments/16518067875735) Geração dos arquivos de remessa das notas fiscais modelo 21 e 22

**(1)** Criou-se a tela **“Geração de Arquivos de Remessa NFST Modelo 21 e 22”.** Nela são apresentados os filtros de Empresa, Competência (mês que deseja gerar o arquivo), Finalidade (Normal ou Substituto). 

**(1)** Alguns campos desta tela são próprios para a geração de Nota Fiscal/Conta de Energia Elétrica, modelo 6. Exemplo: Classe de Consumo  e Grupo de Tensão. Como o sistema não emite esse modelo de nota, esses campos devem ser preenchidos com “zero”.

**(1)** Caso o período informado tenha mais de uma série de nota fiscal, será gerado um tipo de arquivo para cada arquivo.

**(1)** Ao preencher o filtro, realize o processamento da tela.

**(1)** Serão apresentados todos os dados conforme consta no Convênio ICMS 115/03.

Importante que se tenha atenção no Layout de envio, que se encontra na sessão [Anexo Unico](https://www.confaz.fazenda.gov.br/legislacao/convenios/2003/CV115_03), no final do convênio: 

 

#### ![Imagem 7: Fundos fust e funttel das notas fiscais modelo 21 e 22](https://ajuda.sankhya.com.br/hc/article_attachments/16518067877527) Fundos fust e funttel das notas fiscais modelo 21 e 22

**(1)** Na tela **"Preferências"** da Empresa, aba **"Livros Fiscais"**, preencha os campos relacionados às alíquotas de FUST e FUNTTEL.

**(1)** Atualmente, a lei 9.998 inciso IV no artigo 6º trata a alíquota de FUST como 1%.

**(1)** A Lei 10.052, inciso III no artigo 4º trata a alíquota de FUNTTEL como 0,5%.

**(1)** Na tela de **"Produtos",** foram criados dois campos “**Calcular FUST?”** e **“Calcular FUNTTEL?”**. Marque se o item em questão terá a incidência dessas contribuições.

**(1)** Na tela da **"TOP"**, aba **"Impostos"**, foram criados dois campos: **“Calcular FUST?”** e **“Calcular FUNTTEL?”**. Ambos terão o seguinte comportamento:

**(1)** **Usar do Cadastro de Produto**: quando selecionado, o sistema irá ler o cadastro de produto para decidir se irá calcular ou não.

**(1)** **Calcular**: quando selecionado, o sistema irá calcular para todos os itens usados com essa TOP, mesmo se o cadastro de produto estiver com a opção “calcular” desmarcada.

**(1)** **Não calcular**: quando selecionado, o sistema não irá efetuar o cálculo, mesmo se o cadastro de produto estiver com a opção “calcular” marcada.

**(1)** O cálculo é feito da seguinte forma:

[(Base de Cálculo - Descontos Concedidos) - Valor do ICMS do item - Valor do PIS do item - Valor da COFINS do item] x %contribuição

**(1)** Foram criados os campos na tabela de Itens dos portais (TGFITE) para identificar o cálculo das contribuições, BC FUST, Alíquota FUST, Valor FUST, BC FUNTTEL, Alíquota FUNTTEL, Valor FUNTTEL.
