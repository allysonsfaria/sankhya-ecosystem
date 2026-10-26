---
id: "30446587263767"
titulo: "Sankhya Tax - Parametrização para Integração NFSe (Captura e Integração de NFS-e de Serviços Tomados)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Sankhya-Tax-Parametriza%C3%A7%C3%A3o-para-Integra%C3%A7%C3%A3o-NFSe-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Sankhya TAX"
atualizado_em: "2026-10-13T15:40:40Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "API", "INTEGRAÇÃO", "SERVIÇOS TOMADOS", "NOTA MODELO", "ASIS", "NFS-E", "KOLOSSUS"]
---

# Sankhya Tax - Parametrização para Integração NFSe (Captura e Integração de NFS-e de Serviços Tomados)

```
 Módulo: Configurações > Rotinas     Versão disponível: A partir da 4.32
```

---

A **API de Importação de Notas Fiscais de Serviços Tomados** foi desenvolvida para **automatizar** o processo de importação de notas fiscais emitidas por fornecedores. Com essa integração, os dados fiscais são importados diretamente para o sistema de gestão, **eliminando a necessidade de inserção manual** e reduzindo erros.

O serviço ASIS captura as **Notas Fiscais de Serviços Tomados** e as envia para o **ERP Sankhya** de forma segura e eficiente.

#### Principais benefícios

- **Maior eficiência** na gestão de notas fiscais.
- **Redução de erros** causados por digitação manual.
- **Conformidade legal**, garantindo que os documentos sejam registrados corretamente.
- **Integração flexível**, permitindo adaptação a diferentes necessidades.
- **Escalabilidade**, acompanhando o crescimento da empresa.

#### Evita registros duplicados

Para garantir que cada documento seja registrado **apenas uma vez**, a API utiliza uma **chave única** formada pelos seguintes dados:

- **CNPJ do Prestador.**
- **Número da Nota.**
- **Número do RPS.**
- **Série da Nota.**
- **Data de Emissão.**

Essa estrutura impede inconsistências e duplicações, tornando o processo mais seguro e confiável.

