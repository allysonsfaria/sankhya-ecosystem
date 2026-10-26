---
id: "5152321106583"
titulo: "Instalação do Sankhya Checkout"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5152321106583-Instala%C3%A7%C3%A3o-do-Sankhya-Checkout"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:18:05Z"
rotulos: ["Configuração", "PDV", "NFC-e", "Sankhya Checkout", "SAT", "Sistema PDV OFF-LINE emissão de NFC-e e CF-e/SAT sem necessidade de ERP", "Instalação integração com ERP e ajustes de impressoras e SAT", "Hardware software backup e configuração do ERP", "Instalação", "CF-e"]
---

# Instalação do Sankhya Checkout

### ![Imagem 1: Instalação do Sankhya Checkout](https://ajuda.sankhya.com.br/hc/article_attachments/16361880772759) Instalação do Sankhya Checkout

O Sankhya Checkout - Sistema de Automação Comercial é uma plataforma de Ponto de Venda (PDV) **OFF-LINE** ou seja independente de conexão com SEFAZ (Contingência Offline) e ERP ele está apto para realizar a emissão de documentos fiscais, do tipo Notas Fiscais Eletrônica(NFC-e) e Cupom Fiscal Eletrônico(CF-e)/SAT. 

O Sankhya Checkout após ser preparado e receber sua carga de atualizações de dados do ERP Sankhya, possuirá independência da base de dados do ERP para a realização de vendas.

O Sistema trabalha com Tabela de Preços única, produtos com código de barras, formas de pagamentos restritas a dinheiro, cartões de crédito/Débito e cartões POS, que é o mais indicado para estabelecimentos varejistas.

A versão inicial do sistema **não** irá atender as seguintes características de negócio atendidas pelo Fast Service:

- Análises por tipo de negociação das vendas do checkout no ERP.
- Vendas com KIT.
- Controles de crédito.
- Cartão/Voucher presente.
- Controles adicionais de estoque para Venda.
- Liberações por limite.
- Controle de estoque no PDV.
- Controle financeiro no PDV. “Tela de movimentação Financeira”.
- Instalação compartilhada em TS.
- Tela concomitante de botões.
- Pesquisa sofisticada de produtos Exemplo: “Ctrl-P, Ctrl-Q” do Fast Service.
- Ficha de Parceiros.
- Vendas com CUPOM FISCAL - PAF-ECF.
- Cálculo de Juros.

#### 1.1 Recomendações de Hardware

As configurações recomendadas de hardware para performance adequada, segue os mesmos padrões estabelecidos e exigidos na contratação.

- Resolução de monitor mínima em 1024x768(pixels).
- Memória RAM 6GB.
- HD SSD com mínimo de 250GB.
- Portas USB 3.0 ou superior.
- Pastas do checkout e TEF nas exceções do AntiVirus.
- Aplicação do Checkout liberada como segura no Windows defender.

#### 1.2 Recomendações de Software

- Sankhya-W 3.30.
- Jiva-W 3.30.

#### 1.3 Download e Atualizações

