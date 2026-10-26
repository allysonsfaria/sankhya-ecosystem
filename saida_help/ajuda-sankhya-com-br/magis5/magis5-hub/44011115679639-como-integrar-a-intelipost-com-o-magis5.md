---
id: "44011115679639"
titulo: "Como integrar a Intelipost com o Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011115679639-Como-integrar-a-Intelipost-com-o-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:56:01Z"
rotulos: ["sync_hc", "magis5", "magis5_204048115776", "sync_hash_0ee827bb9051"]
---

# Como integrar a Intelipost com o Magis5 Hub?

## Neste manual, iremos aprender a efetuar a integração com a logística Intelipost.

---

A Intelipost é uma plataforma de gestão de fretes (TMS), que possui conexão com transportadoras, proporcionando uma visão completa de entregas desde o cálculo do frete, gestão de despacho, rastreamento de entregas e serviços de consultoria logística.

**Requisitos para começar**

- Abra um chamado pela [Central de Ajuda](https://suporte.intelipost.com.br/servicedesk) para o time de **Suporte** da Intelipost solicitando a API Key da conta para integração com o Magis5 Hub.
- Para a integração da Intelipost em seu canal de venda, será necessário auxílio do nosso time de **Suporte** para inserir códigos via API. 
  Por conta disso, [abra um chamado pelo chat](https://ajuda.magis5.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br) localizado no canto inferior direito do seu painel do Magis5 Hub ou pelo nosso [WhatsApp](https://wa.me/551935321952).

**Para essa integração, iremos dividir em 3 etapas:
[1) Cadastro de logísticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011115679639-Como-integrar-a-Intelipost-com-o-Magis5-Hub#cadastro-logisticas)
[2) Integração Intelipost x Magis5](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011115679639-Como-integrar-a-Intelipost-com-o-Magis5-Hub#integracao-intelipost-magis5)
[3) Integração canais de venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011115679639-Como-integrar-a-Intelipost-com-o-Magis5-Hub#integracao-canais-venda)**

### 1) Cadastro de logísticas

Na primeira etapa, é necessário a criação no Magis5 Hub das transportadoras ativas que existem em seu painel da Intelipost que fica localizado em Transportadoras/Minhas Transportadoras.

![Imagem 1: Na primeira etapa, é necessário a criação no Magis5 Hub das transportadoras ativas que existem em seu painel da…](https://ajuda.sankhya.com.br/hc/article_attachments/44011142852375)

Certifique-se de que as transportadoras que você irá utilizar estejam **ativas** no painel da Intelipost. **Caso contrário, elas não são consideradas para a geração de cotação de frete.**

Agora, no Magis5 Hub, vá em **"Configurações" -> "Cadastros" -> clique em "Logísticas".**
![Imagem 2: Agora, no Magis5 Hub, vá em "Configurações" -> "Cadastros" -> clique em "Logísticas". Ao acessar a tela, clique no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011126005783)
Ao acessar a tela, clique no botão **'Novo'** localizado abaixo da busca.

![Imagem 3: Agora, no Magis5 Hub, vá em "Configurações" -> "Cadastros" -> clique em "Logísticas". Ao acessar a tela, clique no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011116038039)

Então, preencha os dados de todas as abas do cadastro.

⚠️ Lembrando que todos esse dados serão registrados na Nota Fiscal dos pedidos que tiverem esta logística informada.

**Geral**

![Imagem 4: Geral](https://ajuda.sankhya.com.br/hc/article_attachments/44011097096087)

Nesta aba, preencha os campos:

- **Nome da Transportadora:** Insira exatamente o nome da transportadora que aparece na coluna de 'Nome' do painel que aparece na Intelipost. Exemplo: Correios PAC.

![Imagem 5: Nome da Transportadora: Insira exatamente o nome da transportadora que aparece na coluna de 'Nome' do painel que…](https://ajuda.sankhya.com.br/hc/article_attachments/44011124350359)

- **CNPJ:** Insira o CNPJ sem os traços e barra que aparece na edição da transportadora cadastrada no painel da Intelipost.

![Imagem 6: CNPJ: Insira o CNPJ sem os traços e barra que aparece na edição da transportadora cadastrada no painel da Intelipost.](https://ajuda.sankhya.com.br/hc/article_attachments/44011116409239)

![Imagem 7: CNPJ: Insira o CNPJ sem os traços e barra que aparece na edição da transportadora cadastrada no painel da Intelipost.](https://ajuda.sankhya.com.br/hc/article_attachments/44011116527511)

Caso não tenha CNPJ no cadastro da transportadora na Intelipost, deixe o campo em branco.

- **Inscrição Estadual;**
- **Frete por conta:** Modalidades de frete padrão para esta transportadora sendo as opções:
  0 = Contratação do Frete por conta do Remetente (CIF);
  1 = Contratação do Frete por conta do Destinatário (FOB);
  2 = Contratação do Frete por conta de Terceiros;
  3 = Transporte Próprio por conta do Remetente;
  4 = Transporte Próprio por conta do Destinatário;
  9 = Sem Ocorrência de Transporte.

**Endereço**

Preencha todos os dados de endereço da transportadora nesta aba.

![Imagem 8: Preencha todos os dados de endereço da transportadora nesta aba.](https://ajuda.sankhya.com.br/hc/article_attachments/44011124709911)

**Dados adicionais**

![Imagem 9: Dados adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/44011116759063)

- **URL rastreio:** endereço do site utilizado para rastrear pedidos referente a esta transportadora;
- **E-mail para envio da NFe:** caso esta transportadora receba seus pedidos de envio por e-mail, informe em qual endereço de e-mail deverão ser enviados os dados dos pedidos e a Nota Fiscal anexada;

**Imagem logística**

![Imagem 10: Imagem logística](https://ajuda.sankhya.com.br/hc/article_attachments/44011126720407)

Nesta aba, insira a logo da transportadora em si. Por exemplo, caso a transportadora seja da JadLog, coloque a imagem que representa o logotipo da empresa JadLog.

O padrão da imagem deve ser:

- Formato .PNG
- Com fundo transparente
- Sem bordas

Finalize clicando em **Salvar.**

**Repita o processo acima para cada transportadora existente dentro do painel da Intelipost.**

### 2) Integração Intelipost x Magis5 Hub

Na segunda etapa iremos integrar a Intelipost. No Magis5 Hub, vá em **"Configurações" -> "Integrações" -> clique em "Logísticas".**
![Imagem 11: Na segunda etapa iremos integrar a Intelipost. No Magis5 Hub, vá em "Configurações" -> "Integrações" -> clique em…](https://ajuda.sankhya.com.br/hc/article_attachments/44011117018007)

Clique em **'Novo'.**

![Imagem 12: Clique em 'Novo'.](https://ajuda.sankhya.com.br/hc/article_attachments/44011159712407)

No campo Integração selecione 'Intelipost' e preencha os campos da aba **Geral** conforme abaixo:

![Imagem 13: No campo Integração selecione 'Intelipost' e preencha os campos da aba Geral conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44011126995351)

- **Descrição:** O nome da sua preferência (Ex: Intelipost ABC)
- **API Key:**Insira o código fornecido pela Intelipost, conforme informado no [requisito](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011115679639-Como-integrar-a-Intelipost-com-o-Magis5-Hub#requisito).

Na aba **Endereço remetente,** preencha com os dados do endereço de onde irão sair os pedidos embalados.

![Imagem 14: Na aba Endereço remetente, preencha com os dados do endereço de onde irão sair os pedidos embalados.](https://ajuda.sankhya.com.br/hc/article_attachments/44011098109591)

Se atente que o campo **CEP** precisa ser o mesmo que está cadastrado no centro de distribuição da Intelipost. Para fazer essa conferência, no painel da Intelipost, vá em **Configuração -> Centros de Distribuição,** copie o código do CEP e insira no Magis5 Hub sem o traço.

Aproveite para copiar a informação da coluna de **'Código'** enquanto ainda no painel de Centros de Distribuição da Intelipost. Utilizaremos este código mais tarde.

![Imagem 15: Aproveite para copiar a informação da coluna de 'Código' enquanto ainda no painel de Centros de Distribuição da…](https://ajuda.sankhya.com.br/hc/article_attachments/44011127172247)

Na aba **Imagem etiqueta,** insira a imagem que representa o logo da sua empresa. Ela será utilizada na geração da etiqueta.

![Imagem 16: Na aba Imagem etiqueta, insira a imagem que representa o logo da sua empresa. Ela será utilizada na geração da etiqueta.](https://ajuda.sankhya.com.br/hc/article_attachments/44011098286871)

O padrão da imagem deve ser:

- Formato .PNG
- Com fundo transparente
- Sem bordas

Ao terminar de preencher todos os campos, basta clicar em **'Salvar'**.

### 3) Integração canais de venda

Na última etapa, iremos vincular o canal de venda com a Intelipost para as cotações de frete e geração de etiquetas. Para isso, no Magis5 Hub vá para **"Configurações"**, depois em **"Integrações"** e por último clique em **"Marketplaces"** **OU** **"Lojas Virtuais"**, dependendo da integração.

![Imagem 17: Na última etapa, iremos vincular o canal de venda com a Intelipost para as cotações de frete e geração de etiquetas.…](https://ajuda.sankhya.com.br/hc/article_attachments/44011160160023)

Clique em **'Editar'** no canal de venda que deseja vincular a Intelipost.

![Imagem 18: Clique em 'Editar' no canal de venda que deseja vincular a Intelipost.](https://ajuda.sankhya.com.br/hc/article_attachments/44011098521239)

Na aba de **Logística** preencha os campos conforme abaixo:

![Imagem 19: Na aba de Logística preencha os campos conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44011127534615)

- **Padrão:** Defina a **Integração Logística Intelipost** como a principal, pois não podem haver logísticas diferentes estando vinculadas a um mesmo canal simultaneamente;
- **Integração Logística:**Selecione a integração de logística Intelipost que você cadastrou anteriormente;
- **Código do CD:** Insira o código que [copiou](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011115679639-Como-integrar-a-Intelipost-com-o-Magis5-Hub#codigo) do painel da Intelipost.

Em seguida, clique na aba de **"Envio"** e clique em "**Novo Método de envio".**

Nessa etapa será necessário entrar em contato com o nosso time de Suporte conforme mencionado nos [requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011115679639-Como-integrar-a-Intelipost-com-o-Magis5-Hub#requisito).

![Imagem 20: Nessa etapa será necessário entrar em contato com o nosso time de Suporte conforme mencionado nos requisitos .](https://ajuda.sankhya.com.br/hc/article_attachments/44011098679959)

Será necessário também verificar no [Painel de transportadoras da Intelipost](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011115679639-Como-integrar-a-Intelipost-com-o-Magis5-Hub#cadastro-logisticas) o ID da transportadora para o preenchimento do campo **ID do método de envio**.

![Imagem 21: Será necessário também verificar no Painel de transportadoras da Intelipost o ID da transportadora para o preenchimento…](https://ajuda.sankhya.com.br/hc/article_attachments/44011098738455)

Após estes, não e necessário preencher outros campos da aba Envio. Feito o preenchimento de todos os campos indicados, finalize clicando no botão **'Salvar'**. O preenchimento dos restantes será feito automaticamente pelo sistema por meio da API da Intelipost.

Para garantir a geração da pré-lista de postagem (PLP) e o retorno correto dos códigos de rastreio, a Magis5 agora utiliza o status **"Pronto para envio"** antes de **"Despachado"** ao processar pedidos.

Essa atualização visa otimizar a comunicação com a transportadora e evitar falhas na obtenção de informações de rastreamento.
