---
id: "43529821213335"
titulo: "Como calcular a folha de autônomos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43529821213335-Como-calcular-a-folha-de-aut%C3%B4nomos"
trilha: "Manual do Produto > Pessoas+ > Contratos Especiais > Contrato Autônomo"
atualizado_em: "2026-10-02T15:22:04Z"
rotulos: ["ID: br.com.sankhya.rh.CalculoIndFolha", "FPCODEVEAUT", "FPCALAUTONOMOS", "Cálculo da folha de Autônomos", "FPRELATRPA"]
---

# Como calcular a folha de autônomos

**Módulo:**Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.rh.CalculoIndFolha

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A tela **Cálculos** permite realizar os cálculos de folha de pagamento, individuais ou coletivos, para todos os tipos de vínculo. Para autônomos, existe uma opção específica de cálculo de Recibo de Pagamento Autônomo (RPA), utilizada quando o profissional recebe honorários em mais de uma data dentro da mesma referência.

Depois de calculados os RPAs necessários, é feito o cálculo mensal, que consolida os valores pagos e apura os tributos (INSS, IRRF, ISS) de forma unificada para a referência.

### 2. Pré-requisitos

#### Permissões necessárias

- Possuir acesso à tela **Cálculos** e às demais telas utilizadas no processo.
- Parâmetro **Libera cálculo de autônomos - FPCALAUTONOMOS** habilitado na tela **Preferências** (Configurações > Avançado).
- Permissão **Realizar cálculos de autônomos** habilitada para o grupo do seu usuário.

  Para conferir, acesse o **Painel de Configurações**(Pessoal+ > Configurações).

  Vá até a seção **Configuração de Permissões** e selecione a tela **Cálculos**, em seguida, o grupo de acessos e usuários desejados e certifique-se de que a permissão**para Realizar cálculos de autônomos ou todos os tipos de cálculo** esteja habilitada para permitir o uso da tela.

  [GIF animado: Imagem 1: Vá até a seção Configuração de Permissões e selecione a tela Cálculos , em seguida, o grupo de acessos e usuários…](https://ajuda.sankhya.com.br/hc/article_attachments/43542636218263)

#### Configurações prévias

- Evento de honorário cadastrado com a identificação 200 - Outros Eventos Suplementares, para que apareça corretamente na folha RPA.

  Um exemplo é o evento padrão **RESTITUIÇÃO DESC INDEVIDO**, que não possui essa identificação por padrão, pois não é exclusivo para RPA.

  Nesse caso, é possível editar diretamente o evento na aba **Básico**, informando a **Identificação do Evento: 200 - Outros Eventos Suplementares**. Porém, preferencialmente, deve-se duplicar o evento e configurar a identificação **200** na nova cópia, deixando-o exclusivo para uso em folhas de RPA.

  | ℹ️ **Nota**  A partir da versão **5.109.8**, eventos com identificação **200 - Outros Eventos Suplementares** também são considerados no cálculo do evento **516 - Líquido Autônomos**, responsável por zerar o líquido na folha mensal do autônomo. Em versões anteriores, apenas eventos com identificação **119 - Eventos Honorários** eram considerados nesse cálculo. |
  | --- |
- Os códigos dos eventos correspondentes aos valores líquidos dos autônomos também devem estar configurados no parâmetro **Cód. Evento Folha de autonomo com líquido zerado - FPCODEVEAUT** para que o cálculo seja efetuado com base no acumulado desses eventos nas folhas.

### 3. Jornada de Uso

**🔹Calcular o RPA**

[GIF animado: Imagem 2: 🔹Calcular o RPA](https://ajuda.sankhya.com.br/hc/article_attachments/43533062172823)

1. Acesse a tela **Cálculos** (Pessoal+ > Rotinas Folha).
2. Selecione a opção **Autônomos**, o modo **Individual** ou **Coletivo** e o tipo de folha **RPA**.
3. Preencha os campos **Referência**, **Data de Pagamento**, **Empresa** e **Funcionário**.
4. Com os campos preenchidos, o botão **Honorários** é habilitado. Clique em **+ (Lançar Honorário)** para lançar o RPA: informe o **Código do Evento**, a **Sequência** (0 para o primeiro recibo da referência) e o **Valor**. Preencha **Observação**, se necessário.
5. Clique em **Confirmar**.

   | **⚠️** **Atenção**  Os códigos dos eventos correspondentes aos valores líquidos dos autônomos devem estar configurados no parâmetro **Cód. Evento Folha de autonomo com líquido zerado - FPCODEVEAUT**. Essa configuração permite que o cálculo seja realizado com base no acumulado desses eventos nas folhas. |
   | --- |

   Também é possível realizar o lançamento de **Honorários** por meio da tela **Lançamento de Movimentos**.

   📚 Para saber mais, acesse [**Lançamento de Movimento para Cálculo de Autônomo**](https://ajuda.sankhya.com.br/hc/pt-br/articles/25948428448535).
6. Clique na tela principal e depois em **Próximo**.
7. Clique em **Calcular** e confirme a folha.

**🔹Calcular outro RPA na mesma referência**

Após lançar o primeiro RPA, caso seja necessário lançar outro RPA para o mesmo autônomo e na mesma referência:

1. Retorne à tela **Cálculos**.
2. Lance o próximo evento e confirme.
3. Clique em **Próximo**.
4. Clique em **Calcular**.

**🔹Conferir as folhas RPA**

Com a folha calculada, confira os valores e se os dados estiverem corretos, clique em **Marcar como CONFERIDA**.

![Imagem 3: Com a folha calculada, confira os valores e se os dados estiverem corretos, clique em Marcar como CONFERIDA .](https://ajuda.sankhya.com.br/hc/article_attachments/43533605048343)

Se necessário, use a opção de **Excluir**.

Após a confirmação do cálculo das folhas RPA, acesse o **Gerenciador de Folhas**.

[GIF animado: Imagem 4: Após a confirmação do cálculo das folhas RPA, acesse o Gerenciador de Folhas .](https://ajuda.sankhya.com.br/hc/article_attachments/43533695903255)

1. Pesquise as folhas desejadas.
2. Clique no card **Suplementar**.
3. Selecione a aba **Folhas**.

Serão apresentadas as sequências dos cálculos realizados anteriormente.

Quando houver dois ou mais RPA na mesma referência, por exemplo, as folhas serão apresentadas em sequências diferentes:

- **Sequência 1:** primeira folha RPA;
- **Sequência 2:** segunda folha RPA.

**🔹Agrupar as folhas RPA na folha mensal**

Após calcular as folhas suplementares, é necessário realizar o agrupamento delas para possibilitar a transmissão das informações para o **eSocial**.

[GIF animado: Imagem 5: Após calcular as folhas suplementares, é necessário realizar o agrupamento delas para possibilitar a transmissão das…](https://ajuda.sankhya.com.br/hc/article_attachments/43533952802455)

Para isso:

1. Acesse a tela **Cálculos**.
2. Clique no botão **Autônomo**.
3. Selecione a opção **Mensal**.
4. Preencha **Referência**, **Data de Pagamento**, **Código da Empresa** e **Código do Funcionário**, clique em **Próximo** e depois em **Calcular**.
5. Realize as conferências necessárias e clique em **Confirmar Folha**.

| ℹ️ **Nota**  No cálculo mensal, o sistema apresenta o evento **516 - Líquido Autônomos**, que corresponde ao valor já pago ao autônomo.  Esse tratamento permite que o valor já pago nos RPAs seja considerado no cálculo mensal sem gerar duplicidade no resumo e na integração financeira.  Para que o líquido seja zerado corretamente, o evento de honorário utilizado deve possuir uma destas identificações:   - **119 - Eventos Honorários**; - **200 - Outros Eventos Suplementares**, considerada nesse cálculo a partir da versão **5.109.8**.   Se o evento estiver configurado com outra identificação, o líquido da folha mensal poderá não ser zerado como esperado. |
| --- |

**🔹Emitir holerite da folha RPA**

Após a conferência e confirmação da folha mensal dos RPAs, é possível emitir o holerite **individual** ou **coletivo**.

- **Emissão individual**

  [GIF animado: Imagem 6: Emissão individual](https://ajuda.sankhya.com.br/hc/article_attachments/43535495600919)

1. Na tela **Cálculos** (Pessoal+ > Rotinas Folha), expanda a opção **Documentos**.
2. Clique em **Holerite mensal**.
3. Escolha a forma de de emissão entre **Baixar**, **Imprimir** ou **Enviar por e-mail**, seguindo o fluxo padrão do sistema.

- **Emissão coletiva**

  [GIF animado: Imagem 7: Emissão coletiva](https://ajuda.sankhya.com.br/hc/article_attachments/43535794450583)

1. Na tela **Gerenciador de Folhas**, marque a opção **Ativa Seleção**, selecione os colaboradores desejados e utilize a opção **Emitir Holerite**.
2. Escolha a opção de emissão entre **Baixar** ou **Enviar por e-mail**, seguindo o fluxo padrão do sistema.

   O sistema gera o recibo utilizando:

   - o relatório configurado no parâmetro **Recibo a Autônomos - FPRELATRPA**, quando informado;
   - ou o modelo padrão utilizado para a folha de autônomo, caso o parâmetro não esteja configurado.

**🔹Envio da folha RPA ao eSocial**

Após o cálculo da folha mensal dos autônomos, **não é necessário realizar um processo específico para liberar os valores da folha para o eSocial**.

O processo ocorre da mesma forma que nas demais folhas: após o cálculo pela tela **Gerenciador de Folhas**, [libere a folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247-Gerenciador-de-Folhas#h_01KQN3XPDJ4KAYEW7VWMBHPXCZ) para que os dados fiquem disponíveis para os procedimentos realizados posteriormente pela Central do eSocial.

####

####

### 4. Pontos de Atenção

- Eventos diversos usados no RPA (além dos eventos padrão já preparados para isso) precisam estar com a identificação **200 - Outros Eventos Suplementares** para aparecer corretamente na folha. Prefira duplicar o evento padrão e configurar a cópia com essa identificação, mantendo-a exclusiva para uso em RPA.
- A partir da versão 5.109.8, eventos com identificação 200 também passam a ser considerados no cálculo do evento 516 - Líquido Autônomos, responsável por zerar o líquido na folha mensal. Em versões anteriores, apenas eventos com identificação 119 - Eventos Honorários eram considerados nesse cálculo.
- Os eventos S-1200 e S-1210 enviados até o dia 15 do mês têm seus dados coletados a partir das 23h do dia 16. Os dados são contabilizados por CPF, um colaborador com folhas de férias, adiantamento e mensal na mesma referência é contabilizado uma única vez.
- A data de pagamento informada no cálculo mensal deve estar dentro da referência em que os RPAs foram pagos, pois o eSocial usa essa data como referência de leitura.

### 5. Dicas de Usabilidade

- Prefira duplicar eventos padrão em vez de alterar a identificação de um evento já em uso por outras rotinas.
- Para lançar mais de um RPA na mesma referência, realize o cálculo de cada recibo separadamente e utilize sequências diferentes.
- Ative o Log completo durante o cálculo para conferir a memória de cálculo, caso precise investigar algum valor.
- Utilize a tela **Gerenciador de Folhas** para conferir os valores pagos e descontados antes de confirmar a folha.
- Para lançamentos de honorários, além da rotina de RPA, também é possível utilizar a tela **Lançamento de Movimentos**.

## Perguntas Frequentes (FAQ)

**1. Por que a opção de calcular Autônomo (RPA) não aparece na tela Cálculos?**

Verifique se o parâmetro **Libera cálculo de autônomos - FPCALAUTONOMOS** está ligado e se a permissão **Realizar cálculos de autônomos** está habilitada para o seu grupo de usuário.

**2. Como lançar mais de um RPA para o mesmo autônomo na mesma referência?**

Realize o cálculo de cada RPA pela opção **Autônomos → Individual → RPA**. Para o primeiro recibo, utilize a sequência **0**. Para lançar outro RPA na mesma referência, retorne à tela **Cálculos**, clique em **Próximo** e depois em **Calcular**. Os RPA serão apresentados em sequências diferentes no **Gerenciador de Folhas**.

**3. Por que um evento não aparece corretamente na folha de pagamento RPA?**

Verifique se o evento está configurado com a identificação **200 - Outros Eventos Suplementares**. Essa identificação permite que eventos diversos sejam considerados corretamente na folha de pagamento RPA.

**4. Por que o líquido da folha mensal do autônomo não está sendo zerado?**

Confirme a identificação do evento de honorário utilizado (119 - Eventos Honorários ou 200 - Outros Eventos Suplementares, esta última considerada a partir da versão 5.109.8) e se os códigos dos eventos de líquido estão configurados no parâmetro FPCODEVEAUT.

**5. Como configurar o ISS do autônomo para calcular automaticamente no RPA?**

Veja o artigo [Como configurar o cálculo de ISS para autônomos no RPA](https://ajuda.sankhya.com.br/hc/pt-br/articles/39267510149527).

## Artigos Relacionados

- [Lançamento de Movimento para Cálculo de Autônomo](https://ajuda.sankhya.com.br/hc/pt-br/articles/25948428448535)
- [Como configurar o cálculo de ISS para autônomos no RPA](https://ajuda.sankhya.com.br/hc/pt-br/articles/39267510149527)