Acesse o endereço: [Download Checkout](http://downloads.sankhya.com.br/downloads?app=Checkout) e faça o download do pacote mais atualizado possível do ERP.

#### 1.4 Recomendações de rotinas de Backup

- Crie uma rotina e use softwares próprios para fazer backup da pasta do aplicativo e salvar em outro hardware. 
  - Exemplo de softwares : Winrar, Winzip, 7zip

####

### ![Imagem 2: Configurações do ERP pré-instalação](https://ajuda.sankhya.com.br/hc/article_attachments/16362271024151) Configurações do ERP pré-instalação

#### 2.1 Modelos de Notas

Na tela de **"Modelos de Notas e Pedidos"**, defina as configurações para modelo de nota.

No Cadastro de Empresa (Caminho de acesso: Comercial >> Empresa), defina na aba **"Geral"** a NF Modelo, NF de Troca e NF Demonstração na seção de Notas de Modelo Checkout

#### 2.2 Modelos de Notas migração do Fast Service

As notas dos modelos existentes no Fast Service serão migradas, estes campos existentes no cadastro da Empresa de Modelo de Troca, de Nota e Demonstração serão populados automaticamente.

#### 2.3 Tutorial de instalação

Após download, localize o Instalador Sankhya Checkout no diretório escolhido ou no diretório padrão de downloads: 

“**C:\Users\<usuario>\Downloads**”

![Imagem 3: “ C:\Users\<usuario>\Downloads ”](https://ajuda.sankhya.com.br/hc/article_attachments/5152371854999)

Execute o arquivo e defina as preferências de diretório de instalação da forma que desejar. O Instalador do Checkout já trás um caminho recomendado “**C:\Program Files (x86)\Sankhya Checkout**”. Para alterar, escreva o novo caminho ou clique em procurar e selecionar a pasta desejada. Clique próximo.

![Imagem 4: Execute o arquivo e defina as preferências de diretório de instalação da forma que desejar. O Instalador do Checkout já…](https://ajuda.sankhya.com.br/hc/article_attachments/5152442633367)

Marque a opção **“Criar um ícone na área de trabalho”**. Clique Próximo.

![Imagem 5: Marque a opção “Criar um ícone na área de trabalho” . Clique Próximo.](https://ajuda.sankhya.com.br/hc/article_attachments/5152412246167)

Antes de iniciar definitivamente a instalação, verifique o resumo de dados relacionado às telas anteriores. Caso haja alguma alteração a ser feita, clique em Voltar e faça as devidas alterações. Para prosseguir clique em Instalar.

![Imagem 6: Antes de iniciar definitivamente a instalação, verifique o resumo de dados relacionado às telas anteriores. Caso haja…](https://ajuda.sankhya.com.br/hc/article_attachments/5152453833367)

Aguarde o término da instalação.

![Imagem 7: Aguarde o término da instalação.](https://ajuda.sankhya.com.br/hc/article_attachments/5152480815127)

Com a opção **“Iniciar o Checkout PDV**” marcada. Clique em Concluir e inicie a configurações de integração com o ERP.

![Imagem 8: Com a opção “Iniciar o Checkout PDV ” marcada. Clique em Concluir e inicie a configurações de integração com o ERP.](https://ajuda.sankhya.com.br/hc/article_attachments/5152718929175)

#### 2.4 Iniciando a Integração de dados com ERP

Conexão com o ERP.

![Imagem 9: Conexão com o ERP.](https://ajuda.sankhya.com.br/hc/article_attachments/5152850946839)

Nesta tela, informe o endereço IP do ERP, como no exemplo de preenchimento mostrado pelo campo Endereço. Os campos Usuário e Senha, devem ser preenchidos com usuário e senha válidos no ERP. Clique Próximo.

![Imagem 10: Nesta tela, informe o endereço IP do ERP, como no exemplo de preenchimento mostrado pelo campo Endereço. Os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/5152874927255)

Aguarde a conexão e downloads para prosseguir para o próximo passo de configurações.

#### 2.5 Configurações do Checkout

![Imagem 11: 2.5 Configurações do Checkout](https://ajuda.sankhya.com.br/hc/article_attachments/5152905162135)

Na tela de Cadastro de Checkout, pode ser definido as configurações básicas da estação. Defina Descrição, Empresa e Endereço IP.

O endereço IP do PDV são todos os hardwares de possível conexão com esta máquina, ou seja, conexão cabeada, wireless, hotspot - todas as conexões referentes a esta máquina serão listadas no campo IP. 

Quando marcado “Mostra imagem do produto”, o sistema irá buscar para a base local as imagens no cadastro de produto do ERP onde verificará se a imagem está no banco de dados ou apenas relacionada por um caminho, nessa segunda hipótese o caminho precisa estar acessível para o ERP. 

Quando marcado “Integrar Parceiro”, o sistema irá buscar para a base local todos os parceiros ativos do ERP para que se possa fazer venda identificada.

Nas abas abaixo, selecione o tipo de ambiente, o TEF. A seleção do tipo de ambiente, disponibiliza uma aba adjacente para configuração de Série.

![Imagem 12: Nas abas abaixo, selecione o tipo de ambiente, o TEF. A seleção do tipo de ambiente, disponibiliza uma aba adjacente…](https://ajuda.sankhya.com.br/hc/article_attachments/5153092625175)

O Id Token e Código de Segurança do Contribuinte (CSC) do ambiente de produção é coletado pelo Certificado (cert-sannfe.exp) que foi exportado através do SanNFE (Console NFe). 

No exemplo abaixo foi marcado a opção de Homologação, por isso foi necessário informar o Id Token e Código de CSC.

![Imagem 13: No exemplo abaixo foi marcado a opção de Homologação, por isso foi necessário informar o Id Token e Código de CSC.](https://ajuda.sankhya.com.br/hc/article_attachments/16363699928471)

O ambiente de Demonstração, está disponível apenas para apresentações comerciais da **Software House**, o movimento de venda realizado no PDV será possível integrar ao ERP mas não possuirá nenhum valor fiscal.

#### 2.6 Configurações de impressoras

![Imagem 14: 2.6 Configurações de impressoras](https://ajuda.sankhya.com.br/hc/article_attachments/16363701059735)

Faça as devidas configurações de impressora, após finalizar aguarde o término de sincronização de dados. Caso tenha deixado para “Sempre perguntar”, durante a venda toda impressora irá pedir para selecionar o aparelho de saída da impressão.

#### 2.7 Configurações SAT

![Imagem 15: 2.7 Configurações SAT](https://ajuda.sankhya.com.br/hc/article_attachments/5154499531543)

### Cadastro SAT

![Imagem 16: Cadastro SAT](https://ajuda.sankhya.com.br/hc/article_attachments/5154471060887)

Para Cupom Fiscal Eletrônico Sat as configurações de cadastro são similares às de impressora em relação a porta e compartilhamento. 

As configurações de Nro. Série e Código de Ativação são referentes ao registro do aparelho feito na SEFAZ.

Essa tela será apresentada se na tela inicial do PDV foi informado que usará SAT.

Após finalizar com sucesso, todas estas configurações ficarão salvas no ERP e serão passíveis de alteração quando estiver on-line com ERP. 

Para fazer, acesse com usuário que possua permissão para tais alterações.

O licenciamento do checkout passou a ser controlado pelo SAS assim elas precisam ser liberadas em no máximo 30 dias pelo implantador do ERP utilizando a tela de administração de Tasks.

#### 2.8 Configurações Gerais do Sankhya Checkout

[Configurações Gerais do Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/5155097417751-Configura%C3%A7%C3%B5es-Gerais-do-Sankhya-Checkout)

#### 2.9 Configurações Implantação do Sankhya Checkout

[Configurações Implantação do Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/5155887602583-Implanta%C3%A7%C3%A3o-Sankhya-Checkout)

#### 2.10 Configurações de Integração de dados do Checkout com o ERP

[Integração de dados do Sankhya Checkout com o ERP](https://ajuda.sankhya.com.br/hc/pt-br/articles/5219386455319-Integra%C3%A7%C3%A3o-de-dados-do-Sankhya-Checkout-com-o-ERP)

#### 2.11 Sistema de Autenticação e Transmissão de Cupons Fiscais Eletrônicos

[Sistema de Autenticação e Transmissão de Cupons Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/5219786026391--Sistema-de-Autentica%C3%A7%C3%A3o-e-Transmiss%C3%A3o-de-Cupons-Fiscais-Eletr%C3%B4nicos)
