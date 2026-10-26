---
id: "40715992800279"
titulo: "Como funciona a geração do CIOT no Sankhya Log TMS?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40715992800279-Como-funciona-a-gera%C3%A7%C3%A3o-do-CIOT-no-Sankhya-Log-TMS"
trilha: "Sankhya Official Pack - SOP > TMS"
atualizado_em: "2026-08-25T13:25:56Z"
rotulos: ["Configuração", "CIOT", "Transporte", "CIOT no Sankhya Log TMS", "TAC TAC Equiparado e ETC", "Emissão obrigatória CIOT", "integração com a ANTT", "SOP TMS", "Código Identificador da Operação de Transporte", "Documentos Eletrônicos", "Sankhya Log TMS", "ANTT"]
---

# Como funciona a geração do CIOT no Sankhya Log TMS?

O **CIOT (Código Identificador da Operação de Transporte)** é um registro obrigatório que identifica operações de transporte rodoviário remunerado de cargas perante a **ANTT**. Ele reúne informações como contratante, transportador, origem, destino, valor do frete, tipo de operação e veículos utilizados.

A partir de **24/05/2026**, a emissão do CIOT passa a ser obrigatória para as categorias **TAC**, **TAC Equiparado** e **ETC**. A obrigatoriedade é dispensada apenas para operações com veículos não emplacados e transporte de cargas especiais, conforme a Portaria Suroc nº 6, de 23 de abril de 2026.

### O que é o CIOT e para que serve?

O CIOT cumpre as seguintes funções na operação de transporte:

- **Identificação da operação:** cada operação registrada recebe um código único;
- **Rastreabilidade:** permite acompanhar quem contratou, quem transportou e quais dados foram declarados;
- **Apoio à fiscalização:** auxilia na verificação da regularidade da operação;
- **Verificação do piso mínimo:** permite conferir se o frete declarado está compatível com as regras aplicáveis;
- **Segurança às partes:** contratante e transportador passam a ter um registro formal da operação.

### Quando é obrigatória a emissão do CIOT?

O CIOT é obrigatório para **todas as operações de transporte remunerado de cargas**. A emissão é dispensada apenas nos seguintes casos:

- Operações envolvendo **veículos não emplacados**;
- Transporte de **cargas especiais**, conforme a Portaria Suroc nº 6, de 23 de abril de 2026.

### Quem é responsável pela emissão do CIOT?

A responsabilidade pela emissão varia conforme o tipo de transportador que realiza a operação:

- **Transporte realizado por TAC ou TAC Equiparado:** a emissão é de responsabilidade de quem contratou o transporte. Em caso de subcontratação, a responsabilidade passa a ser de quem subcontratou o TAC ou o TAC Equiparado.
- **Transporte realizado por ETC não equiparada a TAC:** a responsabilidade pelo registro da operação é da própria ETC que efetivamente realizará o transporte.

### Como emitir o CIOT?

A forma de emissão depende da categoria do transportador:

- **Transporte realizado por TAC ou TAC Equiparado:** a operação deve ser registrada obrigatoriamente por meio de uma **Instituição de Pagamento (IP) homologada**.
- **Transporte realizado por ETC:** a emissão pode ocorrer de duas formas:

  - Diretamente, por meio da **integração com a API da ANTT**, desde que o veículo informado esteja vinculado à frota da ETC no RNTRC;
  - Por meio de uma **Instituição de Pagamento homologada**.

### Para quais operações a ETC pode emitir o CIOT diretamente?

A ETC pode emitir o CIOT diretamente via **integração com a API da ANTT** somente nas operações de transporte que ela própria irá realizar. O pré-requisito é que o **veículo automotor** informado na operação esteja vinculado à **frota da ETC no RNTRC**.

Veja abaixo as responsabilidades nos casos de subcontratação:

- **ETC subcontrata TAC ou TAC Equiparado:** a responsabilidade continua sendo da ETC contratante, mas o CIOT deve ser emitido por meio de uma Instituição de Pagamento homologada.
- **ETC subcontrata outra ETC:** a responsabilidade pelo registro passa a ser da ETC subcontratada, que efetivamente realizará o transporte.

### Como o CIOT é gerado para TAC e TAC Equiparado no SOP?

Para as categorias **TAC** e **TAC Equiparado**, a geração do CIOT ocorre **exclusivamente** por meio de uma **Instituição de Pagamento (IP) homologada**. O módulo **TMS** do Sankhya Log (SOP Logística) possui integração com as seguintes operadoras:

- Pamcard
- Repom
- PagBem
- Strada
- e-Frete
- Target
- FFCred

### Como o CIOT é gerado para ETC no SOP?

Para a categoria **ETC**, a geração do CIOT pode ocorrer de duas formas:

- Por meio de uma **Instituição de Pagamento (IP) homologada**, utilizando as mesmas operadoras disponíveis para TAC;
- Por meio da **integração direta com a ANTT** — esta opção ainda não está disponível no Sankhya Om; a **Lincros** já possui solução para esse fluxo.

Atenção: a maior parte das transportadoras está na categoria **ETC**. No entanto, quando há contratação de um **agregado**, a operação passa para a categoria **TAC Equiparado**, o que inviabiliza o uso da API da ANTT e exige a emissão via Instituição de Pagamento.

### É necessário atualizar o SOP para emitir o CIOT?

Sim. Para utilizar as adequações relacionadas às novas exigências da ANTT, é necessário atualizar o **SOP TMS** para a versão disponibilizada com as adequações. A atualização contempla todas as integrações com as operadoras homologadas e **não requer nenhuma configuração adicional**.

A versão atualizada inclui **6 novos campos** na tela **"Viagem"**, exigidos pela ANTT:

- **"Distância"**
- **"Produto Principal"**
- **"Tipo Operação CIOT"**
- **"Cálculo do Frete Mínimo"**
- **"Quantidade de Eixos"**
- **"Retorno Vazio"**

Esses campos foram incorporados à tela já conhecida pela equipe, **sem alteração na jornada de trabalho** dos usuários.

![Imagem 1: Esses campos foram incorporados à tela já conhecida pela equipe, sem alteração na jornada de trabalho dos usuários.](https://ajuda.sankhya.com.br/hc/article_attachments/40716012976663)
