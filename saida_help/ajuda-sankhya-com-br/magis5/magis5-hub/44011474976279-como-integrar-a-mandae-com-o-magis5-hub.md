---
id: "44011474976279"
titulo: "Como integrar a Mandaê com o Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011474976279-Como-integrar-a-Manda%C3%AA-com-o-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:04:45Z"
rotulos: ["sync_hc", "magis5", "magis5_204048108419", "sync_hash_40fab792c3b7"]
---

# Como integrar a Mandaê com o Magis5 Hub?

## Neste manual, iremos aprender a efetuar a integração com a logística Mandaê.

---

A Mandaê é uma empresa brasileira de logística que oferece soluções para coleta, armazenamento, empacotamento e entrega de produtos, especialmente para e-commerces e negócios que precisam de serviços de transporte eficientes.

Este manual é para clientes que já possuem uma conta na Mandaê. Caso ainda não possua, [clique aqui](https://www.mandae.com.br/quero-contratar/) para preencher o formulário de cadastro da Mandaê!

**Requisitos para começar**

- Para a integração da Mandaê em seu canal de venda, orientamos realizar com o auxílio do nosso time de **Suporte**, pois algumas informações será necessário buscar códigos via API.
  Por conta disso, [abra um chamado pelo chat](https://ajuda.magis5.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br) localizado no canto inferior direito do seu painel do Magis5 Hub ou pelo nosso [WhatsApp](https://wa.me/551191369439).

**Para essa integração, iremos dividir em 3 etapas:
[1) Cadastro de logísticas](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011474976279-Como-integrar-a-Manda%C3%AA-com-o-Magis5-Hub#cadastro-logisticas)
[2) Integração Mandaê x Magis5](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011474976279-Como-integrar-a-Manda%C3%AA-com-o-Magis5-Hub#integracao-mandae-magis5)
[3) Integração canais de venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011474976279-Como-integrar-a-Manda%C3%AA-com-o-Magis5-Hub#integracao-canais-venda)**

### 1) Cadastro de logísticas

Na primeira etapa, é necessário a criação no Magis5 Hub dos dois serviçoes de envio da Mandaê conhecidos como Econômico e Rápido.

Para isso, vá em **"Configurações" -> "Cadastros" -> clique em "Logísticas".**
![Imagem 1: Para isso, vá em "Configurações" -> "Cadastros" -> clique em "Logísticas". Ao acessar a tela, clique no botão 'Novo'…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-31-49-0368-PM.png?width=625&height=483&name=image-png-Feb-15-2024-12-31-49-0368-PM.png)
Ao acessar a tela, clique no botão**'Novo'**localizado abaixo da busca.

![Imagem 2: Para isso, vá em "Configurações" -> "Cadastros" -> clique em "Logísticas". Ao acessar a tela, clique no botão 'Novo'…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-34-43-5802-PM.png?width=405&height=210&name=image-png-Feb-15-2024-12-34-43-5802-PM.png)

Então, preencha os dados de todas as abas do cadastro.

⚠️ Lembrando que todos esse dados serão registrados na Nota Fiscal dos pedidos que tiverem esta logística informada.

**Geral**

![Imagem 3: Geral](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-36-05-7281-PM.png?width=688&height=144&name=image-png-Feb-15-2024-12-36-05-7281-PM.png)

Nesta aba, preencha os campos:

- **Nome da Transportadora:** Insira o nome de um dos serviços de envio da Mandaê. Exemplo: Mandaê Econômico.
- **CNPJ:**Insira o CNPJ sem os traços e barra que deseja ser inserido na seção de Transportadores da NF-e
- **Inscrição Estadual;**
- **Frete por conta:**Modalidades de frete padrão para esta transportadora sendo as opções:
  0 = Contratação do Frete por conta do Remetente (CIF);
  1 = Contratação do Frete por conta do Destinatário (FOB);
  2 = Contratação do Frete por conta de Terceiros;
  3 = Transporte Próprio por conta do Remetente;
  4 = Transporte Próprio por conta do Destinatário;
  9 = Sem Ocorrência de Transporte.

**Endereço**

Preencha todos os dados de endereço da transportadora nesta aba.

![Imagem 4: Preencha todos os dados de endereço da transportadora nesta aba.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-47-01-8545-PM.png?width=688&height=193&name=image-png-Feb-15-2024-12-47-01-8545-PM.png)

**Dados adicionais**

![Imagem 5: Dados adicionais](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-47-51-4820-PM.png?width=529&height=125&name=image-png-Feb-15-2024-12-47-51-4820-PM.png)

- **URL rastreio:**endereço do site utilizado para rastrear pedidos referente a esta transportadora;
- **E-mail para envio da NFe:**caso esta transportadora receba seus pedidos de envio por e-mail, informe em qual endereço de e-mail deverão ser enviados os dados dos pedidos e a Nota Fiscal anexada;

**Imagem logística**

![Imagem 6: Imagem logística](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-50-15-4166-PM.png?width=416&height=100&name=image-png-Feb-15-2024-12-50-15-4166-PM.png)

Nesta aba, insira a imagem que representa a logotipo da Mandaê.

O padrão da imagem deve ser:

- Formato .PNG
- Com fundo transparente
- Sem bordas

Finalize clicando em **Salvar.**

**Repita o processo acima, porém no campo de 'Nome da transportadora' insira o outro serviço de envio da Mandaê. Como no primeiro exemplo usamos  o método de envio 'Mandaê Econômico', o outro deverá ser criado com o nome 'Mandaê Rápido'.**

### 2) Integração Mandaê x Magis5 Hub

Na segunda etapa iremos integrar a Mandaê.
Para isso, na Mandaê vá em **"Configurações" -> "API"**e copie os 3 itens abaixo:

- **Token**
- **Customer ID**
- **Prefixo Rastreamento**

![Imagem 7: Prefixo Rastreamento](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Sep-03-2024-10-12-33-1077-PM.png?width=688&height=319&name=image-png-Sep-03-2024-10-12-33-1077-PM.png)

Agora no Magis5 Hub, vá em **"Configurações" -> "Integrações" -> clique em "Logísticas".**
![Imagem 8: Agora no Magis5 Hub, vá em "Configurações" -> "Integrações" -> clique em "Logísticas".](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-56-32-5666-PM.png?width=621&height=472&name=image-png-Feb-15-2024-12-56-32-5666-PM.png)

Clique em **'Novo'.**

![Imagem 9: Clique em 'Novo'.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-57-30-5962-PM.png?width=377&height=187&name=image-png-Feb-15-2024-12-57-30-5962-PM.png)

No campo Integração selecione 'Mandaê' e preencha os campos da aba **Geral** conforme abaixo:

![Imagem 10: No campo Integração selecione 'Mandaê' e preencha os campos da aba Geral conforme abaixo:](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Sep-03-2024-10-14-58-9705-PM.png?width=688&height=332&name=image-png-Sep-03-2024-10-14-58-9705-PM.png)

- **Descrição:** O nome da sua preferência (Ex: Mandaê ABC)
- **Usuário:** Cole o **Customer ID** que foi copiado no painel da Mandaê.
- **API Key:**Cole o **Token** que foi copiado no painel da Mandaê.
- **Prefixo Rastreamento:**Cole o **Prefixo Rastreamento** que foi copiado no painel da Mandaê.
- **Incluir valor do seguro:** Ative caso desejar que todos os pedidos de envio criados na Mandaê possuam seguro.

Na aba **Endereço remetente,** preencha com os dados do endereço de onde irão sair os pedidos embalados.

![Imagem 11: Na aba Endereço remetente, preencha com os dados do endereço de onde irão sair os pedidos embalados.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-12-59-39-3116-PM.png?width=688&height=225&name=image-png-Feb-15-2024-12-59-39-3116-PM.png)

Na aba **Imagem etiqueta,** insira a imagem que representa o logo da sua empresa. Ela será utilizada na geração da etiqueta.

![Imagem 12: Na aba Imagem etiqueta, insira a imagem que representa o logo da sua empresa. Ela será utilizada na geração da etiqueta.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-01-08-44-4682-PM.png?width=362&height=99&name=image-png-Feb-15-2024-01-08-44-4682-PM.png)

O padrão da imagem deve ser:

- Formato .PNG
- Com fundo transparente
- Sem bordas

**Ao terminar de preencher todos os campos, basta clicar em 'Salvar'.**

### 3) Integração canais de venda

Na última etapa, iremos vincular o canal de venda com a Mandaê para as cotações de frete e geração de etiquetas. Para isso, no Magis5 Hub vá para **"Configurações"**, depois em **"Integrações"** e por último clique em **"Marketplaces"** **OU** **"Lojas Virtuais"**, dependendo da integração.

![Imagem 13: Na última etapa, iremos vincular o canal de venda com a Mandaê para as cotações de frete e geração de etiquetas. Para…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-01-12-34-1375-PM.png?width=625&height=468&name=image-png-Feb-15-2024-01-12-34-1375-PM.png)

Clique em **'Editar'** no canal de venda que deseja vincular a Mandaê.

![Imagem 14: Clique em 'Editar' no canal de venda que deseja vincular a Mandaê.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Sep-03-2024-10-28-29-6223-PM.png?width=688&height=74&name=image-png-Sep-03-2024-10-28-29-6223-PM.png)

Na aba de **Logística** preencha os campos conforme abaixo:

![Imagem 15: Na aba de Logística preencha os campos conforme abaixo:](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Sep-03-2024-10-30-01-7212-PM.png?width=688&height=328&name=image-png-Sep-03-2024-10-30-01-7212-PM.png)

- **Padrão:** Defina a **Integração Logística Mandaê** como a principal, pois não podem haver logísticas diferentes estando vinculadas a um mesmo canal simultaneamente;
- **Integração Logística:**Selecione a integração de logística Mandaê que você cadastrou anteriormente;

Em seguida, clique na aba de**"Envio"**e clique em "**Novo Método de envio"**e preencha os campos conforme abaixo:

![Imagem 16: Em seguida, clique na aba de "Envio" e clique em " Novo Método de envio" e preencha os campos conforme abaixo:](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-15-2024-01-18-48-6975-PM.png?width=688&height=175&name=image-png-Feb-15-2024-01-18-48-6975-PM.png)

- **Nome da transportadora:**Insira exatamente o nome da transportadora que cadastrou na etapa 1.
- **ID do método de envio:**Insira 'Econômico' ou 'Rápido' com base no que preencheu no campo anterior.
  Exemplo: Se no campo anterior preencheu **Mandaê Rápido,** nesse preencha como **Rápido** e vice-versa.
- **Nome do método de envio no marketplace:**Insira o nome do método de envio que está vindo na API do canal de venda.
  - Nessa etapa orientamos entrar em contato com o nosso time de Suporte conforme mencionado nos [requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011474976279-Como-integrar-a-Manda%C3%AA-com-o-Magis5-Hub#requisitos).

Após estes, não é necessário preencher outros campos da aba Envio.
Feito o preenchimento de todos os campos indicados, finalize clicando no botão**'Salvar'**.

![Imagem 17: Após estes, não é necessário preencher outros campos da aba Envio. Feito o preenchimento de todos os campos indicados,…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Sep-04-2024-03-34-17-7876-PM.png?width=688&height=294&name=image-png-Sep-04-2024-03-34-17-7876-PM.png)

Pronto, sua integração está concluída!
Caso queira entender como será o fluxo para criação de pedidos de envio na Mandaê, [clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/44010891830935).