| Como utilizar essa rotina? |
| --- |
| [Configurações ASIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Sankhya-Tax-Parametriza%C3%A7%C3%A3o-para-Integra%C3%A7%C3%A3o-NFSe-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados#Configura%C3%A7%C3%B5es) |
| [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Sankhya-Tax-Parametriza%C3%A7%C3%A3o-para-Integra%C3%A7%C3%A3o-NFSe-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados#NFS-e) |
| [A solução no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Sankhya-Tax-Parametriza%C3%A7%C3%A3o-para-Integra%C3%A7%C3%A3o-NFSe-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados#Asolu%C3%A7%C3%A3onoERPSankhya) |

---

### Configurações ASIS

As parametrizações iniciais acontecem por meio do Kolossus, na plataforma da ASIS.

Para configurar a integração NFS-e, siga estes passos:

- Acesse a opção **"Integração"** na sua **"Conta"** do Kolossus.
- Selecione a integração **Sankhya**.
- Preencha os campos de Autenticação e NFS-e, conforme descrito abaixo.

**Autenticação**

- **Token:** é necessário incluir o token na plataforma da ASIS. Para gerá-lo, acesse [Como realizar a autenticação](https://developers.asisprojetos.com.br/autenticacao.html) a e siga as instruções deste material.
- **Token Homologação:** este token é utilizado para a integração com o ambiente de homologação. Siga as mesmas orientações do material [Como realizar a autenticação](https://developers.asisprojetos.com.br/autenticacao.html).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Sankhya-Tax-Parametriza%C3%A7%C3%A3o-para-Integra%C3%A7%C3%A3o-NFSe-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados#top)

### NFS-e

Após a autenticação, o sistema passa para uma tela de configuração da integração. Para que a integração funcione corretamente, é necessário **inserir a Nota Modelo** correspondente a cada empresa que fará a escrituração automática. Isso permite que a **ASIS** capture e envie os dados para o ERP de forma íntegra e automatizada. Para preencher corretamente, utilize as informações abaixo:

**Nota Modelo**

A **Nota Modelo** é um agrupamento de informações presentes no cabeçalho da nota dentro do **Sankhya OM**. Esse atributo organiza os dados essenciais para que o sistema possa incluir o movimento no **ERP**, garantindo que o serviço reconheça:

- **Empresa.**
- **Tipo de operação.**
- **Tipo de negociação.**

**(1)** Demais informações fica a cargo de utilização do usuário, como Centro de Resultado, Natureza, entre outros.

Neste passo da **integração** você deve preencher o **CNPJ** e o **N.º Único** da Nota Modelo. Certifique-se de inserir **todos os CNPJs e seus respectivos n.º Únicos**.

O **n.º Único** pode ser localizado na tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/Modelo%20de%20Notas%20e%20Pedidos) dentro do **ERP Sankhya**.

![Imagem 1: A configuração da nota modelo, acontece dentro do ERP Sankhya. Para configurar um Modelo de Nota , consulte o artigo…](https://ajuda.sankhya.com.br/hc/article_attachments/30446587262615) A configuração da nota modelo, acontece dentro do ERP Sankhya. Para configurar um **Modelo de Nota**, consulte o artigo [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos).

**Integração Automática ASIS**

Após parametrizar as **Notas Modelo**, é necessário ativar a opção **"Integração Automática"** no Portal Kolossus.

- **Quando ativada**: todas as **NFS-e** capturadas pelo **Kolossus** serão **automaticamente enviadas** para o **ERP Sankhya**.
- **Quando desativada:** a integração **não ocorre** sem a intervenção manual.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Sankhya-Tax-Parametriza%C3%A7%C3%A3o-para-Integra%C3%A7%C3%A3o-NFSe-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados#top)

### A solução no ERP Sankhya

Para que a integração ocorra sem erros, é necessário algumas configurações prévias. São elas:

- **Modelo de Nota:** um por empresa contendo as informações minímas de "Empresa", "TOP" e "Tipo de Negociação".
- **Prestador:** o Parceiro precisa ter um CNPJ único, ou seja, o mesmo CNPJ não pode estar vinculado a mais de um parceiro. Além disso, o tipo de parceiro deve estar configurado como Fornecedor. Caso essas condições não sejam atendidas, a importação da NFS-e pode falhar. Por isso, é importante revisar e corrigir o cadastro antes de realizar a integração.
- **Serviço:** é necessário informar o código do serviço conforme a regra do município. Esse código pode ser baseado na Lei Complementar n° 116, que é uma lista federal de atividades de prestação de serviço, ou em um código específico definido pelo próprio município. Essa informação é essencial para a correta identificação do serviço a ser escriturado. Essa informação deve ser inserida no campo **"Tipo de Serviço"** do Cadastro do Serviço.

![Imagem 2: É importante garantir que não existam múltiplos serviços cadastrados com o mesmo item da lista da Lei Complementar n°…](https://ajuda.sankhya.com.br/hc/article_attachments/30446587262615) É importante garantir que não existam múltiplos serviços cadastrados com o mesmo item da lista da Lei Complementar n° 116, pois isso pode impedir o sistema de identificar corretamente qual serviço deve ser escriturado quando há duplicidade de código.

Ocorrendo a importação da NFS-e, os documentos podem ser acessados nas seguintes telas do **ERP Sankhya**:

**(1)** [**Portal de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras)

Se a importação for bem-sucedida, o documento aparecerá no **Portal de Compras** com o seguinte status:

- **Status da nota**: Pendente.
- **Coluna Confirmado**: Não (o que significa que ainda precisa ser confirmado).

Para finalizar a escrituração, é necessário abrir o documento, conferir as informações e confirmar a nota.

**(1)** [**Central de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)

Ao acessar a nota na **Central de Compras**, você encontrará no campo **Observação** uma identificação de que o documento foi **importado via API**.

![Imagem 3: Observações importantes:](https://ajuda.sankhya.com.br/hc/article_attachments/30446587262615) **Observações importantes:**

- Todas as **notas importadas via API** terão essa observação.
- Dentro do campo de observação, será exibida a seção **"Valores dos impostos retidos conforme análise ASIS"**, permitindo comparar os valores calculados na nota conforma a configuração do sistema com a análise tributária dos impostos realizada pela ASIS.

Após realizar as verificações e ajustes necessários, o documento pode ser confirmado para que a escrituração seja finalizada. Esse processo garante que todas as informações foram corretamente importadas e validadas, evitando, erros na contabilização e no cumprimento das obrigações fiscais. Uma vez confirmado, o documento segue para as próximas etapas dentro do ERP, permitindo sua utilização nos relatórios e demais processos financeiros da empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/30446587263767-Sankhya-Tax-Parametriza%C3%A7%C3%A3o-para-Integra%C3%A7%C3%A3o-NFSe-Captura-e-Integra%C3%A7%C3%A3o-de-NFS-e-de-Servi%C3%A7os-Tomados#top)
